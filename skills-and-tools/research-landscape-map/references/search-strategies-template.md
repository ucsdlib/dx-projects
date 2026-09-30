# Search Strategies Template — `search-strategies.md`

`search-strategies.md` is the human-facing record of the search stage. Write it in **plain
language**: a scholar who has never used this tool should understand what was searched, why,
and what it means. Define terms on first use and include a glossary. State every decision with
its rationale, and be transparent about strengths, weaknesses, and limits.

This template is topic-agnostic. Use `[bracketed placeholders]` for run-specific content; never
put real-topic content in the template text itself.

## Required structure

### 1. Header
Topic slug, date, skills/versions used, status (e.g., "verified live run" / "illustrative"),
and a link to the sibling `landscape-dashboard.md`.

### 2. What this document is (plain-language intro)
Explain in 2–4 sentences what a search strategy is: a plan for asking the library's collections
questions through deliberate queries; that every query is reproducible (copy-paste query + link);
that discovery is built on metadata (catalog facts, abstracts, full-text links).

### 3. Working interpretation (the topic spec)
Table of the Stage 1 agreement, with one-line plain-language definitions of each field:
- `concepts` — the core ideas of the question.
- `synonyms` — alternative words the literature uses for those ideas.
- `scope` — one-line statement of what is being covered.
- `constraints` — deliberate boundaries chosen (dates, populations, geography, peer-reviewed only).
Add one line: why these constraints were chosen.

### 4. Glossary
Starter list — define each in plain language, then add any term the intended reader would ask about:
boolean operators (`AND`/`OR`/`NOT`), phrase search (quotes), truncation (`*`), parentheses/grouping,
field codes (`any`, `title`, `sub`, `creator`), filter/facet, peer-reviewed, search scope (all ten
UC campuses by default), result count (an estimate — validate by scanning), DOI, Crossref, abstract,
full text, metadata, deduplication, screening.

### 5. Strategy table
One row per executed strategy, columns:
`Strategy` | `Goal (plain language)` | `Copy-paste query` | `Link` | `Filters` | `Approx. results (validate by scanning)` | `What we're looking for`

### 6. Decisions & rationale
Bullets covering at minimum:
- Why this number of strategies (each query reflects one framing/vocabulary; N deliberate angles).
- Filter choices (e.g., peer-reviewed, material type) and why.
- Date range and its tradeoff (recent-first keeps currency; may under-represent foundational work).
- Parentheses around every `OR` group — `AND` binds before `OR` on this Primo instance (verified);
  always group synonyms as `(A OR B) AND C`.
- Field choices (e.g., `any` for core, `title`/`sub` for probes).
- Any deliberate gap-probing queries — state the hypothesis being tested (sparse results are
  information, recorded later as a labeled gap, never as proof of absence).

### 7. Screening & depth-read plan
- Screening cap: 20–30 records per strategy.
- All screened records receive Tier-1 capture (metadata + abstract).
- Depth-read records are marked `read: true`, and each is listed with **why it was chosen**
  (e.g., corroborated by multiple strategies, review/high-yield type, needed to represent a zone,
  side of a contested question, or region/population coverage, HTML full-text availability).
- Tier-2 claims (well understood / contested) come only from depth-read records.

### 8. Strengths & weaknesses
Of the approach as used in this run: reproducibility, auditable claims, fidelity labels,
API-first efficiency, gap-awareness — and the limits: estimated counts, screening-cap scope,
metadata/coverage gaps (gray literature, datasets, books), language/scope bias, abstract-derived
proxy tags.

### 9. Limits & next steps
Validate high-value results by opening them; dedupe across strategies; citation chaining from
reviews; options for alerts, reference-manager export, wider scope, or additional languages.
