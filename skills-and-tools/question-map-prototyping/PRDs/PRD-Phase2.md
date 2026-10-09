# Question Map — Visualization Product Requirements Document

**Version:** 0.2 draft  
**Date:** 2026-10-06  
**Phase:** Visualization  
**Canonical data:** `question_map.json`  
**Pilot:** `runs/urban-extreme-heat-health/visualizations/`
**Pilot examples in this skill:** `examples/urban-extreme-heat-health/visualizations/`

## 1. Summary

Phase 2 turns the quote-anchored `question_map.json` graph into three complementary views:

1. A static **Mermaid question map** for READMEs, documents, review, and quick orientation.
2. An interactive **HTML/JavaScript map** for exploration, evidence checking, filtering, and identifying productive follow-up questions.
3. A linear **human-readable Markdown companion** for review without graphics and as an accessible text alternative.

The canonical research object remains `question_map.json`. Visualizations are derived views, not sources of truth. They must not introduce claims that cannot be traced back to nodes, edges, themes, or source metadata.

## 2. Product goals

1. Show the question landscape, not a generic literature summary.
2. Make theme, question, source-question, source, and possible-next-question roles visually distinct.
3. Preserve the difference between:
   - direct source-question support,
   - theme/source support,
   - inferred support,
   - metadata-only support,
   - generated possible next questions.
4. Allow a user to move from an overview question to the source and quote that grounds it.
5. Make the difference between evidence-backed, inferred, and generated questions visible.
6. Provide a stable Mermaid view and a more expressive interactive view without requiring a JavaScript build system.
7. Prepare the graph for future re-launch, where a user can turn a theme or question into a new inquiry root.

## 3. Non-goals for Phase 2

- Do not classify questions as settled, contested, or emerging.
- Do not use citation counts as measures of quality, truth, or consensus.
- Do not hide evidence limitations through color or clustering.
- Do not require users to run `npm install`, a bundler, or a local development server.
- Do not make PDFs or unavailable full text appear to have been read.
- Do not replace the `question_map.json` schema.
- Do not visualize every possible metadata relation in the first implementation if it makes the map unreadable.

## 4. Existing data strengths and gaps

The urban-extreme-heat pilot has 60 nodes, 89 edges, 22 quotes, 23 sources, 23 source questions, 8 canonical questions, 6 themes, and 6 possible next questions. Most evidence is abstract-and-metadata. Citation counts exist in the OpenAlex enrichment files but are not consistently copied into `question_map.json`.

The pilot exposed a useful modeling distinction:

- A canonical question may have **direct source-question support**.
- Its parent theme may have **source support** even when no source question is yet linked directly to the canonical question.

Counting provenance is a known modeling gap; see the Phase 3 data-model refinement section below. Visualizations must show direct question support and theme source support separately, and must not present theme support as direct question support.

The pilot also confirmed that `source_question.question_text` is useful as a temporary source orientation phrase, but it is not a durable substitute for a plain-language key finding with quoted support. The current Mermaid experiments use that proxy because it gives researchers useful orientation without adding unsupported claims.

## 5. Proposed artifacts

For every visualization-enabled run, the skill should create:

```text
visualizations/
  question-map-mermaid.md
  question-map.md
  question-map-force.html
  visualization-data.json
  visualization-data.js
  build_visualizations.py
```

The pilot currently names the generator `build_prototypes.py`; the production skill should standardize on `build_visualizations.py`.

The pilot examples in `examples/urban-extreme-heat-health/visualizations/` should serve as working references during implementation. The skill can add small templates or skeletons as it is productionized, but it should not wait on a separate template-building phase before the graph schema and output contracts stabilize.

### `question-map-mermaid.md`

The static Mermaid view should be the overview layer. The confirmed v4/v5 pattern is:

- `# Question Map — [User's Research Question]`;
- a short plain-language introduction;
- a concise result-count sentence;
- themes as circles, left-aligned vertically on the left side;
- canonical questions as rectangles with left-aligned text in the center column;
- `<hr>` after the main question when source orientation is shown;
- UC Library Search permalinks in the concise `Author et al. (YYYY)` form;
- the possible next questions in a footer, rather than a third Mermaid column;
- `## Where would you like to go next?` followed by the questions and prompts for launching follow-up inquiry.

The v5 baseline omits source and source-question nodes. It should be valid Mermaid and remain useful when pasted into GitHub, Notion, Google Docs, or an issue.

