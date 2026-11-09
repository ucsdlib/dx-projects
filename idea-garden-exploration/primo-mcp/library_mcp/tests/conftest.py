import pytest


@pytest.fixture
def anyio_backend():
    """Run async tests with asyncio (the anyio plugin comes with the MCP SDK)."""
    return "asyncio"


@pytest.fixture
def primo_env(monkeypatch):
    """Fake settings so tests never touch your real .env values or real Primo."""
    monkeypatch.setenv("PRIMO_BASE_URL", "https://primo.test")
    monkeypatch.setenv("PRIMO_API_KEY", "test-key")
    monkeypatch.setenv("PRIMO_VID", "TEST:VIEW")
    monkeypatch.setenv("PRIMO_TAB", "Everything")
    monkeypatch.setenv("PRIMO_SCOPE", "MyInst_and_CI")
    monkeypatch.setenv("PRIMO_DISCOVERY_URL", "https://discovery.test")
