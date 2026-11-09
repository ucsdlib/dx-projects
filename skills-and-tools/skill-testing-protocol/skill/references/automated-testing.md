# Automated Testing

## Purpose

This reference provides the procedure for running fresh-session automated tests. After the user has approved the testing protocols and scenario cards, the agent runs all scenarios autonomously in fresh sessions. The user does not need to manually start sessions, paste turns, or manage transcripts.

## Preconditions

1. The skill under test is installed or accessible in the TritonAI environment.
2. A clean session mechanism is available (e.g., `codex exec` or an equivalent subagent approach).
3. Scenario cards are saved in the working directory and available to the testing agent but not to the tested session.
4. Run the latest version of the skill before changing it.
5. The user has approved the testing protocols and scenario cards.

## Autonomous Execution

For each scenario:

1. Start a fresh session in a neutral working directory (e.g., `/tmp/<skill>-tests` rather than the skill's repository).
2. Submit only the exact user turns from the scenario card.
3. Stop after an activation failure unless activation is the focus of the scenario.
4. Capture the full transcript verbatim—including user turns, skill responses, file-loading or tool evidence, and unavailable signals.
5. Score against the rubric (see the Evaluation Rubric section in `SKILL.md` or the PRD).
6. Record severity, confidence, scenario verdict, and specific evidence in the report.
7. Save the transcript to the `testing/` directory and the scored report to the working directory.

After all scenarios are complete, generate a run summary and present the findings to the user. The user reviews results and decides whether to proceed to synthesis and skill revision.

## Isolation

Two directory contexts are involved:

- **Tested session working directory:** A neutral directory such as `/tmp/<skill>-tests`. The tested model runs here with no access to the skill's repository. It may access packaged skill references but not the `testing/` directory or other repository-only context.
- **Testing agent working directory:** The skill's repository. The testing agent runs here and saves transcripts, reports, and summaries to the `testing/` directory within the repository.

Do not provide the repository path, skill source, AGENTS instructions, or evaluation criteria in the tested session.

Scenario cards, rubrics, and prior findings belong to the testing agent, not the tested session.

## Instrumentation

If the skill under test supports an optional test-mode marker, the marker may request a structured test log. Use the log as self-reported evidence unless the harness exposes tool use. If no marker is available, evaluate conceptual alignment and mark direct reference use as "Not observed."

Recommend using markers sparingly because they add setup cost and can change behavior.

## Saving Artifacts

The testing agent saves artifacts to the output location established during the gather-information phase. When the tester has an editable copy of the skill, the default is `testing/` within the skill's repository. When the tester only has the installed skill (no local repository), the default is a `testing/` directory in the tester's working directory. The user may always specify a different path. The tested session's neutral working directory is always separate and unaffected. A typical skill repository is structured as:

```text
<skill-repo>/
|-- skill/
|   |-- SKILL.md
|   |-- agents/
|   |-- references/
|   `-- assets/
|-- testing/
|   |-- scenarios/
|   |-- transcripts/
|   |-- reports/
|   `-- runs/
|-- PRD.md
|-- CHANGELOG.md
`-- README.md
```

After each scenario, save:

- A transcript file to `testing/transcripts/` (e.g., `testing/transcripts/2026-11-05-scn01.md`).
- A scored report to `testing/reports/` (e.g., `testing/reports/2026-11-05-scn01-report.md`).

If a testing directory already exists with prior artifacts, the testing agent should detect them before writing. Prior test reports from earlier rounds are valuable for regression comparison. Ask the user whether to create a new run subdirectory, use a different location, or otherwise handle existing files. Never silently overwrite existing test artifacts.

After all scenarios are complete, save a run summary to `testing/runs/` (e.g., `testing/runs/2026-11-05-run01-summary.md`).

Use the templates in `assets/` for consistent formatting.
