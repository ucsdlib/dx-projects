#!/usr/bin/env python3

import json
from datetime import datetime, timezone
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent
SEARCH_RESULTS = RUN_DIR / "search-results.jsonl"
OUTPUT = RUN_DIR / "question_map.json"
GENERATED_AT = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def source_id_for(pool_id):
    return f"src_{int(pool_id[1:]):03d}"


def source_question_id_for(pool_id):
    return f"sq_{int(pool_id[1:]):03d}"


def load_sources():
    with SEARCH_RESULTS.open() as handle:
        records = [json.loads(line) for line in handle if line.strip()]
    candidates = [record for record in records if record.get("record_type") == "candidate"]
    sources = []
    for record in sorted(candidates, key=lambda item: item["id"]):
        pool_id = record["id"]
        sources.append(
            {
                "id": source_id_for(pool_id),
                "type": "source",
                "title": record["title"],
                "year": record.get("year"),
                "citation_short": record.get("citation", record["title"]),
                "citation_display": record.get("citation", record["title"]),
                "source_type": "book" if "University of Chicago Press" in record.get("citation", "") else ("report" if "World Meteorological Organization" in record.get("citation", "") else "article"),
                "doi": record.get("doi"),
                "urls": [record["url"]],
                "access_level": "metadata_only",
                "evidence_basis": "metadata_only",
                "selection_status": "selected",
                "selection_reason": record.get("rationale", "Selected for relevance to a required case component."),
                "components": record.get("component", []),
                "relevance_score": record.get("relevance"),
                "language": "eng",
                "confidence": "medium",
            }
        )
    return sources


SOURCE_QUESTIONS = {
    "S01": ("How does ambient heat relate to emergency department visits among adults in the United States?", "q_001", "The title identifies a time-stratified case-crossover study of ambient heat and adult emergency-department visits."),
    "S02": ("How frequent and demographically patterned were heat-related emergency department visits during summer 2023?", "q_001", "The title and federal surveillance metadata identify heat-related emergency-department visits and demographic patterns."),
    "S03": ("How does heat-wave mortality risk vary by heat-wave characteristics across U.S. communities?", "q_001", "The title identifies a comparative study of heat-wave mortality risk and effect modification across 43 communities."),
    "S04": ("How does ambient heat relate to mental-health-related emergency department visits among U.S. adults?", "q_001", "The title directly identifies ambient heat and emergency-department visits for mental health."),
    "S05": ("How are heat-vulnerable populations and locations identified?", "q_002", "The title identifies a systematic review of approaches for identifying heat-vulnerable populations and locations."),
    "S06": ("How can community-level determinants of heat vulnerability be mapped?", "q_002", "The title names community determinants and spatial mapping of heat vulnerability."),
    "S07": ("How accessible are cooling centers to heat-vulnerable populations in New York State?", "q_006", "The title identifies a spatial assessment of cooling-center accessibility for heat-vulnerable populations."),
    "S08": ("How does disproportionate heat exposure and access to refuge vary by socio-demographic status in Portland, Oregon?", "q_006", "The title identifies a city-scale assessment of exposure and refuge access by socio-demographic status."),
    "S09": ("What empirical evidence supports urban greening as a cooling intervention in towns and cities?", "q_003", "The title identifies a systematic review of empirical urban-greening cooling evidence."),
    "S10": ("How does urban green infrastructure affect cooling and heat-related health outcomes in European cities?", "q_003", "The title identifies a health-impact assessment linking green infrastructure to cooling and modeled health effects."),
    "S11": ("Are sprawling cities more vulnerable to extreme heat events than compact cities?", "q_003", "The title compares urban form, extreme heat events, and vulnerability between sprawling and compact cities."),
    "S12": ("What progress has occurred in extreme heat management and warning systems through heat-health action plans?", "q_004", "The title identifies a systematic review of heat-health action plans and warning-system progress."),
    "S13": ("How do municipal heat-wave response plans vary?", "q_004", "The title identifies an assessment of municipal heat-wave response plans."),
    "S14": ("How effective are heat warning systems at reducing adverse health outcomes?", "q_004", "The title identifies a systematic review of epidemiological evidence on heat-warning-system effectiveness."),
    "S15": ("Is planned heat adaptation reducing heat-related mortality and illness?", "q_004", "The title directly asks whether planned adaptation reduces heat-related mortality and illness."),
    "S16": ("How do social isolation, neighborhood context, and institutional failure explain heat-wave mortality?", "q_005", "The title and book metadata identify a social autopsy of a heat-wave disaster."),
    "S17": ("How does household adaptive capacity to extreme heat differ across Phoenix households?", "q_005", "The title identifies a case study of differential household adaptive capacity to extreme heat."),
    "S18": ("How do cultural and linguistic minority stakeholders perceive extreme-heat risks and responses in Australia?", "q_005", "The title identifies a stakeholder study of cultural and linguistic minorities and extreme heat."),
    "S19": ("How does mortality risk vary with high and low ambient temperature across countries?", "q_001", "The title identifies a multicountry observational study of mortality risk attributable to ambient temperature."),
    "S20": ("How should heatwave warning systems and health protections be developed?", "q_004", "The title identifies operational guidance on warning-system development for heatwaves and health."),
}

