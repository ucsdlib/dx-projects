import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from library_mcp.models import DatabaseRecord

DB = Path(__file__).resolve().parent.parent / "data" / "databases.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS databases (database_id INTEGER PRIMARY KEY, name TEXT NOT  NULL,record_json TEXT NOT NULL);
CREATE VIRTUAL TABLE IF NOT EXISTS databases_fts USING fts5(name, alt_names, description, subjects, types);
CREATE TABLE IF NOT EXISTS sync_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
"""


def connect(path: Path | str = DB) -> sqlite3.Connection:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def replace_all(con: sqlite3.Connection, records: list[DatabaseRecord]) -> None:
    """Swap in the whole list in ONE transaction: all or nothing."""
    with con:
        con.execute("DELETE FROM databases")
        con.execute("DELETE FROM databases_fts")
        for r in records:
            con.execute("INSERT INTO databases(database_id, name, record_json) VALUES (?, ?, ?)",
                        (r.database_id, r.name, r.model_dump_json()))
            con.execute(
                "INSERT INTO databases_fts(rowid, name, alt_names, description, subjects, types) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (r.database_id, r.name, " ".join(r.alt_names), r.description," ".join(r.subjects), " ".join(r.types)))
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        con.execute("INSERT OR REPLACE INTO sync_meta(key, value) VALUES ('last_synced', ?)", (stamp,))


def count(con: sqlite3.Connection) -> int:
    return con.execute("SELECT COUNT(*) FROM databases").fetchone()[0]


def last_synced(con: sqlite3.Connection) -> str | None:
    row = con.execute("SELECT value FROM sync_meta WHERE key = 'last_synced'").fetchone()
    return row[0] if row else None


def search(con: sqlite3.Connection, text: str, limit: int = 5) -> list[DatabaseRecord]:
    words = [w.replace('"', "") for w in text.split()][:10]  # quote words: plain text, not syntax
    if not words:
        return []
    match = " OR ".join(f'"{w}"' for w in words)
    rows = con.execute(
        "SELECT databases.record_json FROM databases_fts "
        "JOIN databases ON databases.database_id = databases_fts.rowid "
        "WHERE databases_fts MATCH ? "
        "ORDER BY bm25(databases_fts, 10.0, 5.0, 1.0, 2.0, 2.0) LIMIT ?",
        (match, limit),
    ).fetchall()
    return [DatabaseRecord.model_validate_json(r["record_json"]) for r in rows]


def get(con: sqlite3.Connection, database_id: int) -> DatabaseRecord | None:
    row = con.execute("SELECT record_json FROM databases WHERE database_id = ?",(database_id,)).fetchone()
    return DatabaseRecord.model_validate_json(row["record_json"]) if row else None