# Synthesis and Iteration

## Purpose

This reference provides guidance for synthesizing findings after all automated and human sessions are scored.

## When to Synthesize

Synthesize after all sessions in a round are complete and scored. Do not change the skill until synthesis is done.

## Process

1. **Score all sessions before changing the skill.** Ensure every scenario has a completed report.
2. **Group similar findings and de-duplicate causes.** A single root cause may explain findings across multiple scenarios.
3. **Separate model or harness effects from skill-guidance effects.** A failure caused by the model's capability differs from one caused by unclear instructions.
4. **Select the smallest set of changes likely to resolve high-impact findings.** Prefer narrow corrections over broad rewrites.
5. **Trace each planned change to at least one piece of evidence.** Reference the specific scenario, session, and rubric dimension.
6. **Add regression scenarios for important fixes.** A regression scenario tests whether a fix causes a previously working behavior to break.
7. **Update the backlog instead of accumulating broad universal rules.** Log specific, evidence-backed changes rather than general advice.
8. **Rerun affected scenarios and a small regression set after changes.** Confirm improvements and check for regressions.

## Grouping Findings

Group findings by:

- Recurring failure pattern (e.g., "skill does not preserve constraints across revisions").
- Root cause: skill instructions, reference files, tool behavior, model behavior, harness context, or scenario quality.
- Evidence across scenarios (which sessions showed this issue).
- Severity and confidence.
- Whether it is a regression from an earlier round.

## Prioritizing Changes

Address in order:

1. Blockers that produce incorrect, harmful, or fundamentally unusable output.
2. High-impact issues that break important workflows or could materially mislead users.
3. Moderate issues that cause friction, rework, or reduced trust.
4. Minor polish issues only after higher-severity items are resolved.

## Change Backlog

For each planned change, record:

- Finding ID or short description.
- Root cause.
- Evidence (scenario, session, rubric dimension).
- Proposed change (which file, which rule, which reference).
- Regression scenario needed (yes/no).
- Status: planned, in progress, done, or deferred.

Use `assets/findings-synthesis-template.md` and `assets/run-summary-template.md` for consistent formatting.

## Handoff Reports

When the tester is not the developer and does not have an editable copy of the skill, the synthesis output is a handoff report. The synthesis process (grouping, root-cause analysis, prioritization) is identical; only the audience and next step differ.

For a handoff report:

- Frame the run summary and findings synthesis as documents to share with the developer, not as a change backlog the tester implements.
- Include enough root-cause detail (which file, which rule, which reference) that the developer can act without re-testing.
- Preserve evidence links to specific scenarios and sessions so the developer can verify findings.
- Note whether a future testing round is recommended after the developer makes changes.

The change-backlog format above remains useful in a handoff context as a prioritized list of proposed changes, but ownership of implementation transfers to the developer.
