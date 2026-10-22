#!/usr/bin/env python3
"""Validate the minimum structure of an annotated-bibliography run manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_TOP_LEVEL = {
    "schema_version",
    "run_id",
    "created_at",
    "working_question",
    "breadth_tier",
    "output_mode",
    "queries",
    "sources",
    "themes",
    "questions",
    "selected_paths",
    "limitations",
    "stage_log",
    "reference_log",
}

REQUIRED_STAGES = {"intake", "landscape", "selection"}
REQUIRED_REFERENCE_BASENAMES = {
    "interaction-model.md",
    "response-templates.md",
    "search-and-selection.md",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()

    with args.manifest.open(encoding="utf-8") as file:
        manifest = json.load(file)

    missing = sorted(REQUIRED_TOP_LEVEL - set(manifest))
    if missing:
        raise SystemExit(f"Missing manifest fields: {', '.join(missing)}")

    stages = {event.get("stage") for event in manifest.get("stage_log", [])}
    missing_stages = sorted(REQUIRED_STAGES - stages)
    if missing_stages:
        raise SystemExit(f"Missing stage_log entries: {', '.join(missing_stages)}")

    references = {
        Path(event.get("reference", "")).name
        for event in manifest.get("reference_log", [])
    }
    missing_references = sorted(REQUIRED_REFERENCE_BASENAMES - references)
    if missing_references:
        raise SystemExit(f"Missing reference_log entries: {', '.join(missing_references)}")

    for source in manifest.get("sources", []):
        if not source.get("source_id"):
            raise SystemExit("Every source record must have a source_id")

    for theme in manifest.get("themes", []):
        if not theme.get("source_ids"):
            raise SystemExit(f"Theme {theme.get('theme_id', '?')} must have source_ids")

    for question in manifest.get("questions", []):
        if not question.get("source_ids"):
            raise SystemExit(f"Question {question.get('question_id', '?')} must have source_ids")

    print("Manifest valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
