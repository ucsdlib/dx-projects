#!/usr/bin/env python3
"""Validate a research landscape data model (landscape.json, v0.1).

Checks required fields, enums, and referential integrity. Exits 0 when valid,
1 when invalid. Prints a summary of counts (provenance, concepts, aspects,
takeaways, gaps) on success and every issue on failure.

Usage: validate_landscape.py landscape.json [--strict]
"""
import argparse
import json
import sys

SCHEMA_VERSION_PREFIX = "0."
REQUIRED_TOP = [
    "schema_version", "topic", "run", "topic_spec",
    "query_trail", "concepts", "dimensions", "aspects",
    "takeaways", "gaps", "provenance", "not_found_statements",
]
CONFIDENCE = {"high", "medium", "low"}
EVIDENCE_STATE = {"well_understood", "contested", "emerging", "mixed", "weak", "not_found"}
ASPECT_KIND = {"component", "framework", "lens", "sub_question"}
ASPECT_ORIGIN = {"user_defined", "literature_emergent", "mixed"}
GRANULARITY = {"region", "country", "urban", "suburban", "rural", "neighborhood"}
APPROACH = {"quantitative", "qualitative", "mixed", "modeling", "review"}
SOURCE = {"primo", "crossref", "html_fulltext"}
ACCESS_LEVEL = {"full", "abstract", "paywalled"}
TAKEAWAY_TYPE = {"convergence", "tension", "gap"}
GAP_TYPE = {"not_retrieved", "absent_in_corpus", "weak_coverage"}
DIMENSION_KEYS = {"geography", "population", "context", "methodology", "time_periods", "disciplines"}


