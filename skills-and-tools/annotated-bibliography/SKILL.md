---
name: annotated-bibliography
description: Create comprehensive, research-grade annotated bibliographies that accurately represent sources and distinguish between direct evidence, reasonable inference, and interpretive connection. Use when user requests "annotated bibliography on [topic]", "comprehensive research on [question]", "sources for and against [claim]", literature reviews, or "what does research say about [topic]".
---

This skill guides creation of faithful, comprehensive annotated bibliographies that prioritize accurate source representation over making arguments work. The user provides a research question or topic requiring multiple sources with critical analysis.

## Core Principles

### 1. Faithful Over Helpful
- Represent what sources actually claim, not what would support hypotheses
- Use direct quotes extensively
- Flag when making inferences beyond source text
- Report null findings or absence of evidence honestly
- **NEVER manufacture controversy** - report honestly what literature shows

### 2. Comprehensive Search Strategy

**Stage 0: UC Library Search first.**
- If the `uc-library-search` skill is available in the session, begin by using it to build UC Library Search strategies for the research question (typically the focused query plus a zoom-out ladder) using that skill's `scripts/build_url.py`.
- **Execute via the documented Primo PNX REST API.** Read `references/primo-api.md` before first use each session for the verified endpoints, parameter recipe, filter translation, PNX metadata inventory, and troubleshooting. Use a 120-second timeout; run the preflight probe before trusting the keyless campus mount. Result counts are unreliable — paginate by fidelity, never by count.
- **Adaptive screening:** fetch one page (`limit=20`, `sort=rank`), classify every record (on-topic / adjacent / noise) using the full PNX metadata, and continue paging only while fidelity (the on-topic plus adjacent share) stays at or above 50%. At 25–50%, fetch one more page, then stop and refine. Below 25%, stop immediately and refine the query instead of dredging. Tier budgets (cumulative records per query — ceilings, not targets): Focused ~40, Comprehensive ~80, Exhaustive ~200. Stop early when a full page yields nothing new. Log fidelity per query.
- **Component decomposition ("search within"):** after a high-fidelity search, run fresh API calls for each conceptual component of the research question (base query AND component synonyms), giving each sub-topic its own relevance ranking and surfacing on-topic items buried deep in a broad query's ranking. Facet slicing (type, subject) counts as decomposition too. Focused: skip. Comprehensive: 2–3 components. Exhaustive: full decomposition plus facet slices.
- **Division of labor (during the run):** the agent does the bulk screening. During the run, the human contributes: (a) the breadth-tier choice, (b) optional domain input on query terms when offered, (c) retrieval of specific items the agent cannot access (bot-blocked pages, paywalled or campus-SSO content). After the run, the human leads the deep dive — see "Human Next Steps."
- **Verification still applies:** articles found via UC Library Search must have citation metadata confirmed via OpenAlex/Crossref before annotation; books may be annotated at description/TOC level under the rules in "Verify Before Annotating."
- **If the `uc-library-search` skill is unavailable or both API mounts fail:** proceed directly to the API-based tools below and record a **documented skip — never silent.** The search log must state (a) that Stage 0 was skipped, (b) why, and (c) the expected coverage consequence (books, library-science venues, and UC holdings underweighted). Repeat the coverage gap in the opening summary's pipeline-transparency line.

Search across MULTIPLE perspectives in phases:
- **Phase 1 (3-5 searches)**: Core concepts directly
- **Phase 2 (2-4 searches)**: Contrasting views - "critique of [X]", "[X] limitations", alternative frameworks
- **Phase 3 (2-3 searches)**: Different methods - empirical studies, reviews, theoretical papers, practitioner sources
- **Phase 4 (1-3 searches)**: Fill gaps - historical sources, recent developments, related domains

**Total: 8-15 searches for comprehensive work, counted across all tools including Stage 0**

