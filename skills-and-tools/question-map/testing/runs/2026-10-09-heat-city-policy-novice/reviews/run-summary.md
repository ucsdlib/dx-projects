# Run Summary

**Run ID:** 2026-10-09-heat-city-policy-novice  
**Case ID:** heat-city-policy-novice  
**Date:** 2026-10-09  
**Coordinator:** Independent reviewer sessions  
**Adjudicator:** Fresh-session Adjudicator  

## Phase status

| Phase | Status | Reviewer(s) | Key issue |
|---|---|---|---|
| Independent reference pool | Pass | Search Auditor; Source-Selection Reviewer | All 20 independently identified sources were retained and no selected source was irrelevant or unsupported. |
| Graph generation | Conditional pass | Evidence Auditor; Generated-Edge Comparison | Direct edges had no unsupported or overclaimed verdicts, but source-question provenance and some relationship granularity were wrong. |
| Validation and build | Conditional pass | Coordinator build log; Visualization Review | Referential validation passed and the graph has explicit theme roles, but the validator did not catch provenance error, unsupported cross-cutting assignments, or next-question/theme mismatches. |
| Source selection review | Conditional pass | Source-Selection Reviewer; Practitioner Reviewer | 20/20 sources were relevant, but the set was overinclusive for a novice city stakeholder and underrepresented implementation, cost, recent lived experience, and some populations. |
| Edge adjudication | Conditional pass | Evidence Auditor; Generated-Edge Comparison | 20 direct-support edges were defensible or better and none was unsupported, but three blind direct relations and seven conceptual relations were missing; 15 stated questions were labeled inferred. |
| Theme membership review | Fail | Theme Membership Reviewer | Explicit `primary` and `cross_cutting` roles are present, but three cross-cutting links were unsupported and all five next-question/theme edges disagreed with theme records. |
| Visualization review | Conditional pass | Visualization and Accessibility Reviewer; Novice Visualization Reviewer; Practitioner Reviewer | Orientation and semantic distinctions were strong, but interactive HTML has accessibility gaps, unlabeled source nodes, uncertain live-filter behavior, and metadata-strength wording risks. |

## Scores

| Measure | Result | Provisional gate | Pass? |
|---|---:|---|---|
| Source precision | 20/20 = 100%; all rated 2–3 | No selected source irrelevant or unsupported | Yes |
| Reference recall | 20/20 independent pool sources included = 100% | Core independent sources included | Yes |
| Component coverage | 6/6 required components covered = 100%; several weakly operationalized | Every major component covered or explicitly marked as a gap | Yes |
| Multi-question fidelity | 10/10 generated secondary relationships defensible or better; 0 overclaimed | Defensible multi-question links represented without arbitrary forcing or overclaim | Yes |
| Direct support precision | 20/20 = 100% at defensible-or-better; 18/20 = 90% strict exact | No direct support edge judged unsupported | Yes |
| Direct support recall | 20/31 = 64.5% strict; 28/31 = 90.3% if secondary coverage is accepted | No provisional threshold; coverage gap recorded | Conditional |
| Stated/inferred agreement | 5/20 = 25% | At least 85% agreement | No |
| Secondary-link overclaim rate | 0/10 = 0%; four links understated | Secondary links not overclaimed | Yes |
| Theme-membership agreement | 15/18 = 83.3%; 7 primary and 8 cross-cutting assignments agreed; 3 unsupported | No theme implies containment where the relationship is cross-cutting; unsupported memberships must be corrected | Conditional |
| Unsupported edge count | 0 | 0 unsupported direct or secondary edges | Yes |
| Novice orientation success | 7/7 core orientation tasks completed; both novice-context reviewers found a useful next step | Novice can orient and identify a useful next step | Yes |

### Provisional gate roll-up

| Gate | Result |
|---|---|
| Referential validation passes | Pass |
| No selected source is irrelevant or unsupported | Pass |
| Every major component is covered or transparently marked as a gap | Pass |
| No direct support edge is judged unsupported | Pass |
| No secondary relationship is visually indistinguishable from direct support | Pass, with live interaction untested |
| Source-question origin labels agree with evidence in at least 85% of adjudicated cases | Fail (25%) |
| No theme implies containment where reviewers judge the relationship cross-cutting | Pass structurally; three unsupported cross-cutting assignments remain |
| Novice reviewers can orient and identify a useful next step | Pass |
| User prompt appears as framing, not as an unsupported canonical question | Pass |

