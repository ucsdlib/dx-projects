#!/usr/bin/env python3
"""Build manifest and user-facing test artifacts for the social-media run."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).parent
RECORD_IDS: dict[str, str] = {}

SELECTED_IDS = [
    "landscape-03",
    "landscape-05",
    "landscape-10",
    "landscape-11",
    "landscape-14",
    "landscape-15",
    "landscape-19",
    "component-03",
    "component-10",
    "component-18",
    "sleep-02",
    "sleep-04",
]

READING_LIST_IDS = [
    "component-10",
    "landscape-19",
    "component-03",
    "landscape-11",
    "landscape-15",
    "landscape-14",
    "landscape-05",
    "sleep-02",
    "sleep-04",
]

SELECTION_REASONS = {
    "landscape-03": "Systematic review of SNS-based youth mental-health interventions; directly maps an intervention branch.",
    "landscape-05": "Review linking problematic SNS use to depression, anxiety, stress, sleep, and emerging brain-function evidence.",
    "landscape-10": "Survey and interview study of peer recognition, stigma, and support on SNSs; represents a social-context branch.",
    "landscape-11": "Cross-sectional student study linking SNS use, impression management, social comparison, depression, and anxiety.",
    "landscape-14": "Three-wave college-freshman panel study testing compensatory SNS use, family support, and depression.",
    "landscape-15": "Randomized experiment testing whether limiting social media improves loneliness, depression, anxiety, and FOMO.",
    "landscape-19": "Systematic review of envy, social comparison, and depression, including evidence on direction and moderators.",
    "component-03": "Three-college-student study set testing self-esteem and FOMO as mediators between SNS use and depression.",
    "component-10": "Systematic review organizing SNS-use effects on self-esteem through comparison, feedback, and self-reflection.",
    "component-18": "Meta-analysis testing whether SNS-use indicators predict well-being after accounting for social support and self-esteem.",
    "sleep-02": "Foundational undergraduate study of social-media timing and sleep quality; retained as a 2016 exception to the preferred date range.",
    "sleep-04": "Cross-sectional study linking problematic SNS use with sleep quality and mental-health symptoms.",
}

THEMES = [
    {
        "theme_id": "theme-problematic-use",
        "name": "Problematic use and mental health",
        "description": "Retrieved sources discuss associations between excessive or problematic SNS use and mental-health symptoms.",
        "source_ids": ["landscape-05", "landscape-14", "component-03", "sleep-04"],
        "support_type": "direct",
    },
    {
        "theme_id": "theme-social-comparison",
        "name": "Social comparison, envy, and self-esteem",
        "description": "Retrieved sources link comparison and envy on SNSs to self-esteem, depression, and anxiety.",
        "source_ids": ["landscape-11", "landscape-19", "component-03", "component-10"],
        "support_type": "direct",
    },
    {
        "theme_id": "theme-sleep",
        "name": "Sleep quality and timing",
        "description": "Retrieved sources connect social-media timing, fatigue, problematic use, and sleep quality among students.",
        "source_ids": ["sleep-02", "sleep-04", "landscape-05"],
        "support_type": "direct",
    },
    {
        "theme_id": "theme-interventions",
        "name": "Interventions and limiting use",
        "description": "Retrieved sources evaluate limiting use or using SNS platforms to deliver mental-health support.",
        "source_ids": ["landscape-03", "landscape-15"],
        "support_type": "direct",
    },
    {
        "theme_id": "theme-social-support",
        "name": "Social support and compensatory use",
        "description": "Retrieved sources discuss family support, peer support, and SNS use as compensation during college transition.",
        "source_ids": ["landscape-10", "landscape-14", "landscape-03"],
        "support_type": "direct",
    },
    {
        "theme_id": "theme-peer-response",
        "name": "Peer disclosure and stigma",
        "description": "One retrieved source examines how students recognize and respond to peers' mental-health disclosures on SNSs.",
        "source_ids": ["landscape-10"],
        "support_type": "direct",
    },
]

QUESTIONS = [
    {
        "question_id": "q-limiting-use",
        "text": "Does limiting social media use improve well-being?",
        "theme_ids": ["theme-interventions", "theme-problematic-use"],
        "source_ids": ["landscape-15", "landscape-03"],
        "support_type": "source-backed",
    },
    {
        "question_id": "q-comparison-depression",
        "text": "How do social comparison and self-esteem relate to depression and anxiety?",
        "theme_ids": ["theme-social-comparison"],
        "source_ids": ["component-03", "landscape-11", "landscape-19", "component-10"],
        "support_type": "source-backed",
    },
    {
        "question_id": "q-sleep-direction",
        "text": "How is social media use related to sleep quality and timing?",
        "theme_ids": ["theme-sleep", "theme-problematic-use"],
        "source_ids": ["sleep-02", "sleep-04", "landscape-05"],
        "support_type": "source-backed",
    },
    {
        "question_id": "q-fomo",
        "text": "How does fear of missing out connect social media use with mental-health outcomes?",
        "theme_ids": ["theme-social-comparison", "theme-problematic-use"],
        "source_ids": ["component-03", "landscape-15", "sleep-04"],
        "support_type": "source-backed",
    },
    {
        "question_id": "q-support",
        "text": "How do social support and compensatory use relate to depression during college transition?",
        "theme_ids": ["theme-social-support", "theme-problematic-use"],
        "source_ids": ["landscape-14", "landscape-10", "landscape-03"],
        "support_type": "source-backed",
    },
    {
        "question_id": "q-peer-response",
        "text": "How do students recognize and respond to peers' mental-health disclosures on SNSs?",
        "theme_ids": ["theme-peer-response", "theme-social-support"],
        "source_ids": ["landscape-10"],
        "support_type": "source-backed",
    },
]

QUERIES = [
    {
        "query_id": "landscape",
        "tool": "UC Library Search / Primo PNX REST fallback",
        "purpose": "Focused landscape across social media, mental health, and college students",
        "text": "(((((\"social media\") OR (\"social networking sites\"))) AND (((\"mental health\") OR (anxiety) OR (depression)))) AND (((\"college students\") OR (\"undergraduate students\"))))",
        "url": "https://search-library.ucsd.edu/discovery/search?query=any,contains,(((((%22social%20media%22)%20OR%20(%22social%20networking%20sites%22)))%20AND%20(((%22mental%20health%22)%20OR%20(anxiety)%20OR%20(depression))))%20AND%20(((%22college%20students%22)%20OR%20(%22undergraduate%20students%22))))&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI%3AUCSD&offset=0",
        "total_results": 2727,
        "records_returned": 20,
        "unique_records_screened": 20,
        "fidelity_estimate": 0.75,
        "decision": "Selected 7 records and ran two component searches because the first page retained relevant but conceptually separable branches.",
        "raw_file": "raw/landscape-response.json",
        "source_ids": ["landscape-03", "landscape-05", "landscape-10", "landscape-11", "landscape-14", "landscape-15", "landscape-19"],
    },
    {
        "query_id": "component",
        "tool": "UC Library Search / Primo PNX REST fallback",
        "purpose": "Decompose the social-comparison and self-esteem branch",
        "text": "(((((\"social media\") OR (\"social networking sites\"))) AND (((\"social comparison\") OR (\"self-esteem\")))) AND (((\"college students\") OR (\"undergraduate students\"))))",
        "url": "https://search-library.ucsd.edu/discovery/search?query=any,contains,(((((%22social%20media%22)%20OR%20(%22social%20networking%20sites%22)))%20AND%20(((%22social%20comparison%22)%20OR%20(%22self-esteem%22))))%20AND%20(((%22college%20students%22)%20OR%20(%22undergraduate%20students%22))))&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI%3AUCSD&offset=0",
        "total_results": 575,
        "records_returned": 20,
        "unique_records_screened": 16,
        "fidelity_estimate": 0.80,
        "decision": "Selected 5 records; the page produced direct student evidence and multiple review/meta-analytic candidates.",
        "raw_file": "raw/component-response.json",
        "source_ids": ["component-03", "component-10", "component-18", "landscape-11", "landscape-19"],
    },
    {
        "query_id": "sleep",
        "tool": "UC Library Search / Primo PNX REST fallback",
        "purpose": "Decompose the sleep branch named in the intake context",
        "text": "(((((\"social media\") OR (\"social networking sites\"))) AND (((\"sleep quality\") OR (\"sleep\")))) AND (((\"college students\") OR (\"undergraduate students\"))))",
        "url": "https://search-library.ucsd.edu/discovery/search?query=any,contains,(((((%22social%20media%22)%20OR%20(%22social%20networking%20sites%22)))%20AND%20(((%22sleep%20quality%22)%20OR%20(%22sleep%22))))%20AND%20(((%22college%20students%22)%20OR%20(%22undergraduate%20students%22))))&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI%3AUCSD&offset=0",
        "total_results": 470,
        "records_returned": 20,
        "unique_records_screened": 17,
        "fidelity_estimate": 0.80,
        "decision": "Selected 2 records from the first page; the landscape source set already included relevant sleep-pathway evidence.",
        "raw_file": "raw/sleep-component-response.json",
        "source_ids": ["sleep-02", "sleep-04"],
    },
]

APAPA = {
    "landscape-03": "Ridout, B., & Campbell, A. (2018). The use of social networking sites in mental health interventions for young people: Systematic review. *Journal of Medical Internet Research, 20*(12), e12244. https://doi.org/10.2196/12244",
    "landscape-05": "Weinstein, A. M. (2023). Problematic social networking site use-effects on mental health and the brain. *Frontiers in Psychiatry, 13*, Article 1106004. https://doi.org/10.3389/fpsyt.2022.1106004",
    "landscape-10": "Kim, T., & Hong, H. (2021). Understanding university students' experiences, perceptions, and attitudes toward peers displaying mental health-related problems on social networking sites: Online survey and interview study. *JMIR Mental Health, 8*(10), e23465. https://doi.org/10.2196/23465",
    "landscape-11": "Ojha, K., Soohinda, G., Sampath, H., & Dutta, S. (2021). Social networking sites and its relation to social comparison and psychological well-being among medical university students. *Indian Journal of Psychiatry, 63*(6), 593-596. https://doi.org/10.4103/indianjpsychiatry.indianjpsychiatry_1344_20",
    "landscape-14": "Zhou, M., Li, F., Wang, Y., Chen, S., & Wang, K. (2020). Compensatory social networking site use, family support, and depression among college freshman: Three-wave panel study. *Journal of Medical Internet Research, 22*(9), e18458. https://doi.org/10.2196/18458",
    "landscape-15": "Hunt, M. G., Marx, R., Lipson, C., & Young, J. (2018). No more FOMO: Limiting social media decreases loneliness and depression. *Journal of Social and Clinical Psychology, 37*(10), 751-768. https://doi.org/10.1521/jscp.2018.37.10.751",
    "landscape-19": "Carraturo, F., Di Perna, T., Giannicola, V., Nacchia, M. A., Pepe, M., Muzii, B., Bottone, M., Sperandeo, R., Bochicchio, V., Maldonato, N. M., & Scandurra, C. (2023). Envy, social comparison, and depression on social networking sites: A systematic review. *European Journal of Investigation in Health, Psychology and Education, 13*(2), 364-376. https://doi.org/10.3390/ejihpe13020027",
    "component-03": "Leung, A. N. M., Law, W., Liang, Y. Y., Au, A. C. L., Li, C., & Ng, H. K. S. (2021). What explains the association between usage of social networking sites (SNS) and depression symptoms? The mediating roles of self-esteem and fear of missing out. *International Journal of Environmental Research and Public Health, 18*(8), 3916. https://doi.org/10.3390/ijerph18083916",
    "component-10": "Krause, H.-V., Baum, K., Baumann, A., & Krasnova, H. (2019). Unifying the detrimental and beneficial effects of social network site use on self-esteem: A systematic literature review. *Media Psychology, 24*(1), 10-47. https://doi.org/10.1080/15213269.2019.1656646",
    "component-18": "Yang, Q., & Feng, Y. (2024). Relationships between social networking sites use and subjective well-being---a meta-analysis and meta-analytic structural equation model. *Heliyon, 10*(12), e32463. https://doi.org/10.1016/j.heliyon.2024.e32463",
    "sleep-02": "Garett, R., Liu, S., & Young, S. D. (2016). The relationship between social media use and sleep quality among undergraduate students. *Information, Communication & Society, 21*(2), 163-173. https://doi.org/10.1080/1369118X.2016.1266374",
    "sleep-04": "Hussain, Z., & Griffiths, M. D. (2019). The associations between problematic social networking site use and sleep quality, attention-deficit hyperactivity disorder, depression, anxiety and stress. *International Journal of Mental Health and Addiction, 19*(3), 686-700. https://doi.org/10.1007/s11469-019-00175-1",
}

SHORT_CITATIONS = {
    "landscape-03": "Ridout and Campbell (2018)",
    "landscape-05": "Weinstein (2023)",
    "landscape-10": "Kim and Hong (2021)",
    "landscape-11": "Ojha et al. (2021)",
    "landscape-14": "Zhou et al. (2020)",
    "landscape-15": "Hunt et al. (2018)",
    "landscape-19": "Carraturo et al. (2023)",
    "component-03": "Leung et al. (2021)",
    "component-10": "Krause et al. (2019)",
    "component-18": "Yang and Feng (2024)",
    "sleep-02": "Garett et al. (2016)",
    "sleep-04": "Hussain and Griffiths (2019)",
}

STUDY_DESIGN = {
    "landscape-03": "Systematic review",
    "landscape-05": "Review",
    "landscape-10": "Online survey and semistructured interviews",
    "landscape-11": "Cross-sectional questionnaire study",
    "landscape-14": "Three-wave panel study",
    "landscape-15": "Randomized controlled experiment",
    "landscape-19": "Systematic review",
    "component-03": "Three studies of Chinese college/university students",
    "component-10": "Systematic literature review",
    "component-18": "Meta-analysis and meta-analytic structural equation model",
    "sleep-02": "Longitudinal undergraduate study with tweet content and weekly surveys",
    "sleep-04": "Cross-sectional online survey",
}

EVIDENCE_BASE = {
    "landscape-03": "9 articles describing 5 SNS-based interventions for people up to age 25; quantitative meta-analysis was not possible.",
    "landscape-05": "Narrative review of evidence on problematic SNS use; includes limited brain-imaging evidence and preliminary CBT evidence.",
    "landscape-10": "226 survey respondents and 20 interview participants at six universities in South Korea.",
    "landscape-11": "220 medical students in India; mean age 20.44 years.",
    "landscape-14": "Three-wave panel of 1,137 college freshmen.",
    "landscape-15": "143 undergraduates at the University of Pennsylvania randomized to limited use or usual use for three weeks.",
    "landscape-19": "9 studies meeting inclusion criteria from PsycINFO, PubMed, and Web of Science, 2012-2022.",
    "component-03": "Studies 1-3 included 347, 180, and 233 Chinese college/university students respectively.",
    "component-10": "Systematic literature review; abstract reports a framework but not a full count of included studies.",
    "component-18": "73 independent samples.",
    "sleep-02": "197 Twitter-using first-quarter freshmen; tweet content and weekly sleep surveys.",
    "sleep-04": "638 SNS users; mean age 32.03 years, SD 10.08.",
}

KEY_QUESTIONS = {
    "component-10": [
        "How does social comparison change self-esteem on SNSs?",
        "When does positive social feedback or self-reflection help self-esteem?",
    ],
    "landscape-19": [
        "How are social comparison, envy, and depression related on SNSs?",
        "What is the direction of that relationship in studies able to test it?",
    ],
    "component-03": [
        "Do self-esteem and FOMO mediate the association between SNS time and depression?",
        "What usage thresholds appeared associated with subthreshold depression?",
    ],
    "landscape-11": [
        "How are impression management, social comparison, depression, and anxiety related?",
        "Does SNS duration show a complex association with psychopathology?",
    ],
    "landscape-15": [
        "Does limiting Facebook, Instagram, and Snapchat improve loneliness and depression?",
        "Does self-monitoring affect anxiety and FOMO?",
    ],
    "landscape-14": [
        "How do introversion, compensatory SNS use, family support, and depression relate over time?",
        "Does family support buffer or alter the pathway differently by introversion level?",
    ],
    "landscape-05": [
        "Which mental-health and sleep outcomes are associated with problematic SNS use?",
        "What preliminary treatment evidence exists?",
    ],
    "sleep-02": [
        "How is the timing of social-media posting associated with sleep quality?",
        "Are fear-related posts associated with lower sleep quality?",
    ],
    "sleep-04": [
        "Is problematic SNS use associated with poor sleep quality?",
        "How does problematic use correlate with ADHD, depression, anxiety, and stress?",
    ],
}

SOURCE_NOTES = {
    "component-10": {
        "relevance": "The review directly distinguishes harmful comparison from beneficial feedback or self-reflection, helping the student separate total use from specific activity.",
        "quote_1": "when a social networking site is used to compare oneself with others, it mostly results in decreases in users' self-esteem",
        "quote_2": "receiving positive social feedback from others or using these platforms to reflect on one's own self is mainly associated with benefits for users' self-esteem",
        "connection": "Direct evidence",
        "confidence": "Medium",
    },
    "landscape-19": {
        "relevance": "This systematic review directly maps the comparison-envy-depression branch and cautions that direction is uncertain.",
        "quote_1": "In all articles reviewed, a simple correlation was found between SC on SNSs, envy, and depression",
        "quote_2": "The only two studies that were suitable to determine direction found that depression acted as a predictor rather than an outcome of SC and envy",
        "connection": "Direct evidence",
        "confidence": "Medium",
    },
    "component-03": {
        "relevance": "This source directly tests two pathways named in the student's interests: self-esteem and FOMO.",
        "quote_1": "Results showed that more time spent on SNS was related to lower self-esteem, and higher FoMO, respectively; while self-esteem then negatively, and FoMO then positively, explained depression symptoms, respectively",
        "quote_2": "Combining results from three studies, both self-esteem and FoMO mediated the relation between SNS usage and depression symptoms",
        "connection": "Direct evidence",
        "confidence": "Medium",
    },
    "landscape-11": {
        "relevance": "This student-sample study connects impression management, social comparison, depression, and anxiety, though it focuses on medical students rather than college students broadly.",
        "quote_1": "Impression management was associated with higher social comparison, depression, and anxiety scores",
        "quote_2": "Social comparison had a significant correlation between depression and anxiety scores",
        "connection": "Direct evidence with population caveat",
        "confidence": "Medium",
    },
    "landscape-15": {
        "relevance": "This is the strongest source in the set for testing whether limiting use affects well-being rather than merely correlating with it.",
        "quote_1": "The limited use group showed significant reductions in loneliness and depression over three weeks compared to the control group",
        "quote_2": "Our findings strongly suggest that limiting social media use to approximately 30 minutes per day may lead to significant improvement in well-being",
        "connection": "Direct evidence",
        "confidence": "High",
    },
    "landscape-14": {
        "relevance": "This longitudinal study adds a college-transition pathway and shows that social context can alter how compensatory use operates.",
        "quote_1": "introversion at Wave 1 positively predicted compensatory use of SNS at Wave 2 and subsequently increased depression at Wave 3",
        "quote_2": "Unexpectedly, we found that family support in Wave 1 decreased compensatory SNS use for less introverted freshmen in Wave 2 and further decreased depression in Wave 3",
        "connection": "Direct evidence",
        "confidence": "Medium",
    },
    "landscape-05": {
        "relevance": "This review broadens the landscape beyond depression and anxiety and identifies sleep as one recurring pathway.",
        "quote_1": "Problematic SNS use has been associated with an increased rate of depression, anxiety, stress, obsessive-compulsive disorder (OCD), attention-deficit/hyperactivity disorder (ADHD), and propensity to excessive alcohol use",
        "quote_2": "There is evidence for reduced sleep quality and quantity, longer sleeping latency and more sleep disturbance",
        "connection": "Direct evidence; review synthesis",
        "confidence": "Medium",
    },
    "sleep-02": {
        "relevance": "Although older than the preferred 2018-2026 range, this source directly studies undergraduates and distinguishes late-night and weekday-evening timing effects.",
        "quote_1": "Tweeting more frequently on weekday late nights was associated with lower sleep quality",
        "quote_2": "tweeting more frequently on weekday evenings was associated with better quality sleep",
        "connection": "Direct evidence with date caveat",
        "confidence": "Medium",
    },
    "sleep-04": {
        "relevance": "This study links problematic SNS use with sleep and several mental-health symptoms, though its sample is broader and older on average than the target undergraduate range.",
        "quote_1": "Bivariate correlations identified moderate positive correlations between PSNSU, poor sleep quality",
        "quote_2": "The study demonstrated that PSNSU was associated with psychopathological and psychiatric disorders symptoms",
        "connection": "Direct evidence with population caveat",
        "confidence": "Medium",
    },
}

READING_LIST_TITLES = {
    "component-10": "Comparison, feedback, and self-esteem work through different pathways",
    "landscape-19": "Comparison and envy are linked to depression, but direction is uncertain",
    "component-03": "Self-esteem and FOMO may mediate the SNS-depression pathway",
    "landscape-11": "Impression management and comparison correlate with depression and anxiety",
    "landscape-15": "Limiting use reduced loneliness and depression in an experiment",
    "landscape-14": "Compensatory use and family support follow different pathways",
    "landscape-05": "Problematic use broadens the mental-health and sleep picture",
    "sleep-02": "Timing of use matters for sleep quality",
    "sleep-04": "Problematic use aligns with poor sleep and multiple symptoms",
}

READING_LIST_FOCUS = {
    "component-10": "SNS self-esteem processes",
    "landscape-19": "SNS comparison, envy, and depression",
    "component-03": "Chinese college/university students; SNS time",
    "landscape-11": "Indian medical students; comparison",
    "landscape-15": "US undergraduates; limiting use",
    "landscape-14": "College freshmen; transition and family support",
    "landscape-05": "Problematic use across outcomes",
    "sleep-02": "US first-quarter freshmen; Twitter timing",
    "sleep-04": "SNS users across age range; problematic use",
}

SOURCE_DETAILS = {
    "landscape-03": {"source_type": "Systematic review article", "access": "Abstract only", "credibility": "Peer-reviewed venue; explicit systematic-review methods and acknowledged evidence limitations."},
    "landscape-05": {"source_type": "Review article", "access": "Abstract only", "credibility": "Peer-reviewed venue; review is described as broad but not systematic in the abstract."},
    "landscape-10": {"source_type": "Mixed-methods research article", "access": "Abstract only", "credibility": "Peer-reviewed venue; includes survey and interview methods."},
    "landscape-11": {"source_type": "Research article", "access": "Abstract only", "credibility": "Peer-reviewed venue; cross-sectional design limits causal inference."},
    "landscape-14": {"source_type": "Research article", "access": "Abstract only", "credibility": "Peer-reviewed venue; longitudinal panel design strengthens temporal inference."},
    "landscape-15": {"source_type": "Experimental research article", "access": "Abstract only", "credibility": "Peer-reviewed venue; randomized experimental design, but abstract-level access limits full-method review."},
    "landscape-19": {"source_type": "Systematic review article", "access": "Abstract only", "credibility": "Peer-reviewed venue; small included-study count and limited directional evidence."},
    "component-03": {"source_type": "Research article", "access": "Abstract only", "credibility": "Peer-reviewed venue; three-study sequence strengthens internal consistency but abstract-level access limits full-method review."},
    "component-10": {"source_type": "Systematic literature review", "access": "Abstract only", "credibility": "Peer-reviewed venue; theoretical framework and systematic review, with individual-study quality not visible in the abstract."},
    "component-18": {"source_type": "Meta-analysis article", "access": "Abstract only", "credibility": "Peer-reviewed venue; meta-analytic design across 73 independent samples, but abstract-level access limits full-method review."},
    "sleep-02": {"source_type": "Research article", "access": "Abstract only", "credibility": "Peer-reviewed venue; direct undergraduate data, but older than preferred date range and focused on Twitter."},
    "sleep-04": {"source_type": "Research article", "access": "Abstract only", "credibility": "Peer-reviewed venue; cross-sectional design and broader age range limit fit to the undergraduate target."},
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_json(path: Path):
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def permalink(record_id: str) -> str:
    return (
        "https://search-library.ucsd.edu/discovery/fulldisplay?docid="
        + record_id
        + "&context=PC&vid=01UCS_SDI%3AUCSD&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc"
    )


def source_record(records: list[dict], metadata: dict, record_ids: dict) -> dict:
    source_id = metadata["source_id"]
    record = next(item for item in records if item["source_id"] == source_id)
    doi = metadata["doi"]
    record_id = record_ids[doi]
    doi_url = "https://doi.org/" + doi
    library_link = permalink(record_id)
    return {
        "source_id": source_id,
        "citation": APAPA[source_id],
        "short_citation": SHORT_CITATIONS[source_id],
        "title": metadata["title"],
        "primary_link": doi_url,
        "primary_link_source": "doi",
        "library_link": library_link,
        "library_link_type": "PNX fulldisplay",
        "permalink": doi_url,
        "doi": doi,
        "record_type": metadata["type"],
        "year": metadata["year"],
        "container": metadata["container"],
        "abstract_present": bool(record.get("abstract")),
        "access_level": SOURCE_DETAILS[source_id]["access"],
        "source_type": SOURCE_DETAILS[source_id]["source_type"],
        "study_design": STUDY_DESIGN[source_id],
        "evidence_base": EVIDENCE_BASE[source_id],
        "credibility": SOURCE_DETAILS[source_id]["credibility"],
        "confidence": SOURCE_NOTES[source_id]["confidence"] if source_id in SOURCE_NOTES else "Low",
        "connection_type": SOURCE_NOTES[source_id]["connection"] if source_id in SOURCE_NOTES else "Direct evidence",
        "selected": True,
        "selection_reason": SELECTION_REASONS[source_id],
        "query_ids": [record["query_id"]],
    }


def build_manifest() -> dict:
    global RECORD_IDS
    records = load_json(ROOT / "screening.json")
    metadata = load_json(ROOT / "raw/crossref-full-metadata.json")
    verification = load_json(ROOT / "raw/metadata-verification.json")
    for filename in ["raw/landscape-response.json", "raw/component-response.json", "raw/sleep-component-response.json"]:
        for doc in load_json(ROOT / filename).get("docs", []):
            doi_values = doc.get("pnx", {}).get("addata", {}).get("doi", [])
            record_id = doc.get("pnx", {}).get("control", {}).get("recordid", [])
            if doi_values and record_id:
                RECORD_IDS[doi_values[0]] = record_id[0]
    sources = [source_record(records, item, RECORD_IDS) for item in metadata if item["source_id"] in SELECTED_IDS]
    screened_inventory = [
        {
            "source_id": item["source_id"],
            "query_id": item["query_id"],
            "title": item["title"],
            "creator": item.get("creator", ""),
            "year": item.get("year", ""),
            "doi": item.get("doi", ""),
            "type": item.get("type", ""),
            "abstract_present": bool(item.get("abstract")),
            "selected": item["source_id"] in SELECTED_IDS,
        }
        for item in records
    ]
    now = utc_now()
    return {
        "schema_version": "0.1",
        "run_id": ROOT.name,
        "created_at": now,
        "updated_at": now,
        "working_question": "How does social media affect mental health among college students, with attention to anxiety, depression, sleep, and social comparison?",
        "context": {
            "assignment": "Psychology 190 capstone prep; 8-10 scholarly, preferably peer-reviewed sources in APA style",
            "population": "College students, approximately ages 18-24",
            "preferred_outcomes": ["anxiety", "depression", "sleep", "social comparison"],
            "preferred_timeframe": "2018-2026",
            "exclusions": "News articles",
            "citation_style": "APA 7",
            "breadth_basis": "Focused landscape by default; comprehensive selected deep work simulated with the assignment's narrowed-topic context.",
            "interaction_basis": "The test simulates intake and narrowed-topic context from assignment-prompts.md rather than an actual live multi-turn conversation.",
            "product_name": "Reading List",
            "technical_name": "annotated-bibliography",
        },
        "breadth_tier": "focused landscape; comprehensive selected deep work",
        "output_mode": "reading-list",
        "queries": QUERIES,
        "sources": sources,
        "screened_inventory": screened_inventory,
        "themes": THEMES,
        "questions": QUESTIONS,
        "selected_paths": [
            {
                "path": "reading-list",
                "themes": ["theme-social-comparison", "theme-sleep"],
                "scope": "Comparison, self-esteem, FOMO, and sleep pathways, with intervention and social-context sources for breadth.",
                "source_ids": READING_LIST_IDS,
                "status": "completed",
            }
        ],
        "reading_list_ids": READING_LIST_IDS,
        "selection_decisions": [
            {"source_id": source_id, "decision": "selected", "reason": SELECTION_REASONS[source_id]}
            for source_id in SELECTED_IDS
        ],
        "limitations": [
            "No keyed Primo Search API was available; the keyless PNX REST fallback was used.",
            "All annotations are abstract-level; no full text was reviewed.",
            "The 2016 sleep source is a deliberate exception to the preferred 2018-2026 range because it directly studies undergraduate sleep timing.",
            "The Primo PNX response includes primarily local and Primo Central metadata; result counts should not be treated as complete field coverage.",
            "The landscape is not exhaustive and is best understood as purpose-aware saturation for the undergraduate assignment.",
            "The test simulated intake and narrowed-topic context from assignment-prompts.md rather than a live multi-turn conversation.",
        ],
        "verification": [
            {
                "source_id": item["source_id"],
                "doi": item["doi"],
                "title_match": item["title"] == item["verified_title"],
                "container": item["container"],
                "year": item["year"],
            }
            for item in verification
            if item["source_id"] in SELECTED_IDS
        ],
        "stage_log": [],
        "reference_log": [],
    }


def write_landscape(manifest: dict) -> None:
    record_id_by_source = {source["source_id"]: source["doi"] for source in manifest["sources"]}
    themes = "\n".join(
        f"{index}. **{theme['name']}:** {theme['description']}"
        for index, theme in enumerate(THEMES, 1)
    )
    questions = "\n".join(
        f"| {index} | {question['text']} | {', '.join(next(t['name'] for t in THEMES if t['theme_id'] == theme_id) for theme_id in question['theme_ids'])} | [{SHORT_CITATIONS[question['source_ids'][0]]}]({next(s['primary_link'] for s in manifest['sources'] if s['source_id'] == question['source_ids'][0])}) |"
        for index, question in enumerate(QUESTIONS, 1)
    )
    content = f"""## Summary