Two variants preserve that three-layer reading flow. Production uses the explicit-source layer by default; the wider inline-source layer is optional.

- **5a — explicit source layer (default):** one source card per selected source, displayed in a right-hand column and formatted as `Author et al. (YYYY) — [core question]`. The card links to UC Library Search. Edges trace `source_id → source_question_id → question_id` when determining which source supports which canonical question. In the rendered left-to-right layout, the dashed edge is drawn from question to source so that the source remains the third visual column.
- **5b — inline source layer (optional):** sources remain inside question cards, while the card uses inline HTML such as `<div style='width:520px;text-align:left'>` to create a wider, more readable rectangle. This variant is better for compact review; 5a is better for auditing each source’s orientation.

Counts such as `[theme-linked sources]` and `[source-specific questions]` are removed from the current Mermaid cards because their provenance is not yet sufficiently well defined. They can return only after the graph has an explicit, validated counting rule.

### `question-map.md`

The linear Markdown view should be the top-to-bottom reading companion. It should include:

- the core inquiry, purpose, breadth, and confirmation status;
- coverage summary and reading notes;
- each theme with its statement, support tier, confidence, coherence basis, key terms, and theme sources;
- each canonical question with its type, origin, confidence, and direct source-question support;
  - each source question with its source citation, evidence basis, and quote or metadata rationale;
  - possible next questions with generation basis and related canonical questions;
- explicit “not found in retrieved coverage” statements;
- limitations.

This file should be readable without rendering Mermaid or opening the interactive map. It should preserve enough structure to serve as an accessible alternative to the graphic.

### `question-map-force.html`

The interactive view should be a self-contained HTML file plus a separate derived-data JavaScript file. The HTML should use a CDN-hosted D3 v7 file and a local `visualization-data.js` file generated by the skill. This avoids `fetch()` and CORS issues when the user opens the file directly from disk.

The pilot demonstrates the intended controls:

- **Question landscape** — themes, canonical questions, and possible next questions.
- **Questions + source anchors** — adds sources for context.
- **Full graph** — adds source questions and evidence edges.
- Text search across labels, statements, subjects, and quotes.
- Hover and click details.
- Zoom, pan, drag, and fit-to-view.
- Reset view.

### `visualization-data.json` and `visualization-data.js`

These derived files should make rendering deterministic and inspectable. They should include:

- all nodes and edges from `question_map.json`;
- themes promoted into the renderable node list;
- quotes;
- citation metadata, including provider and retrieval time;
- direct support counts per canonical question;
- theme source counts;
- generation and run metadata.

The JSON is for auditing and validation. The JavaScript file is for direct browser use.

## 6. Visual grammar

### Nodes

| Node type | Shape | Suggested visual treatment |
|---|---|---|
| Theme | Circle | Larger size by supported source count; color indicates theme; label and source count visible. |
| Canonical question | Rounded rectangle | Color follows parent theme; size follows direct support plus parent-theme support; inquiry root receives a stronger border or marker. |
| Possible next question | Dashed rounded rectangle | Orange or otherwise distinct; explicitly labeled/generated; no source-backed visual weight. |
| Source | Rectangle | Smaller; size may reflect citation count when available; text is usually hidden until focus or hover. |
| Source question | Small rounded rectangle | Color follows theme; opacity reflects confidence; metadata-only records receive a dashed border or reduced emphasis. |

### Edges

| Relation | Suggested treatment |
|---|---|
| Theme membership | Light dashed edge. |
| Source asks source question | Solid neutral edge. |
| Source question supports question | Stronger neutral edge. |
| Question relates to question | Medium edge; may be hidden in overview if visually noisy. |
| Question proposes next question | Dashed accent edge. |
| Citation/source similarity | Hidden by default; visible only in focused evidence mode. |

### Transparency

Every node detail panel should show:

- full question text or theme statement;
- source citation information when relevant;
- direct support count and parent-theme source count;
- confidence;
- evidence basis, such as `abstract_and_metadata`, `metadata_only`, or full-text basis;
- origin, such as explicit, inferred, user-defined, or generated;
- exact quote when available;
- extraction rationale when a quote is not available;
- citation count and provider when available.

Metadata-only source questions should never be visually indistinguishable from quote-anchored source questions.

## 7. Layout strategy

The first interactive version should use a force-directed graph with deterministic behavior:

- themes act as light group centers;
- canonical questions are pulled toward their theme;
  - possible next questions are pulled toward their parent questions;
