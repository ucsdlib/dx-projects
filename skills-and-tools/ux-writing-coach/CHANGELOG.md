# UX Writing Coach — Changelog

This changelog records product and workflow changes in reverse chronological order.

The repository does not currently contain Git history. Earlier entries are reconstructed from current files, file timestamps, `PRD.md` v0.3, and testing summaries. They are intentionally conservative and are not intended to be an exhaustive commit-level history.

## 2026-11-05 — V2 workflow and documentation updates

### Added or refined

- Added a plan-first workflow for structured Library content.
- Added the five-field working plan pattern: goal, audiences and eligibility, top jobs, approach, and items to confirm.
- Added reusable response templates for plan-only turns, plan revisions, direct drafting, drafting after an approved plan, feedback or evaluation, and pre-send consistency checks.
- Added options-first drafting behavior, with tradeoffs, strengths, areas for improvement, and next steps.
- Added test logging through `UXWC_TEST_MODE=1`, including scenario routing, input classification, Plan Gate behavior, response template, copy size, molecule, references used, and next-step type.
- Expanded the structured-evaluation Plan Gate so evaluation, feedback, or review of structured Library content also requires a plan before recommendations.
- Added clearer guidance for translating source material into user-facing copy rather than paraphrasing internal service definitions.
- Expanded the reusable test suite to scenarios A1 through A7.

### Testing

- Run 01 tested the V2 base with A1, A2, A6, and A7: four passes.
- Run 02 tested the first plan-first update with A1 through A7: two passes, two failures, three partial results.
- Run 03 tested the response-template update with A1 through A7: five passes, one failure, one partial result.
- Run 04 tested options-first drafting with A4 and A6: one pass and one partial result.
- Run 05 tested the structured-evaluation Plan Gate update with A4: one pass. This resolved the A4 Plan Gate failure.
- The latest targeted regressions show that A4 and A6 pass under the current V2 behavior.
- A full A1 through A7 regression remains pending.

### Documentation

- Updated `README.md` to describe the current V2 behavior, testing workflow, installation refresh, maintenance process, and validator command.
- Replaced `PRD.md` with this living product requirements document based on the current V2 state.

### Known issues and unknowns

- Earlier V2 rounds showed uneven reference logging, first-response introduction inconsistencies, generic citation labels, and occasional internal phrasing in public-facing drafts. Some later rounds improved these issues, but the full regression has not yet confirmed the current state.
- No continuous commit history is available in this workspace. The exact sequence and implementation details for some earlier V2 changes are inferred from file timestamps, current implementation, and testing summaries rather than from a complete change log.

## 2026-10-27 — V1 testing and calibration

### Testing

- Ran six fresh-session scenarios, A1 through A6, covering intake, drafting, feedback, evaluation, combination behavior, service content, microcopy, contact pathways, eligibility boundaries, and audience-specific calls to action.
- A3, A4, A5, and A6 passed.
- A1 and A2 produced useful copy but received partial results because of verification drift, terminology changes that were not flagged, formatting inconsistencies, generic calls to action, or internal context leaking into first drafts.

### Findings

- The skill generally selected appropriate content molecules, used task-first structure, handled follow-ups without restarting, avoided fabricated facts, and framed outputs as drafts needing review.
- Main calibration needs were stricter handling of audience and eligibility terminology, repeatable verification reminders, consistent style-rule enforcement, more specific calls to action, and earlier removal of internal workflow details from drafts.

## 2026-10-22 — Initial reference foundation and PRD draft

### Added

- Established the initial product requirements in `PRD.md` v0.3.
- Built the initial reference foundation from UC San Diego Library, UC San Diego Editorial Style Guide, UC San Diego Brand Voice and Messaging, and NN/g UX writing sources.
- Added local reference notes for Library style, terminology, voice and messaging, inclusive language, UX writing principles, style mechanics, and source citations.
- Added the initial build-time source corpus under `research/`.

### Notes

- The PRD at this point described the initial V1 build plan and was later revised through testing and V2 workflow changes. No historical PRD copy is preserved in the current repository.
- This entry reflects the initial reference and requirements foundation. Exact order of creation within the date is inferred from file timestamps and current file contents.
