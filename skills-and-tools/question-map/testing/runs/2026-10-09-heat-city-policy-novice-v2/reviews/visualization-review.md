# Visualization Review

**Run ID:** 2026-10-09-heat-city-policy-novice-v2  
**Case ID:** heat-city-policy-novice  
**Reviewer:** OpenAI Codex — Visualization & Accessibility Reviewer  
**Persona:** Novice researcher preparing city council evidence  
**Review date:** 2026-10-09  

## Artifact reviewed

- [x] Default Mermaid view
- [x] Optional wide-card Mermaid view — same file includes the 340px source cards
- [x] Interactive HTML view — static inspection and a temporary data-injected harness only; the original standalone artifact was not directly testable
- [x] Linear Markdown companion

## Orientation tasks

| Task | Completed? | Answer | Difficulty 1–5 | Notes |
|---|---|---|---|---|
| State the main research question | Yes | “What should my city do about extreme heat and public health? I want recent research evidence to bring to a city council meeting.” | 1 | Stated clearly in the Markdown companion and Mermaid heading. |
| Name the main themes | Yes | Heat action plans and governance; intervention evidence and trade-offs; heat and health outcomes; heat plan evaluation methods; heat risk distribution. | 2 | The Markdown companion gives the clearest overview. |
| Find a source supporting one question | Yes | Example: Randazza et al., 2023 directly supports “What components do existing heat action plans include and omit…?” | 2 | Direct-support chains and citations are explicit in the Markdown companion. |
| Distinguish stated from inferred questions | Partially | The Markdown companion is clear; the Mermaid view uses “Stated” and “Inferred,” but also labels three source cards only as “Reviewed.” | 3 | “Reviewed” describes method, not whether the research question was stated or inferred. |
| Distinguish direct support from cross-cutting relevance | Partially | The Mermaid rendering and Markdown companion distinguish these concepts well. The temporary HTML harness showed the cross-cutting filter returned zero links. | 3 | See rendering and code defects below. |
| Use the relationship filter to isolate direct, secondary, cross-cutting, and next-question links | Partially | In an evidence view, the temporary harness isolated 22 direct links and 12 secondary links. In the default landscape, direct and secondary filters returned zero links; the cross-cutting filter also returned zero links. | 4 | The filter depends on the selected graph view and the cross-cutting role lookup appears reversed. |
| Identify one possible next question | Yes | Example: “Which heat action plan components are associated with reduced heat-related morbidity and mortality?” | 2 | Clearly labeled as generated questions, not findings. |
| Say what you would do next | Yes | Choose a theme or question, then request a focused search or annotated bibliography. | 1 | The Mermaid companion and Markdown companion both provide this guidance. |

## Honesty and readability checks

| Check | Pass? | Artifact location | Issue |
|---|---|---|---|
| The user prompt appears as framing, not as a canonical question | Yes | `visualizations/question-map.md`; `visualizations/question-map-mermaid.md` | The broad prompt is retained as context rather than promoted to a source-supported question. |
| No source card is duplicated | Yes | `visualizations/question-map-mermaid.md` | All 18 source IDs occur exactly once as source-card definitions. |
| Direct support is visually distinct from secondary relevance | Yes | `visualizations/question-map-mermaid.md`; `visualizations/question-map-force.html` | Solid versus dashed/lighter treatment is present. |
| Secondary links are lighter or dashed rather than visually equal to direct support | Yes | `visualizations/question-map-mermaid.md`; `visualizations/question-map-force.html` | The Mermaid CLI rendering showed lighter dashed secondary links. |
| Cross-cutting theme links are visually distinct from primary membership | Partial | `visualizations/question-map-force.html` | Mermaid is visually distinct, but the HTML role lookup keys `theme_id|question_id` while the JSON member edges use `question_id|theme_id`, so the cross-cutting filter loses its role. |
| Stated and inferred questions are distinguishable | Partial | `visualizations/question-map-mermaid.md` | Three Mermaid cards use only “Reviewed”; the Markdown companion correctly reports explicit/inferred status. |
| Possible next questions are not presented as findings | Yes | `visualizations/question-map.md`; `visualizations/question-map-mermaid.md` | They are framed as future questions. |
| Source links are usable | Yes | `question_map.json`; all visualization artifacts | All 18 UC Library Search links returned HTTP 200 during this review. |
| Access-level or evidence limitations are visible or reachable | Yes | `visualizations/question-map.md`; `visualizations/question-map-force.html` | The Markdown companion states abstract-only/metadata-only limits; the HTML details panel reports access level. |
| Labels are readable | Partial | `visualizations/question-map-force.html`; `visualizations/question-map-mermaid.md` | Mermaid labels are readable but the graph is dense. HTML labels are truncated and the temporary harness showed unstable fit/clipping. |
| Linear Markdown is usable without graphics | Yes | `visualizations/question-map.md` | Structured, linked, citation-rich, and comprehensible without diagrams. |

