#!/usr/bin/env python3
"""Assemble an importable QSF from a base export and a spec JSON.

The base export must be a real QSF export from the target instance.
SurveyEntry (except SurveyName), support elements, and skin are kept
verbatim; questions, blocks, and flow come from the spec.

Spec format:
{
  "survey_name": "...",
  "questions": [ {SQ payload objects, each with QuestionID} ],
  "blocks": [ {BL payload array entries} ],
  "flow": {FL payload object}
}
"""

import argparse
import json
import re
import sys


def die(errors):
    print("QSF assembly failed:", file=sys.stderr)
    for error in errors:
        print(f"  - {error}", file=sys.stderr)
    sys.exit(1)


def load_json(path, label):
    try:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        die([f"cannot read {label} {path}: {exc}"])


def element_of(base, code, primary):
    matches = [
        e for e in base["SurveyElements"]
        if e.get("Element") == code and e.get("PrimaryAttribute") == primary
    ]
    if len(matches) != 1:
        die([f"base export must contain exactly one {code} element"
             f" with PrimaryAttribute {primary!r}, found {len(matches)}"])
    return matches[0]


def validate_and_assemble(base, spec):
    errors = []
    entry = base.get("SurveyEntry")
    if not entry or "SurveyID" not in entry:
        errors.append("base export is missing SurveyEntry.SurveyID")
        die(errors)

    questions = spec.get("questions")
    blocks = spec.get("blocks")
    flow = spec.get("flow")
    survey_name = spec.get("survey_name")
    if not survey_name or not isinstance(survey_name, str):
        errors.append("spec.survey_name is required")
    if not isinstance(questions, list) or not questions:
        errors.append("spec.questions must be a non-empty list of SQ payloads")
    if not isinstance(blocks, list) or not blocks:
        errors.append("spec.blocks must be a non-empty list of block objects")
    if not isinstance(flow, dict) or flow.get("Type") != "Root":
        errors.append('spec.flow must be an object with "Type": "Root"')
    if errors:
        die(errors)

    qids = []
    tags = []
    descriptions = {}
    for payload in questions:
        qid = payload.get("QuestionID")
        if not qid:
            errors.append("every question payload needs QuestionID")
            continue
        if qid in qids:
            errors.append(f"duplicate QuestionID {qid}")
        qids.append(qid)
        tag = payload.get("DataExportTag")
        if not tag:
            errors.append(f"{qid}: missing DataExportTag")
        elif tag in tags:
            errors.append(f"{qid}: duplicate DataExportTag {tag}")
        else:
            tags.append(tag)
        for field in ("QuestionType", "Selector", "QuestionText",
                      "QuestionDescription", "Validation"):
            if field not in payload:
                errors.append(f"{qid}: missing {field}")
        validation = payload.get("Validation", {})
        force = validation.get("Settings", {}).get("ForceResponse")
        if force not in ("ON", "OFF"):
            errors.append(f"{qid}: Validation.Settings.ForceResponse must be ON or OFF")
        descriptions[qid] = payload.get("QuestionDescription")

    block_ids = []
    block_qids = []
    for block in blocks:
        block_id = block.get("ID")
        if not block_id or not re.fullmatch(r"BL_[A-Za-z0-9]{16}", block_id):
            errors.append(f"block id {block_id!r} must match BL_ + 16 chars")
        elif block_id in block_ids:
            errors.append(f"duplicate block ID {block_id}")
        else:
            block_ids.append(block_id)
        for element in block.get("BlockElements", []):
            if element.get("Type") == "Question":
                block_qids.append(element.get("QuestionID"))
    for qid in block_qids:
        if qid not in qids:
            errors.append(f"block references unknown QuestionID {qid}")
    for qid in qids:
        if qid not in block_qids:
            errors.append(f"{qid} is not placed in any block")

    flow_ids = []
    flow_block_ids = []

    def walk(nodes):
        for node in nodes:
            if not isinstance(node, dict):
                continue
            flow_id = node.get("FlowID")
            if flow_id:
                flow_ids.append(flow_id)
            if node.get("Type") in ("Block", "Standard") and node.get("ID"):
                flow_block_ids.append(node["ID"])
            if isinstance(node.get("Flow"), list):
                walk(node["Flow"])

    walk(flow.get("Flow", []))
    for node_id in flow_block_ids:
        if node_id not in block_ids:
            errors.append(f"flow references unknown block ID {node_id}")
    default_blocks = [b for b in blocks if b.get("Type") == "Default"]
    if len(default_blocks) != 1:
        errors.append("exactly one block must have Type Default")
    elif flow_block_ids and flow_block_ids[0] != default_blocks[0]["ID"]:
        errors.append("the first flow reference must be the Default block")

    numeric = []
    for flow_id in flow_ids:
        match = re.fullmatch(r"FL_(\d+)", flow_id)
        if match:
            numeric.append(int(match.group(1)))
        else:
            errors.append(f"FlowID {flow_id!r} must be FL_ + number")
    if numeric:
        expected_count = max(numeric)
        flow.setdefault("Properties", {})["Count"] = expected_count

    if errors:
        die(errors)

    survey_id = entry["SurveyID"]
    sq_elements = [
        {
            "SurveyID": survey_id,
            "Element": "SQ",
            "PrimaryAttribute": payload["QuestionID"],
            "SecondaryAttribute": payload["QuestionDescription"],
            "TertiaryAttribute": None,
            "Payload": payload,
        }
        for payload in questions
    ]

    bl = element_of(base, "BL", "Survey Blocks")
    fl = element_of(base, "FL", "Survey Flow")
    qc = element_of(base, "QC", "Survey Question Count")
    bl["Payload"] = blocks
    fl["Payload"] = flow
    qc["SecondaryAttribute"] = str(len(questions))

    others = [e for e in base["SurveyElements"]
              if e.get("Element") != "SQ" and e.get("Element") != "STAT"]
    stats = [e for e in base["SurveyElements"] if e.get("Element") == "STAT"]
    base["SurveyElements"] = others + sq_elements + stats
    entry["SurveyName"] = survey_name
    return base


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_export", help="real QSF export from the target instance")
    parser.add_argument("spec", help="spec JSON (questions/blocks/flow/survey_name)")
    parser.add_argument("-o", "--output", required=True, help="output QSF path")
    args = parser.parse_args()

    base = load_json(args.base_export, "base export")
    spec = load_json(args.spec, "spec")
    assembled = validate_and_assemble(base, spec)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(assembled, handle, indent=2, ensure_ascii=False)
    count = len(spec["questions"])
    print(f"wrote {args.output}: {count} questions,"
          f" {len(spec['blocks'])} blocks, flow count"
          f" {spec['flow'].get('Properties', {}).get('Count')}")


if __name__ == "__main__":
    main()
