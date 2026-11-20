import json
from pathlib import Path

import httpx2
import pytest
from mcp import Client

import server
from library_mcp import az_sync, databases_db, libguides_client

SAMPLE = json.loads(Path("mock_libguides/sample_az.json").read_text(encoding="utf-8"))


@pytest.fixture
def libguides_env(monkeypatch):
    monkeypatch.setenv("LIBGUIDES_API_BASE", "https://lg.test")
    monkeypatch.setenv("LIBGUIDES_CLIENT_ID", "id")
    monkeypatch.setenv("LIBGUIDES_CLIENT_SECRET", "secret")
    monkeypatch.setattr(libguides_client, "_token", None)

def fake_libguides(items):
    def handler(request: httpx2.Request) -> httpx2.Response:
        if request.url.path == "/1.2/oauth/token":
            return httpx2.Response(200, json={"access_token": "t", "expires_in": 3600})
        assert request.headers["Authorization"] == "Bearer t"
        return httpx2.Response(200, json=items)
    return httpx2.MockTransport(handler)


def test_mapping_drops_hidden_records_and_private_fields():
    records = [r for r in (az_sync.to_database(x) for x in SAMPLE) if r]
    assert "Hidden Test Database" not in [r.name for r in records]
    dump = " ".join(r.model_dump_json() for r in records).lower()
    assert "password" not in dump and "do not share" not in dump
    assert "<p>" not in dump 


@pytest.mark.anyio
async def test_sync_then_search_finds_alternate_names(libguides_env, tmp_path):
    con = databases_db.connect(tmp_path / "t.db")
    assert await az_sync.sync(con, transport=fake_libguides(SAMPLE)) == 3
    found = databases_db.search(con, "journal storage")
    assert found and found[0].name == "JSTOR"
    assert databases_db.last_synced(con)


@pytest.mark.anyio
async def test_an_empty_reply_keeps_the_old_list(libguides_env, tmp_path):
    con = databases_db.connect(tmp_path / "t.db")
    await az_sync.sync(con, transport=fake_libguides(SAMPLE))
    before = databases_db.count(con)
    with pytest.raises(libguides_client.LibGuidesError):
        await az_sync.sync(con, transport=fake_libguides([]))
    assert databases_db.count(con) == before


@pytest.mark.anyio
async def test_tool_answers_from_the_local_copy(libguides_env, tmp_path, monkeypatch):
    path = tmp_path / "t.db"
    con = databases_db.connect(path)
    await az_sync.sync(con, transport=fake_libguides(SAMPLE))
    con.close()
    real_connect = databases_db.connect
    monkeypatch.setattr(databases_db, "connect", lambda: real_connect(path))
    async with Client(server.mcp) as client:
        result = await client.call_tool("search_databases", {"query": "nursing"})
    text = json.dumps(result.structured_content)
    assert "CINAHL Complete" in text and "last_synced" in text
    assert "DO NOT SHARE" not in text