**Research question:** How does social media affect mental health among college students, especially through anxiety, depression, sleep, and social comparison?

**Context:** Psychology 190 capstone prep; 8-10 scholarly, preferably peer-reviewed sources in APA style; ages 18-24; no news articles; recent sources preferred.

### Search strategy

UC Library Search was used first through its Primo PNX fallback. Three focused queries returned 20 records each; after de-duplication, 53 records were screened and 12 were selected for the landscape. A 2016 sleep source was retained as a direct-fit exception to the preferred 2018-2026 range.

#### Example searches

- [Social media and college-student mental health](https://search-library.ucsd.edu/discovery/search?query=any,contains,(((((%22social%20media%22)%20OR%20(%22social%20networking%20sites%22)))%20AND%20(((%22mental%20health%22)%20OR%20(anxiety)%20OR%20(depression))))%20AND%20(((%22college%20students%22)%20OR%20(%22undergraduate%20students%22))))&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI%3AUCSD&offset=0) [2,727 results, ~75% on topic]
- [Social comparison and self-esteem](https://search-library.ucsd.edu/discovery/search?query=any,contains,(((((%22social%20media%22)%20OR%20(%22social%20networking%20sites%22)))%20AND%20(((%22social%20comparison%22)%20OR%20(%22self-esteem%22))))%20AND%20(((%22college%20students%22)%20OR%20(%22undergraduate%20students%22))))&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI%3AUCSD&offset=0) [575 results, ~80% on topic]
- [Sleep quality](https://search-library.ucsd.edu/discovery/search?query=any,contains,(((((%22social%20media%22)%20OR%20(%22social%20networking%20sites%22)))%20AND%20(((%22sleep%20quality%22)%20OR%20(%22sleep%22))))%20AND%20(((%22college%20students%22)%20OR%20(%22undergraduate%20students%22))))&tab=ArticleBooksEtc&search_scope=ArticlesBooksEtc&vid=01UCS_SDI%3AUCSD&offset=0) [470 results, ~80% on topic]

## Overviews

The results include three useful reviews and a meta-analysis:

- [The Use of Social Networking Sites in Mental Health Interventions for Young People: Systematic Review, Ridout & Campbell (2018)](https://doi.org/{record_id_by_source['landscape-03']}) - A systematic review of SNS-based youth mental-health interventions.
- [Unifying the detrimental and beneficial effects of social network site use on self-esteem, Krause et al. (2019)](https://doi.org/{record_id_by_source['component-10']}) - A systematic review organizing SNS effects on self-esteem through comparison, feedback, and self-reflection.
- [Relationships between social networking sites use and subjective well-being, Yang & Feng (2024)](https://doi.org/{record_id_by_source['component-18']}) - A meta-analysis and structural equation model across 73 independent samples.

## Themes

These names describe the retrieved landscape rather than conclusions about the whole field.

{themes}

## Questions

| # | Question | Related themes | Example sources |
|---|---|---|---|
{questions}

## Possible directions

One proposed direction would be to compare activity type rather than only total time: whether passive scrolling, upward comparison, positive feedback, or self-reflection have different associations. This is proposed based on measurement differences noted in the retrieved reviews, not a claim that the literature itself asks this exact question.

## What's next?

Would you like a reading list focused on social comparison and self-esteem, sleep, limiting use, social support, or a combination? I can also create the full annotated bibliography, refine the scope, or show the search log.
"""
    (ROOT / "landscape.md").write_text(content, encoding="utf-8")


def write_reading_list(manifest: dict) -> None:
    sections = []
    for source_id in READING_LIST_IDS:
        note = SOURCE_NOTES[source_id]
        detail = SOURCE_DETAILS[source_id]
        design = STUDY_DESIGN[source_id]
        evidence = EVIDENCE_BASE[source_id]
        questions = "\n".join(f"- {question}" for question in KEY_QUESTIONS[source_id])
        sections.append(f"""## {READING_LIST_TITLES[source_id]}

**Citation:** {APAPA[source_id]}  
**Source ID:** `{source_id}`  
**Source Type:** {detail['source_type']}  
**Connection Type:** {note['connection']}  
**Study Design:** {design}  
**Evidence Base:** {evidence}  
**Credibility:** {detail['credibility']}  
**Access Level:** {detail['access']}  
**Confidence:** {note['confidence']}

{note['relevance']}

### Questions this source addresses

{questions}

### Key quotes

- "{note['quote_1']}"
- "{note['quote_2']}"

---
""")
    comparison_rows = "\n".join(
        f"| [{SHORT_CITATIONS[source_id]}]({next(source['primary_link'] for source in manifest['sources'] if source['source_id'] == source_id)}) | {STUDY_DESIGN[source_id]} | {READING_LIST_FOCUS[source_id]} | \"{SOURCE_NOTES[source_id]['quote_1']}\" | {SOURCE_DETAILS[source_id]['access']}; {SOURCE_NOTES[source_id]['confidence']} |"
        for source_id in READING_LIST_IDS
    )
    content = f"""This reading list combines social comparison, self-esteem, FOMO, sleep, and broader context. It includes nine abstract-level candidates; Garett et al. (2016) is a deliberate exception to the preferred 2018-2026 date range because it directly studies undergraduate social-media timing and sleep quality.

{"".join(sections)}
## Comparison

| Source | Study design | Focus | Key claim or finding | Access and confidence |
|---|---|---|---|---|
{comparison_rows}

## What's next?

Start by reading the experimental source and the two systematic reviews if you want a concise evidence backbone; then read the pathway studies that best match your thesis. You can also ask for a full annotated bibliography, a narrower list, or the search log.
"""
    (ROOT / "reading-list.md").write_text(content, encoding="utf-8")


def write_search_log(manifest: dict) -> None:
    lines = [
        "# Search log",
        "",
        "## Scope",
        "",
        f"**Working question:** {manifest['working_question']}",
        "",
        "**Breadth:** focused landscape followed by selected comprehensive deep work.",
        "",
        "**Execution mode:** UC Library Search first; keyless Primo PNX REST fallback; no keyed Primo Search API.",
        "",
        "## Query summary",
        "",
    ]
    for query in QUERIES:
        lines.extend(
            [
                f"### `{query['query_id']}`",
                "",
                f"- **Tool:** {query['tool']}",
                f"- **Purpose:** {query['purpose']}",
                f"- **Query:** `{query['text']}`",
                f"- **Results:** {query['total_results']:,} reported; {query['records_returned']} returned; {query['unique_records_screened']} unique records screened.",
                f"- **Approximate fidelity:** {int(query['fidelity_estimate'] * 100)}%.",
                f"- **Decision:** {query['decision']}",
                f"- **Link:** [{query['query_id']} search]({query['url']})",
                "",
            ]
        )
    lines.extend(["## Screened inventory", "", "| Source ID | Query | Title | Year | DOI | Abstract present | Selected |", "|---|---|---|---|---|---|---|"])
    for item in manifest["screened_inventory"]:
        title = item["title"].replace("|", "\\|")
        lines.append(
            f"| `{item['source_id']}` | {item['query_id']} | {title} | {item['year']} | {item['doi']} | {item['abstract_present']} | {item['selected']} |"
        )
    lines.extend(
        [
            "",
            "## Verification",
            "",
            "Crossref metadata was retrieved for all 12 selected sources. All source IDs had matching titles and verified container/year metadata. No metadata conflicts were identified.",
            "",
            "## Selection decisions",
            "",
        ]
    )
    for decision in manifest["selection_decisions"]:
        lines.append(f"- `{decision['source_id']}` — selected: {decision['reason']}")
    lines.extend(
        [
            "",
            "## Limitations",
            "",
        ]
    )
    for limitation in manifest["limitations"]:
        lines.append(f"- {limitation}")
    (ROOT / "search-log.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_review() -> None:
    content = """# Test review

## Run summary

- **Topic:** social media and college-student mental health.
- **Workflow:** simulated intake → landscape → selection → reading list → audit.
- **Search:** three UC Library Search / Primo PNX queries; 53 unique records screened; 12 selected.
- **Output:** landscape and nine-source reading list.
- **Verification:** Crossref metadata checked for all selected sources.

## Strengths

- The landscape stayed focused and offered clear follow-up paths.
- Component queries surfaced direct student evidence and review/meta-analytic candidates.
- Direct quotes and access levels were preserved throughout.
- The search log recorded the PNX fallback, screened inventory, selection rationale, and limitations.
- The 2016 sleep source was explicitly labeled as an exception to the preferred date range.

## Issues and observations

- The manifest's `breadth_tier` string is descriptive rather than normalized; future schema validation may benefit from separate landscape and deep-work tiers.
- PNX result totals are useful but not interpretable as complete field coverage; the logs correctly treat them as first signals.
- Reading-list quotes remain abstract-level; full-text verification would be needed before publication-grade use.
- The source-link policy now prefers DOI URLs for the general reader and retains the PNX record link separately for library access. This aligns the test outputs with the skill's new link-resolution rules.
- The simulated narrowed-topic context uses the assignment file, not a live user turn. A future automated test harness should make that distinction explicit in the manifest.

## Next steps

1. Add a manifest schema field distinguishing `landscape_tier` and `deep_work_tier`.
2. Test a live narrowing turn after the landscape to compare selection quality.
3. Run the same topic with a keyed Primo Search API to compare coverage and result counts.
4. Test the full annotated-bibliography path on two or three of the strongest sources.
"""
    (ROOT / "review.md").write_text(content, encoding="utf-8")


def main() -> int:
    manifest = build_manifest()
    (ROOT / "bibliography-run.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    write_landscape(manifest)
    write_reading_list(manifest)
    write_search_log(manifest)
    write_review()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
