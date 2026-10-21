# Theme Membership Review

**Run ID:** 2026-10-09-heat-city-policy-novice  
**Case ID:** heat-city-policy-novice  
**Reviewer:** Independent domain expert — theme-and-question review  
**Review date:** 2026-10-09  
**Inputs reviewed:** `00-case.md`, `question_map.json`, and the blank theme-membership review template only.

## Question-level theme review

The map encodes every question-theme relation as `member_of`. It does not encode whether that relation means primary containment or cross-cutting relevance. The reviewer roles below therefore treat the seven substantive theme anchors as primary and the remaining links as either cross-cutting or unsupported.

| Question ID | Theme | Generated role | Reviewer role | Agreement? | Rationale |
|---|---|---|---|---|---|
| q_001 | theme_001 | Unspecified; encoded as `member_of` | `primary` | Yes, if an explicit primary role is added | q_001 asks about health outcomes and healthcare use. Metadata titles for src_001–src_004 and src_019 directly concern emergency-department visits, mortality risk, and mental-health visits. |
| q_001 | theme_006 | Unspecified; encoded as `member_of` | `none` | No | The question is substantive, not methodological. A multicountry mortality study (src_019) does not by itself justify membership in a measurement-and-evidence-limitations theme. |
| q_002 | theme_002 | Unspecified; encoded as `member_of` | `primary` | Yes, if an explicit primary role is added | q_002 is the vulnerability-identification and mapping question. Titles for src_005 and src_006 directly support this relation. |
| q_002 | theme_006 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | Vulnerability indicators and mapping methods are methodologically relevant, but q_002 should not be treated as contained by the measurement theme. |
| q_003 | theme_001 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | The link is defensible because src_010's title connects green infrastructure to heat-related health outcomes, but the primary relation is to urban form and cooling. |
| q_003 | theme_003 | Unspecified; encoded as `member_of` | `primary` | Yes, if an explicit primary role is added | q_003 is the urban-form, green-space, and cooling question. src_009–src_011 directly support this theme. |
| q_003 | theme_006 | Unspecified; encoded as `member_of` | `none` | No | The question concerns substantive urban-form effects. A systematic-review title alone does not make q_003 a member of the measurement-limitations theme. |
| q_004 | theme_004 | Unspecified; encoded as `member_of` | `primary` | Yes, if an explicit primary role is added | q_004 concerns governance, warnings, and emergency response. Titles for src_012, src_013, src_014, src_015, and src_020 support it. |
| q_004 | theme_006 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | Effectiveness evaluation is relevant to governance evidence, but q_004 is primarily a governance question, not a methodological question. |
| q_005 | theme_002 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | Social circumstances and adaptive capacity relate to vulnerability and equity, but the primary relation is lived experience. |
| q_005 | theme_005 | Unspecified; encoded as `member_of` | `primary` | Yes, if an explicit primary role is added | q_005 concerns lived experience and adaptive capacity. Titles for src_016–src_018 directly support this relation. |
| q_005 | theme_006 | Unspecified; encoded as `member_of` | `none` | No | Social context is not automatically an evidence-limitation issue. Membership here applies a methodological frame to a substantive question. |
| q_006 | theme_002 | Unspecified; encoded as `member_of` | `primary` | Yes, if an explicit primary role is added | q_006 concerns equitable access to cooling resources and refuge. src_007 and src_008 titles directly support this relation. |
| q_006 | theme_004 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | Access can inform municipal response, but q_006 is not primarily a governance-response question. |
| q_006 | theme_005 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | Access and refuge can connect to lived experience and adaptive capacity, but the map's direct source-question support for this link is limited. |
| q_007 | theme_001 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | Effectiveness evaluation may use mortality and emergency-department endpoints, but q_007 is primarily methodological rather than a health-outcomes question. |
| q_007 | theme_004 | Unspecified; encoded as `member_of` | `cross_cutting` | No — relation type is under-specified | Warning-system evaluation relates to governance, but q_007 should not be contained by the governance theme. |
| q_007 | theme_006 | Unspecified; encoded as `member_of` | `primary` | Yes, if an explicit primary role is added | q_007 is the methodological question about adaptation and warning-system effectiveness. Titles for src_012, src_014, and src_015 support this anchor. |

## Conceptual-distinction check

