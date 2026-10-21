#!/usr/bin/env python3
"""Validate a question_map.json graph (schema v0.1).

Checks required fields, enums, IDs, evidence links, theme support, and core
referential integrity. Exits 0 when valid, 1 when invalid, and 2 when the
input cannot be loaded.
"""

import argparse
import json
import sys

CONFIDENCE = {"high", "medium", "low"}
ROOT_STATUS = {"primary_user_root", "inquiry_root", "none"}
ACCESS_LEVEL = {"full_text", "abstract_only", "publisher_description", "metadata_only"}
EVIDENCE_BASIS = {
    "full_text_machine_readable",
    "abstract_and_metadata",
    "publisher_description_and_toc",
    "metadata_only",
}
SELECTION_STATUS = {"selected", "candidate", "excluded"}
CONNECTION_TYPE = {"direct_evidence", "reasonable_inference", "interpretive_connection"}
QUESTION_TYPE = {
    "empirical",
    "methodological",
    "theoretical",
    "policy",
    "interpretive",
    "comparative",
    "measurement",
    "intervention",
    "equity",
    "gap",
}
NODE_TYPES = {
    "question",
    "source_question",
    "next_question",
    "source",
    "discipline",
    "method",
    "population",
    "geography",
    "context",
    "concept",
}
SUPPORT_TIERS = {
    "single_question",
    "single_source",
    "multi_question",
    "multi_source",
    "multi_source_multi_question",
}
EDGE_ROLES = {"primary", "cross_cutting"}

EDGE_RELATIONS = {
    ("source", "source_question"): {"asks", "infers", "raises", "reviews"},
    ("source_question", "question"): {"supports", "variant_of", "relates_to"},
    ("question", "question"): {
        "relates_to",
        "refines",
        "generalizes",
        "specifies",
        "contrasts_with",
        "co_occurs_with",
    },
    ("question", "next_question"): {"proposes", "narrows_to", "extends_to"},
    ("question", "theme"): {"member_of", "proposed_for"},
    ("next_question", "theme"): {"member_of", "proposed_for"},
    ("source", "source"): {"cites", "similar_to", "contrasts_with"},
    ("source", "discipline"): {"informs", "uses", "studies", "located_in", "applies_to"},
    ("source", "method"): {"informs", "uses", "studies", "located_in", "applies_to"},
    ("source", "population"): {"informs", "uses", "studies", "located_in", "applies_to"},
    ("source", "geography"): {"informs", "uses", "studies", "located_in", "applies_to"},
    ("source", "context"): {"informs", "uses", "studies", "located_in", "applies_to"},
    ("source", "concept"): {"informs", "uses", "studies", "located_in", "applies_to"},
}


def is_nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def require_enum(value, allowed, label, errors):
    require(value in allowed, f"ERROR {label} has invalid value {value!r}", errors)


def validate_top_level(data, errors):
    require(isinstance(data, dict), "ERROR top-level object must be a JSON object", errors)
    if not isinstance(data, dict):
        return
    for key in ("schema_version", "run", "request", "search_log", "nodes", "edges", "quotes", "themes", "coverage", "limitations"):
        require(key in data, f"ERROR missing top-level field: {key}", errors)
    require(
        isinstance(data.get("schema_version"), str) and data["schema_version"].startswith("0."),
        "ERROR schema_version must be a 0.x string",
        errors,
    )
    for key in ("run", "request", "search_log", "coverage"):
        require(isinstance(data.get(key), dict), f"ERROR {key} must be an object", errors)
    for key in ("nodes", "edges", "quotes", "themes", "limitations"):
        require(isinstance(data.get(key), list), f"ERROR {key} must be a list", errors)


