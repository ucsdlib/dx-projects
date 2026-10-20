# Test Cases

These cases test different disciplines, expertise frames, and edge-semantics risks. Use one case per run and save artifacts under `testing/runs/<YYYY-MM-DD>-<case-id>/`.

For every case, send the **raw user prompt** to `question-map` unchanged. If a case provides **simulated user context**, hold it back and use it only as realistic answers to the tool's clarifying questions. The **confirmed working scope** may add only the user's stated purpose; it must not import the reviewer coverage lenses. Those lenses are for reviewers to assess blind spots and gaps, not requirements embedded in the prompt.

## Case 1 — `heat-city-policy-novice`

**Raw user prompt:** “What should my city do about extreme heat and public health?”

**Simulated user context for clarification:** “I'm a novice researcher trying to prepare for a city council meeting. I want to bring evidence from recent research.”

**Confirmed working scope:** “What should my city do about extreme heat and public health? I want recent research evidence to bring to a city council meeting.”

**Researcher expertise:** Novice; city staff member or interested resident.

**Discipline:** Urban planning, public health, climate adaptation.

**Reviewer coverage lenses — not passed to the skill**

- health outcomes and healthcare use;
- vulnerable populations and equity;
- urban form, green space, and cooling;
- governance, policy, and emergency response;
- lived experience and social consequences;
- measurement or evidence limitations.

**Expected edge traps**

- The broad prompt may become an unsupported canonical question.
- Policy relevance may be presented as direct empirical support.
- Equity may be treated as a broad theme even when evidence is narrower.

**Primary review focus**

- intake refinement;
- source relevance for practical city decision-making;
- theme containment versus cross-cutting equity links.

## Case 2 — `clinical-prediction-bias-expert`

**Raw user prompt:** “How do clinical prediction models reproduce or reduce racialized and socioeconomic health disparities?”

**Simulated user context for clarification:** None. Run with the raw prompt and record any clarifying questions the tool asks.

**Confirmed working scope:** Use the raw prompt.

**Researcher expertise:** Domain expert in health data science, clinical informatics, or health equity.

**Discipline:** Medicine, computational social science, health equity, machine learning.

**Reviewer coverage lenses — not passed to the skill**

- prediction-model performance;
- bias measurement and fairness methods;
- clinical deployment and workflow;
- race, socioeconomic status, and structural inequity;
- data quality and missingness;
- interventions or governance safeguards.

**Expected edge traps**

- Measurement fairness may be linked to every empirical question by default.
- Technical model performance may be conflated with equity impact.
- Policy implications may be presented as direct empirical findings.
- A source may legitimately support both technical model performance and equity impact; do not force one arbitrary mapping.

**Primary review focus**

- technical and equity validity;
- methodological cross-cutting links;
- distinction between empirical support and conceptual relevance.

## Case 3 — `coastal-housing-adaptation-practitioner`

**Raw user prompt:** “Which coastal adaptation policies protect low-income renters without increasing displacement risk?”

**Simulated user context for clarification:** None. Run with the raw prompt and record any clarifying questions the tool asks.

**Confirmed working scope:** Use the raw prompt.

**Researcher expertise:** Practitioner in planning, housing policy, environmental consulting, or local government.

**Discipline:** Environmental policy, housing, climate adaptation, urban planning.

**Reviewer coverage lenses — not passed to the skill**

- coastal hazards and exposure;
- housing affordability and renter vulnerability;
- relocation, managed retreat, or buyouts;
- zoning, infrastructure, and insurance;
- displacement and gentrification;
- implementation and governance.

**Expected edge traps**

- Environmental adaptation may dominate housing evidence.
- Displacement may appear as a theme without direct source-question support.
- Policy options may be grouped together despite different mechanisms.

**Primary review focus**

- interdisciplinary source coverage;
- policy and displacement edge validity;
- usefulness for practitioner-led inquiry.

## Case 4 — `migration-oral-history-mixed`

**Raw user prompt:** “How do migrant communities narrate home, belonging, and displacement through oral histories?”

**Simulated user context for clarification:** None. Run with the raw prompt and record any clarifying questions the tool asks.

**Confirmed working scope:** Use the raw prompt.

**Researcher expertise:** Mixed; undergraduate or community researcher with guidance from a humanities or qualitative-methods reviewer.

**Discipline:** History, anthropology, migration studies, memory studies, community archives.

**Reviewer coverage lenses — not passed to the skill**

- oral-history methodology;
- memory, narrative, and identity;
- displacement and migration contexts;
- home and belonging;
- archives, ethics, and community participation;
- interpretation limits and positionality.

**Expected edge traps**

- Interpretive claims may be forced into empirical question frames.
- Narrative evidence may be treated as direct support for broad social outcomes.
- Community participation may be treated as method and topic without distinction.

**Primary review focus**

- preserving qualitative and interpretive meaning;
- source-question origin and quote fidelity;
- avoiding unsupported synthesis.

## Fixture cases to add after the first live suite

Create small synthetic graphs when a live run exposes a reproducible failure:

- source with explicit `asks` versus inferred `infers`;
- metadata-only source with low-confidence inferred question;
- direct `supports` edges plus defensible secondary `variant_of` or `relates_to` links;
- primary and cross-cutting theme memberships for one question;
- unsupported direct-support edge that must fail validation;
- broad user prompt retained as context rather than canonical question;
- duplicate source card that must be removed by the builder.

Each fixture should be minimal, named after the failure, and tied to one validator or builder behavior.
