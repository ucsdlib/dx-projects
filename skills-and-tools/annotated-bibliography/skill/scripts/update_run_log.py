#!/usr/bin/env python3
"""Create or update an annotated-bibliography run manifest."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_manifest(path: Path, run_id: str) -> dict:
    if path.exists():
        with path.open(encoding="utf-8") as file:
            manifest = json.load(file)
    else:
        manifest = {
            "schema_version": "0.1",
            "run_id": run_id,
            "created_at": utc_now(),
            "working_question": "",
            "context": {},
            "breadth_tier": "",
            "output_mode": "",
            "queries": [],
            "sources": [],
            "themes": [],
            "questions": [],
            "selected_paths": [],
            "limitations": [],
            "stage_log": [],
            "reference_log": [],
        }
        path.parent.mkdir(parents=True, exist_ok=True)

    manifest.setdefault("stage_log", [])
    manifest.setdefault("reference_log", [])
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--run-id", default="")
    parser.add_argument("--kind", required=True, choices=("stage", "reference"))
    parser.add_argument("--stage", help="Stage name for a stage event.")
    parser.add_argument("--status", help="Stage status, such as started or completed.")
    parser.add_argument("--reference", help="Reference path for a reference event.")
    parser.add_argument("--purpose", help="Why the reference was consulted.")
    parser.add_argument("--evidence", help="Rule, template, or API recipe used from the reference.")
    parser.add_argument("--note", default="", help="Additional event detail.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_id = args.run_id or args.manifest.parent.name
    manifest = load_manifest(args.manifest, run_id)
    manifest["updated_at"] = utc_now()

    event = {"timestamp": utc_now(), "note": args.note}
    if args.kind == "stage":
        if not args.stage:
            raise SystemExit("--stage is required for a stage event")
        event.update({"stage": args.stage, "status": args.status or "completed"})
        manifest["stage_log"].append(event)
    else:
        if not args.reference:
            raise SystemExit("--reference is required for a reference event")
        event.update(
            {
                "reference": args.reference,
                "purpose": args.purpose or "",
                "evidence": args.evidence or "",
            }
        )
        manifest["reference_log"].append(event)

    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    with args.manifest.open("w", encoding="utf-8") as file:
        json.dump(manifest, file, indent=2, ensure_ascii=False)
        file.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
