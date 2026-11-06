# Search and Selection Reference

Use this reference when building or executing search strategies, screening results, deciding source breadth, curating themes and questions, or producing a search log.

## UC Library Search First

If the `uc-library-search` skill is available, use it to build the focused query plus a zoom-out ladder and component queries. Execute through Primo’s documented REST pathways in this order:

1. Use the keyed Primo Search API only if the skill directory contains `.env` with a non-empty `PRIMO_KEY`. Read [primo-search-api.md](primo-search-api.md) for activation, query, filter, pagination, and troubleshooting rules.
2. If that pathway cannot activate or authenticate, use the PNX REST API fallback. Read [primo-pnx-api.md](primo-pnx-api.md), run its keyless campus preflight probe, and use its verified parameter recipe.
3. Use a 120-second timeout in either pathway.
4. If the `uc-library-search` skill is unavailable or both Primo pathways fail, proceed to other tools and record a **documented skip — never silent.** State why UC Library Search was skipped and that books, library-science venues, and UC holdings may be underweighted.

Result counts are unreliable. Paginate by fidelity, never by count.

## Source Link Resolution

Use a DOI as the primary user-facing link when one exists because it is stable, portable, and not dependent on campus authentication. Retain the UC Library Search / Primo record link separately for library stakeholders, holdings, resolver access, and provenance review. If no DOI exists, use the library record link as the primary link.

Maintain these fields in source state:

| Field | Purpose |
|---|---|
| `primary_link` | Best general-purpose link shown to the reader. |
| `primary_link_source` | Origin and rule used: `doi`, `library_record`, `native_record`, or `metadata_search`. |
| `library_link` | UC Library Search / Primo access record, when available. |
| `library_link_type` | `pnx_record`, `permalink`, or `search_link`. |

Use this fallback order for the primary link:

1. **DOI:** normalize `https://doi.org/<DOI>` from Crossref, OpenAlex, PNX, Semantic Scholar, or another verified source.
2. **Library record:** use the UC Library Search permalink or PNX record link when no DOI exists.
3. **Native record:** use PubMed, ERIC, arXiv, OpenAlex, publisher, WorldCat, or another canonical native URL when no DOI or library record exists.
4. **Metadata search:** use a title-author search link only when no stable identifier is available, and label the access level as metadata-only.

For a PNX record, extract links in this order:

1. Read `pnx.addata.doi[0]` and normalize it to an HTTPS DOI. Prefer this as the primary link for articles and other DOI-bearing records.
2. Read `pnx.control.recordid[0]`. Use this to construct the UC Library Search / Primo record link. Keep it as the library-access link; for records without a DOI, promote it to the primary link.
3. Read `pnx.display.identifier` for ISBN or OCLC when a native DOI is absent and a book-record link is needed.
4. Use other PNX or delivery links only when they are explicit URLs, not placeholder tokens such as `$$Topenurlfull_article`.

Never fabricate a library permalink or substitute an unverified search-result URL for a known canonical identifier. If a generated PNX record link cannot be verified, retain the DOI as the primary link and mark the library link as unverified in the manifest or search log.

## Adaptive Screening

Fetch one page with `limit=20` and `sort=rank`. Classify every record as on-topic, adjacent, or noise using the full metadata described by the active Primo reference.

- At fidelity of 50% or higher, continue paging while records remain useful.
- At 25–49%, fetch one more page, then stop and refine.
- Below 25%, stop immediately and refine the query instead of dredging.
- Stop early when a full page yields nothing new.
- Log fidelity and every triggered decision.

Tier budgets are cumulative records per query and ceilings, not targets:

| Tier | Records per query |
|---|---|
| Focused | approximately 40 |
| Comprehensive | approximately 80 |
| Exhaustive | approximately 200 |

## Component Decomposition

After a high-fidelity search, run fresh API calls for each conceptual component using base query plus component synonyms. This gives each subtopic its own relevance ranking and can surface items buried in a broad query. Facet slicing by type or subject counts as decomposition.

- Focused landscape: skip unless low fidelity or concept gaps require it.
- Comprehensive deep work: use two or three components.
- Exhaustive deep work: use full decomposition plus facet slices.

## Breadth and Curation

Tier guidance:

| Tier | Typical deep-work profile |
|---|---|
| Focused | approximately eight searches, eight to ten sources, two or three tool types; quick exploratory work |
| Comprehensive | ten to fifteen searches, twelve to eighteen sources, UC Library Search plus three to five API/web tools; literature reviews and strategic work |
| Exhaustive | fifteen or more searches, eighteen or more sources, all applicable tools, citation chaining, and saved-search alerts; publication-grade or contested topics |

The tier governs the final curated set, not search effort. Stage 0 and API candidates compete for the same slots. If new finds exceed the tier limit, prune the weakest sources by relevance and confidence, with rationale, or ask once whether to upgrade the tier. A stronger find may supersede a weaker source on the same theme.

