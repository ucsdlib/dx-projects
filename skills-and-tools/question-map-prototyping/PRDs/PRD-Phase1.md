# Question Map — Product Requirements Document

**Version:** 0.2 draft  
**Date:** 2026-10-06  
**Skill name:** `question-map`  
**Primary artifact:** `question_map.json`

## 1. Summary

`question-map` maps the questions embedded in a scholarly landscape, leveraging structured search and analysis of search results. It intentionally does not attempt to summarize the research landscape for the user.

Given a user prompt, the skill first clarifies the user’s core research question, then uses UC Library Search as the first discovery pathway and follows the `annotated-bibliography` philosophy of fidelity-driven search, “search within,” direct quotation, access-level transparency, and accurate-before-helpful representation.

The selected sources are converted into a standalone, quote-anchored graph. Each source can ask, address, infer, challenge, or relate to one or more research questions. Similar source questions are canonicalized into shared question nodes, and related questions are grouped into themes. The graph also includes possible next questions generated from gaps, slot substitutions, or the question structure itself. The v0.1 dataset is designed to support future network visualizations and follow-up inquiry, but it should not attempt settled/contested/emerging classification or interactive rendering yet.

## 2. Goals

1. Identify and represent the research questions that selected scholarly sources explicitly ask or clearly imply.
2. Preserve multiple questions per source and retain the source text used to derive each question.
3. Build a robust, source-and-question graph that supports future visualizations.
4. Use adaptive search breadth based on user intent, search fidelity, and component decomposition rather than a fixed target number of sources.
5. Capture as much reliable metadata as feasible: disciplines, topics, methods, populations, geographies, citation counts, references, related works, publication year, venue, access level, open-access links, and subject vocabulary.
6. Close each run by showing the user which themes and possible next questions are available for deeper inquiry and where to go next. Serve as a launching point to foster human-driven research as the next steps.
7. Keep the map honest: unsupported synthesis, forced controversy, and inferred consensus are prohibited.

## 3. Non-Goals for v0.1

- Do not produce an interactive or polished network visualization.
- Do not classify questions as settled, contested, or emerging.
- Do not answer the user’s research question or provide a final literature synthesis.
- Do not use citation counts as measures of correctness, quality, or consensus.
- Do not extract text from PDFs. Store PDF URLs for human retrieval, but rely on APIs, metadata, abstracts, and machine-readable HTML full text when available.
- Do not silently treat missing data, low-fidelity search results, or absence in the retrieved corpus as evidence of absence.
- Do not force every source into a question if the available text does not support one.

## 4. Invocation and Intake

### Invocation

Use automatic skill activation when a user asks to map questions, map a research landscape through questions, build a question graph, or identify the questions inside a literature. Also support explicit invocation as `$question-map`.

### Intake rules

The skill should ask zero to three concise clarifying questions, or up to five total only when initial responses are too vague to proceed responsibly.

Ask only for material missing information, such as:

- The refined research question, if the prompt is ambiguous.
- The purpose: quick orientation, literature review, publication-grade survey, or focused inquiry.
- Preferred breadth: focused, comprehensive, or exhaustive.
- Scope constraints: time period, peer-reviewed only, disciplines, population, geography, or publication types.
- Whether the user wants the questions to emphasize empirical findings, methods, policy, theory, lived experience, or another lens.

If the initial prompt is already sufficient, proceed without clarification. Before searching, state the working question and any major constraints in one short confirmation line. Record confirmation as one of:

- `user_confirmed` — the user explicitly confirmed after follow-up.
- `initial_prompt_only` — the assistant judged the prompt sufficient and proceeded.
- `blocked` — no search should run until the user confirms.

## 5. Search and Curation Workflow

### Stage 1 — Question specification

Create a working specification with:

```json
{
  "core_question": "...",
  "sub_questions": [],
  "purpose": "...",
  "breadth": "focused | comprehensive | exhaustive",
  "concepts": [],
  "synonyms": [],
  "constraints": [],
  "confirmation_status": "user_confirmed | initial_prompt_only | blocked"
}
```

