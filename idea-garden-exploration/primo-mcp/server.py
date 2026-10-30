from mcp.server import MCPServer
from library_mcp.config import get_settings
from library_mcp.fake_catalogue import FAKE_BOOKS
from library_mcp.primo_client import search_catalogue_simple

settings = get_settings()
mcp = MCPServer(settings.server_name)

@mcp.tool()
def search_books(keyword: str) -> list[dict]:
    """Search the (pretend) library catalogue for books whose title contains a keyword."""
    keyword = keyword.lower()
    return [book for book in FAKE_BOOKS if keyword in book["title"].lower()][: settings.max_results]
@mcp.tool()
async def search_catalogue(query: str, limit: int = 5) -> list[dict]:
    """Search the library catalogue (Primo) and return brief records."""
    return await search_catalogue_simple(query, min(limit, settings.max_results))

if __name__ == '__main__':
    mcp.run()