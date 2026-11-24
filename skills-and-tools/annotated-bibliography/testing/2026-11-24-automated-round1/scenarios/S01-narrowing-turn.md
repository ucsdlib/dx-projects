# Scenario S01: Live narrowing turn after landscape

## Focus

**Mode or workflow:** Intake, landscape, selection, refinement (narrowing a theme), targeted follow-up.

**Assumed role:** A senior psychology undergraduate preparing a capstone literature review.

**Situation:** The student has a broad topic and no settled angle. They want to see the literature's shape before committing, then narrow to the sleep component once the landscape is visible. This is the live version of the narrowing turn the 2026-10-22 run simulated from `assignment-prompts.md`, enabling a direct comparison.

**Activation expectation:** Explicit for this round, per protocol Revision 1 (routing deferred; Run 01 documented the natural-activation failure). Turn 1 receives one mechanical invocation line; turns 2-3 arrive verbatim.

## Realistic Input Material

No external material. The assignment context (scholarly sources, APA, capstone) is embedded in the user's own words. This is approximate, matching the prior run's simulated context.

## Exact User Turns

### Turn 1

```text
I'm a senior psychology major getting ready for my capstone. I need sources on how social media affects mental health in college students. I haven't settled on an angle yet — I'd like to see what the literature looks like before I commit to anything.
```

### Turn 2

```text
Looking at this, the sleep part is what I keep thinking about. My roommate swears her anxiety got worse when she stayed up scrolling, but I don't know if that's actually documented. Can we focus on social media and sleep for college students?
```

### Turn 3

```text
Out of what you found, what would you read first if you were me, and what should I double-check myself?
```

## Expected Behavior and Success Criteria

- Turn 1 produces a focused landscape by default (not a full bibliography) with a clear working question and one primary next-step offer.
- Turn 2 triggers refinement behavior: prior state is preserved, targeted search is proportionate to the narrowed scope, and landscape sources relevant to sleep are reused rather than rediscovered.
- Turn 3 produces a prioritized reading path with faithful evidence (access level, confidence, quotes where available) and a "human next steps"-style answer about what the user should verify.
- Clarification stays within the discipline rules: at most four material questions before search, and no repeated questions after the user names a direction.

## Scoring Focus and Known Failure Modes

**Rubric dimensions to watch:** Intake, Workflow compliance, Task quality, Follow-up handling, Accuracy and boundaries, Efficiency.

**Known failure modes:**

- Turn 2 reruns the full search instead of incrementally refining.
- The narrowed output implies exhaustive coverage of social media and sleep when the search was targeted.
- Turn 3 is answered generically instead of from actual run state (themes, sources, gaps).
- The landscape never surfaces sleep, making Turn 2 awkward; log as a coverage observation, not automatically a failure.

## Comparability Note

Prior baseline: `testing/2026-10-22-social-media-mental-health/`. Differences in this run (DOI-first links, synced installed skill, automated multi-turn) should be noted in the report.
