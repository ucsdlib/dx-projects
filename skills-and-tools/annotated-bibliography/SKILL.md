---
name: annotated-bibliography
description: Build faithful, source-backed research reading lists, landscapes, and annotated bibliographies. Use when the user asks for a reading list, annotated bibliography, literature review, comprehensive research, sources for or against a claim, or what research says about a topic.
---

The working product name is **Reading List**. The technical and compatibility name remains `annotated-bibliography`. Treat an “annotated bibliography” request as valid activation and as the full deep-work mode.

The skill prepares and supports human reading. It does not replace source engagement. Screen, verify, map, and organize evidence so the user can decide what to read next with confidence.

## Non-Negotiables

- **Faithful over helpful:** represent what retrieved sources actually say. Label inference. Never manufacture controversy, consensus, or false precision.
- **UC Library Search first.** Use the `uc-library-search` skill to build strategies when available, then execute through the Primo pathways.
- **Verify before annotating.** Confirm citation metadata and content provenance. Record access level and confidence.
- **Preserve provenance.** Every theme, question, selected source, and research direction must trace to a query, retrieved source, or user input.
- **Trace execution.** Maintain stage and reference logs when using the manifest. A reference log is the best available record that the skill used a reference file, but it is model-reported rather than a filesystem hook.
- **State limitations.** Skips, fallbacks, low fidelity, missing full text, weak evidence, and coverage gaps are findings, not embarrassments.
- **Keep the human in control.** The agent screens and orients; the user chooses depth, path, and interpretation.

## Operating Workflow

1. **Intake.** Build a working question, scope brief, and breadth decision. Ask two to four material clarifications only when needed; otherwise proceed with a stated default.
2. **Landscape.** For most ordinary requests, run a focused UC Library Search pass first. Identify descriptive themes and source-backed questions before deep work. Skip the landscape for research-paper-scoped questions, explicit full-bibliography requests, or complete re-run briefs.
3. **Selection.** Present a scannable landscape and one primary next-step offer: reading list, full annotated bibliography, refinement, search log, or a user-defined path.
4. **Deep work.** Reuse relevant landscape sources before searching again. A reading list is curated, not exhaustive unless requested and supported. Full bibliographies use the existing fidelity-first annotation structure.
5. **Refinement.** Preserve valid state when scope changes, avoid rerunning unchanged queries, and curate new and existing candidates under the same tier rules.
6. **Audit.** Keep the search log out of ordinary output. Render it on request; create a machine-readable manifest in test mode.

Do not start full bibliography work until the user has seen the landscape or explicitly bypassed it.

In test mode, create and maintain a manifest with `scripts/update_run_log.py`, log every major stage transition, and append a record whenever a reference file informs a decision. Run `scripts/validate_run.py` before ending the run.

## References

- Read [references/interaction-model.md](references/interaction-model.md) for run state, manifests, clarification and stage rules, landscape sufficiency, follow-up mapping, and refinement behavior.
- Use [scripts/update_run_log.py](scripts/update_run_log.py) in test mode to maintain stage and reference logs; use [scripts/validate_run.py](scripts/validate_run.py) before ending a manifest-backed run.
- Read [references/response-templates.md](references/response-templates.md) before rendering intake, landscape, reading-list, bibliography, refinement, or search-log responses.
- Read [references/search-and-selection.md](references/search-and-selection.md) for UC Library Search execution, adaptive screening, tool order, breadth tiers, curation, themes, questions, source-link resolution, and search-log detail.
- Read [references/annotation-rules.md](references/annotation-rules.md) before full-bibliography work, confidence assignment, weak-evidence reporting, or closing human next steps.
- Read [references/primo-search-api.md](references/primo-search-api.md) when the keyed Primo Search API is available.
- Read [references/primo-pnx-api.md](references/primo-pnx-api.md) when using the PNX REST fallback or troubleshooting Primo extraction.

## Quality Check

Before responding, verify:

1. The working question, breadth basis, and material scope are clear.
2. Search decisions, skips, fallbacks, and coverage limitations are recorded.
3. Themes and questions have source provenance; generated directions are labeled separately.
4. Claims, quotes, access levels, and confidence ratings are faithful to retrieved evidence.
5. The output is scannable and offers a clear next step without asking repeated questions.
