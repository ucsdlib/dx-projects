# Annotated Bibliography: Next Phase Product Requirements Document

**Version:** 0.2 draft  
**Date:** 2026-10-21  
**Skill:** `annotated-bibliography`  
**Working product name:** Reading List  
**Technical and compatibility name:** `annotated-bibliography`  
**Primary focus:** modular interaction, follow-up, and response rendering  
**Related skill:** `uc-library-search`

## 1. Summary

The next phase should make the annotated bibliography skill easier to navigate without weakening its fidelity-first engine. The current skill reliably builds search strategies, executes UC Library Search first, uses adaptive screening and component decomposition, verifies sources, and produces faithful annotations. Its principal weakness is that the interaction model is largely implicit. A user can receive a useful bibliography, but the skill does not consistently show the major themes and questions first, learn from the user's research interests and preferences, offer relevant, specific paths forward, or render different stages of work through reusable response patterns.

This phase will introduce a modular conversation framework. It will preserve the existing search, verification, and annotation behavior while adding a structured landscape stage, a small set of follow-up paths, stable run state, and reusable response templates. The user should be able to move from an initial question to a landscape, a reading list, a full bibliography, a refinement, or an audit without restarting the run or losing source provenance.

### Product naming and positioning

The working product name is **Reading List**. This better expresses the intended outcome: preparing and supporting human reading, analysis, and next research decisions. `annotated-bibliography` remains the technical and compatibility name during this phase. Requests for an “annotated bibliography” should continue to activate the skill and may route to its full deep-work mode. The current PRD does not execute a directory, invocation, or artifact rename; see `PRD-naming-migration.md` for that future phase.

## 2. Current State

### Working well

- UC Library Search is the first discovery pathway.
- Search strategies are created through the `uc-library-search` skill.
- Search uses the Primo Search API when a key is available and the PNX REST API as the documented fallback.
- Adaptive screening classifies on-topic, adjacent, and noise records by page fidelity.
- Component decomposition surfaces sources buried in broad rankings.
- Verification happens before annotation.
- Adaptive refinement responds to search signals instead of fixed result counts.
- Direct quotes and explicit connection classifications keep annotations faithful.
- The skill treats themes as descriptive and avoids manufactured controversy.
- The full search log is available for testing or detailed auditing.

### Needs improvement

- The conversation has no clear state model, so large runs can lose their structure between stages.
- Clarification and follow-up rules are dispersed across the skill rather than centralized.
- The user often cannot see the research landscape before committing to a full bibliography.
- Themes and questions are not consistently offered as reusable paths for follow-up.
- Reading lists, full annotations, search audits, and refinement responses need stable output shapes.
- The default response can be too much for users who need orientation, not a complete bibliography.
- Provenance between query, source, theme, question, and response is implicit rather than systematic.

## 3. Goals

1. Preserve “Faithful Over Helpful” throughout every interaction stage.
2. Let users see a high-level landscape before choosing deeper work.
3. Make the primary interaction stages modular: intake, landscape, selection, deep work, refinement, and audit.
4. Reduce repeated questions and clarify once, with a small number of high-value questions.
5. Give each theme and question explicit source provenance.
6. Render common outputs through reusable response templates.
7. Keep the full search log out of the default response while making it available as an explicit mode.
8. Support follow-up reading lists built from already selected sources, with optional targeted supplementary search.
9. Maintain accessibility, source accuracy, and transparency as core quality requirements.
10. Enable forward testing against fresh research questions.

## 4. Working Assumptions

1. The existing search, verification, and annotation engine should remain stable during this phase.
2. The landscape stage is the default first search stage for most ordinary requests. It is a lightweight orientation step, not a substitute for a comprehensive or exhaustive bibliography.
3. The landscape should be skipped when the request is already narrowly scoped to the level of a research paper, when the user explicitly asks for a complete annotated bibliography without a landscape, or when a re-run provides a complete scope brief.
4. The initial landscape runs at the focused level. Subsequent reading lists, bibliographies, and deep dives run at the tier selected by the user or inferred from explicit prompt markers.
5. Templates constrain required evidence and ordering, not wording. Templates will be stored in the skill's `references` directory.
6. The MVP should maintain in-conversation state. A persistent run manifest is required in test mode and optional elsewhere.