**Reliable Search Tools** (use in pipeline order):
1. **UC Library Search (via `uc-library-search` skill)**: Books, e-books, subject-heading discovery, and UC-specific holdings. Strength: surfaces formats, subject vocabulary, and library-science venues that article APIs underweight. Execute via the Primo PNX REST API (see `references/primo-api.md`).
2. **OpenAlex API**: Broad scholarly index with machine-readable metadata, reconstructable abstracts, and citation counts. First choice for programmatic discovery and source verification.
3. **ERIC API**: Education-specific peer-reviewed and grey literature. First choice when the topic touches teaching, learning, or educational policy.
4. **Crossref API**: Canonical DOI and publication metadata. Use for citation verification even when a source is found elsewhere.
5. **arXiv API**: Preprints in CS, HCI, and computational fields. Use for emerging topics where the formal literature lags.
6. **Semantic Scholar API**: Citation graphs and abstracts; useful for citation chaining. Caveat: aggressive rate limits - retry once, then move on.
7. **Google Scholar (via browser, if available)**: Citation chaining ("Cited by") and discovery of practitioner work. Caveat: no API; bot-protected without browser tools.
8. **Open web (e.g., DuckDuckGo HTML, publisher and organizational sites)**: Practitioner reports and policy documents (EDUCAUSE, UNESCO, ARL, Ithaka S+R, institutional guidance). Always verify by retrieving the actual document, never from search-result snippets.

### 3. Verify Before Annotating
- Always search and access original sources
- Read full text when available, abstracts when necessary
- Never rely on memory about sources
- Note access level (full text / abstract only / publisher description and TOC / metadata only)
- **Primo-sourced articles:** the PNX `addata.abstract` is a full abstract, not a snippet — use it for screening and first-pass verification, but confirm citation metadata (DOI, venue, year, authors) via OpenAlex or Crossref before annotating.
- **Primo-sourced books:** the PNX publisher description (`display.description`) and table of contents (`display.contents`) support a description-level annotation. Label the access level "Publisher description and table of contents reviewed (via Primo record)," cap confidence at MEDIUM, and state that the description is promotional copy and chapter-level quality is unassessed. Never present a publisher description's evaluative claims as independent evidence of effectiveness.
- **Book verification ladder (stop at first success):** (1) PNX fields (`addata.abstract`, `display.description`, `display.contents`); (2) Google Books API; (3) WorldCat or library catalog record; (4) chapter-level Crossref records; (5) human retrieval via campus library access; (6) if all fail, annotate at metadata level, mark "Metadata only," assign LOW confidence, and make no content claims.
- Read complete articles when URLs are provided: open them in the collaborative browser
  (`preview_navigate` -> `preview_snapshot` / `preview_evaluate` to extract text); read
  local files directly with `exec_command`. This harness has no `web_search`/`web_fetch`
  tools - run searches through the browser (e.g., Google Scholar, publisher sites,
  library databases) for any web-sourced content.

## Search Breadth

Before searching, ask the user ONE question offering three tiers:
- **Focused:** ~8 searches, 8-10 sources, 2-3 tool types. For quick, exploratory needs.
- **Comprehensive (default/recommended):** 10-15 searches, 12-18 sources, UC Library Search plus 3-5 API/web tools. For literature reviews and strategic work.
- **Exhaustive:** 15+ searches, 18+ sources, all applicable tools, citation chaining, and saved-search alerts. For publication-grade or contested topics.

**Mode-aware asking:** if the request context determines the tier (a controlled comparison, a re-run, or an explicit "be thorough"), state the chosen tier and proceed without asking. Otherwise, ask once, at the beginning only; if the user declines to choose, does not respond, or says "you decide," use **Comprehensive** without asking again. Record the chosen tier and its basis (user-selected / default-applied / context-determined) in the opening summary.

**Curation rule:** the tier governs the FINAL annotated set, not the search effort. Stage 0 and API candidates compete for the same slots. When new finds exceed the tier limit, prune the weakest sources (the default) with the justification recorded in the closing synthesis, or ask the user once whether to upgrade the tier. Prune by relevance and confidence, not discovery order — a stronger find supersedes a weaker source on the same theme.

