# Automated Testing Plan: UX Writing Coach

## Purpose

This plan tests the installed `ux-writing-coach` skill in fresh TritonAI Harness sessions. The goal is to observe how the skill behaves across intake, drafting, feedback, evaluation, and combined modes, using realistic Library requests rather than synthetic prompts.

## Test Principles

- Start each scenario in a new session with no conversation history from this repository.
- Use only the source excerpts supplied in the scenario card; do not point the model to repository files.
- Ask one authentic initial request and no more than three total user turns.
- Preserve the full transcript verbatim, including any tool or reference-loading behavior.
- Score the interaction against the skill's own workflow and quality rules.
- Evaluate whether the skill identifies itself, offers useful options, explains tradeoffs, and invites iteration.
- Do not alter the skill during a test run.

## Preconditions

1. The packaged skill is installed at the TritonAI skills path.
2. A clean TritonAI session is available, preferably from a neutral working directory such as `/tmp/ux-writing-coach-tests` rather than this repository.
3. The scenario card is available to the tester but not to the model.
4. If the harness supports it, disable unrelated skills for the run so activation can be observed.
5. Run the latest version of the skill before changing it.

## Invocation Protocol

For each scenario, copy the exact user turns from the scenario card into the new session. If a scenario does not activate the skill naturally, stop after the first turn and record that as an activation failure. Do not add explicit invocation text unless that is the intended behavior being tested.

Do not provide the repository path, skill source, AGENTS instructions, or evaluation criteria in the tested session. The model may access packaged skill references, but it should not access `testing/` or other repository-only context.

For instrumented runs, prefix Turn 1 with the test-mode marker `UXWC_TEST_MODE=1` on its own line. This marker is a harness/testing convention, not part of the scenario prompt. It asks the skill to emit a `uxwc-test-log` HTML comment recording the routed scenario, input type, plan stage, copy size, molecule, references used, and next-step type. If the harness does not support a reliable marker, leave the marker off and mark direct routing and reference use as `Not observed`.

## Reference-Use Evaluation

Evaluate each response against the applicable files in `references/`, not only against general quality impressions. Record whether the skill used the reference conceptually, cited it, or missed it. If the harness does not expose tool or file-loading behavior, mark direct use as `Not observed`; do not infer that a file was opened solely because the response aligns with it.

When `UXWC_TEST_MODE=1` is enabled, preserve the `uxwc-test-log` HTML comment from the skill response and use it as evidence of the skill's own routing and reference choices. Treat the log as self-reported evidence, not as proof that a file was opened, unless the harness also exposes a tool-use record.

| Reference | Evaluate whether the response |
| --- | --- |
| `content-scenarios.md` | Routes the request to the correct writing scenario and avoids unrelated workflows. |
| `working-plan.md` | Classifies input, uses a working plan only when needed, and translates source material without sentence-level paraphrase. |
| `response-templates.md` | Matches the plan-only, plan-revision, direct-drafting, feedback, or consistency-check response shape and preserves the review gate. |
| `content-strategy-elements.md` | Selects and adapts the relevant service molecule or content element. |
| `library-style.md` | Respects source hierarchy and handles uncertain rules conservatively. |
| `ux-writing-principles.md` | Matches copy size, structure, scanning patterns, brevity, and revision strategy. |
| `voice-and-messaging.md` | Applies UC San Diego voice, Library voice, tone by context, and service-critical language. |
| `style-mechanics.md` | Applies naming, capitalization, numbers, dates, punctuation, links, and interface terms. |
| `library-terminology.md` | Uses approved Library names, spaces, systems, and public-facing terminology. |
| `inclusive-language.md` | Applies identity, disability, gender, race, ethnicity, and inclusive UX patterns when relevant. |
| `source-citations.md` | Uses exact labels and canonical URLs only when a citation is needed. |

For each applicable reference, mark `Pass`, `Partial`, `Fail`, or `Not applicable`. If the response did not visibly load the reference, mark direct use `Not observed` and evaluate conceptual alignment separately.

## Transcript Format

Use readable Markdown for the transcript so reviewers can scan prompts and responses without opening code blocks. For each turn:

- Start with a level-three heading in the form `### Turn 1 — User` or `### Turn 1 — Skill`.
- Place the turn's verbatim content in a blockquote. Prefix every nonblank line with `> ` and use `>` alone on blank lines inside the quote.
- Preserve Markdown structure in the quoted response, including headings, lists, bold text, nested lists, and hard line breaks.
- Preserve any `uxwc-test-log` HTML comment verbatim inside the quoted skill turn.
- Separate consecutive turns with `---` on its own line, with one blank line before and after the divider.
- Do not add commentary inside the blockquote. Keep all tester observations in the evaluation sections.

The `Full Transcript` section in `testing/reports/report-template.md` is the canonical example.

## Coverage Matrix

| Scenario | Primary mode | Secondary mode | Copy output | Service context |
| --- | --- | --- | --- | --- |
| A1 | Intake | Drafting | Service overview | Ask |
| A2 | Drafting | Feedback | Service-offering cards | Borrow and Use Physical Collections |
| A3 | Feedback | Drafting | Status, alert, or help message | Technology Lending Program |
| A4 | Evaluation | Intake | Service page assessment | Undergraduate Library Research Prize |
| A5 | Intake | Drafting | Contact and support molecule | Ask |
| A6 | Combination | Boundary handling | Error/help message and scope statement | Technology Lending Program |
| A7 | Intake | Drafting | Source-material working plan | Borrow and Use Physical Collections |

