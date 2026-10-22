# Response Template Reference

Templates are required-element contracts, not canned prose. Adapt wording to evidence and omit a section only when it genuinely does not apply. Use plain language in user-facing responses; keep API and query detail in the search log unless the user asks for it.

## Clarification

Use when the initial prompt is ambiguous.

1. One-line statement of the working question.
2. What is already understood.
3. Two to four concise questions with concrete options.
4. A note that unanswered questions will receive sensible defaults.

## Initial Landscape

```markdown
## Summary

**Research question:** [Concise restatement]

**Context:** [Optional concise statement of material clarifications]

### Search strategy

[Plain-language overview of search approach, tools used, number of queries, total sources found and screened, and number selected.]

#### Example searches

- [Search name](UC Library Search link) [number of results, approximate on-topic share]
- [Search name](UC Library Search link) [number of results, approximate on-topic share]

## Overviews

[Optional one-sentence introduction if relevant overviews exist.]

- [Title, Author(s), Year](Primary source link) [Plain-language description, using abstract wording where possible]

## Themes

[One-sentence descriptive introduction.]

1. **Theme name:** [One- to two-sentence description grounded in retrieved sources.]

## Questions

| # | Question | Related themes | Example sources |
|---|---|---|---|
| 1 | [Concise question?] | [Theme names] | [APA short citation](Primary source link) |

## Possible directions

[Optional one-sentence introduction if generated next-step questions would help the user.]

1. **[Generated question?]** [Why this direction may be useful; base it on an explicit source gap, recurring pattern, or user context. Label it as proposed, not source-backed.]

## What's next?

[Short offer of reading list, full bibliography, refinement, search log, or another user-defined path.]
```

Requirements:

- Include three to eight themes when the evidence supports that many; never manufacture themes to fill a quota.
- Themes describe the retrieved landscape; they are not analytical claims about the field.
- Every theme has at least one source in run state.
- Every source-backed question identifies at least one example source.
- Keep generated directions out of the Questions table and label them separately.
- Add a transparency line for UC Library Search skip, fallback, materially limited coverage, or unusually weak results.
- Estimate fidelity conservatively and label it approximate.

## Reading List

```markdown
[One- to two-sentence plain-language introduction.]

## [Descriptive title of key finding]

**Citation:** [Full APA 7th edition with DOI or URL]  
**Source ID:** [Stable run-state ID]  
**Source Type:** [Article, book, book chapter, dissertation, policy report, etc.]  
**Connection Type:** [Direct evidence, reasonable inference, interpretive connection, or user-defined]  
**Study Design:** [Include when known or relevant]  
**Evidence Base:** [Sample, data, methods, limitations, when available]  
**Credibility:** [Peer review, venue, author expertise, scholarly press, citations, limitations acknowledged]  
**Access Level:** [Full text reviewed, abstract only, publisher description and table of contents reviewed, metadata only]  
**Confidence:** [High, medium, or low]

**Library access:** [Optional UC Library Search / Primo link; include when a DOI is not present or when holdings and resolver access are useful.]

[One or two sentences explaining relevance to the selected theme or question. Stay close to explicit source statements and use direct quotes when possible.]

### Questions this source addresses

- [Question one]
- [Question two]

### Key quotes

- “[Direct quote one]”
- “[Direct quote two]”

### Comparison

[Optional. Include when three or more empirical sources compare usefully.]

| Source | Study design | Focus | Key claim or finding | Access and confidence |
|---|---|---|---|---|
| [APA short citation](DOI or URL) | [Study design] | [Population, context, or intervention] | [Explicit claim, using a direct quote when possible] | [Access level, confidence] |

---

[Closing sentence offering next steps.]
```

Requirements:

- Default to sources already selected for the chosen theme or question.
- If fewer than two useful sources are available, perform at most one targeted supplementary search before asking whether to continue.
- Label adjacent sources and their connection type; do not inflate the list.
- Use direct quotes for key claims whenever available text supports them.
- Use adaptive source budgets: two to five for a narrow path, five to eight for a single broad theme, and eight to twelve for a multi-theme or overview list. These are reading-burden guardrails, not comprehensiveness measures. Purpose, user preference, and evidence availability may raise or lower them.
- If evidence is unavailable, say what is missing rather than fill the section with inference.
- Preserve full annotation rules for confidence, access level, and verification.
- Use the source-link resolution rules in search-and-selection.md: prefer a DOI for the primary user-facing link, then library or native record links, and keep a separate UC Library Search / Primo access link when available.
- Include the comparison table when three or more empirical sources are present and comparison improves scannability.

Illustrative comparison layout:

| Source | Study design | Focus | Key claim or finding | Access and confidence |
|---|---|---|---|---|
| [Author A et al. (2023)](DOI or URL) | Mixed-methods study | Library workflow adoption | “Staff reported that the workflow reduced duplicate review, but training time was a barrier.” | Abstract only; medium |
| [Author B and Author C (2024)](DOI or URL) | Comparative case study | Two academic libraries | “Both sites linked success to earlier subject-librarian involvement.” | Full text reviewed; high |

## Full Annotated Bibliography

Use the structure in [annotation-rules.md](annotation-rules.md). In addition:

- Include a source ID from run state.
- Link related theme and question IDs where helpful.
- Open with a summary using the same transparency and search-strategy principles as the landscape.
- Close with human next steps.

The full bibliography remains deep work. Do not collapse it into the shorter reading-list format unless the user asks for condensed output.

## Refinement

Use when the user changes scope, narrows a theme, combines themes, or requests a different perspective.

1. One-line restatement of changed scope.
2. What remains valid from the prior run.
3. What will be newly searched or discarded.
4. Whether the breadth tier changed.
5. A short result summary, using the landscape format when results materially change the landscape.
6. One next-step question.

## Search Log

Use only as an explicit audit mode. Include:

1. Working question and scope.
2. Breadth tier and selection basis.
3. UC Library Search execution mode: Primo Search API, PNX REST API fallback, or documented skip.
4. Tool order and number of searches per tool.
5. Each query, purpose, pages screened, fidelity estimate, and resulting decisions.
6. Component decomposition and facet slices.
7. Adaptive refinement events.
8. Verification outcomes and metadata conflicts.
9. Selected, excluded, and pruned sources, with reasons.
10. Access, coverage, fallback, and evidence limitations.

During the experimental phase, err toward completeness: include screened-record inventory, per-page classifications, and candidate-level decisions in the manifest or search log. Optimize later for efficiency and token use.

Use tables and compact bullets. The log may be long because it is an audit artifact.