## Reviewer disagreements

| Topic | Reviewers | Positions | Adjudicated decision | Rationale |
|---|---|---|---|---|
| Theme membership roles | Theme Membership Reviewer; Visualization Reviewer; question_map.json | Theme reviewer said roles were missing; visualization reviewer counted 7 primary and 11 cross-cutting links. | Reject the “missing roles” claim, but sustain the substantive theme findings. | The graph has explicit `role` fields on all 18 `member_of` edges: 7 `primary` and 11 `cross_cutting`. Eight cross-cutting assignments match the reviewer’s semantic classification. Three—`edge_theme_002` (q_001→theme_006), `edge_theme_007` (q_003→theme_006), and `edge_theme_012` (q_005→theme_006)—should be removed or split rather than retained as cross-cutting. |
| Metadata evidence versus direct support | Evidence Auditor; Generated-Edge Comparison | The blind audit warned that metadata alone cannot establish several effectiveness/health claims. The comparison found no generated direct edge unsupported or overclaimed. | Both are correct at different layers. | The five candidate relations the blind audit rejected as direct support were not admitted as generated direct support. Still, all support is metadata-derived, and S09→health, S11→governance, S16→quantitative intervention effect, S18→policy effect, and S20→causal effectiveness must remain out of the direct layer unless full text supports them. |
| Theme semantics versus visualization pass | Theme Membership Reviewer; Visualization Reviewer | Theme review failed; visualization review passed. | Reconcile: rendering distinguishes roles, but data semantics still fail. | Explicit roles prevent primary containment from being visually implied, satisfying the containment gate structurally. They do not cure unsupported q_006-like measurement assignments or the systematic next-question/theme mismatch. |
| Source relevance versus novice-actionability | Source-Selection Reviewer; Practitioner Reviewer | Source review found all 20 relevant; practitioner found the result inadequate as a city decision bridge. | Both findings stand. | Topical precision is high, but a novice needs local implementation, governance, data, cost, operations, and feasibility questions that the scholarly map does not currently provide. |
| Direct-support strength for novices | Novice Visualization Reviewer; Visualization Reviewer; Practitioner Reviewer | Novice worried that “direct support” plus “inferred” could imply stronger evidence; accessibility reviewer found the distinction visible; practitioner wanted uncertainty more operational. | Conditional visualization finding. | Solid/dashed styling and labels are honest, but the UI should explicitly state that direct support means metadata-supported relevance to the question, not full-text effect confirmation. |
| Broken source links | Visualization Reviewer; Source-Selection Reviewer | Eight of twenty HTTP checks returned 403. | Do not score these as broken links. | 403 responses are consistent with publisher or bot protection. Record accessibility as partial, but preserve the URLs unless browser-level checks fail. |
| Next-question theme placement | Theme Membership Reviewer; question_map.json | Theme records and `proposed_for` edges disagreed. | Sustain the reviewer’s mismatch finding. | Direct inspection confirms: nq_001→theme_001 instead of theme_004; nq_002→theme_002 instead of theme_003; nq_003→theme_003 and nq_004→theme_004 instead of theme_002; nq_005→theme_005 instead of theme_006. |

## Triage

