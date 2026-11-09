# Test Planning

## Purpose

This reference provides detailed guidance for the first four phases of the test planning workflow: gathering information, analyzing the skill, setting objectives, and building testing protocols.

## Phase 1: Gather Information

Before analyzing the skill under test, ask the user for:

- Skill name, purpose, primary modes, and intended user.
- Whether they can provide the skill's `SKILL.md` and relevant reference files, or a path to them.
- Known strengths, limitations, failure modes, and prior test reports.
- High-value user materials, example inputs, policies, or source-content types the skill processes.
- Activation expectations: natural discovery, explicit invocation, both, or unknown.
- Optional observability: test-mode marker, tool or reference logs, harness metadata.
- Preferred output location for testing artifacts. The default is `testing/` within the skill's repository, but the user may specify a different path. Record this path and use it consistently for all artifacts.
- Whether the user has an editable copy of the skill or is testing the installed version. If they only have the installed skill, they can read the skill files from the harness path (e.g., `~/.tritonai-harness/codex/skills/<skill-name>/`) for test planning. The synthesis output is then framed as a handoff report to share with the developer rather than a change backlog the tester implements.

Ask what the user is most concerned about. Early stated concerns often identify the highest-value scenarios.

If a testing directory already exists at the default or user-specified location, detect existing artifacts. Prior test reports from earlier rounds are valuable input for test planning (known failure modes, regression baseline). Present what exists and ask the user whether to create a new run subdirectory, use a different location, or otherwise handle existing files. Never silently overwrite existing test artifacts.

## Phase 2: Analyze the Skill

Read the skill's `SKILL.md` and applicable reference files. Identify:

- **Modes:** Distinct workflows or response types the skill handles. A skill that only drafts copy has one mode; one that drafts, evaluates, and manages tone has three.
- **Intended outcomes:** What the skill promises the user will accomplish.
- **Constraints:** Non-negotiable rules, review gates, boundaries, or safety requirements.
- **Failure points:** Where the skill's instructions are ambiguous, where it might overreach, or where it depends on reference files that could be misapplied.

Convert unclear promises into testable questions. For example, "handles feedback gracefully" becomes "when the user asks for a revision, does the skill preserve earlier constraints and identify what changed?"

## Phase 3: Set Round Objectives

Identify three scenarios by default. Increase only when the skill is complex enough to justify it. Prioritize risks by:

- Primary and high-risk modes.
- Routine work plus edge cases.
- Activation, intake, wrong-tool behavior, accuracy, boundaries, privacy, safety, accessibility, citations, revision handling, and release readiness.
- Whether the concern is best detected through automated behavior, human judgment, or both.

Present the selected risks and rationale to the user before building scenario cards.

## Phase 4: Build Testing Protocols

Create both protocols at this stage. Each protocol includes:

- Scenario cards for each scenario.
- Execution steps.
- Reporting templates (copied from assets).

The automated protocol should be ready for the skill to guide the user through. The human protocol should be ready for the user to run independently with participants.

## Presenting the Plan

When presenting the plan for review, summarize:

- Number of scenarios and which modes or risks each covers.
- One sentence per scenario describing the situation and what is being tested.
- Whether each scenario uses natural or explicit activation.
- The default turn count (one initial request plus up to two follow-ups).

Ask the user to confirm or flag concerns before proceeding.
