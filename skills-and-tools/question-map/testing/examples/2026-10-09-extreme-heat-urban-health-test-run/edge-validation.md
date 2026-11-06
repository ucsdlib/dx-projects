# Edge validation — extreme heat and urban health/wellbeing

**Audited graph:** `question_map.json` (schema v0.1)  
**Edges:** 95  
**Validation:** graph passes the skill validator; this file adds a substantive audit beyond referential integrity.

## Summary

| Edge group | Count | Verdict |
|---|---:|---|
| Source → source question | 20 | Valid after splitting `asks` from `infers` |
| Source question → canonical question (primary) | 20 | Valid |
| Source question → canonical question (secondary) | 20 | Valid but interpretive; demoted to `variant_of`, medium confidence |
| Question → question | 6 | Valid structural relations |
| Question → theme | 17 | Valid after moving the root prompt out of the analytical question graph |
| Question → possible next question | 12 | Valid as generated inquiry paths, not evidence claims |

## Specific corrections

1. **Inferred source questions** (`sq_006`, `sq_007`, `sq_008`, `sq_009`, `sq_011`, `sq_012`) now use `infers`, not `asks`. Their evidence is a title or abstract, not a stated objective.
2. **Secondary source-question mappings** are now `variant_of` with medium confidence instead of `supports` with high confidence. This prevents them from being counted as primary support and reduces the false impression that every source directly answers two canonical questions.
3. **Prompt framing** was corrected. The user prompt is no longer rendered as an analytic question node. It is retained as `ctx_001` (`context`) with `root_status: primary_user_root`, and the document title uses the prompt directly.

## Interpretation

The source-to-source-question edges are supported by the retained abstract/title text. The primary source-question-to-question edges are justified by the source-specific wording. The secondary mappings are useful for exploration, but they should be read as conceptual variants rather than direct evidence.

The visualization is now more accurate because:

- source cards are not duplicated across multiple question sections;
- inferred title-derived questions are no longer presented as if directly stated;
- the root question is no longer visually attached to a narrower theme.

## Remaining limitations

- Evidence remains abstract-plus-metadata; no PDFs were extracted.
- The graph is an exploratory map, not a systematic review.
- Citation counts measure attention, not correctness or consensus.
