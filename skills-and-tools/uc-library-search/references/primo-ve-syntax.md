# Primo VE Syntax and URL Construction (Verified)

Source of truth for building UC Library Search queries. Everything marked **verified** was
tested live against `search-library.ucsd.edu` (Sept 2026). Anything labeled "vendor-documented
but unverified" comes from Ex Libris documentation and should be treated as a claim, not a fact.

## Table of Contents

- [URL anatomy](#url-anatomy)
- [Encoding rules](#encoding-rules)
- [Boolean operators and precedence](#boolean-operators-and-precedence)
- [Phrase searching](#phrase-searching)
- [Truncation and wildcards](#truncation-and-wildcards)
- [Field codes and search types](#field-codes-and-search-types)
- [Filters (facets)](#filters-facets)
- [Pitfall: chained query parameters](#pitfall-chained-query-parameters)
- [Result counts are estimates](#result-counts-are-estimates)
- [Advanced Search interface notes](#advanced-search-interface-notes)
- [How to verify a generated URL](#how-to-verify-a-generated-url)

## URL anatomy

```
https://search-library.ucsd.edu/discovery/search
  ?query=<field>,<search_type>,<url-encoded boolean expression>
  &tab=ArticleBooksEtc
  &search_scope=ArticlesBooksEtc
  &vid=01UCS_SDI:UCSD
  [&mfacet=...&facet=...]   # optional filters
```

- The **entire boolean expression** goes in ONE `query` parameter, parentheses preserved.
- Primo may append extra params (`lang=en`, `offset=0`) when it normalizes the URL; you do not
  need to add them.
- `search-library.ucsd.edu` is the UCSD instance of UC Library Search. The systemwide entry
  point is `library.universityofcalifornia.edu`; campus instances share the same URL scheme.
- Default scope covers all 10 UC campuses. "Articles, books, and more" = `ArticleBooksEtc`.

## Encoding rules

| Character | Encode as | Notes (verified) |
|---|---|---|
| space | `%20` | |
| `"` (phrase) | `%22` | |
| `(` `)` | keep literal | required for grouping; do NOT encode |
| `?` (wildcard) | `%3F` | a literal `?` breaks the URL (query separator) |
| `*` (truncation) | keep literal | `%2A` also works; both verified identical |
| AND / OR / NOT | `%20AND%20` / `%20OR%20` / `%20NOT%20` | UPPERCASE only; lowercase is ignored |
| `&` `#` `%` `+` | encode via `urllib.parse.quote` | not used in normal queries |

Build URLs with `scripts/build_url.py` (uses `urllib.parse.quote(query, safe="()*")`) so these
rules never get applied by hand.

## Boolean operators and precedence

- **UPPERCASE only**: `AND`, `OR`, `NOT`. Lowercase (`and`, `or`, `not`) is not honored.
- **AND binds before OR (verified)**: `zebrafish OR medaka AND cancer` → 91,564 results vs
  `(zebrafish OR medaka) AND cancer` → 13,333 results. Therefore:
  - Always group synonyms with `( ... OR ... )`.
  - Parentheses control order of operations, like in math.
- NOT works (verified: `zebrafish NOT cancer` → ~78k vs ~91k for `zebrafish` alone). Use only
  when essential and warn users that NOT may exclude relevant results. When NOT is the only
  operator applied to one concept, still parenthesize when combined: `(zebrafish NOT cancer)`.
- No **proximity operators** (NEAR, W/n, ADJ) exist in Primo VE. Compensate with phrase
  searching (`"machine learning"` instead of machine-within-2-words-of-learning).

## Phrase searching

- Quotation marks require terms to appear together in order: `"social media"` searches the
  exact phrase, not social AND media anywhere.
- Use phrase searching for nearly all multi-word concepts — it is the single biggest precision
  lever available, especially because proximity operators are missing.
- Zero results from a phrase? Check for characters inside the phrase that Primo might not index
  (hyphens, ampersands, punctuation); try a keyword version of the same concept.

## Truncation and wildcards

- **Right truncation** with `*`: `cultur*` matches culture, cultural, culturally, cultures.
  Verified working in URLs. Remember counts are estimates — the exact-match word can even
  outrank/outcount a truncated stem; check with a quick test when in doubt.
- **Wildcard** with `?` for one character: `wom?n` matches woman, women. **URL-encode `?` as
  `%3F` or the URL breaks** (verified working encoded).
- Abbreviations/American-British variants: `colo?r` → color, colour.
- Vendor-documented limits, unverified on this instance: maximum 7 asterisks per query for
  words longer than 2 characters; maximum 8 question marks per query.
- Precision rule: prefer explicit variants (`therapy OR therapies OR therapeutic`) over broad
  truncation (`therap*`) when variants are few and known.

## Field codes and search types

Field codes (verified; counts are single-observation samples, not authoritative):

| Code | Field | Verified example |
|---|---|---|
| `any` | Anywhere / all fields | `any,contains,zebrafish` |
| `title` | Title | `title,contains,"zebrafish" AND cancer` |
| `sub` | Subject headings | `sub,contains,"zebrafish"` |
| `creator` | Author/creator | `creator,contains,driever` |

Search types: `contains` (standard, verified) and `exact` (verified it executes; prefer
`contains` plus phrase quotes unless you need strict field equality).

**Field codes cannot be typed in the simple search box** ("title:term" does not work there).
Field-specific searching requires the Advanced Search interface, whose line builders produce the
same `query=<field>,<type>,<term>,<OP>` structure under the hood.

## Filters (facets)

Verified filter parameters (append in any order after `&vid=...`):

```
&mfacet=tlevel,include,peer_reviewed,1                      # Peer-reviewed Journals
&mfacet=rtype,include,articles,1                            # Articles
&facet=searchcreationdate,include,2018%7C,%7C2026,lk        # Published 2018-2026
```

- Date range format: `facet=searchcreationdate,include,START%7C,%7CEND,lk` where `%7C` is the
  pipe `|`; the literal spec is `START|,|END`. Use 4-digit years.
- Applied filters appear under "Active filters" in the left sidebar; the search box keeps showing
  the clean query (the search box is NOT garbled by filter codes in this format).
- Standard facet codes that exist in Primo VE but were NOT re-verified on this instance — check
  the left sidebar after applying manually, or test the URL before promising:
  - `&mfacet=tlevel,include,available,1` (available items)
  - `&mfacet=tlevel,include,online_resources,1` (online resources)
  - `&mfacet=rtype,include,books,1` / `rtype,include,dissertations,1` / other rtype values
  - `&mfacet=rtype,exclude,reviews,1` (exclude reviews)
  - `&mfacet=lang,include,eng,1` (English) and other language codes

Decision rule: include filters when explicitly requested (peer-reviewed, date range, material
type), or when precision clearly benefits. Omit for exploratory searches and when uncertain.

## Pitfall: chained query parameters

Primo's own UI can rewrite a typed query into multiple `query` parameters:

```
query=any,contains,term1,AND&query=any,contains,term2&...
```

On this instance that representation **mis-executes**. Live test results:

- `any,contains,zebrafish,AND&any,contains,cancer` → **17 results**
- `any,contains,zebrafish AND cancer` (single param) → **27,802 results** (same intended logic)
- The prompt-era three-concept example in chained form returned a meaningless **47,346,467**.

Behavior to watch for: the search box displaying internal notation like `term1,AND;any,contains,term2`.
If that appears, the URL is in the wrong form — regenerate via `scripts/build_url.py` so the whole
expression lives in one `query` parameter.

## Result counts are estimates

Primo's displayed counts are estimates and fluctuate between loads (e.g., `zebrafish` read
191,794 on one load and 91,327 on another). Never promise an exact count; give ranges and tell
users to validate by scanning the first 20–30 results and checking for known key articles.

## Advanced Search interface notes

- Recommend Advanced Search when the user needs field-specific searching (Title, Subject,
  Author), multiple pre-applied filters, or a visual query builder.
- Advanced Search lines map to the same single-parameter URL when a search runs.
- Filters can be applied before searching or after via the left sidebar.

## How to verify a generated URL

1. Open the link (browser). Results load and the search box shows the clean boolean expression.
2. Confirm filters appear under "Active filters" if included.
3. Scan the first 20–30 results: on-topic? The expected material type/date range?
4. If the search box shows internal syntax (`term,AND;any,contains,...`) or results look
   wrong-scale, regenerate the URL in single-parameter form and test again.