### Stage 2 — UC Library Search first

If `uc-library-search` is available:

1. Use it to build the focused query plus adaptive zoom-out and component queries.
2. Generate direct links with `scripts/build_url.py`.
3. Execute through the documented Primo pathways described by `annotated-bibliography`:
   - Primo Search API when a `PRIMO_KEY` is available.
   - Otherwise, the keyless Primo PNX REST fallback after a campus preflight probe.
4. Use a 120-second timeout, `limit=20`, `sort=rank`, and adaptive pagination.

Record a documented skip if both Primo pathways fail or the skill is unavailable. State the coverage consequence rather than silently switching tools.

### Stage 3 — Fidelity-driven screening and provisional theme scan

Use the `annotated-bibliography` adaptive-screening model:

- Classify each record as `on_topic`, `adjacent`, or `noise`.
- Continue paging while fidelity — the on-topic plus adjacent share — remains at or above 50%.
- At 25–50%, fetch one more page, then refine.
- Below 25%, stop and refine the query.
- Stop a page early when it yields nothing new.
- Do not use Primo result totals as reliable counts.

Use component decomposition, or “search within,” after high-fidelity base searches. Component queries should reflect the actual question rather than a generic template. For the exploratory heat-health example, useful components included exposure/measurement, vulnerable populations, interventions/policy, built environment, wellbeing/lived experience, and methods/evidence.

While screening, maintain a provisional theme scratchpad. Record recurring question labels, source IDs, connection types, and confidence. Use the scratchpad to guide component decomposition and source selection, but do not promote a provisional theme to a final theme until question extraction is complete.

### Stage 4 — Additional discovery and enrichment

Follow the `annotated-bibliography` pipeline order and add tools only when they improve coverage:

| Tool | v0.1 role |
|---|---|
| UC Library Search / Primo PNX | First discovery, UC holdings, formats, subjects, abstracts, identifiers, local access links |
| OpenAlex | Primary scholarly enrichment: DOI matching, citation counts, topics, fields, concepts, abstracts, references, related works, open-access status |
| Crossref | DOI and publication verification, citation count, reference count, license, funder, and full-text link metadata |
| Semantic Scholar | Optional citation graph, field-of-study tags, influential citations, and open-access PDFs; retry once and move on if rate-limited |
| PubMed / ERIC / arXiv | Domain-specific enrichment when relevant |
| Browser / Google Scholar | Citation chaining and discovery only when a browser is available; verify from the source, not snippets |

When a DOI is present, verify against OpenAlex and Crossref when feasible. When no DOI is present, attempt title/author matching but record the match method and confidence. Every API-derived field must record its provider and retrieval timestamp.

### Stage 5 — Source selection

Do not impose a fixed source count. Select an adaptive set based on:

1. Direct relevance to the user’s confirmed question.
2. Quality and explicitness of question evidence.
3. Contribution to thematic diversity.
4. Disciplinary, methodological, population, and geographic coverage.
5. Access level and evidence basis.
6. Citation attention, treated only as a discovery aid, not as correctness.
7. Value for the user’s next stage of inquiry.

Prune weak duplicates and low-confidence sources when a stronger source covers the same question or theme. Record the pruning rationale. Sources should be marked `selected`, `candidate`, or `excluded`.

## 6. Question Extraction Rules

For each selected source, extract all source questions supported by the source text, not only the central question. Every source question must have:

- A canonical label, if the source question is mapped to a canonical question.
- A concise source-specific question text.
- Variants or near-duplicate labels, when applicable.
- An origin: `explicit`, `inferred`, or `user_defined`.
- A connection type from the `annotated-bibliography` model: `direct_evidence`, `reasonable_inference`, or `interpretive_connection`.
- Direct supporting quote or quotes.
- Access level and evidence basis.
- A confidence rating: `high`, `medium`, or `low`.
- A short extraction rationale.

### Connection types