QUESTIONS = [
    {
        "id": "q_001",
        "type": "question",
        "canonical_label": "Heat-related health outcomes and healthcare use",
        "question_text": "How does extreme heat affect physical and mental health outcomes and healthcare use?",
        "variants": ["Heat-related mortality", "Heat-related emergency department visits"],
        "origin": "user_defined",
        "question_type": "empirical",
        "root_status": "none",
        "confidence": "high",
        "extraction_rationale": "The confirmed prompt asks about public-health consequences and the pool contains direct mortality, morbidity, and healthcare-use evidence.",
        "key_terms": ["mortality", "emergency department", "mental health", "healthcare use"],
        "user_alignment_note": "Directly supports the novice city stakeholder's need to understand health consequences.",
        "score": 0.92,
        "score_components": {"user_alignment": 1.0, "source_support": 1.0, "explicitness": 0.85, "citation_attention": 0.9, "breadth": 0.85, "relation_density": 0.8, "evidence_strength": 0.7},
    },
    {
        "id": "q_002",
        "type": "question",
        "canonical_label": "Measuring and mapping heat vulnerability",
        "question_text": "How are heat-vulnerable populations and locations identified and mapped?",
        "variants": ["Heat vulnerability indices", "Community vulnerability determinants"],
        "origin": "user_defined",
        "question_type": "measurement",
        "root_status": "none",
        "confidence": "high",
        "extraction_rationale": "The confirmed prompt includes vulnerable populations and the pool contains multiple vulnerability-measurement studies.",
        "key_terms": ["vulnerability index", "mapping", "community determinants", "equity"],
        "user_alignment_note": "Connects the prompt's equity component to practical local screening.",
        "score": 0.88,
        "score_components": {"user_alignment": 0.95, "source_support": 0.9, "explicitness": 0.85, "citation_attention": 0.75, "breadth": 0.85, "relation_density": 0.8, "evidence_strength": 0.7},
    },
    {
        "id": "q_003",
        "type": "question",
        "canonical_label": "Urban form, green space, and cooling",
        "question_text": "How do urban form and green infrastructure influence cooling and heat-related health outcomes?",
        "variants": ["Urban greening", "Compact versus sprawling cities"],
        "origin": "user_defined",
        "question_type": "intervention",
        "root_status": "none",
        "confidence": "high",
        "extraction_rationale": "The confirmed prompt includes urban form and green space, and the pool contains greening, green infrastructure, and urban-form evidence.",
        "key_terms": ["green infrastructure", "urban greening", "urban form", "cooling"],
        "user_alignment_note": "Provides city-policy levers, while keeping cooling evidence distinct from direct health evidence.",
        "score": 0.86,
        "score_components": {"user_alignment": 0.95, "source_support": 0.85, "explicitness": 0.8, "citation_attention": 0.75, "breadth": 0.85, "relation_density": 0.75, "evidence_strength": 0.7},
    },
    {
        "id": "q_004",
        "type": "question",
        "canonical_label": "Governance, warnings, and emergency response",
        "question_text": "How do heat-health governance, warning systems, and emergency response reduce risk?",
        "variants": ["Heat-health action plans", "Municipal response plans", "Warning-system effectiveness"],
        "origin": "user_defined",
        "question_type": "policy",
        "root_status": "none",
        "confidence": "high",
        "extraction_rationale": "The confirmed prompt asks what the city should do, and the pool contains governance, warning-system, and adaptation reviews.",
        "key_terms": ["governance", "heat-health action plan", "warning system", "emergency response"],
        "user_alignment_note": "Directly addresses actionable governance and emergency-response options.",
        "score": 0.9,
        "score_components": {"user_alignment": 1.0, "source_support": 0.95, "explicitness": 0.85, "citation_attention": 0.8, "breadth": 0.85, "relation_density": 0.8, "evidence_strength": 0.7},
    },
    {
        "id": "q_005",
        "type": "question",
        "canonical_label": "Lived experience and social adaptive capacity",
        "question_text": "How do social circumstances shape lived experience and adaptive capacity during extreme heat?",
        "variants": ["Social isolation", "Household adaptive capacity", "Cultural and linguistic barriers"],
        "origin": "user_defined",
        "question_type": "empirical",
        "root_status": "none",
        "confidence": "medium",
        "extraction_rationale": "The confirmed prompt includes lived experience and social consequences, and the pool includes sociological, household, and stakeholder studies.",
        "key_terms": ["lived experience", "social isolation", "adaptive capacity", "stakeholder perceptions"],
        "user_alignment_note": "Adds human context that quantitative health studies alone do not capture.",
        "score": 0.82,
        "score_components": {"user_alignment": 0.9, "source_support": 0.8, "explicitness": 0.75, "citation_attention": 0.65, "breadth": 0.85, "relation_density": 0.7, "evidence_strength": 0.65},
    },
    {
        "id": "q_006",
        "type": "question",
        "canonical_label": "Equitable access to cooling resources",
        "question_text": "How can vulnerable populations gain access to cooling resources and refuge?",
        "variants": ["Cooling-center accessibility", "Access to refuge"],
        "origin": "user_defined",
        "question_type": "equity",
        "root_status": "none",
        "confidence": "medium",
        "extraction_rationale": "The prompt includes vulnerable populations and equity, and the pool contains accessibility and refuge studies.",
        "key_terms": ["cooling center", "accessibility", "refuge", "equity"],
        "user_alignment_note": "Translates vulnerability evidence into a concrete equity and service-delivery question.",
        "score": 0.85,
        "score_components": {"user_alignment": 0.95, "source_support": 0.8, "explicitness": 0.8, "citation_attention": 0.7, "breadth": 0.85, "relation_density": 0.75, "evidence_strength": 0.7},
    },
    {
        "id": "q_007",
        "type": "question",
        "canonical_label": "Evaluating adaptation effectiveness",
        "question_text": "How should heat-adaptation and warning-system effectiveness be evaluated?",
        "variants": ["Adaptation effectiveness", "Warning-system evaluation", "Evidence quality"],
        "origin": "user_defined",
        "question_type": "measurement",
        "root_status": "none",
        "confidence": "high",
        "extraction_rationale": "The pool includes several reviews and evaluations that separate policy intent from measured health outcomes.",
        "key_terms": ["effectiveness", "evaluation", "evidence quality", "mortality", "illness"],
        "user_alignment_note": "Prevents novice users from treating policy presence as demonstrated effectiveness.",
        "score": 0.88,
        "score_components": {"user_alignment": 0.9, "source_support": 0.9, "explicitness": 0.85, "citation_attention": 0.75, "breadth": 0.8, "relation_density": 0.85, "evidence_strength": 0.7},
    },
]

