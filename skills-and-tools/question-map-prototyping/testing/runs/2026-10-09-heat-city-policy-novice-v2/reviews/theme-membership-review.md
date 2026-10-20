# Theme Membership Review

**Run ID:** 2026-10-09-heat-city-policy-novice-v2  
**Case ID:** heat-city-policy-novice  
**Reviewer:** Domain Expert / theme-and-question reviewer  
**Review date:** 2026-10-09  

## Question-level theme review

The reviewed graph has 14 explicit question-to-theme membership edges: nine primary and five cross-cutting. I reviewed all of them.

| Question ID | Theme | Generated role | Reviewer role | Agreement? | Rationale |
|---|---|---|---|---|---|
| q_001 | theme_001 | primary | primary | Yes | Heat action plan content is squarely within a plans-and-governance theme, but q_001 is broader than several of its supporting source questions; see the canonicalization concerns below. Confidence: high for theme membership, medium for the coherence of the canonical frame. |
| q_002 | theme_001 | primary | primary | Yes | The titles and abstract questions for src_003–src_005 directly address why and how cities plan for heat and the role of urban planning. Confidence: high. |
| q_007 | theme_001 | primary | primary | Yes | “Urban Greenspace, Climate Adaptation and Health Co-Benefits: Municipal Policy and Practice in London” and the quote “This paper looks at the municipal evidence base in London” support a governance/policy-integration membership. Confidence: medium because this primary membership rests on one source. |
| q_004 | theme_002 | primary | primary | Yes | src_011 and src_014 address greening/imperviousness and evaluations of multiple cooling interventions. The shared action–effect framing is appropriate, while the graph correctly avoids treating all interventions as one mechanism. Confidence: high. |
| q_008 | theme_002 | primary | primary | Yes | “Examining the Optimal Placement of Cooling Centers…” and the literature review title support cooling-center access as an intervention question. Confidence: high. |
| q_009 | theme_002 | primary | primary | Yes | The src_018 abstract explicitly compares street trees, cool roofs, green roofs, rooftop PV, and reflective pavements using heat-stress, energy, and ventilation metrics. Confidence: high. |
| q_003 | theme_003 | primary | primary | Yes | src_016 and src_017, and especially the heat-wave mortality and sociodemographic-exposure objectives, directly support heat/health-outcome evidence. The src_008 support edge should be qualified; see canonicalization concerns. Confidence: high for the primary theme, medium for the q_003 support from src_008. |
| q_005 | theme_004 | primary | primary | Yes | src_008 and src_009 directly concern evaluating a heat action plan against mortality and reviewing heat-plan evaluation methods. Confidence: high. |
| q_006 | theme_005 | primary | primary | Yes | The scoping-review objective for src_017 directly concerns urban heat exposure and sociodemographic factors. This is narrower than the user prompt and is not imposed by the reviewer-only equity lens. Confidence: high. |
| q_006 | theme_001 | cross_cutting | cross_cutting | Yes | Risk distribution can inform plan targeting, outreach, and engagement, but the sociodemographic-distribution evidence is not itself plan-content evidence. Confidence: high. |
| q_004 | theme_004 | cross_cutting | cross_cutting | Yes | Evaluation quality is relevant to intervention evidence, but q_004 is not primarily a heat-plan evaluation-methods question. The graph avoids over-attaching q_005 to every intervention theme. Confidence: high. |
| q_008 | theme_005 | cross_cutting | cross_cutting | Yes | src_013 states that it examined “how well they [cooling centers] serve areas with high social vulnerability.” That supports an equity linkage without collapsing cooling-center access into risk-distribution evidence. Confidence: high. |
| q_009 | theme_003 | cross_cutting | cross_cutting | Yes | The infrastructure comparison includes heat and health-related metrics, but it is a modeling comparison rather than primary health-outcome evidence. Confidence: high. |
| q_007 | theme_003 | cross_cutting | cross_cutting | Yes | Health co-benefits and indicators connect greenspace policy to health outcomes, but the study’s primary focus is municipal integration, not heat-health epidemiology. Confidence: medium. |

## Possible-next-question audit

| Node ID | Reviewer status | Rationale |
|---|---|---|
| nq_001 | Properly proposed | It addresses a stated evidence gap: component-level plan evidence associated with morbidity/mortality was not found. The `proposed_for` relation is appropriate. |
| nq_002 | Properly proposed | It localizes generic intervention evidence to “the user’s city”; no city-specific evidence was retrieved. |
| nq_003 | Properly proposed | It narrows q_006 and q_008 to local burden and access; it is not presented as an observed finding. |
| nq_004 | Properly proposed | It converts general governance evidence into a local coordination question. |
| nq_005 | Properly proposed | It extends the multi-outcome and measurement findings into a local indicator question. |

