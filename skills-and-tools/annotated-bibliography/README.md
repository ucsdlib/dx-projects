# annotated-bibliography

Research skill for the TritonAI harness (Codex-based) that creates comprehensive, faithful annotated bibliographies — representing what sources actually claim and classifying connections as direct evidence, reasonable inference, or interpretive connection.

## What It Is and How It Works

The skill guides an agent through a staged research pipeline that begins with UC Library Search (executed programmatically via the documented Primo PNX REST API, when the companion `uc-library-search` skill and API mounts are available), then widens to scholarly APIs in a fixed reliability order — OpenAlex, ERIC, Crossref, arXiv, Semantic Scholar — and finally to open-web retrieval for practitioner and policy sources. Screening is adaptive: each query's results are classified by fidelity (on-topic, adjacent, noise), and paging continues, stops, or triggers query refinement based on that fidelity rather than raw result counts. After a high-fidelity search, the question is decomposed into conceptual components (authorship, workflow, policy, and so on), each getting its own ranked query so sources buried deep in broad results surface. Every candidate is verified against citation registries before annotation; books follow a verification ladder that can stop at the Primo record's own description, table of contents, or abstract.

The output layer is built around faithfulness: annotations stay close to what each source explicitly states, every connection to the research question is classified as direct evidence, reasonable inference, or interpretive connection, and confidence ratings drop whenever access is limited or inference is required. A breadth-tier dialog (Focused, Comprehensive, Exhaustive) governs both search effort and the *final* source count — candidates compete for slots, and pruning decisions are documented rather than silent. During the run, the human's role is deliberately narrow — choose the breadth tier, optionally refine query terms, and retrieve inaccessible items — and all bulk screening is the agent's job. After the run, the roles reverse: every bibliography must close with a "Human Next Steps" section (priority reading list, verification targets, open questions, targeted follow-up searches, and reading-and-verification guidance) that frames the deliverable as a springboard for human-led reading, verification, and interpretation, grounded in information-literacy practice — the bibliography orients; the human investigates.

## Origins

- **Author**: Doug Worsham, Digital Experience Manager, UC San Diego Library; developed with AI assistance.
- **First version**: 2026-02-12 (package metadata). No standalone creation record exists for this skill.
- **Motivation**: counter the "helpful but unfaithful" failure mode in which AI bibliographies distort or exaggerate sources to fit a hypothesis. Shares its three-level evidence classification with the companion skill `claim-evaluation-skill`.
- **Domain signals**: worked examples reference design and UX research (e.g., Cross 2004; Wiltschnig et al., 2013), consistent with the author's digital experience role at UC San Diego Library.

## Development History

- **2026-02-12** — Initial version, distributed as a Claude-style `.skill` ZIP archive (`annotated-bibliography.skill`).
- **2026-09-15** — Brought into `dx-tools` (commit `128176c`) as a plain skill directory; the `.skill` ZIP was removed and this directory became the source of truth.
- **2026-09-15** — Adapted for the TritonAI/Codex harness: the `web_fetch` instruction was replaced with the collaborative browser (`preview_navigate` / `preview_snapshot` / `preview_evaluate`) and `exec_command` guidance for reading sources.
- **2026-09-26** — Major pipeline update: Stage 0 executes UC Library Search via the documented Primo PNX REST API (see `references/primo-api.md`); adaptive fidelity-based screening; component decomposition; mode-aware breadth dialog; curation rule binding the final set to the tier; book verification ladder; documented-skip rule.
- **2026-09-26** — Human-in-the-loop closing added: a required "Human Next Steps" section (priority reading list, verification targets, open questions, follow-up searches, reading guidance) reframes the bibliography as a springboard for human-led research rather than a terminal deliverable, operationalizing information-literacy principles.

## Testing and Development

Three controlled runs against one research question — *"What are current best practices for developing ethical AI ways of working for creative teams in higher education?"* — each exercising a successive version of the pipeline. Full run artifacts and comparison memos live in the development workspace (`dx-strategy/dx-ai-strategy/`).

