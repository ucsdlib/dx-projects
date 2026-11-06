#!/usr/bin/env python3
"""Normalize visible Springshare A-Z assets into compact JSON and CSV."""

import argparse
import csv
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSV_FIELDS = [
    "id",
    "name",
    "description",
    "more_info",
    "url",
    "friendly_url",
    "vendor",
    "types",
    "subjects",
    "featured_subjects",
    "access_notes",
    "alt_names",
    "created",
    "updated",
    "hidden",
]


def plain_text(value):
    """Convert Springshare HTML strings into normalized plain text."""
    if not value:
        return ""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", value))).strip()


def optional_text(value):
    value = plain_text(value)
    return value or None


def unique_values(values):
    seen = set()
    output = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            output.append(value)
    return output


def normalize_asset(asset):
    subjects = []
    featured_subjects = []
    for subject in asset.get("subjects", []):
        name = plain_text(subject.get("name"))
        if not name:
            continue
        subjects.append(name)
        try:
            rank = int(float(subject.get("featured", 0)))
        except (TypeError, ValueError):
            rank = 0
        if rank > 0:
            featured_subjects.append({"name": name, "rank": rank})

    types = [plain_text(item.get("name")) for item in asset.get("az_types", [])]
    access_notes = [plain_text(item.get("name")) for item in asset.get("az_flags", [])]
    alt_names = plain_text(asset.get("alt_names")).split(",")

    return {
        "id": str(asset.get("id") or ""),
        "name": plain_text(asset.get("name")),
        "description": plain_text(asset.get("description")),
        "more_info": plain_text(asset.get("meta", {}).get("more_info")),
        "url": optional_text(asset.get("url")),
        "friendly_url": optional_text(asset.get("friendly_url")),
        "vendor": optional_text(asset.get("az_vendor_name")),
        "types": unique_values(types),
        "subjects": unique_values(subjects),
        "featured_subjects": featured_subjects,
        "access_notes": unique_values(access_notes),
        "alt_names": unique_values(alt_names),
        "created": optional_text(asset.get("created")),
        "updated": optional_text(asset.get("updated")),
        "hidden": bool(int(float(asset.get("enable_hidden", 0)))),
    }


def write_json(path, assets):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(assets, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_csv(path, assets):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for asset in assets:
            writer.writerow({**asset, **{key: json.dumps(asset[key], ensure_ascii=False) for key in ("types", "subjects", "featured_subjects", "access_notes", "alt_names")}})


def main():
    parser = argparse.ArgumentParser(
        description="Normalize visible Springshare A-Z assets into JSON and CSV."
    )
    parser.add_argument(
        "--input",
        default="temp/az_database_list_api.json",
        help="Raw A-Z JSON path, relative to the skill directory.",
    )
    parser.add_argument(
        "--json-output",
        default="references/az_databases.json",
        help="Normalized JSON output path, relative to the skill directory.",
    )
    parser.add_argument(
        "--csv-output",
        default="references/az_databases.csv",
        help="Normalized CSV output path, relative to the skill directory.",
    )
    args = parser.parse_args()

    input_path = ROOT / args.input
    assets = json.loads(input_path.read_text(encoding="utf-8"))
    visible = [normalize_asset(asset) for asset in assets if str(asset.get("enable_hidden")) == "0"]
    visible.sort(key=lambda asset: asset["name"].casefold())

    write_json(ROOT / args.json_output, visible)
    write_csv(ROOT / args.csv_output, visible)

    featured_subject_count = sum(len(asset["featured_subjects"]) for asset in visible)
    print("Normalized {} visible assets.".format(len(visible)))
    print("With subjects: {}".format(sum(bool(asset["subjects"]) for asset in visible)))
    print("With types: {}".format(sum(bool(asset["types"]) for asset in visible)))
    print("With featured subjects: {}".format(sum(bool(asset["featured_subjects"]) for asset in visible)))
    print("Featured subject associations: {}".format(featured_subject_count))
    print("Saved JSON: {}".format(ROOT / args.json_output))
    print("Saved CSV: {}".format(ROOT / args.csv_output))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("ERROR: {}".format(exc), file=sys.stderr)
        sys.exit(1)