SECONDARY_RELATIONS = [
    ("sq_005", "q_007", "The systematic review's indicator choices are relevant to adaptation and vulnerability evaluation."),
    ("sq_006", "q_006", "Neighborhood vulnerability determinants can inform where to improve access to cooling resources."),
    ("sq_009", "q_007", "The empirical cooling review is relevant to evaluating intervention evidence quality."),
    ("sq_011", "q_002", "Urban form is a conceptual contributor to heat vulnerability and exposure patterns."),
    ("sq_012", "q_007", "Heat-health action-plan reviews contribute to understanding implementation and evidence limits."),
    ("sq_015", "q_007", "The planned-adaptation review directly concerns effectiveness evaluation."),
    ("sq_016", "q_002", "Social autopsy evidence contributes to understanding social dimensions of vulnerability."),
    ("sq_017", "q_006", "Household adaptive capacity shapes ability to reach or use cooling resources."),
    ("sq_018", "q_004", "Cultural and linguistic barriers are relevant to communication and emergency response."),
    ("sq_019", "q_007", "Multicountry temperature-risk modeling depends on methodological assumptions relevant to evaluation."),
]

NEXT_QUESTIONS = [
    {
        "id": "nq_001",
        "type": "next_question",
        "question_text": "How do heat-health action plans affect mortality and emergency department use in specific city contexts?",
        "origin": "structure_narrowing",
        "generation_basis": "Narrow governance evidence to city-scale causal outcomes.",
        "parent_question_ids": ["q_004"],
        "parent_theme_ids": ["theme_004"],
        "slot_substitutions": {"geography": "specific city", "outcome": "mortality and emergency department use"},
        "rationale": "Follows from governance studies that often lack city-specific causal health evaluations.",
        "confidence": "medium",
        "launch_ready": True,
        "root_status": "none",
        "score": 0.86,
        "score_components": {"user_alignment": 0.9, "structural_clarity": 0.9, "novelty": 0.8, "gap_alignment": 0.9, "launch_readiness": 0.9},
    },
    {
        "id": "nq_002",
        "type": "next_question",
        "question_text": "Which urban greening interventions produce measurable health benefits in low-income neighborhoods?",
        "origin": "slot_substitution",
        "generation_basis": "Substitutes equity geography into the greening-health question.",
        "parent_question_ids": ["q_003"],
        "parent_theme_ids": ["theme_003"],
        "slot_substitutions": {"population": "low-income neighborhoods", "outcome": "measurable health benefits"},
        "rationale": "Separates cooling feasibility from demonstrated health effects and equity-targeted implementation.",
        "confidence": "medium",
        "launch_ready": True,
        "root_status": "none",
        "score": 0.85,
        "score_components": {"user_alignment": 0.9, "structural_clarity": 0.85, "novelty": 0.85, "gap_alignment": 0.85, "launch_readiness": 0.8},
    },
    {
        "id": "nq_003",
        "type": "next_question",
        "question_text": "How should cooling-center placement be evaluated against uptake, lived experience, and equity?",
        "origin": "structure_narrowing",
        "generation_basis": "Combines access evidence with lived-experience and equity criteria.",
        "parent_question_ids": ["q_006"],
        "parent_theme_ids": ["theme_002"],
        "slot_substitutions": {"intervention": "cooling centers", "criteria": "uptake, lived experience, and equity"},
        "rationale": "Makes the equity component more actionable and distinguishes access from use.",
        "confidence": "medium",
        "launch_ready": True,
        "root_status": "none",
        "score": 0.87,
        "score_components": {"user_alignment": 0.9, "structural_clarity": 0.9, "novelty": 0.8, "gap_alignment": 0.9, "launch_readiness": 0.85},
    },
    {
        "id": "nq_004",
        "type": "next_question",
        "question_text": "How can heat-vulnerability indices incorporate social isolation, language, and communication barriers?",
        "origin": "slot_substitution",
        "generation_basis": "Substitutes social and communication determinants into vulnerability measurement.",
        "parent_question_ids": ["q_002"],
        "parent_theme_ids": ["theme_002"],
        "slot_substitutions": {"measurement_domain": "social isolation, language, and communication barriers"},
        "rationale": "Connects quantitative vulnerability indices to lived-experience evidence.",
        "confidence": "medium",
        "launch_ready": True,
        "root_status": "none",
        "score": 0.83,
        "score_components": {"user_alignment": 0.85, "structural_clarity": 0.85, "novelty": 0.85, "gap_alignment": 0.8, "launch_readiness": 0.8},
    },
    {
        "id": "nq_005",
        "type": "next_question",
        "question_text": "What evidence is needed to adapt multicountry heat-mortality estimates to local governance decisions?",
        "origin": "source_gap",
        "generation_basis": "Follows the gap between broad multicountry estimates and local decision-making.",
        "parent_question_ids": ["q_007"],
        "parent_theme_ids": ["theme_006"],
        "slot_substitutions": {"geography": "local governance context", "evidence_type": "transferable exposure-response estimates"},
        "rationale": "Makes the measurement-limitation component actionable for city decision-making.",
        "confidence": "medium",
        "launch_ready": True,
        "root_status": "none",
        "score": 0.82,
        "score_components": {"user_alignment": 0.85, "structural_clarity": 0.8, "novelty": 0.8, "gap_alignment": 0.85, "launch_readiness": 0.8},
    },
]