| Issue | Present? | Node or edge IDs | Rationale |
|---|---|---|---|
| The user prompt is treated as a canonical question without direct source analysis | No | ctx_001; `request.core_question` | The raw prompt is stored as a context node rather than as q_001–q_007. However, `request.core_question` is phrased as “what … should … consider,” so it should be explicitly labeled as a working frame, not as a source-answerable canonical finding. |
| A theme implies containment where the evidence supports only cross-cutting relevance | Yes | edge_theme_002, edge_theme_005, edge_theme_006, edge_theme_007, edge_theme_009, edge_theme_011, edge_theme_014, edge_theme_015, edge_theme_017, edge_theme_018; theme_006 memberships | All question-theme links use `member_of`. This makes cross-cutting links such as q_003–theme_001, q_004–theme_006, and q_007–theme_004 appear to be containment. |
| A methodological question is attached to every relevant theme by default | No, but a related problem is present | q_007; theme_001, theme_004, theme_006; q_001–q_005 memberships in theme_006 | q_007 is not attached to every theme, so this specific trap is avoided. The related problem is that theme_006 attaches a measurement lens to substantive questions q_001, q_003, and q_005 without a corresponding methodological variant. |
| A narrower question is collapsed into a broader question | No | q_002–nq_004, q_003–nq_002, q_004–nq_001, q_006–nq_003, q_007–nq_005 | The `narrows_to` edges distinguish parent questions from proposed narrower questions. nq_003 and nq_004 are compound but still narrower than their parents. |
| A possible next question appears to be source-backed evidence | No, with a presentation risk | nq_001–nq_005; edge_nq_theme_001–edge_nq_theme_005 | The nodes are typed as next questions and have no source IDs or evidence basis. They are therefore distinguishable from findings. The `proposed_for` edges, however, point to the wrong themes and could mislead readers about where each proposal belongs. |

## Additional structural findings

- **Next-question/theme edge mismatch.** The thematic `next_question_ids` and the `proposed_for` edges disagree systematically:
  - nq_001 belongs in theme_004 by the theme record, but edge_nq_theme_001 targets theme_001.
  - nq_002 belongs in theme_003 by the theme record, but edge_nq_theme_002 targets theme_002.
  - nq_003 and nq_004 belong in theme_002 by the theme records, but the edges target theme_003 and theme_004 respectively.
  - nq_005 belongs in theme_006 by the theme record, but edge_nq_theme_005 targets theme_005.
- **Provisional status.** nq_001–nq_005 are correctly not represented as evidence findings, but `confidence: medium` may be read as evidentiary support rather than confidence in the proposed question's relevance.
- **Membership semantics.** `member_of` alone cannot distinguish primary containment from cross-cutting relevance. This is the central cause of the overstated containment problem.
- **Equity scope.** theme_002 appropriately keeps vulnerability, equity, and access as a distinct theme, but q_005 and q_006 require cross-cutting edges rather than containment. Additional equity links should not be inferred for q_001, q_003, or q_004 without clearer title/metadata support.

## Summary

- **Theme memberships reviewed:** 18 question-theme membership relations.
- **Agreements:** 7 primary anchors are substantively coherent.
- **Overstated containment links:** 11 nonprimary relations are encoded as `member_of`; 3 of these (q_001–theme_006, q_003–theme_006, and q_005–theme_006) are unsupported at the question level.
- **Missing cross-cutting links:** No additional equity link should be added on the current metadata-only evidence; the missing work is explicit typing of existing cross-cutting relations.
- **Canonicalization concerns:** The canonical questions are appropriately separated from the raw prompt, but `request.core_question` should be labeled as a working frame. The methodological theme is overbroad.

## Reviewer verdict

- [ ] Pass
- [ ] Conditional pass
- [x] Fail

**Reason:** The graph correctly separates the user prompt from canonical questions and clearly types possible next questions as provisional. However, all question-theme relations use `member_of` without distinguishing primary containment from cross-cutting relevance. The measurement theme over-contains substantive questions, and all five possible-next-question/theme edges contradict the themes' own `next_question_ids`.

**Theme or question fixes:**

1. Add an explicit `membership_role` (`primary` or `cross_cutting`) to question-theme edges, or replace nonprimary `member_of` edges with a typed `relates_to` relation.
2. Retain as primary containment only: q_001–theme_001, q_002–theme_002, q_003–theme_003, q_004–theme_004, q_005–theme_005, q_006–theme_002, and q_007–theme_006.
3. Convert the eight defensible nonprimary links to cross-cutting relations: q_002–theme_006, q_003–theme_001, q_004–theme_006, q_005–theme_002, q_006–theme_004, q_006–theme_005, q_007–theme_001, and q_007–theme_004.
4. Remove or split q_001–theme_006, q_003–theme_006, and q_005–theme_006 unless narrower methodological source questions are added.
5. Reconcile proposed-next-question theme edges with the theme records: nq_001→theme_004, nq_002→theme_003, nq_003→theme_002, nq_004→theme_002, and nq_005→theme_006. Add secondary `relates_to` links only where explicitly justified.
6. Replace next-question `confidence: medium` with a provisional status such as `proposed_only`, or document that confidence refers to framing relevance rather than evidentiary support.
7. Label `request.core_question` as the working framing question, not a canonical node or supported finding.
