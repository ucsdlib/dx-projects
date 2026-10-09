#!/usr/bin/env python3
"""Build the Phase 2 visualization artifacts from question_map.json."""

import argparse
import html
import json
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


ORIGIN_LABELS = {
    "explicit": "explicit",
    "inferred": "inferred",
    "user_defined": "working core question",
    "structure_narrowing": "structure narrowing",
    "slot_substitution": "slot substitution",
    "source_gap": "source gap",
    "user_intent": "user intent",
}
EVIDENCE_LABELS = {
    "abstract_and_metadata": "abstract and metadata",
    "metadata_only": "metadata only",
    "publisher_description_and_toc": "publisher description and table of contents",
    "full_text_machine_readable": "full text",
}
CONNECTION_LABELS = {
    "direct_evidence": "direct evidence",
    "reasonable_inference": "reasonable inference",
    "interpretive_connection": "interpretive connection",
}
SUPPORT_TIER_LABELS = {
    "single_question": "single question",
    "single_source": "single source",
    "multi_question": "multiple questions",
    "multi_source": "multiple sources",
    "multi_source_multi_question": "multiple sources and questions",
}


def load_json(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def humanize(value, mapping=None):
    if not value:
        return "Not recorded"
    if mapping and value in mapping:
        return mapping[value]
    return str(value).replace("_", " ")


def escape_label(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def escaped_url(url):
    return html.escape(str(url), quote=True)


def source_link(node):
    url = node.get("ucls_permalink") or (node.get("urls") or [None])[0]
    if not url:
        return node.get("citation_short") or node.get("title") or "Untitled"
    text = node.get("citation_short") or node.get("title") or "Open source"
    return f"<a href='{escaped_url(url)}'>{escape_label(text)}</a>"


def markdown_link(node):
    url = node.get("ucls_permalink") or (node.get("urls") or [None])[0]
    text = node.get("citation_short") or node.get("title") or "Untitled"
    if not url:
        return text
    return f"[{text}]({url})"


def derive_support(graph):
    nodes = graph.get("nodes", [])
    node_index = {node["id"]: node for node in nodes}
    support_by_question = defaultdict(list)
    for edge in graph.get("edges", []):
        source = node_index.get(edge.get("source_id"))
        target = node_index.get(edge.get("target_id"))
        if source and target and edge.get("relation") == "supports" and source.get("type") == "source_question" and target.get("type") == "question":
            support_by_question[target["id"]].append(source["id"])
    return node_index, support_by_question


def source_questions_by_source(node_index, support_by_question):
    grouped = defaultdict(list)
    for question_id in sorted(support_by_question):
        for source_question_id in support_by_question[question_id]:
            source_question = node_index[source_question_id]
            grouped[source_question["source_id"]].append(source_question)
    return grouped


def validate_inputs(graph, node_index):
    errors = []
    assigned_question_ids = set()
    for theme in graph.get("themes", []):
        for question_id in theme.get("question_ids", []):
            assigned_question_ids.add(question_id)
            if question_id not in node_index:
                errors.append(f"Theme {theme.get('id')} references missing question {question_id}.")
        for source_id in theme.get("source_ids", []):
            if source_id not in node_index:
                errors.append(f"Theme {theme.get('id')} references missing source {source_id}.")
    for question in (node for node in graph.get("nodes", []) if node.get("type") == "question"):
        if question["id"] not in assigned_question_ids:
            errors.append(f"Question {question['id']} is not assigned to a theme.")
    for source in (node for node in graph.get("nodes", []) if node.get("type") == "source"):
        for field in ("citation_short", "citation_display"):
            if not source.get(field):
                errors.append(f"Source {source.get('id')} is missing normalized citation field {field}.")
        if not source.get("ucls_permalink") and not source.get("urls"):
            errors.append(f"Source {source.get('id')} has no UC Library Search permalink or external URL.")
    for quote in graph.get("quotes", []):
        if quote.get("source_id") not in node_index:
            errors.append(f"Quote {quote.get('quote_id')} references missing source {quote.get('source_id')}.")
    for node in graph.get("nodes", []):
        for parent_id in node.get("parent_question_ids", []):
            if parent_id not in node_index:
                errors.append(f"Node {node.get('id')} references missing parent question {parent_id}.")
    if errors:
        print("Visualization validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def build_visualization_data(graph, node_index, support_by_question):
    question_support = {
        question["id"]: len(support_by_question[question["id"]])
        for question in graph.get("nodes", [])
        if question.get("type") == "question"
    }
    citation_metadata = {
        node["id"]: node.get("citation_metadata") or {}
        for node in graph.get("nodes", [])
        if node.get("type") == "source"
    }
    return {
        "schema_version": graph["schema_version"],
        "run": graph["run"],
        "request": graph["request"],
        "nodes": graph["nodes"],
        "edges": graph["edges"],
        "themes": graph["themes"],
        "quotes": graph["quotes"],
        "citation_metadata": citation_metadata,
        "question_support": question_support,
    }


def build_mermaid(graph, node_index, support_by_question, wide_cards=False):
    lines = [
        f"# Question Map — {graph['request']['core_question']}",
        "",
        "This map shows the main research questions emerging from the retrieved literature.",
    ]
    if wide_cards:
        lines.extend([
            "Themes appear as circles on the left, and wider question cards appear in the middle.",
            "Each question card lists its supporting sources, with links to UC Library Search.",
        ])
    else:
        lines.extend([
            "Themes appear as circles on the left, related questions in the middle, and supporting",
            "sources as cards on the right. Each source card names the source’s stated question.",
        ])
    lines.extend([
        "",
        f"This first pass identified {graph['coverage']['source_count']} selected sources, "
        f"{graph['coverage']['question_count']} core questions across {graph['coverage']['theme_count']} themes, and "
        f"{graph['coverage']['next_question_count']} possible next questions.",
        "",
        "```mermaid",
        "flowchart LR",
    ])
    source_questions = source_questions_by_source(node_index, support_by_question)
    seen_sources = set()

    for theme in graph["themes"]:
        lines.append(f'    {theme["id"]}(("{escape_label(theme["label"])}")):::theme')
        for question_id in theme["question_ids"]:
            question = node_index[question_id]
            if wide_cards:
                orientation_lines = []
                for source_question_id in support_by_question[question_id]:
                    source_question = node_index[source_question_id]
                    source = node_index[source_question["source_id"]]
                    text = source_question.get("question_text", "")
                    orientation_lines.append(f"• {source_link(source)} — <i>{escape_label(text)}</i>")
                source_text = "<br/>".join(orientation_lines) if orientation_lines else "No direct source support yet."
                label = (
                    "<div style='width:520px;text-align:left'>"
                    f"{escape_label(question['question_text'])}"
                    "<hr/>"
                    f"{source_text}"
                    "</div>"
                )
            else:
                label = f"<div style='text-align:left'>{escape_label(question['question_text'])}</div>"
            lines.append(f'    {question_id}["{label}"]:::question')
            lines.append(f'    {theme["id"]} --> {question_id}')
            if not wide_cards:
                for source_question_id in support_by_question[question_id]:
                    source_question = node_index[source_question_id]
                    source = node_index[source_question["source_id"]]
                    if source["id"] not in seen_sources:
                        seen_sources.add(source["id"])
                        orientation_lines = []
                        for item in source_questions[source["id"]]:
                            text = item.get("question_text", "")
                            orientation_lines.append(f"• {escape_label(text)}")
                        orientation_text = "<br/>".join(orientation_lines)
                        source_label = (
                            "<div style='width:340px;text-align:left'>"
                            f"{source_link(source)} — <i>{orientation_text}</i>"
                            "</div>"
                        )
                        lines.append(f'    {source["id"]}["{source_label}"]:::source')
                    lines.append(f'    {question_id} -.-> {source["id"]}')
        lines.append("")

    lines.extend([
        "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
        "    classDef question fill:#f8fafc,stroke:#334155,stroke-width:1px,text-align:left;",
    ])
    if not wide_cards:
        lines.append("    classDef source fill:#fffbeb,stroke:#b45309,stroke-width:1px,text-align:left;")
    lines.extend([
        "```",
        "",
        "## Where would you like to go next?",
        "",
        "Questions to explore:",
        "",
    ])
    for next_question in (node for node in graph["nodes"] if node.get("type") == "next_question"):
        lines.append(f"- {next_question['question_text']}")
    lines.extend([
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
    return lines


def build_linear(graph, node_index, support_by_question):
    lines = [
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
        "- Canonical questions collect related source questions.",
        "- Source questions show whether they are explicit or inferred and whether the evidence basis is abstract/metadata, metadata only, or another access type.",
        "- Possible next questions are generated from gaps, substitutions, or question structure. They are not source-backed findings.",
        "- OpenAlex citation counts are discovery signals, not measures of quality, truth, or consensus.",
        "",
        "## Coverage summary",
        "",
        f"- Sources selected: {graph['coverage']['source_count']}",
        f"- Source questions: {graph['coverage']['source_question_count']}",
        f"- Canonical questions: {graph['coverage']['question_count']}",
        f"- Themes: {graph['coverage']['theme_count']}",
        f"- Possible next questions: {graph['coverage']['next_question_count']}",
        f"- Screening: {graph['coverage']['screening_counts']['on_topic']} on topic, {graph['coverage']['screening_counts']['adjacent']} adjacent, {graph['coverage']['screening_counts']['noise']} noise",
        "",
    ]

    for theme_index, theme in enumerate(graph["themes"], start=1):
        support = theme["support_summary"]
        lines.extend([
            f"## {theme_index}. {theme['label']}",
            "",
            theme["statement"],
            "",
            f"**Support tier:** {humanize(theme.get('support_tier'), SUPPORT_TIER_LABELS)}",
            "",
            f"**Confidence:** {theme.get('confidence', 'Not recorded')}",
            "",
            f"**Support:** {support['source_count']} sources, {support['question_count']} canonical questions, {support['direct_evidence_count']} direct-evidence connections",
            "",
        ])
        if theme.get("coherence_basis"):
            lines.extend(["**Coherence:** " + theme["coherence_basis"], ""])
        if theme.get("key_terms"):
            lines.extend(["**Key terms:** " + " · ".join(theme["key_terms"]), ""])
        if theme.get("source_ids"):
            lines.extend(["**Sources in this theme:**", ""])
            for source_id in theme["source_ids"]:
                source = node_index[source_id]
                lines.append(f"- {markdown_link(source)} — {source.get('title', 'Untitled')}")
            lines.append("")
        for question_id in theme["question_ids"]:
            question = node_index[question_id]
            support_count = len(support_by_question[question_id])
            lines.extend([
                f"### {question['question_text']}",
                "",
                f"**Type:** {humanize(question.get('question_type'))}  ",
                f"**Origin:** {humanize(question.get('origin'), ORIGIN_LABELS)}  ",
                f"**Confidence:** {question.get('confidence', 'Not recorded')}  ",
                f"**Direct source-question support:** {support_count}",
                "",
            ])
            if not support_by_question[question_id]:
                lines.extend(["No direct source-question support is attached to this canonical question in the current graph.", ""])
                continue
            for source_question_id in support_by_question[question_id]:
                source_question = node_index[source_question_id]
                source = node_index[source_question["source_id"]]
                quote_ids = source_question.get("quote_ids") or []
                lines.append(f"- **{source_question['question_text']}**")
                lines.append(f"  - **Source:** {markdown_link(source)}")
                lines.append(f"  - **Citation:** {source.get('citation_display', 'Not recorded')}")
                lines.append(
                    "  - **Evidence:** "
                    f"{humanize(source_question.get('origin'), ORIGIN_LABELS)} · "
                    f"{humanize(source_question.get('connection_type'), CONNECTION_LABELS)} · "
                    f"{humanize(source_question.get('evidence_basis'), EVIDENCE_LABELS)}"
                )
                if quote_ids:
                    quote = next((item for item in graph["quotes"] if item["quote_id"] == quote_ids[0]), None)
                    if quote:
                        lines.append(f"  - **Anchor:** “{quote['text']}”")
                elif source_question.get("metadata_rationale"):
                    lines.append(f"  - **Metadata rationale:** {source_question['metadata_rationale']}")
                elif source_question.get("extraction_rationale"):
                    lines.append(f"  - **Extraction rationale:** {source_question['extraction_rationale']}")
            lines.append("")

    lines.extend([
        "## Possible next questions",
        "",
        "These are generated questions for further inquiry, not source-backed conclusions.",
        "",
    ])
    for next_question in (node for node in graph["nodes"] if node.get("type") == "next_question"):
        lines.extend([
            f"### {next_question['question_text']}",
            "",
            f"**Origin:** {humanize(next_question.get('origin'), ORIGIN_LABELS)}",
            "",
            f"**Generation basis:** {next_question.get('generation_basis', 'Not recorded')}",
            "",
        ])
        if next_question.get("parent_question_ids"):
            parents = ", ".join(node_index[parent_id]["question_text"] for parent_id in next_question["parent_question_ids"])
            lines.extend(["**Related canonical questions:** " + parents, ""])
        if next_question.get("slot_substitutions"):
            substitutions = ", ".join(f"{key}: {value}" for key, value in next_question["slot_substitutions"].items())
            lines.extend(["**Slot substitutions:** " + substitutions, ""])
        lines.extend([f"**Confidence:** {next_question.get('confidence', 'Not recorded')}", ""])

    lines.extend(["## Not found in retrieved coverage", ""])
    for item in graph["coverage"].get("not_found_statements", []):
        lines.append(f"- {item['statement']}")
    lines.extend(["", "## Limitations", ""])
    for limitation in graph["limitations"]:
        lines.append(f"- {limitation}")
    lines.extend([
        "",
        "---",
        "",
        f"Generated from `{graph['run']['run_id']}` · data model `{graph['run']['data_model_version']}`.",
    ])
    return lines


def write_text(path, lines):
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", required=True, type=Path, help="Path to question_map.json")
    parser.add_argument("--output-dir", type=Path, help="Directory for generated artifacts")
    parser.add_argument("--html-template", type=Path, help="Path to the interactive HTML template")
    parser.add_argument("--wide-cards", action="store_true", help="Use the wider inline-source card variant")
    args = parser.parse_args()

    graph_path = args.graph.resolve()
    graph = load_json(graph_path)
    node_index, support_by_question = derive_support(graph)
    validate_inputs(graph, node_index)

    validator_path = Path(__file__).with_name("validate_question_map.py")
    result = subprocess.run(
        [sys.executable, str(validator_path), str(graph_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode != 0:
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        raise SystemExit("Phase 1 graph validation failed.")

    output_dir = args.output_dir.resolve() if args.output_dir else graph_path.parent / "visualizations"
    output_dir.mkdir(parents=True, exist_ok=True)
    html_template = args.html_template.resolve() if args.html_template else Path(__file__).resolve().parents[1] / "assets" / "question-map-force-template.html"
    if not html_template.exists():
        raise SystemExit(f"Interactive HTML template not found: {html_template}")

    visualization_data = build_visualization_data(graph, node_index, support_by_question)
    with (output_dir / "visualization-data.json").open("w", encoding="utf-8") as handle:
        json.dump(visualization_data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    with (output_dir / "visualization-data.js").open("w", encoding="utf-8") as handle:
        handle.write("window.QUESTION_MAP_DATA = ")
        json.dump(visualization_data, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write(";\n")

    write_text(output_dir / "question-map-mermaid.md", build_mermaid(graph, node_index, support_by_question, args.wide_cards))
    write_text(output_dir / "question-map.md", build_linear(graph, node_index, support_by_question))
    shutil.copyfile(html_template, output_dir / "question-map-force.html")
    print(f"Generated visualization artifacts in {output_dir}.")


if __name__ == "__main__":
    main()
