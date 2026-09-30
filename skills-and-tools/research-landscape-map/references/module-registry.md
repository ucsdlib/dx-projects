# Visualization Module Registry — v0.1

`landscape.json` is visualization-agnostic; modules only *read from* the data model. Selection is **data-driven + explainable**: every decision is recorded in the dashboard's "Why these views" section.

Run `python3 scripts/module_select.py <landscape.json>` to get the data-driven decision, then add any affinity-based adjustment the topic_spec clearly justifies (record it as the reason).

## Module spec

| ID | Name | Requires | Data signal to include | Recipe |
|---|---|---|---|---|
| `quadrant` | Landscape quadrant | `concepts[].evidence_state` | Base module (always) | Mermaid flowchart clustering concepts into established / contested / emerging / gap |
| `aspect_coverage` | Aspect coverage matrix | `aspects[]` (incl. `dimensions`) | ≥ 2 aspects | Table: aspect × evidence state × count × anchors — which aspects are addressed vs. untouched |
| `geo_pop` | Geography & population | `dimensions.geography`, `.population` | ≥ 5 records with place/group tags and sufficiency ≥ 0.3 | Table (or `mindmap`): place/group × evidence state |
| `chronology` | Chronology | `dimensions.time_periods` | ≥ 3 populated periods | Table: period × volume, peak marked |
| `methods` | Methodology mix | `dimensions.methodology` | ≥ 6 records tagged with method | `xychart-beta` bar: method × count |
| `takeaways` | Takeaway cards | `takeaways[]`, `provenance` | Base module — but omit if nothing is strongly supported | Blockquotes with anchors + confidence |

Sufficiency = records carrying the required data ÷ records screened (`provenance` count). Default threshold **0.3**; override with `--threshold`.

Affinity rule (implemented by the agent, not the script): if the researcher's question explicitly emphasizes a dimension (a certain population, region, method, or time frame), include the matching module even below threshold and say so in the reason.

## Output format (append to dashboard, section "Why these views")

```
- quadrant — base module (5 concepts, 3 evidence states)
- geo_pop — included: 8/12 records carry place/group tags (67% sufficiency)
- methods — included: 8 records tagged with methodology
- chronology — omitted: only 1 populated time period
- aspects (asp_001) — included: affinity (user asked about rural populations)
```

## Idea garden (deferred — do not build)

Dissonance/contradiction scatter; discipline-silo matrix (reads `aspects[].vocabulary`); citation terrain; PRISMA-style screening tracker; corpus comparison; funder-context layer; interactive canvas. The data model already supports all of these without schema change.
