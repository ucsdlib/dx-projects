#!/usr/bin/env python3
"""Build direct UC Library Search (Primo VE) search URLs.

Generates the single-query-parameter URL format that is verified to work on
search-library.ucsd.edu. All boolean logic lives in ONE `query` parameter; the
chained `query=...,AND&query=...,AND&query=...` format is unreliable on this
instance and is never emitted here.

Usage:
    python3 build_url.py "<boolean query>" [--field any|title|sub|creator] \
        [--filters peer_reviewed] [--filters articles] [--filters books] \
        [--filters online_resources] [--filters YYYY-YYYY] [--self-test]

Examples:
    python3 build_url.py '("social media" OR Facebook) AND (anxiety OR depression) AND ("college students")'
    python3 build_url.py '"climate change" AND policy' --field title --filters peer_reviewed --filters 2018-2026

Encoding rules (verified against the live instance):
    space     -> %20
    quote     -> %22  (phrase searching)
    question  -> %3F  (wildcard; a literal '?' would break the URL)
    parens    -> kept literal  (grouping; Primo binds AND before OR)
    asterisk  -> kept literal (truncation; %2A also works)
    AND/OR/NOT -> UPPERCASE, encoded as %20AND%20 etc.
"""

import argparse
import sys
import urllib.parse

DEFAULT_HOST = "https://search-library.ucsd.edu"
TAB = "ArticleBooksEtc"
SCOPE = "ArticlesBooksEtc"
VID = "01UCS_SDI:UCSD"

FIELDS = {"any": "any", "title": "title", "sub": "sub", "creator": "creator"}

# (--filters value, URL parameter)
FILTER_PARAMETERS = {
    "peer_reviewed": "mfacet=tlevel,include,peer_reviewed,1",
    "articles": "mfacet=rtype,include,articles,1",
    "books": "mfacet=rtype,include,books,1",
    "online_resources": "mfacet=tlevel,include,online_resources,1",
}


def encode_query(query):
    """Percent-encode a Primo VE boolean query for the query= parameter."""
    return urllib.parse.quote(query.strip(), safe="()*")


def build_filter_params(filters):
    """Return a list of encoded URL parameters for the requested filters."""
    params = []
    for value in filters:
        key = value.lower()
        if key in FILTER_PARAMETERS:
            params.append(FILTER_PARAMETERS[key])
        elif len(key) == 9 and key[4] == "-" and key[:4].isdigit() and key[5:].isdigit():
            start, end = key[:4], key[5:]
            params.append(
                "facet=searchcreationdate,include,{}%7C,%7C{},lk".format(start, end)
            )
        else:
            raise ValueError(
                "Unknown filter {!r}. Use one of: peer_reviewed, articles, books, "
                "online_resources, or a YYYY-YYYY date range.".format(value)
            )
    return params


def build_url(query, field="any", filters=None, host=DEFAULT_HOST):
    """Build the canonical UC Library Search URL for a boolean query."""
    if field not in FIELDS:
        raise ValueError("Field {!r} not supported. Use one of: any, title, sub, creator.".format(field))
    query = query.strip()
    if not query:
        raise ValueError("Query must not be empty.")

    url = "{}/discovery/search?query={},contains,{}&tab={}&search_scope={}&vid={}".format(
        host,
        FIELDS[field],
        encode_query(query),
        TAB,
        SCOPE,
        VID,
    )
    filter_params = build_filter_params(filters or [])
    if filter_params:
        url += "&" + "&".join(filter_params)
    return url


def self_test():
    failures = []
    cases = [
        (
            'climate change',
            dict(),
            "https://search-library.ucsd.edu/discovery/search?query=any,contains,climate%20change&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD",
        ),
        (
            '"social media"',
            dict(),
            "https://search-library.ucsd.edu/discovery/search?query=any,contains,%22social%20media%22&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD",
        ),
        (
            '("social media" OR Facebook) AND anxiety',
            dict(),
            "https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20anxiety&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD",
        ),
        (
            'wom?n',
            dict(),
            "https://search-library.ucsd.edu/discovery/search?query=any,contains,wom%3Fn&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD",
        ),
        (
            'zebrafis*',
            dict(),
            "https://search-library.ucsd.edu/discovery/search?query=any,contains,zebrafis*&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD",
        ),
        (
            '"zebrafish" AND cancer',
            dict(field="title"),
            "https://search-library.ucsd.edu/discovery/search?query=title,contains,%22zebrafish%22%20AND%20cancer&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD",
        ),
        (
            '"social media" AND anxiety',
            dict(filters=["peer_reviewed", "articles", "2018-2026"]),
            "https://search-library.ucsd.edu/discovery/search?query=any,contains,%22social%20media%22%20AND%20anxiety&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2018%7C,%7C2026,lk",
        ),
    ]
    for query, kwargs, expected in cases:
        try:
            actual = build_url(query, **kwargs)
        except Exception as exc:  # pragma: no cover
            failures.append("{} {!r} raised: {}".format(kwargs, query, exc))
            continue
        if actual != expected:
            failures.append(
                "MISMATCH for {!r} {!r}:\n  expected: {}\n  actual:   {}".format(
                    query, kwargs, expected, actual
                )
            )

    if failures:
        print("FAIL ({})".format(len(failures)))
        for message in failures:
            print(" - " + message)
        return False

    print("PASS ({} cases)".format(len(cases)))
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Build a direct UC Library Search (Primo VE) search URL."
    )
    parser.add_argument("query", nargs="?", help="Boolean query as typed in the simple search box")
    parser.add_argument("--field", default="any", choices=sorted(FIELDS), help="Search field (default: any)")
    parser.add_argument("--filters", action="append", default=[], help="Filter to apply; repeatable")
    parser.add_argument("--self-test", action="store_true", help="Run encoding self-tests and exit")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    if not args.query:
        parser.error("a <query> argument or --self-test is required")

    try:
        print(build_url(args.query, field=args.field, filters=args.filters))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
