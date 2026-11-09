# Skill Testing Protocol — Changelog

This changelog records product and workflow changes in reverse chronological order.

## 2026-11-06 — Dual-role support: non-developer testers

### Added or refined

- Added support for testers who are not the skill's developer and do not have an editable local copy. The tester can read installed skill files from the harness path for test planning.
- Added a Phase 1 question: whether the user has an editable copy or is testing the installed version. This determines the default output location and the framing of the synthesis output.
- Adjusted the default output location: when the tester has an editable copy, artifacts default to `testing/` within the skill's repository; when the tester only has the installed skill, artifacts default to a `testing/` directory in the tester's working directory.
- Added a "Handoff Reports" section to `references/synthesis.md`. When the tester is not the developer, the synthesis output is framed as a shareable handoff report with root-cause detail and evidence links sufficient for the developer to act without re-testing.
- Updated `SKILL.md` Phases 1 and 7, `references/test-planning.md`, `references/automated-testing.md`, `PRD.md`, and `README.md` accordingly.

The workflow structure (gather → analyze → build → review → execute → synthesize) is unchanged. The tester's role is detected during the gather phase rather than asked as a separate step.

## 2026-11-06 — Moved response template from assets to references

### Refined

- Moved `response-template.md` from `assets/` to `references/` to follow the skill-creator anatomy: references hold instructions the model reads to guide its behavior, while assets hold files copied into user-facing output.
- Updated `SKILL.md` Communication section to link to `references/response-template.md`.
- Updated `README.md` structure section to clarify the distinction between references (procedures and communication templates) and assets (output templates copied into user artifacts).

The five output templates (`scenario-card-template.md`, `automated-report-template.md`, `human-report-template.md`, `run-summary-template.md`, `findings-synthesis-template.md`) remain in `assets/` because they are copied or adapted into the user's testing output.

## 2026-11-06 — Output-location flexibility and existing-directory handling

### Added or refined

- Added user-specified output location for testing artifacts during the gather-information phase; defaults to `testing/` within the skill's repository.
- Added existing-directory detection: the skill identifies prior testing artifacts, presents them to the user, and asks whether to create a new run subdirectory, use a different location, or otherwise handle existing files. Prior test reports are treated as evidence for regression comparison, never silently overwritten.
- Updated `references/test-planning.md` to ask for and record the output location, and to detect existing testing directories during Phase 1.
- Updated `references/automated-testing.md` to describe the default `testing/` path as overridable and to document existing-artifact handling before writing.
- Updated `PRD.md` Skill Under Test Inputs and Automated Testing Protocol sections accordingly.
- Created `README.md` with usage, output-location flexibility, and directory structure.

## 2026-11-05 — Autonomous execution redesign and directory structure

### Added or refined

- Redesigned Phase 6 from user-guided manual testing to autonomous agent-executed testing (e.g., via `codex exec` or an equivalent subagent mechanism).
- Rewrote `references/automated-testing.md` around autonomous execution; removed the manual "Guidance for the Skill's Interaction" section.
- Added an Isolation section distinguishing the tested session's neutral working directory (`/tmp/<skill>-tests`) from the testing agent's repository-based artifact directory (`testing/`).
- Added a recommended skill repository directory structure (`skill/`, `testing/scenarios/`, `testing/transcripts/`, `testing/reports/`, `testing/runs/`).
- Updated `assets/response-template.md` Phase 6 to reflect autonomous execution and post-run presentation.
- Updated `SKILL.md` Phase 6 and `PRD.md` to match.

## 2026-11-05 — Initial build and PRD clarifications

### Added

- Created the initial PRD with design principles, scope, test planning workflow, automated and human testing protocols, evaluation rubric, artifact structure, and synthesis guidance.
- Built the skill using the skill-creator initializer: `SKILL.md`, `agents/openai.yaml`, five reference files (`test-planning.md`, `scenario-design.md`, `automated-testing.md`, `human-testing.md`, `synthesis.md`), and six asset templates (`scenario-card-template.md`, `response-template.md`, `automated-report-template.md`, `human-report-template.md`, `run-summary-template.md`, `findings-synthesis-template.md`).
- Validator passed.

### PRD clarifications during initial build

- Clarified "create a concise, risk-based test plan by analyzing the skill under test" (not "turn the skill into a test plan").
- Clarified that transcripts save to a `testing/` directory and reports/summaries save to the working directory for user review.
- Clarified that the skill creates the human testing protocol but does not run human sessions; the user runs those independently.
- Added response templates to scope and artifacts for structuring user interactions during each workflow phase.
- Noted that the user should help supply or validate scenario context for realistic prompts.
- Restructured the Test Planning Workflow into a six-step gather → analyze → build → review → execute sequence with explicit user review before running tests.
- Scoped human testing to informal testing within the local unit; deferred consent language to local policy.
- Reduced default human participants from five to eight to three to five.
- Reduced default automated scenarios to three, with more only when complexity justifies it.
- Confirmed file-only v1 (no scripts) and separate automated/human report templates.