def validate_run(data, errors):
    run = data.get("run") or {}
    for key in ("run_id", "topic_slug", "generated_at", "skill_version", "data_model_version"):
        require(is_nonempty_string(run.get(key)), f"ERROR run.{key} must be a non-empty string", errors)
    require_enum(run.get("confirmation_status"), {"user_confirmed", "initial_prompt_only", "blocked"}, "run.confirmation_status", errors)
    require_enum(run.get("breadth"), {"focused", "comprehensive", "exhaustive"}, "run.breadth", errors)
    rule = run.get("theme_creation_rule")
    require(isinstance(rule, dict), "ERROR run.theme_creation_rule must be an object", errors)
    if isinstance(rule, dict):
        require(is_nonempty_string(rule.get("rule")), "ERROR run.theme_creation_rule.rule must be non-empty", errors)
        require(is_nonempty_string(rule.get("rationale")), "ERROR run.theme_creation_rule.rationale must be non-empty", errors)

    edge_audit = run.get("edge_audit")
    if edge_audit is not None:
        require(isinstance(edge_audit, list), "ERROR run.edge_audit must be a list", errors)
        for index, entry in enumerate(edge_audit or []):
            require(
                isinstance(entry, dict) and is_nonempty_string(entry.get("edge_id")) and is_nonempty_string(entry.get("reason")),
                f"ERROR run.edge_audit[{index}] must include edge_id and reason",
                errors,
            )

    for weight_key in ("question_score_weights", "theme_score_weights"):
        weights = run.get(weight_key)
        if weights is None:
            continue
        require(isinstance(weights, dict), f"ERROR run.{weight_key} must be an object", errors)
        if isinstance(weights, dict) and weights:
            numeric = [v for v in weights.values() if isinstance(v, (int, float))]
            require(
                len(numeric) == len(weights) and abs(sum(numeric) - 1.0) < 0.01,
                f"ERROR run.{weight_key} numeric weights must sum to 1.0",
                errors,
            )


def validate_request(data, errors):
    request = data.get("request") or {}
    require(is_nonempty_string(request.get("core_question")), "ERROR request.core_question must be non-empty", errors)
    require_enum(request.get("confirmation_status"), {"user_confirmed", "initial_prompt_only", "blocked"}, "request.confirmation_status", errors)
    require_enum(request.get("breadth"), {"focused", "comprehensive", "exhaustive"}, "request.breadth", errors)


def validate_search_log(data, errors):
    log = data.get("search_log") or {}
    ucls = log.get("uc_library_search") or {}
    require(isinstance(ucls, dict), "ERROR search_log.uc_library_search must be an object", errors)
    if isinstance(ucls, dict):
        require_enum(
            ucls.get("mode"),
            {"primo_search_api", "primo_pnx_rest", "documented_skip"},
            "search_log.uc_library_search.mode",
            errors,
        )
        if ucls.get("mode") == "documented_skip":
            require(is_nonempty_string(ucls.get("skip_reason")), "ERROR a documented UC Library Search skip requires skip_reason", errors)
            require(is_nonempty_string(ucls.get("coverage_consequence")), "ERROR a documented UC Library Search skip requires coverage_consequence", errors)
    for key in ("queries", "component_decomposition", "adaptive_refinements", "api_calls", "skips"):
        require(isinstance(log.get(key), list), f"ERROR search_log.{key} must be a list", errors)
    coverage = log.get("component_coverage")
    if coverage is not None:
        require(isinstance(coverage, list), "ERROR search_log.component_coverage must be a list", errors)
        for index, entry in enumerate(coverage or []):
            require(
                isinstance(entry, dict)
                and is_nonempty_string(entry.get("component"))
                and entry.get("coverage_status") in {"covered", "weak", "not_found_in_retrieved_coverage"},
                f"ERROR search_log.component_coverage[{index}] requires component and a valid coverage_status",
                errors,
            )


