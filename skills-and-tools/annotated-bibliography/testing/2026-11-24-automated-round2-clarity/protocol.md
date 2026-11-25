# Automated Testing Protocol — Round 2: User-Friendly Language

**Date:** 2026-11-24
**Skill under test:** `annotated-bibliography` (Reading List), installed harness version, synced 2026-11-24 with the Plain-Language Rules, restructured landscape template, and turn-opening contract.
**Focus:** Clarity of the skill's responses from the perspective of the user defined in each scenario — would that person understand the response, trust it, and know what to do next?
**Scenarios:** S01 in this round (others follow if S01 validates the revised templates). Scenario cards adapt the round-1 cards; user turns are unchanged so results compare directly against `2026-11-24-automated-round1` run 02.
**Artifact root:** this directory. Prior rounds untouched.

## What Changed Since Round 1

The skill now includes a Plain-Language contract (see `skill/references/response-templates.md`): interpretation-first openings, no internal vocabulary, transparency as consequences rather than mechanisms, silent bookkeeping, and the restructured landscape (theme headings with folded questions, representative readings, find-more links, possibilities-framed directions).

## Evaluation Lens: User-Perspective Clarity

Score clarity as the scenario's persona would experience it, using this checklist:

1. **Jargon audit:** no internal vocabulary (landscape, manifest, breadth tier, fidelity, PNX, component decomposition) appears in user-facing text; any necessary technical concept is translated.
2. **Interpretation-first opening:** the response opens by restating the working question(s) and how the skill will proceed; no bookkeeping lead.
3. **Consequence-based transparency:** limitations are stated with what they mean for the user's conclusions and what to do next; no API mechanics.
4. **Estimates, not false precision:** counts and coverage claims are labeled approximate; no reliability narration.
5. **Next-step clarity:** after reading the response, the persona could state what they would do next without guessing.
6. **Trust support:** the persona could tell what is well-supported versus provisional, and why.

Record direct quotes as evidence for each pass or fail. Judge from the persona's perspective (a senior psychology undergraduate for S01), not from the developer's.

## Execution

Same mechanics as round 1: fresh delegated session per scenario, neutral working directory, explicit invocation line at Turn 1 (routing deferred per round-1 decision), verbatim turns 2-3, full transcript capture, scored report per scenario, run summary at the end.
