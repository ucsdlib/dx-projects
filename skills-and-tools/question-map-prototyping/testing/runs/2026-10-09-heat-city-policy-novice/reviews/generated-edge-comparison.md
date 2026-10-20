# Generated-Edge Comparison

**Run ID:** `2026-10-09-heat-city-policy-novice`  
**Compared against:** `reviews/edge-adjudication-sheet.md`  
**Graph inputs inspected:** `question_map.json` and `visualizations/edge-validation.md`  
**Review date:** 2026-10-09

## Scope and method

This comparison covers the 20 generated `source_question -> question` edges marked `supports` and the 10 marked `relates_to`. The graph was not modified. A generated `supports` edge was classified `exact` when it matched the blind direct relation and canonical target; `defensible` when the target was a reasonable canonicalization but not a precise component match; `understated` when the evidence justified a stronger relation; `overclaimed` or `unsupported` when the relation exceeded the blind evidence; and `missing` when the blind adjudication identified a relationship absent from the graph.

The graph labels every source-to-source-question edge as `infers`. That is compared separately below because it concerns question-origin labeling rather than the direct-support and secondary-link edges.

## Direct `supports` edge comparison

| Edge ID | Generated relation | Reviewer relation | Verdict | Rationale |
|---|---|---|---|---|
| `edge_sq_q_001` | S01 → heat-related health outcomes/use | Direct support | `exact` | Both identify the empirical heat-to-ED-use relation. |
| `edge_sq_q_002` | S02 → heat-related health outcomes/use | Direct support | `exact` | Both identify heat-related ED-visit surveillance. |
| `edge_sq_q_003` | S03 → heat-related health outcomes/use | Direct support | `exact` | Both identify heat-wave mortality risk. |
| `edge_sq_q_004` | S04 → heat-related health outcomes/use | Direct support | `exact` | Both identify mental-health-related ED use. |
| `edge_sq_q_005` | S05 → measuring/mapping vulnerability | Direct support | `defensible` | The measurement relation is direct, but the graph target does not separately preserve the equity-targeting relation. |
| `edge_sq_q_006` | S06 → measuring/mapping vulnerability | Direct support | `exact` | Both identify spatial mapping of vulnerability determinants. |
| `edge_sq_q_007` | S07 → equitable access to cooling resources | Direct support | `exact` | Both identify cooling-center access for heat-vulnerable populations. |
| `edge_sq_q_008` | S08 → equitable access to cooling resources | Direct support | `exact` | Both identify differential exposure and refuge access by socio-demographic status. |
| `edge_sq_q_009` | S09 → urban form, green space, and cooling | Direct support | `exact` | Both identify empirical urban-greening cooling evidence. |
| `edge_sq_q_010` | S10 → urban form, green space, and cooling | Direct support | `exact` | The canonical question includes cooling and heat-related health outcomes, matching the health-impact assessment. |
| `edge_sq_q_011` | S11 → urban form, green space, and cooling | Direct support | `exact` | Both compare urban form and extreme-heat vulnerability. |
| `edge_sq_q_012` | S12 → governance, warnings, and emergency response | Direct support | `exact` | Both address heat-health action plans and warning-system governance. |
| `edge_sq_q_013` | S13 → governance, warnings, and emergency response | Direct support | `defensible` | The governance relation is appropriate, though the metadata did not establish the plan-assessment criteria. |
| `edge_sq_q_014` | S14 → governance, warnings, and emergency response | Direct support | `exact` | Both evaluate heat-warning-system effectiveness. |
| `edge_sq_q_015` | S15 → governance, warnings, and emergency response | Direct support | `exact` | Both address planned heat adaptation as a governance response. |
| `edge_sq_q_016` | S16 → lived experience and social adaptive capacity | Direct support | `exact` | Both use the social-autopsy framing for lived and social consequences. |
| `edge_sq_q_017` | S17 → lived experience and social adaptive capacity | Direct support | `exact` | Both address differential household adaptive capacity. |
| `edge_sq_q_018` | S18 → lived experience and social adaptive capacity | Direct support | `exact` | Both address stakeholder perceptions among cultural and linguistic minorities. |
| `edge_sq_q_019` | S19 → heat-related health outcomes/use | Direct support | `exact` | Both address temperature-attributable mortality risk. |
| `edge_sq_q_020` | S20 → governance, warnings, and emergency response | Direct support | `defensible` | Warning-system development guidance is a direct governance source, but it remains operational guidance rather than causal evidence. |

## Secondary `relates_to` edge comparison

