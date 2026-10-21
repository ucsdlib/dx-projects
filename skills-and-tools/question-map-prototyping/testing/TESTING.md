# Question Map Testing Protocol

This protocol tests whether `question-map` produces source selections, edge relationships, themes, and visualizations that are relevant, evidence-anchored, and interpretable. It is designed to run inside TritonAI, but the acceptance decision should not be made by the same conversation that generated the map.

## Principles

1. **Separate generation from review.** The graph-generating session may validate its own file, but it must not be the sole judge of relevance or edge accuracy.
2. **Blind where possible.** Source-selection and edge reviewers should form judgments before seeing the generated graph or its rationale.
3. **Test levels separately.** A relevant source set can still have inaccurate edges; a valid graph can still be visually misleading.
4. **Preserve evidence.** Every review verdict must trace to a quote, title, abstract, metadata rationale, or explicit access-level limitation.
5. **No PDF extraction.** Use the available evidence basis and record its limits.
6. **Fail visibly.** Do not smooth over disagreement; record it and triage the root cause.
7. **Keep intake realistic.** Start with the user's raw prompt. Reviewer coverage lenses may be used to audit the resulting map, but they are not user requirements and must not be inserted into the prompt, confirmed working scope, or question graph.
8. **Run the source pipeline.** When available, use `uc-library-search` for discovery and `annotated-bibliography` for source verification, citation fidelity, access-level discipline, quotation rules, and evidence-limit reporting.

## Run layout

Create one folder per run:

```text
testing/runs/<YYYY-MM-DD>-<case-slug>/
  00-case.md
  01-intake-transcript.md
  01-reference-pool.md
  question_map.json
  search-strategies.md
  search-results.jsonl
  run-log.md
  visualizations/
  reviews/
    source-selection-review.md
    edge-adjudication-sheet.md
    theme-membership-review.md
    visualization-review.md
    run-summary.md
```

Run validation and generation from the repository root:

```bash
python3 scripts/validate_question_map.py testing/runs/<run-id>/question_map.json
python3 scripts/build_visualizations.py --graph testing/runs/<run-id>/question_map.json --output-dir testing/runs/<run-id>/visualizations
```

The optional wider-card view can be generated with `--wide-cards`, but the default review should use the explicit-source view.

## Review roles

Use at least these roles for a robust test:

- **Novice Reader:** tests orientation and plain-language comprehension.
- **Practitioner Reviewer:** tests practical usefulness, source appropriateness, and follow-up launchability.
- **Domain Expert:** tests disciplinary validity, source relevance, and conceptual overreach.
- **Search Auditor:** independently builds a reference pool and evaluates search coverage.
- **Evidence Auditor:** evaluates stated/inferred question status, quote fidelity, access level, and edge meaning.
- **Adjudicator:** resolves reviewer disagreement and records the final acceptance recommendation.

One human may hold multiple roles only if the blind-review sequence is preserved. The graph-generating conversation may serve as coordinator or technical validator, but not as the sole evaluator.

## Live test cases

Use `CASES.md` as the default matrix. The minimum robust suite is four cases:

1. novice broad urban-policy question;
2. expert technical/equity question;
3. practitioner policy/environment question;
4. mixed-expertise qualitative/humanities question.

Before expanding the suite, add cases only when they introduce a new failure mode or question type.

Case prompts are test inputs, not analyst-created research agendas. Send the **raw user prompt** to `question-map`. If a case includes **simulated user context**, reveal it only as realistic answers to the tool's clarification questions. The **confirmed working scope** should preserve the user's purpose in the user's voice; it must not become a checklist of all reviewer coverage lenses.

## Testing procedure

### Phase 0 — Prepare

