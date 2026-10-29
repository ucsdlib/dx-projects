import httpx2 

from library_mcp.config import get_settings


def search_primo_raw(query: str, limit: int = 5) -> dict:
    """Send one search to Primo (or the mock) and return the raw JSON."""
    s = get_settings()
    params = {
        "vid": s.primo_vid,
        "tab": s.primo_tab,
        "scope": s.primo_scope,
        "q": f"any,contains,{query}",
        "limit": limit,
        "offset": 0,
    }
    headers = {"Authorization": f"apikey {s.primo_api_key}", "Accept": "application/json"}
    response = httpx2.get(f"{s.primo_base_url}/primo/v1/search",
params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

def first(section: dict, field: str) -> str | None:
    """PNX stores every value as a list; return the first item or None."""
    values = section.get(field) or []
    return values[0] if values else None


def search_catalogue_simple(query: str, limit: int = 5) -> list[dict]:
    data = search_primo_raw(query, limit)
    results = []
    for doc in data.get("docs", []):
        display = doc.get("pnx", {}).get("display", {})
        results.append({
            "title": first(display, "title"),
            "creator": first(display, "creator"),
            "date": first(display, "creationdate"),
            "type": first(display, "type"),
        })
    return results