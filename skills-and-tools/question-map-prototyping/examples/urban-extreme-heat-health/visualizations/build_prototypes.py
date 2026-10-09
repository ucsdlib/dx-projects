#!/usr/bin/env python3
import json
from urllib.parse import quote as url_quote
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = Path(__file__).resolve().parent
with (RUN_DIR / "question_map.json").open() as handle:
    graph = json.load(handle)
with (RUN_DIR / "selected.json").open() as handle:
    selected_records = json.load(handle)

citations = {}
for path in sorted((RUN_DIR / "enrichment").glob("*.json")):
    source_id = "_".join(path.stem.split("_")[:2])
    with path.open() as handle:
        item = json.load(handle)
    citations[source_id] = {
        "count": item.get("cited_by_count"),
        "provider": "openalex",
    }

nodes = {node["id"]: node for node in graph["nodes"]}
question_support = {node["id"]: 0 for node in graph["nodes"] if node["type"] == "question"}
for edge in graph["edges"]:
    if edge["relation"] == "supports" and edge["target_id"] in question_support:
        question_support[edge["target_id"]] += 1

quotes = {quote["quote_id"]: quote for quote in graph["quotes"]}
record_ids = {record["id"]: record["record_id"] for record in selected_records if record.get("record_id")}
record_contexts = {record["id"]: record.get("context") for record in selected_records if record.get("record_id")}
supports_by_question = {}
for edge in graph["edges"]:
    if edge["relation"] == "supports" and edge["target_id"] in question_support:
        supports_by_question.setdefault(edge["target_id"], []).append(edge["source_id"])

viz_data = {
    "schema_version": graph["schema_version"],
    "run": graph["run"],
    "request": graph["request"],
    "nodes": graph["nodes"],
    "edges": graph["edges"],
    "themes": graph["themes"],
    "quotes": graph["quotes"],
    "citation_metadata": citations,
    "question_support": question_support,
}

with (OUT_DIR / "visualization-data.json").open("w") as handle:
    json.dump(viz_data, handle, indent=2)
with (OUT_DIR / "visualization-data.js").open("w") as handle:
    handle.write("window.QUESTION_MAP_DATA = ")
    json.dump(viz_data, handle, separators=(",", ":"))
    handle.write(";\n")

theme_palette = [
    "#0f766e", "#1d4ed8", "#7c3aed", "#b45309",
    "#be123c", "#334155", "#0e7490", "#4d7c0f",
]
lines = [
    "# Question Map — Mermaid Prototype",
    "",
    "This static view shows themes as circles, supported research questions as rectangles,",
    "and candidate next questions as dashed rectangles. Full text and interactive controls",
    "are in `question-map-force.html`.",
    "",
    "```mermaid",
    "flowchart LR",
]
for index, theme in enumerate(graph["themes"]):
    label = theme["label"].replace('"', "'")
    statement = theme["statement"].replace('"', "'")
    source_count = len(theme["source_ids"])
    lines.append(
        f'    {theme["id"]}(("{label}<br/>[{source_count} sources]")):::theme'
    )
    for question_id in theme["question_ids"]:
        question = nodes[question_id]
        question_text = question["question_text"].replace('"', "'")
        support_count = question_support.get(question_id, 0)
        lines.append(f'    {question_id}["{question_text}<br/>[{support_count} source questions]"]')
        lines.append(f'    {theme["id"]} --> {question_id}')
    lines.append("")

for index, question in enumerate(node for node in graph["nodes"] if node["type"] == "question"):
    pass

for node in graph["nodes"]:
    if node["type"] != "next_question":
        continue
    question_text = node["question_text"].replace('"', "'")
    lines.append(f'    {node["id"]}["{question_text}"]:::next')
    for parent_id in node["parent_question_ids"]:
        lines.append(f'    {parent_id} -.-> {node["id"]}')

lines.extend([
    "",
    "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
    "    classDef next fill:#fff7ed,stroke:#c2410c,stroke-width:2px,stroke-dasharray:5 3;",
    "```",
    "",
    "## Signal notes",
    "",
    "- Source counts come from `theme.source_ids` and `question_support` derived from `supports` edges.",
    "- Candidate next questions are generated, not source-backed.",
    "- Themes and question texts are quote-anchored in `question_map.json`.",
])
(OUT_DIR / "question-map-mermaid.md").write_text("\n".join(lines) + "\n")