**Adaptive refinement (tier-dependent):** the breadth question is asked once, but mid-run check-ins are permitted when search signals warrant:
- High count, low fidelity → narrow (add an AND concept, phrase-quote, field search, or filter facet)
- Very few relevant results across the whole ladder → zoom out or expand synonyms
- Unexpected high-value cluster → flag it and consider a dedicated component search
- **Focused:** adjust autonomously and log every decision. **Comprehensive:** up to two autonomous adjustments, logged with rationale; one mid-run question only if scope is genuinely ambiguous. **Exhaustive:** present the preliminary landscape and ask which branches to pursue before the deep pass.

## Search Log

Record the full pipeline:
- Which tools were used, in what order
- How many searches each tool contributed
- Whether Stage 0 ran, and in which execution mode (Primo API extraction vs. documented skip with reason)
- Per-query fidelity estimates and any adaptive screening or refinement decisions they triggered
- Any fallbacks or skips, with reasons and coverage consequences

## Understanding the Research Question

Before searching, clarify (if unclear):
1. Specific research question or thesis?
2. Discipline/domain?
3. Specific perspectives needed?
4. Time period for sources?
5. Peer-reviewed only, or include practitioner sources?
6. Approximate number of sources needed?

## Annotation Structure

For each source:

```markdown
# [lowercase descriptive title of key finding]

---
**Citation:** [Full APA 7th edition with DOI/URL]
**Access Level:** [Full text reviewed / Abstract only / Publisher description and TOC reviewed (via Primo record) / Metadata only]
**Source Type:** [Empirical study / Review / Theoretical / Practitioner / Book]
---

## What the Source Claims

[2-4 paragraphs staying close to source's explicit statements. Use direct quotes for key claims.]

**Key quotes:**
- "[Direct quote 1]"
- "[Direct quote 2]"

## Methodology/Evidence

**Study Design:** [Type]
**Evidence Base:** [Sample, data sources, methods, limitations]
**Credibility:** [Peer-reviewed? Citations? Author expertise? Limitations acknowledged?]

## Relevance to Research Question

**Research Question:** [Restate for clarity]

### Connection Classification:

**1. Direct Evidence** (if applicable):
Source explicitly discusses [topic] and demonstrates [finding] through [evidence].
**Quote:** "[supporting quote]"

**2. Reasonable Inference** (if applicable):
Source demonstrates [related finding], suggesting [connection] because [reasoning].

**3. Interpretive Connection** (if applicable):
Source addresses [related domain], which could be relevant because [reasoning]. However, this requires [describe leap].

## Confidence Level: [HIGH / MEDIUM / LOW]

**Justification:** [Explain rating based on directness, rigor, generalizability, inference required]

---
```

## Organization

**Opening Summary:**
- Research question
- Search breadth tier (Focused / Comprehensive / Exhaustive)
- Search strategy
- One "Search pipeline transparency" line naming the tools used and any notable coverage gaps (e.g., "books underweighted because UC Library Search screening was declined")
- Scope (time period, domains, types)
- Key finding (consensus, debate, or gaps?)
- Structure of sections

**Section Headers:**
- Core Empirical Evidence
- Theoretical Frameworks
- Contrasting Perspectives / Critiques
- Methodological Studies
- Applied / Practitioner Work
- Historical / Foundational Sources

**Closing Synthesis:**
- Consensus areas
- Contested issues
- Methodological notes
- Gaps in literature
- Unexpected findings
- Recommendations for user

**Human Next Steps (required):** every bibliography closes with the "Human Next Steps" section defined below — the deliverable is a springboard for human-led research.

## Human Next Steps

The bibliography orients; the human investigates. This closing section operationalizes information literacy (research as inquiry, scholarship as conversation, authority as contextual): the human selects, reads, verifies, and interprets; the agent has screened, oriented, and flagged.

