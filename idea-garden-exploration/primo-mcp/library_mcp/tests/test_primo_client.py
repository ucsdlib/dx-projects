import asyncio
import json
from pathlib import Path

import httpx2
import pytest

from library_mcp import primo_client

SAMPLE = json.loads(Path("mock_primo/sample_search.json").read_text(encoding="utf-8"))


@pytest.mark.anyio
async def test_search_builds_records_and_sends_key_in_header(primo_env):
    seen = {}

    def handler(request: httpx2.Request) -> httpx2.Response:
        seen["auth"] = request.headers.get("Authorization")
        seen["q"] = request.url.params.get("q")
        return httpx2.Response(200, json=SAMPLE)

    result = await primo_client.search_catalogue(
        "water, rights", 3, transport=httpx2.MockTransport(handler)
    )

    assert seen["auth"] == "apikey test-key"
    assert seen["q"] == "any,contains,water rights"
    assert result.total_found == 3
    assert result.records[0].link.startswith("https://discovery.test/discovery/fulldisplay")


@pytest.mark.anyio
async def test_daily_quota_gives_friendly_message(primo_env):
    def handler(request):
        return httpx2.Response(429, text="<errorCode>DAILY_THRESHOLD</errorCode>")

    with pytest.raises(primo_client.PrimoError, match="midnight GMT"):
        await primo_client.search_catalogue("water", 3, transport=httpx2.MockTransport(handler))


@pytest.fixture
def counting_primo(primo_env, monkeypatch):
    """Replace the HTTP call with a counter; start each test with empty cache state."""
    primo_client._CACHE.clear()
    primo_client._INFLIGHT.clear()
    state = {"calls": 0, "fail": False}

    async def fake_raw(query, limit, transport=None):
        state["calls"] += 1
        await asyncio.sleep(0.01)  # yield so concurrent callers overlap
        if state["fail"]:
            raise primo_client.PrimoError("boom")
        return SAMPLE

    monkeypatch.setattr(primo_client, "search_primo_raw", fake_raw)
    yield state
    primo_client._CACHE.clear()
    primo_client._INFLIGHT.clear()


@pytest.mark.anyio
async def test_repeat_search_is_served_from_cache(counting_primo):
    first = await primo_client.search_catalogue("Water", 3)
    second = await primo_client.search_catalogue(" water ", 3)
    assert counting_primo["calls"] == 1
    assert first is second


@pytest.mark.anyio
async def test_cache_is_bounded_and_prunes_expired(counting_primo, monkeypatch):
    monkeypatch.setattr(primo_client, "MAX_ENTRIES", 3)
    for i in range(6):
        await primo_client.search_catalogue(f"query {i}", 3)
    assert len(primo_client._CACHE) <= 3
    assert ("query 5", 3) in primo_client._CACHE  # newest kept
    assert ("query 0", 3) not in primo_client._CACHE  # oldest evicted

    monkeypatch.setattr(primo_client, "CACHE_SECONDS", -1)  # next entry is born expired
    await primo_client.search_catalogue("stale one", 3)
    monkeypatch.setattr(primo_client, "CACHE_SECONDS", 300)
    await primo_client.search_catalogue("fresh one", 3)
    assert ("stale one", 3) not in primo_client._CACHE


@pytest.mark.anyio
async def test_concurrent_identical_searches_make_one_call(counting_primo):
    results = await asyncio.gather(*[primo_client.search_catalogue("water", 3) for _ in range(5)])
    assert counting_primo["calls"] == 1
    assert all(r is results[0] for r in results)
    assert primo_client._INFLIGHT == {}


@pytest.mark.anyio
async def test_failure_reaches_all_waiters_and_is_not_cached(counting_primo):
    counting_primo["fail"] = True
    outcomes = await asyncio.gather(
        *[primo_client.search_catalogue("water", 3) for _ in range(3)], return_exceptions=True
    )
    assert all(isinstance(o, primo_client.PrimoError) for o in outcomes)
    assert counting_primo["calls"] == 1
    assert primo_client._CACHE == {} and primo_client._INFLIGHT == {}

    counting_primo["fail"] = False
    await primo_client.search_catalogue("water", 3)  # retries Primo
    assert counting_primo["calls"] == 2


def test_injection_text_is_not_passed_on():
    record = primo_client.to_record(SAMPLE["docs"][2])
    assert "IGNORE" not in record.model_dump_json()
