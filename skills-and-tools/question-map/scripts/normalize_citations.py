#!/usr/bin/env python3
"""Normalize display citations and provider counts into question_map.json."""

import argparse
import json
from pathlib import Path


def load_json(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def clean_author(value):
    if not isinstance(value, str):
        return ""
    return value.split(".$$Q", 1)[0].strip()


def author_prefix(authors):
    cleaned = [clean_author(author) for author in authors or []]
    cleaned = [author for author in cleaned if author]
    if not cleaned:
        return "No author recorded"
    if len(cleaned) <= 3:
        return ", ".join(cleaned)
    return ", ".join(cleaned[:3]) + ", et al."


def citation_short(node):
    year = node.get("year") or "n.d."
    return f"{author_prefix(node.get('authors'))} ({year})"


def citation_display(node):
    parts = [citation_short(node), node.get("title") or "Untitled"]
    if node.get("venue"):
        parts.append(node["venue"])
    if node.get("doi"):
        parts.append(f"DOI: {node['doi']}")
    elif node.get("pmid"):
        parts.append(f"PMID: {node['pmid']}")
    elif node.get("urls"):
        parts.append(f"URL: {node['urls'][0]}")
    return ". ".join(str(part).rstrip(".") for part in parts) + "."


def enrichment_by_source(enrichment_dir):
    records = {}
    for path in sorted(Path(enrichment_dir).glob("*.json")):
        source_id = "_".join(path.stem.split("_")[:2])
        records[source_id] = load_json(path)
    return records


def normalize(graph, selected_records, enrichment_dir):
    enrichment = enrichment_by_source(enrichment_dir) if enrichment_dir else {}
    record_ids = {
        record.get("id"): record.get("record_id")
        for record in selected_records or []
        if record.get("id") and record.get("record_id")
    }
    generated_at = graph.get("run", {}).get("generated_at")
    changed = 0
    for node in graph.get("nodes", []):
        if node.get("type") != "source":
            continue
        node["citation_short"] = citation_short(node)
        node["citation_display"] = citation_display(node)
        if record_ids.get(node.get("id")):
            node["ucls_permalink"] = (
                f"https://search-library.ucsd.edu/permalink/01UCS_SDI/qkke1q/{record_ids[node['id']]}"
            )
        item = enrichment.get(node.get("id"))
        if item and item.get("cited_by_count") is not None:
            node["citation_metadata"] = {
                "primary_count": item["cited_by_count"],
                "primary_provider": "openalex",
                "retrieved_at": generated_at,
                "alternative_counts": [],
                "counts_by_year_available": bool(item.get("counts_by_year")),
                "provider_record_id": item.get("id"),
            }
        else:
            node["citation_metadata"] = None
        changed += 1
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", required=True, type=Path)
    parser.add_argument("--selected", required=True, type=Path)
    parser.add_argument("--enrichment-dir", required=True, type=Path)
    args = parser.parse_args()

    graph = load_json(args.graph)
    selected_records = load_json(args.selected)
    changed = normalize(graph, selected_records, args.enrichment_dir)
    with args.graph.open("w", encoding="utf-8") as handle:
        json.dump(graph, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"Normalized citations for {changed} source nodes.")


if __name__ == "__main__":
    main()
