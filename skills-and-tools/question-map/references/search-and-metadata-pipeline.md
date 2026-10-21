# Search and Metadata Pipeline

Read this reference before building or executing searches. It defines the v0.1 discovery and enrichment rules.

## Stage 1 — Question specification

Create a working specification containing:

```json
{
  "core_question": "",
  "sub_questions": [],
  "purpose": "",
  "breadth": "focused | comprehensive | exhaustive",
  "concepts": [],
  "synonyms": [],
  "constraints": [],
  "confirmation_status": "user_confirmed | initial_prompt_only | blocked"
}
```

Do not search when confirmation is `blocked`.

## Stage 2 — UC Library Search first

If `uc-library-search` is available, use it to construct the focused query plus adaptive zoom-out and component queries. Generate direct links only with its `scripts/build_url.py`. Use single-parameter Primo query syntax, uppercase Boolean operators, quoted phrases, and parenthesized `OR` groups.

Execute through the `annotated-bibliography` pathways in this order:

1. **Primo Search API** only when the skill directory has a non-empty `PRIMO_KEY`.
2. **Primo PNX REST fallback** when Search API activation or authentication fails.
3. **Documented skip** when both pathways fail or the skill is unavailable.

For the PNX fallback, use:

```text
https://search-library.ucsd.edu/primaws/rest/pub/pnxs
```

with a campus preflight probe, 120-second timeout, `offset=0`, `limit=20`, `sort=rank`, `pcAvailability=false`, and the UCSD `inst`, `vid`, `scope`, and `tab` values. Use bracket date syntax in `qInclude`, for example:

```text
facet_searchcreationdate,exact,[2016 TO 2026]
```

Never use the UI deep-link date form through the API. Never log an API key.

If Stage 0 is skipped, record:

- that it was skipped,
- why,
- the execution mode attempted,
- the expected coverage consequence.

## Stage 3 — Adaptive screening

Classify every returned record as `on_topic`, `adjacent`, or `noise`. Fidelity is `(on_topic + adjacent) / records screened` for the query.

- Continue paging while fidelity is at least 50%.
- At 25–50%, fetch one more page, then refine.
- Below 25%, stop and refine.
- Stop early when a full page yields nothing new.
- Treat Primo result totals as estimates, not reliable counts.

Use component decomposition after a high-fidelity base query. Components should come from the actual research question. For example, an urban heat question may need exposure/measurement, vulnerable populations, interventions/policy, built environment, wellbeing/lived experience, and methods/evidence components.

While screening, keep a provisional theme scratchpad with recurring question labels, candidate source IDs, connection types, and confidence. Do not promote provisional themes to final themes until question extraction is complete.

Record a component-coverage summary in the search log. For each major component, include the queries used, selected source IDs, and `covered | weak | not_found_in_retrieved_coverage`. This prevents one broad query from producing a map that is rich in clinical outcomes but silent on lived experience, governance, methods, or equity.

## Stage 4 — Enrichment

Use additional tools only when they improve coverage. Record each provider, query, lookup, timestamp, failure, and skip.

| Tool | Role |
|---|---|
| UC Library Search / Primo PNX | First discovery, UC holdings, formats, subjects, abstracts, identifiers, and access links |
| OpenAlex | Primary work-level enrichment: DOI matching, citation counts, topics, fields, concepts, abstracts, references, related works, and open-access status |
| Crossref | DOI and publication verification, citation count, reference count, license, funder, and link metadata |
| Semantic Scholar | Optional citation graph, fields of study, influential citations, abstracts, and open-access PDFs; retry once, then move on if rate-limited |
| PubMed / ERIC / arXiv | Domain-specific enrichment when relevant |
| Browser / Google Scholar | Citation chaining and discovery only when a browser is available; verify from the source, not snippets |

When a DOI is present, verify with OpenAlex and Crossref when feasible. When no DOI is present, attempt title/author matching, record the match method, and assign confidence. Preserve competing citation counts and abstract availability by provider rather than overwriting one with another.

## Access and evidence rules

Use the safest available substrate:

1. Machine-readable full text.
2. Abstract plus metadata.
3. Publisher description and table of contents.
4. Metadata only.

Do not extract text from PDFs. Capture PDF links as retrieval targets. A metadata-only source may produce a low-confidence inferred question if the title or venue is sufficient; otherwise record `no_supported_question`.

## Stage 5 — Source selection

Do not impose a fixed source count. Select an adaptive set based on:

1. Direct relevance to the confirmed question.
2. Quality and explicitness of question evidence.
3. Contribution to thematic diversity.
4. Disciplinary, methodological, population, and geographic coverage.
5. Access level and evidence basis.
6. Citation attention, as a discovery aid only.
7. Value for the next stage of inquiry.

Prune weak duplicates only when a stronger source covers the same question or theme. Record the rationale. Mark sources `selected`, `candidate`, or `excluded`.
