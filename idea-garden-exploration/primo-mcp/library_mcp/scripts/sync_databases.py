import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from library_mcp import az_sync, databases_db
from library_mcp.libguides_client import LibGuidesError


async def main() -> int:
    con = databases_db.connect()
    try:
        count = await az_sync.sync(con)
        print(f"Synced{count} databases. Last synced:{databases_db.last_synced(con)}")
        return 0
    except LibGuidesError as err:
        print(f"Sync failed, keeping the old list:{err}", file=sys.stderr)
        return 1
    finally:
        con.close()


sys.exit(asyncio.run(main()))