- **Direct evidence:** the source explicitly states the question, objective, aim, hypothesis, review objective, or research gap.
- **Reasonable inference:** the source does not phrase the question explicitly, but its stated purpose, methods, findings, or limitations clearly imply it.
- **Interpretive connection:** the source addresses a related domain and may help frame the question, but the connection requires a documented interpretive step.

Only `direct_evidence` and `reasonable_inference` may count as primary support for a theme. `interpretive_connection` may remain visible with lower confidence but must not be treated as equivalent support.

### Confidence guidance

- **High:** explicit question or aim, direct quote, and reliable abstract or full-text basis.
- **Medium:** clear inference from an explicitly quoted purpose, findings, title, abstract, or research gap.
- **Low:** weak inference, metadata-only basis, multiple interpretive steps, or uncertain source matching.

If a source has no question that can be represented faithfully, record `no_supported_question` rather than inventing one.

Metadata-only sources may produce low-confidence questions when the title or venue is sufficient to infer a question; otherwise record `no_supported_question`. In either case, set `evidence_basis: metadata_only` and preserve the access limitation in the graph.

### Possible next questions

After source questions are extracted and canonicalized, generate possible next questions by:

- narrowing a parent question to a specific outcome, mechanism, population, geography, method, or time frame;
- substituting one slot in a recurring question structure;
- following an explicit research gap named in a source; or
- proposing a question the user could pursue in a follow-up run.

Possible next questions must be represented as `next_question` nodes, not as source-backed questions. Each should record its generation basis, parent question or theme, slot substitutions, rationale, and confidence. Unless the next question is explicitly named in a source, it should not have source support and should not be treated as evidence about the literature.

## 7. Primary Data Model: `question_map.json`

The file should be a standalone graph with conventions reused from `research-landscape-map` where useful, especially stable IDs, provenance, query trails, confidence labels, and “not found in retrieved coverage” phrasing.

### Top-level structure

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

### `run`

Include:

- Stable run ID.
- Topic slug.
- Generated-at timestamp.
- Skill versions and helper versions.
- Confirmation status.
- Search breadth.
- Data-model version.
- User choices that affected scope.

### `request`

Preserve the working question specification from Stage 1, including concepts, synonyms, constraints, purpose, breadth, and confirmation.

### `search_log`

Record the full pipeline:

- Whether UC Library Search ran and in which mode.
- Every query, copy-paste form, URL, provider, page, and screen result.
- On-topic/adjacent/noise counts and fidelity percentage.
- Component decomposition decisions.
- Adaptive refinements.
- API calls, lookups, skips, and rate limits.
- Coverage consequences of any skip.

Also persist the raw screening output in `search-results.jsonl` so `question_map.json` does not have to preserve every low-value record.

### `nodes`

Use stable IDs and typed nodes. Node types should include:

| Node type | Purpose |
|---|---|
| `question` | Canonical/shared research question |
| `source_question` | Literal or inferred question from one source |
| `next_question` | Possible follow-up question generated from structure, a gap, or user intent |
| `source` | Selected source or citation-graph source |
| `theme` | Topic label and plain-language statement emerging from supported questions |
| `discipline` | Academic or professional domain |
| `method` | Study design, data, or analytic approach |
| `population` | Population or group studied |
| `geography` | Place or spatial scope |
| `context` | Setting, system, policy, infrastructure, or environment |
| `concept` | Repeated topic or vocabulary term |

A source node should include title, authors, year, venue, source type, DOI/PMID/other identifiers, URL, access level, evidence basis, abstract source, selected/candidate/excluded status, selection reason, subjects, keywords, language, open-access metadata, citation metadata, and any full-text links. Captured PDF links should be marked as retrieval targets, not extracted text.

Citation metadata should preserve competing provider values rather than silently overwriting one with another:

```json
{
  "citation_metadata": {
    "primary_count": 58,
    "primary_provider": "openalex",
    "retrieved_at": "2026-10-05T00:00:00Z",
    "alternative_counts": [
      {"provider": "crossref", "count": 53},
      {"provider": "semantic_scholar", "count": 59}
    ],
    "referenced_works_count": 29,
    "related_works_count": 10,
    "counts_by_year_available": true
  }
}
```