| Issue | Artifact/node/edge | Root cause | Proposed fix | Regression fixture needed? |
|---|---|---|---|---|
| 15 stated source questions labeled inferred | All `sq_*` and `infers` edges except S02, S16, S17, S18, and S20 | Source-question extraction | Preserve title/method-derived stated-question provenance; require per-source evidence-basis quotes for `asks`, `reviews`, or `infers`; recompute agreement. | Yes — 15-stated/5-inferred provenance fixture |
| Three unsupported measurement-theme assignments | `edge_theme_002`, `edge_theme_007`, `edge_theme_012` | Theme membership; canonicalization | Remove or split into narrower methodological source questions; retain only evidence-supported cross-cutting links. | Yes — unsupported methodological containment fixture |
| Next-question/theme mismatch | `edge_nq_theme_001` through `edge_nq_theme_005` | Validator gap | Align `proposed_for` targets with theme `next_question_ids`; add a cross-field consistency validator. | Yes — next-question/theme consistency fixture |
| Three blind direct relations absent | S07→governance; S08→urban form; S18→equity | Edge semantics; canonicalization | Add or explicitly justify direct component edges, using canonical targets that preserve the original component. | Yes — multi-component direct-support fixture |
| Four direct relations encoded as secondary | `edge_sq_related_042`, `edge_sq_related_046`, `edge_sq_related_047`, `edge_sq_related_048` | Edge semantics | Upgrade S06→equity/access, S15→measurement limitations, S16→equity, and S17→equity/access where metadata supports direct component treatment; otherwise document the stricter interpretation. | Yes — understated-versus-direct relation fixture |
| Seven conceptual bridges absent | S02, S06, S09, S14, S15, S16, and S20 secondary candidates | Edge semantics; coverage | Add low-confidence conceptual links only where the blind evidence supports them and keep them visually secondary. | No — improve recall, but do not create an unsupported-edge fixture |
| Practitioner decision layer missing | Graph questions; next questions; HTML and Markdown views | Skill instruction gap; canonicalization | Add a separate novice/city-action layer with local baseline data, ownership, authority, budget, staffing, operations, procurement, feasibility, community engagement, and evaluation questions. Do not mix it into source-backed causal evidence. | Yes — novice practitioner-orientation fixture |
| Interactive HTML is not accessibility-verified or keyboard-equivalent | `question-map-force.html` | Visualization layout or readability; validator gap | Add keyboard reachability, accessible names, focus-triggered details, live-region announcements, visible source labels, text fallback, reduced-motion support, and responsive labels; then test keyboard and screen-reader use. | Yes — keyboard/screen-reader visualization fixture |
| Live relationship filtering untested | HTML relationship controls | Validator gap | Add automated DOM/interaction checks for all four relationship filters and both landscape/evidence views. | Yes — filter-state fixture |
| “Direct support,” confidence, and metadata-only basis may be misread | Source cards, edge labels, theme confidence, HTML and Markdown | Documentation or skill instruction gap | Use a short UI definition: metadata-derived direct support is not full-text causal confirmation; replace or qualify theme “high confidence” in user-facing views. | Yes — metadata-strength labeling fixture |
| Source set is overinclusive for novice implementation use | S11 and S13 in particular; broader 20-source set | Source selection | Prune or demote historical/contextual records when they are not needed; add local implementation, cost-effectiveness, municipal guidance, recent participatory lived-experience, disability, renter, older-adult, and outdoor-worker evidence as available. | Yes — novice relevance-pruning fixture |
| Closed-access metadata-only records constrain claim extraction | S05, S09, S12, S13, S14, S16, and S17 | Search strategy or coverage; source-question extraction | Capture abstracts or lawful full text before source-specific substantive mapping; retain metadata-only labels otherwise. | No — operational access improvement |

## Decision

- [ ] Pass
- [ ] Conditional pass
- [x] Fail

**Reason:** This run is not accepted as passing because it fails an explicit provisional acceptance gate: only 25% of source-question origin labels agree with the blind evidence, versus the required 85%. The failure is systematic but narrowly correctable. The run otherwise has strong foundations: no selected source is irrelevant, all six components are covered, no generated direct or secondary edge is unsupported or overclaimed, explicit theme roles distinguish primary from cross-cutting membership, and both novice-context reviewers can orient and identify a useful next step. The user prompt remains framing rather than a canonical question.  

**Required before next run:**  

1. Correct all source-question origin labels and add a provenance regression fixture; require at least 85% adjudicated agreement.
2. Remove or split the three unsupported measurement-theme assignments and retain explicit `primary`/`cross_cutting` roles.
3. Align all five `proposed_for` edges with their themes’ `next_question_ids` and add schema-level cross-field validation.
4. Add or justify the three missing blind direct relations and resolve the four understated secondary links.
5. Add a novice practitioner/data-gap layer and make metadata-derived support wording explicit in the user-facing views.
6. Repair and test interactive-view keyboard access, accessible names, focus behavior, filters, source labels, and reduced-motion support.
7. Prune or demote low-value contextual sources where appropriate, and capture abstracts or lawful full text for closed-access metadata-only records before substantive mapping.