origin_labels = {
    "explicit": "explicit",
    "inferred": "inferred",
    "user_defined": "working core question",
    "structure_narrowing": "structure narrowing",
    "slot_substitution": "slot substitution",
    "source_gap": "source gap",
    "user_intent": "user intent",
}
evidence_labels = {
    "abstract_and_metadata": "abstract and metadata",
    "metadata_only": "metadata only",
    "publisher_description_and_toc": "publisher description and table of contents",
}
connection_labels = {
    "direct_evidence": "direct evidence",
    "reasonable_inference": "reasonable inference",
    "interpretive_connection": "interpretive connection",
}
support_tier_labels = {
    "single_question": "single question",
    "single_source": "single source",
    "multi_question": "multiple questions",
    "multi_source": "multiple sources",
    "multi_source_multi_question": "multiple sources and questions",
}

def source_citation(source):
    authors = source.get("authors") or []
    if authors:
        author_text = ", ".join(authors[:3])
        if len(authors) > 3:
            author_text += ", et al."
    else:
        author_text = "No author recorded"
    year = source.get("year") or "n.d."
    citation = f"{author_text} ({year}). {source.get('title', 'Untitled')}."
    if source.get("venue"):
        citation += f" *{source['venue']}*."
    identifiers = []
    if source.get("doi"):
        identifiers.append(f"DOI: {source['doi']}")
    if source.get("pmid"):
        identifiers.append(f"PMID: {source['pmid']}")
    elif source.get("urls"):
        identifiers.append(f"URL: {source['urls'][0]}")
    if identifiers:
        citation += " " + "; ".join(identifiers) + "."
    citation_info = citations.get(source["id"])
    if citation_info and citation_info.get("count") is not None:
        citation += f" OpenAlex: {citation_info['count']} citations."
    return citation

def ucls_url(source):
    record_id = record_ids.get(source["id"])
    if record_id:
        return f"https://search-library.ucsd.edu/discovery/fulldisplay/{url_quote(record_id)}/01UCS_SDI%3AUCSD"
    if source.get("doi"):
        return f"https://doi.org/{source['doi']}"
    return source.get("urls", [""])[0]

def ucls_deep_link(source):
    record_id = record_ids.get(source["id"])
    if not record_id:
        return ucls_url(source)
    return f"https://search-library.ucsd.edu/permalink/01UCS_SDI/qkke1q/{url_quote(record_id)}"

def citation_link(source):
    return (
        f"<a href='{ucls_deep_link(source)}'>{concise_citation(source)}</a>"
    )

def concise_citation(source):
    authors = source.get("authors") or []
    if not authors:
        return f"Untitled ({source.get('year') or 'n.d.'})"
    surname = authors[0].split(",")[0].strip()
    if len(authors) == 1:
        return f"{surname} ({source.get('year') or 'n.d.'})"
    return f"{surname} et al. ({source.get('year') or 'n.d.'})"

def inline_citations(question_id):
    source_ids = []
    for source_question_id in supports_by_question.get(question_id, []):
        source_id = nodes[source_question_id]["source_id"]
        if source_id not in source_ids:
            source_ids.append(source_id)
    return [
        f"<a href='{ucls_url(nodes[source_id])}'>{concise_citation(nodes[source_id])}</a>"
        for source_id in source_ids
    ]

def pluralize(count, singular, plural=None):
    return singular if count == 1 else (plural or f"{singular}s")

def humanize(value, mapping=None):
    if not value:
        return "Not recorded"
    if mapping and value in mapping:
        return mapping[value]
    return value.replace("_", " ")

