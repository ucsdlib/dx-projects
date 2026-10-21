# Run Summary

**Run ID:** `2026-10-09-heat-city-policy-novice-v2`  
**Case ID:** `heat-city-policy-novice`  
**Date:** 2026-10-09  
**Coordinator:** Fresh graph-generation/coordinator session  
**Adjudicator:** Fresh adjudicator session, not the generator or graph defender  

## Phase status

| Phase | Status | Reviewer(s) | Key issue |
|---|---|---|---|
| Intake realism | Pass | Coordinator / intake audit | Raw prompt preserved; simulated context used only after clarification; reviewer-only lenses were not injected into confirmed scope. |
| Skill composition | Pass | Coordinator / technical validator | UC Library Search and verification workflow were used; no PDF extraction; access levels were explicit. |
| Independent reference pool | Complete | Search Auditor | Pool of 20 sources was completed blind to the generated map. |
| Graph generation | Complete | Coordinator | 51 nodes and 88 edges were generated; the broad prompt remained a context frame. |
| Validation and build | Pass | Validator / build tools | Validation passed after a permalink correction; visualization build succeeded. |
| Source selection review | Conditional pass | Domain Expert / Search Auditor | No irrelevant source, but governance literature was overrepresented; recent health-use, equity, lived-experience, warning-system, and intervention-comparison coverage was weak. |
| Edge adjudication | Conditional pass | Evidence Auditor | Blind adjudication found defensible candidates but abstract-only limits, two weak title-only objectives, and two conservative mappings. |
| Generated-edge comparison | Conditional pass | Evidence Auditor | 22 direct edges and 12 secondary edges were compared; four direct supports were overclaimed; no edge was wholly unsupported. |
| Theme membership review | Conditional pass | Domain Expert / theme reviewer | All 14 explicit theme-role assignments agreed, but `q_001` over-collapsed related plan questions and `sq_008 → q_003` overstated directness. |
| Visualization review | Conditional pass | Visualization & Accessibility Reviewer; Novice Reader; Practitioner Reviewer | Mermaid and Markdown were useful, but HTML filtering, keyboard accessibility, labels, and council-preparation guidance needed work. |

## Scores

| Measure | Result | Provisional gate | Pass? |
|---|---:|---|---|
| Intake realism | 4/4 checks | Raw prompt preserved; reviewer lenses not added to scope | Pass |
| Source precision | 17/18 = 94.4% | No wholly irrelevant source; `src_015` is metadata-only and cannot support detailed plan claims | Conditional |
| Reference recall | 3/15 core pool items = 20.0%; 3/20 total pool items overlapped | Low core-pool overlap | Fail |
| Confirmed-scope coverage | 5/5 major scope components covered or explicitly marked weak/not found | City actions, heat, public health, recency, and council-use purpose were represented with transparent gaps | Pass |
| Reviewer-lens coverage | Governance strong; urban cooling good; measurement limits good; health/equity partial; lived experience weak | Non-gating gap report | Pass |
| Multi-question fidelity | Overall relation precision 30/34 = 88.2% | Most multi-question links were defensible, but four direct links overclaimed | Conditional |
| Direct support precision | 18/22 = 81.8% exact or defensible; 4/22 overclaimed | No direct edge was unsupported, but directness must be corrected | Conditional |
| Direct support recall | 23/25 best-mapped blind candidates = 92.0% | Two candidates were conservatively represented or absent; no evidence of material loss | Pass |
| Stated/inferred agreement | 18/18 source questions agree with evidence status; 13 explicit and 5 inferred | 100% is above the 85% gate | Pass |
| Secondary-link overclaim rate | 0/12 = 0.0%; 12/12 exact or defensible at relation level | Secondary links were not overclaimed as direct evidence | Pass |
| Theme-membership agreement | 14/14 = 100% | No theme implies containment where cross-cutting relevance is appropriate | Pass |
| Unsupported edge count | 0 | 0 | Pass |
| Novice orientation success | 6/8 tasks fully successful; 2/8 partially successful; difficulty 3/5 | Novice identified main question, themes, supporting source, status distinction, and next step without coaching | Pass |

### Confirmed-scope coverage versus reviewer-only lenses

The confirmed scope was “What should my city do about extreme heat and public health? I want recent research evidence to bring to a city council meeting.” The graph addressed city actions, extreme heat, public-health framing, mostly recent evidence, and the council-meeting purpose. It also transparently marked no named city, no component-level outcome evidence, no cost/implementation-effectiveness evidence, and no full-text verification.

Healthcare use, vulnerable-population specificity, lived experience, emergency-response depth, and intervention comparison were reviewer-only coverage lenses. Their gaps are useful for quality improvement but do not by themselves invalidate the confirmed scope. Notably, the graph did not manufacture unsupported healthcare-use or lived-experience links. Governance sources were overrepresented even though the reviewer lens itself is non-gating.

## Reviewer disagreements