- source-question and source nodes are only pulled in when evidence/full modes are enabled;
- collision radius prevents node overlap;
- after initial settling, the view fits all visible nodes to the stage.

A future alternate layout may use compound theme containers or radial grouping. Force-directed layout is the best first choice because the graph is small, questions may have multiple parents, and custom detail rendering is important.

If the graph grows beyond roughly 150 visible nodes, the skill should favor:

1. a filtered question landscape by default;
2. progressive disclosure of sources;
3. compound grouping or clustering;
4. an explicit focused subgraph.

## 8. Interaction model

The default interaction should prioritize comprehension:

1. Open in **Question landscape** view.
2. Show themes and canonical questions.
3. Show possible next questions but visually distinguish them from evidence-backed nodes.
4. Hide source and source-question nodes by default.
5. Let the user search, click, filter, and switch to evidence/full modes.

Node details should open in a stable right-hand panel, not a floating tooltip only. Tooltips may be used for quick labels.

Useful filters, in priority order, are:

- search text;
- view mode;
- hide/show possible next questions;
- hide/show sources;
- hide/show source questions;
- focus on one theme;
- focus on one question and its neighbors.

## 9. Technology recommendation

For the first production implementation, use **D3 v7** because it is small, CDN-loadable, flexible, and does not require a build system. The current pilot validates this approach.

Other options should be considered only when a concrete need emerges:

| Library | Strengths | Use if |
|---|---|---|
| D3 | Custom visual grammar, force graph, fine control, no build step | Default choice. |
| Cytoscape.js | Compound nodes, graph layouts, mature graph interactions | Themes need durable containers or graph editing becomes important. |
| React Flow | Polished node/edge UI and React ecosystem | A broader web app or persistent workspace is built. |
| Mermaid | Static, portable, easy review | Always useful as the overview artifact. |
| Observable Plot / D3 scales | Small multiples and matrices | The graph becomes too dense and a matrix or dashboard view is needed. |

Avoid adding a framework unless the visualization becomes part of a larger application.

## 10. Accessibility requirements

The interactive and static maps must remain usable without relying on color alone.

Required:

  - shape differences between themes, questions, sources, and possible next questions;
- text labels or accessible alternatives;
- visible focus treatment for keyboard users;
- evidence status and confidence in text;
- color contrast at least WCAG AA for text;
- alt text or a text summary when a static image is exported;
- a data table or Markdown summary for users who cannot use the graphic.

The details panel should be reachable by keyboard and announced as the details region.

## 11. Validation

Visualization generation should fail closed when the input graph is invalid. Validation should check:

1. `question_map.json` passes the existing Phase 1 validator.
2. Every edge endpoint resolves to a node or theme.
3. Every theme ID in `question_ids`, `source_ids`, and `next_question_ids` exists.
4. Direct support counts derive only from `source_question -> question` support edges.
5. Theme source counts derive only from the theme's `source_ids`.
6. Possible next questions are never counted as source support.
7. Citation metadata records provider and retrieval time when present.
8. Missing citation metadata is displayed as “not retrieved,” not as zero support.
9. All generated artifacts are syntactically valid.
10. The interactive HTML loads from disk without requiring a server.

## 12. Acceptance criteria for the first production implementation

Given a valid `question_map.json`:

1. Running the visualization builder creates a Mermaid Markdown file, a linear Markdown file, an HTML map, and derived data files.
2. The default view opens on the question landscape.
3. Themes, questions, possible next questions, sources, and source questions are visually distinct.
4. The user can search and click through to source quotes and metadata.
5. The map clearly distinguishes direct question support from theme support.
6. Possible next questions are visibly generated rather than source-backed.
7. The interactive view opens directly from disk without a local web server.
8. The Mermaid file renders with at least GitHub’s Mermaid implementation.
9. No artifact presents citation counts as evidence of correctness.
10. The visualization remains usable for a 20–150 node graph.

## 13. Open implementation questions

1. Should the canonical `question_map.json` include a compact `visualization` object, or should all rendering metadata remain in the derived artifact?
2. How should citation metadata be represented in `question_map.json`? Working recommendation: include the normalized fields needed for display and traceability—concise citation, DOI/PMID/URL, UC Library Search permalink, access level, provider, and retrieval timestamp—while keeping raw provider payloads in enrichment files.
3. Should canonical questions inherit any display weight from parent-theme sources, or should only direct source-question support affect node size?
4. Is a theme-guided force layout sufficient for production, or should compound theme containers be introduced earlier?
5. What should the export set be: PNG, SVG, PDF, standalone HTML, or Mermaid only?
6. How much metadata filtering belongs in Phase 2 versus Phase 3?
7. Should the user-facing Mermaid map hide source and question counts until we have a single, well-defined rule for computing “theme-linked sources” and “direct question support”?
8. Should each source in a question card have a concise orientation phrase, such as its core question, method, or key finding?
   The pilot currently uses the source question text as a temporary orientation proxy. A durable implementation should use a dedicated source orientation field with plain-language finding, method, or core-question labels plus quoted support.