def validate_nodes(data, node_index, errors):
    nodes = data.get("nodes") or []
    seen = set()
    for index, node in enumerate(nodes):
        label = f"nodes[{index}]"
        if not isinstance(node, dict):
            errors.append(f"ERROR {label} must be an object")
            continue
        node_id = node.get("id")
        node_type = node.get("type")
        require(is_nonempty_string(node_id), f"ERROR {label}.id must be non-empty", errors)
        require(node_type in NODE_TYPES, f"ERROR {label}.type has invalid value {node_type!r}", errors)
        if not is_nonempty_string(node_id) or node_type not in NODE_TYPES:
            continue
        require(node_id not in seen, f"ERROR duplicate node id: {node_id}", errors)
        seen.add(node_id)
        node_index[node_id] = node
        require_enum(node.get("confidence"), CONFIDENCE, f"{label}.confidence", errors)
        if "root_status" in node:
            require_enum(node.get("root_status"), ROOT_STATUS, f"{label}.root_status", errors)

        if node_type == "question":
            require(is_nonempty_string(node.get("canonical_label")), f"ERROR {label}.canonical_label must be non-empty", errors)
            require(is_nonempty_string(node.get("question_text")), f"ERROR {label}.question_text must be non-empty", errors)
            require_enum(node.get("origin"), {"user_defined", "explicit", "inferred"}, f"{label}.origin", errors)
            if "question_type" in node:
                require_enum(node.get("question_type"), QUESTION_TYPE, f"{label}.question_type", errors)
        elif node_type == "source_question":
            require(is_nonempty_string(node.get("source_id")), f"ERROR {label}.source_id must be non-empty", errors)
            require(is_nonempty_string(node.get("question_text")), f"ERROR {label}.question_text must be non-empty", errors)
            require_enum(node.get("origin"), {"explicit", "inferred"}, f"{label}.origin", errors)
            require_enum(node.get("connection_type"), CONNECTION_TYPE, f"{label}.connection_type", errors)
            require_enum(node.get("access_level"), ACCESS_LEVEL, f"{label}.access_level", errors)
            require_enum(node.get("evidence_basis"), EVIDENCE_BASIS, f"{label}.evidence_basis", errors)
            require(is_nonempty_string(node.get("extraction_rationale")), f"ERROR {label}.extraction_rationale must be non-empty", errors)
            require(isinstance(node.get("quote_ids"), list), f"ERROR {label}.quote_ids must be a list", errors)
            if node.get("evidence_basis") == "metadata_only":
                require(
                    is_nonempty_string(node.get("metadata_rationale")),
                    f"ERROR {label} with metadata_only evidence requires metadata_rationale",
                    errors,
                )
            else:
                require(
                    bool(node.get("quote_ids")),
                    f"ERROR {label} with non-metadata evidence requires at least one quote_id",
                    errors,
                )
            if node.get("origin") == "inferred":
                require(
                    bool(node.get("quote_ids")) or is_nonempty_string(node.get("metadata_rationale")),
                    f"ERROR inferred {label} requires quote or metadata-derived rationale",
                    errors,
                )
        elif node_type == "next_question":
            require(is_nonempty_string(node.get("question_text")), f"ERROR {label}.question_text must be non-empty", errors)
            require_enum(
                node.get("origin"),
                {"structure_narrowing", "slot_substitution", "source_gap", "user_intent"},
                f"{label}.origin",
                errors,
            )
            require(is_nonempty_string(node.get("generation_basis")), f"ERROR {label}.generation_basis must be non-empty", errors)
            require(is_nonempty_string(node.get("rationale")), f"ERROR {label}.rationale must be non-empty", errors)
            require(isinstance(node.get("parent_question_ids"), list), f"ERROR {label}.parent_question_ids must be a list", errors)
            require(isinstance(node.get("parent_theme_ids"), list), f"ERROR {label}.parent_theme_ids must be a list", errors)
            require(
                bool(node.get("parent_question_ids")) or bool(node.get("parent_theme_ids")),
                f"ERROR {label} requires at least one parent question or theme",
                errors,
            )
            require(isinstance(node.get("slot_substitutions"), dict), f"ERROR {label}.slot_substitutions must be an object", errors)
            require(isinstance(node.get("launch_ready"), bool), f"ERROR {label}.launch_ready must be boolean", errors)
        elif node_type == "source":
            require(is_nonempty_string(node.get("title")), f"ERROR {label}.title must be non-empty", errors)
            if "access_level" in node:
                require_enum(node.get("access_level"), ACCESS_LEVEL, f"{label}.access_level", errors)
            if "evidence_basis" in node:
                require_enum(node.get("evidence_basis"), EVIDENCE_BASIS, f"{label}.evidence_basis", errors)
            if "selection_status" in node:
                require_enum(node.get("selection_status"), SELECTION_STATUS, f"{label}.selection_status", errors)
            citation = node.get("citation_metadata")
            if citation is not None:
                require(isinstance(citation, dict), f"ERROR {label}.citation_metadata must be an object", errors)
                if isinstance(citation, dict) and "primary_count" in citation:
                    require(is_nonempty_string(citation.get("primary_provider")), f"ERROR {label}.citation_metadata.primary_provider is required", errors)
                    require(is_nonempty_string(citation.get("retrieved_at")), f"ERROR {label}.citation_metadata.retrieved_at is required", errors)
            for citation_field in ("citation_short", "citation_display", "ucls_permalink"):
                if citation_field in node:
                    require(is_nonempty_string(node.get(citation_field)), f"ERROR {label}.{citation_field} must be non-empty", errors)
        else:
            require(is_nonempty_string(node.get("label")), f"ERROR {label}.label must be non-empty", errors)
            if node_type == "context":
                require(is_nonempty_string(node.get("statement")), f"ERROR {label}.statement must be non-empty", errors)
                require(is_nonempty_string(node.get("rationale")), f"ERROR {label}.rationale must be non-empty", errors)

    return seen