## 5. Non-Goals

- Do not change the UC Library Search pipeline or demote other reliable APIs until testing supports a change.
- Do not convert the skill into a full systematic-review tool.
- Do not invent research directions that are not source-backed.
- Do not force every result into a theme or question.
- Do not produce a graphical interface in this phase.
- Do not make abstract-level claims behave like full-text findings.
- Do not treat citation counts or relevance ranking as measures of truth.
- Do not create a separate database or external service.
- Do not define source-count ceilings as measures of comprehensiveness or exhaustiveness.

## 6. Primary Users and Jobs

### Exploratory researcher

The user has a broad question and wants to understand the shape of the literature. They need themes, questions, and a path to a short reading list before they commit to a full bibliography.

### Literature-review researcher

The user already knows the scope and needs a comprehensive source set with faithful annotations. They care about coverage, methods, limitations, credibility, and direct evidence.

### Instructor or student

The user needs an orientation resource for a course or assignment. They need short, plain-language summaries, credible starting points, and clear next steps.

### Skill developer or tester

The user is evaluating the pipeline. They need the full search log, query decisions, fidelity, skips, fallbacks, and pruning rationale without turning off the user-facing output model.

## 7. Interaction Model

### 7.1 Run state

Every invocation should maintain a lightweight run state during the conversation. It need not become a required external file in the MVP, but it must be stable enough to render follow-ups and audit summaries.

Minimum state fields:

| Field | Purpose |
|---|---|
| `run_id` | Distinguishes one run from another in the same session. |
| `working_question` | The concise question or topic the skill is actually addressing. |
| `context` | Clarifications, audience, discipline, time frame, source-type constraints, and other scope inputs. |
| `breadth_tier` | Focused, comprehensive, or exhaustive, with its selection basis. |
| `output_mode` | Landscape, reading list, full bibliography, search log, refinement, or undefined. |
| `queries` | Query text, tool, purpose, page count, fidelity, and decisions. |
| `sources` | Stable source ID, citation, permalink, access level, source type, study design, evidence base, credibility, confidence, and connection type. |
| `themes` | Stable theme ID, plain-language name, descriptive summary, related source IDs, and support confidence. |
| `questions` | Stable question ID, question text, related theme IDs, supporting source IDs, and confidence. |
| `selected_paths` | Follow-up actions the user has chosen. |
| `limitations` | Access, coverage, fallback, pruning, and evidence limitations. |
| `stage_log` | Ordered record of major workflow transitions. |
| `reference_log` | Model-reported record of reference files consulted and decisions they informed. |

The skill should retain source IDs across stages so a reading list can say which sources came from which query, belong to which themes, and support which questions.

#### Run state versus run manifest

| Approach | Benefits | Costs | Recommended role |
|---|---|---|---|
| In-conversation state | No filesystem side effects; low implementation overhead; fast for short runs; easy to keep user-facing responses clean | Can be lost through context compression or new turns; hard to inspect and replay; long runs consume context; search-log reconstruction can become unreliable | Always use as the active state |
| Run manifest | Durable and inspectable; supports replay, testing, provenance review, and post-run comparison; separates machine state from user-facing output | Adds file management, schema maintenance, cleanup, and privacy considerations; can create stale files or versioning questions | Required in test mode; optional by user request or for comprehensive and exhaustive deep runs |

A run manifest should be canonical, machine-readable state, not a second source of truth. The user-facing search log may be derived from it. In test mode, the skill should create a manifest such as `annotated-bibliography-runs/<run_id>/bibliography-run.json` and optionally a human-readable `search-log.md` in the same directory. If no output directory is supplied, use the current working directory and clearly tell the user where files were written.

Manifest minimum content:

