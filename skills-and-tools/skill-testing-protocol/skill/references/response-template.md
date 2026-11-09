# Response Templates

These templates guide how the testing skill communicates with the user during each workflow phase. Adapt tone and brevity to context; keep the structure.

## Phase 1: Gathering Information

> I need to understand the skill under test before building a test plan. Could you share:
>
> 1. The skill's name and a brief description of what it does.
> 2. Its `SKILL.md` file or a path to it.
> 3. Any known limitations, failure modes, or concerns you'd like the tests to focus on.
> 4. Example materials, inputs, or source content the skill processes.
> 5. Whether the skill should activate naturally, require explicit invocation, or both.

## Phase 2–3: Presenting the Test Plan

> Based on the skill analysis, I recommend [N] scenarios covering these risks:
>
> | ID | Mode / Risk | What it tests |
> | --- | --- | --- |
> | S01 | [mode] | [one sentence] |
> | S02 | [mode] | [one sentence] |
> | S03 | [mode] | [one sentence] |
>
> Each scenario uses one initial request plus up to two follow-ups. Would you like to adjust the scope, add or remove scenarios, or provide additional context before I build the scenario cards?

## Phase 4: Presenting Scenario Cards

> Here are the scenario cards. Please review each one and let me know:
>
> - Does each scenario feel like a realistic request?
> - Does the input material match what users would bring?
> - Are the expected behaviors aligned with the skill's intent?
> - Are any important modes or risks missing?

## Phase 5: Confirming Before Execution

> The testing protocols and scenario cards are ready. Once you confirm they look good, I'll guide you through running each automated scenario in a fresh session.

## Phase 6: Guiding Automated Testing

> The testing protocols and scenario cards are approved. I'll now run all [N] automated scenarios in fresh sessions and save transcripts, scored reports, and a run summary. This will take a few minutes.
>
> [After all scenarios are complete:]
>
> All [N] scenarios are complete. Here's the run summary:
>
> | Scenario | Overall result | Key finding |
> | --- | --- | --- |
> | S01 | Pass / Partial / Fail | [one sentence] |
> | S02 | Pass / Partial / Fail | [one sentence] |
> | S03 | Pass / Partial / Fail | [one sentence] |
>
> Transcripts are saved in `testing/` and scored reports are in the working directory. Would you like to review any scenario in detail, or proceed to synthesis?

## Phase 7: Presenting Synthesized Findings

> Here's the synthesis across all sessions:
>
> **Top issues:**
> 1. **[Severity] [Issue description]** — [Evidence: which scenarios, what pattern.]
> 2. **[Severity] [Issue description]** — [Evidence: which scenarios, what pattern.]
>
> **Recommended changes:**
> 1. [Specific file or rule to change, traced to evidence.]
> 2. [Specific file or rule to change, traced to evidence.]
>
> Would you like to discuss any finding before proceeding to skill revisions?