def validate_quotes(data, node_index, errors):
    quotes = data.get("quotes") or []
    quote_index = {}
    for index, quote in enumerate(quotes):
        label = f"quotes[{index}]"
        if not isinstance(quote, dict):
            errors.append(f"ERROR {label} must be an object")
            continue
        quote_id = quote.get("quote_id")
        require(is_nonempty_string(quote_id), f"ERROR {label}.quote_id must be non-empty", errors)
        if not is_nonempty_string(quote_id):
            continue
        require(quote_id not in quote_index, f"ERROR duplicate quote id: {quote_id}", errors)
        quote_index[quote_id] = quote
        source_id = quote.get("source_id")
        require(is_nonempty_string(source_id), f"ERROR {label}.source_id must be non-empty", errors)
        if is_nonempty_string(source_id):
            source = node_index.get(source_id)
            require(source is not None and source.get("type") == "source", f"ERROR {label}.source_id does not resolve to a source node", errors)
        require(is_nonempty_string(quote.get("text")), f"ERROR {label}.text must be non-empty", errors)
        require(is_nonempty_string(quote.get("locator")), f"ERROR {label}.locator must be non-empty", errors)
        require_enum(quote.get("access_level"), ACCESS_LEVEL, f"{label}.access_level", errors)
        require_enum(quote.get("evidence_basis"), EVIDENCE_BASIS, f"{label}.evidence_basis", errors)
        require_enum(quote.get("confidence"), CONFIDENCE, f"{label}.confidence", errors)
    return quote_index


