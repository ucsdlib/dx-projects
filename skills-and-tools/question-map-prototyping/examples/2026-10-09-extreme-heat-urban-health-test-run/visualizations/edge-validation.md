# Edge validation

**Audited graph:** `run-2026-10-09-extreme-heat-urban-health`
**Edges:** 95

## Summary

| Edge group | Count |
|---|---:|
| Source → source question | 20 |
| Source question → canonical question (direct support) | 20 |
| Source question → canonical question (secondary conceptual) | 20 |
| Question → primary theme membership | 7 |
| Question → cross-cutting theme membership | 10 |

## Interpretation

- Direct support is limited to `source_question -> question` edges with relation `supports`.
- A source question may have more than one direct-support edge when each edge has evidence.
- Secondary conceptual links use `variant_of` or `relates_to` and are not counted as direct evidence support.
- Source cards distinguish `asks` (stated) from `infers` (inferred) where the graph records that distinction.
- Theme membership is shown once for primary containment and as cross-cutting for secondary relevance.

## Limitations

- This audit summarizes edge semantics; it does not replace source-level evidence review.
- Corrections made during graph construction should still be recorded in the run log.
