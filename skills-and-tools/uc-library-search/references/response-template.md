# Response Template and Worked Example

Required output shape for every UC Library Search interaction. Complete all sections that apply;
always include the direct link (built with `scripts/build_url.py`), copy-paste query, Advanced
Search instructions, alternatives, and the plain-language explanation.

## Required output layout

```markdown
## 🎯 Recommended Search Query

### ⚡ Direct Search Link (Click to Search - EASIEST):
**[Click here to run this search in UC Library Search](<URL from scripts/build_url.py>)**

*This link opens UC Library Search with your query already executed. Just click and browse the results.*

**Optional filtered versions** (only when requested or clearly useful):
- **[With peer-reviewed filter](<URL>) — Only scholarly, peer-reviewed content**
- **[Last N years only](<URL>) — Recent publications**
- **[Articles only](<URL>) — Skips books and reviews**

---

### 📋 Copy-Paste Query (For Simple Search Box):
```
("exact phrase" OR synonym) AND ("exact phrase" OR synonym) AND (term OR synonym)
```

**How to use:** Copy the query, paste into the UC Library Search search box, click Search, then
apply any filters from the left sidebar.

---

### 🔍 Advanced Search Strategy (For Higher Precision):
**Line 1 (Title or Subject):** [Field] contains ["exact phrase" OR synonym]
**Line 2:** AND [Field] contains ["exact phrase" OR synonym]
**Line 3:** AND Anywhere contains [supporting terms]

**Recommended Filters:**
- Peer-Reviewed: [Yes / No / Either — with rationale]
- Publication Date: [strategic range — with rationale]
- Material Type: [selection — with rationale]
- Language: [if applicable]

---

## 🔄 Alternative Search Strategies

### If You Find Too Few Results (<20):
**[Broader search link](<URL>) — no filters, more synonyms**

```
(query with more synonyms, fewer filters, wider date range)
```

**What this changes:** [explanation]

### If You Find Too Many Results (>1000) or Low Relevance:
**[Narrower search link](<URL>) — peer-reviewed + articles only + narrower dates**

```
(query with more phrase searching, additional concepts, tighter filters)
```

**What this changes:** [explanation]

### Alternative Approach:
**[Different search link](<URL>)**

```
(alternative concept combination, synonym set, or subject-heading approach)
```

**When to use this:** [scenario where this approach works better]

---

## 📖 Plain Language Explanation

### What This Search Does:
[Clear explanation of strategy and goals]

### Why These Terms:
**Concept 1:** [rationale for terms and phrase searching]
**Concept 2:** [rationale for synonyms]
**Concept 3 (if applicable):** [rationale]

### Search Design Decisions:
- **Phrase searching:** [why used for specific terms]
- **Synonym selection:** [why these alternatives, not exhaustive lists]
- **Filters:** [rationale for date/type/peer-review filters]
- **Field searching (if used):** [why Title/Subject instead of Anywhere]

### What to Expect:
- **Estimated Results:** [range — treat Primo counts as estimates; they fluctuate]
- **Expected Precision:** [X% — meaning Y out of 10 items will be relevant]
- **Screening Time:** [rough review burden]
- **Why This Balance:** [precision vs recall tradeoff]

---

## 🔍 Next Steps

1. Run the search; scan the first 20–30 results and check whether known key articles appear.
2. Use left-sidebar facets (subject, date, resource type, peer-reviewed) to refine.
3. Citation chain from 2–3 highly relevant articles (reference lists + "Cited by").
4. Search 2–3 key authors' other publications.
5. Save the search / set alerts for new publications; export citations to Zotero, Mendeley, or
   EndNote.
6. Report back whether results are too many, too few, or not the right type for an targeted
   revision.

---

## ⚙️ Technical Notes

- Boolean operators must be UPPERCASE (AND, OR, NOT).
- Parentheses are mandatory around OR groups — Primo VE binds AND before OR.
- No proximity operators; phrase searching compensates.
- Field-specific searching (Title/Subject) requires the Advanced Search interface.
- Keep the whole query in ONE URL `query` parameter; never chain `query=` parameters.
- Result counts shown by Primo are estimates and can change between loads.
```

## Worked example

User: "I'm writing a literature review on the impact of social media on college student mental
health."

After Stage 1 clarifying answers (focused on anxiety/depression; last 10 years; ~20–25 sources
needed), the response should look like:

```markdown
## 🎯 Recommended Search Query

### ⚡ Direct Search Link (Click to Search - EASIEST):
**[Click here to run this search in UC Library Search](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD)**

*This link opens UC Library Search with your query already executed. Just click and browse the results.*

**Optional filtered versions:**
- **[With peer-reviewed filter](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1)** — scholarly, peer-reviewed content
- **[Last 10 years only](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&facet=searchcreationdate,include,2016%7C,%7C2026,lk)** — 2016-present
- **[Articles only, peer-reviewed, 2018-2026](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2018%7C,%7C2026,lk)**

---

### 📋 Copy-Paste Query (For Simple Search Box):
```
("social media" OR Facebook) AND (anxiety OR depression) AND ("college students")
```

**How to use:** Copy the query, paste into the UC Library Search search box, click Search, then
add: Peer-Reviewed = Yes, Publication Date = Last 10 years, Resource Type = Articles.

---

### 🔍 Advanced Search Strategy (For Higher Precision):
**Line 1 (Anywhere):** contains ("social media" OR Facebook)
**Line 2:** AND Anywhere contains (anxiety OR depression)
**Line 3:** AND Anywhere contains ("college students")

**Recommended Filters:**
- Peer-Reviewed: Yes — ensures scholarly quality.
- Publication Date: 2016–2026 — recent research as requested.
- Material Type: Articles — most relevant for a literature review.
- Language: English if you only read English.

---

## 🔄 Alternative Strategies

### If You Find Too Few Results (<20):
**[Broader version](https://search-library.ucsd.edu/discovery/search?query=any,contains,(%22social%20media%22%20OR%20Facebook%20OR%20Instagram%20OR%20TikTok)%20AND%20(%22mental%20health%22%20OR%20anxiety%20OR%20depression)%20AND%20(student*%20OR%20undergraduate*%20OR%20%22young%20adult*%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD)**

```
("social media" OR Facebook OR Instagram OR TikTok) AND ("mental health" OR anxiety OR depression) AND (student* OR undergraduate* OR "young adult*")
```

**What this changes:** More platforms, a broader mental-health umbrella, and truncation on
population terms. Drop filters if you still get too few.

### If You Find Too Many Results (>1000) or Low Relevance:
**[Narrower version](https://search-library.ucsd.edu/discovery/search?query=title,contains,(%22social%20media%22%20OR%20Facebook)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD&mfacet=tlevel,include,peer_reviewed,1&mfacet=rtype,include,articles,1&facet=searchcreationdate,include,2020%7C,%7C2026,lk)**

```
("social media" OR Facebook) AND (anxiety OR depression) AND ("college students")
```
*Search this narrower version in the **Advanced Search** interface with Line 1 set to **Title**
contains — field codes like `title:` do not work in the simple search box.*

**What this changes:** Title-field searching (via Advanced Search), peer-reviewed + articles
only, and a 2020–2026 window focus the set on the most on-topic recent work.

### Alternative Approach:
**[Subject-heading version](https://search-library.ucsd.edu/discovery/search?query=sub,contains,(%22social%20media%22)%20AND%20(anxiety%20OR%20depression)%20AND%20(%22college%20students%22)&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI:UCSD)**

```
sub: ("social media") AND (anxiety OR depression) AND ("college students")
```

**When to use this:** When keyword relevance is drifting and you want records indexed under
these concepts as subjects (via Advanced Search Subject field).

---

## 📖 Plain Language Explanation

### What This Search Does:
Combines three concepts — social media, mental health, and the student population — with AND, so
every result discusses all three topics.

### Why These Terms:
**Concept 1 (social media):** "social media" is in quotes so the words appear together in that
order; Facebook is included because authors often name the platform instead of the category.
**Concept 2 (mental health):** anxiety and depression are the specific outcomes you named, and
each is a high-precision term.
**Concept 3 (students):** "college students" is quoted as a phrase — the way the literature
usually writes it.

### Search Design Decisions:
- **Phrase searching:** ensures multi-word concepts appear together, the biggest precision lever.
- **Synonym selection:** strategic, not exhaustive — keeps results focused.
- **Filters:** peer-reviewed + recent dates raise quality and relevance for a lit review.

### What to Expect:
- **Estimated Results:** roughly 1,500–3,000 (Primo counts are estimates and vary by load);
  about 1,000–1,500 with peer-review + article filters.
- **Expected Precision:** ~50–60% on the filtered version — 5–6 of every 10 items relevant.
- **Screening Time:** 2–3 hours to review abstracts and select your best 20–25.
- **Why This Balance:** captures the key studies without drowning you in marginal matches.

---

## 🔍 Next Steps

1. Run the search; scan the first 20–30 results.
2. Use subject facets to find related vocabulary you can add.
3. Once you find 2–3 perfect articles, mine their references and "Cited by" lists.
4. Tell me if results are too many, too few, or the wrong type and I'll adjust the strategy.
```

---

## 🔭 Future Research

**Curated database starting points** (2–4 maximum, when useful):

1. **[Database Name](<authenticated URL>)** — [Why it is a strong next step: subject/type fit, featured subject rank, and what it adds beyond UC Library Search.]
2. **[Database Name](<authenticated URL>)** — [Why it is a strong next step: subject/type fit, featured subject rank, and what it adds beyond UC Library Search.]
3. **[Database Name](<authenticated URL>)** — [Why it is a strong next step: subject/type fit, featured subject rank, and what it adds beyond UC Library Search.]

**How to use these:** Run your UC Library Search concepts and synonyms inside the recommended
database, then refine with that database’s native filters and controlled vocabulary. These are
curated starting points, not exhaustive results.

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
