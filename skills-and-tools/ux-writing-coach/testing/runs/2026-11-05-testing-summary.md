# UX Writing Coach Testing Summary — 2026-11-05

## Scope

This summary covers five testing rounds completed on 2026-11-05 for the UC San Diego Library UX Writing Coach skill. The goal was to move the skill from useful one-shot drafting toward a more reliable plan-first, user-centered, and iterative coaching workflow.

All runs used `api-glm-5.3-flash` through Codex CLI 0.151.0 with the UCSD provider and used the `UXWC_TEST_MODE=1` marker for observability.

## Run Overview

| Run | Skill version | Scenarios | Overall result | Primary purpose |
| --- | --- | --- | --- | --- |
| [Run 01](2026-11-05-run01-summary.md) | V2 base | A1, A2, A6, A7 | 4 pass | Initial V2 input classification, task-first drafting, boundary handling, and source-material translation. |
| [Run 02](2026-11-05-run02-summary.md) | V2 plan-first update | A1–A7 | 2 pass, 2 fail, 3 partial | First full test of the plan-first rule. |
| [Run 03](2026-11-05-run03-summary.md) | V2 response-template update | A1–A7 | 5 pass, 1 fail, 1 partial | Full regression after adding response templates and tightening the Plan Gate. |
| [Run 04](2026-11-05-run04-summary.md) | V2 response-template and options-first update | A4, A6 | 1 pass, 1 partial | Test options-first drafting and structured evaluation behavior. |
| [Run 05](2026-11-05-run05-summary.md) | V2 structured-evaluation Plan Gate update | A4 | 1 pass | Regression after explicitly requiring the Plan Gate for structured evaluations. |

## Major Skill Changes Tested

1. **Plan-first workflow.** Added a visible working plan for structured Library content before drafting or review.
2. **Five-field plan pattern.** Required `Goal`, `Audience`, `Top jobs`, `Approach`, and `To confirm`, followed by a review invitation.
3. **Response templates.** Added reusable templates for plan-only, plan-revision, direct-drafting, approved-plan drafting, feedback or evaluation, and pre-send checks.
4. **Options-first drafting.** Encouraged more than one viable direction, explained tradeoffs, and used strengths and areas for improvement to frame revision as development work.
5. **Structured-evaluation Plan Gate.** Clarified that evaluation, review, or feedback requests about structured content also require a working plan.
6. **Reference logging.** Expanded test logs to include the response template and improve visibility into routing and reference use.

## Overall Findings

### What improved

- The skill became much more consistent at using a complete plan-only turn before drafting structured service content.
- A2 no longer treated a requested output format, such as “turn this into cards,” as permission to skip planning.
- A6 demonstrated strong boundary handling for eligibility and limited media playback access.
- A7 showed reliable source-material translation: it identified user jobs rather than republishing the internal service definition sentence by sentence.
- A3 continued to show the correct Plan Gate exception for short, well-specified outage microcopy.
- The response templates improved consistency and made the intended workflow easier for non-designers to follow.
- The options-first update produced useful alternatives, tradeoffs, strengths, areas for improvement, and next steps.
- The structured-evaluation update resolved A4’s remaining Plan Gate failure.

### Persistent or newly identified issues

- **Evaluation mode initially bypassed the Plan Gate.** A4 and, in earlier rounds, A6 showed that the skill could treat structured evaluation as ordinary feedback. The final update addressed this.
- **Reference logging was uneven.** Some responses omitted required references such as `voice-and-messaging.md` or `content-strategy-elements.md` even when those principles shaped the response.
- **First-response consistency varied.** A6 omitted the skill introduction in one round. This should be checked in future full runs.
- **Some internal phrasing still leaked into drafts**, especially “non-public or offsite locations,” though later versions improved concrete wording and flagged terms for verification.
- **Citation labels were sometimes generic** even when a more specific UX principle was relevant.

## Current State

The latest version of the skill now has:

- a stricter Plan Gate for structured service, collection, space, expertise, contact, eligibility, offering-card, and evaluation content;
- reusable response templates;
- options-first drafting with strengths and areas for improvement;
- clearer source-material translation guidance;
- improved boundary and eligibility language;
- a validated and synced installed copy.

The latest targeted regression tests show that the structured-evaluation failure in A4 is resolved and that A6 continues to pass.

## Next Steps

1. Run the full A1–A7 suite against the latest skill version to confirm there are no regressions.
2. Add automated checks for first-turn introduction consistency.
3. Add checks for reference-log completeness on copy-changing turns.
4. Continue testing whether the options-first pattern produces useful alternatives without adding unnecessary length.
5. Review whether “Strengths” and “Areas for improvement” should also be required in plan-only turns or reserved for drafted copy.
6. Improve citation specificity when a response relies on a particular UX principle.