1. `schema_version`, `run_id`, creation and update timestamps.
2. Working question, scope brief, and breadth-tier decision.
3. Query records with tool, text, purpose, pages screened, fidelity estimates, and adaptive decisions.
4. Source records with stable IDs, full citations, permalinks, access level, source type, study design, evidence base, credibility, confidence, connection type, and linked queries.
5. Theme and question records with stable IDs, provenance, supporting source IDs, and support type.
6. Selection, exclusion, and pruning decisions.
7. Coverage, access, fallback, skip, and evidence limitations.
8. `stage_log` entries for intake, landscape, selection, deep work, refinement, and audit.
9. `reference_log` entries for reference files that informed workflow, templates, search, annotation, or API decisions.

The MVP may serialize state at checkpoints rather than after every record. It must not let manifest maintenance override fidelity, verification, or user-facing responsiveness.

### 7.2 Clarification policy

Use the following rules before search:

1. If the initial prompt contains enough scope to search responsibly, proceed without clarification.
2. If clarification is needed, ask two to four concise questions in one turn.
3. Ask only for material information: refined question, discipline, time frame, perspective, research output, intended audience, source-type constraints, or breadth.
4. Offer a default or concrete option whenever possible.
5. Do not ask about tier and clarification separately unless necessary.
6. If the user declines to answer, proceed with the recommended default and record the basis.

Recommended intake questions:

- “Do you want a quick overview, an annotated reading list, or an exhaustive survey?”
- “Should the search prioritize recent work, historical work, empirical studies, theory, policy, or a mix?”
- “Should it include practitioner and policy sources, or focus primarily on scholarly work?”
- “Is there a discipline, population, geography, or time period that must be included or excluded?”

The response should open with a one-line working question and state that the user may correct it. If no questions were necessary, state the working question, constraints, and chosen tier in one line and proceed.

### 7.3 Primary stages

Each stage should have a clear input, responsibility, and output. The responsibilities may live in one skill file or in referenced guidance, but the model should be explicit.

| Stage | Input | Responsibility | Output |
|---|---|---|---|
| Intake | User prompt and context | Confirm scope and choose breadth | Working question and scope brief |
| Landscape | Scope brief and UC Library Search strategy | Screen a focused result set and map themes and questions | Landscape response and run state |
| Selection | Landscape response | Offer reusable follow-up paths | User-selected path |
| Deep work | Selected path and existing source set | Produce reading list, bibliography, or targeted expansion | Requested output with provenance |
| Refinement | Scope change | Preserve valid state and search incrementally | Updated landscape, reading list, or bibliography |
| Audit | User request or test mode | Reconstruct the full pipeline | Search log |

#### Stage 1: Intake

Build a working question and scope brief. Confirm material constraints. The default depth path is: focused landscape first, then user-selected deep work at comprehensive or exhaustive breadth. Prompt markers such as “quick,” “brief,” “literature review,” “thorough,” “publication-grade,” or “research paper” may override the default. If the request is already narrowly scoped to a research-paper-level question, skip the broad landscape and use the selected tier directly.

Do not begin full bibliography work until the user has seen the initial landscape or explicitly says to proceed directly to a full bibliography. Record whether the landscape was selected, skipped by scope judgment, skipped by user instruction, or bypassed by an explicit full-run request.

#### Stage 2: Initial landscape

Run a focused UC Library Search pass first. Use the current Primo Search API and PNX fallback rules, adaptive screening, and query refinement. Keep this stage deliberately small enough to orient the user.

Required landscape work:

- Identify major themes in the on-topic and adjacent results.
- Identify questions the retrieved sources explicitly ask or clearly imply.
- Identify strong overviews, reviews, meta-analyses, scoping reviews, or bibliometric analyses when present.
- Record source provenance for each theme and question.
- Record search fidelity, adaptive decisions, and fallbacks in the internal run state.
- Stop the landscape when it has enough coverage to describe major themes and questions, not when every relevant source has been found.
- Do not produce the full annotated bibliography at this stage unless the user explicitly asks for it.

#### Stage 3: User selection

Present the landscape and offer paths forward. The user may choose one or more existing themes or questions, combine them, name a new theme or question, request a full bibliography, refine scope, or request the search log.

