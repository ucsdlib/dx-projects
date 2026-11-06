# Interaction Model Reference

Use this reference when planning an invocation, asking clarifications, moving between modes, preserving state, refining scope, creating a test manifest, or rendering an audit.

## Run State

Maintain lightweight in-conversation state for every run. It need not be written to disk in the MVP, but it must be stable enough to render follow-ups and audit summaries.

| Field | Purpose |
|---|---|
| `run_id` | Distinguishes one run from another in the same session. |
| `working_question` | The concise question or topic actually being addressed. |
| `context` | Clarifications, audience, discipline, time frame, source-type constraints, and other scope inputs. |
| `breadth_tier` | Focused, comprehensive, or exhaustive, with its selection basis. |
| `output_mode` | Landscape, reading list, full bibliography, search log, refinement, or undefined. |
| `queries` | Query text, tool, purpose, page count, fidelity, and decisions. |
| `sources` | Stable source ID, citation, primary link and source, library link when available, access level, source type, study design, evidence base, credibility, confidence, and connection type. |
| `themes` | Stable theme ID, plain-language name, descriptive summary, related source IDs, and support confidence. |
| `questions` | Stable question ID, question text, related theme IDs, supporting source IDs, and confidence. |
| `selected_paths` | Follow-up actions the user has chosen. |
| `limitations` | Access, coverage, fallback, pruning, and evidence limitations. |
| `stage_log` | Ordered record of major workflow transitions. |
| `reference_log` | Model-reported record of reference files consulted and the decisions they informed. |

Retain stable source IDs across stages so later output can connect sources to queries, themes, questions, and follow-up work.

## Run Manifests

| Approach | Benefits | Costs | Role |
|---|---|---|---|
| In-conversation state | No filesystem side effects; low overhead; fast; keeps user-facing responses clean | Can be lost through context compression; hard to inspect or replay; long runs consume context | Always use as active state |
| Run manifest | Durable, inspectable, replayable, useful for provenance review and comparisons | Adds file management, schema maintenance, cleanup, and privacy considerations | Required in test mode; optional by user request or for deep runs |

A manifest is canonical machine-readable state, not a second source of truth. In test mode, create `annotated-bibliography-runs/<run_id>/bibliography-run.json` and optionally `search-log.md` in the same directory. If no output directory is supplied, use the current working directory and tell the user where files were written.

Minimum manifest content:

1. `schema_version`, `run_id`, creation and update timestamps.
2. Working question, scope brief, and breadth-tier decision.
3. Query records with tool, text, purpose, pages screened, fidelity estimates, and adaptive decisions.
4. Source records with stable IDs, full citations, primary link and source, library link when available, access level, source type, study design, evidence base, credibility, confidence, connection type, and linked queries.
5. Theme and question records with stable IDs, provenance, supporting source IDs, and support type.
6. Selection, exclusion, and pruning decisions.
7. Coverage, access, fallback, skip, and evidence limitations.
8. `stage_log` entries for intake, landscape, selection, deep work, refinement, and audit.
9. `reference_log` entries for reference files that informed workflow, templates, search, annotation, or API decisions.

Serialize at checkpoints when needed. Do not let manifest maintenance delay or displace fidelity, verification, or user-facing work.

### Stage and Reference Logs

Use `scripts/update_run_log.py` to create and update a manifest in test mode. Each stage event should include the stage name, status, and a concise note about the decision or artifact produced. Each reference event should include the reference path, purpose, and a short evidence note naming the rule, template, schema, or API recipe that informed the response.

```json
{
  "stage_log": [
    {
      "stage": "landscape",
      "status": "completed",
      "note": "Focused Primo landscape produced six themes and five source-backed questions.",
      "timestamp": "2026-10-21T12:00:00Z"
    }
  ],
  "reference_log": [
    {
      "reference": "references/interaction-model.md",
      "purpose": "Initialize run state and landscape stage",
      "evidence": "Used stage definitions and landscape-sufficiency signals before search.",
      "timestamp": "2026-10-21T11:58:00Z"
    }
  ]
}
```

The reference log is a fidelity aid, not proof of file access. Treat it as model-reported provenance and inspect it alongside the output and manifest.

Serialize at checkpoints when needed. Do not let manifest maintenance delay or displace fidelity, verification, or user-facing work.

## Clarification Policy

- Proceed without clarification when the prompt already contains enough scope to search responsibly.
- Otherwise ask two to four concise questions in one turn.
- Ask only for material information: refined question, discipline, time frame, perspective, research output, intended audience, source-type constraints, or breadth.
- Offer concrete defaults when possible.
- Do not ask about tier and clarification separately unless necessary.
- If the user declines to answer, proceed with the recommended default and record the basis.

