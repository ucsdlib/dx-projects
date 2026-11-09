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


def test_injection_text_is_not_passed_on():
    record = primo_client.to_record(SAMPLE["docs"][2])
    assert "IGNORE" not in record.model_dump_json()
