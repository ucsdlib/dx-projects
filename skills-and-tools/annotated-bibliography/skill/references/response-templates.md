# Response Template Reference

Templates are required-element contracts, not canned prose. Select the template that matches the current stage and response type before writing, and default to it unless the request clearly fits none; if no template fits, adapt deliberately and note the deviation in the manifest when one exists. Adapt wording to evidence and omit a section only when it genuinely does not apply. Use plain language in user-facing responses; keep API and query detail in the search log unless the user asks for it.

## Plain-Language Rules

These rules govern all user-facing text. They are fidelity requirements, not style preferences: a user who cannot understand the response cannot verify it.

1. **Open with interpretation.** Every substantive response begins by restating the working question or questions as you understand them (plural is allowed) and one line on how you will proceed. Never open with bookkeeping.
2. **Write for the user, not the pipeline.** Never use internal vocabulary in user-facing text: landscape, manifest, breadth tier, fidelity, PNX, component decomposition, run state. Say "overview of the research" or "initial overview" for the landscape stage; describe tiers and search effort in plain words ("a quick pass," "a comprehensive search").
3. **Transparency means consequences, not mechanisms.** When a limitation matters, state what it means for the user's conclusions and what they should do about it. Technical detail (API names, endpoints, query syntax, execution state, count reliability) belongs in the search log or manifest only.
4. **Uncertainty is labeled, not narrated.** Mark estimates as approximate. Where access is limited, say so with its implication and next action: "These summaries are based on article abstracts rather than the full texts. Read the full articles to confirm findings before citing them." Do not add meta-commentary about count reliability unless it changes what the user can conclude.
5. **Bookkeeping is silent.** Never open with manifest, validation, or file-save notices. When outputs were written to files, mention locations once at the end in plain terms.
6. **The search log is on request.** Do not include it in default next-step offers. When the user asks for it, render the audit; if it must be named in conversation, call it "a detailed record of how I searched."
7. **Plain language governs wording, not structure.** Never omit required template elements for brevity or readability. Overviews keep theme headings, folded questions, representative readings, and find-more links. Reading lists and bibliographies keep the full annotation block: full citation, source ID, study design, access level, confidence, and key quotes. Condensing wording is good; condensing evidence is not.

## Clarification

Use when the initial prompt is ambiguous.

1. One-line statement of how you are interpreting the request and the working question.
2. What is already understood.
3. Two to four concise questions with concrete options.
4. A note that unanswered questions will receive sensible defaults.

## Initial Landscape

```markdown
## Summary

**Research question:** [Concise restatement]

**Context:** [Optional concise statement of material clarifications]

### Search strategy

[Plain-language overview of the search approach in user terms: what was searched, roughly how much was reviewed, and how sources were chosen. Label estimates as approximate. If a limitation matters, state its consequence for the user in plain language. Keep API names, endpoints, execution states, and count-reliability commentary out of this section.]

#### Example searches

- [Search name](UC Library Search link) [number of results, approximate on-topic share]
- [Search name](UC Library Search link) [number of results, approximate on-topic share]
[Describe searches as what was searched, not execution mechanics. If a prepared search was not run, omit it here and record it in the search log.]

## Overviews

[One sentence on what these are for, when overviews exist: "These take a broad view of the whole topic."]

- [Title, Author(s), Year](Primary source link) [Plain-language description, using abstract wording where possible]

## Themes

[One-sentence descriptive introduction.]

### [Theme name as a heading]

[One- to two-sentence description grounded in retrieved sources.]

**Questions explored in this theme:** [One to two concise questions, phrased with this theme's emphasis. A question may appear in several themes with different phrasing; keep provenance in run state.]

**Representative readings:**

- [Title, Author(s), Year](Primary source link) [One-sentence plain-language description]
- [Two to three representative readings per theme when the evidence supports them; at least one.]

[Find more on this theme: [structured UC Library Search link] — introduced with a plain-language phrase such as "Search for more on this theme:"]

## Possible directions

[One-sentence introduction framing these as openings the user could explore, when generated directions would help.]

- **[Direction name]** [What the user could explore here and why it might matter for their research. Base it on an explicit source gap, recurring pattern, or user context, and phrase it as a possibility for the user's research — not a proposal, a next step, or a claim about the field.]

## What's next?

[Short offer of reading list, full annotated bibliography, refinement, or another user-defined path. Do not mention the search log unless the user has asked for it.]
```

Requirements:

- Include three to eight themes when the evidence supports that many; never manufacture themes to fill a quota.
- Themes describe the retrieved landscape; they are not analytical claims about the field.
- Every theme has at least one source in run state.
- Fold source-backed questions into their themes with theme-specific phrasing; a question may appear in more than one theme. Every question retains at least one example source and full provenance in run state, even though the user-facing Questions table is gone.
- Include two to three representative readings per theme when the evidence supports them, plus one structured "find more" search link per theme.
- Keep generated directions clearly separated from theme questions, and phrase them as possibilities for the user's research rather than proposals or claims about the field.
- Add a transparency line, in plain language, when UC Library Search was skipped, a limitation materially affects coverage, or results are unusually weak. State the consequence for the user's conclusions; leave mechanism detail to the search log.
- Estimate fidelity conservatively and label it approximate.

## Reading List

```markdown
[One- to two-sentence plain-language introduction that restates the working question and how you are proceeding. Never open with bookkeeping.]

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
- Open by restating the working question and how you are proceeding, then a summary using the same transparency and search-strategy principles as the landscape. Follow the plain-language rules throughout.
- Close with human next steps.

The full bibliography remains deep work. Do not collapse it into the shorter reading-list format unless the user asks for condensed output.

## Refinement

Use when the user changes scope, narrows a theme, combines themes, or requests a different perspective.

1. Plain-language restatement of how you are interpreting the changed request and the working question.
2. What still applies from the earlier overview, in user terms ("the sources and themes from your first overview still apply"), never internal state language.
3. What will be newly searched or discarded.
4. Whether search depth has changed, in plain words.
5. A short result summary, using the overview format when results materially change the landscape.
6. One next-step question.

## Search Log

Use only when the user asks for it; never include it in default next-step offers. Include:

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
