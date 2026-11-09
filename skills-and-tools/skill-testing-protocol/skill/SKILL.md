---
name: skill-testing-protocol
description: Design, run, and synthesize fresh-session automated tests and lightweight human participant tests for another TritonAI or Codex skill.
---

# Skill Testing Protocol

Guide a user through testing another skill in a structured but lightweight process. The workflow gathers skill context, builds a risk-based test plan with scenario cards, presents it for user review, then guides the user through automated testing and hands off a human testing protocol for independent execution.

## Core Workflow

Follow these phases in order. Do not proceed to running tests until the user has reviewed and approved the testing protocols and scenario cards.

1. **Gather information.** Ask the user for the skill under test's name, purpose, modes, intended user, known risks, and any example materials they can provide. Ask whether they have an editable copy of the skill or are testing the installed version. Read the skill's `SKILL.md` and relevant reference files (from the user's local copy or the harness's installed path). See [references/test-planning.md](references/test-planning.md) for detailed guidance.
2. **Analyze the skill.** Identify its modes, intended outcomes, constraints, and failure points. Convert unclear promises into testable questions.
3. **Set round objectives.** Identify three scenarios by default; increase only when the skill is complex enough to justify it. Prioritize by primary modes, edge cases, and risk type.
4. **Build testing protocols.** Create both the automated testing protocol and the human testing protocol, including scenario cards, execution steps, and reporting templates. See [references/scenario-design.md](references/scenario-design.md) for card design and [references/automated-testing.md](references/automated-testing.md) and [references/human-testing.md](references/human-testing.md) for execution procedures.
5. **Review and validate.** Present the complete protocols and scenario cards to the user. Ask them to confirm that scenarios are realistic, risks align with their concerns, and expected behaviors match their understanding. Revise before proceeding.
6. **Run automated tests.** Execute all scenarios autonomously in fresh sessions (e.g., via `codex exec` or an equivalent subagent mechanism). For each scenario, submit the exact user turns, capture the full transcript, score the rubric, and save the report. After all scenarios are complete, generate a run summary and present findings to the user. See [references/automated-testing.md](references/automated-testing.md). The human testing protocol is handed off for the user to run independently.
7. **Synthesize findings.** After scoring all sessions, group recurring issues by severity and root cause, then recommend specific skill changes. If the tester is not the developer, frame the output as a handoff report to share with the developer. See [references/synthesis.md](references/synthesis.md).

## Communication

Use [references/response-template.md](references/response-template.md) to structure interactions during each workflow phase. Keep responses concise and actionable.

## Templates

Copy or adapt the following templates as needed:

- Scenario card: [assets/scenario-card-template.md](assets/scenario-card-template.md)
- Automated report: [assets/automated-report-template.md](assets/automated-report-template.md)
- Human report: [assets/human-report-template.md](assets/human-report-template.md)
- Run summary: [assets/run-summary-template.md](assets/run-summary-template.md)
- Findings synthesis: [assets/findings-synthesis-template.md](assets/findings-synthesis-template.md)

## Scope

This skill tests conversational and agentic skills in TritonAI or Codex. It does not replace product, legal, accessibility, security, or compliance review, and it does not handle continuous integration or fully unattended test orchestration.

Human testing guidance is designed for informal testing within the local unit or team. It defers to local policy for consent language, IRB requirements, or formal research regulations.