#### Stage 4: Follow-up work

Use the selected path to run one of the supported follow-up modes. If the selected path remains at the landscape level, reuse the landscape source set. If it narrows to a specific theme or question, reuse relevant landscape sources first, then run targeted searches at the selected breadth tier. A broad reading list may be a curated subset of the landscape; it must not be presented as exhaustive unless the user explicitly requests exhaustive work and the search supports that claim.

#### Stage 5: Refinement or audit

If scope changes, preserve useful state and run an incremental search rather than a full restart. If the user requests an audit, render the complete search log mode.

### 7.4 Follow-up paths

The initial landscape should end with a short navigation offer containing these options:

1. **Reading list:** Select one or more themes or questions.
2. **Full annotated bibliography:** Produce the complete fidelity-first bibliography.
3. **Refine scope:** Narrow, broaden, reframe, add constraints, or redirect the search.
4. **Search log:** Show the full pipeline and audit details.
5. **User-defined path:** Ask for another theme, question, comparison, output, or source set.

The offer should use ordinary prose or a short list, not a rigid menu that prevents other requests. The skill should accept any reasonable follow-up, but internally map it to one of the supported modes.

### 7.5 Asking after the landscape

After the landscape, ask one open-ended question such as:

> Which theme or question is most useful to explore first? I can create a reading list, move directly to a full annotated bibliography, refine the search, or show the search log.

Do not repeatedly ask for confirmation when the user has already named a path. Do not ask tier again unless the user requests a materially different scope.

## 8. Response Templates

Templates are rendering contracts. They define required elements and ordering, not canned prose. Every response must adapt to the evidence and should omit a section only when it genuinely does not apply.

### 8.1 Template: clarification

Use when the initial prompt is ambiguous.

Required elements:

1. One-line statement of the working question.
2. What is already understood.
3. Two to four concise questions with concrete options.
4. A note that unanswered questions will receive sensible defaults.

The template should avoid technical vocabulary, field codes, Boolean syntax, and API terminology unless the user asks about the strategy.

### 8.2 Template: initial landscape

```markdown
## Summary

**Research question:** [Concise restatement]

**Context:** [Optional concise statement of material clarifications]

### Search strategy

[Plain-language overview of the search approach, tools used, number of queries, total sources found and screened, and number selected.]

#### Example searches

- [Search name](UC Library Search link) [number of results, approximate on-topic share]
- [Search name](UC Library Search link) [number of results, approximate on-topic share]

## Overviews

[Optional one-sentence introduction if relevant overviews exist.]

- [Title, Author(s), Year](UC Library Search permalink) [Plain-language description, using abstract wording where possible]

## Themes

[One-sentence descriptive introduction.]

1. **Theme name:** [One- to two-sentence description grounded in retrieved sources.]

## Questions

| # | Question | Related themes | Example sources |
|---|---|---|---|
| 1 | [Concise question?] | [Theme names] | [APA short citation](UC Library Search permalink) |

## Possible directions

[Optional one-sentence introduction if generated next-step questions would help the user.]

1. **[Generated question?]** [Why this direction may be useful; base it on an explicit source gap, recurring pattern, or user context. Clearly label it as a proposed direction, not a source-backed finding.]

## What's next?

[Short offer of reading list, full bibliography, refinement, search log, or another user-defined path.]
```

Requirements:

- Include three to eight themes when the evidence supports that many. Do not manufacture themes to fill a quota.
- Themes must be descriptive of the retrieved landscape, not analytical claims about the field.
- Each theme should have at least one source in the run state.
- Each question should identify at least one example source.
- Do not present a generated question as source-backed unless a retrieved source explicitly asks or clearly implies it.
- Keep generated research directions outside the Questions table and mark them as proposed directions.
- Include a transparency line if UC Library Search was skipped, fallback occurred, coverage is materially limited, or results are unusually weak.
- Estimate fidelity conservatively and label it as approximate.

### 8.3 Template: reading list

