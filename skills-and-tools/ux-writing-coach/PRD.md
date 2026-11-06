# UX Writing Coach — Living Product Requirements

**Skill line:** V2  
**PRD revision:** 2026-11-05  
**Status:** Draft implementation; human expert review is required before publication  
**Product owner:** Doug Worsham  

This document describes the current product, not its original build history. Update it before substantive behavioral, scope, or workflow changes. For dated changes and evidence, see `CHANGELOG.md`.

## Document Roles

- `PRD.md` is the current product intent, scope, and acceptance criteria.
- `SKILL.md` is the current runtime workflow and behavior.
- `references/` contains the packaged style, terminology, and content guidance.
- `testing/runs/` contains validation evidence and findings.
- `CHANGELOG.md` records dated changes and the evidence supporting them.

If this document and the implementation conflict, reconcile them before release.

## 1. Purpose

`ux-writing-coach` helps UC San Diego Library staff plan, draft, revise, and evaluate user-centered digital UX copy. It acts as a collaborative writing coach rather than a one-shot editing tool: it clarifies the user task, offers distinct options, explains tradeoffs briefly, preserves factual meaning, and identifies the next human review step.

The skill applies Library-specific voice, terminology, and content patterns alongside UC San Diego style and NN/g UX writing guidance. It does not replace policy experts, accessibility auditors, brand approvers, or CMS publishing workflows.

## 2. Users and Scope

The primary users are UC San Diego Library staff responsible for digital copy. Secondary users include supervisors and student employees drafting first-pass content under staff review.

The skill prioritizes Library website and interface writing about:

- services and service desks;
- collections, archives, and special collections;
- spaces and wayfinding;
- expertise and research support;
- policies, access, and eligibility;
- forms, interface labels, alerts, and help content;
- events, research guides, contact sections, and related Library UX writing.

Out of scope:

- general campus copy outside the Library;
- full WCAG or accessibility conformance audits;
- CMS editing or publishing workflows;
- legal, policy, brand, accessibility, or AP approval;
- translation and localization.

The skill may flag copy-adjacent accessibility concerns, such as vague link text, and recommend expert review or testing.

## 3. Product Principles

1. **Coach, not gatekeeper.** Offer useful directions, explain tradeoffs, and invite iteration.
2. **User task first.** Lead with the user’s action or benefit; place limits, eligibility, and process later.
3. **Options, not one answer.** Treat drafts as development work in progress.
4. **Preserve meaning and boundaries.** Clarify restrictions without erasing them.
5. **No invented facts.** Do not invent services, hours, locations, links, policies, names, deadlines, or eligibility.
6. **Human review required.** Every output is a draft; identify concrete next steps and required experts.
7. **Least-prior-knowledge lens.** Write for the user with the greatest need or least familiarity, then check whether experienced users can still work efficiently.
8. **Library specificity.** Use approved UC San Diego and Library terminology, voice, and content patterns.
9. **Concise reasoning.** Explain substantive recommendations without turning coaching into a lecture.

## 4. Core Workflow

The current workflow has four linked stages: classify, plan, draft, and evaluate or iterate. Exact implementation language lives in `SKILL.md`; the required behavior is summarized below.

### 4.1 Classify the Request

The skill determines whether the user needs intake, drafting, feedback, evaluation, or a combination. It also classifies supplied material as:

- source material;
- a rewrite object;
- mixed input;
- a context-only request.

If the input type is ambiguous, the skill assumes source material and states the assumption in one short line. It evaluates rewrite objects against user tasks rather than preserving their framing by default.

### 4.2 Apply the Plan Gate

Structured Library content requires a plan before drafting or review. This includes service pages, service descriptions, offering cards, eligibility and access copy, contact sections, collection descriptions, space descriptions, expertise pages, and evaluations or reviews of those content types.

The working plan uses five fields:

- goal;
- audiences and eligibility;
- top jobs;
- approach or content molecule;
- items to confirm.

The exact visible labels are defined in `references/response-templates.md`.

The Plan Gate may be skipped only when all required plan inputs are already supplied or when the request is short, well-specified microcopy or a small line-level edit. A requested output format alone, such as “turn this into cards,” does not satisfy the gate.

For structured content, a plan-only turn must stop before recommended copy, revised copy, card sets, alerts, evaluation tables, or page drafts. It may include assumptions and up to two high-priority clarifying questions, and must end with an invitation to revise or approve the plan.

### 4.3 Draft

Drafting begins after the user approves the plan, supplies missing material, or explicitly asks to proceed. The skill uses the approved structure rather than restarting the analysis.

Current defaults:

- **Microcopy:** offer two to three distinct options with one-line rationales.
- **Short form:** offer two versions or one recommended revision plus a bolder alternative.
- **Long form:** propose structure and cuts first; offer alternative treatments of the highest-impact section.
- **Follow-up:** build on the selected direction rather than restarting.