linear = [
    "# Question Map — Linear Reading View",
    "",
    "This is a human-readable companion to the interactive and Mermaid views.",
    "",
    "## Inquiry",
    "",
    f"**Core question:** {graph['request']['core_question']}",
    "",
    f"**Purpose:** {graph['request'].get('purpose', 'Not recorded')}",
    "",
    f"**Breadth:** {graph['request'].get('breadth', 'Not recorded')}",
    "",
    f"**Confirmation status:** {humanize(graph['request'].get('confirmation_status'))}",
    "",
    "## Reading notes",
    "",
    "- Themes summarize recurrent question clusters; they are not evidence-state classifications.",
    "- Canonical questions collect related source-specific questions.",
    "- Source questions show whether they are explicit or inferred and whether the evidence basis is abstract/metadata, metadata only, or another access type.",
    "- Candidate next questions are generated from gaps, substitutions, or question structure. They are not source-backed findings.",
    "- OpenAlex citation counts are discovery signals, not measures of quality, truth, or consensus.",
    "",
    "## Coverage summary",
    "",
    f"- Sources selected: {graph['coverage']['source_count']}",
    f"- Source questions: {graph['coverage']['source_question_count']}",
    f"- Canonical questions: {graph['coverage']['question_count']}",
    f"- Themes: {graph['coverage']['theme_count']}",
    f"- Candidate next questions: {graph['coverage']['next_question_count']}",
    f"- Screening: {graph['coverage']['screening_counts']['on_topic']} on topic, {graph['coverage']['screening_counts']['adjacent']} adjacent, {graph['coverage']['screening_counts']['noise']} noise",
    "",
]

for theme_index, theme in enumerate(graph["themes"], start=1):
    support = theme["support_summary"]
    linear.extend([
        f"## {theme_index}. {theme['label']}",
        "",
        theme["statement"],
        "",
        f"**Support tier:** {humanize(theme.get('support_tier'), support_tier_labels)}",
        "",
        f"**Confidence:** {theme.get('confidence', 'Not recorded')}",
        "",
        f"**Support:** {support['source_count']} sources, {support['question_count']} canonical questions, {support['direct_evidence_count']} direct-evidence connections",
        "",
    ])
    if theme.get("coherence_basis"):
        linear.extend([
            "**Coherence:** " + theme["coherence_basis"],
            "",
        ])
    if theme.get("key_terms"):
        linear.extend([
            "**Key terms:** " + " · ".join(theme["key_terms"]),
            "",
        ])
    if theme.get("source_ids"):
        linear.append("**Sources in this theme:**")
        linear.append("")
        for source_id in theme["source_ids"]:
            source = nodes[source_id]
            linear.append(f"- {source.get('title', 'Untitled')} ({source.get('year', 'n.d.')})")
        linear.append("")
    for question_id in theme["question_ids"]:
        question = nodes[question_id]
        support_count = question_support.get(question_id, 0)
        linear.extend([
            f"### {question['question_text']}",
            "",
            f"**Type:** {humanize(question.get('question_type'))}  ",
            f"**Origin:** {humanize(question.get('origin'), origin_labels)}  ",
            f"**Confidence:** {question.get('confidence', 'Not recorded')}  ",
            f"**Direct source-question support:** {support_count}",
            "",
        ])
        source_question_ids = supports_by_question.get(question_id, [])
        if source_question_ids:
            for source_question_id in source_question_ids:
                source_question = nodes[source_question_id]
                source = nodes[source_question["source_id"]]
                linear.extend([
                    f"- **{source_question['question_text']}**",
                    f"  - **Source:** {source_citation(source)}",
                    f"  - **Evidence:** {humanize(source_question.get('origin'), origin_labels)} · {humanize(source_question.get('connection_type'), connection_labels)} · {humanize(source_question.get('evidence_basis'), evidence_labels)}",
                ])
                quote_ids = source_question.get("quote_ids") or []
                if quote_ids:
                    quote = quotes[quote_ids[0]]
                    linear.append(f"  - **Anchor:** “{quote['text']}”")
                elif source_question.get("metadata_rationale"):
                    linear.append(f"  - **Metadata rationale:** {source_question['metadata_rationale']}")
                elif source_question.get("extraction_rationale"):
                    linear.append(f"  - **Extraction rationale:** {source_question['extraction_rationale']}")
            linear.append("")
        else:
            linear.extend([
                "No source questions are directly attached to this canonical question in the current graph.",
                "",
            ])
            if theme.get("source_ids"):
                linear.extend([
                    "The theme sources listed above are not represented as direct source-question support for this canonical question.",
                    "",
                ])

