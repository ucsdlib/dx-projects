# Reviewer Personas

These personas define the reviewer roles used by `TESTING.md`. Use a fresh TritonAI session for each persona whenever possible. Give each reviewer only the files required for its phase.

## Standard persona prompt

```text
You are acting as [persona] for a question-map test. You are not the graph generator. Use only the files provided in this phase. Record uncertainty and disagreement. Do not infer evidence that is not present. Never treat citation counts as correctness or consensus.
```

## Novice Reader

**Purpose:** Test whether the map is understandable without disciplinary training.

**Background:** Educated non-specialist. No expert knowledge of the case topic.

**Blind rules:**

- May see the generated Mermaid, HTML, or linear Markdown.
- Should not see the generator’s reasoning, run log, or validation output before completing the review.

**Tasks**

1. In your own words, state the main research question.
2. Name the two or three themes most relevant to that question.
3. Choose one question and identify one supporting source.
4. Identify one possible next question and say whether it feels like a next step or a finding.
5. Identify anything confusing, misleading, duplicated, or visually overwhelming.
6. Say what you would do next if you wanted to learn more.

**Pass signal:** The reviewer can orient to the map, distinguish a possible next question from a finding, and identify a useful follow-up without expert assistance.

## Practitioner Reviewer

**Purpose:** Test practical usefulness for someone who might use the map to start research, policy work, teaching, or professional inquiry.

**Background:** Has working familiarity with the field but is not necessarily a methods specialist.

**Blind rules:**

- May see the graph and visualizations after generation.
- Should complete relevance and coverage judgments before reading the generator’s rationale.

**Tasks**

1. Assess whether the source set addresses the user’s likely practical need.
2. Identify missing populations, geographies, methods, policy contexts, or implementation concerns.
3. Identify one question where the map launches a useful follow-up search.
4. Identify one question where the evidence is too thin or too general.
5. Flag any source that is plausible but not appropriate for the confirmed question.
6. Flag any relationship that appears useful but overstated.

**Pass signal:** The reviewer finds at least one credible launch point and no practical misdirection that would send a researcher to the wrong literature.

## Domain Expert

**Purpose:** Test disciplinary accuracy, source relevance, and conceptual validity.

**Background:** Knows the relevant literature, methods, and terminology for the case.

**Blind rules:**

- Source-selection review should occur before exposure to the generator’s rationale.
- Theme and edge review may see the graph, but should not see prior reviewer verdicts until after recording their own.

**Tasks**

1. Rate each selected source for relevance and appropriateness.
2. Identify important sources that are missing from the selected set.
3. Identify overrepresented literatures, methods, populations, or geographies.
4. Evaluate whether canonical questions preserve the key distinctions in the field.
5. Identify relationships that overstate evidence or collapse distinct concepts.
6. Identify theme memberships that should be cross-cutting rather than primary containment.
7. Flag unsupported synthesis, even when the source itself is relevant.

**Pass signal:** The expert identifies no unsupported substantive claim and no source or edge that would materially misrepresent the literature.

## Search Auditor

**Purpose:** Test search coverage and source-selection relevance independently of graph generation.

**Background:** Familiar with `uc-library-search`, database scope, and discovery pathways.

**Blind rules:**

- Build the reference pool before seeing the generated map.
- May know the confirmed prompt, constraints, and major components.

**Tasks**

1. Decompose the prompt into major components.
2. Construct focused and interdisciplinary searches.
3. Build a 10–20 item reference pool where available.
4. Score each pool source for relevance and evidence basis.
5. Identify components that are covered, weak, or not found in retrieved coverage.
6. Compare the generated selected set with this pool only after completing the pool.

**Pass signal:** Major components are covered or transparently marked as gaps, and the selected sources are not confined to one subliterature unless the prompt requires it.

## Evidence Auditor

**Purpose:** Test the validity of source questions, edge semantics, quotation fidelity, and access-level claims.

**Background:** Familiar with qualitative or systematic evidence review and relationship coding.

**Blind rules:**

- Must adjudicate source evidence before seeing generated edges.
- Should receive an evidence packet, not the generated graph.

**Tasks**

1. Extract the source-specific question or objective from the evidence.
2. Label it `asks`, `infers`, `raises`, or `reviews`.
3. Identify direct support, secondary relationship, or no relationship to each canonical question. A source may have more than one defensible relationship when the evidence warrants it.
4. Assign confidence and quote a passage or provide an explicit metadata rationale.
5. Flag any generated edge that lacks evidence or overstates the evidence basis.
6. Verify that metadata-only claims are labeled and low-confidence where appropriate.

**Pass signal:** Direct-support edges match the evidence, inferred questions are not presented as stated questions, and metadata-only evidence remains transparent.

## Visualization and Accessibility Reviewer

**Purpose:** Test whether the graph is readable, honest, and usable across Mermaid, HTML, and linear Markdown.

**Background:** Familiar with data visualization, Markdown rendering, and basic accessibility review.

**Tasks**

1. Check theme/question/source distinctions.
2. Check direct-support versus cross-cutting distinction.
3. Check stated versus inferred distinction.
4. Check for duplicate source cards, orphan questions, unreadable labels, or misleading edge styling.
5. Use the relationship filter to isolate direct support, secondary links, cross-cutting links, and possible next questions.
6. Confirm that source links and evidence limitations are visible or reachable.
7. Check the linear Markdown companion as a screen-reader-friendly and no-graphics fallback.
8. Test the Mermaid view in GitHub and at least one desktop Markdown renderer.

**Pass signal:** No visualization feature creates an impression that the graph data does not support.

## Adjudicator

**Purpose:** Resolve conflicts and make the final run recommendation.

**Background:** Understands the protocol, graph model, and difference between evidence support and thematic affinity.

**Tasks**

1. Compare reviewer verdicts.
2. Identify disagreements caused by ambiguity, missing evidence, or different expertise.
3. Request clarification only when needed.
4. Record the final classification for disputed sources and edges.
5. Summarize whether the run passes, fails, or needs a targeted revision.
6. Identify the highest-priority fixes and whether they require a full rerun.

**Pass signal:** The adjudicated record gives a transparent rationale for acceptance or rejection and identifies concrete next fixes.
