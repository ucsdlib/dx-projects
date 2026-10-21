# Generated Edge Comparison

**Run ID:** 2026-10-09-heat-city-policy-novice-v2  
**Case ID:** heat-city-policy-novice  
**Reviewer:** Evidence Auditor  
**Review date:** 2026-10-09  
**Comparison basis:** Blind adjudication in `reviews/edge-adjudication-sheet.md` compared against the 22 generated source-question → canonical-question `supports` edges and 12 `relates_to` links in `question_map.json`. The graph was inspected only for this comparison and was not modified.

## Scoring assumptions

- **Exact:** The generated relation and target question match the blind adjudication’s construct and outcome without material widening.
- **Defensible:** The relation is supported by the source’s objective, quoted evidence, or graph metadata, but the canonical target is broader or slightly shifted.
- **Overclaimed:** The target relation is plausible topically, but the supplied evidence or metadata does not establish the direct construct/outcome match asserted by a `supports` edge.
- **Understated:** The graph uses a weaker relation than the prior blind candidate supported, though the generated link may still be conservative.
- **Unsupported:** No defensible relationship exists. None of the generated direct or secondary links met this threshold.
- **Missing:** A blind direct-support candidate has no corresponding generated direct relation.
- **Precision/recall:** Precision is based on the 22 generated direct edges. Recall is a best-mapped comparison of those edges against the 25 blind direct-support candidate pairs, allowing graph questions to subsume the blind review’s broader `G`, `H`, `U`, `E`, and `M` areas. Secondary links are scored separately at the relation level.

## Generated direct-support comparison

| Edge ID | Source → target | Generated relation | Reviewer verdict | Rationale |
|---|---|---|---|---|
| edge_support_001 | sq_001 → q_001 | supports | Defensible | A critical analysis of California HAPs can directly inform plan components and gaps, but the target is broader than state-specific plan strengths. |
| edge_support_002 | sq_002 → q_001 | supports | Exact | The source’s stated content-analysis objective is nearly identical to the plan-content/gaps question. |
| edge_support_003 | sq_003 → q_002 | supports | Exact | The source explicitly asks why and how cities plan for heat. |
| edge_support_004 | sq_004 → q_002 | supports | Defensible | A planner survey directly informs heat-planning processes, though the target is broader than planner-reported strategies. |
| edge_support_005 | sq_005 → q_002 | supports | Exact | The quoted aim is explicitly urban heat governance focused on planning. |
| edge_support_006 | sq_006 → q_001 | supports | Overclaimed | Public-health preparedness and HAPs are related, but the review does not directly establish HAP component inclusion/omission evidence. |
| edge_support_007 | sq_007 → q_001 | supports | Defensible | The source directly concerns evidence- and community-based HAP development, but it is a process case rather than a broad plan-content analysis. |
| edge_support_008 | sq_008 → q_005 | supports | Defensible | A quasi-experimental HAP mortality evaluation supports evaluation evidence, though it is one example rather than a general methods answer. |
| edge_support_009 | sq_008 → q_003 | supports | Exact | The source directly evaluates HAP impact on all-cause mortality. |
| edge_support_010 | sq_009 → q_005 | supports | Exact | The source explicitly reviews HAP evaluation methods and remaining challenges. |
| edge_support_011 | sq_010 → q_001 | supports | Overclaimed | A title-only policy commentary on strengthening HAPs does not directly establish which plan components are included or omitted. |
| edge_support_012 | sq_011 → q_004 | supports | Exact | The study directly examines urban-form characteristics in the temperature-mortality relationship. |
| edge_support_013 | sq_011 → q_003 | supports | Exact | The study directly addresses the temperature-mortality relationship. |
| edge_support_014 | sq_012 → q_007 | supports | Exact | The source directly examines municipal greenspace, climate adaptation, health, policy, and practice. |
| edge_support_015 | sq_013 → q_008 | supports | Exact | The source directly examines cooling-center placement and access areas. |
| edge_support_016 | sq_013 → q_006 | supports | Exact | The source directly compares service to areas with high social vulnerability. |
| edge_support_017 | sq_014 → q_004 | supports | Exact | The review directly evaluates multiple urban cooling interventions. |
| edge_support_018 | sq_014 → q_008 | supports | Overclaimed | A review of cooling-center evaluations does not directly establish which populations/places cooling centers serve or how well they reach high-risk groups. |
| edge_support_019 | sq_015 → q_001 | supports | Overclaimed | Metadata identify a systematic review of HAPs and warning systems, but do not substantiate direct evidence about plan components or omissions. |
| edge_support_020 | sq_016 → q_003 | supports | Exact | The objective directly examines heat-wave mortality and lag effects. |
| edge_support_021 | sq_017 → q_006 | supports | Exact | The scoping review directly examines urban heat exposure and sociodemographic factors. |
| edge_support_022 | sq_018 → q_009 | supports | Exact | The source directly compares five infrastructure strategies across multiple outcomes. |

## Generated secondary-relation comparison

