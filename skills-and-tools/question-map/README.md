# Question Map

`question-map` is an experimental Codex skill for mapping the questions embedded in a scholarly literature landscape. It produces a quote-anchored, machine-readable graph rather than a conventional literature summary.

**Current status:** Phase 1 — dataset construction. Visualization and inquiry-launch workflows are deferred to later phases.

The skill is designed to compose with `uc-library-search` and `annotated-bibliography`. It uses UC Library Search as the preferred first discovery pathway, applies fidelity-driven screening and theme-based “search within” strategies, enriches records with scholarly metadata APIs, and preserves source-specific wording, access level, confidence, and provenance throughout.

## Primary artifact

Each run writes to `runs/<topic-slug>/`:

```text
search-strategies.md      # human-readable search plan and decisions
search-results.jsonl      # screened source records and enrichment data
question_map.json         # primary graph artifact
run-log.md                # adaptive decisions, skips, limitations, and handoff
```

`question_map.json` contains:

- `question` nodes for canonical/shared research questions;
- `source_question` nodes for literal or inferred questions from individual sources;
- `next_question` nodes for possible follow-up questions;
- `source` nodes for selected or candidate sources;
- `theme` nodes with short labels and plain-language statements;
- edges, quotes, metadata nodes, coverage summaries, and limitations.

The graph is intended to support later question-network visualizations, but Phase 1 does not include a dashboard or interactive view.

## Repository layout

```text
SKILL.md                                             # skill entrypoint and workflow
PRD.md                                               # product requirements and design history
agents/openai.yaml                                   # UI metadata and invocation policy
assets/question_map.template.json                    # starter artifact template
references/search-and-metadata-pipeline.md           # search, screening, enrichment, and selection
references/question-extraction-and-scoring.md        # question extraction, themes, and scoring
references/question-map-schema.md                    # question_map.json schema and invariants
scripts/validate_question_map.py                     # graph validator
```

## Usage

Invoke the skill explicitly:

```text
Use $question-map to map the research questions around this prompt: [research question].
```

Or:

```text
$question-map - [research question].
```

The skill may also activate implicitly for requests to map questions, build a question landscape, create thematic question clusters, or construct structured data for a question-network visualization.

## Validation

After building a graph, run:

```bash
python3 scripts/validate_question_map.py runs/<topic-slug>/question_map.json
```

The validator checks required top-level fields, enums, IDs, edge endpoints, quote evidence, theme support, citation metadata, and “not found in retrieved coverage” phrasing.

To validate the skill structure itself:

```bash
python3 ~/.tritonai-harness/codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## Scope and guardrails

The skill is intended to orient and foster inquiry, not replace it. It does not answer the research question, synthesize the literature, classify questions as settled/contested/emerging, or use citation counts as evidence of correctness. It records whether evidence came from full text, abstracts, publisher descriptions, or metadata only. It does not extract text from PDFs.

See `PRD.md` for the full product requirements, exploratory findings, schema rationale, and roadmap.

## Creation note

This experimental Phase 1 skill was developed iteratively by Doug Worsham with TritonAI (GLM 5.3 Flash) assistance. Doug supplied the initial concept, scope decisions, example research question, exploratory bibliography, and successive redirects; the model drafted the PRD, skill instructions, reference guides, template, and validator. The work is shared in an exploratory state for testing and experimentation purposes only. 
