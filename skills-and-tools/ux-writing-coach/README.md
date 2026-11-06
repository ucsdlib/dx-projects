# UX Writing Coach

A Codex skill that helps UC San Diego Library staff plan, draft, revise, and evaluate user-centered web and interface copy. It routes requests through Library-specific scenario guidance and applies UC San Diego and Library voice, terminology, editorial style, inclusive-language guidance, and NN/g UX writing principles.

## Status

Draft V2, with `PRD.md` revision 2026-11-05. The latest skill update is the structured-evaluation Plan Gate update. Targeted regression tests for scenarios A4 and A6 pass; a full A1 through A7 regression is still pending.

All output is coaching material, not final or approved copy. A human expert should review anything before publication.

## What It Does

- Classifies the request as intake, drafting, feedback, evaluation, or a combination, and distinguishes source material from a rewrite object.
- Applies the Plan Gate to structured Library content, such as service pages, offering cards, eligibility copy, contact sections, and evaluations of those types.
- Uses reusable response templates for plan-only turns, plan revisions, direct drafting, drafting after an approved plan, feedback or evaluation, and pre-send consistency checks.
- Offers options-first drafts with tradeoffs and concrete next steps instead of presenting a single authoritative rewrite.
- Preserves factual meaning, separates public-facing information from internal context, and flags facts, terminology, links, or eligibility conditions that require human verification.

## Scope

The skill prioritizes Library website writing about services, collections, spaces, and expertise. It also supports interface text, forms, wayfinding, research guides, events, policies, help content, alerts, and related UX writing.

It does not provide:

- full WCAG or accessibility conformance audits;
- CMS publishing or page-editing workflows;
- general campus copy outside the Library;
- legal, policy, brand, or accessibility approval;
- translation or localization.

## Repository Contents

```text
SKILL.md                            Skill entrypoint and workflow
agents/openai.yaml                  UI metadata
references/                         Packaged style and workflow guidance
testing/                            Automated and human test plans, scenarios, and reports
PRD.md                              Living product requirements
CHANGELOG.md                        Dated product and workflow history
research/                           Build-time source corpus; not packaged with the skill
```

The packaged skill consists of `SKILL.md`, `agents/`, and `references/`. The `testing/`, `PRD.md`, `CHANGELOG.md`, and `research/` artifacts support development and validation; they are not runtime dependencies.

## Reference Structure

- **Routing and workflow:** `references/content-scenarios.md` selects the smallest relevant reference set; `references/working-plan.md` defines input classification and the Plan Gate; `references/response-templates.md` defines response shape; `references/content-strategy-elements.md` provides structured content molecules.
- **Style and UX principles:** `references/library-style.md` defines source hierarchy, AI-tells, and verification; `references/voice-and-messaging.md` defines voice, tone, and messaging; `references/ux-writing-principles.md` defines copy sizes, scanning, brevity, jargon handling, and audience fit.
- **Domain details and provenance:** `references/style-mechanics.md` covers campus and web style; `references/library-terminology.md` contains exact Library names and terms; `references/inclusive-language.md` covers inclusive language and UX patterns; `references/source-citations.md` maps labels to canonical sources.

For any task that drafts, rewrites, reviews, evaluates, or changes copy, `references/voice-and-messaging.md` is required, not optional.

## Example Prompts

- “Revise this paragraph for a Library service page.”
- “Give me three button labels for requesting an item through interlibrary loan.”
- “Review this error message and suggest clearer options.”
- “Evaluate this borrowing-policy page for students, staff, and community borrowers.”
- “Rewrite this policy so it leads with what users can do while preserving the limit.”
- “Check this draft against Library terminology and pre-send consistency rules.”

## Installation

Install the packaged skill into your Codex skills directory:

```bash
mkdir -p "$CODEX_HOME/skills/ux-writing-coach"
rsync -a --delete SKILL.md agents references "$CODEX_HOME/skills/ux-writing-coach/"
```

If `CODEX_HOME` is not set, use `~/.codex/skills/ux-writing-coach` or your harness’s equivalent skills directory.

To refresh an existing installation after making changes, rerun the same `rsync` command.

## Testing

The reusable test suite covers seven Library content scenarios, labeled A1 through A7. Start with `testing/scenarios/README.md` for the scenario index, then use:

- `testing/automated-testing-plan.md` for the fresh-session protocol, scoring checklist, and reporting rules.
- `testing/human-testing-plan.md` for facilitated Library staff sessions.
- `testing/reports/report-template.md` for complete test reports.
- `testing/runs/2026-11-05-testing-summary.md` for the latest skill changes, findings, current state, and regression priorities.

To enable structured test logs in automated runs, prefix the first user turn with `UXWC_TEST_MODE=1`. The log records scenario routing, input classification, Plan Gate behavior, response template, copy size, molecule, references used, and next-step type.

## Maintenance

- Update style guidance in `references/`, not in `SKILL.md`.
- Keep `SKILL.md` focused on workflow, routing, and quality rules.
- Add a new source to `references/source-citations.md` with its canonical URL, verification date, scope, and hierarchy level before citing it.
- When style rules change, update the relevant reference file and the source citation date.
- Keep `research/` for source material and context. Do not cite those local files in user-facing output.
- Before a release, refresh the installed skill with the installation command, run the skill validator, and run the A1 through A7 regression suite.
- Update `PRD.md` before substantive behavioral, scope, or workflow changes, and record the completed change in `CHANGELOG.md`.

## Validation

In this TritonAI Harness environment, run the packaged skill validator from the repository root or the installed skill folder:

```bash
python3 "$HOME/.tritonai-harness/codex/skills/.system/skill-creator/scripts/quick_validate.py" .
```

For substantive changes, follow `testing/automated-testing-plan.md`. Representative coverage should include service pages, policies, forms and interface copy, errors, wayfinding, research guides, events, and collections. Human review remains required for substantive style, policy, accessibility, or audience-fit changes.
