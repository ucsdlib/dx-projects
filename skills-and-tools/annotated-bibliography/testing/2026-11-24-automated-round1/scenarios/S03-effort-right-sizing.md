# Scenario S03: Effort right-sizing and depth signaling

## Focus

**Mode or workflow:** Intake (depth markers), landscape, escalation to deep work, adaptive clarification.

**Assumed role:** A master's student in an education program.

**Situation:** The user starts with an explicit quick request ahead of a meeting with their advisor, then escalates to comprehensive work for their thesis literature review, then asks what distinguishes the two. This is the baseline test for the phase 3 "right-sizing" direction: the current skill's behavior on quick requests and on deep-work expectation-setting, on a fresh topic.

**Activation expectation:** Explicit for this round, per protocol Revision 1.

## Realistic Input Material

No external material. Topic: supports and barriers to first-generation college student success. Chosen to be plausible for a graduate education student and distinct from S01/S02's topic.

## Exact User Turns

### Turn 1

```text
I'm a master's student in education, and I have a meeting with my advisor tomorrow about my thesis direction. I want to talk about first-generation college students — what actually helps them succeed. Could you give me a quick sense of the research? Just the highlights, maybe a handful of sources I can skim tonight.
```

### Turn 2

```text
Okay, this is good. My advisor wants me to build a real literature review chapter on this, though — can you do a comprehensive annotated bibliography on the same question? It doesn't need to be done tonight, but sooner is better.
```

### Turn 3

```text
Before you go deep — what's the difference between what you just gave me and the full version?
```

## Expected Behavior and Success Criteria

- Turn 1 stays quick: a landscape-level response with a handful of strong sources, no comprehensive run, and honest language about what the quick pass does and does not cover.
- Turn 2 begins with an unprompted one-line expectation statement (that a comprehensive run involves substantial searching and may take several minutes) before deep work starts. The user's turn contains no request for this; volunteering it is the behavior under test.
- Escalation preserves state: the quick pass's sources and themes remain valid in the comprehensive run.
- Turn 3 is answered clearly in plain language, distinguishing scope, source count, and annotation depth without jargon.
- Responses follow the plain-language contract throughout: interpretation-first openings, no internal vocabulary, limitations as consequences with next actions.

## Scoring Focus and Known Failure Modes

**Rubric dimensions to watch:** Intake, Efficiency, Workflow compliance, Audience and accessibility, Follow-up handling, Plain language.

**Known failure modes:**

- Turn 1 over-runs: component decomposition and exhaustive tool pipelines triggered despite the explicit "quick" request ahead of a next-day meeting.
- Turn 2 starts deep work without volunteering an expectation statement. (Distinguish this from the user asking and being ignored, which would be a different, responsive-compliance failure; this scenario only tests the proactive case.)
- Turn 3 is vague or uses internal vocabulary (tiers, PNX, fidelity) without translation.
