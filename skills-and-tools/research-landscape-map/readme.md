# research-landscape-map — skill overview

**Status:** v0.1.1 prototype — internal experimentation. Not yet researcher-facing.

A skill that treats library collections as data and turns a research question into a
**sourced landscape map**: what is well understood, contested, emerging, and not found in
retrieved coverage — across geography, populations, contexts, methods, time, disciplines,
and emergent aspects (components, frameworks, lenses, sub-questions).

## What it produces

Each run writes to `runs/<topic-slug>/`:

| File | What it is |
|---|---|
| `search-strategies.md` | Human-facing search plan: goals, copy-paste queries, links, rationale, glossary, strengths/weaknesses |
| `search-results.jsonl` | Structured records (metadata, abstracts, HTML full text when machine-readable) |
| `landscape.json` | The landscape data model (schema v0.1) — visualization-agnostic, every claim anchored |
| `landscape-dashboard.md` | Human-facing visualization: quadrant, coverage matrix, geography/population, chronology, methods, takeaways, gaps, module rationale |

## How it works (five stages)

1. **Intake & refine** — clarify the question into a topic spec (concepts, synonyms, scope, constraints).
2. **Search** — runs the `uc-library-search` workflow (up to 5 strategies); API-first lookups (Crossref → structured HTML → Primo pages); no PDF extraction.
3. **Capture** — persists all artifacts to disk; no in-context-only state.
4. **Interpret & synthesize** — extracts dimensions, discovers aspects, assigns evidence states and confidence, detects gaps under the epistemic contract.
5. **Render** — module selection via `scripts/module_select.py`, dashboard per template, `landscape.json` validated by `scripts/validate_landscape.py`.

Two-tier fidelity: structural claims come from metadata/abstracts (Tier 1); "well understood"/"contested"
claims require full text actually read (Tier 2, top 10 per major zone). Gaps are always phrased
"not found in retrieved coverage" — never proof of absence.

## Folder layout

- `SKILL.md` — the agent-facing instructions (the contract; the source of truth for behavior).
- `readme.md` — this human-facing overview.
- `agents/openai.yaml` — UI metadata (name, blurb, default prompt).
- `references/` — `landscape-data-model.md` (schema), `aspect-discovery.md` (method),
  `module-registry.md` (visualization modules + selection rule), `dashboard-template.md`
  and `search-strategies-template.md` (plain-language output structures).
- `scripts/` — `validate_landscape.py` (schema + integrity), `module_select.py` (deterministic
  module selection with reasons).

## Usage

In a TritonAI session with network access (the search stage hits UC Library Search and Crossref):

```text
Use $research-landscape-map to map the research landscape for my question:
[research question].
```

The skill composes with `uc-library-search`; it deliberately does **not** replace it.

## Install / update

```bash
cp -R /Users/d2worsham/TritonAI/research-process/research-landscape-map ~/.tritonai-harness/codex/skills/
diff -r /Users/d2worsham/TritonAI/research-process/research-landscape-map ~/.tritonai-harness/codex/skills/research-landscape-map
```

Validate structure after edits:

```bash
python3 ~/.tritonai-harness/codex/skills/.system/skill-creator/scripts/quick_validate.py research-landscape-map
```

## Development notes

- **Plain language by rule:** human-facing outputs must be plain-language, define terms,
  state decisions with rationale, and disclose strengths/weaknesses and limitations (SKILL.md
  hard rule 9; enforced by the output templates).
- **Reference examples:** `runs/extreme-heat-urban-communities/` holds illustrative baseline
  examples (mock, pre-Run-1) — they show prose style, not live results.
- **Known revision queue:** the post-Run 1 clarifications (aspect-kind decision rule, normative
  depth-selection procedure, `topic_spec` spec, Crossref lookup notes) are captured in the
  planned `post-run1-revisions.md` for the repo root; apply after Run 1 evidence lands.
- **Validation fixtures:** `validate_landscape.py` and `module_select.py` are regression-tested
  against valid/broken/sparse fixtures before each release of the skill.