linear.extend([
    "## Possible next questions",
    "",
    "These are generated candidates for further inquiry, not source-backed conclusions.",
    "",
])
for next_question in [node for node in graph["nodes"] if node["type"] == "next_question"]:
    parent_questions = ", ".join(
        nodes[parent_id]["question_text"] for parent_id in next_question.get("parent_question_ids", [])
    )
    linear.extend([
        f"### {next_question['question_text']}",
        "",
        f"**Origin:** {humanize(next_question.get('origin'), origin_labels)}",
        "",
        f"**Generation basis:** {next_question.get('generation_basis', 'Not recorded')}",
        "",
    ])
    if parent_questions:
        linear.extend([
            "**Related canonical questions:** " + parent_questions,
            "",
        ])
    if next_question.get("slot_substitutions"):
        substitutions = ", ".join(f"{key}: {value}" for key, value in next_question["slot_substitutions"].items())
        linear.extend([
            "**Slot substitutions:** " + substitutions,
            "",
        ])
    linear.extend([
        f"**Confidence:** {next_question.get('confidence', 'Not recorded')}",
        "",
    ])

linear.extend([
    "## Not found in retrieved coverage",
    "",
])
for item in graph["coverage"].get("not_found_statements", []):
    linear.append(f"- {item['statement']}")
linear.extend([
    "",
    "## Limitations",
    "",
])
for limitation in graph["limitations"]:
    linear.append(f"- {limitation}")
linear.extend([
    "",
    "---",
    "",
    f"Generated from `{graph['run']['run_id']}` · data model `{graph['run']['data_model_version']}`.",
])
(OUT_DIR / "question-map.md").write_text("\n".join(linear) + "\n")

mermaid2 = [
    "# Question Map — Mermaid Citation Experiments",
    "",
    "This file explores two ways to make sources visible in the map without losing the question as the primary unit.",
    "",
    "## Labels used",
    "",
    "- **Source-specific questions** means the number of source questions directly linked to this canonical question.",
    "- **Theme-linked sources** means the number of distinct source nodes explicitly listed under the theme.",
    "- These two counts are related but not interchangeable: a source can ask more than one question, and a theme may list sources that are not directly linked to every question inside it.",
    "",
    "## Variant A — inline citations inside question nodes",
    "",
    "This keeps the map compact and puts the citation directly next to the question. Links use Mermaid HTML labels.",
    "",
    "```mermaid",
    "flowchart LR",
]
for theme in graph["themes"]:
    source_count = len(theme["source_ids"])
    lines.append(f'    {theme["id"]}(("{theme["label"]}<br/>[{source_count} theme-linked sources]")):::theme')
    for question_id in theme["question_ids"]:
        question = nodes[question_id]
        support_count = question_support.get(question_id, 0)
        citation_text = "<br/>".join(inline_citations(question_id))
        question_label = pluralize(support_count, "source-specific question")
        label = f'{question["question_text"]}<br/>[{support_count} {question_label}]<br/>{citation_text}'
        mermaid2.append(f'    {question_id}["{label}"]')
        mermaid2.append(f'    {theme["id"]} --> {question_id}')
    mermaid2.append("")
for next_question in [node for node in graph["nodes"] if node["type"] == "next_question"]:
    mermaid2.append(f'    {next_question["id"]}["{next_question["question_text"]}"]:::next')
    for parent_id in next_question.get("parent_question_ids", []):
        mermaid2.append(f'    {parent_id} -.-> {next_question["id"]}')
mermaid2.extend([
    "",
    "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
    "    classDef next fill:#fff7ed,stroke:#c2410c,stroke-width:2px,stroke-dasharray:5 3;",
    "```",
    "",
    "## Variant B — compact source boxes with UC Library Search links",
    "",
    "This is more explicit and avoids relying on HTML inside node labels. It is better when you want one stable click target per source.",
    "",
    "```mermaid",
    "flowchart LR",
])
seen_sources = set()
for question in [node for node in graph["nodes"] if node["type"] == "question"]:
    mermaid2.append(f'    {question["id"]}["{question["question_text"]}"]')
    for source_question_id in supports_by_question.get(question["id"], []):
        source_id = nodes[source_question_id]["source_id"]
        source = nodes[source_id]
        if source_id not in seen_sources:
            mermaid2.append(f'    {source_id}["{concise_citation(source)}"]:::source')
            mermaid2.append(f'    click {source_id} href "{ucls_url(source)}" "Open UC Library Search record"')
            seen_sources.add(source_id)
        mermaid2.append(f'    {source_id} -.-> {question["id"]}')