def errs_from(issues, data, strict):
    errors = []

    def add(msg):
        errors.append(msg)

    for key in REQUIRED_TOP:
        if key not in data:
            add(f"ERROR missing top-level key: {key}")
    if errors:
        return errors  # stop early; rest is undefined

    if not str(data["schema_version"]).startswith(SCHEMA_VERSION_PREFIX):
        add(f"ERROR schema_version must start with {SCHEMA_VERSION_PREFIX!r}: {data['schema_version']!r}")
    if not isinstance(data.get("query_trail"), list) or not data["query_trail"]:
        add("ERROR query_trail must be a non-empty list")

    prov = {p["record_id"] for p in data.get("provenance", []) if isinstance(p, dict) and "record_id" in p}
    all_ids = [p.get("record_id") for p in data.get("provenance", []) if isinstance(p, dict) and "record_id" in p]
    if len(all_ids) != len(set(all_ids)):
        add("ERROR duplicate record_id in provenance")

    def check_refs(container, where, label):
        for i, item in enumerate(container):
            rids = item.get(label, []) or []
            for rid in rids:
                if rid not in prov:
                    add(f"ERROR {where}[{i}].{label} references unknown record: {rid}")

    concepts = data.get("concepts", [])
    for i, c in enumerate(concepts):
        if c.get("evidence_state") not in EVIDENCE_STATE:
            add(f"ERROR concepts[{i}].evidence_state invalid: {c.get('evidence_state')!r}")
        if c.get("confidence") not in CONFIDENCE:
            add(f"ERROR concepts[{i}].confidence invalid: {c.get('confidence')!r}")
    check_refs(concepts, "concepts", "support_record_ids")

    dims = data.get("dimensions", {})
    for dkey in DIMENSION_KEYS:
        entries = dims.get(dkey, []) or []
        for i, e in enumerate(entries):
            check_refs([e], f"dimensions.{dkey}", "record_ids")
            if dkey == "geography" and e.get("granularity") not in GRANULARITY:
                add(f"ERROR dimensions.geography[{i}].granularity invalid: {e.get('granularity')!r}")
            if dkey == "methodology" and e.get("approach") not in APPROACH:
                add(f"ERROR dimensions.methodology[{i}].approach invalid: {e.get('approach')!r}")
            if dkey in ("geography", "population", "context", "methodology") and e.get("confidence") not in CONFIDENCE:
                add(f"ERROR dimensions.{dkey}[{i}].confidence invalid: {e.get('confidence')!r}")

    aspects = data.get("aspects", [])
    aspect_ids = set()
    for i, a in enumerate(aspects):
        if a.get("id") in aspect_ids:
            add(f"ERROR duplicate aspect id: {a.get('id')}")
        aspect_ids.add(a.get("id"))
        if a.get("kind") not in ASPECT_KIND:
            add(f"ERROR aspects[{i}].kind invalid: {a.get('kind')!r}")
        if a.get("origin") not in ASPECT_ORIGIN:
            add(f"ERROR aspects[{i}].origin invalid: {a.get('origin')!r}")
        cov = a.get("coverage") or {}
        if cov.get("evidence_state") not in EVIDENCE_STATE:
            add(f"ERROR aspects[{i}].coverage.evidence_state invalid: {cov.get('evidence_state')!r}")
        if cov.get("confidence") not in CONFIDENCE:
            add(f"ERROR aspects[{i}].coverage.confidence invalid: {cov.get('confidence')!r}")
        check_refs([{"record_ids": cov.get("record_ids", [])}], f"aspects[{i}].coverage", "record_ids")
        for pid in (a.get("parent_id") or None, *((a.get("sub_aspects") or []) if a.get("sub_aspects") else [])):
            if pid is not None and pid not in aspect_ids - {a.get("id")}:
                add(f"ERROR aspects[{i}] references unknown aspect: {pid}")
    if strict and len(aspect_ids) != len({a.get("id") for a in aspects}):
        add("ERROR aspects have missing/invalid ids")

    takeaways = data.get("takeaways", [])
    for i, t in enumerate(takeaways):
        if t.get("type") not in TAKEAWAY_TYPE:
            add(f"ERROR takeaways[{i}].type invalid: {t.get('type')!r}")
        if t.get("confidence") not in CONFIDENCE:
            add(f"ERROR takeaways[{i}].confidence invalid: {t.get('confidence')!r}")
    check_refs(takeaways, "takeaways", "support_record_ids")

    gaps = data.get("gaps", [])
    for i, g in enumerate(gaps):
        if g.get("gap_type") not in GAP_TYPE:
            add(f"ERROR gaps[{i}].gap_type invalid: {g.get('gap_type')!r}")
        aid = g.get("aspect_id")
        if aid is not None and aid not in aspect_ids:
            add(f"ERROR gaps[{i}].aspect_id references unknown aspect: {aid}")

    for i, p in enumerate(data.get("provenance", [])):
        if p.get("source") not in SOURCE:
            add(f"ERROR provenance[{i}].source invalid: {p.get('source')!r}")
        if p.get("access_level") not in ACCESS_LEVEL:
            add(f"ERROR provenance[{i}].access_level invalid: {p.get('access_level')!r}")

    for i, nf in enumerate(data.get("not_found_statements", [])):
        if "not found in retrieved coverage" not in nf.get("statement", ""):
            add(f"ERROR not_found_statements[{i}] must phrase as 'not found in retrieved coverage'")
    return errors


def summary(data, issues):
    if issues:
        return
    print("landscape.json valid (schema v%s)" % data.get("schema_version"))
    print("  provenance records: %d" % len(data.get("provenance", [])))
    print("  concepts: %d | aspects: %d | takeaways: %d | gaps: %d" % (
        len(data.get("concepts", [])), len(data.get("aspects", [])),
        len(data.get("takeaways", [])), len(data.get("gaps", []))))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", help="path to landscape.json")
    ap.add_argument("--strict", action="store_true", help="require every aspect to have a unique id")
    args = ap.parse_args()
    try:
        data = json.load(open(args.path))
    except Exception as exc:
        print(f"FATAL could not load {args.path}: {exc}")
        sys.exit(2)
    issues = errs_from(issues=None, data=data, strict=args.strict)
    if issues:
        for line in issues:
            print(line)
        sys.exit(1)
    summary(data, issues)
    sys.exit(0)


if __name__ == "__main__":
    main()
