# Edge validation

**Audited graph:** `urban-extreme-heat-health-2026-10-06`
**Edges:** 89

## Summary

| Edge group | Count |
|---|---:|
| Source → source question | 23 |
| Source question → canonical question (direct support) | 23 |
| Source question → canonical question (secondary conceptual) | 0 |
| Question → primary theme membership | 8 |
| Question → cross-cutting theme membership | 0 |

## Interpretation

- Direct support is limited to `source_question -> question` edges with relation `supports`.
- A source question may have more than one direct-support edge when each edge has evidence.
- Secondary conceptual links use `variant_of` or `relates_to` and are not counted as direct evidence support.
- Source cards distinguish `asks` (stated) from `infers` (inferred) where the graph records that distinction.
- Theme membership is shown once for primary containment and as cross-cutting for secondary relevance.

## Limitations

- This audit summarizes edge semantics; it does not replace source-level evidence review.
- Corrections made during graph construction should still be recorded in the run log.