**Required components:**

1. **Priority reading list (3–6 sources):** the sources that most reward full-text human reading, each with a one-line reason (what to look for, why it matters to the question). Prioritize sources whose claims carry the most weight in the synthesis, sources accessed at Abstract only / Publisher description and TOC / Metadata only, and items the human must retrieve through authenticated access.
2. **Verification targets:** specific claims, statistics, or quotes where abstract-level access or inference does heavy lifting. Phrase each as a question the human can answer by reading (e.g., "Does the full text report effect sizes for the creativity decline?").
3. **Open questions for the researcher (2–4):** compelling questions the search surfaced but available evidence could not answer. Frame as research directions arising from the analysis, not as deficiencies.
4. **Targeted follow-up searches (2–3):** concrete queries, databases, or citation-chaining leads tied to documented gaps — written so the human or a future agent run could execute them directly.
5. **Reading-and-verification guidance:** state plainly that the human should select the sources that matter most to their question, obtain and read the full texts, verify key claims against them, and reach their own conclusions. Agent annotations are screening and orientation, not substitutes for engaging the sources. Where a source disagrees with its annotation, the source wins.

**Tone:** practical and specific, never generic. Every item must trace to a named source, a logged gap, or a contested finding in the run above. If the evidence base is weak, say what reading would strengthen it and why.

## Confidence Level Guidelines

**HIGH**: Source directly addresses research question through rigorous empirical methods. No interpretive leap required.

**MEDIUM**: Source provides solid evidence but requires modest inference from behavioral observations to cognitive processes, or addresses closely related domain.

**LOW**: Source requires substantial interpretive work across historical periods, disciplines, or levels of analysis. Appropriate as historical context but not empirical evidence.

## Guardrails Against "Helpful but Unfaithful"

Before finalizing any annotation, verify:
- ❌ Did I add interpretation not in the source? → Move to "Interpretive Connection"
- ❌ Did I smooth over contradictions source mentions? → Include them
- ❌ Am I using different terminology than source? → Justify or acknowledge shift
- ❌ Did I quote accurately and in context? → Fix immediately
- ❌ Am I making source "fit" user's hypothesis? → Describe what source actually says
- ❌ Did I inflate confidence to be more helpful? → Lower and explain honestly

## When Evidence is Weak/Absent

If literature reveals limited evidence:
- ✅ Say so clearly
- ✅ Don't force tangential sources to "count"
- ✅ Acknowledge gaps explicitly
- ✅ Note what kind of evidence is missing

## Common Patterns

**No contrasting evidence found:**
"Literature search found strong support from multiple sources. No direct challenges found, though this may reflect search limitations, research consensus, or lack of scholarly attention to alternatives."

**Popular claims vs. academic evidence:**
Include both practitioner advocacy AND academic critiques. Note divergence between practitioner literature and empirical research.

**Can't access full text:**
- Mark: "Access Level: Abstract only"
- Lower confidence rating
- Note: "Full text access would strengthen evaluation"
- Focus on what abstract explicitly states

## Output Formats

**Default**: Full annotations (comprehensive literature reviews, thesis work)
**Condensed**: Shorter format for quick overviews (exploratory research)
**Comparative Matrix**: Table format for comparing methodologies or synthesizing evidence

Ask user preference if unclear which format suits their needs.

## Final Reminders

- Your job is accuracy, not advocacy
- Absence of evidence ≠ evidence of absence
- Quote liberally as evidence for faithful representation
- Access level matters - note full text vs. abstract
- When in doubt, rate confidence lower
- Best bibliography might contradict user's hypothesis - that's valuable
- Gaps and contradictions are findings - report honestly
- The bibliography is the beginning of the human's research, not the end - always close with Human Next Steps

**The user benefits most from a bibliography they can trust completely, even if it's less convenient than one confirming their priors.**
