from mcp.server import MCPServer
from library_mcp.config import get_settings
from library_mcp.fake_catalogue import FAKE_BOOKS

settings = get_settings()
mcp = MCPServer(settings.server_name)

@mcp.tool()
def search_books(keyword: str) -> list[dict]:
    """Search the (pretend) library catalogue for books whose title contains a keyword."""
    keyword = keyword.lower()
    return [book for book in FAKE_BOOKS if keyword in book["title"].lower()][: settings.max_results]

if __name__ == '__main__':
    mcp.run()