The graph should distinguish three question-like node types:

- **`question`** — a canonical/shared question that may aggregate similar questions from multiple sources. It should include a canonical label, variants, origin, question type, root status, confidence, extraction rationale, key terms, user-alignment note, score, and score components. Question types may include `empirical`, `methodological`, `theoretical`, `policy`, `interpretive`, `comparative`, `measurement`, `intervention`, `equity`, or `gap`.
- **`source_question`** — a literal or inferred question from one source. It should include the source ID, question text, origin, connection type, evidence basis, access level, confidence, quote IDs, and canonicalization notes.
- **`next_question`** — a possible follow-up question generated by narrowing a parent question, substituting a slot, following an explicit research gap, or responding to user intent. It should include parent question/theme IDs, slot substitutions, generation basis, rationale, confidence, and whether it is ready to launch as a new inquiry. In the user interface, call these “possible next questions,” not “candidate branches.”

Any question-like node (`question`, `source_question`, or `next_question`) may have `root_status: primary_user_root | inquiry_root | none`. The original user question is normally the `primary_user_root`; future runs may promote a `next_question` or any other question-like node to an `inquiry_root`. The visualization can style root nodes differently.

### `edges`

Every edge must have an ID, source node ID, target node ID, relation type, evidence IDs where applicable, basis, confidence, and provider/provenance fields.

Useful edge types include:

| Direction | Relation types |
|---|---|
| source → source_question | `asks`, `infers`, `raises`, `reviews` |
| source_question → question | `supports`, `variant_of` |
| question → question | `relates_to`, `refines`, `generalizes`, `specifies`, `contrasts_with`, `co_occurs_with` |
| question → next_question | `proposes`, `narrows_to`, `extends_to` |
| question/next_question → theme | `member_of`, `proposed_for` |
| source → source | `cites`, `similar_to`, `contrasts_with` |
| source → metadata node | `informs`, `uses`, `studies`, `located_in`, `applies_to` |

All source-to-source-question edges require at least one quote or an explicit metadata-derived rationale. Source-question-to-question edges record how a specific source question supports or becomes a variant of a canonical question. Question-to-question and question-to-next-question edges may use co-occurrence, shared source, citation, shared concept, explicit language, or slot substitution as their basis, and must record that basis.

### `quotes`

Every quote should include:

```json
{
  "quote_id": "quote_001",
  "source_id": "src_001",
  "text": "exact quoted sentence or passage",
  "locator": "abstract, findings section, page, URL, or other location",
  "access_level": "full_text | abstract_only | publisher_description | metadata_only",
  "evidence_basis": "full_text_machine_readable | abstract_and_metadata | publisher_description_and_toc | metadata_only",
  "confidence": "high | medium | low",
  "provenance": {}
}
```

Quotes must preserve the source’s wording. Whitespace normalization is acceptable only if the run records that normalization; do not paraphrase or elide in a way that changes meaning.

### `themes`

Each theme should have both a short label and a plain-language statement:

```json
{
  "theme_id": "theme_001",
  "label": "...",
  "statement": "...",
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
  "confidence": "high | medium | low",
  "coherence_basis": "shared question | shared concept | citation relation | repeated finding | explicit framing",
  "key_terms": [],
  "coverage_summary": {},
  "rationale": "..."
}
```

Themes are topic groupings of questions, not evidence-state zones. They may include coverage counts by source, year, discipline, method, population, geography, and citation attention, but v0.1 must not assign settled/contested/emerging labels.

Theme creation should be adaptive rather than fixed. As a starting heuristic:

- In a small selected set, a single-source or single-question theme may be useful and should be kept visible with low confidence and a `single_question` or `single_source` support tier.
- In a comprehensive set, prefer at least two supporting questions or two distinct sources for a primary theme, while retaining weaker themes as exploratory and lower-confidence.
- In an exhaustive set, prefer three or more supporting questions or sources for primary themes, but do not discard weaker themes.