```markdown
[One- to two-sentence plain-language introduction.]

## [Descriptive title of key finding]

**Citation:** [Full APA 7th edition with DOI or URL]  
**Source Type:** [Article, book, book chapter, dissertation, policy report, etc.]  
**Study Design:** [Include when known or relevant]  
**Evidence Base:** [Sample, data, methods, limitations, when available]  
**Credibility:** [Peer review, venue, author expertise, scholarly press, citations, limitations acknowledged]  
**Access Level:** [Full text reviewed, abstract only, publisher description and table of contents reviewed, metadata only]  
**Confidence:** [High, medium, or low]

[One or two sentences explaining relevance to the selected theme or question. Stay close to explicit source statements. Use direct quotes when possible.]

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
- If fewer than two useful sources are already available, perform at most one targeted supplementary search before asking the user whether to continue.
- Do not inflate a reading list by adding adjacent sources without labeling their connection type.
- Use direct quotes for key claims whenever the available text supports them.
- Use adaptive source budgets. A narrowly scoped reading list may need only two to five sources. A single broad theme may warrant five to eight. A multi-theme or overview-level reading list may warrant eight to twelve. These are reading-burden guardrails, not measures of comprehensiveness. User preferences, purpose, and evidence availability may raise or lower them. If a broad request cannot be covered exhaustively, say so rather than implying a complete source set.
- If evidence is unavailable, say what is missing rather than filling the section with inference.
- Preserve the full annotation rules for confidence, access level, and verification.
- Include the compact comparison table when three or more empirical sources are present and comparison would help the user distinguish methods, populations, findings, and limitations.

### 8.4 Template: full annotated bibliography

Continue using the current annotation structure. Add:

- A source ID from the run state.
- A stable link to related theme and question IDs where helpful.
- An opening summary using the same transparency and search-strategy principles as the landscape template.
- A closing set of human next steps.

The full bibliography remains the deep-work mode. It should not collapse into the shorter reading-list format unless the user asks for condensed output.

### 8.5 Template: refinement

Use when the user changes scope, narrows a theme, combines themes, or requests a different perspective.

Required elements:

1. One-line restatement of the changed scope.
2. What remains valid from the prior run.
3. What will be newly searched or discarded.
4. Whether the breadth tier has changed.
5. A short result summary, using the landscape format when the results materially change the landscape.
6. One next-step question.

Incremental refinement should avoid rerunning unchanged queries. New results compete with existing sources under the same tier and curation rules.

### 8.6 Template: search log

The search log is an explicit audit mode, not the default response. It should include:

1. Working question and scope.
2. Breadth tier and its selection basis.
3. UC Library Search execution mode: Primo Search API, PNX REST API fallback, or documented skip.
4. Tool order and number of searches per tool.
5. Each query, its purpose, pages screened, fidelity estimate, and resulting decisions.
6. Component decomposition and facet slices.
7. Adaptive refinement events.
8. Verification outcomes and metadata conflicts.
9. Selected, excluded, and pruned sources, with reasons.
10. Access, coverage, fallback, and evidence limitations.

During the current experimental phase, err toward completeness: include an inventory of screened records, per-page classifications, and candidate-level decisions in the manifest or search log. Optimize this later for efficiency and token use after the interaction model stabilizes.

This mode should use tables and compact bullets. It may be long because it is an audit artifact.

## 9. Search and Selection Rules

### 9.1 Landscape pass

The initial landscape should use a focused UC Library Search pass. It may use a zoom-out ladder or component queries when the first query has low fidelity. It is not the comprehensive bibliography pass.

Use a landscape-sufficiency check rather than a fixed query budget:

1. **Concept coverage:** every core concept in the working question has at least one on-topic source or is explicitly documented as absent from retrieved coverage.
2. **Perspective coverage:** major intended perspectives, such as empirical, theoretical, practitioner, policy, historical, or recent work, have a source or documented gap.
3. **Theme saturation:** recent pages and component searches are mostly mapping sources into known themes rather than revealing new themes.
4. **Question novelty:** recent sources mostly answer or refine existing questions rather than producing a stream of previously unseen source-backed questions.
5. **Candidate stability:** additional high-confidence candidates are strengthening known themes rather than creating a competing landscape.
6. **Fidelity:** the adaptive screening rule permits stopping and the query is not materially biased toward one concept or source type.
7. **Purpose fit:** a quick overview can stop earlier than a comprehensive survey. The tier, user language, and expected depth should calibrate the stopping point.

As a practical signal, if two consecutive high-fidelity pages or component searches introduce no new theme or source-backed question, treat the landscape as saturated for the current purpose. If more than about one third of a recent page supports a new theme or question, continue searching or run a targeted component query. These signals are heuristics; they must be logged, not treated as proof of complete coverage.

If the user explicitly asks for a complete bibliography and no landscape, the skill may skip the landscape and run the selected breadth tier directly.

### 9.2 Additional tools

After the landscape, use the existing tool pipeline when the selected path requires broader coverage. UC Library Search remains first. Additional tools should improve coverage, verification, or citation chaining rather than merely inflate source count.

### 9.3 Source selection

Sources should be selected by:

1. Direct relevance to the selected theme or question.
2. Explicitness of the evidence.
3. Source type, method, and perspective diversity.
4. Access level and verification basis.
5. Contribution to coverage of the selected path.
6. Confidence and credibility.
7. Value for the user’s next research step.

A strong new source may replace a weaker source on the same theme. Record pruning rationale.

### 9.4 Themes

Themes are descriptive groupings of retrieved sources. They may include on-topic and adjacent evidence when adjacency is labeled. Do not treat a theme as a consensus or claim. Theme support should be marked as direct, inferred, or interpretive when the distinction matters to the response.

### 9.5 Questions

Questions should be drawn from one of three origins:

| Origin | Rule |
|---|---|
| Source-backed | The source explicitly asks or clearly implies the question. |
| User-defined | The user asks the question during intake or follow-up. |
| Research-direction | The skill identifies a gap or productive next line, clearly labeled as generated rather than source-backed. |

Research-direction questions are generated by the skill, not asked by a source and not supplied by the user. They may help the user see a productive next move, such as narrowing a broad theme, testing a named source limitation, or comparing two methods. They should appear only in a clearly labeled “Possible directions” section or closing offer. They should not appear in the source-backed Questions table and must never be represented as claims about what the literature asks or studies.

## 10. Fidelity and Transparency Requirements

1. Direct quotes are preferred for key claims and must preserve context.
2. Inference beyond the source must be labeled.
3. Interpretive connections must not appear as direct evidence.
4. Metadata-only sources should carry low confidence and no content claims beyond metadata.
5. Publisher descriptions must not be presented as independent evaluation.
6. Abstract-level evidence must be labeled as abstract-level.
7. Null findings, missing evidence, and coverage gaps must be reported.
8. If UC Library Search is skipped, the reason and expected coverage consequence must be stated in the opening summary and search log.
9. Relevance ranking and citation counts are discovery aids, not evidence of correctness.
10. Source disagreements and absence of controversy must be reported honestly.

## 11. Accessibility and Output Quality

Every user-facing response should:

- Use plain-language section names.
- Explain technical concepts when necessary.
- Avoid result-count claims that imply precision when counts are estimates.
- Use semantic Markdown headings and accessible tables.
- Use descriptive link text, not bare URLs.
- Keep link text consistent across the same source where possible.
- Avoid walls of unstructured text.
- Offer a concise alternative when the full output becomes long.

The default landscape should remain scannable. Long evidence and audit details belong in the search log or full bibliography.

## 12. Success Criteria

### Functional success

1. A fresh research question can move from intake to landscape to at least one follow-up without restarting the run.
2. An ordinary broad or moderately scoped request begins with a focused landscape unless the user explicitly bypasses it or the question is already research-paper scoped.
3. Each landscape theme has at least one source-backed record in run state.
4. Each source-backed question has at least one example source and theme linkage.
5. A reading list can reuse prior source IDs, citations, permalinks, access levels, and confidence ratings.
6. A scope refinement preserves useful prior state and records the reason for new or retained sources.
7. A search-log request renders the full pipeline without changing the default response mode.
8. A test-mode run produces a machine-readable manifest with schema, query, source, theme, question, selection, and limitation records.

### Quality success

1. No source-backed claim lacks provenance to a retrieved source.
2. No theme is presented as analytical consensus.
3. No generated question appears as source-backed.
4. No annotation relies on remembered or unverified source content.
5. No API failure, skip, fallback, or filter limitation is silent.
6. No response invents controversy or hides disagreement.

### Usability success

1. A user can identify the next available path in less than one screen of the landscape response.
2. Clarification questions are absent when the prompt is already clear.
3. Clarification does not exceed four material questions before search.
4. After the landscape, the skill asks only one primary next-step question.
5. A user can request a search log at any point after search begins.

## 13. Testing Plan

### Test 1: Forward landscape test

Use a fresh research question unrelated to prior controlled runs.

Evaluate:

- Clarification frequency and quality.
- Whether the default landscape is used for an ordinary request.
- Whether the focused landscape pass yields useful themes and questions.
- Whether every theme and question has provenance.
- Whether the landscape-sufficiency signal is useful, premature, or excessive.
- Whether generated directions are visually distinct from source-backed questions.
- Whether the next-step offer is clear.
- Whether the user can choose a reading list from prior sources.
- Whether the test-mode manifest contains the expected state.

### Test 2: Reading-list continuation

From the landscape in Test 1, select one theme and one question.

Evaluate:

- Reuse of prior sources.
- Whether new supplementary search is proportionate.
- Access-level labeling.
- Direct quote accuracy.
- Whether the source relevance stays close to explicit source statements.
- Whether the comparative table appears when three or more empirical sources are present and whether it improves scannability without oversimplifying evidence.

### Test 3: Full bibliography continuation

From the same run, request a comprehensive bibliography.

Evaluate:

- Whether the landscape sources carry forward.
- Whether additional tool use is justified.
- Whether the final set honors the breadth tier and curation rule.
- Whether annotations meet the existing fidelity standard.
- Whether pruned sources and rationale are documented.

### Test 4: Refinement test

Narrow the question, change time frame, or add a new perspective.

Evaluate:

- Whether prior state is preserved.
- Whether unchanged queries are avoided.
- Whether new and existing sources are curated consistently.
- Whether the response clearly says what remains valid and what changed.

### Test 5: Search-log audit

Request the search log at the end.

Evaluate:

- Completeness of tool, query, fidelity, screened-record, fallback, skip, verification, pruning, and limitations data.
- Whether the log explains coverage consequences.
- Whether the user-facing response remains separate from the audit detail.
- Whether the manifest is sufficient to reconstruct the run and reproduce the search log.

### Test 6: Failure-path test

Run with UC Library Search unavailable or with a deliberately weak query.

Evaluate:

- Documented skip and expected coverage consequence.
- Query refinement behavior.
- Honest weak-evidence reporting.
- Whether the response avoids forcing a bibliography from inadequate sources.

### Test 7: Narrow-scope bypass

Use a request already scoped to a research-paper-level question.

Evaluate:

- Whether the skill skips the broad landscape and searches the selected tier directly.
- Whether the working question and tier are stated before search.
- Whether the absence of a landscape improves or harms usefulness.

## 14. Implementation Milestones

### Milestone 1: Interaction skeleton

Add the run-state model, stage definitions, clarification policy, and navigation paths to the skill. Keep existing search behavior unchanged.

### Milestone 2: Landscape and templates

Implement the focused landscape stage and initial response template. Add rules for theme and question provenance.

### Milestone 3: Follow-up modes

Implement reading lists, refinement, search-log mode, and full-bibliography continuation.

### Milestone 4: Forward tests

Run the seven tests above on at least two fresh questions. Capture examples, strengths, failure cases, and template improvements.

### Milestone 5: Revision and release

Revise templates and interaction rules from test findings. Update README, creation note, and testing artifacts. Validate the focused-landscape default and narrow-scope exception before broader use.

## 15. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Templates make responses formulaic | Treat templates as required-element contracts, not fixed prose. Allow omission of nonapplicable sections. |
| Theme generation becomes interpretive synthesis | Require source provenance and keep themes descriptive. |
| Questions become speculative | Separate source-backed, user-defined, and research-direction questions. |
| Landscape stage adds latency | Keep it focused and clearly distinct from comprehensive search. Allow direct full-bibliography requests. |
| Run state is lost across turns | Standardize stable IDs and require the skill to restate the working question before deep work. |
| Manifests clutter the workspace | Create manifests by default only in test mode or by user request, use a predictable directory, and document cleanup behavior. |
| Search log bloats every response | Make it an explicit audit mode only. |
| Reading lists mix weak sources with strong sources | Label connection type, access level, and confidence. |
| User corrections break the run | Preserve prior state, mark changed scope, and run incremental refinement. |
| API fallback changes coverage silently | Report fallback, skip reason, and expected coverage consequence. |
| Template length overwhelms users | Prioritize scannability and offer condensed output when requested. |

## 16. Decisions and Future Considerations

### Decisions for this phase

1. **Landscape default:** Use the focused landscape by default for most ordinary requests. Exceptions are research-paper-scoped questions, explicit full-bibliography requests, and complete re-run briefs.
2. **Depth sequencing:** Run the landscape at focused level first, then run selected deep work at comprehensive or exhaustive level. Clear prompt markers may override the default sequence.
3. **State:** Maintain in-conversation state for the active run. Require a machine-readable manifest in test mode and make it optional by user request or for deep runs.
4. **Landscape sufficiency:** Use purpose-aware saturation signals rather than a fixed query budget.
5. **Reading-list size:** Use adaptive source budgets tied to scope, purpose, and evidence availability rather than a fixed ceiling.
6. **Research directions:** Keep generated directions out of the source-backed Questions table and label them separately.
7. **Search log:** Include rich record-level detail during the experimental phase, including screened records and per-page classifications, to support testing and audit.
8. **Comparative table:** Include a compact table when a reading list has three or more empirical sources and comparison improves scannability.

### Bookmarked for a later phase

1. Optimize search-log verbosity to reduce token use once the interaction model and manifest schema are stable.
2. Design versioning, saved-output behavior, and return-to-run workflows for users who revisit a run after several turns.

### Remaining questions for testing

1. Does the proposed landscape-sufficiency signal stop too early for interdisciplinary or rapidly evolving topics?
2. Should the manifest write to the current working directory, a user-specified directory, or a conventional project directory?
3. Should a broad overview-level reading list use only the landscape set by default, or should it trigger one additional comprehensive pass before display?
4. How much comparative detail belongs in the reading-list table before it competes with the per-source annotations?

## 17. Recommendation

The next phase should not begin by changing the search engine. It should begin by making the interaction model explicit. A focused landscape, reusable templates, stable run state, and a small set of follow-up modes will make the skill more useful while preserving its strongest asset: a bibliography the user can trust.

## Appendix A: Comparative Table Example

This is an illustrative rendering, not a real run. Use it as a layout model for three or more empirical sources in a reading list.

| Source | Study design | Focus | Key claim or finding | Access and confidence |
|---|---|---|---|---|
| [Author A et al. (2023)](DOI or URL) | Mixed-methods study | Library staff adopting a new workflow | “Staff reported that the workflow reduced duplicate review, but training time was a barrier.” | Abstract only; medium |
| [Author B and Author C (2024)](DOI or URL) | Comparative case study | Two academic libraries | “Both sites linked success to earlier subject-librarian involvement.” | Full text reviewed; high |
| [Author D et al. (2025)](DOI or URL) | Quasi-experimental study | Student-facing service pilot | “The pilot reported improved completion rates, though the sample was limited to one campus.” | Abstract only; medium |

Use direct quotes where the retrieved abstract or full text supports them. When the evidence does not permit a quote, summarize only the source’s explicit statement and mark the lower access level.