mermaid2.extend([
    "",
    "    classDef source fill:#f8fafc,stroke:#64748b,stroke-width:1px;",
    "    linkStyle default stroke:#94a3b8,stroke-width:1px;",
    "```",
    "",
    "## Notes",
    "",
    "- Variant A is more compact, but some Mermaid renderers may strip HTML links or make long labels harder to read.",
    "- Variant B is more verbose, but gives each source a stable click target and makes multi-source support easier to inspect.",
    "- If the graph later supports source-to-source deduplication, the source boxes could become a compact bibliography layer connected to both source questions and canonical questions.",
])
(OUT_DIR / "question-map-mermaid-2.md").write_text("\n".join(mermaid2) + "\n")

mermaid3 = [
    "# Question Map — Mermaid Citation Layout Experiment",
    "",
    "This experiment keeps themes as circles on the left, questions as rectangles in the middle,",
    "and candidate next questions on the right. Question cards use left-aligned text, a divider,",
    "and concise source citations linked to UC Library Search permalinks.",
    "",
    "```mermaid",
    "flowchart LR",
]
for theme in graph["themes"]:
    source_count = len(theme["source_ids"])
    mermaid3.append(f'    {theme["id"]}(("{theme["label"]}<br/>[{source_count} theme-linked sources]")):::theme')
    for question_id in theme["question_ids"]:
        question = nodes[question_id]
        support_count = question_support.get(question_id, 0)
        question_label = pluralize(support_count, "source-specific question")
        citation_lines = "<br/>".join(
            citation_link(nodes[nodes[source_question_id]["source_id"]])
            for source_question_id in supports_by_question.get(question_id, [])
        )
        if not citation_lines:
            citation_lines = "No direct source questions yet"
        label = (
            f"<div style='text-align:left'>"
            f"{question['question_text']}"
            f"<hr/>"
            f"[{support_count} {question_label}]"
            f"<br/>{citation_lines}"
            "</div>"
        )
        mermaid3.append(f'    {question_id}["{label}"]:::question')
        mermaid3.append(f'    {theme["id"]} --> {question_id}')
    mermaid3.append("")
for next_question in [node for node in graph["nodes"] if node["type"] == "next_question"]:
    mermaid3.append(f'    {next_question["id"]}["<div style=\'text-align:left\'>{next_question["question_text"]}</div>"]:::next')
    for parent_id in next_question.get("parent_question_ids", []):
        mermaid3.append(f'    {parent_id} -.-> {next_question["id"]}')
mermaid3.extend([
    "",
    "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
    "    classDef question fill:#f8fafc,stroke:#334155,stroke-width:1px,text-align:left;",
    "    classDef next fill:#fff7ed,stroke:#c2410c,stroke-width:2px,stroke-dasharray:5 3,text-align:left;",
    "```",
    "",
    "## Link strategy",
    "",
    "These cards use UC Library Search permalinks derived from the selected record ID:",
    "",
    "```text",
    "https://search-library.ucsd.edu/permalink/01UCS_SDI/qkke1q/<record_id>",
    "```",
    "",
    "We currently have the internal `record_id` for each selected source. The `qkke1q` segment appears to be a stable UCSD view code, so the permalink is derivable from `record_id`. If that proves unstable across a larger corpus, we should capture the human-facing permalink during record selection.",
])
(OUT_DIR / "question-map-mermaid-3.md").write_text("\n".join(mermaid3) + "\n")

mermaid_start = mermaid3.index("```mermaid")
mermaid_end = mermaid3.index("```", mermaid_start + 1)
question_map_block = mermaid3[mermaid_start:mermaid_end + 1]

