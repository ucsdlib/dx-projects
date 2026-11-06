# Aspect Discovery — Stage 4 sub-step

Aspects, frameworks, and lenses are how the literature actually slices a question. They are **discovered, not assumed**. An aspect is a decomposition of the *question* — finer-grained and more structural than a concept — and it must be validated against records.

## Four sub-steps

1. **Decompose (top-down, co-produced).** Work with the user to split the question into candidate sub-questions. Default probe set for most questions: *exposure/conditions, impacts, interventions, populations, governance/policy, measurement/data, economics, equity*. Do not force all of these — keep only ones the question genuinely suggests.
2. **Emerge (bottom-up).** Let the corpus propose framings the user never named. Signals to look for:
   - **Shared vocabulary** — recurring terms/phrases across titles and abstracts (e.g., an environmental-justice vocabulary in heat research).
   - **Subject-heading families** — LCSH/MeSH clusters in record metadata.
   - **Concept co-occurrence** — which concepts travel together across records.
   - **Discipline vocabulary** — the same phenomenon named differently by field (e.g., "heat island" in climatology vs. "thermal comfort" in planning).
   - **Citation anchors** — records cited across many others (only if citation data is available).
3. **Validate.** Every candidate aspect must anchor to records: collect `record_ids` and assign `coverage.evidence_state`. An aspect with **no support is a finding, not an error** — report it with `evidence_state: not_found` and `origin` reflecting how it arose, plus a suggested next query to test it.
4. **Assign provenance.** Set `origin` (`user_defined | literature_emergent | mixed`), `kind` (`component | framework | lens | sub_question`), optional `parent_id`/`sub_aspects` for layering, `vocabulary` (terms + disciplines), `lenses`, and `confidence`.

## Coverage states (per aspect)

| State | Meaning |
|---|---|
| `well_understood` | Multiple Tier-2-read records converge; few voiced challenges |
| `contested` | Read records disagree or findings are context-dependent |
| `emerging` | Recent, growing, or sparse but promising engagement |
| `weak` | Some coverage, but thin or low confidence |
| `not_found` | No supporting records in retrieved coverage — phrase it as such |

Assignment rules: `well_understood` and `contested` are **Tier-2** states — they require read full text (top-N = 10 per major zone). `emerging`/`weak`/`not_found` may be assigned from metadata/abstracts (Tier 1) with confidence labels.

## Reporting on the map

- Each aspect becomes a row in the `aspect_coverage` module view (aspect × evidence state × record count × anchors).
- Layer relations (question → component → sub-aspect) appear as nested/grouped rows or a Mermaid cluster, per the module recipe.
- Vocabulary notes surface in a footnote or inline: "this framing uses planning-school vocabulary (thermal comfort) more than public-health vocabulary."

## Pitfalls

- Don't silently rename the user's concepts into aspect labels — keep `aliases` on concepts and use aspects for *question decomposition*, not synonym groups.
- Don't treat a `not_found` aspect as proof the topic is unstudied — it is a statement about *retrieved coverage*; always offer a test query (and record it as a gap entry).
- Don't flatten contested clusters into consensus — Tier-2 claims only, and surface the tension in `takeaways` with both sides anchored.
- Don't create an aspect for every concept — aspects are larger-grain decompositions of the question; concepts are entities within them.