For a broad prompt, run a focused landscape first and let the user choose deep-work breadth. Prompt markers may override this. For a research-paper-scoped question, explicit full-bibliography request, or complete re-run brief, use the selected tier directly.

## Landscape Sufficiency

Use purpose-aware saturation rather than a fixed landscape query budget:

1. Concept coverage: every core concept has an on-topic source or documented absence.
2. Perspective coverage: intended empirical, theoretical, practitioner, policy, historical, or recent perspectives have a source or documented gap.
3. Theme saturation: recent pages map into known themes more than they reveal new themes.
4. Question novelty: recent sources refine existing questions more than they create a stream of new source-backed questions.
5. Candidate stability: additional high-confidence candidates strengthen known themes rather than create a competing landscape.
6. Fidelity: adaptive screening permits stopping and the query is not materially biased.
7. Purpose fit: a quick overview may stop earlier than a comprehensive survey.

If two consecutive high-fidelity pages or component searches introduce no new theme or source-backed question, treat the landscape as saturated for the current purpose. If more than about one third of a recent page supports a new theme or question, continue searching or run a targeted component query. Log the decision; saturation is not proof of complete coverage.

## Additional Tools

Use additional tools after the landscape when the selected path requires broader coverage, verification, or citation chaining. UC Library Search remains first.

1. **UC Library Search:** books, e-books, subject headings, UC holdings, and library-science venues.
2. **OpenAlex API:** broad scholarly metadata, reconstructable abstracts, citation counts, and verification.
3. **ERIC API:** education-specific scholarly and grey literature.
4. **Crossref API:** canonical DOI and publication metadata for verification.
5. **arXiv API:** preprints in CS, HCI, and computational fields.
6. **Semantic Scholar API:** citation graphs and abstracts; retry once if rate-limited, then move on.
7. **Google Scholar via browser:** citation chaining and practitioner work when browser tools are available.
8. **Open web:** practitioner reports and policy documents. Verify from the actual document, never snippets.

For comprehensive work, consider four phases: core concepts, contrasting views, different methods or source types, and gap filling. Count searches across all tools, including Stage 0.

## Source Selection

Select sources by:

1. Direct relevance to the selected theme or question.
2. Explicitness of evidence.
3. Source type, method, and perspective diversity.
4. Access level and verification basis.
5. Contribution to coverage of the selected path.
6. Confidence and credibility.
7. Value for the user’s next research step.

A strong new source may replace a weaker source on the same theme. Record pruning rationale.

## Themes and Questions

Themes are descriptive groupings of retrieved sources. They may include on-topic and adjacent evidence when adjacency is labeled. Do not treat a theme as consensus or a claim. Mark theme support as direct, inferred, or interpretive when the distinction matters.

Question origins:

| Origin | Rule |
|---|---|
| Source-backed | A source explicitly asks or clearly implies the question. |
| User-defined | The user asks the question during intake or follow-up. |
| Research-direction | The skill identifies a gap or productive next line, clearly labeled as generated rather than source-backed. |

Research directions may help the user narrow a broad theme, test a named limitation, or compare methods. Put them only in a labeled “Possible directions” section or closing offer. Never represent them as claims about what the literature asks or studies.

## Search Log

Record the full pipeline:

- Tool order and number of searches per tool.
- Whether Stage 0 ran, and in which mode: Primo Search API, PNX REST fallback, or documented skip.
- Per-query fidelity and adaptive screening or refinement decisions.
- Component decomposition and facet slices.
- Verification outcomes and metadata conflicts.
- Selected, excluded, and pruned sources with reasons.
- Access, coverage, fallback, skip, and evidence limitations.

During the experimental phase, err toward completeness. Include screened-record inventory, per-page classifications, and candidate-level decisions in the manifest or search log. Optimize verbosity later.

## Verification

Always search and access original sources. Read full text when available and abstracts when necessary. Never rely on memory.

- Note access level: full text, abstract only, publisher description and table of contents, or metadata only.
- For Primo-sourced articles, use `addata.abstract` for screening and first-pass verification, but confirm citation metadata through OpenAlex or Crossref before annotation.
- For Primo-sourced books, PNX publisher description and table of contents support description-level annotation. Label the access level “Publisher description and table of contents reviewed (via Primo record),” cap confidence at MEDIUM, and state that the description is promotional copy and chapter-level quality is unassessed.
- Book verification ladder, stopping at first success: PNX fields; Google Books API; WorldCat or library catalog record; chapter-level Crossref records; human retrieval via campus library access; if all fail, annotate at metadata level, mark “Metadata only,” assign LOW confidence, and make no content claims.
- Read complete articles when URLs are available: use the collaborative browser tools for remote documents and direct file tools for local files. This harness has no general `web_search` or `web_fetch` tools; use available browser or API pathways for web-sourced content.
