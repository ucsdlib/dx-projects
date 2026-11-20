import asyncio
import logging

import httpx2

from library_mcp.config import get_settings
from library_mcp.models import Record, SearchResult
from library_mcp.safety import clean_query, tidy
import time

_CACHE: dict[tuple[str, int], tuple[float, SearchResult]] = {}
_INFLIGHT: dict[tuple[str, int], asyncio.Task[SearchResult]] = {}
CACHE_SECONDS = 300
MAX_ENTRIES = 256

log = logging.getLogger(__name__)


class PrimoError(Exception):
    """A problem talking to Primo, with a message safe to show people."""


def first(section: dict, field: str) -> str | None:
    values = section.get(field) or []
    return values[0] if values else None


def explain_status(status: int, body: str) -> str:
    if status in (401, 403):
        return "Primo rejected the API key. Check PRIMO_API_KEY and its Primo permissions."
    if status == 429 and "DAILY_THRESHOLD" in body:
        return "Today's Primo API allowance is used up. It resets at midnight GMT."
    if status == 429:
        return "Too many requests to Primo at once. Please wait a moment and retry."
    if status == 400:
        return "Primo did not accept the search. Check PRIMO_VID, PRIMO_TAB and PRIMO_SCOPE."
    if status >= 500:
        return "Primo is having problems right now. Please try again later."
    return f"Unexpected reply from Primo (HTTP{status})."


async def search_primo_raw(
    query: str, limit: int, transport: httpx2.AsyncBaseTransport | None = None
) -> dict:
    s = get_settings()
    params = {
        "vid": s.primo_vid,
        "tab": s.primo_tab,
        "scope": s.primo_scope,
        "q": f"any,contains,{query}",
        "limit": limit,
        "offset": 0,
        "lang": "eng",
        "skipDelivery": "true",
        "pcAvailability": "true",
    }
    headers = {"Authorization": f"apikey {s.primo_api_key}", "Accept": "application/json"}
    try:
        async with httpx2.AsyncClient(transport=transport, timeout=20) as client:
            response = await client.get(f"{s.primo_base_url}", params=params, headers=headers)
    except httpx2.TimeoutException as err:
        raise PrimoError("Primo took too long to answer. Please try again.") from err
    except httpx2.HTTPError as err:
        raise PrimoError("Could not reach Primo. Check PRIMO_BASE_URL.") from err
    if response.status_code != 200:
        raise PrimoError(explain_status(response.status_code, response.text))
    remaining = response.headers.get("X-Exl-Api-Remaining")
    if remaining is not None and int(remaining) <= 5:
        raise PrimoError("The library's daily Primo allowance is nearly used up; pausing searches.")
    return response.json()


def to_record(doc: dict) -> Record:
    s = get_settings()
    pnx = doc.get("pnx", {})
    display = pnx.get("display", {})
    record_id = first(pnx.get("control", {}), "recordid") or "unknown"
    context = doc.get("context", "L")
    link = None
    if s.primo_discovery_url:
        link = (
            f"{s.primo_discovery_url}/discovery/fulldisplay"
            f"?docid={record_id}&context={context}&vid={s.primo_vid}"
        )
    return Record(
        title=tidy(first(display, "title")) or "(no title)",
        creators=[name for c in display.get("creator", [])[:5] if (name := tidy(c))],
        date=tidy(first(display, "creationdate")),
        resource_type=tidy(first(display, "type")),
        record_id=record_id,
        link=link,
    )


def _store(key: tuple[str, int], result: SearchResult) -> None:
    """Write to the cache, first pruning expired entries and capping total size."""
    now = time.monotonic()
    for k in [k for k, (expires, _) in _CACHE.items() if expires <= now]:
        del _CACHE[k]
    while len(_CACHE) >= MAX_ENTRIES:
        del _CACHE[next(iter(_CACHE))]  # oldest inserted
    _CACHE[key] = (now + CACHE_SECONDS, result)


async def _fetch(
    cleaned: str, limit: int, transport: httpx2.AsyncBaseTransport | None
) -> SearchResult:
    data = await search_primo_raw(cleaned, limit, transport)
    records = [to_record(d) for d in data.get("docs", [])]
    log.info("primo search ok: query_chars=%d results=%d", len(cleaned), len(records))
    return SearchResult(
        query=cleaned, total_found=data.get("info", {}).get("total", 0), records=records
    )


async def search_catalogue(
    query: str, limit: int, transport: httpx2.AsyncBaseTransport | None = None
) -> SearchResult:
    cleaned = clean_query(query)
    if transport is not None:
        return await _fetch(cleaned, limit, transport)

    key = (cleaned.lower(), limit)
    hit = _CACHE.get(key)
    if hit and hit[0] > time.monotonic():
        return hit[1]

    task = _INFLIGHT.get(key)
    if task is None:
        task = asyncio.create_task(_fetch(cleaned, limit, None))
        _INFLIGHT[key] = task

        def _finish(t: asyncio.Task) -> None:
            _INFLIGHT.pop(key, None)
            if not t.cancelled() and t.exception() is None:
                _store(key, t.result())

        task.add_done_callback(_finish)

    return await asyncio.shield(task)
