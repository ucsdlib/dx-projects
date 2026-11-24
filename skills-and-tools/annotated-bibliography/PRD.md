# Reading List Product Requirements Document

**Version:** 0.3 draft
**Date:** 2026-11-24
**Skill:** `annotated-bibliography`
**Working product name:** Reading List
**Technical and compatibility name:** `annotated-bibliography`
**Status:** Phase 2 shipped and forward-tested; this document consolidates the phase 2 PRD and the naming-migration PRD, and defines phase 3.

Progress against this document is tracked in [CHANGELOG.md](CHANGELOG.md). Detailed interaction, template, search, and annotation rules live in the skill's `references/` directory; this document owns product intent, scope, and success criteria.

## 1. Summary

Phase 2 made the skill's interaction model explicit: a focused landscape by default, modular run state, reusable response templates, and a small set of follow-up paths. It shipped 2026-10-21 and passed a forward test on 2026-10-22. Post-test work added DOI-first source-link resolution.

Phase 3 should deepen the transition from "annotated bibliography" to "reading list": a tool that adapts to the user's research purpose and intended outcomes through well-designed response templates; a non-linear, adaptive interaction that supports guided human inquiry; and explicit right-sizing of query and token effort so users know what depth they are initiating before the tool begins.

## 2. Product Naming and Positioning

The working product name is **Reading List**; `annotated-bibliography` remains the technical and compatibility name. Requests for an "annotated bibliography" remain valid activations and route to the full deep-work mode. Naming migration follows this PRD's phases:

1. **Stage 1 — Positioning (done).** Reading List appears in documentation and user-facing language; the directory and installed name stay `annotated-bibliography`.
2. **Stage 2 — Technical rename (future).** After interaction behavior is stable and forward-tested, rename the skill directory to `reading-list`, update frontmatter, references, tests, and manifest directories (`annotated-bibliography-runs` → `reading-list-runs`).
3. **Stage 3 — Compatibility.** Retain "annotated bibliography," "literature review," "sources for and against," and "what should I read" as natural-language triggers; configure an alias if the harness supports one.

Naming rules: **Reading List** for the product, **reading list** for the curated intermediate output, **annotated bibliography** for the full deep-work output, **landscape** for the initial themes-and-questions stage, **search log** for the audit mode. Never imply that a reading list is automatically comprehensive or exhaustive.

## 3. Current State

### Shipped and verified

- Landscape-first interaction model with focused-default intake, landscape, selection, deep work, refinement, and audit stages.
- Run state, test-mode manifests, stage and reference logs, and manifest validation scripts.
- Response templates for clarification, landscape, reading list, bibliography, refinement, and search log.
- Adaptive fidelity-based screening, component decomposition, breadth tiers with curation rules, book verification ladder, and documented-skip rules.
- DOI-first source-link resolution with a separate library-access link (in dev copy; not yet synced to the installed skill).
- One phase 2 forward test passed with manifest validation, provenance checks, and quote-accuracy checks.

### Open gaps from testing

- Annotations remain abstract-level; full-text retrieval for the highest-value sources is the persistent quality ceiling.
- The manifest's `breadth_tier` is descriptive; it needs separate normalized `landscape_tier` and `deep_work_tier` fields.
- The phase 2 narrowing context was simulated from `assignment-prompts.md`; a live narrowing turn has not been tested.
- The keyed Primo Search API path has not been compared against the PNX fallback on the same topic.
- The full annotated-bibliography continuation path has not been exercised end-to-end.
- The installed harness skill needs a sync from the dev copy before further testing.

## 4. Goals

1. Preserve "Faithful Over Helpful" in every stage and template.
2. Adapt output to the user's research purpose and intended outcome, not just their topic.
3. Support guided human inquiry through a non-linear, adaptive interaction.
4. Right-size query and token effort, and communicate expectations before deep work begins.
5. Keep landscape sources, themes, and questions reusable across all follow-up paths.
6. Maintain provenance, access-level labeling, and transparency requirements without exception.

## 5. Non-Goals

- Do not convert the skill into a systematic-review tool or a graphical interface.
- Do not change the UC Library Search pipeline during phase 3; improvements there follow evidence from testing.
- Do not invent research directions that are not source-backed.
- Do not define source-count ceilings as measures of comprehensiveness.
- Do not execute the technical rename in this phase (see Section 2).

## 6. Users and Jobs

| User | Job | Primary purpose |
|---|---|---|
| Exploratory researcher | Understand the shape of a broad question | Quick orientation |
| Literature-review researcher | Comprehensive, faithful source set with annotations | Publication-grade deep work |
| Instructor or student | Orientation resource for a course or assignment | Course support |
| Decision maker | Sources bearing on a specific decision or claim | Decision support |
| Skill developer or tester | Full pipeline visibility | Audit |

## 7. Phase 3 Feature Areas

### 7.1 Purpose-adaptive reading lists

The skill should recognize the user's research purpose at intake and select the response template, evidence depth, and structure that serve it. Purpose is distinct from breadth tier: it shapes *what the output is for*.

Requirements:

