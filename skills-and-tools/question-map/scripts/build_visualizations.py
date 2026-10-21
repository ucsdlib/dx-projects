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
ORIGIN_TAG_LABELS = {
    "asks": "Stated",
    "infers": "Inferred",
    "raises": "Raised",
    "reviews": "Reviewed",
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


def derive_question_source_relations(graph, node_index):
    relations_by_question = defaultdict(list)
    for edge in graph.get("edges", []):
        source_question = node_index.get(edge.get("source_id"))
        question = node_index.get(edge.get("target_id"))
        if (
            source_question
            and question
            and source_question.get("type") == "source_question"
            and question.get("type") == "question"
            and edge.get("relation") in {"supports", "variant_of", "relates_to"}
        ):
            relations_by_question[question["id"]].append({
                "source_id": source_question.get("source_id"),
                "source_question_id": source_question.get("id"),
                "relation": edge.get("relation"),
                "edge": edge,
            })
    return relations_by_question


def derive_source_question_origins(graph, node_index):
    origins = {}
    for edge in graph.get("edges", []):
        source = node_index.get(edge.get("source_id"))
        target = node_index.get(edge.get("target_id"))
        if source and target and source.get("type") == "source" and target.get("type") == "source_question":
            origins[target["id"]] = edge.get("relation")
    return origins


def derive_theme_memberships(graph, node_index, support_by_question):
    memberships_by_question = defaultdict(list)
    theme_order = {theme["id"]: index for index, theme in enumerate(graph.get("themes", []))}

    for edge in graph.get("edges", []):
        source = node_index.get(edge.get("source_id"))
        target = edge.get("target_id")
        if source and source.get("type") == "question" and target in theme_order and edge.get("relation") == "member_of":
            memberships_by_question[source["id"]].append({
                "theme_id": target,
                "role": edge.get("role"),
            })

    for theme in graph.get("themes", []):
        for question_id in theme.get("question_ids", []):
            if not any(item["theme_id"] == theme["id"] for item in memberships_by_question[question_id]):
                memberships_by_question[question_id].append({"theme_id": theme["id"], "role": None})

    for question_id, memberships in memberships_by_question.items():
        explicit_primary = [item for item in memberships if item.get("role") == "primary"]
        if explicit_primary:
            primary = explicit_primary[0]
        else:
            question = node_index[question_id]
            scored = []
            for item in memberships:
                theme = next(candidate for candidate in graph["themes"] if candidate["id"] == item["theme_id"])
                support_count = len(support_by_question[question_id])
                label_bonus = (
                    1
                    if question.get("question_type") == "methodological"
                    and any(word in theme.get("label", "").lower() for word in ("measurement", "evidence", "method"))
                    else 0
                )
                scored.append((support_count + label_bonus, -theme_order[theme["id"]], item))
            primary = max(scored, key=lambda value: (value[0], value[1]))[2]
        for item in memberships:
            item["role"] = "primary" if item is primary else "cross_cutting"
    return memberships_by_question


def source_questions_by_source(node_index, relations_by_question):
    grouped = defaultdict(list)
    seen = set()
    for relations in relations_by_question.values():
        for relation in relations:
            source_question_id = relation["source_question_id"]
            if source_question_id in seen:
                continue
            seen.add(source_question_id)
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


def source_orientation_html(source_questions, source_question_origins):
    orientation_lines = []
    for item in source_questions:
        origin = source_question_origins.get(item.get("id"), "infers")
        tag = ORIGIN_TAG_LABELS.get(origin, "Question")
        orientation_lines.append(f"{tag} — {escape_label(item.get('question_text', ''))}")
    return "<br/>".join(f"• {line}" for line in orientation_lines)


def build_mermaid(
    graph,
    node_index,
    support_by_question,
    source_question_origins,
    theme_memberships,
    source_relations,
    wide_cards=False,
):
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
            "sources as cards on the right. Source cards distinguish stated questions from inferred questions.",
            "Solid links show direct support; dashed `related` links show secondary conceptual relationships.",
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
    source_questions = source_questions_by_source(node_index, source_relations)
    seen_sources = set()
    seen_questions = set()
    cross_cutting_edge_indexes = []
    related_edge_indexes = []
    edge_index = 0
    seen_relations = set()

    for theme in graph["themes"]:
        lines.append(f'    {theme["id"]}(("{escape_label(theme["label"])}")):::theme')
        memberships = [
            (question_id, item)
            for question_id, items in theme_memberships.items()
            for item in items
            if item["theme_id"] == theme["id"]
        ]
        for membership in memberships:
            question_id, membership = membership
            question = node_index[question_id]
            if wide_cards:
                orientation_lines = []
                for source_question_id in support_by_question[question_id]:
                    source_question = node_index[source_question_id]
                    source = node_index[source_question["source_id"]]
                    text = source_question.get("question_text", "")
                    origin = source_question_origins.get(source_question_id, "infers")
                    tag = ORIGIN_TAG_LABELS.get(origin, "Question")
                    orientation_lines.append(f"• Direct — {source_link(source)} — {tag} — <i>{escape_label(text)}</i>")
                for relation in source_relations.get(question_id, []):
                    if relation["relation"] == "supports":
                        continue
                    source_question = node_index[relation["source_question_id"]]
                    source = node_index[relation["source_id"]]
                    text = source_question.get("question_text", "")
                    origin = source_question_origins.get(relation["source_question_id"], "infers")
                    tag = ORIGIN_TAG_LABELS.get(origin, "Question")
                    orientation_lines.append(f"• Related — {source_link(source)} — {tag} — <i>{escape_label(text)}</i>")
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
            if question_id not in seen_questions:
                seen_questions.add(question_id)
                lines.append(f'    {question_id}["{label}"]:::question')
            if membership["role"] == "primary":
                lines.append(f'    {theme["id"]} --> {question_id}')
            else:
                lines.append(f'    {theme["id"]} -. cross-cutting .-> {question_id}')
                cross_cutting_edge_indexes.append(edge_index)
            edge_index += 1
            if not wide_cards:
                if membership["role"] == "primary":
                    for source_question_id in support_by_question[question_id]:
                        source_question = node_index[source_question_id]
                        source = node_index[source_question["source_id"]]
                        if source["id"] not in seen_sources:
                            seen_sources.add(source["id"])
                            orientation_text = source_orientation_html(source_questions[source["id"]], source_question_origins)
                            source_label = (
                                "<div style='width:340px;text-align:left'>"
                                f"{source_link(source)} — <i>{orientation_text}</i>"
                                "</div>"
                            )
                            lines.append(f'    {source["id"]}["{source_label}"]:::source')
                        lines.append(f'    {question_id} --> {source["id"]}')
                        edge_index += 1
                for relation in source_relations.get(question_id, []):
                    if relation["relation"] == "supports":
                        continue
                    source = node_index.get(relation["source_id"])
                    if not source:
                        continue
                    if source["id"] not in seen_sources:
                        seen_sources.add(source["id"])
                        orientation_text = source_orientation_html(source_questions[source["id"]], source_question_origins)
                        source_label = (
                            "<div style='width:340px;text-align:left'>"
                            f"{source_link(source)} — <i>{orientation_text}</i>"
                            "</div>"
                        )
                        lines.append(f'    {source["id"]}["{source_label}"]:::source')
                    relation_key = (question_id, source["id"], relation["relation"])
                    if relation_key not in seen_relations:
                        seen_relations.add(relation_key)
                        lines.append(f'    {question_id} -. related .-> {source["id"]}')
                        related_edge_indexes.append(edge_index)
                        edge_index += 1
        lines.append("")

    lines.extend([
        "    classDef theme fill:#ecfeff,stroke:#0e7490,stroke-width:2px;",
        "    classDef question fill:#f8fafc,stroke:#334155,stroke-width:1px,text-align:left;",
    ])
    if cross_cutting_edge_indexes:
        indexes = ",".join(str(index) for index in cross_cutting_edge_indexes)
        lines.append(f"    linkStyle {indexes} stroke:#94a3b8,stroke-width:1px,stroke-dasharray:4 3;")
    if related_edge_indexes:
        indexes = ",".join(str(index) for index in related_edge_indexes)
        lines.append(f"    linkStyle {indexes} stroke:#94a3b8,stroke-width:1px,stroke-dasharray:7 4,stroke-opacity:.65;")
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
    source_relations = derive_question_source_relations(graph, node_index)
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
            else:
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
            secondary_relations = [
                relation for relation in source_relations.get(question_id, [])
                if relation["relation"] in {"variant_of", "relates_to"}
            ]
            if secondary_relations:
                lines.extend([
                    "",
                    "**Secondary conceptual links:**",
                    "",
                    "These relationships are not counted as direct evidence support.",
                    "",
                ])
                for relation in secondary_relations:
                    source_question = node_index[relation["source_question_id"]]
                    source = node_index[relation["source_id"]]
                    edge = relation["edge"]
                    lines.append(f"- **{source_question['question_text']}**")
                    lines.append(f"  - **Source:** {markdown_link(source)}")
                    lines.append(f"  - **Relation:** {humanize(relation['relation'])} · confidence {edge.get('confidence', 'Not recorded')}")
                    lines.append(f"  - **Basis:** {edge.get('basis', 'Not recorded')}")
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


def build_edge_validation(
    graph,
    node_index,
    support_by_question,
    source_question_origins,
    theme_memberships,
    source_relations,
):
    edges = graph.get("edges", [])
    source_question_edges = [
        edge for edge in edges
        if node_index.get(edge.get("source_id"), {}).get("type") == "source"
        and node_index.get(edge.get("target_id"), {}).get("type") == "source_question"
    ]
    support_edges = [
        edge for edge in edges
        if node_index.get(edge.get("source_id"), {}).get("type") == "source_question"
        and node_index.get(edge.get("target_id"), {}).get("type") == "question"
        and edge.get("relation") == "supports"
    ]
    secondary_edges = [
        edge for edge in edges
        if node_index.get(edge.get("source_id"), {}).get("type") == "source_question"
        and node_index.get(edge.get("target_id"), {}).get("type") == "question"
        and edge.get("relation") in {"variant_of", "relates_to"}
    ]
    membership_edges = [
        edge for edge in edges
        if node_index.get(edge.get("source_id"), {}).get("type") == "question"
        and edge.get("relation") == "member_of"
    ]
    role_by_edge = {edge.get("id"): edge.get("role") for edge in membership_edges}
    primary_memberships = [edge_id for edge_id, role in role_by_edge.items() if role == "primary"]
    cross_cutting_memberships = [edge_id for edge_id, role in role_by_edge.items() if role == "cross_cutting"]
    edge_audit = graph.get("run", {}).get("edge_audit") or []
    inferred_memberships = []
    for question_id, memberships in theme_memberships.items():
        for item in memberships:
            edge = next(
                (candidate for candidate in membership_edges if candidate.get("source_id") == question_id and candidate.get("target_id") == item["theme_id"]),
                None,
            )
            if edge is None or not edge.get("role"):
                inferred_memberships.append({
                    "question_id": question_id,
                    "theme_id": item["theme_id"],
                    "role": item["role"],
                })

    lines = [
        "# Edge validation",
        "",
        f"**Audited graph:** `{graph['run']['run_id']}`",
        f"**Edges:** {len(edges)}",
        "",
        "## Summary",
        "",
        "| Edge group | Count |",
        "|---|---:|",
        f"| Source → source question | {len(source_question_edges)} |",
        f"| Source question → canonical question (direct support) | {len(support_edges)} |",
        f"| Source question → canonical question (secondary conceptual) | {len(secondary_edges)} |",
        f"| Question → primary theme membership | {len(primary_memberships)} |",
        f"| Question → cross-cutting theme membership | {len(cross_cutting_memberships)} |",
        "",
        "## Interpretation",
        "",
        "- Direct support is limited to `source_question -> question` edges with relation `supports`.",
        "- A source question may have more than one direct-support edge when each edge has evidence.",
        "- Secondary conceptual links use `variant_of` or `relates_to` and are not counted as direct evidence support.",
        "- Source cards distinguish `asks` (stated) from `infers` (inferred) where the graph records that distinction.",
        "- Theme membership is shown once for primary containment and as cross-cutting for secondary relevance.",
        "",
    ]
    if edge_audit:
        lines.extend([
            "## Recorded edge corrections",
            "",
            "| Edge | Correction | Reason |",
            "|---|---|---|",
        ])
        for correction in edge_audit:
            edge_id = correction.get("edge_id", "Not recorded")
            change = correction.get("correction", "Not recorded")
            if correction.get("from") or correction.get("to"):
                change = f"{change}: {correction.get('from', 'not recorded')} → {correction.get('to', 'not recorded')}"
            reason = correction.get("reason", "Not recorded")
            lines.append(f"| `{edge_id}` | {change} | {reason} |")
        lines.append("")
    if inferred_memberships:
        lines.extend([
            "## Inferred membership roles",
            "",
            "These memberships had no explicit `role`; the builder assigned a primary theme from direct support and question type, and marked the rest as cross-cutting.",
            "",
            "| Question | Theme | Assigned role |",
            "|---|---|---|",
        ])
        for item in inferred_memberships:
            lines.append(
                f"| {item['question_id']} | {item['theme_id']} | {item['role']} |"
            )
        lines.append("")
    lines.extend([
        "## Limitations",
        "",
        "- This audit summarizes edge semantics; it does not replace source-level evidence review.",
        "- Corrections made during graph construction should still be recorded in the run log.",
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

    source_question_origins = derive_source_question_origins(graph, node_index)
    theme_memberships = derive_theme_memberships(graph, node_index, support_by_question)
    source_relations = derive_question_source_relations(graph, node_index)
    write_text(output_dir / "question-map-mermaid.md", build_mermaid(graph, node_index, support_by_question, source_question_origins, theme_memberships, source_relations, args.wide_cards))
    write_text(output_dir / "question-map.md", build_linear(graph, node_index, support_by_question))
    write_text(output_dir / "edge-validation.md", build_edge_validation(graph, node_index, support_by_question, source_question_origins, theme_memberships, source_relations))
    shutil.copyfile(html_template, output_dir / "question-map-force.html")
    print(f"Generated visualization artifacts in {output_dir}.")


if __name__ == "__main__":
    main()