Options should explain their emphasis or tradeoff, such as clearer, warmer, shorter, more specific, or more inclusive. Substantive drafting turns should include strengths, areas for improvement, and concrete next steps.

### 4.4 Evaluate and Iterate

Feedback or evaluation follows the response template. It leads with specific strengths, then identifies no more than three high-impact opportunities. It offers suggested revisions, explains why they improve audience or task fit, and recommends next steps.

The skill treats audience assumptions as hypotheses. When vocabulary, task fit, eligibility language, or emotional resonance is uncertain, it recommends user testing or expert review.

## 5. Content and Reference Architecture

The skill uses a modular reference architecture. The runtime reads only the references relevant to the task.

- `references/content-scenarios.md` routes the request to the smallest useful reference set.
- `references/working-plan.md` defines input classification, the Plan Gate, and source-material translation.
- `references/response-templates.md` defines response shape and review gates.
- `references/content-strategy-elements.md` defines reusable content elements and molecules.
- `references/library-style.md` defines source hierarchy, AI-sounding language rules, and source verification.
- `references/voice-and-messaging.md` defines UC San Diego voice, Library voice, messaging themes, headline and body-copy guidance, and tone by context.
- `references/ux-writing-principles.md` defines copy sizes, scanning, user-centered transformation, brevity, jargon handling, and audience fit.
- `references/style-mechanics.md` covers campus naming, numbers, dates, times, punctuation, links, URLs, and interface terms.
- `references/library-terminology.md` defines exact Library names, spaces, programs, systems, collections, and terminology.
- `references/inclusive-language.md` defines inclusive language and UX patterns.
- `references/source-citations.md` maps compact labels to canonical sources and section anchors.

`references/voice-and-messaging.md` is required for any task that drafts, rewrites, reviews, evaluates, or otherwise changes copy.

`SKILL.md`, `agents/`, and `references/` form the packaged skill. `testing/`, `PRD.md`, `CHANGELOG.md`, and `research/` are development and validation artifacts, not runtime dependencies.

## 6. Output and Quality Requirements

All substantive output should:

- use UC San Diego, never UCSD;
- use approved Library terminology where supplied;
- preserve factual meaning and material limits;
- avoid em dashes in suggested copy and rationales;
- avoid hype, throat-clearing, and unnecessary intensifiers;
- flag unverified facts, links, names, deadlines, eligibility terms, or terminology changes;
- cite exact compact labels and canonical URLs when source support is relevant;
- identify a concrete next step for human review;
- not describe copy as approved or publication-ready.

When local references conflict or are incomplete, the skill should state the uncertainty and ask for verification rather than presenting an unverified campus or AP rule as authoritative.

## 7. Testing and Validation

The reusable automated suite uses scenarios A1 through A7. `testing/automated-testing-plan.md` defines the fresh-session protocol, scoring checklist, failure categories, and reporting rules. `testing/human-testing-plan.md` supports facilitated Library staff testing.

Structured test logs are enabled by prefixing the first user turn with `UXWC_TEST_MODE=1`. The log records scenario routing, input classification, Plan Gate behavior, response template, copy size, molecule, references used, and next-step type.

Current status:

- targeted regressions for A4 and A6 pass;
- a full A1 through A7 regression against the latest V2 is pending;
- human expert review remains required for substantive style, policy, accessibility, or audience-fit changes.

Known areas to watch include first-response introduction consistency, complete reference logging, citation specificity, and avoiding internal workflow language in public-facing drafts.

## 8. Release and Maintenance Process

For substantive changes, follow this sequence:

1. Update `PRD.md` with the intended behavior, scope, and acceptance criteria.
2. For a medium or large change, create a dated proposal under `proposals/` or an equivalent working file.
3. Implement the change in `SKILL.md` or `references/`.
4. Run the skill validator and appropriate test scenarios.
5. Record results in `testing/runs/`.
6. Update `CHANGELOG.md`.
7. Refresh the installed skill with the repository installation command.

Small wording, typo, or reference-file updates may skip a proposal but still require a changelog entry and targeted validation.

Style guidance should be maintained in `references/`, not `SKILL.md`. Keep `SKILL.md` focused on workflow, routing, response shape, and quality rules. New sources must be added to `references/source-citations.md` with their canonical URL, verification date, scope, and hierarchy level before they are cited.

## 9. Current Gaps and Open Questions

The following items are known but not yet resolved:

- Complete a full A1 through A7 regression on the latest V2 implementation.
- Add automated checks for first-turn introduction consistency.
- Add automated checks for reference-log completeness on copy-changing turns.
- Clarify whether plan-only turns should also include “Strengths” and “Areas for improvement,” or reserve those for drafted copy.
- Improve citation specificity when a response relies on a particular UX principle.
- Decide whether a local override system is needed for unit-specific terminology, approved exceptions, or local examples.
- Define a stable, machine-readable skill version field if release tracking becomes more formal.
