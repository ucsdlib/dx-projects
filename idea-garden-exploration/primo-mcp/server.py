from mcp.server import MCPServer

mcp = MCPServer("Library Research Toolkit")

FAKE_BOOKS = [
    {"title": "Information Literacy in the Wild", "author": "R. Okafor", "year": 2021},
    {"title": "Cataloguing for Beginners", "author": "M. Lindqvist", "year": 2019},
    {"title": "The Quiet Archive", "author": "S. Patel", "year": 2023},
]

@mcp.tool()
def search_books(keyword: str) -> list[dict]:
    """Search the (pretend) library catalogue for books whose title contains a keyword."""
    keyword = keyword.lower()
    return [book for book in FAKE_BOOKS if keyword in book["title"].lower()]

if __name__ == '__main__':
    mcp.run()