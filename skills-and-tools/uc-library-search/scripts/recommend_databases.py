#!/usr/bin/env python3
"""Recommend UCSD A-Z databases from normalized metadata."""

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_INPUT = "references/az_databases.json"


def parse_terms(query):
    phrases = re.findall(r'"([^"]+)"', query)
    remainder = re.sub(r'"[^"]+"', " ", query)
    words = re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", remainder)
    boolean_operators = {"and", "or", "not"}
    words = [word for word in words if word.casefold() not in boolean_operators]
    return list(dict.fromkeys(phrases + words))


def rank_bonus(rank):
    if rank <= 0:
        return 0
    if rank == 1:
        return 4
    if rank == 2:
        return 2
    return 1


def score_asset(asset, terms, subjects, types):
    name = asset["name"].casefold()
    alt_names = [name.casefold() for name in asset["alt_names"]]
    subject_text = " ".join(asset["subjects"]).casefold()
    type_text = " ".join(asset["types"]).casefold()
    description_text = " ".join([asset["description"], asset["more_info"]]).casefold()
    featured_names = {item["name"].casefold() for item in asset["featured_subjects"]}
    reasons = []
    score = 0

    subject_matches = [subject for subject in subjects if subject.casefold() in subject_text]
    featured_matches = [subject for subject in subjects if subject.casefold() in featured_names]
    type_matches = [type_name for type_name in types if type_name.casefold() in type_text]

    if featured_matches:
        best_rank = min(item["rank"] for item in asset["featured_subjects"] if item["name"].casefold() in {s.casefold() for s in featured_matches})
        score += 8 + rank_bonus(best_rank)
        reasons.append("Featured subject match: {}".format(", ".join(featured_matches)))
    if subject_matches:
        score += 4
        reasons.append("Subject match: {}".format(", ".join(subject_matches)))
    if type_matches:
        score += 2
        reasons.append("Type match: {}".format(", ".join(type_matches)))

    term_matches = {
        "name": [],
        "alt_names": [],
        "subjects": [],
        "description": [],
    }
    for term in terms:
        folded_term = term.casefold()
        if any(folded_term in candidate for candidate in alt_names):
            term_matches["alt_names"].append(term)
        elif folded_term in name:
            term_matches["name"].append(term)
        if folded_term in subject_text:
            term_matches["subjects"].append(term)
        if folded_term in description_text:
            term_matches["description"].append(term)

    if term_matches["name"]:
        score += 3 * len(term_matches["name"])
        reasons.append("Name match: {}".format(", ".join(term_matches["name"])))
    if term_matches["alt_names"]:
        score += 3 * len(term_matches["alt_names"])
        reasons.append("Alt-name match: {}".format(", ".join(term_matches["alt_names"])))
    if term_matches["subjects"]:
        score += 2 * len(term_matches["subjects"])
        reasons.append("Subject-term match: {}".format(", ".join(term_matches["subjects"])))
    if term_matches["description"]:
        score += 1 * len(term_matches["description"])
        reasons.append("Description match: {}".format(", ".join(term_matches["description"])))

    if len(featured_names) > 1:
        score += 1
        reasons.append("Interdisciplinary featured coverage")

    return score, reasons


def main():
    parser = argparse.ArgumentParser(
        description="Recommend UCSD A-Z databases from normalized metadata."
    )
    parser.add_argument("--query", required=True, help="User concepts, keywords, or quoted phrases.")
    parser.add_argument("--subjects", default="", help="Comma-delimited subject names.")
    parser.add_argument("--types", default="", help="Comma-delimited A-Z type names.")
    parser.add_argument("--limit", type=int, default=4, help="Maximum recommendations (default: 4).")
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Normalized JSON path, relative to skill.")
    args = parser.parse_args()

    if args.limit < 1:
        parser.error("--limit must be at least 1.")

    data_path = ROOT / args.input
    assets = json.loads(data_path.read_text(encoding="utf-8"))
    subjects = [subject.strip() for subject in args.subjects.split(",") if subject.strip()]
    types = [type_name.strip() for type_name in args.types.split(",") if type_name.strip()]
    terms = parse_terms(args.query)

    scored = []
    for asset in assets:
        if asset["name"].casefold().startswith(("z-", "zz-")):
            continue
        score, reasons = score_asset(asset, terms, subjects, types)
        if score > 0:
            scored.append((score, asset, reasons))

    scored.sort(key=lambda item: (-item[0], item[1]["name"].casefold()))
    for score, asset, reasons in scored[: args.limit]:
        output = {
            "score": score,
            "name": asset["name"],
            "url": asset["url"],
            "friendly_url": asset["friendly_url"],
            "vendor": asset["vendor"],
            "types": asset["types"],
            "subjects": asset["subjects"],
            "featured_subjects": asset["featured_subjects"],
            "access_notes": asset["access_notes"],
            "alt_names": asset["alt_names"],
            "reasons": reasons,
        }
        print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("ERROR: {}".format(exc), file=sys.stderr)
        sys.exit(1)
