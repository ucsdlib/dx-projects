# Skill Testing Protocol

A reusable TritonAI/Codex skill that helps a small team design, run, score, and synthesize tests for another skill.

The tester may be the skill's developer (who has an editable copy) or a non-developer assigned to testing (who has only the installed skill and shares findings with the developer).

## What This Skill Does

- Guides the user through gathering skill context, building a risk-based test plan, and creating scenario cards.
- Runs fresh-session automated tests autonomously (e.g., via `codex exec` or an equivalent subagent mechanism) after the user approves the plan.
- Saves transcripts, scored reports, and run summaries to the user's preferred output location.
- Creates a lightweight human testing protocol for the user to run independently with participants from their local unit.
- Synthesizes findings across automated and human rounds into a prioritized change backlog.

## Usage

Invoke with `$skill-testing-protocol` and provide the skill under test. The skill will:

1. Ask about the skill's purpose, modes, risks, and example materials.
2. Analyze the skill and build a testing plan with three scenarios by default.
3. Present scenario cards for your review.
4. After approval, run all automated scenarios and generate a run summary.
5. Provide a human testing protocol for you to run with participants.
6. Synthesize findings and recommend specific skill changes.

## Output Location

Testing artifacts default to a `testing/` directory within the skill's repository. If the tester only has the installed skill (no local repository), the default shifts to a `testing/` directory in the tester's working directory:

```text
testing/
|-- scenarios/
|-- transcripts/
|-- reports/
`-- runs/
```

You may specify a different output location during the gather-information phase. If a testing directory already exists with prior artifacts, the skill will detect them and ask how to proceed—prior test reports are treated as evidence, not overwritten.

When the tester is not the developer, the synthesis output is framed as a handoff report to share with the developer, who decides what to implement.

## Structure

```text
skill-testing-protocol/
|-- SKILL.md                  Entrypoint with core workflow
|-- PRD.md                    Product requirements
|-- agents/openai.yaml        UI metadata
|-- references/               Procedures and communication templates (loaded on demand)
`-- assets/                   Output templates (copied or adapted into user artifacts)
```

`references/response-template.md` guides how the skill communicates during each workflow phase. The `assets/` templates are copied or adapted into the user's testing output (scenario cards, reports, run summaries, and synthesis).