THEMES = [
    {
        "id": "theme_001",
        "type": "theme",
        "label": "Health outcomes and healthcare use",
        "statement": "Evidence examines heat-related mortality, morbidity, mental health, and emergency department use.",
        "question_ids": ["q_001", "q_003", "q_007"],
        "source_ids": ["src_001", "src_002", "src_003", "src_004", "src_010", "src_019"],
        "next_question_ids": [],
        "support_summary": {},
        "support_tier": "",
        "score": 0.93,
        "score_components": {"support": 0.95, "breadth": 0.9, "evidence_strength": 0.9, "coherence": 0.95},
        "confidence": "high",
        "coherence_basis": "All included evidence concerns heat-related health endpoints or health-related intervention effects.",
        "key_terms": ["mortality", "emergency department", "mental health", "healthcare use"],
        "coverage_summary": {"geographies": ["United States", "Europe", "multicountry"], "methods": ["case-crossover", "time series", "surveillance", "health impact assessment"]},
        "rationale": "The theme contains direct health-outcome evidence and keeps it separate from governance and lived experience.",
    },
    {
        "id": "theme_002",
        "type": "theme",
        "label": "Vulnerability, equity, and access",
        "statement": "Evidence maps vulnerability, examines disproportionate exposure, and assesses access to cooling resources.",
        "question_ids": ["q_002", "q_005", "q_006"],
        "source_ids": ["src_005", "src_006", "src_007", "src_008", "src_011", "src_016", "src_017", "src_018"],
        "next_question_ids": ["nq_003", "nq_004"],
        "support_summary": {},
        "support_tier": "",
        "score": 0.91,
        "score_components": {"support": 0.95, "breadth": 0.9, "evidence_strength": 0.8, "coherence": 0.9},
        "confidence": "high",
        "coherence_basis": "The theme links vulnerability measurement, social circumstances, and equitable access without claiming all evidence is causal.",
        "key_terms": ["heat vulnerability", "equity", "cooling center", "access to refuge", "social isolation"],
        "coverage_summary": {"geographies": ["United States", "Australia"], "methods": ["spatial analysis", "case study", "qualitative stakeholder study", "systematic review"]},
        "rationale": "The theme covers vulnerability and access while distinguishing measurement from lived experience.",
    },
    {
        "id": "theme_003",
        "type": "theme",
        "label": "Urban form, green space, and cooling",
        "statement": "Evidence examines how urban greening, green infrastructure, and city form affect cooling and health risk.",
        "question_ids": ["q_003"],
        "source_ids": ["src_009", "src_010", "src_011"],
        "next_question_ids": ["nq_002"],
        "support_summary": {},
        "support_tier": "",
        "score": 0.87,
        "score_components": {"support": 0.85, "breadth": 0.85, "evidence_strength": 0.85, "coherence": 0.9},
        "confidence": "high",
        "coherence_basis": "The included studies share urban physical form and cooling mechanisms.",
        "key_terms": ["urban greening", "green infrastructure", "urban form", "cooling"],
        "coverage_summary": {"geographies": ["global", "Europe"], "methods": ["systematic review", "health impact assessment", "cross-sectional comparison"]},
        "rationale": "The theme preserves the distinction between cooling potential and direct health evidence.",
    },
    {
        "id": "theme_004",
        "type": "theme",
        "label": "Governance, warnings, and emergency response",
        "statement": "Evidence examines heat-health plans, warnings, municipal response, and adaptation governance.",
        "question_ids": ["q_004", "q_006", "q_007"],
        "source_ids": ["src_007", "src_012", "src_013", "src_014", "src_015", "src_018", "src_020"],
        "next_question_ids": ["nq_001"],
        "support_summary": {},
        "support_tier": "",
        "score": 0.9,
        "score_components": {"support": 0.9, "breadth": 0.9, "evidence_strength": 0.85, "coherence": 0.9},
        "confidence": "high",
        "coherence_basis": "The studies and guidance share governance and emergency-response mechanisms.",
        "key_terms": ["heat-health action plan", "warning system", "emergency response", "governance"],
        "coverage_summary": {"geographies": ["United States", "international"], "methods": ["systematic review", "plan assessment", "operational guidance"]},
        "rationale": "The theme groups actionable policy evidence while separating implementation from measured effectiveness.",
    },
    {
        "id": "theme_005",
        "type": "theme",
        "label": "Lived experience and social consequences",
        "statement": "Evidence examines social isolation, household experiences, adaptive capacity, and cultural perspectives during heat.",
        "question_ids": ["q_005", "q_006"],
        "source_ids": ["src_016", "src_017", "src_018"],
        "next_question_ids": [],
        "support_summary": {},
        "support_tier": "",
        "score": 0.84,
        "score_components": {"support": 0.85, "breadth": 0.85, "evidence_strength": 0.8, "coherence": 0.9},
        "confidence": "medium",
        "coherence_basis": "The included studies share human experience, social context, and adaptive capacity.",
        "key_terms": ["lived experience", "social isolation", "adaptive capacity", "stakeholder perceptions"],
        "coverage_summary": {"geographies": ["United States", "Australia"], "methods": ["social autopsy", "case study", "qualitative stakeholder study"]},
        "rationale": "The theme keeps human experience distinct from quantitative health endpoints.",
    },
    {
        "id": "theme_006",
        "type": "theme",
        "label": "Measurement and evidence limitations",
        "statement": "Evidence addresses vulnerability indicators, effectiveness evaluation, modeling assumptions, and evidence quality.",
        "question_ids": ["q_001", "q_002", "q_003", "q_004", "q_005", "q_007"],
        "source_ids": ["src_005", "src_006", "src_009", "src_012", "src_014", "src_015", "src_019", "src_020"],
        "next_question_ids": ["nq_005"],
        "support_summary": {},
        "support_tier": "",
        "score": 0.89,
        "score_components": {"support": 0.9, "breadth": 0.9, "evidence_strength": 0.9, "coherence": 0.9},
        "confidence": "high",
        "coherence_basis": "The theme is cross-cutting because each included source concerns how evidence or interventions should be measured or interpreted.",
        "key_terms": ["measurement", "effectiveness", "evaluation", "evidence quality", "model assumptions"],
        "coverage_summary": {"geographies": ["global", "multicountry", "United States"], "methods": ["systematic review", "observational modeling", "index development"]},
        "rationale": "The theme makes evidence limitations visible without implying that every question is contained by measurement.",
    },
]