def validate_edges(data, node_index, theme_index, quote_index, errors):
    edges = data.get("edges") or []
    seen_edges = set()
    seen_endpoint_relations = set()
    for index, edge in enumerate(edges):
        label = f"edges[{index}]"
        if not isinstance(edge, dict):
            errors.append(f"ERROR {label} must be an object")
            continue
        edge_id = edge.get("id")
        require(is_nonempty_string(edge_id), f"ERROR {label}.id must be non-empty", errors)
        if is_nonempty_string(edge_id):
            require(edge_id not in seen_edges, f"ERROR duplicate edge id: {edge_id}", errors)
            seen_edges.add(edge_id)
        source_id = edge.get("source_id")
        target_id = edge.get("target_id")
        require(is_nonempty_string(source_id), f"ERROR {label}.source_id must be non-empty", errors)
        require(is_nonempty_string(target_id), f"ERROR {label}.target_id must be non-empty", errors)
        require(is_nonempty_string(edge.get("relation")), f"ERROR {label}.relation must be non-empty", errors)
        require_enum(edge.get("confidence"), CONFIDENCE, f"{label}.confidence", errors)
        require(is_nonempty_string(edge.get("basis")), f"ERROR {label}.basis must be non-empty", errors)
        if not (is_nonempty_string(source_id) and is_nonempty_string(target_id)):
            continue
        source = node_index.get(source_id) or theme_index.get(source_id)
        target = node_index.get(target_id) or theme_index.get(target_id)
        require(source is not None, f"ERROR {label}.source_id does not resolve: {source_id}", errors)
        require(target is not None, f"ERROR {label}.target_id does not resolve: {target_id}", errors)
        if source is None or target is None:
            continue
        source_type = source.get("type")
        target_type = target.get("type")
        relation = edge.get("relation")
        endpoint_relation = (source_id, target_id, relation)
        require(
            endpoint_relation not in seen_endpoint_relations,
            f"ERROR duplicate edge endpoint and relation: {endpoint_relation}",
            errors,
        )
        seen_endpoint_relations.add(endpoint_relation)
        allowed = EDGE_RELATIONS.get((source_type, target_type))
        require(
            allowed is not None and relation in allowed,
            f"ERROR {label} has unsupported relation {source_type} --{relation}--> {target_type}",
            errors,
        )
        if "role" in edge:
            require_enum(edge.get("role"), EDGE_ROLES, f"{label}.role", errors)
        evidence_ids = edge.get("evidence_ids") or []
        require(isinstance(evidence_ids, list), f"ERROR {label}.evidence_ids must be a list", errors)
        for evidence_id in evidence_ids:
            require(evidence_id in quote_index, f"ERROR {label}.evidence_id does not resolve: {evidence_id}", errors)

    validate_edge_semantics(edges, node_index, theme_index, quote_index, errors)


def validate_edge_semantics(edges, node_index, theme_index, quote_index, errors):
    support_counts = {}
    membership_edges = {}
    for edge in edges:
        if not isinstance(edge, dict):
            continue
        source = node_index.get(edge.get("source_id"))
        target = node_index.get(edge.get("target_id")) or theme_index.get(edge.get("target_id"))
        if source is None or target is None:
            continue
        source_type = source.get("type")
        target_type = target.get("type")
        relation = edge.get("relation")
        label = edge.get("id") or "unnamed edge"

        if source_type == "source" and target_type == "source_question":
            if target.get("evidence_basis") == "metadata_only":
                require(
                    not edge.get("evidence_ids"),
                    f"ERROR {label} to metadata_only source_question should rely on metadata_rationale, not quote evidence",
                    errors,
                )
            else:
                require(
                    bool(edge.get("evidence_ids")),
                    f"ERROR {label} from source to source_question requires evidence_ids",
                    errors,
                )
            expected_origin = {"asks": "explicit", "infers": "inferred", "raises": "inferred", "reviews": "explicit"}.get(relation)
            require(
                expected_origin is None or target.get("origin") == expected_origin,
                f"ERROR {label} uses {relation} but source_question {target.get('id')} does not have {expected_origin} origin",
                errors,
            )

        elif source_type == "source_question" and target_type == "question":
            allowed_evidence = set(source.get("quote_ids") or [])
            if source.get("evidence_basis") != "metadata_only":
                require(
                    bool(edge.get("evidence_ids")),
                    f"ERROR {label} with non-metadata evidence requires evidence_ids",
                    errors,
                )
            for evidence_id in edge.get("evidence_ids") or []:
                quote = quote_index.get(evidence_id)
                if quote:
                    require(
                        quote.get("source_id") == source.get("source_id"),
                        f"ERROR {label} evidence {evidence_id} belongs to a different source",
                        errors,
                    )
                    require(
                        not allowed_evidence or evidence_id in allowed_evidence,
                        f"ERROR {label} evidence {evidence_id} is not listed on source_question {source.get('id')}",
                        errors,
                    )
            if relation == "supports":
                support_counts[source.get("id")] = support_counts.get(source.get("id"), 0) + 1
            elif relation in {"variant_of", "relates_to"}:
                require(
                    edge.get("confidence") != "high",
                    f"ERROR {label} uses {relation} and should not have high confidence",
                    errors,
                )

        elif source_type == "question" and target_type == "theme" and relation == "member_of":
            require(
                edge.get("role") in EDGE_ROLES,
                f"ERROR {label} member_of edge requires role primary or cross_cutting",
                errors,
            )
            membership_edges.setdefault(source.get("id"), []).append(edge)

    for source_question_id, node in node_index.items():
        if node.get("type") == "source_question":
            require(
                support_counts.get(source_question_id, 0) >= 1,
                f"ERROR source_question {source_question_id} has no evidence-backed supports edge",
                errors,
            )

    for question_id, question_edges in membership_edges.items():
        roles = [edge.get("role") for edge in question_edges]
        require(
            roles.count("primary") == 1,
            f"ERROR question {question_id} has {roles.count('primary')} primary theme memberships; expected exactly 1",
            errors,
        )
        require(
            all(role in EDGE_ROLES for role in roles),
            f"ERROR question {question_id} has an invalid theme-membership role",
            errors,
        )