| Topic | Reviewers | Positions | Adjudicated decision | Rationale |
|---|---|---|---|---|
| Reference recall denominator | Source Selection Reviewer; protocol scorer | Reviewer reported 3/20 pool overlap; the protocol defines recall against core sources | Use 3/15 core-pool sources = 20%, while also recording the 3/20 total-pool overlap | The independent pool contains 15 sources rated relevance 3; using the protocol denominator avoids overstating the coverage problem while preserving both counts. |
| `sq_008 → q_003` directness | Evidence Auditor; theme reviewer | The edge comparison called the HAP-mortality support exact; the theme reviewer considered it a direct intervention evaluation, not the broader heat-exposure/mortality association | Downgrade to `informs` or `relates_to` and retain `sq_008 → q_005` as direct support | `sq_008` explicitly evaluates a HAP against all-cause mortality, but that is intervention-evaluation evidence, not evidence of the urban heat-exposure/heat-wave mortality association posed by `q_003`. |
| Breadth of `q_001` | Edge reviewer; theme reviewer | The edge reviewer flagged three direct overclaims; the theme reviewer flagged broader collapse of plan-content, preparedness, development, strengthening, and review questions | Treat `q_001` over-collapse as a canonicalization issue. Preserve direct support only where plan-content/gaps are explicit; downgrade or split related preparedness/development/strengthening/review edges | The strongest evidence supports plan-content analysis. Related plan-oriented studies may inform planning, but should not be visually or semantically interchangeable with component-gap findings. |
| Theme role assignment | Visualization reviewer; theme reviewer | The HTML review described lost cross-cutting roles; the theme-review sheet found complete role agreement | No graph role-data failure; treat the issue as HTML lookup/build logic | Direct inspection of `question_map.json` found explicit `role` fields on all 14 membership edges: nine `primary` and five `cross_cutting`. The theme-review table matches these fields. The defect is the HTML key direction/filter behavior, not missing graph data. |
| Practitioner completeness | Novice/practitioner reviewers; scope scorer | Practitioner reviewer wanted implementation, financing, staffing, operations, authority, and feasibility guidance; the confirmed scope asks for research evidence, not a complete policy package | Treat council-preparation support as a high-priority usability/skill gap, not a confirmed-scope coverage failure | The graph is evidence-oriented and honest about limits. It can orient a novice, but it should not be mistaken for a complete council briefing or decision-support package. |

## Triage

| Issue | Artifact/node/edge | Root cause | Proposed fix | Regression fixture needed? |
|---|---|---|---|---|
| P1: `q_001` absorbs distinct plan-content, preparedness, development, strengthening, and review questions | `q_001`; `edge_support_006`, `edge_support_007`, `edge_support_011`, `edge_support_019`; related edges | Canonicalization | Split `q_001` into plan-content/gaps and plan-development/preparedness/strengthening questions, or narrow its wording and downgrade non-content `supports` edges to `informs`/`relates_to` | Yes |
| P1: Metadata-only direct support | `src_015`, `sq_015`, `edge_support_019` | Source-question extraction | Remove `src_015` or obtain full text/abstract before any detailed plan-content claim; keep metadata-only links explicitly indirect and low-confidence | Yes |
| P1: Two title-only source questions receive reduced confidence but feed a direct graph edge | `sq_010`, `sq_015`; `edge_support_011`, `edge_support_019` | Source-question extraction | Require an objective quote or full text for `supports`; otherwise use `relates_to` and preserve low confidence | Yes |
| P2: Intervention-evaluation and cooling-access relationships are overdirected | `edge_support_009` (`sq_008 → q_003`); `edge_support_018` (`sq_014 → q_008`) | Edge semantics | Distinguish intervention-effect evaluation from exposure/outcome association and distinguish cooling-center evaluation from measured placement/access outcomes; adjust relation or target | Yes |
| P2: Four generated direct edges are overclaimed but defensible topically | `edge_support_006`, `edge_support_011`, `edge_support_018`, `edge_support_019` | Edge semantics | Add relation-validation tests that prevent broad topical relevance from becoming `supports` without construct/outcome match | Yes |
| P2: Core reference-pool overlap is low; recent health-use, warning-system, community-intervention, equity, and lived-experience sources are absent | Selected-source list versus `01-reference-pool.md` | Search strategy or coverage | Add query branches for surveillance/healthcare use, disaggregated vulnerable populations, resident experience, warning systems, and community intervention comparisons; prioritize relevance-3 pool sources | Yes |
| P2: Governance/plan literature is overrepresented and partly redundant | `src_001`–`src_010`, `src_015` | Source selection | Enforce source-diversity caps by theme and trim redundant governance sources; add balancing constraints for outcomes, equity, interventions, and evidence limitations | Yes |
| P3: HTML cross-cutting filter loses roles and returns zero links despite valid graph roles | `question_map-force.html`; `edge_cross_001`–`edge_cross_005` | Visualization layout or readability | Correct the `question_id|theme_id` lookup direction, make filters view-independent, and add interaction tests for all four relationship filters | Yes |
| P3: Interactive HTML is not keyboard-accessible and lacks accessible status/name semantics | `question_map-force.html` | Visualization layout or readability | Add focusable nodes with accessible names/roles, visible focus, Enter/Space behavior, polite details updates, labeled search, described SVG, and accessible tooltip replacement | Yes |
| P3: Stated/inferred method is confusing in some Mermaid cards | Mermaid source cards | Visualization layout or readability | Use consistent “Stated” and “Inferred” labels; show review method separately where useful | Yes |
| P3: Graph density, long labels, truncation, and link semantics challenge novice/practitioner readers | Mermaid and HTML views | Visualization layout or readability | Add plain-language link legend, wrap labels, compact practitioner/evidence panels, and maintain the linear Markdown fallback | Yes |
| P3: Standalone HTML and rendering environments were not fully testable | `question_map-force.html` | Visualization layout or readability | Embed data or ship and test the data dependency; repeat GitHub, desktop, standalone HTML, keyboard-only, and assistive-technology tests | Yes |
| P3: Map is not a complete council-preparation tool | Next-question layer; practitioner view | Documentation or skill instruction gap | Add an explicit council-preparation layer with implementation, financing, staffing, operations, authority, feasibility, procurement, and sequencing prompts; mark these as decision-guidance, not findings | Yes |
| P4: Evidence transferability is implicit for non-local contexts | Source/theme metadata and visualization notes | Documentation or skill instruction gap | Add compact jurisdiction/population/time-period transferability labels and a novice-facing entry point | No |
| P4: Abstract-only basis is disclosed but may not be conspicuous enough before citation/export | HTML and Markdown evidence panels | Visualization layout or readability | Surface “abstract-only; not full-text verified” near export/citation controls and in the novice entry point | No |