Record the theme-creation rule used in the run. Never imply that a single-source theme represents broad agreement. `next_question_ids` may be associated with a theme through `proposed_for`, but they do not count as source support for the theme.

### `coverage`

Record what the retrieved corpus covers and where it is thin:

- Number and share of on-topic, adjacent, and noise records.
- Question and theme counts.
- Distinct sources per question.
- Year, discipline, method, population, geography, and context distributions.
- Citation-count distributions and provider.
- Access-level and evidence-basis distributions.
- Explicit statements using the phrase “not found in retrieved coverage.”

### Validation requirements

A future validator should check:

- Required top-level fields and enums.
- Unique node, edge, quote, and theme IDs.
- All edge endpoints resolve to nodes.
- All quote source IDs and edge evidence IDs resolve.
- Every source-to-source-question edge has at least one quote or explicit metadata-derived rationale.
- Every inferred source question has at least one supporting quote or explicit metadata-derived rationale.
- Every citation count has a provider and retrieval timestamp.
- Every unsupported or uncertain claim has a confidence label.
- Coverage-gap statements use “not found in retrieved coverage.”

## 8. Question Scoring

Score questions with a transparent weighted combination. Store both the raw components and the weights used in the run.

### v0.1 default components

| Component | Default weight | Meaning |
|---|---:|---|
| `user_alignment` | 0.30 | Connection to the confirmed core question and stated scope |
| `source_support` | 0.20 | Number and quality of distinct selected sources supporting the question |
| `explicitness` | 0.15 | Average explicitness of the supporting statements |
| `citation_attention` | 0.10 | Normalized citation attention from available citation providers |
| `breadth` | 0.10 | Diversity of disciplines, methods, populations, geographies, or contexts |
| `relation_density` | 0.10 | Strength and number of relations to other questions |
| `evidence_strength` | 0.05 | Access level, direct quotation, and source-match confidence |

The weights should be stored in the run and may be tuned later. Citation data should include `cited_by_count`, provider, retrieval timestamp, and alternatives from other providers when fetched. Citation counts must never be used to infer truth, consensus, or evidence state.

Theme scoring should combine mean member-question score, number of distinct sources, relation density, breadth, and access-quality distribution. Every score should be reproducible from the stored components.

Possible next questions should not be scored as source-backed questions. Score them separately using user alignment, structural clarity, novelty, relation to observed gaps, and launch readiness. Record the generation basis and confidence. Because a possible next question has not yet been searched, citation counts are not meaningful for it.

## 9. Exploratory Findings

The PRD was informed by a small exploratory run using the heat-health prompt:

> How does extreme heat affect health and wellbeing in urban communities? I’m writing a literature review and need recent, peer-reviewed articles.

### UC Library Search / Primo PNX

Four exploratory queries returned 20 records per page:

| Query | Primo reported total | Unique DOIs on first page |
|---|---:|---:|
| Focused heat-health base query | 189 | 19 |
| Exposure/measurement component | 1,181 | 20 |
| Interventions/policy component | 11,431 | 20 |
| Vulnerable-populations component | 1,301 | 20 |

On the focused first page:

- 20 of 20 records had a DOI.
- 19 of 20 had a Primo abstract.
- 19 of 20 had subjects.
- 16 of 20 had a full-text, PDF, HTML, source, or Unpaywall-style link.

Primo PNX provides strong first-pass data: title, creators, year, format, subjects, abstract, DOI/PMID/ISSN, venue, publisher, links, open-access flag, and UC holdings context. It does not provide reliable citation counts.

### OpenAlex, Crossref, and Semantic Scholar

For a 12-DOI sample from the focused Primo page:

| Signal | Availability |
|---|---:|
| OpenAlex topic | 12 / 12 |
| OpenAlex concepts | 12 / 12 |
| OpenAlex citation count | 12 / 12 |
| OpenAlex reconstructed abstract | 10 / 12 |
| Crossref citation count | 12 / 12 |
| Crossref reference count | 12 / 12 |
| Crossref abstract | 6 / 12 |
| Semantic Scholar citation count | 12 / 12 |
| Semantic Scholar influential citation count | 12 / 12 |
| Semantic Scholar abstract | 9 / 12 |

These results support a layered enrichment design: Primo/UC Library Search for discovery and local context; OpenAlex as the primary work-level enrichment source; Crossref for DOI verification and publication metadata; Semantic Scholar as an optional citation-graph source. Because providers disagree on citation counts and abstract presence, `question_map.json` must preserve the provider for every count and abstract.

## 10. Transparency and Epistemic Rules

1. **Accurate before helpful.** The skill may not smooth over contradictions, force questions into a preferred framing, or imply more support than exists.
2. **Evidence before inference.** Every source-derived question requires a direct quote or explicit metadata-derived rationale.
3. **Access level matters.** Full text, abstract-only, publisher-description, and metadata-only evidence must be distinguished.
4. **Confidence everywhere.** Questions, edges, themes, and uncertain matches require confidence labels.
5. **Citations are not evidence states.** Citation counts describe attention and visibility, not correctness or consensus.
6. **Gaps are relative.** Missing themes must be described as “not found in retrieved coverage,” not as absent from scholarship.
7. **No PDF extraction.** PDF URLs may be captured for human retrieval, but the skill must not derive claims from extracted PDF text.
8. **No silent skips.** Every failed lookup, API skip, rate limit, or unavailable field must be recorded with its coverage consequence.
9. **The map orients; the user investigates.** The output should launch the user’s next inquiry, not replace it.

## 11. Run Artifacts

Use this artifact layout:

```text
runs/<topic-slug>/
  search-strategies.md      # human-readable search plan and decisions
  search-results.jsonl      # screened source records and enrichment data
  question_map.json         # primary graph artifact
  run-log.md                # adaptive decisions, skips, limitations, and handoff
```

The v0.1 skill may render a short plain-language preview of themes, possible next questions, and selected sources, but it must not attempt the future dashboard or interactive visualization.

## 12. Proposed Skill Structure

```text
question-map/
  PRD.md
  SKILL.md
  agents/openai.yaml
  references/
    question-map-schema.md
    question-extraction-and-scoring.md
    search-and-metadata-pipeline.md
  scripts/
    validate_question_map.py
  assets/
    question_map.template.json
```

This structure should be refined during implementation. Keep `SKILL.md` short and route detailed schema, extraction, scoring, and search guidance to references only when needed.

## 13. Roadmap

### Phase 1 — Dataset

- Implement intake, search, enrichment, question extraction, scoring, thematic synthesis, and `question_map.json`.
- Add the validator and template.
- Run focused and comprehensive test cases.

### Phase 2 — Visualization

- Use the populated `question_map.json` to determine which graph signals are reliable and visually meaningful.
- Design question, source, discipline, relation, and theme views after the dataset has been tested.
- Add a Markdown/Mermaid view and, only if justified, an interactive view.

### Phase 3 — Launch

- Add curated priority reading lists.
- Add targeted follow-up searches.
- Add verification targets and open questions for the researcher.
- Support optional handoff into `uc-library-search`, `annotated-bibliography`, or another inquiry workflow.
- Support optional inquiry launch from a theme, question, source question, or possible next question.

## 14. Open Implementation Questions

1. How aggressively should near-duplicate questions be canonicalized while still preserving source-specific wording?
2. Should citation attention use provider-specific raw counts, provider percentiles, or a log-scaled corpus normalization? The v0.1 default is corpus-normalized log scaling with provider and timestamp recorded.
3. What semantic similarity approach should generate `user_alignment` without overfitting to exact terminology?
4. Which full-text HTML formats are reliable enough for automated reading without PDF extraction?
5. How should temporary emerging topics with low citation counts be weighted against established but highly cited work? The v0.1 answer is to keep citation attention as only one of several components and record the rationale.
