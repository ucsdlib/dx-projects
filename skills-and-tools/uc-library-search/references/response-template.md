# Response Template and Worked Example

Required output shape for every UC Library Search interaction. Complete all sections that apply;
always include the direct link (built with `scripts/build_url.py`), copy-paste query, the
higher-precision option, and alternatives. Add Future Research when the topic maps to A-Z data.
Each "Run..." link opens the search with its URL filters already applied; the accompanying query
is for users who prefer to paste the search and build filters themselves.

## Required output layout

```markdown
## 🎯 Initial Search Strategy

[Concise, 1-2 sentence overview of the initial search strategy in plain, easy to understand language]

**[Run this search with its filters](<URL from scripts/build_url.py>)** - *Click the link to browse the results.*

```
("exact phrase" OR synonym) AND ("exact phrase" OR synonym) AND (term OR synonym)
```

**If you paste the query instead:** use the simple search box and apply any filters included in the linked version from the left sidebar.

### Concept Breakdown:
**Concept 1:** [rationale for terms and phrase searching]
**Concept 2:** [rationale for synonyms]
**Concept 3 (if applicable):** [rationale]

### Search Design Decisions:
- **Phrase searching:** [why used for specific terms]
- **Synonym selection:** [why these alternatives, not exhaustive lists]
- **Filters:** [rationale for date/type/peer-review filters]
- **Field searching (if used):** [why Title/Subject instead of Any field]

### What to Expect:
- Results will vary in relevance: some will directly address the question, some will be adjacent, and some will not be useful.
- Browsing is part of the search: scan for direct matches, adjacent work, and unexpected perspectives or vocabulary.
- Treat search as iterative inquiry. Adjust filters, change terms, or try a different lens as the results reshape what you know or want to ask.

## Optional filtered versions (only when requested or clearly useful):
- **[With peer-reviewed filter](<URL>) — Only scholarly, peer-reviewed content**
- **[Last N years only](<URL>) — Recent publications**
- **[Articles only](<URL>) — Skips books and reviews**
- Material Type: [selection — with rationale]
- Language: [if applicable]

---

## 🔍 Increasing Precision and Relevance with "Advanced Search":

**Plain-language tip:** If your searches are too broad, or if you are not getting enough relevant results, use UC Library Search’s [Advanced Search](https://search-library.ucsd.edu/discovery/search?vid=01UCS_SDI:UCSD&mode=advanced) interface and set one or two central concept lines to Title or Subject. Start with one search concept at a time, testing your results as you go. Adapt the lines below to the concepts that matter most in your question.

**Single-field example link:** **[Run this query with Title selected](<URL from scripts/build_url.py --field title --advanced>)** — *This demonstrates a Title-field search; every concept group in the query is searched in the Title field.*

**Line 1 (Title or Subject):** [Field] contains ["exact phrase" OR synonym]
**Line 2:** AND [Field] contains ["exact phrase" OR synonym]
**Line 3:** AND Any field contains [supporting terms]

**To use different fields on different lines:** build the query in the Advanced Search interface. A single URL can reliably apply the same field to the whole query, but it cannot reliably represent a mixed-field line layout.


---

## 🔄 Alternative Search Strategies

### If You Want to Broaden Your Search to Find More Results:
**[Broader search link](<URL>) — no filters, more synonyms**

```
(query with more synonyms, fewer filters, wider date range)
```

**What this changes:** [explanation]

### If You Find Too Many Results or Low Relevance:
**[Narrower search link](<URL>) — peer-reviewed + articles only + narrower dates**

```
(query with more phrase searching, additional concepts, tighter filters)
```

**What this changes:** [explanation]

### To Focus on [relevant aspect or concept]:
**[Run this focused search](<URL>)**

```
(topic-specific concept combination or synonym set)
```

**What this adds:** [why this lens is useful to this question]

### To Focus on [other relevant aspect or concept]:
**[Run this focused search](<URL>)**

```
(another topic-specific concept combination or synonym set)
```

**What this adds:** [how this lens differs or expands the search]


---

## 🔍 Next Steps

1. Run the search and browse the initial results. Expect a mix of direct matches, adjacent work, and less relevant records.
2. Use left-sidebar facets (subject, date, resource type, peer-reviewed) to refine and discover useful vocabulary.
3. Experiment: change a term, adjust a filter, or try a different lens. Search is a way of exploring the topic, not a one-time lookup.

[include additional next steps, if relevant based on the user's specific research needs]

---

## 🔭 Future Research (when useful)

**Curated database starting points** (2–4 maximum, when the topic maps to A-Z data):

1. **[Database Name](<authenticated URL>)** — [Why it adds coverage beyond UC Library Search.]
2. **[Database Name](<authenticated URL>)** — [Why it adds coverage beyond UC Library Search.]

**How to use these:** Run the same concepts and synonyms in the recommended database, then use that database’s native filters and controlled vocabulary.

---
```

## Worked example

User: "I'm writing a literature review on the impact of social media on college student mental
health."

After Stage 1 clarifying answers (focused on anxiety/depression; last 10 years; ~20–25 sources
needed), the response should look like:

```markdown
## 🎯 Initial Search Strategy

This search connects three concepts — social media, two mental-health outcomes, and the college-student population — and focuses on peer-reviewed articles from 2016–2026. That structure keeps the literature review centered on the outcomes and population you named while filtering out older and non-peer-reviewed work.

**[Run this search with its filters](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2016%7C,%7C2026,lk)** - *Click the link to browse the results.*

```
("social media" OR Facebook) AND (anxiety OR depression) AND ("college students")
```

**If you paste the query instead:** use UC Library Search’s simple search box, then apply peer-reviewed, articles-only, and 2016–2026 filters from the left sidebar.

### Concept Breakdown:
**Concept 1 (social media):** "social media" is quoted so the words appear together in that order; Facebook captures records that name the platform instead of the broader category.
**Concept 2 (mental health):** anxiety and depression are the specific outcomes you named, and they are more precise than the broad phrase "mental health."
**Concept 3 (students):** "college students" is quoted because that phrase is commonly used in the literature.

### Search Design Decisions:
- **Phrase searching:** keeps multi-word concepts — "social media" and "college students" — together in the intended order.
- **Synonym selection:** Facebook and the two mental-health outcomes are strategic additions, not exhaustive synonym lists.
- **Filters:** peer-reviewed, articles-only, and 2016–2026 filters align the search with recent literature-review sources.

### What to Expect:
- You will see a mix of direct matches, adjacent work, and less relevant records. That variation is normal.
- Browse for the most useful sources, but also watch for unexpected perspectives, methods, or vocabulary you may not have considered.
- Treat this as an exploration: change one term or filter at a time, then compare how the results change.

## Optional filtered versions (only when requested or clearly useful):
- **[With peer-reviewed filter](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1)** — Only scholarly, peer-reviewed content
- **[2016–2026 only](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&facet=searchcreationdate,include,2016%7C,%7C2026,lk)** — Recent publications
- **[Articles only](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=rtype,include,articles,1)** — Skips books and reviews

---

## 🔍 Increasing Precision and Relevance with "Advanced Search":

**Plain-language tip:** If the results are too broad, use UC Library Search’s Advanced Search interface to move the most central concept to Title or Subject. Here, social media is the core concept; keep the outcome and population lines on "Any field" so the search does not become too narrow.

**Single-field example link:** **[Run this query with Title selected](https://search-library.ucsd.edu/discovery/search?query=title,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mode=advanced&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2016%7C,%7C2026,lk)** — *This demonstrates a Title-field search; every concept group in the query is searched in the Title field.*

**Line 1 (Title):** ("social media" OR Facebook)
**Line 2 (Any field):** AND (anxiety OR depression)
**Line 3 (Any field):** AND ("college students")

**To use different fields on different lines:** build the query in the Advanced Search interface. The link above applies Title to the entire query; it is a useful single-field demonstration rather than the mixed-field line layout shown here.

---

## 🔄 Alternative Search Strategies

### If You Want to Broaden Your Search to Find More Results:
**[Broader search link](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook%20OR%20Instagram%20OR%20TikTok)%20AND%20(%22mental%20health%22%20OR%20anxiety%20OR%20depression)%20AND%20(student*%20OR%20undergraduate*%20OR%20%22young%20adult*%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD)** — no filters, more synonyms

```
("social media" OR Facebook OR Instagram OR TikTok) AND ("mental health" OR anxiety OR depression) AND (student* OR undergraduate* OR "young adult*")
```

**What this changes:** Adds platforms, broadens the mental-health concept, widens the population vocabulary, and removes the filters.

### If You Find Too Many Results or Low Relevance:
**[Narrower search link](https://search-library.ucsd.edu/discovery/search?query=title,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2020%7C,%7C2026,lk)** — peer-reviewed + articles only + narrower dates

```
("social media" OR Facebook) AND (anxiety OR depression) AND ("college students")
```

**What this changes:** Searches the keywords in titles, adds peer-reviewed and articles-only filters, and narrows the window to 2020–2026.

### To Focus on Self-Esteem and Identity:
**[Run this focused search](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook%20OR%20Instagram)%20AND%20(%22self-esteem%22%20OR%20%22self%20concept%22)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2016%7C,%7C2026,lk)**

```
("social media" OR Facebook OR Instagram) AND ("self-esteem" OR "self concept") AND ("college students")
```

**What this adds:** Explores identity-related aspects of social media use beyond anxiety and depression.

### To Focus on Academic Experiences:
**[Run this focused search](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(%22academic%20performance%22%20OR%20studying)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2016%7C,%7C2026,lk)**

```
("social media" OR Facebook) AND ("academic performance" OR studying) AND ("college students")
```

**What this adds:** Connects social media to study behaviors and academic outcomes, which may reveal a different evidence base.

---

## 🔍 Next Steps

1. Run the search and browse the initial results. Expect a mix of direct matches, adjacent work, and less relevant records.
2. Use left-sidebar facets (subject, date, resource type, peer-reviewed) to refine and discover useful vocabulary.
3. Experiment by changing one element at a time — a platform, outcome, date range, or filter — and compare how the results change.
4. Once you find 2–3 highly relevant articles, mine their references and "Cited by" lists.
5. Tell me if results are too many, too few, or not the right type and I'll adjust the strategy.

---

## 🔭 Future Research (when useful)

**Curated database starting points:**

1. **[PsycINFO](https://ucsd.libguides.com/psycinfo)** — Strong psychology coverage and controlled vocabulary for mental-health concepts.
2. **[PsycArticles](https://ucsd.libguides.com/psycarticles)** — Adds full-text psychology journal articles beyond UC Library Search.

**How to use these:** Run the same concepts and synonyms in the recommended database, then use that database’s native filters and controlled vocabulary.
```

## Production notes

- Generate every URL with `scripts/build_url.py`; never hand-encode or reuse a URL that was not
  emitted by the script. Update the dates/terms above to match the user's actual research need.
- If counts or dates drift from reality (Primo versions updates, index changes), re-verify one
  generated URL in a browser before sending.
- Keep explanations at the user's experience level (ask in Stage 1); beginners get more syntax
  detail, advanced users get precedence/truncation/field-search rationale.
- Expert, fully specified requests: skip clarifying questions — open the response with a
  one-line strategy confirmation (concepts, scope, filters) and proceed straight to the four
  formats.