1. Maintain a small purpose registry in `references/response-templates.md`, initially: quick orientation, course/assignment support, literature review, decision support, and sources-for-and-against. Each purpose maps to a template variant, evidence expectations, annotation depth, and a default reading-list size guardrail.
2. Intake infers purpose from prompt markers ("for my students," "I need to write a review," "we're deciding whether...") and confirms it in one line; when ambiguous, purpose becomes one of the two-to-four material clarification questions.
3. Purpose is recorded in run state and the manifest alongside the breadth tier.
4. Each template variant adapts required elements without weakening fidelity rules: provenance, access level, confidence, evidence classification, and human next steps remain mandatory everywhere.
5. A purpose's reading-list guardrail is a reading-burden heuristic, not a completeness claim; the response states what the list is and is not.

### 7.2 Guided human inquiry

The interaction should be non-linear: the user can branch from any theme, question, or source at any time, and the skill adapts its offers accordingly.

Requirements:

1. Every landscape, reading list, and bibliography response ends with adaptive next-step offers drawn from actual run state (themes, questions, named sources, detected gaps), not a fixed menu.
2. The user may pivot at any point: combine themes, challenge a question, name a source to dig into, request comparisons, or redirect scope. The skill maps the request to a supported mode and preserves valid state.
3. Follow-up work should teach as it goes: state what the search found, what it means for the user's question, and what a human should verify or read next, in plain language.
4. Clarification is adaptive, not front-loaded only: one focused question may follow a landscape when the user's selection opens a genuine fork (for example, comparing two populations versus merging them). More than two sequential clarification turns without search is a failure.
5. The "Human Next Steps" closing remains required for deep-work outputs and should be tailored to the selected path and purpose.

### 7.3 Right-sizing query and token effort

The skill should let users choose — and clearly signal — the effort level before work begins, so a multi-minute deep run is never a surprise.

Requirements:

1. Offer a depth dialog at intake when the prompt does not make depth clear, using plain labels: **Quick** (landscape-level, seconds to a minute), **Standard** (focused landscape plus a curated reading list, a few minutes), **Deep** (comprehensive or exhaustive bibliography, potentially several minutes). Defaults: Quick or Standard for ordinary requests; Deep only on explicit request or clear markers.
2. Before any Deep run begins, state in one line what will happen and roughly how long it may take, and give the user a chance to redirect. This is an expectation statement, not a permission gate for Quick and Standard work.
3. Map depth to a query budget: Quick caps at the landscape-sufficiency signals; Standard adds targeted component queries as needed; Deep runs the full tool pipeline. Log the budget and any overruns in the manifest.
4. Keep search-log verbosity out of default responses at every depth; the audit mode remains opt-in.
5. Add normalized effort fields to the manifest: `landscape_tier`, `deep_work_tier`, `effort_mode`, and actual-versus-budgeted query counts.

## 8. Testing Plan

Phase 2 tests (from the prior PRD, still pending where noted): live narrowing turn after a landscape; full bibliography continuation; scope refinement; search-log audit; failure paths; narrow-scope bypass. The keyed Primo Search API versus PNX comparison also remains open.

Phase 3 adds:

1. **Purpose-inference test:** run the same fresh topic under each purpose marker; verify template selection, guardrails, and expectation language.
2. **Non-linear interaction test:** from one landscape, branch from a theme, then a specific source, then redirect; verify state preservation and adaptive offers.
3. **Effort-signaling test:** issue a Deep request; verify the expectation statement appears before search, the budget is logged, and actual-vs-budgeted queries are recorded.
4. **Clarification-discipline test:** count sequential clarification turns across several scenarios; more than two without search fails.

## 9. Success Criteria

### Functional

1. A fresh question moves intake → landscape → follow-up without restart, and can branch non-linearly without losing state.
2. Purpose and depth are recorded in run state and shape the response template and guardrails.
3. A Deep run states its expectation before beginning and logs budget vs. actual effort.
4. All phase 2 success criteria continue to hold (provenance, no invented controversy, one primary next-step question after landscape, search log on demand, manifest completeness).

### Quality

1. No source-backed claim lacks provenance; no generated direction appears source-backed.
2. No annotation relies on remembered or unverified content; access level is always stated.
3. No skip, fallback, or coverage limitation is silent.

### Usability

1. A user can identify the next available path within one screen of any response.
2. A user initiating deep work knows it will take minutes, not seconds, before it starts.
3. Clarification never exceeds four material questions before search, or two sequential turns after a landscape.

## 10. Decisions and Open Questions

Decisions carried forward: landscape default with documented exceptions; focused-then-deep sequencing; in-conversation state with test-mode manifests; purpose-aware landscape sufficiency; adaptive reading-list budgets; research directions labeled separately; rich audit detail in experimental phase; comparative table at three or more empirical sources.

Open questions for phase 3 testing:

1. Which purpose categories earn their own template variants, and which can share one?
2. Do Quick/Standard/Deep labels communicate well to students versus researchers, or should depth language follow the existing tier vocabulary?
3. Should a Standard reading list ever trigger one supplementary comprehensive pass, or stay strictly within the landscape set?
4. How should the effort budget respond when adaptive screening finds unexpectedly rich results mid-run?
5. Does the harness support skill-name aliases for the eventual `reading-list` rename?