| Edge ID | Generated relation | Reviewer relation | Verdict | Rationale |
|---|---|---|---|---|
| `edge_sq_related_041` | S05 → evaluating adaptation effectiveness | Not in blind relation set | `defensible` | A new but plausible conceptual link from vulnerability indicators to evaluation. |
| `edge_sq_related_042` | S06 → equitable access to cooling resources | Blind direct support to vulnerable populations/equity | `understated` | The graph treats as conceptual a link the blind adjudication treated as directly equity-relevant. |
| `edge_sq_related_043` | S09 → evaluating adaptation effectiveness | Not in blind relation set | `defensible` | A reasonable conceptual link between cooling evidence and intervention-evaluation quality. |
| `edge_sq_related_044` | S11 → measuring/mapping vulnerability | Blind conceptual link to vulnerability/equity | `defensible` | The graph target is a reasonable canonicalization of the conceptual vulnerability relation. |
| `edge_sq_related_045` | S12 → evaluating adaptation effectiveness | Not in blind relation set | `defensible` | A plausible link from plan review to implementation and evidence limitations. |
| `edge_sq_related_046` | S15 → evaluating adaptation effectiveness | Blind direct support to measurement/evidence limitations | `understated` | The blind adjudication treated this as direct evidence-limitation support, not merely a low-confidence conceptual link. |
| `edge_sq_related_047` | S16 → measuring/mapping vulnerability | Blind direct support to vulnerable populations/equity | `understated` | The social-autopsy evidence directly supports equity context, though the graph target emphasizes vulnerability measurement. |
| `edge_sq_related_048` | S17 → equitable access to cooling resources | Blind direct support to vulnerable populations/equity | `understated` | Differential household adaptive capacity directly informs equitable access, so a low-confidence conceptual edge is weaker than warranted. |
| `edge_sq_related_049` | S18 → governance, warnings, and emergency response | Blind conceptual link | `exact` | Both treat cultural and linguistic barriers as conceptually relevant to emergency communication. |
| `edge_sq_related_050` | S19 → evaluating adaptation effectiveness | Blind direct support to measurement/evidence limitations | `understated` | The multicountry modeling assumptions support measurement limitations directly, not merely by analogy. |

## Missing or unrepresented relationships

| Source | Case component / relation | Reviewer relation | Graph status | Rationale |
|---|---|---|---|---|
| S07 | Governance, policy, and emergency response | Direct support | Missing | Cooling-center accessibility is also an operational response component, but the graph represents only equitable access. |
| S08 | Urban form, green space, and cooling | Direct support | Missing | The city-scale heat/refuge assessment directly concerns urban conditions, but the graph represents only equitable access. |
| S18 | Vulnerable populations and equity | Direct support | Missing | Cultural and linguistic minorities are directly equity-relevant, but no separate equity edge is present. |
| S02 | Vulnerable populations and equity | Conceptual support | Missing | Demographic patterns can contextualize vulnerability, but no secondary link was generated. |
| S06 | Urban form, green space, and cooling | Conceptual support | Missing | The spatial vulnerability determinants may overlap with urban form, but no secondary link was generated. |
| S09 | Health outcomes and healthcare use | Conceptual support | Missing | Cooling evidence may relate to health, but the graph correctly avoids direct support; a low-confidence secondary link would be more complete. |
| S14 | Health outcomes and healthcare use | Conceptual support | Missing | Warning-system effectiveness may use health endpoints, but no secondary health-outcome link was generated. |
| S15 | Health outcomes and healthcare use | Conceptual support | Missing | Adaptation effectiveness may use health endpoints, but no secondary health-outcome link was generated. |
| S16 | Governance, policy, and emergency response | Conceptual support | Missing | Institutional failure may be relevant to governance, but no secondary governance link was generated. |
| S20 | Measurement or evidence limitations | Conceptual support | Missing | Guidance can inform measurement and system-design limitations, but no secondary link to evaluation was generated. |

No generated `supports` or `relates_to` edge was classified `overclaimed` or `unsupported`.

## Source-question origin agreement

The blind adjudication classified 15/20 source questions as stated (`asks` or `reviews`) and 5/20 as inferred (`infers`). The graph labels all 20 source questions as `inferred`. The five origin matches are S02, S16, S17, S18, and S20. The remaining 15 origins are systematically understated, though this does not by itself invalidate the 20 direct-support edges.

## Summary precision and recall

- **Generated direct-support precision:** 20/20 = 1.000 at `defensible`-or-better level; 18/20 = 0.900 at strict `exact` level.
- **Strict direct-edge recall against blind direct relations:** 20/31 = 0.645.
- **Graph-coverage recall for blind direct relations:** 28/31 = 0.903 when either a direct `supports` or a secondary `relates_to` edge is accepted; S07 governance, S08 urban form, and S18 equity remain absent.
- **Secondary-link precision:** 10/10 = 1.000 at `defensible`-or-better level; 1/10 = 0.100 at strict `exact` level.
- **Blind conceptual-link recall:** 2/9 = 0.222; the graph includes only S11→measuring/mapping vulnerability and S18→governance from the blind conceptual set, while adding eight plausible new secondary links.
- **Unsupported generated edges:** 0.
- **Overclaimed generated edges:** 0.
- **Understated generated edges:** 4 secondary links plus 15 source-question origin labels.
- **Missing relationships:** 3 blind direct relations and 7 blind conceptual relations listed above.

## Updated verdict

- [x] Conditional pass
- [ ] Pass
- [ ] Fail

**Reason:** The generated direct-support layer is strong: no direct edge was overclaimed or unsupported, and all 20 are defensible or better. However, the graph omits three defensible direct relations, understates several evidence/measurement links, lacks some useful conceptual bridges, and systematically marks stated source questions as inferred. These are correctable annotation and coverage issues rather than structural failures.
