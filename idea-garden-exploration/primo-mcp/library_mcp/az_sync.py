import httpx2

from library_mcp import databases_db
from library_mcp.libguides_client import LibGuidesError, fetch_az_databases
from library_mcp.models import DatabaseRecord
from library_mcp.safety import plain_text


def _flag(value) -> bool:
    return str(value).lower() in ("1", "true")


def _names(items) -> list[str]:
    found = [plain_text(i.get("name", ""), 80) for i in (items or []) if isinstance(i, dict)]
    return [n for n in found if n][:10]


def to_database(raw: dict) -> DatabaseRecord | None:
    """Read ONLY the keys named here. Anything else in the reply is ignored."""
    if _flag(raw.get("enable_hidden", 0)):
        return None
    name = plain_text(raw.get("name") or "", 200)
    url = raw.get("url") or ""
    if not str(raw.get("id", "")).isdigit() or not name or not url.startswith("https://"):
        return None
    alt = [a.strip() for a in plain_text(raw.get("alt_names") or "", 300).split(",") if a.strip()]
    return DatabaseRecord(
        database_id=int(raw["id"]),
        name=name,
        description=plain_text(raw.get("description") or "", 500),
        url=url,
        proxied=_flag(raw.get("enable_proxy", 0)),
        vendor=plain_text(raw.get("vendor") or "", 100) or None,  # field name unconfirmed; harmless if absent
        alt_names=alt[:10],
        subjects=_names(raw.get("subjects")),
        types=_names(raw.get("az_types")),
    )


async def sync(con, transport: httpx2.AsyncBaseTransport | None = None) -> int:
    raw = await fetch_az_databases(transport)
    records = [r for r in (to_database(item) for item in raw) if r is not None]
    old = databases_db.count(con)
    if not records:
        raise LibGuidesError("LibGuides returned no usable databases; keeping the existing list.")
    if old and len(records) < old * 0.5:
        raise LibGuidesError(
            f"The new list ({len(records)}) is under half the old one ({old}); keeping the old list.")
    databases_db.replace_all(con, records)
    return len(records)