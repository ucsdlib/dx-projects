# Automated Testing Protocol — Round 1

**Date:** 2026-11-24
**Skill under test:** `annotated-bibliography` (Reading List), installed harness version, synced 2026-11-24 to the dev copy including DOI-first link resolution.
**Scenarios:** 3 (see `scenarios/`). All three are student-facing: S01/S02 use a psychology capstone topic; S03 uses a graduate education thesis topic.

## Revision 1 (2026-11-24, user-approved): explicit invocation

Run 01 found a blocker: in all three sessions, `uc-library-search` intercepted natural topical requests and `annotated-bibliography` never activated (see `runs/2026-11-24-run01-summary.md`). Per user decision, skill triggering and routing is deferred to a later effort. For this round, every tested session receives one mechanical invocation line at the start of Turn 1:

```text
Use the annotated-bibliography skill for this request.
```

Follow-up turns are sent verbatim with no framing. This round therefore evaluates the Reading List pipeline's behavior, output quality, and usability — not activation. The activation failure is recorded as a separate backlog item for future routing work.
**Artifact root:** this directory. Prior runs (`2026-10-21-*`, `2026-10-22-*`) are untouched baselines.

## Execution Steps

For each scenario S01, S02, S03, in that order:

1. Start a fresh delegated session (subagent) with a neutral working directory (`/tmp/reading-list-tests-round1/<scenario-id>`), no access to scenario cards, rubrics, or this repository's testing context.
2. Submit the exact user turns from the scenario card sequentially. The tested session must respond to each turn before seeing the next.
3. Capture the full transcript verbatim, including any files the tested session writes (manifests, reading lists, search logs) in its working directory.
4. Score the transcript against the scenario card's expected behavior using the automated report template (`assets/automated-report-template.md` from the skill-testing-protocol skill). Save the transcript to `transcripts/` and the scored report to `reports/` in this directory.
5. After all three scenarios, produce a run summary (`runs/`) with cross-scenario patterns, severity-grouped issues, and proposed skill changes.

## Isolation Rules

- The tested session never sees scenario cards, expected behavior, rubric dimensions, or prior test reports.
- The only test-specific framing permitted is the mechanical instruction that user turns arrive in order and the session should respond to each as a fresh user conversation.
- The tester (this session) scores results; the tested sessions produce no self-scores.

## Known Limitations

- The tested sessions know they are part of a test (they receive turns as a batch instruction). This is unavoidable with the delegation mechanism and matches the prior run's simulated-turn approach; note it in each report's metadata.
- Real network search results vary between runs; landscape content will differ across sessions. Compare structure and behavior, not specific sources.
- Automated sessions cannot fully replicate a human's narrowing turn; S01's Turn 2 is scripted to be robust to landscape variation (it names sleep directly rather than referring to theme numbers).

## Human Testing

A lightweight human protocol can be derived from these same scenario cards for live participant testing (the live narrowing turn in its fully authentic form). Deferred until automated results are reviewed; not part of this round's execution.