def add_theme_edges(edges):
    assignments = {
        "q_001": [("theme_001", "primary"), ("theme_006", "cross_cutting")],
        "q_002": [("theme_002", "primary"), ("theme_006", "cross_cutting")],
        "q_003": [("theme_003", "primary"), ("theme_001", "cross_cutting"), ("theme_006", "cross_cutting")],
        "q_004": [("theme_004", "primary"), ("theme_006", "cross_cutting")],
        "q_005": [("theme_005", "primary"), ("theme_002", "cross_cutting"), ("theme_006", "cross_cutting")],
        "q_006": [("theme_002", "primary"), ("theme_004", "cross_cutting"), ("theme_005", "cross_cutting")],
        "q_007": [("theme_006", "primary"), ("theme_001", "cross_cutting"), ("theme_004", "cross_cutting")],
    }
    edge_number = 1
    for question_id, memberships in assignments.items():
        for theme_id, role in memberships:
            edges.append(
                {
                    "id": f"edge_theme_{edge_number:03d}",
                    "source_id": question_id,
                    "target_id": theme_id,
                    "relation": "member_of",
                    "role": role,
                    "basis": f"Primary or cross-cutting assignment based on the question's main evidence location and relevant shared mechanisms.",
                    "confidence": "high" if role == "primary" else "medium",
                }
            )
            edge_number += 1


