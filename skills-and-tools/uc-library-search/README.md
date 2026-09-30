# UC Library Search Skill (`uc-library-search`)

A TritonAI/Codex skill that builds high-fidelity search strategies for **UC Library Search**
(Primo VE) and generates direct, clickable search links for the UCSD instance
(`search-library.ucsd.edu`).

Adapted from the TritonGPT "UC Library Search Query Generator" system prompt, preserving its
values-based approach: never summarize literature; ask clarifying questions first, scaled to
the request (2–4 for open or novice requests, 0–1 to fill a material gap for detailed or
expert requests); target balanced precision and recall; and always deliver a direct search
link, copy-paste query, advanced-search instructions, alternative strategies, and a
plain-language explanation.

## Usage

Invoke with `$uc-library-search` or `/uc-library-search`, or ask it to build a literature
search — e.g., "Use $uc-library-search to build a search strategy for my literature review on
social media and adolescent depression."

URL mechanics were verified live against `search-library.ucsd.edu`; links use the verified
single-parameter `query=` format, and `scripts/build_url.py` builds them deterministically so
encoding is never hand-rolled. Run `python3 scripts/build_url.py --self-test` to check the
builder.

## Files

- `SKILL.md` — core workflow and behavioral constraints
- `references/primo-ve-syntax.md` — verified Primo VE syntax, encoding rules, filters, pitfalls
- `references/response-template.md` — required output layout with a worked example
- `scripts/build_url.py` — deterministic search-link builder (stdlib only) with `--self-test`
- `references/az_databases.json` — normalized visible UCSD A-Z database metadata
- `references/az_databases.csv` — CSV version of normalized A-Z data
- `scripts/fetch_az_api.py` — harvests A-Z data via the Springshare API (requires local `.env` credentials)
- `scripts/normalize_az_api.py` — converts raw API export into normalized JSON and CSV
- `scripts/recommend_databases.py` — ranks A-Z database candidates from user concepts and optional subject/type filters
- `agents/openai.yaml` — harness UI metadata
- `.testing-log.md` — hidden testing/reference log (ignored by standard agent file discovery)

## Installing

```bash
cp -R uc-library-search ~/.tritonai-harness/codex/skills/
```

Skills load on the next turn or session.

## Examples

```bash
python3 scripts/build_url.py '("social media" OR Facebook) AND (depression OR "depressive symptoms") AND (adolescent* OR teenager*)' --filters peer_reviewed --filters articles --filters 2018-2026
```

## Creation record

**Work identification**
- Title: UC Library Search skill (`uc-library-search`)
- Type: TritonAI/Codex skill — Markdown guidance, Python helper script, documentation
- Date: 2026-09-15 (v1.0)
- Audience: UC San Diego Library digital experience team and the TritonAI/Codex harness
- Stage: Finalized

**Human contribution summary**
- **Doug Worsham** — Digital Experience Manager, UC San Diego Library
  - Roles: Conceptualization, Methodology, Writing – Original Draft (with Claude), Supervision
  - Contribution: researched and authored the source system instructions (co-authored with
    Claude) covering high-fidelity search best practices and Primo VE syntax; set the
    values-based requirements (no literature summarization, staged clarifying workflow, balanced
    precision/recall); directed the technical-accuracy work; and made the product decisions —
    needs-based clarifying questions, verified single-parameter URL format only, filtered URL
    variants, and placement in `dx-tools` for team sharing
- Initial testing by Doug Worsham, created as an experiment. Further testing and experimentation needed.

**AI contribution summary**
- Contribution: AI-Assisted (multi-party) — human-authored framework with substantial AI
  implementation and verification
- AI systems and roles:
  - **Claude (Anthropic; version unspecified)** — co-authored the source TritonGPT system
    prompt with Doug: research into search-query best practices, Primo VE syntax drafting,
    and workflow design (Writing – Original Draft)
  - **Codex (OpenAI Codex CLI harness, served via TritonAI as `api-deepseek-v4-flash`)** —
    adapted the system prompt into a skill package: authored `SKILL.md`, `references/`, and
    `scripts/build_url.py`; performed live URL verification against `search-library.ucsd.edu`
    (Technical Documentation, Software, Validation/Testing and QA)
- Prompt characterization: iterative with human source material — Doug's expert-authored
  system prompt was the source; multiple directed rounds refined structure, content, and policy


**Process narrative**
The tool began as a TritonGPT system prompt Doug co-authored with Claude, defining how an
assistant should build UC Library Search strategies. Before adapting it, the Codex agent
verified the prompt's URL-construction claims live against `search-library.ucsd.edu`,
confirming the single-parameter `query=` format, field codes, and filter parameters — and
discovering that the prompt's chained-parameter example URLs mis-execute on the live instance.
That evidence set the technical baseline for the skill.

The Codex agent then restructured the prompt into the skill package — core workflow in
`SKILL.md`, a verified syntax reference, a response template with a worked example, and a
deterministic URL builder script with self-tests — under Doug's direction. Doug reviewed the
testing results, refined the clarifying-question policy to scale with request detail, and
approved sharing the skill through this repo. Testing evidence is logged in
`.testing-log.md`.

