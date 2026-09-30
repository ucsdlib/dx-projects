#!/usr/bin/env python3
"""Select visualization modules for a research landscape (v0.1).

Data-driven selection per references/module-registry.md: base modules
(quadrant, takeaways) plus sufficiency >= threshold for data-dependent
modules. Emits JSON {included, excluded} with a reason for every decision.

Usage: module_select.py landscape.json [--threshold 0.3] [--include id,...] [--exclude id,...]
"""
import argparse
import json
import sys

MODULE_NAMES = {
    "quadrant": "Landscape quadrant",
    "aspect_coverage": "Aspect coverage matrix",
    "geo_pop": "Geography & population",
    "chronology": "Chronology",
    "methods": "Methodology mix",
    "takeaways": "Takeaway cards",
}


def load(path):
    with open(path) as fh:
        return json.load(fh)


def record_ids(entries):
    out = set()
    for e in entries or []:
        out.update(e.get("record_ids") or [])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", help="path to landscape.json")
    ap.add_argument("--threshold", type=float, default=0.3)
    ap.add_argument("--include", help="comma-separated module ids to force include")
    ap.add_argument("--exclude", help="comma-separated module ids to force exclude")
    args = ap.parse_args()

    data = load(args.path)
    prov = data.get("provenance", [])
    total = max(len(prov), 1)
    concepts = data.get("concepts", [])
    aspects = data.get("aspects", [])
    takeaways = data.get("takeaways", [])
    dims = data.get("dimensions", {})

    decided = []

    def decide(mod_id, include, reason):
        decided.append({"id": mod_id, "name": MODULE_NAMES[mod_id], "include": include, "reason": reason})

    # quadrant (base)
    if len(concepts) >= 2:
        states = {c.get("evidence_state") for c in concepts}
        note = "" if (len(concepts) >= 4 and len(states) >= 2) else \
            f" (richness limited: {len(concepts)} concepts, {len(states)} evidence states)"
        decide("quadrant", True, "base module" + note)
    else:
        decide("quadrant", False, f"only {len(concepts)} concept(s)")

    # takeaways (base, conditional)
    strong = [t for t in takeaways
              if t.get("confidence") in ("high", "medium") and t.get("support_record_ids")]
    if strong:
        decide("takeaways", True, f"base module ({len(strong)} strongly supported takeaway(s))")
    else:
        decide("takeaways", False, "no strongly supported takeaways (confidence high/medium with anchors)")

    # aspect_coverage
    if len(aspects) >= 2:
        decide("aspect_coverage", True, f"{len(aspects)} aspects with per-aspect coverage")
    else:
        decide("aspect_coverage", False, f"only {len(aspects)} aspect(s); need >= 2")

    # geo_pop
    geo = record_ids(dims.get("geography"))
    pop = record_ids(dims.get("population"))
    n = len(geo | pop)
    suff = n / total
    if n >= 5 and suff >= args.threshold:
        decide("geo_pop", True, f"{n}/{total} records carry place/group tags ({suff:.0%} sufficiency)")
    else:
        decide("geo_pop", False, f"only {n}/{total} records carry place/group tags ({suff:.0%} sufficiency)")

    # chronology
    periods = [p for p in (dims.get("time_periods") or []) if p.get("record_ids")]
    if len(periods) >= 3:
        decide("chronology", True, f"{len(periods)} populated time periods")
    else:
        decide("chronology", False, f"only {len(periods)} populated time period(s); need >= 3")

    # methods
    m = record_ids(dims.get("methodology"))
    if len(m) >= 6:
        decide("methods", True, f"{len(m)} records tagged with methodology")
    else:
        decide("methods", False, f"only {len(m)} records tagged with methodology; need >= 6")

    # overrides
    force_inc = set(args.include.split(",")) if args.include else set()
    force_exc = set(args.exclude.split(",")) if args.exclude else set()
    for d in decided:
        if d["id"] in force_inc:
            d["include"], d["reason"] = True, "forced include (override)"
        if d["id"] in force_exc:
            d["include"], d["reason"] = False, "forced exclude (override)"

    included = [{"id": d["id"], "name": d["name"], "reason": d["reason"]} for d in decided if d["include"]]
    excluded = [{"id": d["id"], "name": d["name"], "reason": d["reason"]} for d in decided if not d["include"]]
    print(json.dumps({"included": included, "excluded": excluded}, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