mermaid4 = [
    f"# Question Map — {graph['request']['core_question']}",
    "",
    "This map shows the main research questions emerging from the retrieved literature.",
    "Themes appear as circles on the left, related questions as rectangles in the middle, and",
    "possible next questions on the right. Each question card lists the sources that support it,",
    "with links to UC Library Search.",
    "",
    f"This first pass identified {graph['coverage']['source_count']} selected sources, "
    f"{graph['coverage']['question_count']} core questions across {graph['coverage']['theme_count']} themes, and "
    f"{graph['coverage']['next_question_count']} possible next questions.",
    "",
    *question_map_block,
    "",
    "## Where would you like to go next?",
    "",
    "The candidate next questions on the right are starting points for inquiry, not evidence-backed conclusions.",
    "",
    "You can use this map as a launching point for your own inquiry. For example, you might:",
    "",
    "- ask me to explore one theme in more depth;",
    "- choose a question and turn it into a targeted UC Library Search;",
    "- request a focused annotated bibliography from one or more questions;",
    "- pick one of the candidate next questions and start a new inquiry from it.",
    "",
    "Tell me the theme, question, or candidate question that interests you, and I can take it from there.",
]
(OUT_DIR / "question-map-mermaid-4.md").write_text("\n".join(mermaid4) + "\n")

def source_orientation_lines(question_id):
    lines = []
    for source_question_id in supports_by_question.get(question_id, []):
        source_question = nodes[source_question_id]
        source = nodes[source_question["source_id"]]
        citation = citation_link(source)
        orientation = source_question.get("question_text", "")
        if orientation:
            orientation = f" — <i>{orientation}</i>"
        lines.append(f"• {citation}{orientation}")
    return lines

mermaid5 = [
    f"# Question Map — {graph['request']['core_question']}",
    "",
    "This map shows the main research questions emerging from the retrieved literature.",
    "Themes appear as circles on the left, related questions as rectangles in the middle.",
    "Each question card lists the sources that support it, with a concise orientation phrase",
    "and a link to UC Library Search.",
    "",
    f"This first pass identified {graph['coverage']['source_count']} selected sources, "
    f"{graph['coverage']['question_count']} core questions across {graph['coverage']['theme_count']} themes, and "
    f"{graph['coverage']['next_question_count']} possible next questions.",
    "",
    "```mermaid",
    "flowchart LR",
]
for theme in graph["themes"]:
    mermaid5.append(f'    {theme["id"]}(("{theme["label"]}")):::theme')
    for question_id in theme["question_ids"]:
        question = nodes[question_id]
        orientation_lines = source_orientation_lines(question_id)
        if orientation_lines:
            source_text = "<br/>".join(orientation_lines)
        else:
            source_text = "No sources linked yet."
        label = (
            f"<div style='text-align:left'>"
            f"{question['question_text']}"
            f"<hr/>"
            f"{source_text}"
            "</div>"
        )
        mermaid5.append(f'    {question_id}["{label}"]:::question')
        mermaid5.append(f'    {theme["id"]} --> {question_id}')
    mermaid5.append("")
mermaid5.extend([
    "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
    "    classDef question fill:#f8fafc,stroke:#334155,stroke-width:1px,text-align:left;",
    "```",
    "",
    "## Where would you like to go next?",
    "",
    "Questions to explore:",
    "",
])
for next_question in [node for node in graph["nodes"] if node["type"] == "next_question"]:
    mermaid5.append(f"- {next_question['question_text']}")
mermaid5.extend([
    "",
    "You can use this map as a launching point for your own inquiry. For example, you might:",
    "",
    "- ask me to explore one theme in more depth;",
    "- choose a question and turn it into a targeted UC Library Search;",
    "- request a focused annotated bibliography from one or more questions;",
    "- pick one of the questions to explore and start a new inquiry from it.",
    "",
    "Tell me which theme, question, or future-research question interests you, and I can take it from there.",
])
(OUT_DIR / "question-map-mermaid-5.md").write_text("\n".join(mermaid5) + "\n")