| Edge ID | Source → target | Generated relation | Reviewer verdict | Rationale |
|---|---|---|---|---|
| edge_variant_001 | sq_001 → q_002 | relates_to | Exact | The blind review treated HAP governance as conceptually related to broader municipal governance. |
| edge_variant_002 | sq_002 → q_005 | relates_to | Exact | Plan gaps can relate to evaluation methods, while remaining non-outcome evidence. |
| edge_variant_003 | sq_003 → q_004 | relates_to | Defensible | The source concerns heat planning and can relate to intervention evidence; graph metadata identifies tree canopy and cool walls without claiming effectiveness. |
| edge_variant_004 | sq_004 → q_001 | relates_to | Defensible | A planner survey may touch plans and strategies, but it is not a HAP content analysis. |
| edge_variant_005 | sq_005 → q_001 | relates_to | Defensible | Governance study across municipal plans is related to plan content but is not component coding. |
| edge_variant_006 | sq_006 → q_004 | relates_to | Defensible | Preparedness actions are conceptually related to interventions, but the source does not evaluate specific cooling measures. |
| edge_variant_007 | sq_007 → q_006 | relates_to | Understated | The blind review marked a moderate direct equity candidate; the graph’s secondary link is conservative and defensible, but weaker than the prior candidate. |
| edge_variant_008 | sq_008 → q_004 | relates_to | Defensible | A HAP is an intervention, but this source evaluates mortality rather than comparing cooling measures. |
| edge_variant_009 | sq_011 → q_006 | relates_to | Exact | Urban form may vary across neighborhoods, but the supplied evidence does not assert a sociodemographic disparity analysis. |
| edge_variant_010 | sq_012 → q_001 | relates_to | Exact | Municipal greenspace policy is related to HAP content but is not HAP-component analysis. |
| edge_variant_011 | sq_015 → q_005 | relates_to | Exact | A metadata-only systematic review may relate to evaluation, but cannot directly substantiate methods. |
| edge_variant_012 | sq_018 → q_004 | relates_to | Defensible | Infrastructure strategies are interventions, but this evidence concerns modeled multi-outcome trade-offs rather than a broad intervention synthesis. |

## Summary

- **Generated direct-support edges:** 22.  
- **Direct supports exact:** 14.  
- **Direct supports defensible:** 4.  
- **Direct supports overclaimed:** 4.  
- **Direct supports unsupported:** 0.  
- **Direct-support precision:** `18/22 = 0.818` using exact + defensible as accepted direct support.  
- **Blind direct-support candidate pairs:** 25.  
- **Best-mapped direct-support recall:** `23/25 = 0.920`. The two less-well represented blind candidates were `sq_007 → q_006` and `sq_012 → q_002`.  
- **Generated secondary links:** 12.  
- **Secondary links exact:** 6.  
- **Secondary links defensible:** 5.  
- **Secondary links understated:** 1.  
- **Secondary relation precision:** `12/12 = 1.000` at the relation level, with one link understated relative to the prior candidate.  
- **Overall relation precision:** `30/34 = 0.882` when exact + defensible count as accepted and the understated secondary link is not counted as accepted.

## Unsupported and overclaimed edges

**Overclaimed direct supports:**

- `edge_support_006`: `sq_006 → q_001`. Preparedness/HAP relevance was treated as direct support for HAP content.
- `edge_support_011`: `sq_010 → q_001`. Title-only strengthening commentary was treated as direct support for plan components/gaps.
- `edge_support_018`: `sq_014 → q_008`. A cooling-intervention review was treated as direct support for cooling-center placement/access.
- `edge_support_019`: `sq_015 → q_001`. Metadata-only HAP-review evidence was treated as direct support for plan components/gaps.

**Unsupported edges:** None. Every generated relation had a defensible topical basis; the failures were directness or construct/outcome specificity rather than complete lack of relation.

**Basis caveats:** Some secondary-edge rationales rely on graph metadata beyond the evidence-packet quotes, especially for `edge_variant_003`, `edge_variant_007`, and `edge_variant_008`. Those rationales are defensible in the graph context, but they would not all be independently provable from the packet quotes alone.

## Missing or understated relationships

- **`sq_007 → q_006`:** The graph uses `relates_to`; the blind review had identified a moderate direct equity/risk-distribution candidate. The generated secondary link is conservative and defensible but understated relative to that prior judgment.
- **`sq_012 → q_002`:** No direct municipal-governance relation was generated for the London municipal policy source. The graph’s `q_007` target is more precise, but a `q_002` conceptual link would also be defensible.
- **`sq_008 → q_002`:** The graph captures the HAP evaluation and mortality outcome through `q_005` and `q_003`. A secondary governance relation is plausible but less central and should not be treated as a required correction.

## Preserved distinctions

- The graph correctly keeps HAP content, municipal governance, evaluation methods, and health outcomes separate.
- It correctly avoids treating generic urban cooling as direct equity evidence.
- It keeps `src_013` cooling-center access and `src_017` heat-risk distribution as direct equity/risk-distribution evidence without inferring health-care use.
- It keeps `src_008` as the clearest HAP-to-mortality evaluation and does not generalize that result to all cooling interventions.
- It keeps lived experience and healthcare-use areas absent rather than manufacturing unsupported links.

## Updated reviewer verdict

- [ ] Pass
- [x] Conditional pass
- [ ] Fail

**Reason:** Most generated direct and secondary relations are semantically sound: 18/22 direct edges are exact or defensible and all 12 secondary links are defensible at the relation level. The conditional verdict reflects four overclaimed direct edges, two conservative/missing governance-equity mappings, and the need to keep packet-level evidence distinct from graph metadata when auditing directness.

**Edges requiring correction:**

1. `edge_support_006` — downgrade `supports` or rephrase `q_001` to a broader preparedness/HAP question.
2. `edge_support_011` — downgrade `supports` or require a fuller quote showing that the commentary addresses HAP content.
3. `edge_support_018` — downgrade `supports` or narrow the target to the cooling-center intervention family rather than placement/access outcomes.
4. `edge_support_019` — downgrade `supports` unless a fuller abstract demonstrates that the review directly addresses HAP components/omissions.

Optional refinements: add or upgrade `sq_007 → q_006` if richer evidence supports risk distribution, and add `sq_012 → q_002` as a conceptual municipal-governance link.
