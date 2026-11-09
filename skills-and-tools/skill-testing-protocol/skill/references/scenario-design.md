# Scenario Design

## Purpose

This reference provides guidance for building realistic scenario cards. Scenario cards are the test prompts and success criteria; they are never pasted into the tested session.

## Principles

- Use believable work products, materials, ambiguity, and follow-ups.
- Ask the user to supply or validate source material so scenarios reflect actual usage.
- Keep prompts authentic: one initial request and no more than three total user turns.
- Do not include evaluation criteria, rubric language, or the skill's own instructions in the user turns.
- Include enough context that a skilled practitioner would understand the task, but leave realistic gaps the skill must navigate.

## Card Structure

Each card contains:

1. **ID and title:** Stable identifier (e.g., `S01`) and a short descriptive title.
2. **Mode or workflow focus:** Which skill mode or workflow is being tested.
3. **Assumed role:** Who the user is in this scenario.
4. **Situation:** What the user needs to accomplish and why.
5. **Realistic input material:** Source content, policy text, data, or context the user would bring. Ask the user to provide or approve this.
6. **Exact user turns:** Verbatim prompts the tester will submit, numbered by turn.
7. **Expected behavior or success criteria:** Observable outcomes that indicate the skill handled the scenario well.
8. **Scoring focus and known failure modes:** Specific rubric dimensions to watch and common mistakes.
9. **Activation expectation:** Whether the skill should activate naturally, require explicit invocation, or both.

## Writing User Turns

- Turn 1 should be an authentic initial request with enough context to start work but not a script of expected behavior.
- Turn 2 typically asks for a revision, refinement, or decision about a tradeoff.
- Turn 3, if present, probes follow-up handling or boundary awareness.
- Do not tell the skill what to do in the prompt; test how it responds to a realistic request.

## Realistic Input Material

Source material should:

- Come from or closely resemble what the skill's intended user would actually provide.
- Include some ambiguity or missing information the skill must handle.
- Avoid being so clean that the skill has no decisions to make.
- Avoid being so messy that any output would fail.

When possible, ask the user to paste real or plausible material directly into the scenario card. If no material is available, write representative content and flag it as approximate.

## Review

After building all scenario cards, present them to the user. Ask:

- Does each scenario feel like a realistic request?
- Does the input material match what users would bring?
- Are the expected behaviors aligned with the skill's intent?
- Are any important modes, risks, or edge cases missing?

Revise based on feedback before proceeding to execution.
