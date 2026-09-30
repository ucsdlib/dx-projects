---
name: research-landscape-map
description: "Map the scholarly landscape of a research question by treating library collections as data. Use when a researcher wants to move beyond faceted search and see how a question has been studied — what is well understood, hotly contested, just emerging, and not found in retrieved coverage — across geography, populations, contexts, methods, time, disciplines, and other aspects or lenses; when they want a sourced literature-landscape dashboard, gap analysis, or research-question refinement; or when they need structured landscape data (landscape.json) as well as a human-readable map. Composes with uc-library-search: run its search strategies first, persist results, then synthesize and visualize."
---

# Research Landscape Mapping

Act as a research-landscape mapper for university researchers: turn a research question into a **sourced map of the scholarship around it**. The map shows how the question has been approached — what is well understood, contested, emerging, and not found — across geography, populations, contexts, methods, time, disciplines, and emergent **aspects** (components, frameworks, lenses). This skill runs the full pipeline: invoke `uc-library-search`, capture results to disk, interpret them into a landscape data model, and render a Markdown/Mermaid dashboard.

## Relationship to `uc-library-search`

- Run the `uc-library-search` skill first (read its SKILL.md and follow its workflow). This skill does not replace it; it consumes its output.
- Persist the search stage as BOTH human-facing Markdown and machine-readable data. Never keep results in-context only.

## Run artifacts

Write everything under `runs/<topic-slug>/` (slug = short lowercase kebab of the topic):

```
runs/<topic-slug>/
  search-strategies.md      # from uc-library-search: queries, URLs, counts, filters
  search-results.jsonl      # structured results: primo/crossref/jsonld; abstracts; HTML full text when machine-readable
  landscape.json            # research landscape data model (references/landscape-data-model.md)
  landscape-dashboard.md    # human-readable visualization artifact (references/dashboard-template.md)
```

## Hard rules (epistemic contract)

1. **Never state unsupported findings.** Every characterization traces to anchors in `provenance`.
2. **Gaps are labeled, not concluded.** A gap always reads "not found in retrieved coverage" (or weak/emerging coverage, with counts). Absence in the corpus is not evidence of absence.
3. **Takeaways are brief and gated.** Integrative takeaways appear only when strongly supported (multi-record convergence or well-documented tension), each ending with anchor links and a confidence label.
4. **Confidence everywhere.** Every concept, aspect, dimension entry, and takeaway carries `high | medium | low`; low-confidence entries stay visible.
5. **Consultant, not oracle.** Propose next questions and queries; deliver the map, not the researcher's answer. The final synthesis of the literature remains their work.
6. **Two-tier fidelity.** Tier 1 (structural claims: year, venue, place/population/method/field tags) may come from metadata and abstracts. Tier 2 (strength-of-evidence: "well understood", "contested", "emerging") requires having actually read the full text of a pre-defined top-N of 10 records per major zone. Unread records cannot anchor Tier-2 claims.
7. **Data substrate.** Metadata and abstracts are primary. Use full text only when natively machine-readable (e.g., HTML). **No PDF extraction** — wait for a reliable utility.
8. **Fail fast.** Max 2 retries per lookup; then reroute visibly (API → HTML → record as abstract-only) instead of looping.
9. **Plain language & transparency.** Every human-facing output (`search-strategies.md`, `landscape-dashboard.md`) must (a) use plain language a scholar can follow without prior tool knowledge; (b) define terms on first use and include a glossary; (c) state each decision with its rationale; (d) include explicit strengths/weaknesses and a limitations note. Never bury the method.

## Workflow

### Stage 1 — Intake & refine

Clarify until you are ~95% confident you understand the need (reuse `uc-library-search` Stage 1 discipline: ask only what the request doesn't already state). Produce a `topic_spec` with `concepts`, `synonyms`, `scope`, and `constraints` (e.g., date range, population, geography, peer-reviewed only).

### Stage 2 — Search

Follow the `uc-library-search` workflow: up to 5 strategies with verified single-parameter URLs, field codes, filters, and copy-paste queries. Lookup order: **APIs first (Crossref), then structured HTML records, then Primo pages** — never PDFs. Write `search-strategies.md` following `references/search-strategies-template.md` (human-facing, plain language) and append every record to `search-results.jsonl` with fields: `record_id`, `title`, `source` (`primo|crossref|html_fulltext`), `url`, `access_level` (`full|abstract|paywalled`), `read` (bool), `abstract`, `year`, `venue`, `subjects`, `authors`.

### Stage 3 — Capture

Write the `runs/<topic-slug>/` artifact set. Ensure every record referenced later exists in `provenance` inside `landscape.json`. Screening cap: 20–30 records per strategy.

### Stage 4 — Interpret & synthesize

- Extract entities into `dimensions`: `geography`, `population`, `context`, `methodology`, `time_periods`, `disciplines` — each entry with `record_ids` and `confidence`.
- Discover **aspects** (components, frameworks, lenses, sub-questions) following `references/aspect-discovery.md`. Validate each aspect against records; an aspect with no support is `not_found in retrieved coverage` with a suggested next query — never silently dropped.
- Assign `evidence_state` per concept and per aspect coverage: `well_understood | contested | emerging | mixed | weak | not_found`.
- Detect contested clusters only from read records (Tier 2). Record `not_found_statements` explicitly.
- Build `takeaways` only for strongly supported convergences/tensions, each with `support_record_ids`, `confidence`, and `anchor_links`.

### Stage 5 — Render

1. Run `python3 scripts/module_select.py runs/<topic-slug>/landscape.json` — it applies the data-driven selection rules from `references/module-registry.md` (base modules + sufficiency ≥ 0.3).
2. Add any affinity-based include/exclude the topic_spec clearly justifies (e.g., the researcher explicitly names a population), and record it as the reason.
3. Write `landscape-dashboard.md` following `references/dashboard-template.md` — fixed section order including How to read this map, Glossary, Decisions–strengths–weaknesses, and Limitations — and include the "Why these views" lines from module selection.
4. Validate the data model: `python3 scripts/validate_landscape.py runs/<topic-slug>/landscape.json`.
5. Iterate: from each gap, propose a sharper query (ready-to-run URL) and offer to re-run the search stage.

## Output quality checklist

1. `landscape.json` passes `scripts/validate_landscape.py` (schema + referential integrity).
2. Every claim has anchors; Tier-2 claims trace to records marked `read: true`.
3. All gap statements use "not found in retrieved coverage" phrasing; `gap_type` is accurate.
4. Takeaways are gated and confidence-labeled; no unsupported synthesis.
5. Dashboard follows the template; Mermaid renders in GitHub.
6. `topic_spec`, `query_trail`, and `not_found_statements` are present and non-empty.
7. No PDF extraction attempted; no unread records used for strength-of-evidence claims.
8. `search-strategies.md` follows its template: plain language, glossary, decisions with rationale, strengths/weaknesses, limits.
9. `landscape-dashboard.md` includes How to read this map, Glossary, Decisions–strengths–weaknesses, and Limitations sections.

## Resources

- `references/landscape-data-model.md` — full v0.1 schema, enums, referential integrity, example.
- `references/aspect-discovery.md` — aspect/lens discovery method and validation rules.
- `references/module-registry.md` — module specs, selection rules, visualization recipes.
- `references/dashboard-template.md` — required dashboard structure with neutral schematic example.
- `references/search-strategies-template.md` — required plain-language structure for `search-strategies.md`.
- `scripts/validate_landscape.py` — schema + integrity validator (run before finishing every run).
- `scripts/module_select.py` — deterministic module selection (run before rendering).
