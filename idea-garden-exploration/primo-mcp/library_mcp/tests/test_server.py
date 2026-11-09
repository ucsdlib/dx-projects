import pytest
from mcp import Client

import server
from library_mcp import primo_client
from library_mcp.models import Record, SearchResult


@pytest.mark.anyio
async def test_tool_is_listed():
    async with Client(server.mcp) as client:
        listing = await client.list_tools()
    assert "search_catalogue" in [t.name for t in listing.tools]


@pytest.mark.anyio
async def test_tool_returns_structured_result(monkeypatch):
    async def fake_search(query, limit, transport=None):
        return SearchResult(
            query=query, total_found=1, records=[Record(title="Test title", record_id="alma1")]
        )

    monkeypatch.setattr(primo_client, "search_catalogue", fake_search)
    async with Client(server.mcp) as client:
        result = await client.call_tool("search_catalogue", {"query": "water", "limit": 2})
    assert result.structured_content["records"][0]["title"] == "Test title"


@pytest.mark.anyio
async def test_primo_error_becomes_tool_error(monkeypatch):
    async def broken(query, limit, transport=None):
        raise primo_client.PrimoError("Primo is having problems right now.")

    monkeypatch.setattr(primo_client, "search_catalogue", broken)
    async with Client(server.mcp) as client:
        result = await client.call_tool("search_catalogue", {"query": "water"})
    assert result.is_error
