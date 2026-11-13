import time

import httpx2

from library_mcp.config import get_settings


class LibGuidesError(Exception):
    """A problem talking to LibGuides, with a message safe to show people."""


_token: tuple[str, float] | None = None

async def _get_token(client: httpx2.AsyncClient) -> str:
    global _token
    if _token and _token[1] > time.monotonic() + 60:
        return _token[0]
    s = get_settings()
    response = await client.post(
        f"{s.libguides_api_base}/1.2/oauth/token",
        data={"client_id": s.libguides_client_id,
            "client_secret": s.libguides_client_secret,
            "grant_type": "client_credentials"},
    )
    if response.status_code != 200:
        raise LibGuidesError("LibGuides rejected the API credentials. Check the app in LibApps.")
    body = response.json()
    _token = (body["access_token"], time.monotonic() + int(body.get("expires_in", 3600)))
    return _token[0]


async def fetch_az_databases(transport: httpx2.AsyncBaseTransport | None = None) -> list[dict]:
    """Fetch the raw A-Z list. Callers must filter it (see az_sync.to_database)."""
    s = get_settings()
    try:
        async with httpx2.AsyncClient(transport=transport, timeout=30) as client:
            token = await _get_token(client)
            response = await client.get(
                f"{s.libguides_api_base}/1.2/az",
                params={"expand": "az_types,subjects"},  # check the options on your Endpoints 1.2 page
                headers={"Authorization": f"Bearer{token}"},
            )
    except httpx2.TimeoutException as err:
        raise LibGuidesError("LibGuides took too long to answer.") from err
    except httpx2.HTTPError as err:
        raise LibGuidesError("Could not reach LibGuides. Check LIBGUIDES_API_BASE.") from err
    if response.status_code in (401, 403):
        raise LibGuidesError("LibGuides refused the request. Check the app's scopes.")
    if response.status_code == 429:
        raise LibGuidesError("LibGuides asked us to slow down. Try again later.")
    if response.status_code != 200:
        raise LibGuidesError(f"Unexpected reply from LibGuides (HTTP{response.status_code}).")
    data = response.json()
    if not isinstance(data, list):
        raise LibGuidesError("LibGuides sent an unexpected reply shape.")
    return data