def support_tier_for_counts(question_count, source_count):
    if question_count > 1 and source_count > 1:
        return "multi_source_multi_question"
    if source_count > 1:
        return "multi_source"
    if question_count > 1:
        return "multi_question"
    if question_count == 1:
        return "single_question"
    if source_count == 1:
        return "single_source"
    return None


def validate_themes(data, node_index, theme_index, errors):
    themes = data.get("themes") or []
    for index, theme in enumerate(themes):
        label = f"themes[{index}]"
        if not isinstance(theme, dict):
            errors.append(f"ERROR {label} must be an object")
            continue
        theme_id = theme.get("id")
        require(is_nonempty_string(theme_id), f"ERROR {label}.id must be non-empty", errors)
        require(theme.get("type") == "theme", f"ERROR {label}.type must be theme", errors)
        require(is_nonempty_string(theme.get("label")), f"ERROR {label}.label must be non-empty", errors)
        require(is_nonempty_string(theme.get("statement")), f"ERROR {label}.statement must be non-empty", errors)
        require(is_nonempty_string(theme.get("rationale")), f"ERROR {label}.rationale must be non-empty", errors)
        require(is_nonempty_string(theme.get("coherence_basis")), f"ERROR {label}.coherence_basis must be non-empty", errors)
        require_enum(theme.get("confidence"), CONFIDENCE, f"{label}.confidence", errors)
        if not is_nonempty_string(theme_id):
            continue
        require(theme_id not in theme_index and theme_id not in node_index, f"ERROR duplicate theme id: {theme_id}", errors)
        theme_index[theme_id] = theme

        question_ids = theme.get("question_ids") or []
        source_ids = theme.get("source_ids") or []
        next_question_ids = theme.get("next_question_ids") or []
        for field, values, expected_type in (
            ("question_ids", question_ids, "question"),
            ("source_ids", source_ids, "source"),
            ("next_question_ids", next_question_ids, "next_question"),
        ):
            require(isinstance(values, list), f"ERROR {label}.{field} must be a list", errors)
            for value in values:
                node = node_index.get(value)
                require(
                    node is not None and node.get("type") == expected_type,
                    f"ERROR {label}.{field} does not resolve to a {expected_type}: {value}",
                    errors,
                )

        summary = theme.get("support_summary") or {}
        require(isinstance(summary, dict), f"ERROR {label}.support_summary must be an object", errors)
        if isinstance(summary, dict):
            for key, expected in (
                ("question_count", len(question_ids)),
                ("source_count", len(source_ids)),
                ("next_question_count", len(next_question_ids)),
            ):
                require(summary.get(key) == expected, f"ERROR {label}.support_summary.{key} does not match the theme lists", errors)
            tier = support_tier_for_counts(summary.get("question_count", 0), summary.get("source_count", 0))
            require(tier is not None, f"ERROR {label} has no supported question or source", errors)
            if tier:
                require_enum(theme.get("support_tier"), SUPPORT_TIERS, f"{label}.support_tier", errors)
                require(theme.get("support_tier") == tier, f"ERROR {label}.support_tier should be {tier}", errors)


