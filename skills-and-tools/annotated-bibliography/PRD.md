# Reading List Product Requirements Document

**Version:** 0.4 draft
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

2026-11-24 update from user testing: "landscape" is internal vocabulary. User-facing text calls the stage an "overview of the research" or "initial overview." The search log is available on request only and does not appear in default next-step offers; it primarily serves testing and audit. All user-facing output follows a plain-language contract: open by restating the working question(s), no internal vocabulary, limitations stated as consequences with next actions, and bookkeeping kept silent (see the Plain-Language Rules in `skill/references/response-templates.md`).

## 3. Current State

### Shipped and verified

- Landscape-first interaction model with focused-default intake, landscape, selection, deep work, refinement, and audit stages.
- Run state, test-mode manifests, stage and reference logs, and manifest validation scripts.
- Response templates for clarification, landscape, reading list, bibliography, refinement, and search log.
- Adaptive fidelity-based screening, component decomposition, breadth tiers with curation rules, book verification ladder, and documented-skip rules.
- DOI-first source-link resolution with a separate library-access link (synced to the installed skill 2026-11-24), plus the version-of-record citation-year rule (2026-11-24).
- Plain-language contract and template-defaulting safeguard, validated in live behavior across three rounds of automated multi-turn testing (2026-11-24): live narrowing turns, reading-list narrowing, full-bibliography continuation, and effort right-sizing markers all exercised.
- One phase 2 forward test passed with manifest validation, provenance checks, and quote-accuracy checks.

### Open gaps from testing

- Annotations remain abstract-level; full-text retrieval for the highest-value sources is the persistent quality ceiling.
- The manifest's `breadth_tier` is descriptive; it needs separate normalized `landscape_tier` and `deep_work_tier` fields.
- Manifest hygiene is inconsistent under behavioral variance: the round 3 S03 quick pass created no manifest and its escalation logged only intake, failing validation. A validation gate before final responses is needed.
- An explicit user source count was not treated as binding (round 3 S02 delivered 16 sources against a requested 8-10); the curation rule needs a user-cap override with documented rationale.
- Effort curves are inverted for urgent requests: the round 3 S03 "quick" pass took 11 min 13 s while the same session's comprehensive escalation took 4 min 46 s. See Section 7.4.
- The keyed Primo Search API path has not been compared against the PNX fallback on the same topic.

## 4. Goals

1. Preserve "Faithful Over Helpful" in every stage and template.
2. Adapt output to the user's research purpose and intended outcome, not just their topic.
3. Support guided human inquiry through a non-linear, adaptive interaction.
4. Right-size query and token effort, keep the first response fast, and communicate expectations before deep work begins.
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

### 7.4 Fast first round (timing progressive disclosure)

Progressive disclosure has a timing dimension: sessions should start fast, and later turns grow with the work the user actually commits to — they may even be faster than the first round when state is reused. Round 3 (S03) made the case for this directly: a "quick" request took 11 min 13 s while the same session's comprehensive escalation took 4 min 46 s. Filesystem evidence rules out the simple explanation (the escalation avoiding queries by reusing state): the escalation ran roughly sixteen new searches across three APIs plus its own 820 KB Crossref verification batch in under five minutes, while the quick pass ran one landscape query and a 209 KB verification batch — and still took over twice as long. The quick pass's cost was dominated by serial, per-source verification and careful annotation composition, not query volume. An initial response in the ten-minute range will be off-putting for many users, especially students and first-contact sessions, even when the eventual output is strong. The remedy is therefore not fewer queries overall; it is cheaper-per-source work in the first round, with verification deferred until the user commits.

The concept: the first reply to any new question is a **fast first round** — substantive, source-backed, and deliberately provisional — with deeper verification deferred until the user commits to a direction. This composes with the other phase 3 areas: quick-orientation purposes (7.1) map naturally to it; fast, provisional content invites early steering in guided inquiry (7.2); and it is the mechanism that makes 7.3's "Quick: seconds to a minute" label true instead of aspirational.

Requirements:

1. **First-substantive-response target.** The first reply to a new question arrives within about a minute (search execution time permitting). It contains real content — the working question, initial themes or candidate sources — not a placeholder or a pure plan.
2. **Verification on commit.** Crossref checks, quote extraction, and confidence calibration are deferred to the turn where the user selects a direction or source set. The fast first round labels provisional items in plain language (access level, "details verified once you pick a direction") so honesty is never sacrificed for speed.
3. **Duration tracks stated urgency, not a fixed depth rule.** Later turns may legitimately run faster than the first — state reuse and batched execution are the reuse dividend, not a failure. The failure to avoid is a first round whose cost ignores the user's stated urgency (a "handful of sources, skim tonight" request paying comprehensive-verification prices). Where verification must happen upfront (the user needs a citable list immediately), the expectation statement says so before work begins.
4. **Interim messages remain the fallback, not the fix.** Live progress notes are required for any turn expected to exceed roughly two minutes, but the fast first round reduces the need for them by arriving quickly.
5. **Fidelity is not negotiable for speed.** The fast first round never presents unverified metadata as verified, never inflates source counts (see the S02 user-cap finding), and never drops the plain-language limitation statement. Speed comes from deferring work, not from silent thinning.
6. **Timing is auditable.** The manifest records the first-response duration (or whether the target was met) and any verification-deferral decisions, so timing regressions surface in testing rather than in user complaints.

## 8. Testing Plan

Phase 2 tests (from the prior PRD, still pending where noted): live narrowing turn after a landscape; full bibliography continuation; scope refinement; search-log audit; failure paths; narrow-scope bypass. The keyed Primo Search API versus PNX comparison also remains open.

Phase 3 adds:

1. **Purpose-inference test:** run the same fresh topic under each purpose marker; verify template selection, guardrails, and expectation language.
2. **Non-linear interaction test:** from one landscape, branch from a theme, then a specific source, then redirect; verify state preservation and adaptive offers.
3. **Effort-signaling test:** issue a Deep request; verify the expectation statement appears before search, the budget is logged, and actual-vs-budgeted queries are recorded.
4. **Clarification-discipline test:** count sequential clarification turns across several scenarios; more than two without search fails.
5. **Fast-first-round test:** on a fresh topic, time the first substantive reply (target: about a minute, provisional labeling present); then escalate in the same session and verify state preservation and that the first round's duration tracks the user's stated urgency rather than a fixed verification depth.

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
4. The first substantive reply to a new question arrives within about a minute; any expected longer turn says so before it starts.

## 10. Decisions and Open Questions

Decisions carried forward: landscape default with documented exceptions; focused-then-deep sequencing; in-conversation state with test-mode manifests; purpose-aware landscape sufficiency; adaptive reading-list budgets; research directions labeled separately; rich audit detail in experimental phase; comparative table at three or more empirical sources.

Open questions for phase 3 testing:

1. Which purpose categories earn their own template variants, and which can share one?
2. Do Quick/Standard/Deep labels communicate well to students versus researchers, or should depth language follow the existing tier vocabulary?
3. Should a Standard reading list ever trigger one supplementary comprehensive pass, or stay strictly within the landscape set?
4. How should the effort budget respond when adaptive screening finds unexpectedly rich results mid-run?
5. Does the harness support skill-name aliases for the eventual `reading-list` rename?
6. How much verification can safely move to the committed turn without weakening trust — and which checks, if any, must stay in the fast first round (for example, DOI resolution for the handful of sources shown)?