## Automated Evaluation Checklist

For each transcript, mark each item as `pass`, `partial`, or `fail`, with a one-sentence note.

### Activation and workflow

- The correct skill activates without a repository hint.
- The skill identifies a plausible starting mode in one line when useful.
- It asks zero to two high-value clarifying questions when clarification is needed.
- It establishes format, copy size, audience, task, and constraints without questionnaire-style intake.
- It classifies input as source material, rewrite object, mixed input, or a context-only request.
- For structured service, collection, space, or expertise content, it uses a plan-first turn by default.
- The plan turn includes all five fields: `Goal`, `Audience`, `Top jobs`, `Approach`, and `To confirm`.
- The plan turn asks for review with `Reply with changes, or say “Go ahead” to draft.`
- It does not include the requested draft in the plan turn unless the user explicitly asks for both.
- It skips the working plan only when all plan inputs are supplied or the task is short microcopy or a line-level edit.
- In test mode, the log records whether the plan stage was `shown`, `skipped`, `combined`, or `none`, and whether the visible response matches the log.

### Content quality

- The output translates source material into user-facing copy based on user jobs and outcomes.
- It does not paraphrase internal source sentences or reuse abstract internal goals as user-facing claims.
- It does not expose internal scope, metrics, roles, staffing, or workflow language.
- It leads with the user's action or benefit and puts limits after the opening path.
- It preserves all material boundaries and does not imply eligibility that does not exist.
- For service content, it uses or adapts the relevant molecule from `content-strategy-elements.md`.
- It selects the molecule from user jobs, audience, and placement, and explains a format conflict when one exists.
- For microcopy, it offers two to three distinct options with one-line rationales.

### Style and safety

- Uses "UC San Diego," not "UCSD."
- Uses approved Library terminology where provided.
- Does not invent services, locations, hours, policies, links, names, deadlines, or facts.
- Flags facts requiring human verification.
- Uses exact citations only when they support the response.
- Avoids em dashes, hype, throat-clearing, and unnecessary intensifiers.
- Does not describe copy as approved or publication-ready.
- Provides a concrete next step.

### Interaction quality

- The response is appropriately concise for the copy size.
- Follow-up turns adapt rather than restart the analysis.
- Feedback leads with strengths and offers no more than three high-impact opportunities.
- Suggestions remain specific and actionable.

### Options, iteration, and self-identification

- The skill identifies itself in the first response with one short line.
- It does not repeat the introduction on later turns unless asked.
- Microcopy offers two to three distinct options with one-line rationales.
- Short-form copy offers two versions or a recommended revision plus a bolder alternative.
- Long-form work proposes structure first and offers alternative treatments of the highest-impact section when rewriting.
- Each option explains its emphasis or tradeoff, such as clearer, warmer, shorter, more specific, or more inclusive.
- Every substantive drafting turn provides a concrete next step and invites iteration.
- Follow-up turns build on the chosen direction instead of restarting the analysis.

## Test Procedure

1. Record the skill version, date, model, harness version, and scenario ID.
2. Create a fresh session.
3. If instrumented logging is available, prefix Turn 1 with `UXWC_TEST_MODE=1`.
4. Paste Turn 1 exactly.
5. Save the full response, including any `uxwc-test-log` block.
6. Paste Turn 2 exactly.
7. Save the full response.
8. Paste Turn 3, where applicable.
9. Save the full response.
10. Complete the evaluation checklist.
11. Write the strengths, issues, and improvement ideas.
12. Copy `testing/reports/report-template.md`, complete every section, and save the report in `testing/reports/`.
13. Check the transcript against the Transcript Format before submitting the report.
14. Complete the Reference-Use Evaluation for every applicable reference, using the test log when available.

## Failure Categories

- **Activation failure:** The skill does not activate or uses the wrong workflow.
- **Intake failure:** It asks excessive questions, misses a material constraint, treats source material as a rewrite object, or skips a needed working plan.
- **Hallucination:** It invents an unavailable fact, link, deadline, service, or policy.
- **Boundary failure:** It implies eligibility or publishes an internal-only detail.
- **Molecule failure:** It ignores or misuses the required content strategy element.
- **Style failure:** It violates Library voice, naming, terminology, or citation rules.
- **Interaction failure:** A follow-up does not adapt usefully.

## Required Artifacts

Each completed automated test should produce:

- the complete tested transcript;
- the completed evaluation checklist;
- a reference-use assessment for each applicable file in `references/`;
- the `uxwc-test-log` block when test-mode logging is enabled;
- evidence that the skill offered useful options, explained tradeoffs, provided next steps, and invited iteration;
- at least one strength;
- all defects or concerns;
- at least one concrete skill improvement;
- a recommendation to run again, revise the skill, or revise the scenario.

Use this report name pattern: `YYYY-MM-DD-scenario-ID-model.md`.

## Suggested Initial Run Order

Run A1, A2, A3, A4, A5, A6, and A7 in fresh sessions after changing the skill. This sequence covers the five usage modes, three service-definition types, structured content, microcopy, source-material intake, and a boundary test. If a scenario exposes a systemic issue, finish the current scenario and record the issue for the next skill revision.
