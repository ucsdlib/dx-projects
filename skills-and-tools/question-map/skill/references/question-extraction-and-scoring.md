# Question Extraction, Themes, and Scoring

Read this reference before extracting questions or assigning scores.

## Source-question extraction

Extract every source question supported by the available text, not only the central question. A source can contribute multiple questions. A source can also contribute no supported question.

For each `source_question`, record:

- a concise source-specific question text;
- a canonical label only if it maps to a canonical `question`;
- variants or near-duplicate labels;
- origin (`explicit` or `inferred`);
- connection type;
- access level and evidence basis;
- quote IDs or, for metadata-only evidence, an explicit metadata-derived rationale;
- confidence;
- extraction rationale.

### Connection types

| Type | Use when |
|---|---|
| `direct_evidence` | The source explicitly states the question, objective, aim, hypothesis, review objective, or research gap. |
| `reasonable_inference` | The stated purpose, methods, findings, title, abstract, or limitation clearly implies the question. |
| `interpretive_connection` | The source addresses a related domain that may frame the question, but the connection requires a documented interpretive step. |

Only `direct_evidence` and `reasonable_inference` count as primary theme support. `interpretive_connection` can remain visible with lower confidence.

### Edge meaning

Use `asks` for an explicit question, objective, aim, hypothesis, review objective, or research gap. Use `infers` for a question derived from a title, abstract, findings, methods, or metadata. Reserve `raises` for a question the source explicitly raises without pursuing, and `reviews` for a synthesis or review question.

Give each `source_question` at least one evidence-backed `supports` edge. A source question may support more than one canonical question when the evidence warrants it; do not impose an arbitrary maximum. If the same evidence also suggests a related question without directly addressing it, add a secondary `variant_of` or `relates_to` edge with medium or low confidence and a clear basis. Never count those secondary edges as direct evidence.

### Confidence

- **High:** explicit question or aim, direct quote, and reliable abstract or full-text basis.
- **Medium:** clear inference from an explicitly quoted purpose, findings, title, abstract, or research gap.
- **Low:** weak inference, metadata-only basis, multiple interpretive steps, or uncertain source matching.

Metadata-only sources may produce low-confidence questions when the title or venue is sufficient. Otherwise record `no_supported_question`. Never invent a question to make a source fit.

## Canonicalization

Use a three-layer approach:

1. **Literal source question.** Preserve the source-specific wording and evidence.
2. **Normalized question frame.** Map the question into typed slots such as exposure, mechanism, outcome, population, context, time, comparison, and relation type.
3. **Canonical question.** Group source questions only when they share the same semantic relation and compatible slots.

Do not merge merely because sources share vocabulary. For example, heat and UHI are related but not equivalent; redlining and income inequality are competing determinants. When in doubt, keep two `question` nodes and connect them with `relates_to`, `refines`, `specifies`, `generalizes`, or `contrasts_with`.

Record each merge decision in `canonicalization_notes` on the source question and, when useful, in the canonical question’s extraction rationale.

## Themes

Create `theme` nodes after source questions are extracted and canonicalized. Each theme needs:

- a short noun-phrase label;
- a plain-language statement, not a question;
- member question IDs and source IDs;
- support counts and support tier;
- confidence;
- coherence basis;
- rationale.

Theme membership is not automatic containment. Assign `role: primary` to the theme that best explains where the question’s evidence belongs. Assign `role: cross_cutting` to additional themes connected through a narrower concept, shared method, or specific subpopulation. Record why the cross-cutting link matters.

Theme support is adaptive rather than fixed:

- In a small set, a single-source or single-question theme may be useful, but should be low confidence.
- In a comprehensive set, prefer two supporting questions or two distinct sources for a primary theme.
- In an exhaustive set, prefer three or more supporting questions or sources for primary themes.

Always keep weaker themes visible as exploratory. Never imply that a single-source theme represents broad agreement. `next_question` nodes may be linked to a theme through `proposed_for`, but they do not count as theme support.

## Possible next questions

Create `next_question` nodes only after source questions and canonical questions exist. Generate them by:

1. narrowing a parent question to a specific outcome, mechanism, population, geography, method, or time frame;
2. substituting one slot in a recurring question structure;
3. following an explicit research gap named in a source; or
4. proposing a question the user could pursue in a follow-up run.

Call these “possible next questions” in user-facing text. Each should record parent question/theme IDs, slot substitutions, generation basis, rationale, confidence, and launch readiness. Unless a source explicitly names the next question, it has no source support and must not be treated as evidence about the literature.

## Scoring

Score canonical questions with a transparent weighted combination. Store raw components and the weights used in the run.

| Component | Default weight | Meaning |
|---|---:|---|
| `user_alignment` | 0.30 | Connection to the confirmed core question and scope |
| `source_support` | 0.20 | Number and quality of distinct selected sources |
| `explicitness` | 0.15 | Average explicitness of supporting statements |
| `citation_attention` | 0.10 | Normalized citation attention from available providers |
| `breadth` | 0.10 | Diversity of disciplines, methods, populations, geographies, or contexts |
| `relation_density` | 0.10 | Strength and number of relations to other questions |
| `evidence_strength` | 0.05 | Access level, direct quotation, and source-match confidence |

Normalize components to the 0–1 range when possible. Record provider and timestamp for citation counts. Citation attention is one input; it is never correctness, consensus, or an evidence state.

Theme scoring should combine mean member-question score, distinct source count, relation density, breadth, and access-quality distribution. Possible next questions use a separate rubric based on user alignment, structural clarity, novelty, relation to observed gaps, and launch readiness. Do not use citation counts for possible next questions.