1. Copy the selected case from `CASES.md` into `00-case.md`.
2. Create `01-intake-transcript.md` from `templates/intake-transcript.md`.
3. Record the raw prompt, any simulated user context, and the reviewer-only coverage lenses.
4. In the graph-generation session, present the raw prompt first. If simulated context is provided, use it only to answer clarification questions actually asked by the tool.
5. Record the confirmed working scope in the user's voice, not as an analyst-created component checklist.
6. Create the run folder and reviewer subfolder.

### Phase 1 — Independent reference pool

Before running `question-map`, the Search Auditor uses `uc-library-search` for discovery and `annotated-bibliography` conventions for verification and evidence discipline. The auditor creates an independent reference pool:

- 10–20 plausible sources, where available;
- concise APA-style citations;
- UC Library Search links;
- relevance score from 0–3;
- evidence basis and access level;
- major question component covered;
- rationale for inclusion or exclusion.

The Search Auditor should not see the generated `question_map.json`, source cards, Mermaid view, HTML view, or run log before completing this pool.

### Phase 2 — Generate and smoke-test

1. Run `question-map` from the raw prompt. Do not pass reviewer-only coverage lenses into the skill.
2. If simulated context is available, use it only when and as the tool asks clarification questions.
3. Confirm that both `uc-library-search` and `annotated-bibliography` were invoked when available, or record an explicit skip reason and coverage consequence.
4. Run the validator and visualization builder.
5. Confirm that all required artifacts are present.
6. Record validator output in the run log.
7. Confirm that no PDF extraction occurred and that access levels are explicit.

### Phase 3 — Source-selection and relevance review

The Domain Expert and Search Auditor compare the selected sources with the independent reference pool and with the confirmed working scope. They also report gaps against the reviewer-only coverage lenses, but those lenses are not pass/fail requirements by themselves.

For each selected source, record:

- citation and permalink;
- relevance score: 0 irrelevant, 1 adjacent, 2 relevant, 3 core;
- component covered;
- appropriateness for the user prompt;
- whether the source is a duplicate or weaker substitute;
- whether the recorded evidence basis supports the mapped question.

Also record:

- major components with no source;
- disciplines, methods, populations, or geographies that are missing;
- source types that are overrepresented;
- any selected source that is plausible but not appropriate for the confirmed question.

Use `templates/source-selection-review-sheet.md`.

### Phase 4 — Evidence-blind edge adjudication

The Evidence Auditor reviews source evidence before seeing the generated edges.

For each source, provide an evidence packet containing only:

- citation;
- title;
- abstract, publisher description, metadata, or quote;
- locator;
- access level and evidence basis.

The reviewer should not see:

- the generated source-question text;
- canonical-question edges;
- theme assignments;
- Mermaid or HTML visualization;
- the graph generator’s rationale.

The reviewer records, from the evidence alone:

1. the source-specific question or objective;
2. whether it is stated, inferred, raised, or reviewed;
3. which canonical questions it directly supports;
4. which canonical questions it is only conceptually related to;
5. which themes are primary and which are cross-cutting;
6. confidence and a quoted or metadata-derived rationale.

Then compare the adjudicated relationships with the generated graph.

Use `templates/edge-adjudication-sheet.md`.

### Phase 5 — Theme and question review

The Domain Expert reviews the canonical questions and theme memberships after edge adjudication, checking whether:

- the user prompt remains a framing context rather than a canonical question;
- themes do not imply containment where the evidence supports only cross-cutting relevance;
- methodological questions are not attached to every theme by default;
- narrower questions are distinguished from broader questions;
- possible next questions are not presented as source-backed findings.

Use `templates/theme-membership-review-sheet.md`.

### Phase 6 — Visualization and comprehension review

Each reviewer completes the visualization tasks without coaching:

1. identify the main research question and themes;
2. choose one question and identify a supporting source;
3. distinguish a stated question from an inferred question;
4. distinguish direct support from cross-cutting relevance;
5. identify one possible next question without mistaking it for a finding;
6. report anything visually misleading, unreadable, duplicated, or unsupported.

