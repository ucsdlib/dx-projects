# Primo Search API Reference

All parameters, query syntax, filters, and pagination limits below are drawn from
the documented Ex Libris Primo Search API. This file pertains only to Primo
Search and not to any other Primo REST surface.

## Documented API

The Primo Search API is documented on the Ex Libris Developer Network:
`https://developers.exlibrisgroup.com/primo/apis/docs/primoSearch/R0VUIC9wcmltby92MS9zZWFyY2g=/`
(`GET /primo/v1/search`, JSON output).

## Activation and Authentication

Use this Primo Search pathway only when the skill directory contains `.env` and
that file defines `PRIMO_KEY`. If `.env` is absent or `PRIMO_KEY` is missing or
empty, skip this pathway and record the documented skip in the search log.

Load `PRIMO_KEY` from `skills-and-tools/annotated-bibliography/.env` at runtime
and send it as the hosted API key. Do not hard-code, echo, or log the key.

## Parameter Recipe

```
GET https://api-na.hosted.exlibrisgroup.com/primo/v1/search?
    vid={VIEW ID}&tab={TAB}&scope={SCOPE}&inst={INSTITUTION}
    &q={URL-ENCODED QUERY}&offset={PAGE OFFSET}&limit={PAGE SIZE}
    &qInclude={OPTIONAL FILTERS}&qExclude={OPTIONAL EXCLUSIONS}
    &lang=eng&sort=rank&pcAvailability=false&apikey=${PRIMO_KEY}
```

- Replace `{VIEW ID}`, `{TAB}`, `{SCOPE}`, and `{INSTITUTION}` with values
  configured for the target institution.
- URL-encode the complete `q` value.
- Use `offset=0`, `limit=20`, `sort=rank`, and `pcAvailability=false` as a
  reproducible initial page.
- Set a 120-second client timeout. Complex boolean queries can be slow.

## Query Syntax

The basic query format is:

```
q=<field>,<precision>,<value>
```

Multiple field clauses are separated by semicolons:

```
q=<field_1>,<precision_1>,<value_1>[,<operator_1>;<field_n>,<precision_n>,<value_n>...]
```

| Component | Values | Example |
|---|---|---|
| Field | `any`, `title`, `creator`, `sub`, `usertag` | `title,contains,home` |
| Precision | `exact`, `begins_with`, `contains` | `title,exact,"AI ethics"` |
| Boolean operator within a value | `AND`, `OR`, `NOT`; group with parentheses | `any,contains,("AI ethics" OR "machine learning")` |
| Field-clause operator | `AND`, `OR`, `NOT`; defaults to `AND` | `title,contains,pop music,AND;sub,contains,korean` |

- Quote phrases that must remain together.
- Parenthesize OR groups.
- A semicolon separates field clauses, so it must not occur inside a clause value.
- Prefer one fully formed `q` expression unless the strategy specifically requires
  separate fielded clauses.

## Filter Translation

`qInclude` and `qExclude` use:

```
<facet_category>,exact,<facet_name>
```

Join multiple facets with the literal separator `|,|`. The logical AND is applied
between facets. Useful categories include:

| Category | Meaning |
|---|---|
| `facet_rtype` | Resource type |
| `facet_topic` | Subject |
| `facet_creator` | Author |
| `facet_tlevel` | Availability |
| `facet_domain` | Collection |
| `facet_library` | Library name |
| `facet_lang` | Language |
| `facet_lcc` | Library of Congress classification |
| `facet_searchcreationdate` | Creation date |

| Goal | Filter |
|---|---|
| Peer-reviewed only | `facet_tlevel,exact,peer_reviewed` |
| Articles only | `facet_rtype,exact,articles` |
| Peer-reviewed articles | `facet_rtype,exact,articles\|,\|facet_tlevel,exact,peer_reviewed` |
| Publication years YYYY–YYYY | `facet_searchcreationdate,exact,[YYYY TO YYYY]` |

**Critical warning:** do not use the UI deep-link date form
`searchcreationdate,include,2022|,|2026,lk` through the API. Use the bracket form
above. If a UI filter cannot be translated confidently, apply it during screening
and record that decision in the search log.

## Optional Parameters

| Parameter | Type / default | Behavior |
|---|---|---|
| `offset` | integer, `0` | Starting result offset. The maximum value of `offset + limit` is 2000. |
| `limit` | integer, `10` | Results per response. Recommended maximum is 50. |
| `sort` | string, `rank` | `rank`, `title`, `author`, `date`, `date_d` (newest), or `date_a` (oldest). |
| `pcAvailability` | boolean | `true` displays records without full text; `false` limits the response to full-text records. Primo VE commonly uses `false`. |
| `lang` | string, `eng` | Language. Use the format appropriate to the Primo version. |
| `fromDate` | string | Database-update cutoff in `YYYYMMDDHHMMSS` format. |
| `multiFacets` | string | Include/exclude facets with OR logic between values and AND logic between categories. |
| `newspapersSearch` | boolean | Enables newspaper search; pair with `pcAvailability=true`. |
| `newspapersActive` | boolean, `true` | Indicates whether newspaper search is active. |
| `skipDelivery` | boolean, `true` | Primo VE option to omit delivery data and improve speed. |
| `disableSplitFacets` | boolean, `true` | Primo VE option to omit facets and improve speed. |
| `conVoc` | boolean, `true` | Enables controlled-vocabulary synonym expansion. Disable when exact reproducibility is required. |
| `personalization` | string | Up to five semicolon-delimited Primo Central disciplines; boosts records in those disciplines. |
| `journals`, `databases`, `getMore` | string | Narrower or legacy options; use only when the script has a separate requirement for them. |

## Pagination

1. Begin with `offset=0` and `limit=20`.
2. Read `info.total`, but do not assume it represents the number of relevant
   results.
3. Continue only while returned results remain materially relevant to the search
   strategy.
4. Stop when `offset + limit >= min(2000, info.total)` or relevance drops.
5. Log pages examined and the stop reason.

Guest requests are reported to be limited to 500 results. Authenticated requests
can retrieve up to 2000 through the `offset + limit` ceiling.

## Troubleshooting

- **HTTP 401:** verify that `.env` exists and contains a non-empty, valid
  `PRIMO_KEY`.
- **HTTP 400 with an empty body:** check that `q` has a field and precision
  prefix, phrase quotes are preserved, OR groups are literal, and no clause value
  contains a semicolon.
- **HTTP 404:** verify the exact `/primo/v1/search` resource path and base URL.
- **Zero results with a date filter:** use
  `facet_searchcreationdate,exact,[YYYY TO YYYY]`, not the UI deep-link date form.
- **30+ second query:** keep the 120-second timeout rather than simplifying the
  query prematurely.
- **HTTP 500:** retry once after a short delay; otherwise fail loudly while
  preserving the query and response context.

Every request should log the endpoint, complete query parameters, status,
`info.total`, the number of returned docs, and any retry or manual-filter
translation.

## Source Notes

Ex Libris Primo Search parameter contract:
`https://developers.exlibrisgroup.com/primo/apis/docs/primoSearch/R0VUIC9wcmltby92MS9zZWFyY2g=/`