| Version | Changes Made | Demonstrated Strengths | Weaknesses / Gaps |
|---|---|---|---|
| **v1** — original API-first pipeline (initial release; test run 2026-09-25) | 14 searches across OpenAlex, ERIC, Crossref, and open web. No UC Library Search (assumed un-extractable). 17 sources. | Reproducible programmatic searching; honest gap reporting; found the core creative-professional and design-education evidence; faithful annotation discipline held throughout. | Zero books; library-science venues underweighted; the creative-teams-in-higher-ed intersection remained thin because formats and venues the article APIs underweight were never searched. |
| **v2** — Stage 0 added (2026-09-26) | UC Library Search executed via the Primo `pnxs` API; 4 zoom-out ladder searches; +9 sources (26 accumulated). | Proved the campus discovery layer is harvestable; surfaced a Routledge book, two IFLA Journal studies, a JMLA editorial, and the corpus's strongest experimental source (Jang 2026); closed the library-context gap. | Fixed `limit=20` missed sources buried deeper; date filter silently lost in API translation (2010/2018 records leaked in); book verification initially misread as impossible (later shown to be a screening artifact — PNX enrichment fields were unread); final set ballooned to 26, eight above the Comprehensive tier. |
| **v3** — updated skill (2026-09-26) | Adaptive fidelity paging; component decomposition (authorship, workflow, library); working bracket-syntax date filter; curation rule; mode-aware tier selection. 11 searches, 220 records screened, 18 curated sources (10 new). | Caught a 0%-fidelity query and auto-refined (initial "artificial intelligence" query → 11,435 irrelevant results → narrowed and recovered); component searches surfaced 10 new sources incl. co-design collectives, human-AI collaboration studies, and library makerspaces; zero out-of-range date records; tier-consistent output with documented pruning rationale. | Abstract-only access persists across all sources; one article (JILA) required PNX + DOAJ verification when its DOI failed in Crossref/OpenAlex; curation genuinely drops useful policy anchors (UNESCO, EDUCAUSE, UC Principles) that a user might want; result counts remain unpredictable. |

**Recommended next test:** a forward test against a fresh research question, outside the comparison context, to confirm the adaptive behaviors (refinement, decomposition, curation) fire without the controlled-run framing.

## What We've Learned

**1. The campus discovery layer is programmatically harvestable.** The v1 assumption that UC Library Search was JavaScript-only and un-extractable was wrong. The Primo PNX REST API is documented by Ex Libris, and the campus frontend's keyless mount accepts the same queries. This reframed Stage 0 from "generate links for a human" to "extract and screen directly."

**2. Screen by fidelity, never by count.** Result totals varied from 222 to 115,417 depending on query structure, and a one-word change ("artificial intelligence" → "generative artificial intelligence") cut one query from 11,435 to 2,198. Counts predict nothing about relevance; only per-page classification of records does. The adaptive protocol (≥50% keep paging; 25–50% one more page then refine; <25% stop and refine) converted a dead query into a course correction in the v3 run.

**3. Filter translation fails silently.** The UI's date-filter deep-link format returns zero results via the API without erroring. The documented bracket syntax (`facet_searchcreationdate,exact,[YYYY TO YYYY]`) works. Any filter that can't be translated must be applied at screening time and logged — otherwise coverage quietly degrades.

**4. Read the full PNX record.** Books carry publisher descriptions, tables of contents, and often full abstracts in PNX enrichment fields. A screening script that reads only title/creator/year discards the most valuable verification data and produces false "books can't be verified" conclusions.

**5. Decomposing the question is the highest-yield search technique.** Component queries ("search within" by concept) give each sub-topic its own relevance ranking. In the v3 run, this surfaced ten sources invisible to the zoom-out ladder — including the sources closest to the actual research question. Facet slicing counts as decomposition too.

**6. Curation must be explicit, or source sets balloon.** Without a rule binding the final set to the breadth tier, pipelines accumulate: v2 reached 26 sources against an 18-source ceiling. Pruning by relevance and confidence — with rationale documented — produces a defensible working set, at the acknowledged cost of dropping sources some users will want.

**7. The human's role is narrow by design.** Tier choice, optional query input, and end-of-run retrieval of inaccessible items. Bulk screening is the agent's job; asking a human to review result lists forfeits the core value of AI assistance.

**8. Access is the persistent ceiling.** All three runs verified sources at abstract level. The single highest-value investment for bibliography quality is not more searching — it is full-text retrieval paths for the six or so highest-value sources each run identifies.

## Status

**Experimental — undergoing active testing.** The current version is installed in the harness and has been exercised through three controlled runs against a single research question. It is **not sufficiently vetted for use beyond testing and exploration**: no forward test on an independent question has been run, all source verification to date is abstract-level, and the companion `uc-library-search` update is still pending. See Testing and Development above.

## Creation Note

*Draft — in progress, shared for collaborative feedback and testing.* This skill's September 2026 pipeline update — including the `SKILL.md` revision, the Primo API reference, the three test runs and comparison artifacts, and this README — was developed iteratively with AI assistance across multiple TritonAI Harness sessions (most recently GLM, api-glm-5.3), where AI executed the literature searches, drafted the skill and documentation changes, and ran the controlled tests, directed throughout by Doug Worsham (Digital Experience Manager, UC San Diego Library), who supplied domain expertise, corrected errors, and made the design decisions. The work is experimental and has not been approved for production use. Doug Worsham is responsible for the work in its current state and is sharing it for testing and exploration.
