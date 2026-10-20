# Visualization Review

**Run ID:** 2026-10-09-heat-city-policy-novice  
**Case ID:** Case 1 — heat-city-policy-novice  
**Reviewer:** Visualization and Accessibility Reviewer  
**Persona:** Novice city stakeholder orientation + accessibility review  
**Review date:** 2026-10-09  

## Artifact reviewed

- [x] Default Mermaid view
- [ ] Optional wide-card Mermaid view — not supplied in the allowed inputs
- [x] Interactive HTML view
- [x] Linear Markdown companion

## Scope and environment notes

- The standalone HTML rendered in headless Chrome: nodes, links, legend, header controls, and details region were present in the resulting DOM.
- Live keyboard, screen-reader, zoom, search, and relationship-filter interaction could not be tested because browser automation was unavailable without elevated permissions. Those items are recorded as **not testable** rather than as passing.
- Source URLs were spot-checked with non-browser HTTP HEAD requests. Eight returned HTTP 403, which is consistent with publisher or bot protection and is not proof that a link is broken.
- Edge counts in the source JSON match `edge-validation.md`: 20 inferred source questions, 20 direct-support edges, 10 secondary links, 7 primary theme memberships, and 11 cross-cutting memberships.

## Orientation tasks

| Task | Completed? | Answer | Difficulty 1–5 | Notes |
|---|---|---|---|---|
| State the main research question | Yes | What evidence and governance actions should a novice city stakeholder consider for extreme heat and public health? | 1 | Clearly present in the Mermaid title, HTML subtitle, and Markdown inquiry section. |
| Name the main themes | Yes | Health outcomes; vulnerability/equity/access; urban form and cooling; governance/emergency response; lived experience; measurement limitations. | 1 | The six themes are easy to identify. |
| Find a source supporting one question | Yes | For heat and emergency-department use, the 2021 BMJ study by Sun et al. is directly linked. | 2 | Easy in Mermaid and Markdown. In HTML, supporting sources are visible as unlabeled circles and require interaction to identify. |
| Distinguish stated from inferred questions | Yes | All 20 retrieved source questions are marked inferred, not stated. | 1 | Marking is clear, but the run has no stated-question example for comparison. |
| Distinguish direct support from cross-cutting relevance | Yes | Direct support uses solid edges; cross-cutting theme relevance uses dashed, lower-opacity links. | 2 | The distinction is honest and visible in the graph. |
| Use the relationship filter to isolate direct, secondary, cross-cutting, and next-question links | Not testable live | Static code supports all four filter states. | n/a | The code maps `supports`, `variant_of`/`relates_to`, cross-cutting `member_of`, and next-question relations correctly. Live interaction could not be exercised. |
| Identify one possible next question | Yes | “How should cooling-center placement be evaluated against uptake, lived experience, and equity?” | 1 | Clearly labeled as possible/next, not source-backed. |
| Say what I would do next | Yes | Turn a next question into a targeted search and verify the resulting evidence basis. | 1 | The graph provides useful launch points. |

## Honesty and readability checks

| Check | Pass? | Artifact location | Issue |
|---|---|---|---|
| The user prompt appears as framing, not as a canonical question | Yes | Mermaid header; HTML subtitle; Markdown inquiry | No conflict found. |
| No source card is duplicated | Yes | Mermaid graph | Sources may be referenced by more than one question, but no duplicate card content was found. |
| Direct support is visually distinct from secondary relevance | Yes | Mermaid and HTML | Solid versus dashed/lighter links. |
| Secondary links are lighter or dashed rather than visually equal to direct support | Yes | Mermaid and HTML | Secondary links use lighter opacity and dashes. |
| Cross-cutting theme links are visually distinct from primary membership | Yes | Mermaid and HTML | Cross-cutting links are lighter and more sparse. |
| Stated and inferred questions are distinguishable | Yes | Mermaid source cards; Markdown evidence entries | All source questions are inferred; the label is explicit. |
| Possible next questions are not presented as findings | Yes | HTML details; Markdown next-question section | Both say they are not source-backed. |
| Source links are usable | Partial | Mermaid, Markdown, and HTML details | Links are present and clickable in Markdown/Mermaid. In HTML, source links are only in the interaction-triggered details panel. 8/20 non-browser HTTP checks returned 403. |
| Access-level or evidence limitations are visible or reachable | Yes | HTML source details; Markdown limitations and evidence entries | Metadata-only basis is explicit. |
| Labels are readable | Partial | Interactive HTML | Question/theme labels are readable, but source circles have no visible labels and HTML labels are truncated. Markdown is clear. |
| Linear Markdown is usable without graphics | Yes | `question-map.md` | Headings, citations, support relationships, limitations, and next questions remain usable as text. |

## Rendering checks

| Environment | Pass? | Notes |
|---|---|---|
| GitHub Markdown | Not testable | GitHub rendering/sanitizer behavior was not available in this environment. |
| Desktop Markdown viewer | Not testable | No desktop Markdown renderer was exercised. |
| Standalone HTML | Pass | Headless Chrome rendered the graph, legend, controls, and details region. |

## Reviewer verdict

- [ ] Pass
- [x] Conditional pass
- [ ] Fail

**Reason:** The graph is semantically honest and the Markdown fallback is strong. Orientation and source identification are easy in Mermaid and Markdown. The conditional verdict is driven by interactive-view accessibility: nodes are not keyboard-reachable, source links depend on mouse interaction, source nodes lack visible labels, and live filtering/screen-reader behavior was not testable.

**Visualization fixes:**

1. Make each interactive node keyboard-reachable with `tabindex="0"`, an accessible name, and Enter/Space activation. Use `role="button"` only if the node genuinely behaves like a button.
2. Make the details panel an `aria-live="polite"` region and reveal source links when a source node receives focus, not only after mouse click.
3. Add visible source labels or a synchronized source list beside the evidence/full views so a supporting source can be identified without hovering.
4. Add a relationship legend showing solid direct support, dashed secondary relevance, sparse cross-cutting links, and next-question links; do not rely on color alone.
5. Resolve the direct-support filter/view mismatch: selecting “Direct support” from the landscape view produces no source links. Either switch automatically to the evidence view or display aggregate direct-support links in landscape.
6. Add `aria-label` to the search field and a visible text-version link to the linear Markdown companion.
7. Respect `prefers-reduced-motion` by pausing or shortening the force simulation and transitions.
8. Increase the HTML layout’s responsiveness and minimum label size; avoid truncating labels that are essential for orientation.
9. Retest with keyboard-only operation, VoiceOver or another screen reader, the four relationship filters, and both landscape/evidence views.
