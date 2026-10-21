# Practitioner Review — Extreme Heat and City Policy for a Novice Stakeholder

**Reviewer role:** Local government / city planning practitioner  
**Review date:** 2026-10-09  
**Inputs reviewed:** `00-case.md`, `question_map.json`, `visualizations/question-map.md`, and `visualizations/question-map-force.html`

## Overall Judgment

**Verdict: conditional-pass.**

The map is a useful orientation tool for a novice city stakeholder. It covers the case’s six required domains, separates health outcomes from vulnerability, urban cooling, governance, lived experience, and evidence limits, and clearly identifies 20 sources. The linear reading view is especially strong: it explains that themes are question clusters rather than evidence-state classifications, that source questions are inferred from metadata, and that next questions are not source-backed findings. The force-directed HTML view adds useful landscape, evidence-anchor, and full-graph views, plus relationship filtering and search.

However, the map does not yet provide a sufficient bridge from scholarly orientation to city decision-making. It identifies relevant questions and sources but omits most practitioner-facing components: implementation, financing, staffing, operations, interagency governance, procurement, maintenance, legal authority, and local political feasibility. A novice could use it to understand the research landscape, but not to plan a heat program or know what a city must do next.

## Practical Orientation

**Strengths**

- The six themes align closely with the prompt and case requirements, making the broad topic easier to navigate.
- Seven canonical questions provide enough focus without forcing the prompt into one unsupported “what should the city do” question.
- The equity component is treated as both measurement and access, rather than as a vague cross-cutting slogan.
- The map keeps urban greening, heat-health governance, warning systems, lived experience, and effectiveness evaluation distinct. This helps avoid the common practitioner error of assuming that a policy, plan, or green infrastructure investment automatically produces health benefits.
- The “not found” section is valuable: it explicitly notes that city-specific causal evaluations and measured local cooling-center uptake were absent from retrieved coverage.
- Limitations are candid and highly relevant to a novice: all support is metadata-derived, the pool is weighted toward the United States, Europe, and Australia, and the map does not recommend a specific policy.

**Weaknesses**

- The map is oriented toward scholarly question discovery, not local implementation. It does not tell a city stakeholder who owns the work, what sequence of decisions is involved, or how evidence translates into a heat plan.
- It lacks local context-setting questions: current heat burden, demographics, healthcare and EMS data, cooling-site inventory, tree canopy and shade access, building stock, utility capacity, transportation barriers, and neighborhood-level vulnerability.
- It lacks explicit questions about municipal authority, budget cycles, staffing, operations, maintenance, procurement, mutual aid, communications, and accountability.
- A novice may misread “high confidence” in the theme view as high certainty about policy effectiveness. The caveats say otherwise, but the presentation does not consistently distinguish confidence in map coverage from confidence in intervention effects.
- The 20-source pool is appropriately compact and mostly relevant, but it is heavily academic. It contains only one implementation-oriented international report and no local government guidance, municipal plan corpora, budget or staffing examples, regulatory materials, community-engagement literature, or city case-study implementation materials.

## Source Appropriateness

The sources are generally appropriate for orienting a novice to the evidence landscape. The pool includes emergency-department studies, mortality analyses, vulnerability-mapping work, green-infrastructure health-impact assessment, heat-plan reviews, warning-system effectiveness reviews, lived-experience case studies, and WHO/WMO guidance. The inclusion of older foundational work is acceptable, but the map should make clearer that implementation norms, climate risk, and local governance practice have changed since several sources were published.

The map’s strongest evidence-hygiene feature is its repeated disclosure that source questions and support edges derive from titles and bibliographic metadata rather than abstracts or full text. This appropriately limits what can be concluded. Still, the metadata-only basis is not always operationalized in the practitioner interface. The visual language sometimes suggests “supported,” “direct evidence,” and “high confidence” more strongly than the actual metadata review warrants.

For a practitioner audience, additional source types would be useful:

- city or county heat plans and after-action reports;
- local public-health, emergency-management, parks, transportation, housing, and utility guidance;
- budget documents, staffing models, and procurement examples;
- legal or policy scans for cooling-center operations, tree planting, building standards, labor protections, and utility shutoff protections;
- community-organization materials and public engagement records;
- data inventories showing what the city can currently measure.

## Actionable Follow-Up

The five possible next questions are well chosen and mostly launchable for further inquiry. They correctly move from general scholarly questions toward city-scale causal outcomes, equity-targeted greening, cooling-center uptake, social vulnerability measurement, and local adaptation of broad mortality estimates. Each is labeled as generated rather than source-backed, which prevents overstating the evidence.

From a practitioner perspective, however, they are still research questions rather than decision packages. To become launchable for a city stakeholder, each should have:

- the decision it could inform;
- likely municipal owner and partners;
- local data sources or acquisition steps;
- feasible scope and timeframe;
- equity and community-engagement considerations;
- cost, staffing, or operational implications;
- a clear deliverable, such as a heat-vulnerability index, cooling-center protocol, pilot evaluation, or heat-plan revision.

High-priority missing follow-up questions include:

1. What is the city’s current heat-health burden, by neighborhood, age, housing status, language, disability, income, and healthcare use?
2. Which departments have authority, budget, staffing, and operational responsibility for heat emergency response, cooling services, outreach, tree and shade programs, building policy, and communications?
3. How are cooling centers staffed, funded, transported to, advertised, evaluated, and connected to vulnerable residents who may not use them?
4. What are the capital, maintenance, and equity tradeoffs of tree canopy, shade, cool surfaces, resilient hubs, and building-level cooling?
5. Which proposed actions are legally, politically, fiscally, and operationally feasible under current municipal authority?
6. How should local implementation be monitored and evaluated after the next heat season?

## Visualization and Usability

The linear markdown view is the best practitioner entry point because it is readable, ordered, and explicit about support and limitations. The force-directed HTML view offers useful exploration through landscape, evidence, and full-graph modes, relationship filters, search, tooltips, and a details panel. Its distinction between research questions, sources, source questions, and next questions is conceptually helpful.

Remaining usability concerns:

- The HTML title is generic and does not immediately signal the topic or intended audience.
- Force-directed layouts can be hard for non-technical users to interpret or use under time pressure.
- Hover/click interaction is not equivalent to a simple readable practitioner checklist.
- The external D3 and sibling visualization-data dependencies may create portability or offline-access issues.
- Interactive graph elements should receive an accessibility review, especially keyboard navigation, equivalent text alternatives, and screen-reader descriptions.

## Highest-Priority Fixes

1. **Add a practitioner decision layer.** Keep the current scholarly map, but add a separate city-action view organized by implementation, financing, staffing, operations, local authority, community engagement, and evaluation.
2. **Create local evidence and data-gap questions.** Ask what the city can currently measure, who owns each dataset, what privacy or interoperability constraints apply, and what baseline indicators should be collected before the next heat season.
3. **Turn next questions into launch kits.** For each possible next question, provide the city decision, owner, data source, likely partners, deliverable, timeframe, and evidence limits.
4. **Make metadata-only uncertainty more visible in practitioner-facing views.** Replace or qualify “high confidence” with language such as “well covered by metadata-derived source questions; not a conclusion about effectiveness.”
5. **Expand the source pool for local feasibility.** Add municipal plans, guidance, budget or staffing examples, regulatory scans, and implementation case studies, while keeping them visually distinct from peer-reviewed causal evidence.

## Final Status

**Conditional-pass.** The map successfully supports novice orientation and avoids several serious evidence overstatements, but it is not yet sufficient as a practitioner-facing starting point for city heat-policy planning.
