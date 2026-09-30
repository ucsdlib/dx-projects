# Research Landscape Data Model — v0.1

Source of truth for `landscape.json`. Two hard rules: the model is **visualization-agnostic** (pure landscape data, no view logic), and every entity carries **provenance + confidence**.

## Top-level structure

```json
{
  "schema_version": "0.1",
  "topic": "string (research question as stated)",
  "run": { "id": "string", "generated_at": "ISO-8601", "skill_versions": {} },
  "topic_spec": { "concepts": [], "synonyms": [], "scope": "string", "constraints": [] },
  "query_trail": [ ],
  "concepts": [ ],
  "dimensions": { },
  "aspects": [ ],
  "takeaways": [ ],
  "gaps": [ ],
  "provenance": [ ],
  "not_found_statements": [ ]
}
```

## Fields

### `topic_spec`
| Field | Required | Notes |
|---|---|---|
| `concepts` | yes | Core concepts (strings), as clarified in Stage 1 |
| `synonyms` | yes | Alternate vocabularies per concept (may be empty array) |
| `scope` | yes | One-line scope statement |
| `constraints` | yes | e.g., date range, populations, geography, peer-reviewed only |

### `query_trail`
One entry per executed search: `stage` (`search`), `strategy` (label), `url` (verified single-parameter Primo URL), `result_count` (int), `filters` (list). Required: at least one entry.

### `concepts`
| Field | Required | Enum / Notes |
|---|---|---|
| `label` | yes | Concept name |
| `aliases` | yes | Synonyms seen in the corpus |
| `evidence_state` | yes | `well_understood | contested | emerging | mixed | weak | not_found` |
| `support_record_ids` | yes | Must resolve in `provenance` |
| `confidence` | yes | `high | medium | low` |
| `notes` | no | Free text (e.g., vocabulary drift) |

### `dimensions` — the guaranteed renderable subset of aspects
| Key | Entry fields | Notes |
|---|---|---|
| `geography` | `place`, `granularity` (`region|country|urban|suburban|rural|neighborhood`), `record_ids`, `confidence` | |
| `population` | `group`, `record_ids`, `confidence` | |
| `context` | `setting` (`urban|suburban|rural|coastal|inland|...`), `record_ids`, `confidence` | |
| `methodology` | `approach` (`quantitative|qualitative|mixed|modeling|review`), `record_ids`, `confidence` | |
| `time_periods` | `period` (e.g., `2000-2010`), `record_ids`, `is_peak` (bool) | |
| `disciplines` | `field`, `record_ids`, `vocabulary_note` | |

All `record_ids` must resolve in `provenance`. All dimension entries carry `confidence` except `time_periods` (derived from counts) and `disciplines` (use `vocabulary_note`).

### `aspects` — the emergent layer
| Field | Required | Enum / Notes |
|---|---|---|
| `id` | yes | Unique, `asp_001`.. |
| `label` | yes | Aspect name |
| `kind` | yes | `component | framework | lens | sub_question` (open enum — unknown kinds are allowed) |
| `origin` | yes | `user_defined | literature_emergent | mixed` |
| `parent_id` | no | Null or a valid aspect `id` |
| `sub_aspects` | no | List of valid aspect `id`s |
| `coverage` | yes | `{ "evidence_state": "well_understood|contested|emerging|mixed|weak|not_found", "record_ids": [], "confidence": "high|medium|low" }` |
| `lenses` | no | Cross-cutting lenses: `equity`, `gender`, `scale`, `temporality`, ... |
| `vocabulary` | no | `{ "terms": [], "disciplines": [] }` — how the literature names it |
| `notes` | no | Free text |

The fixed `dimensions` keys are the guaranteed renderable subset of aspects. Every aspect — standard or emergent — exposes the same surface `{id, coverage, record_ids, confidence}` so any future visualization can render it without a schema change.

### `takeaways`
`statement`, `type` (`convergence|tension|gap`), `support_record_ids` (must resolve), `confidence` (`high|medium|low`), `anchor_links` (list of URLs). Only include when strongly supported (multi-record convergence or documented tension).