def validate_coverage_and_limitations(data, errors):
    coverage = data.get("coverage") or {}
    statements = coverage.get("not_found_statements") or []
    require(isinstance(statements, list), "ERROR coverage.not_found_statements must be a list", errors)
    for index, statement in enumerate(statements):
        text = statement.get("statement") if isinstance(statement, dict) else statement
        require(
            isinstance(text, str) and "not found in retrieved coverage" in text.lower(),
            f"ERROR coverage.not_found_statements[{index}] must use 'not found in retrieved coverage'",
            errors,
        )
    limitations = data.get("limitations") or []
    require(bool(limitations), "ERROR limitations must contain at least one limitation", errors)
    for index, limitation in enumerate(limitations):
        require(
            isinstance(limitation, str) and bool(limitation.strip()),
            f"ERROR limitations[{index}] must be a non-empty string",
            errors,
        )


def validate_question_map(data):
    errors = []
    validate_top_level(data, errors)
    if errors:
        return errors
    validate_run(data, errors)
    validate_request(data, errors)
    validate_search_log(data, errors)
    node_index = {}
    validate_nodes(data, node_index, errors)
    quote_index = validate_quotes(data, node_index, errors)
    theme_index = {}
    validate_themes(data, node_index, theme_index, errors)
    validate_edges(data, node_index, theme_index, quote_index, errors)
    validate_coverage_and_limitations(data, errors)

    for index, correction in enumerate((data.get("run") or {}).get("edge_audit") or []):
        if not isinstance(correction, dict):
            continue
        edge_id = correction.get("edge_id")
        if edge_id and edge_id not in {edge.get("id") for edge in data.get("edges") or []}:
            errors.append(f"ERROR run.edge_audit[{index}] references missing edge: {edge_id}")

    for node_id, node in node_index.items():
        if node.get("type") != "source_question":
            continue
        source = node_index.get(node.get("source_id"))
        if source is None or source.get("type") != "source":
            errors.append(f"ERROR source_question {node_id}.source_id does not resolve to a source: {node.get('source_id')}")

    for node_id, node in node_index.items():
        if node.get("type") != "source_question":
            continue
        for quote_id in node.get("quote_ids") or []:
            if quote_id not in quote_index:
                errors.append(f"ERROR source_question {node_id} references missing quote: {quote_id}")
        if node.get("canonical_question_id"):
            target = node_index.get(node["canonical_question_id"])
            if target is None or target.get("type") != "question":
                errors.append(f"ERROR source_question {node_id} canonical_question_id does not resolve to a question: {node['canonical_question_id']}")

    for node_id, node in node_index.items():
        if node.get("type") != "next_question":
            continue
        for parent_id in node.get("parent_question_ids") or []:
            target = node_index.get(parent_id)
            if target is None or target.get("type") != "question":
                errors.append(f"ERROR next_question {node_id} parent_question_id does not resolve to a question: {parent_id}")
        for parent_id in node.get("parent_theme_ids") or []:
            if parent_id not in theme_index:
                errors.append(f"ERROR next_question {node_id} parent_theme_id does not resolve to a theme: {parent_id}")

    primary_roots = [node for node in node_index.values() if node.get("root_status") == "primary_user_root"]
    require(
        len(primary_roots) >= 1,
        "ERROR question_map requires at least one primary_user_root question-like node",
        errors,
    )
    return errors


def summary(data):
    nodes = data.get("nodes") or []
    type_counts = {}
    for node in nodes:
        if isinstance(node, dict):
            type_counts[node.get("type", "unknown")] = type_counts.get(node.get("type", "unknown"), 0) + 1
    return {
        "nodes": type_counts,
        "edges": len(data.get("edges") or []),
        "quotes": len(data.get("quotes") or []),
        "themes": len(data.get("themes") or []),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="path to question_map.json")
    args = parser.parse_args()
    try:
        with open(args.path, encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception as exc:
        print(f"FATAL could not load {args.path}: {exc}")
        return 2

    errors = validate_question_map(data)
    if errors:
        for error in errors:
            print(error)
        return 1

    counts = summary(data)
    print(f"question_map.json valid (schema v{data.get('schema_version')})")
    print(f"  nodes: {counts['nodes']}")
    print(f"  edges: {counts['edges']} | quotes: {counts['quotes']} | themes: {counts['themes']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
