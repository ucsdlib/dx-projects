# Automated Testing Protocol — Round 3: Template Safeguard

**Date:** 2026-11-24
**Skill under test:** `annotated-bibliography` (Reading List), installed harness version, synced 2026-11-24 with rule 7 ("plain language governs wording, not structure") and the template-defaulting safeguard.
**Focus:** Whether the template-defaulting safeguard holds required template structure while preserving the round 2 clarity gains. The round 2 failure was not template ignorance (the session read `response-templates.md` and logged it) but compression: the Plain-Language Rules were resolved against template structure. This round tests the fix at the same decision point.
**Scenarios:** S01 only (same rationale as round 2: validate the revised behavior on the known-failing case before running others). User turns are verbatim identical to rounds 1-2 so results compare directly.
**Artifact root:** this directory. Prior rounds untouched.

## What Changed Since Round 2

1. Rule 7 in `references/response-templates.md`: required template elements are never omitted for brevity; overviews keep theme headings, folded questions, representative readings, and find-more links; reading lists keep the full annotation block.
2. Non-Negotiable in SKILL.md: select the matching template before rendering any substantive response; deviate only when the request clearly fits no template, noting the deviation in the manifest.
3. Quality Check item 8 in SKILL.md: verify required elements survived rendering.
4. Templates intro states the selection-and-default rule up front.

## Evaluation Lens

Two checklists, both scored with direct quotes as evidence. Judge from the persona's perspective (a senior psychology undergraduate for S01), not from the developer's.

**Structure compliance (new; the round 2 failure mode):**

1. Landscape presents themes as headings (not bolded bullets).
2. Each theme carries one to two theme-phrased questions.
3. Each theme carries two to three representative readings (at least one) plus a find-more structured search link.
4. Reading lists and bibliographies carry the full annotation block: full citation, source ID, study design, access level, confidence, key quotes where available.
5. No required element was silently omitted; if something was omitted, the response or manifest says why.

**User-perspective clarity (unchanged from round 2):** jargon audit, interpretation-first opening, consequence-based transparency, estimates not false precision, next-step clarity, trust support.

Both lenses must pass for an overall pass. A structure pass with a clarity regression, or the reverse, is a partial with the regression named.

## Execution

Same mechanics as rounds 1-2: fresh delegated session, neutral working directory `/tmp/reading-list-tests-round3/s01`, explicit invocation line at Turn 1 (routing deferred per round-1 decision), verbatim turns 2-3, full transcript capture, scored report, run summary.

**Timing capture.** After each turn completes, record the delegated run's `startedAt`/`completedAt` from thread activity and put exact per-turn durations (with UTC timestamps for interim messages) in the transcript header. Where only the orchestrating session's wait wall time is available, label it as such. Duration is part of the Efficiency and right-sizing evidence, not metadata.