The possible questions are labeled as `next_question` nodes and connected to themes with `proposed_for`, not `supports`. This preserves the distinction between hypotheses for further search and evidence found in the reviewed titles/abstracts.

## Conceptual-distinction check

| Issue | Present? | Node or edge IDs | Rationale |
|---|---|---|---|
| The user prompt is treated as a canonical question without direct source analysis | No | ctx_001 | The raw prompt is a context node with `root_status: primary_user_root`. Its rationale explicitly says “Framing only.” No question node carries that status, and no direct source analysis supports the full policy prescription. Confidence: high. |
| A theme implies containment where the evidence supports only cross-cutting relevance | No | edge_member_001–edge_member_009; edge_cross_001–edge_cross_005 | The five themes have defensible primary members. Equity, methodology, and health outcomes are attached as cross-cutting rather than absorbing related questions. Confidence: high. |
| A methodological question is attached to every relevant theme by default | No | q_005; edge_member_008; edge_cross_002 | q_005 remains a narrow heat-plan evaluation-methods question. Its only primary membership is theme_004. q_004 is the sole cross-cutting method link, which is appropriate. Confidence: high. |
| A narrower question is collapsed into a broader question | Yes | q_001; edge_support_006, edge_support_007, edge_support_010, edge_support_011, edge_support_019 | q_001 is reasonable for plan content/gaps, but several source questions concern preparedness, rapid plan development, strengthening, or overall progress rather than components included or omitted. Confidence: high. |
| A possible next question appears to be source-backed evidence | No | nq_001–nq_005; edge_nq_theme_001–edge_nq_theme_005 | The next questions are future inquiry nodes, not findings. They are connected by `proposed_for`, and their rationales describe gaps, narrowing, or monitoring. Confidence: high. |

## Additional canonicalization and evidence-status concerns

1. **q_001 is too broad as a single canonical frame.** It has strong direct support from src_002, whose objective was “To examine commonalities and gaps in the content of local US heat action plans.” However, src_006 is about public-health preparedness, src_007 is about rapidly developing a community- and evidence-based plan, src_010 is a strengthening commentary, and src_015 is a metadata-only systematic review. These are related to heat action plans but do not all directly answer what components plans include or omit.
2. **src_008’s support for q_003 is overstated.** The quote says the study “evaluates the HAP’s impact on all-cause mortality … relative to a … baseline.” That directly supports q_005, but it is intervention-evaluation evidence, not direct support for the broader exposure–mortality association represented by q_003. It may inform q_003, but it should not be presented as equivalent to src_016’s direct heat-wave mortality objective.
3. **Abstract-only evidence limits the strength of several canonical claims.** The run has no full-text evidence and one metadata-only source. Theme membership judgments are therefore stronger than question-level outcome judgments, which should remain conservative.

## Summary

- **Theme memberships reviewed:** 14.
- **Agreements:** 14.
- **Overstated containment links:** 0.
- **Missing cross-cutting links:** 0.
- **Canonicalization concerns:** 2 — q_001 is over-collapsing related but distinguishable plan-content, preparedness/development, strengthening, and progress questions; src_008 is over-attached to q_003 as direct support.
- **Next-question presentation:** Correctly proposed, with no next question presented as a finding.

## Reviewer verdict

- [ ] Pass
- [x] Conditional pass
- [ ] Fail

**Reason:** The user prompt remains framing, theme containment is generally disciplined, cross-cutting roles are well used, methodology is not over-generalized, and next questions are clearly prospective. A conditional pass is warranted because two canonical-support distinctions should be tightened before treating the question layer as fully reliable.

**Theme or question fixes:**

1. Split q_001 into at least two narrower canonical questions, or preserve q_001 as “Heat action plan content and gaps” and downgrade the related-but-distinct source edges:
   - Keep src_001 and src_002 as direct plan-content/gap support.
   - Recharacterize src_006, src_007, src_010, and src_015 as `informs`, `relates_to`, or support for a separate question such as “How are heat action plans developed, prepared for, and strengthened?”
   - Preserve the theme_001 primary membership for the resulting narrower plan-content question and add cross-cutting links where needed.
2. Change the sq_008→q_003 relation from `supports` to `informs` or `relates_to`, or make it a lower-confidence contextual edge. Retain sq_008→q_005 as direct support and keep any connection to q_003 as intervention-evaluation evidence rather than heat-wave association evidence.
3. Do not strengthen q_004, q_007, or q_009 outcome claims without full-text review; the current abstract-based theme memberships are acceptable, but outcome interpretations should remain conservative.