Useful intake questions:

1. “Do you want a quick overview, an annotated reading list, or an exhaustive survey?”
2. “Should the search prioritize recent work, historical work, empirical studies, theory, policy, or a mix?”
3. “Should it include practitioner and policy sources, or focus primarily on scholarly work?”
4. “Is there a discipline, population, geography, or time period that must be included or excluded?”

Open with a one-line working question and note that the user may correct it. If no clarification is needed, state the working question, constraints, and chosen tier in one line and proceed.

## Stages

| Stage | Input | Responsibility | Output |
|---|---|---|---|
| Intake | User prompt and context | Confirm scope and choose breadth | Working question and scope brief |
| Landscape | Scope brief and UC Library Search strategy | Screen a focused result set and map themes and questions | Landscape response and run state |
| Selection | Landscape response | Offer reusable follow-up paths | User-selected path |
| Deep work | Selected path and existing source set | Produce reading list, bibliography, or targeted expansion | Requested output with provenance |
| Refinement | Scope change | Preserve valid state and search incrementally | Updated landscape, reading list, or bibliography |
| Audit | User request or test mode | Reconstruct the full pipeline | Search log |

The default depth path is a focused landscape followed by user-selected deep work at comprehensive or exhaustive breadth. Prompt markers such as “quick,” “brief,” “literature review,” “thorough,” “publication-grade,” or “research paper” may override it. Skip the landscape when the question is already narrowly scoped to research-paper level, when the user explicitly requests a full bibliography without a landscape, or when a re-run provides a complete scope brief.

Record whether the landscape was selected, skipped by scope judgment, skipped by user instruction, or bypassed by an explicit full-run request.

During the landscape:

- Identify major themes in on-topic and adjacent results.
- Identify questions sources explicitly ask or clearly imply.
- Identify strong overviews, reviews, meta-analyses, scoping reviews, or bibliometric analyses when present.
- Record provenance and search decisions.
- Stop when the landscape has enough coverage to describe major themes and questions, not when every relevant source has been found.
- Do not produce the full annotated bibliography unless the user explicitly asks for it.

## Landscape Sufficiency

Use purpose-aware saturation signals rather than a fixed query budget:

1. **Concept coverage:** every core concept has at least one on-topic source or a documented absence.
2. **Perspective coverage:** major intended perspectives have a source or documented gap.
3. **Theme saturation:** recent pages and component searches are mostly mapping sources into known themes rather than revealing new themes.
4. **Question novelty:** recent sources mostly answer or refine existing questions rather than producing a stream of unseen source-backed questions.
5. **Candidate stability:** additional high-confidence candidates strengthen known themes rather than create a competing landscape.
6. **Fidelity:** adaptive screening permits stopping and the query is not materially biased toward one concept or source type.
7. **Purpose fit:** a quick overview can stop earlier than a comprehensive survey.

As a practical signal, if two consecutive high-fidelity pages or component searches introduce no new theme or source-backed question, treat the landscape as saturated for the current purpose. If more than about one third of a recent page supports a new theme or question, continue searching or run a targeted component query. Log these heuristics; do not treat them as proof of complete coverage.

## Follow-Up Paths

After the landscape, offer:

1. **Reading list:** select one or more themes or questions.
2. **Full annotated bibliography:** produce the complete fidelity-first bibliography.
3. **Refine scope:** narrow, broaden, reframe, add constraints, or redirect.
4. **Search log:** show the full pipeline and audit details.
5. **User-defined path:** another theme, question, comparison, output, or source set.

Use ordinary prose or a short list. Accept any reasonable follow-up, but map it internally to a supported mode. Ask one primary next-step question; do not repeat confirmation after the user names a path.

If a selected path remains at landscape level, reuse the landscape source set. If it narrows to a theme or question, reuse relevant landscape sources first, then run targeted searches at the selected breadth tier. A broad reading list may be a curated subset of the landscape; never present it as exhaustive unless the user explicitly requests exhaustive work and the search supports that claim.

## Refinement

When scope changes:

1. Restate the changed scope in one line.
2. Say what remains valid from the prior run.
3. Say what will be newly searched or discarded.
4. Say whether the breadth tier changed.
5. Produce a short result summary; use the landscape format if the landscape materially changes.
6. Ask one next-step question.

Avoid rerunning unchanged queries. New results compete with existing sources under the same tier and curation rules.
