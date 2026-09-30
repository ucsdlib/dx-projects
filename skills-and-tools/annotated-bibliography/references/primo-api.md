# Primo PNX REST API Reference (Stage 0 Execution)

All endpoints, parameters, and filter syntaxes below were verified live against
`search-library.ucsd.edu` (September 2026). Read this file before first Stage 0
execution in a session; use it for troubleshooting whenever extraction behaves
unexpectedly.

## Documented API

The Primo PNX REST API is documented on the Ex Libris Developer Network:
`https://developers.exlibrisgroup.com/primo/apis/webservices/rest/pnxs/`
(`GET /v1/pnxs`, Brief Search API, JSON output).

## Mounts

1. **Hosted mount (preferred when an API key is available):**
   `https://api-na.hosted.exlibrisgroup.com/primo/v1/pnxs?...&apikey=KEY`.
   API keys are free via the Ex Libris Developer Network. This is the supported,
   stable path.
2. **Campus frontend mount (keyless fallback):**
   `https://search-library.ucsd.edu/primaws/rest/pub/pnxs?...`.
   Same documented API surface the Primo web UI calls; requires no key. It is the
   frontend's service layer rather than a published contract, so run a preflight
   probe each session (e.g., `q=any,contains,"AI ethics"`); treat HTTP 400/404 or
   zero-result responses as a signal to re-verify or fall back.

## Parameter Recipe

```
GET {mount}?offset={PAGE OFFSET}&inst=01UCS_SDI&limit=20&vid=01UCS_SDI%3AUCSD
    &scope=ArticlesBooksEtc&tab=ArticleBooksEtc
    &q=any,contains,{URL-ENCODED BOOLEAN QUERY}
    &lang=eng&sort=rank&pcAvailability=false
    &qInclude={optional filters}&qExclude=
```

- The boolean query uses the exact single-parameter format produced by the
  `uc-library-search` skill's `scripts/build_url.py` (phrases quoted, OR groups
  parenthesized, truncation allowed).
- **Timeouts:** complex multi-concept boolean queries can exceed 30 seconds
  server-side. Use a 120-second timeout.
- **Result counts are not predictable from query structure alone.** Do not
  pre-commit to expected counts, and do not treat the `uc-library-search`
  skill's estimates as reliable. The response's `info.total` is a first signal,
  but only screening tells you how much is relevant. Paginate by fidelity, never
  by count.

## Filter Translation

Translate strategy filters to documented `qInclude` facet syntax. Join multiple
facets with the literal separator `|,|`:

| Strategy filter | qInclude value | Verified result |
|---|---|---|
| Peer-reviewed only | `facet_tlevel,exact,peer_reviewed` | Works |
| Articles only | `facet_rtype,exact,articles` | Works; all records type article |
| Combined | `facet_rtype,exact,articles\|,\|facet_tlevel,exact,peer_reviewed` | Works |
| Date range YYYY–YYYY | `facet_searchcreationdate,exact,[YYYY TO YYYY]` | Works; all records in range |

**Critical warning:** the UI deep-link format `searchcreationdate,include,2022|,|2026,lk`
does NOT work via the API and silently returns zero results. The bracket syntax
above is required. If a filter cannot be translated, apply it at screening time
and log that you did so.

## PNX Metadata Inventory

A verified failure mode: a screening script that reads only title/creator/year/type
discards the most valuable fields. When screening and verifying Primo results,
read from this inventory:

| PNX field | Content | Use |
|---|---|---|
| `pnx.display.title` | Title | Screening |
| `pnx.display.creator`, `contributor` | Authors/editors | Screening, citations |
| `pnx.display.creationdate` | Publication year | Scope checks, date screening |
| `pnx.display.type` | Format (book, article, video, ...) | Format-coverage analysis |
| `pnx.display.subject`, `mesh` | Subject headings | Relevance classification, vocabulary discovery |
| `pnx.display.publisher` | Publisher | Citations |
| `pnx.display.description` | Publisher description (books, some articles) | Content verification; description-level annotations |
| `pnx.display.contents` | Table of contents (books) | Chapter-level relevance and coverage claims |
| `pnx.addata.abstract` | Full abstract — present for articles AND many books | Primary first-pass verification source |
| `pnx.addata.doi`, `isbn`, `oclcid` | Identifiers | Cross-verification keys |
| `pnx.addata.source`, `volume`, `issue`, `pages`, `pub` | Venue data | Citation construction |
| `delivery.bestlocation`, `delivery.holding` | Local holdings, call number, availability | Retrieval guidance; human retrieval lists |
| `delivery.almaInstitutionsList` | UC-wide holdings | Retrieval guidance |

Verification policy for these fields (article abstracts vs. book descriptions,
confidence caps) lives in SKILL.md's "Verify Before Annotating" section.

## Troubleshooting

- **HTTP 400, empty body:** usually a malformed `q` — confirm the
  `any,contains,` field prefix is present and the boolean expression is fully
  URL-encoded with parentheses literal.
- **Zero results with a date filter:** wrong date syntax — the UI deep-link form
  fails silently; use `facet_searchcreationdate,exact,[YYYY TO YYYY]`.
- **"No service was found":** wrong path — the search endpoint is
  `/primaws/rest/pub/pnxs`, not `/primaws/rest/search`.
- **30+ second hangs on complex queries:** expected server-side behavior; use a
  120-second timeout rather than simplifying the query prematurely.