Review both the default Mermaid view and the interactive HTML view. Also check the linear Markdown companion as an accessible fallback.

Use `templates/visualization-review-sheet.md`.

## Scoring

### Source relevance

Use:

- **Source precision:** selected sources rated 2–3 divided by all selected sources.
- **Reference recall:** independently identified core sources included in the generated map divided by all core sources in the reference pool.
- **Confirmed-scope coverage:** major components implied by the confirmed working scope and covered or explicitly marked weak/not found divided by all such components.
- **Reviewer-lens coverage:** a non-gating gap report against the reviewer coverage lenses recorded in the case file.
- **Appropriateness:** sources judged suitable for the confirmed question and user context.
- **Multi-question fidelity:** sources with defensible relationships to more than one canonical question are represented without forcing one arbitrary mapping or overstating every link as direct support.

### Edge validity

For each edge, classify as:

- `exact` — generated relationship matches the evidence and reviewer judgment;
- `defensible` — reasonable interpretation, but not the strongest available mapping;
- `overclaimed` — presented as stronger or more direct than the evidence supports;
- `understated` — evidence supports a stronger relationship than the graph records;
- `unsupported` — no quoted or metadata-derived basis;
- `missing` — reviewer identified a defensible relationship absent from the graph.

Report at minimum:

- direct support precision and recall;
- stated/inferred agreement;
- secondary-link overclaim rate;
- theme-membership agreement;
- unsupported edge count.
- intake realism: whether the confirmed scope preserves the raw prompt and simulated context without adding reviewer-only lenses.

### Provisional gates

A run may be accepted for the next test iteration when:

- referential validation passes;
- no selected source is judged irrelevant or unsupported;
- every major component in the confirmed working scope is covered or transparently marked as a gap;
- no direct support edge is judged unsupported;
- no secondary relationship is visually indistinguishable from direct support;
- source-question origin labels agree with the evidence in at least 85% of adjudicated cases;
- no theme implies containment where reviewers judge the relationship cross-cutting;
- novice reviewers can orient to the map and identify a useful next step without help;
- the user prompt appears as framing, not as an unsupported canonical question.

Do not treat a source's appearance under multiple canonical questions as an error by itself. The test question is whether each relationship has evidence and whether direct support is visually distinct from secondary relevance.

Reviewer coverage lenses may reveal gaps, but they do not by themselves fail a run unless they expose a component that was actually part of the confirmed working scope or an evidence claim that is unsupported.

These thresholds are provisional. Record them in `run-summary.md` and revise after the first full suite.

## Triage

When a review fails, classify the root cause as one of:

- search strategy or coverage;
- source selection;
- source-question extraction;
- canonicalization;
- edge semantics;
- theme membership;
- visualization layout or readability;
- validator gap;
- documentation or skill instruction gap.

For each issue, record:

1. case ID;
2. artifact and node/edge ID;
3. reviewer verdict;
4. evidence rationale;
5. likely root cause;
6. proposed fix;
7. whether it should become a regression fixture.

## TritonAI workflow

Use these constraints when running reviews in TritonAI:

- Start a fresh conversation or session for each reviewer persona.
- Give the reviewer only the persona file, case file, template, and the specific artifact needed for that phase.
- Do not give edge reviewers the generated edge list before blind adjudication.
- Do not give source reviewers the generated source list before the reference pool is complete.
- Do not let the graph-generating session summarize or defend the graph until reviews are recorded.
- The coordinator may compile scores and prepare the run summary, but the Adjudicator should make the acceptance recommendation.

## Regression loop

After each failed run:

1. fix the skill, reference, validator, or builder;
2. add a minimal fixture for the failure;
3. rerun the affected phase;
4. rerun the full suite if the change affects generation, not only rendering;
5. update this protocol when the test itself misses an observed failure.

The existing urban-heat examples are useful as smoke tests and comparison references, not as proof that a new run is correct.