9. Should we gather a dedicated plain-language key finding and a quoted support passage for each selected source during Phase 1 enrichment, rather than deriving it at visualization time?

## 14. Roadmap

### Current status

- The Phase 1 data graph is stable enough to drive all three views.
- The pilot has working linear Markdown, Mermaid, and D3 HTML outputs generated from `question_map.json`.
- The skill now includes `build_visualizations.py` and `normalize_citations.py` as the Phase 2a toolkit.
- The v5 baseline confirms a readable two-column Mermaid pattern with source orientation inside question cards and possible next questions in the footer.
- The 5a and 5b experiments are rendering successfully and provide the first evidence for an explicit source layer and a wider inline-source card layer.
- 5a is the Phase 2a default; 5b remains an optional wider-card variant.
- The current source orientation is still a temporary proxy derived from `source_question.question_text`; production needs a dedicated orientation field with quoted support.
- The 2026-10-09 test run confirmed the need for explicit edge semantics: evidence-backed direct support, medium/low-confidence secondary links, and explicit primary/cross-cutting theme membership. A source question may support more than one canonical question when the evidence warrants it; the current toolkit validates these distinctions before rendering.

### Phase 2a — Core visualization toolkit

- Move from the pilot-named `build_prototypes.py` to `build_visualizations.py`.
- Extract the v4/v5 Mermaid, linear Markdown, and D3 HTML logic into the skill’s scripts.
- Add normalized citation metadata to `question_map.json` so visualizations do not depend on raw enrichment payloads.
- Add fail-closed validation of every derived view.
- Validate relationship semantics, not only referential integrity: stated versus inferred source questions, direct versus secondary support, and primary versus cross-cutting theme membership.
- Preserve source orientation, access level, confidence, and permalink generation from the graph rather than hard-coding run-specific assumptions.
- Test the generated Mermaid in GitHub and at least one desktop Markdown renderer.

### Phase 2b — Evidence and focus

- Add a focus mode for one theme or question and its nearby evidence.
- Add evidence-audit, confidence, access-level, and evidence-basis filters.
- Reconcile direct question support and theme source support with explicit, validated counting rules.
- Add a dedicated, provenance-aware source orientation field: a concise plain-language finding or core question, plus a quotation.
- Improve the interactive map for larger graphs with progressive disclosure and deterministic saved positions.

### Phase 2c — Portability and publication

- Static image and vector exports.
- Embeddable HTML.
- Printable report view.
- Accessible data tables.
- Additional layout modes once graph density requires them, such as theme containers, adjacency matrices, or small multiples by question.

### Phase 3 — Data-model refinement

Before or alongside the launch work below, the graph schema likely needs a more expressive edge model. This should not be solved inside Phase 2.

The pilot in `examples/urban-extreme-heat-health/data/question_map.json` exposes the core problem: the `Unequal exposure and vulnerability` theme has no direct question support in the current view because the associated canonical question has no `source_question -> question` edge, even though several of its listed sources are directly related to unequal exposure and health-disparity research. As a result, a Mermaid card can say “No sources linked yet” while the theme itself contains relevant sources.

Phase 3 should consider:

- explicit `source -> theme` edges with confidence and rationale;
- explicit `theme -> question` membership edges instead of relying only on arrays embedded in theme objects;
- allowing a source question or source to support more than one canonical question or theme;
- separate relationship types such as `asks`, `supports`, `extends`, `challenges`, `contextualizes`, and `informs_method`;
- evidence access, confidence, and provenance on every new edge;
- a validated distinction between direct evidence support, thematic affinity, and user-directed grouping.

The objective is to make cross-connections visible without weakening the distinction between quote-anchored support and interpretive organization.

### Phase 3 — Launch

- Turn any theme, canonical question, or possible next question into a new inquiry root.
- Generate follow-up searches through `uc-library-search`.
- Create targeted reading lists through `annotated-bibliography`.
