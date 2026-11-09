# PRD: Skill Testing Protocol

## Summary

Create a reusable TritonAI/Codex skill that helps a small team design, run, score, and synthesize tests for another skill. The workflow should combine fresh-session automated scenarios with lightweight human participant sessions. It should produce evidence-based skill changes without slowing the team down.

The skill is a testing coach and artifact generator. It does not replace the skill under test, diagnose all product quality problems, or turn testing into a heavyweight QA process.

## Users and Jobs

**Primary user:** A maintainer or evaluator of a TritonAI/Codex skill. The tester may be the skill's developer (who has an editable copy) or a non-developer assigned to testing (who has only the installed skill and shares findings with the developer).

**Key jobs:**

- Create a concise, risk-based test plan by analyzing the skill under test.
- Create realistic scenario cards that do not leak the tester's evaluation criteria into the tested session.
- Run fresh-session automated tests, save complete transcripts to a `testing/` directory, and save scored reports and run summaries to the working directory for user review.
- Create a human testing protocol for users to run with participants who represent the skill's actual users.
- Compare findings across automated and human rounds, group recurring issues, and recommend specific skill changes.
- Create a run summary and regression list for future rounds.

## Design Principles

1. **Test observable behavior.** Evaluate what the skill says, asks, references, refuses, or produces—not merely its source text.
2. **Keep sessions fresh.** Each automated scenario begins in a new session with no repository context unless the test deliberately tests persistence or reuse.
3. **Use realistic prompts.** Scenario cards should use believable work products, materials, ambiguity, and follow-ups. The user should help supply or validate this context so scenarios reflect actual usage.
4. **Minimize turns.** Use one authentic initial request and no more than three turns by default.
5. **Separate test and evaluation context.** The tested session should normally not receive the scenario card, rubric, prior findings, or skill source path.
6. **Prefer evidence over inference.** Preserve exact transcripts and mark unavailable signals as “Not observed.” Do not treat alignment with a reference as proof the skill loaded it.
7. **Small team, fast round.** A baseline automated round should fit in one working session; a first human round should use three to five participants with sessions of roughly 20 minutes or less.
8. **Protect the skill under test.** Do not change the skill during a test round. Batch changes after scoring and synthesis.

## Scope

### In scope

- A reusable testing protocol for conversational and agentic skills.
- Skill-under-test analysis, test objectives, and risk selection.
- Automated scenario creation, execution, transcript capture, and scoring.
- Human participant session design, roles, facilitation, ratings, and debrief.
- Generic and mode-specific rubrics for activation, intake, task quality, boundaries, safety, trust, efficiency, follow-up, and release-readiness.
- Transcript, report, run-summary, and synthesis templates.
- Response templates that guide how the skill interacts with the user during planning, review, testing, and synthesis.
- A lightweight change-backlog format for fixes, scenario revisions, and regressions.

### Out of scope for v1

- Continuous integration or fully unattended test orchestration.
- A replacement for a team’s product, legal, accessibility, security, or compliance review.
- Large-scale statistical evaluation.
- Automated code coverage or deterministic unit testing of non-skill code.
- Retaining personally identifying participant data beyond consented and necessary session artifacts.

## Skill Under Test Inputs

Before testing, gather only what is necessary:

- Skill name, purpose, primary modes, and intended user.
- `SKILL.md` and applicable reference files. If the user does not have an editable copy, they can read the installed skill files from the harness path; reading is sufficient for test planning.
- Whether the user has an editable copy of the skill or is testing the installed version. This determines whether the output location defaults to the skill's repository or the tester's working directory, and whether the synthesis output is framed as a change backlog (developer-owned) or a handoff report (shared with the developer).
- Known strengths, limitations, failure modes, and prior test reports.
- High-value user materials, example inputs, policies, or source-content types.
- Activation expectations: natural discovery, explicit invocation, both, or unknown.
- Optional observability: test-mode marker, tool/reference logs, harness metadata.
- Preferred output location for testing artifacts (defaults to `testing/` within the skill's repository).

If a testing directory already exists, the skill should detect existing artifacts during this phase. Prior test reports from earlier rounds are valuable input for test planning (known failure modes, regression baseline). The skill should present what exists and ask the user whether to create a new run subdirectory, use a different location, or otherwise handle existing files. It should never silently overwrite existing test artifacts.

## Test Planning Workflow

The workflow follows a gather → analyze → build → review → execute sequence. The skill guides the user through each step and does not proceed to running tests until the user has reviewed and approved the testing protocols and scenario cards.

### 1. Gather information

Before analyzing the skill, gather the inputs described under "Skill Under Test Inputs." The user should be asked what materials, examples, or context they can provide and which risks they already know about.

### 2. Analyze the skill

Read the skill and identify its modes, intended outcomes, non-negotiable constraints, and common failure points. Convert unclear promises into testable questions.

### 3. Set round objectives

Identify three scenarios by default; increase only when the skill is complex enough to justify it. Prioritize risks by:

- Primary and high-risk modes.
- Routine work plus edge cases.
- Activation, intake, wrong-tool behavior, accuracy, boundaries, privacy, safety, accessibility, citations, revision handling, and release readiness.
- Whether the concern is best detected through automated behavior, human judgment, or both.

### 4. Build testing protocols

Create both the automated testing protocol and the human testing protocol at this stage. Each protocol includes its scenario cards, execution steps, and reporting templates. The automated protocol should be ready for the skill to guide the user through. The human protocol should be ready for the user to run independently with participants.

Each card contains:

- Stable scenario ID and title.
- Mode or workflow focus.
- Assumed role, situation, and realistic input material.
- Exact user turns.
- Expected behavior or success criteria.
- Scoring focus and known failure modes.
- Whether natural activation, explicit invocation, or both apply.

Scenario cards are for testers only. They are not pasted into the tested session unless the experiment specifically tests their use.

### 5. Review and validate

Present the complete testing protocols and scenario cards to the user for review. Ask the user to confirm that the scenarios are realistic, that the risks align with their concerns, and that the expected behaviors match their understanding of the skill. Revise based on feedback before proceeding.

### 6. Run automated tests

Once approved, the agent runs all automated scenarios autonomously. For each scenario, it starts a fresh session (e.g., via `codex exec` or an equivalent subagent mechanism), submits the exact user turns, captures the full transcript, scores it against the rubric, and saves the report. After all scenarios are complete, it generates a run summary. The user reviews the results after the automated round is finished. The human testing protocol is handed off for the user to execute independently.

## Automated Testing Protocol

The agent executes each scenario autonomously in a fresh session (e.g., via `codex exec` or an equivalent subagent mechanism). The user does not need to manually paste turns or manage sessions. All artifacts are saved to the output location established during the gather-information phase (`testing/` by default, or a user-specified alternative).

For each scenario:

1. Start a fresh session in a neutral working directory.
2. Submit only the exact user turns from the scenario card.
3. Stop after an activation failure unless activation is the focus.
4. Save the full transcript verbatim—including user turns, skill responses, file-loading or tool evidence, and unavailable signals—to the `testing/` directory.
5. Score against the skill-specific and generic rubrics.
6. Record severity, confidence, scenario verdict, and specific evidence.

After all scenarios are complete, generate a run summary and present the findings to the user. The user reviews the results and decides whether to proceed to synthesis and skill revision.

### Instrumentation

If the skill under test supports an optional test-mode marker, the marker may request a machine-readable or structured test log. Use the log as self-reported evidence unless the harness exposes tool use. If no marker is available, evaluate conceptual alignment and mark direct reference use as “Not observed.”

The testing skill should recommend using markers sparingly because they add setup cost and can change behavior.

## Human Testing Protocol

This protocol is designed for informal testing within the local unit or team. It provides practical guidance for quick participant sessions but does not claim expertise in organizational policy, IRB requirements, or formal user-research regulations. If the user's testing context requires review or approval, they should follow their local unit's policies.

### Roles

| Role | Responsibility |
| --- | --- |
| Facilitator | Runs the session and avoids coaching the participant |
| Participant | Performs a realistic task |
| Recorder | Captures transcript, reactions, friction, ratings, and timing |
| Reviewer | Applies the rubric and proposes changes |

One person may combine roles for a first round, but a participant should not review their own session.

### Participants

Use three to five sessions for a first round within the local unit. Include participants who represent the skill's main user backgrounds; one participant unfamiliar with the skill is sufficient. There is no requirement to include an expert participant, though the skill may recommend one when the skill under test is specialized or high-stakes. Avoid letting one participant's completed scenario become another participant's training material.

### Session structure

1. Orientation: 1–3 minutes.
2. Setup and consent: 1–2 minutes. Use a brief verbal consent statement; the skill provides an editable template but defers to local policy for required language or review.
3. Task: 10–15 minutes.
4. Debrief: 3–5 minutes.
5. Participant ratings before the reviewer’s evaluation.

### Debrief questions

- What did the skill assume correctly or incorrectly?
- What output would you use or adapt first?
- What helped or hurt trust?
- What was confusing, wrong, missing, or unsafe?
- What would you do next in real work?
- What should the skill do differently?

### Human-only signals

Watch for issues automated tests may miss:

- Outputs that are technically correct but awkward, cold, over-formal, or over-enthusiastic.
- Workflows that add invisible work for users or staff.
- Missing audience, accessibility, policy, cultural, or lived-experience considerations.
- Excessive caveats that reduce usefulness.
- Confident claims the participant knows are wrong.

## Evaluation Rubric

Use one shared rubric for automated and human sessions. Mark each item `Pass`, `Partial`, `Fail`, `Not applicable`, or `Not observed`, with a one-sentence evidence note. Add skill-specific rows when needed.

### Core rubric

| Dimension | Evaluate whether |
| --- | --- |
| Activation | The skill routes to or activates appropriately without extra setup when that is the expected behavior. |
| Intake | It understands the request, uses supplied context, and avoids unnecessary questions. |
| Task quality | Its output is useful, coherent, appropriately scoped, and fit for the user’s goal. |
| Workflow compliance | It follows its own intended sequence, decision rules, and review gates. |
| Reference or tool use | Its relevant guidance or tools are applied; direct loading is reported only when observed. |
| Accuracy and boundaries | It avoids unsupported claims, preserves user-provided facts, and identifies uncertainty. |
| Safety, privacy, and ethics | It handles sensitive input, external actions, and permissions appropriately. |
| Audience and accessibility | It fits the intended audience and avoids exclusionary assumptions. |
| Voice and style | It matches the applicable product or organizational style without becoming generic. |
| Trust and verification | It communicates what is known, unknown, assumed, and ready for review. |
| Efficiency | It reduces time or effort compared with starting without the skill. |
| Follow-up handling | It improves usefully and preserves useful constraints across turns. |
| Release readiness | It distinguishes draft, review, and publication/action-ready output. |

### Severity

| Severity | Meaning |
| --- | --- |
| Blocker | Produces incorrect, harmful, unsafe, unlawful, or fundamentally unusable output. |
| High | Breaks an important workflow or could materially mislead a user. |
| Moderate | Causes friction, rework, reduced trust, or inconsistent quality. |
| Minor | Cosmetic or low-impact polish issue. |

## Artifacts

### Proposed skill structure

```text
skill-testing-protocol/
|-- SKILL.md
|-- agents/openai.yaml
|-- references/
|   |-- test-planning.md
|   |-- scenario-design.md
|   |-- automated-testing.md
|   |-- human-testing.md
|   `-- synthesis.md
`-- assets/
    |-- scenario-card-template.md
    |-- response-template.md
    |-- automated-report-template.md
    |-- human-report-template.md
    |-- run-summary-template.md
    `-- findings-synthesis-template.md
```

`SKILL.md` should carry only the shared purpose, mode-selection rules, core workflow, and links. Detailed procedures and templates should load only when relevant.

### Scenario template

The scenario template should contain:

- ID, title, mode, role, and focus.
- Source material or realistic input.
- Exact user turns.
- Expected behavior and success criteria.
- Scoring focus and known failure modes.
- Activation expectation.

### Response template

Response templates guide how the skill communicates with the user during each workflow phase: gathering information, presenting the testing plan, requesting review, guiding automated test execution, and presenting synthesized findings. These are separate from transcripts and reports; they shape the conversational structure of the testing workflow itself.

### Report template

Each report should contain:

- Metadata: date, tester, skill version, model, harness, session type, scenario card, and observability.
- Full transcript.
- Rubric table with results and evidence.
- Strengths, issues by severity, confidence, and improvement ideas.
- Recommendation: rerun, revise skill, revise scenario, or add scenario.

### Run summary template

Each round summary should contain:

- Run index and links to reports.
- Overall verdict by scenario.
- Cross-scenario patterns.
- Human versus automated differences.
- Top blockers and high-impact issues.
- Change backlog.
- Regression watch list.

### Findings synthesis template

The synthesis should group findings by:

- Recurring failure pattern.
- Root cause in skill instructions, references, tool behavior, model behavior, harness context, or scenario quality.
- Evidence across scenarios.
- Severity and confidence.
- Recommended skill or reference change.
- Whether it is a regression from an earlier round.

## Synthesis and Iteration

After a round:

1. Score all sessions before changing the skill.
2. Group similar findings and de-duplicate causes.
3. Separate model/harness effects from skill-guidance effects.
4. Select the smallest set of changes likely to resolve high-impact findings.
5. Trace each planned change to at least one piece of evidence.
6. Add regression scenarios for important fixes.
7. Update the backlog instead of accumulating broad universal rules.
8. Rerun affected scenarios and a small regression set after changes.

When the tester is not the developer and does not have an editable copy, the synthesis output is a handoff report. The tester shares the run summary and findings synthesis with the developer, who decides what to implement. The synthesis process (grouping, root-cause analysis, prioritization) is identical either way; only the audience and next step differ. A future testing round may be assigned back to the tester after the developer makes changes.

## Success Criteria

The skill is useful when a first-round maintainer can:

- Create a concise plan without external instruction.
- Run realistic fresh-session scenarios without leaking the rubric or scenario design.
- Capture full transcripts and score them consistently.
- Run or prepare a small human round.
- Identify at least one concrete, evidence-backed improvement.
- Tell whether a subsequent change improved behavior or introduced a regression.

A round is successful when:

- Automated scenarios cover the highest-risk modes.
- Human participants can complete the intended task without unnecessary friction.
- Important limitations, uncertainty, and unsafe boundaries are visible.
- Human and automated findings are reconciled into a prioritized backlog.
- No known blocker remains unrecorded or untraced.
