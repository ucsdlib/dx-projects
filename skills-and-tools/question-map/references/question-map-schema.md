# `question_map.json` Schema

Read this reference when constructing or validating the primary artifact. The schema is a standalone, quote-anchored graph with conventions similar to `research-landscape-map`.

## Top-level object

```json
{
  "schema_version": "0.1",
  "run": {},
  "request": {},
  "search_log": {},
  "nodes": [],
  "edges": [],
  "quotes": [],
  "themes": [],
  "coverage": {},
  "limitations": []
}
```

Theme objects are graph-addressable nodes stored in the top-level `themes` collection. Edges may therefore resolve to an object in `nodes` or `themes`.

## `run`

Use stable identifiers and ISO 8601 timestamps. Required and recommended fields:

```json
{
  "run_id": "run-2026-10-06-topic-001",
  "topic_slug": "topic-slug",
  "generated_at": "2026-10-06T00:00:00Z",
  "skill_version": "0.1",
  "data_model_version": "0.1",
  "confirmation_status": "user_confirmed | initial_prompt_only | blocked",
  "breadth": "focused | comprehensive | exhaustive",
  "theme_creation_rule": {
    "rule": "adaptive",
    "rationale": ""
  },
  "question_score_weights": {},
  "theme_score_weights": {},
  "user_choices": []
}
```

## `request`

Preserve the Stage 1 working question specification: `core_question`, `sub_questions`, `purpose`, `breadth`, `concepts`, `synonyms`, `constraints`, and `confirmation_status`.

## `search_log`

Record the full pipeline, including:

- UC Library Search mode: `primo_search_api`, `primo_pnx_rest`, or `documented_skip`;
- skip reason and coverage consequence;
- query, copy-paste form, URL, provider, page, and screen results;
- on-topic/adjacent/noise counts and fidelity;
- component decomposition and adaptive refinements;
- API calls, lookups, failures, rate limits, and skips.

Raw screening records belong in `search-results.jsonl`; do not force every low-value record into `question_map.json`.

## Nodes

Every node needs a unique `id`, `type`, and `confidence`. Use stable IDs such as `src_001`, `sq_001`, `q_001`, `nq_001`, `edge_001`, `quote_001`, and `theme_001`.

### Common enums

```text
confidence: high | medium | low
root_status: primary_user_root | inquiry_root | none
access_level: full_text | abstract_only | publisher_description | metadata_only
evidence_basis: full_text_machine_readable | abstract_and_metadata | publisher_description_and_toc | metadata_only
selection_status: selected | candidate | excluded
connection_type: direct_evidence | reasonable_inference | interpretive_connection
question_type: empirical | methodological | theoretical | policy | interpretive | comparative | measurement | intervention | equity | gap
```

### `question`

Canonical/shared research question. Recommended fields:

```json
{
  "id": "q_001",
  "type": "question",
  "canonical_label": "",
  "question_text": "",
  "variants": [],
  "origin": "user_defined | explicit | inferred",
  "question_type": "empirical",
  "root_status": "none",
  "confidence": "medium",
  "extraction_rationale": "",
  "key_terms": [],
  "user_alignment_note": "",
  "score": 0.0,
  "score_components": {}
}
```

### `source_question`

Literal or inferred question from one source. Recommended fields:

```json
{
  "id": "sq_001",
  "type": "source_question",
  "source_id": "src_001",
  "question_text": "",
  "canonical_question_id": "q_001",
  "variants": [],
  "origin": "explicit | inferred",
  "connection_type": "direct_evidence",
  "access_level": "abstract_only",
  "evidence_basis": "abstract_and_metadata",
  "quote_ids": [],
  "metadata_rationale": "",
  "confidence": "high",
  "extraction_rationale": "",
  "canonicalization_notes": ""
}
```

If `evidence_basis` is `metadata_only`, either a metadata-derived question may be recorded with low confidence and `metadata_rationale`, or the source has `no_supported_question`.

### `next_question`

Possible follow-up question, not source-backed evidence. Recommended fields:

```json
{
  "id": "nq_001",
  "type": "next_question",
  "question_text": "",
  "origin": "structure_narrowing | slot_substitution | source_gap | user_intent",
  "generation_basis": "",
  "parent_question_ids": [],
  "parent_theme_ids": [],
  "slot_substitutions": {},
  "rationale": "",
  "confidence": "medium",
  "launch_ready": false,
  "root_status": "none",
  "score": 0.0,
  "score_components": {}
}
```

Do not give a `next_question` source support unless the source explicitly names the question.

### `context`

Use a context node to preserve the user prompt or another framing statement without treating it as source-derived evidence:

```json
{
  "id": "ctx_001",
  "type": "context",
  "label": "User prompt frame",
  "statement": "",
  "root_status": "primary_user_root",
  "confidence": "high",
  "rationale": "Framing only; not a canonical analytic question."
}
```

### `source`

Selected source or citation-graph source. Include title, authors, year, venue, source type, DOI/PMID/other identifiers, URL, access level, evidence basis, abstract source, selection status, selection reason, subjects, keywords, language, open-access metadata, citation metadata, and links.

For visualization-ready graphs, also include normalized display fields:

- `citation_short`: the concise citation used in maps and tables, such as `Author et al. (YYYY)`;
- `citation_display`: the fuller human-readable citation, including title, venue, and DOI/PMID/URL when available;
- `ucls_permalink`: the UC Library Search permalink, when a record ID is available.

Citation metadata should preserve competing provider values:

```json
{
  "citation_metadata": {
    "primary_count": 58,
    "primary_provider": "openalex",
    "retrieved_at": "2026-10-06T00:00:00Z",
    "alternative_counts": [
      {"provider": "crossref", "count": 53}
    ],
    "referenced_works_count": 29,
    "related_works_count": 10,
    "counts_by_year_available": true
  }
}
```

Raw provider payloads belong in enrichment files. The canonical graph should carry the normalized fields needed for display and traceability, but it does not need to duplicate entire API responses.

### Metadata nodes

Use `discipline`, `method`, `population`, `geography`, `context`, and `concept` node types to capture reliable metadata signals. Keep labels concise and attach them to sources or questions through typed edges.

## Edges

Every edge needs `id`, `source_id`, `target_id`, `relation`, `basis`, and `confidence`. Add `evidence_ids` where applicable.

Useful typed relations:

| Direction | Relations |
|---|---|
| `source` → `source_question` | `asks`, `infers`, `raises`, `reviews` |
| `source_question` → `question` | `supports`, `variant_of`, `relates_to` |
| `question` → `question` | `relates_to`, `refines`, `generalizes`, `specifies`, `contrasts_with`, `co_occurs_with` |
| `question` → `next_question` | `proposes`, `narrows_to`, `extends_to` |
| `question`/`next_question` → `theme` | `member_of`, `proposed_for` |
| `source` → `source` | `cites`, `similar_to`, `contrasts_with` |
| `source` → metadata node | `informs`, `uses`, `studies`, `located_in`, `applies_to` |

All source-to-source-question edges require a quote or explicit metadata-derived rationale. A `source_question` must have at least one evidence-backed `supports` edge and may have more than one when the evidence warrants it; do not impose an arbitrary maximum. Secondary links use `variant_of` or `relates_to` with medium or low confidence. Question-to-question and question-to-next-question edges must record their basis.

Every `question -> theme` `member_of` edge must carry `role: primary` or `role: cross_cutting`. A question may belong to several themes, but exactly one membership is primary. The primary membership reflects where its evidence is grouped; cross-cutting membership is not containment.

When edges are changed during construction, add an entry to `run.edge_audit`:

```json
{
  "edge_id": "edge_sq_001",
  "correction": "changed relation",
  "from": "supports",
  "to": "variant_of",
  "reason": "The quoted evidence frames a related population rather than directly supporting the canonical question.",
  "confidence": "medium"
}
```

## Quotes

```json
{
  "quote_id": "quote_001",
  "source_id": "src_001",
  "text": "exact quoted sentence or passage",
  "locator": "abstract, findings section, page, URL, or other location",
  "access_level": "abstract_only",
  "evidence_basis": "abstract_and_metadata",
  "confidence": "high",
  "provenance": {}
}
```

Preserve source wording. Whitespace normalization is acceptable only when recorded; never paraphrase or elide in a way that changes meaning.

## Themes

```json
{
  "id": "theme_001",
  "type": "theme",
  "label": "",
  "statement": "",
  "question_ids": [],
  "source_ids": [],
  "next_question_ids": [],
  "support_summary": {
    "question_count": 0,
    "source_count": 0,
    "next_question_count": 0,
    "direct_evidence_count": 0,
    "reasonable_inference_count": 0,
    "interpretive_connection_count": 0
  },
  "support_tier": "single_question | single_source | multi_question | multi_source | multi_source_multi_question",
  "score": 0.0,
  "score_components": {},
  "confidence": "medium",
  "coherence_basis": "",
  "key_terms": [],
  "coverage_summary": {},
  "rationale": ""
}
```

`next_question_ids` may be linked through `proposed_for`, but they do not count as source support.

## Coverage and limitations

`coverage` should record:

- on-topic, adjacent, and noise counts;
- question and theme counts;
- distinct sources per question;
- year, discipline, method, population, geography, and context distributions;
- citation-count distributions and provider;
- access-level and evidence-basis distributions;
- explicit `not_found_statements`.

Every not-found statement must use “not found in retrieved coverage.” `limitations` must be an explicit list.

## Validation invariants

The validator checks:

- required top-level collections;
- unique node, edge, quote, and theme IDs;
- valid enums and confidence labels;
- all edge endpoints resolve to a node or theme;
- quote source IDs and edge evidence IDs resolve;
- source questions have quote or metadata-derived evidence;
- at least one evidence-backed `source_question -> question` `supports` edge per source question, with additional support edges allowed when evidence warrants;
- explicit `asks`/`infers`/`raises`/`reviews` semantics that match the source-question origin;
- exactly one primary theme membership per question, with other memberships marked `cross_cutting`;
- every theme has at least one supported question or source;
- theme support summaries and tiers are internally consistent;
- citation counts include provider and retrieval timestamp;
- not-found statements use the required phrasing.
