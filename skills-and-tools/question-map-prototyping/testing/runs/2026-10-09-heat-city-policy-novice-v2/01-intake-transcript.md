# Intake Transcript

**Run ID:** 2026-10-09-heat-city-policy-novice-v2
**Case ID:** heat-city-policy-novice
**Date:** 2026-10-09
**Confirmation status:** `user_confirmed`

## Raw user prompt

Copy the exact prompt from the case file. Do not paraphrase or add components.

> What should my city do about extreme heat and public health?

## Simulated user context available for clarification

Use this only if and when `question-map` asks a clarifying question. Do not paste it into the initial prompt, and do not use it to import reviewer-only coverage lenses.

- I'm a novice researcher trying to prepare for a city council meeting.
- I want to bring evidence from recent research.

## Clarification exchange

Record what the tool actually asked and the simulated user response. If no clarifying questions were asked, write “None asked.”

| # | Tool question | Simulated user response | Used in confirmed scope? |
|---|---|---|---|
| 1 | What are you trying to prepare for, and what evidence do you want to bring? | I'm a novice researcher trying to prepare for a city council meeting. I want to bring evidence from recent research. | Yes |

## Confirmed working scope

Write this in the user's voice and preserve the raw prompt's intent. Do not turn reviewer coverage lenses into requirements.

> What should my city do about extreme heat and public health? I want recent research evidence to bring to a city council meeting.

## Components explicitly requested by the user

Leave empty if the prompt did not explicitly name components. Do not infer a component into this list merely because a reviewer wants to audit it.

- Recent research evidence for a city council meeting.

## Reviewer-only coverage lenses

These lenses help reviewers inspect blind spots, but they are not user requirements and must not be passed to `question-map`.

- health outcomes and healthcare use;
- vulnerable populations and equity;
- urban form, green space, and cooling;
- governance, policy, and emergency response;
- lived experience and social consequences;
- measurement or evidence limitations.

## Intake realism checks

| Check | Pass? | Notes |
|---|---|---|
| The raw prompt was sent unchanged | Yes | Quoted in this transcript and preserved in the graph as a context frame. |
| Simulated context was used only in response to clarification questions | Yes | The two facts supplied here were used only after the clarification question. |
| The confirmed scope does not add reviewer-only lenses | Yes | It adds only the user's stated purpose and evidence preference. |
| The user prompt remains framing rather than a canonical question | Yes | The prompt is represented as a context node, not a source-supported canonical question. |