## Accessibility findings

- The HTML controls use native selects and a native button, but the search input has only a placeholder and no programmatic label.
- HTML graph nodes are mouse/hover interactions only. They have no keyboard focus state, accessible role/name, or Enter/Space activation path.
- Details updates are not announced because the details region has no `aria-live` or equivalent status semantics.
- The tooltip is mouse-position based and not available to keyboard or screen-reader users.
- The SVG has no role or programmatic description summarizing the graph or available interactions.
- Color and dash patterns are not the only cues in Mermaid, which is helpful, but the accessible fallback is the separate Markdown file rather than the Mermaid markup itself.
- The linear Markdown companion is the strongest accessibility artifact and should remain the authoritative fallback.

## Rendering checks

| Environment | Pass? | Notes |
|---|---|---|
| GitHub Markdown | Not testable | No GitHub rendering environment was available. Mermaid CLI rendered the extracted diagram without a syntax error, but that does not establish GitHub behavior. |
| Desktop Markdown viewer | Not testable | No desktop Markdown viewer was available for automated verification. |
| Standalone HTML | Not testable | `question-map-force.html` depends on `visualization-data.js`, which was not among the permitted review inputs. A temporary harness built from `question_map.json` rendered, but it was not the original standalone artifact and should not be treated as a pass. The harness also exposed filter defects. |

## Fidelity checks

- The JSON graph contains 51 nodes and 88 edges, including 22 `supports` edges.
- The Mermaid view contains 31 primary/solid edges, 12 secondary/related edges, and 5 cross-cutting edges.
- `edge-validation.md` reports 18 source→source-question edges, 22 direct-support edges, and 12 secondary conceptual edges, matching the JSON counts for those semantic groups.
- All 18 Mermaid source-card IDs are unique and correspond to the 18 JSON source nodes.
- All 18 UC Library Search links returned HTTP 200.

## Reviewer verdict

- [x] Conditional pass
- [ ] Pass
- [ ] Fail

**Reason:** The Mermaid and linear Markdown artifacts are mostly honest, usable, and well scoped, and the broad prompt is correctly kept as framing. However, the interactive HTML view has accessibility gaps, view-dependent relationship-filter failures, and a cross-cutting role-key defect. Standalone HTML and GitHub/desktop Markdown rendering could not be verified in this environment.

**Visualization fixes:**

1. Make the HTML standalone by embedding the data or shipping and testing `visualization-data.js` with the artifact. Ensure `graph.question_support` exists or derive it from direct-support edges.
2. Fix the HTML cross-cutting role lookup to read the JSON edge direction (`question_id|theme_id`), and add a regression test for the cross-cutting filter.
3. Make the relationship filter independent of graph view, or automatically switch to the required view and tell the user which view is active. Verify direct, secondary, cross-cutting, and next filters each return visible links.
4. Add keyboard access to graph nodes: focusability, accessible names and roles, visible focus, and Enter/Space handlers. Update details on focus/click and mark the details region as a polite live region.
5. Add `aria-label` to the search field, a programmatic name/summary to the SVG, and a keyboard-accessible replacement for the tooltip.
6. Use “Stated” and “Inferred” consistently in Mermaid cards. If method matters, show it separately, such as “Stated · Reviewed.”
7. Reduce HTML label truncation and clipping; allow longer labels to wrap and run a fit-to-view pass after the force simulation settles.
8. Repeat rendering and interaction tests in GitHub, a desktop viewer, the original standalone HTML file, and at least one assistive-technology or keyboard-only session. Record any unavailable environment as not testable.
