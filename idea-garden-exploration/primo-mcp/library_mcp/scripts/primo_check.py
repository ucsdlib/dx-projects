import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from library_mcp.primo_client import search_catalogue


async def main() -> None:
    result = await search_catalogue("climate adaptation", limit=3)
    print("Total found:", result.total_found)
    for r in result.records:
        print("-", r.title, "|", r.record_id, "|", r.link)


asyncio.run(main())
