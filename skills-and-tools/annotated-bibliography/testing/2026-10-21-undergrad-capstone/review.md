# Test Review: Undergraduate Capstone Landscape

## Test setup

- **Topic:** Factors that help undergraduate capstone projects and courses succeed.
- **Test type:** Forward landscape plus reading-list continuation.
- **Mode:** Test mode with a persistent manifest.
- **UC Library Search pathway:** Keyless Primo PNX REST fallback because no `PRIMO_KEY` was present.
- **Fresh-question check:** The topic is undergraduate capstone work rather than library science or the prior AI-ethics test question.

## Observations

| Area | Result | Evidence |
|---|---|---|
| Intake | Working question, audience, time frame, and source-type scope were stated before search. | `bibliography-run.json`, `landscape.md` |
| Landscape default | The run used the focused landscape path rather than jumping directly to a full bibliography. | `landscape.md` |
| UC Library Search first | Two PNX searches screened 26 records; 22 unique records were retained after title-level deduplication. | `search-log.md` |
| Landscape sufficiency | One component search added course-design and professional-preparation perspectives; the landscape was then treated as saturated for orientation. | `search-log.md` |
| Theme provenance | Six themes and six questions were linked to retrieved source IDs. | `bibliography-run.json`, `landscape.md` |
| Follow-up | The run produced a curated five-source reading list focused on course design and professional preparation. | `reading-list.md` |
| Reference trace | The manifest logged use of interaction, response-template, search-and-selection, and annotation-rule references. | `bibliography-run.json` |

## Strengths

1. The landscape stayed small enough for orientation: two API pages produced six themes and six source-backed questions without trying to annotate every candidate.
2. The component search surfaced a useful career-information-literacy source that broadened the initial project-based-learning framing.
3. The reading list reused landscape sources and labeled connection type, access level, and confidence.
4. Stage and reference logs provided a compact execution trace without turning the user-facing response into a search log.

## Issues to watch

1. The reference log is model-reported, not a filesystem hook. It should be treated as evidence of intended use, not proof that a file was read.
2. Several retrieved records lacked publication years in the PNX display fields. Crossref filled some gaps, but `landscape-10` and `component-01` still lack a clean year in the current manifest.
3. The current validator checks manifest structure and required logs, but it does not yet check the presence of landscape or reading-list output sections.
4. Full texts were not reviewed. All annotations remain abstract-level, so confidence and relevance judgments are provisional.

## Artifacts

- `bibliography-run.json`: canonical manifest with stage and reference logs.
- `landscape.md`: user-facing landscape response.
- `reading-list.md`: curated reading-list continuation.
- `search-log.md`: audit view of queries, screening, verification, and limitations.
- `screening.json`: deduplicated candidate-level screening records.
- `raw/`: API responses and Crossref/OpenAlex verification records.

## Recommended next test

Run a narrow-scope bypass test with a research-paper-level capstone question to see whether skipping the broad landscape improves usefulness or loses useful orientation.
