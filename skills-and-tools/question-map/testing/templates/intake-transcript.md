# Intake Transcript

**Run ID:**  
**Case ID:**  
**Date:**  
**Confirmation status:** `initial_prompt_only` | `user_confirmed` | `blocked`

## Raw user prompt

Copy the exact prompt from the case file. Do not paraphrase or add components.

> 

## Simulated user context available for clarification

Use this only if and when `question-map` asks a clarifying question. Do not paste it into the initial prompt, and do not use it to import reviewer-only coverage lenses.

- 

## Clarification exchange

Record what the tool actually asked and the simulated user response. If no clarifying questions were asked, write “None asked.”

| # | Tool question | Simulated user response | Used in confirmed scope? |
|---|---|---|---|
| 1 |  |  |  |

## Confirmed working scope

Write this in the user's voice and preserve the raw prompt's intent. Do not turn reviewer coverage lenses into requirements.

> 

## Components explicitly requested by the user

Leave empty if the prompt did not explicitly name components. Do not infer a component into this list merely because a reviewer wants to audit it.

- 

## Reviewer-only coverage lenses

These lenses help reviewers inspect blind spots, but they are not user requirements and must not be passed to `question-map`.

- 

## Intake realism checks

| Check | Pass? | Notes |
|---|---|---|
| The raw prompt was sent unchanged |  |  |
| Simulated context was used only in response to clarification questions |  |  |
| The confirmed scope does not add reviewer-only lenses |  |  |
| The user prompt remains framing rather than a canonical question |  |  |