## Provisional gate results

| Gate | Result | Evidence |
|---|---|---|
| Referential validation passes | Pass | Validator and visualization build passed after the permalink correction. |
| No selected source is irrelevant or unsupported | Fail | No source was wholly irrelevant, but `src_015` was metadata-only and judged unsupported for detailed plan-component claims. |
| Every major confirmed-scope component is covered or transparently marked as a gap | Pass | Actions, heat, health, recency, and council-use purpose were represented; local-city, outcome, cost, and full-text limits were marked. |
| No direct-support edge is judged unsupported | Pass | 0/22 direct edges were wholly unsupported; 4/22 were overclaimed. |
| No secondary relationship is visually indistinguishable from direct support | Pass | Mermaid and HTML provided visual distinction, although HTML filtering behavior needs repair. |
| Source-question origin labels agree with evidence in at least 85% of cases | Pass | 18/18 = 100%; 13 explicit and 5 inferred. |
| No theme implies containment where the relationship is cross-cutting | Pass | 14/14 explicit theme-role assignments agreed with the reviewer; 9 primary and 5 cross-cutting. |
| Novice reviewers can orient and identify a useful next step without help | Pass | Novice identified the main question, themes, a supporting source, status distinction, and a useful next step; two visualization tasks were only partial. |
| User prompt appears as framing, not an unsupported canonical question | Pass | `ctx_001` has `root_status: primary_user_root`; canonical questions have `root_status: none`; the prompt rationale marks it as framing only. |

**Gate score:** 7/9 gates pass. The source-quality gate fails narrowly because of `src_015`; the coverage gate passes. Four overclaimed direct edges and the HTML defects do not independently trip a stated gate but block unconditional acceptance.

## Decision

- [ ] Pass
- [x] Conditional pass
- [ ] Fail

**Reason:** The run is structurally sound, intake-realistic, and unusually disciplined. The broad prompt remains framing; all explicit theme roles are present and agree with review; no edge is wholly unsupported; novice and practitioner reviewers could orient and launch useful follow-ups; and the confirmed-scope components are covered or transparently marked as gaps. A conditional pass is appropriate for the next iteration because the known failures are scoped: improve source diversity and recency, correct canonical and directness overclaims, remove or verify `src_015`, and repair interactive filtering/accessibility. The map is not yet acceptable as a final council-ready evidence package.

**Required before next run:**

1. Split or narrow `q_001`; downgrade `sq_006`, `sq_010`, and `sq_015` plan-content claims; downgrade `sq_008 → q_003` and `sq_014 → q_008`. Keep `sq_008 → q_005` as direct support.
2. Remove `src_015` until full text is reviewed, or replace it with a verified source; never turn metadata-only evidence into direct support.
3. Rebalance source selection by adding recent health-use, vulnerable-population, lived-experience, warning-system, and community-intervention evidence while trimming redundant governance sources.
4. Add regression tests for direct-support semantics, metadata-only edges, theme-role lookup, HTML filters, and stated/inferred labels.
5. Repair HTML keyboard access, accessible names/status semantics, label handling, relationship filters, and standalone-data dependency; test keyboard-only and, where available, assistive-technology paths.
6. Add a novice entry point and a clearly labeled council-preparation layer for implementation, financing, staffing, operations, authority, feasibility, procurement, and sequencing without presenting those prompts as evidence findings.
