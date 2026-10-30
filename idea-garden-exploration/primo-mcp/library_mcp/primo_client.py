import httpx2 

from library_mcp.config import get_settings


async def search_primo_raw(query: str, limit: int = 5,transport: httpx2.AsyncBaseTransport | None = None) -> dict:
    """Send one search to Primo (or the mock) and return the raw JSON."""
    s = get_settings()
    params = {"vid": s.primo_vid, 
            "tab": s.primo_tab, 
            "scope": s.primo_scope,
            "q": f"any,contains,{query}", 
            "limit": limit, "offset": 0}
    headers = {"Authorization": f"apikey {s.primo_api_key}", "Accept": "application/json"}
    async with httpx2.AsyncClient(transport=transport, timeout=10) as client:
        response = await client.get(f"{s.primo_base_url}/primo/v1/search",params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def first(section: dict, field: str) -> str | None:
    """PNX stores every value as a list; return the first item or None."""
    values = section.get(field) or []
    return values[0] if values else None


async def search_catalogue_simple(query: str, limit: int = 5) -> list[dict]:
    data = await search_primo_raw(query, limit)
    return [
        {"title": first(d["pnx"]["display"], "title"),
        "creator": first(d["pnx"]["display"], "creator")}
        for d in data.get("docs", [])
    ]