### `gaps`
`statement`, `gap_type` (`not_retrieved|absent_in_corpus|weak_coverage`), `aspect_id` (optional, must resolve), `suggested_query` (string), `query_test_url` (ready-to-run URL). Statements must use the phrasing "not found in retrieved coverage" for `not_retrieved`/`absent_in_corpus`.

### `provenance`
```json
{
  "record_id": "rec_001",
  "title": "...",
  "source": "primo|crossref|html_fulltext",
  "url": "...",
  "access_level": "full|abstract|paywalled",
  "read": true,
  "abstract": "...", "year": 2020, "venue": "...", "subjects": [], "authors": []
}
```
`read: true` marks records whose full text was actually read (Tier-2 eligible).

### `not_found_statements`
`about` (`geography|population|method|...`), `statement` (must include "not found in retrieved coverage"). Explicit, qualified absence claims.

## Referential integrity (enforced by `scripts/validate_landscape.py`)

- Every id in `concepts[].support_record_ids`, `dimensions.*[].record_ids`, `aspects[].coverage.record_ids`, and `takeaways[].support_record_ids` resolves to a `provenance` entry.
- `aspects[].parent_id` and every `aspects[].sub_aspects` id resolve to an aspect.
- Every `gaps[].aspect_id` resolves to an aspect.
- No duplicate record, aspect, or gap ids.

## Example (abbreviated)

```json
{
  "schema_version": "0.1",
  "topic": "How does extreme heat affect health in urban communities?",
  "run": { "id": "run-20260918-heat-001", "generated_at": "2026-09-18T00:00:00Z", "skill_versions": {"research-landscape-map": "0.1"} },
  "topic_spec": { "concepts": ["extreme heat", "urban health"], "synonyms": ["heat waves", "urban heat island"], "scope": "Health impacts of extreme heat in urban populations", "constraints": ["2015-2026"] },
  "query_trail": [ { "stage": "search", "strategy": "heat AND urban health", "url": "https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22extreme%20heat%22%20OR%20%22heat%20waves%22)%20AND%20(%22urban%22%20AND%20health)", "result_count": 145, "filters": ["peer_reviewed"] } ],
  "concepts": [ { "label": "heat exposure measurement", "aliases": ["heat metrics"], "evidence_state": "well_understood", "support_record_ids": ["rec_001", "rec_002"], "confidence": "high", "notes": "" } ],
  "dimensions": { "geography": [ { "place": "urban US", "granularity": "urban", "record_ids": ["rec_001"], "confidence": "medium" } ],
                   "population": [ { "group": "outdoor workers", "record_ids": ["rec_003"], "confidence": "medium" } ],
                   "methodology": [ { "approach": "quantitative", "record_ids": ["rec_001"], "confidence": "high" } ], "time_periods": [], "context": [], "disciplines": [] },
  "aspects": [ { "id": "asp_001", "label": "heat exposure measurement", "kind": "component", "origin": "literature_emergent", "parent_id": null, "sub_aspects": [], "coverage": { "evidence_state": "well_understood", "record_ids": ["rec_001", "rec_002"], "confidence": "high" }, "lenses": [], "vocabulary": { "terms": ["urban heat island", "heat index"], "disciplines": ["epidemiology"] }, "notes": "" } ],
  "takeaways": [ { "statement": "Urban heat exposure metrics are well studied; intervention outcomes are contested.", "type": "convergence", "support_record_ids": ["rec_001", "rec_002"], "confidence": "medium", "anchor_links": ["https://doi.org/..."] } ],
  "gaps": [ { "statement": "Heat-health effects in rural communities are not found in retrieved coverage.", "gap_type": "not_retrieved", "aspect_id": "asp_001", "suggested_query": "heat AND (rural OR non-urban) AND health", "query_test_url": "https://search-library.ucsd.edu/discovery/search?query=..." } ],
  "provenance": [ { "record_id": "rec_001", "title": "Urban heat and mortality: a review", "source": "crossref", "url": "https://doi.org/...", "access_level": "abstract", "read": false, "year": 2021 } ],
  "not_found_statements": [ { "about": "geography", "statement": "Rural heat-health studies not found in retrieved coverage." } ]
}
```