mermaid5a = [
    f"# Question Map — {graph['request']['core_question']}",
    "",
    "This map shows the main research questions emerging from the retrieved literature.",
    "Themes appear as circles on the left, related questions as rectangles in the middle, and",
    "supporting sources as cards on the right. Each source card names the source’s stated question",
    "through which it connects to the canonical question.",
    "",
    f"This first pass identified {graph['coverage']['source_count']} selected sources, "
    f"{graph['coverage']['question_count']} core questions across {graph['coverage']['theme_count']} themes, and "
    f"{graph['coverage']['next_question_count']} possible next questions.",
    "",
    "```mermaid",
    "flowchart LR",
]
for theme in graph["themes"]:
    mermaid5a.append(f'    {theme["id"]}(("{theme["label"]}")):::theme')
    for question_id in theme["question_ids"]:
        mermaid5a.append(f'    {question_id}["<div style=\'text-align:left\'>{nodes[question_id]["question_text"]}</div>"]:::question')
        mermaid5a.append(f'    {theme["id"]} --> {question_id}')
        for source_question_id in supports_by_question.get(question_id, []):
            source_question = nodes[source_question_id]
            source = nodes[source_question["source_id"]]
            orientation = source_question.get("question_text", "")
            source_label = (
                f"<div style='width:340px;text-align:left'>"
                f"{citation_link(source)} — <i>{orientation}</i>"
                "</div>"
            )
            mermaid5a.append(f'    {source["id"]}["{source_label}"]:::source')
            mermaid5a.append(f'    {question_id} -.-> {source["id"]}')
    mermaid5a.append("")
mermaid5a.extend([
    "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
    "    classDef question fill:#f8fafc,stroke:#334155,stroke-width:1px,text-align:left;",
    "    classDef source fill:#fffbeb,stroke:#b45309,stroke-width:1px,text-align:left;",
    "```",
    "",
    "## Where would you like to go next?",
    "",
    "Questions to explore:",
    "",
])
for next_question in [node for node in graph["nodes"] if node["type"] == "next_question"]:
    mermaid5a.append(f"- {next_question['question_text']}")
mermaid5a.extend([
    "",
    "You can use this map as a launching point for your own inquiry. For example, you might:",
    "",
    "- ask me to explore one theme in more depth;",
    "- choose a question and turn it into a targeted UC Library Search;",
    "- request a focused annotated bibliography from one or more questions;",
    "- pick one of the questions to explore and start a new inquiry from it.",
    "",
    "Tell me which theme, question, or future-research question interests you, and I can take it from there.",
])
(OUT_DIR / "question-map-mermaid-5a.md").write_text("\n".join(mermaid5a) + "\n")

mermaid5b = [
    f"# Question Map — {graph['request']['core_question']}",
    "",
    "This map shows the main research questions emerging from the retrieved literature.",
    "Themes appear as circles on the left, related questions as wider rectangles in the middle.",
    "Each question card lists the sources that support it, with a concise orientation phrase",
    "and a link to UC Library Search.",
    "",
    f"This first pass identified {graph['coverage']['source_count']} selected sources, "
    f"{graph['coverage']['question_count']} core questions across {graph['coverage']['theme_count']} themes, and "
    f"{graph['coverage']['next_question_count']} possible next questions.",
    "",
    "```mermaid",
    "flowchart LR",
]
for theme in graph["themes"]:
    mermaid5b.append(f'    {theme["id"]}(("{theme["label"]}")):::theme')
    for question_id in theme["question_ids"]:
        question = nodes[question_id]
        orientation_lines = source_orientation_lines(question_id)
        source_text = "<br/>".join(orientation_lines) if orientation_lines else "No sources linked yet."
        label = (
            "<div style='width:520px;text-align:left'>"
            f"{question['question_text']}"
            "<hr/>"
            f"{source_text}"
            "</div>"
        )
        mermaid5b.append(f'    {question_id}["{label}"]:::question')
        mermaid5b.append(f'    {theme["id"]} --> {question_id}')
    mermaid5b.append("")
mermaid5b.extend([
    "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
    "    classDef question fill:#f8fafc,stroke:#334155,stroke-width:1px,text-align:left;",
    "```",
    "",
    "## Where would you like to go next?",
    "",
    "Questions to explore:",
    "",
])
for next_question in [node for node in graph["nodes"] if node["type"] == "next_question"]:
    mermaid5b.append(f"- {next_question['question_text']}")
mermaid5b.extend([
    "",
    "You can use this map as a launching point for your own inquiry. For example, you might:",
    "",
    "- ask me to explore one theme in more depth;",
    "- choose a question and turn it into a targeted UC Library Search;",
    "- request a focused annotated bibliography from one or more questions;",
    "- pick one of the questions to explore and start a new inquiry from it.",
    "",
    "Tell me which theme, question, or future-research question interests you, and I can take it from there.",
])
(OUT_DIR / "question-map-mermaid-5b.md").write_text("\n".join(mermaid5b) + "\n")