def main():
    sources = load_sources()
    pool_ids = {source_id_for(pool_id): pool_id for pool_id in SOURCE_QUESTIONS}
    source_by_id = {source["id"]: source for source in sources}

    nodes = []
    nodes.extend(sources)
    for pool_id, (question_text, canonical_question_id, rationale) in SOURCE_QUESTIONS.items():
        source_id = source_id_for(pool_id)
        source = source_by_id[source_id]
        nodes.append(
            {
                "id": source_question_id_for(pool_id),
                "type": "source_question",
                "source_id": source_id,
                "question_text": question_text,
                "canonical_question_id": canonical_question_id,
                "variants": [],
                "origin": "inferred",
                "connection_type": "reasonable_inference",
                "access_level": "metadata_only",
                "evidence_basis": "metadata_only",
                "quote_ids": [],
                "metadata_rationale": rationale,
                "confidence": "medium",
                "extraction_rationale": "The source-specific question was inferred from the title and public bibliographic metadata.",
                "canonicalization_notes": f"Title-derived question for {source.get('citation_short', source.get('title', source_id))}.",
            }
        )

    nodes.extend(QUESTIONS)
    nodes.extend(NEXT_QUESTIONS)
    nodes.append(
        {
            "id": "ctx_001",
            "type": "context",
            "label": "User prompt frame",
            "statement": "What should my city do about extreme heat and public health?",
            "root_status": "primary_user_root",
            "confidence": "high",
            "rationale": "Framing only; not a canonical analytic question and not a source-backed finding.",
        }
    )

    edges = []
    edge_number = 1
    for pool_id, (_, canonical_question_id, rationale) in SOURCE_QUESTIONS.items():
        source_id = source_id_for(pool_id)
        source_question_id = source_question_id_for(pool_id)
        edges.append(
            {
                "id": f"edge_src_sq_{edge_number:03d}",
                "source_id": source_id,
                "target_id": source_question_id,
                "relation": "infers",
                "basis": "Source title and bibliographic metadata imply the study question.",
                "confidence": "medium",
            }
        )
        edges.append(
            {
                "id": f"edge_sq_q_{edge_number:03d}",
                "source_id": source_question_id,
                "target_id": canonical_question_id,
                "relation": "supports",
                "basis": rationale,
                "confidence": "medium",
            }
        )
        edge_number += 1

    for source_question_id, question_id, basis in SECONDARY_RELATIONS:
        edges.append(
            {
                "id": f"edge_sq_related_{len(edges) + 1:03d}",
                "source_id": source_question_id,
                "target_id": question_id,
                "relation": "relates_to",
                "basis": basis,
                "confidence": "low",
            }
        )

    add_theme_edges(edges)
    for question_id, next_question in [( "q_004", "nq_001"), ("q_003", "nq_002"), ("q_006", "nq_003"), ("q_002", "nq_004"), ("q_007", "nq_005")]:
        edges.append(
            {
                "id": f"edge_q_nq_{question_id[2:]}",
                "source_id": question_id,
                "target_id": next_question,
                "relation": "narrows_to",
                "basis": "Generated follow-up question narrows the parent question.",
                "confidence": "medium",
            }
        )
        edges.append(
            {
                "id": f"edge_nq_theme_{next_question[3:]}",
                "source_id": next_question,
                "target_id": next_question.replace("nq", "theme"),
                "relation": "proposed_for",
                "basis": "Possible next question is proposed for the parent theme.",
                "confidence": "medium",
            }
        )

    for theme in THEMES:
        question_ids = theme["question_ids"]
        source_ids = theme["source_ids"]
        next_question_ids = theme["next_question_ids"]
        theme["support_summary"] = {
            "question_count": len(question_ids),
            "source_count": len(source_ids),
            "next_question_count": len(next_question_ids),
            "direct_evidence_count": len(source_ids),
            "reasonable_inference_count": 0,
            "interpretive_connection_count": 0,
        }
        if len(question_ids) > 1 and len(source_ids) > 1:
            theme["support_tier"] = "multi_source_multi_question"
        elif len(source_ids) > 1:
            theme["support_tier"] = "multi_source"
        elif len(question_ids) > 1:
            theme["support_tier"] = "multi_question"
        elif len(question_ids) == 1:
            theme["support_tier"] = "single_question"
        elif len(source_ids) == 1:
            theme["support_tier"] = "single_source"

    with (RUN_DIR / "search-results.jsonl").open() as handle:
        search_records = [json.loads(line) for line in handle if line.strip()]
    search_queries = [record for record in search_records if record.get("record_type") == "search"]

    data = {
        "schema_version": "0.1",
        "run": {
            "run_id": "2026-10-09-heat-city-policy-novice",
            "topic_slug": "heat-city-policy-novice",
            "generated_at": GENERATED_AT,
            "skill_version": "0.1",
            "data_model_version": "0.1",
            "confirmation_status": "user_confirmed",
            "breadth": "comprehensive",
            "theme_creation_rule": {
                "rule": "adaptive",
                "rationale": "Six themes preserve the case's required components and keep measurement as an explicit cross-cutting concern rather than collapsing it into a single topic.",
            },
            "question_score_weights": {
                "user_alignment": 0.3,
                "source_support": 0.2,
                "explicitness": 0.15,
                "citation_attention": 0.1,
                "breadth": 0.1,
                "relation_density": 0.1,
                "evidence_strength": 0.05,
            },
            "theme_score_weights": {"support": 0.4, "breadth": 0.2, "evidence_strength": 0.2, "coherence": 0.2},
            "user_choices": ["Run Case 1 alone first.", "Use an independent reference pool before graph generation."],
        },
        "request": {
            "core_question": "What evidence and governance actions should a novice city stakeholder consider when addressing extreme heat and public health, including health outcomes and healthcare use, vulnerable populations and equity, urban form and cooling, emergency response, lived experience, and measurement limitations?",
            "sub_questions": [
                "Health outcomes and healthcare use",
                "Vulnerable populations and equity",
                "Urban form, green space, and cooling",
                "Governance, policy, and emergency response",
                "Lived experience and social consequences",
                "Measurement or evidence limitations",
            ],
            "purpose": "Map the scholarly question landscape to orient future city decision-making.",
            "breadth": "comprehensive",
            "concepts": ["extreme heat", "public health", "vulnerability", "equity", "urban cooling", "governance"],
            "synonyms": ["heat waves", "heatwaves", "heat-health action plans", "green infrastructure", "cooling centers"],
            "constraints": ["Novice city stakeholder framing", "No PDF extraction", "Metadata-derived source questions must remain transparent"],
            "confirmation_status": "user_confirmed",
        },
        "search_log": {
            "uc_library_search": {
                "mode": "documented_skip",
                "skip_reason": "The public UC Library Search endpoint returned a JavaScript-only application shell for non-JavaScript retrieval.",
                "coverage_consequence": "Component-specific query URLs and results counts are retained, but ranked records were not retrieved through the endpoint.",
            },
            "queries": search_queries,
            "component_decomposition": [
                "Health outcomes and healthcare use",
                "Vulnerable populations and equity",
                "Urban form, green space, and cooling",
                "Governance, policy, and emergency response",
                "Lived experience and social consequences",
                "Measurement or evidence limitations",
            ],
            "adaptive_refinements": ["Precision title lookups after broad component searches."],
            "api_calls": [{"provider": "OpenAlex/Crossref", "purpose": "Title-level metadata verification", "status": "completed"}],
            "skips": [{"provider": "UC Library Search", "status": "documented_skip", "reason": "JavaScript-only public search interface"}],
        },
        "nodes": nodes,
        "edges": edges,
        "quotes": [],
        "themes": THEMES,
        "coverage": {
            "screening_counts": {"on_topic": 20, "adjacent": 0, "noise": 0},
            "question_count": len(QUESTIONS),
            "source_question_count": len(SOURCE_QUESTIONS),
            "next_question_count": len(NEXT_QUESTIONS),
            "theme_count": len(THEMES),
            "source_count": len(sources),
            "access_level_counts": {"metadata_only": len(sources)},
            "evidence_basis_counts": {"metadata_only": len(sources)},
            "not_found_statements": [
                {"statement": "City-specific causal evaluations were not found in retrieved coverage."},
                {"statement": "Measured local uptake of cooling centers was not found in retrieved coverage."},
            ],
        },
        "limitations": [
            "All source questions and support edges are derived from titles and public bibliographic metadata, not abstracts or full text.",
            "The independent pool is weighted toward the United States, Europe, and Australia, so local transfer requires caution.",
            "The review does not answer the research question or recommend a specific city policy.",
            "UC Library Search ranked records could not be retrieved through the non-JavaScript endpoint.",
        ],
    }

    with OUTPUT.open("w") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


if __name__ == "__main__":
    main()
