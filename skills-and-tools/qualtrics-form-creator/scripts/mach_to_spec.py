#!/usr/bin/env python3
"""Convert Mach Forms component CSV rows into a draft assemble_qsf spec.

The draft is a starting point: it maps field types and choices but does
not infer conditional logic. Review and refine the spec, then assemble
with scripts/assemble_qsf.py. Uncertain mappings and skipped elements
are written to the notes file.
"""

import argparse
import csv
import json
import secrets
import string
import sys


AGREE_SCALE = [
    "Strongly disagree",
    "Somewhat disagree",
    "Neither agree nor disagree",
    "Somewhat agree",
    "Strongly agree",
]


def die(message):
    print(f"mach_to_spec: {message}", file=sys.stderr)
    sys.exit(1)


def block_id():
    alphabet = string.ascii_letters + string.digits
    return "BL_" + "".join(secrets.choice(alphabet) for _ in range(16))


def visibility():
    return {"Private": False, "Hidden": False}


def validation(required, validation_type="None"):
    return {"Settings": {"ForceResponse": "ON" if required else "OFF",
                         "Type": validation_type}}


class SpecBuilder:
    def __init__(self, survey_name):
        self.survey_name = survey_name
        self.questions = []
        self.blocks = []
        self.current = None
        self.flags = []
        self.qid = 0

    def next_qid(self):
        self.qid += 1
        return f"QID{self.qid}"

    def ensure_block(self):
        if self.current is None:
            block_type = "Default" if not self.blocks else "Standard"
            self.current = {"Type": block_type, "Description": "Main",
                            "ID": block_id(), "BlockElements": []}
            if block_type == "Standard":
                self.current["SubType"] = ""
            self.blocks.append(self.current)

    def set_section(self, label):
        self.ensure_block()
        if not self.current["BlockElements"]:
            self.current["Description"] = label
        else:
            self.current = {"Type": "Standard", "SubType": "",
                            "Description": label, "ID": block_id(),
                            "BlockElements": []}
            self.blocks.append(self.current)

    def page_break(self):
        self.ensure_block()
        self.current["BlockElements"].append({"Type": "Page Break"})

    def place(self, payload):
        self.ensure_block()
        self.current["BlockElements"].append(
            {"Type": "Question", "QuestionID": payload["QuestionID"]})
        self.questions.append(payload)

    def flag(self, message):
        if message not in self.flags:
            self.flags.append(message)

    def flow(self):
        if not self.blocks:
            die("no blocks were generated")
        return {
            "Type": "Root",
            "FlowID": "FL_1",
            "Flow": [{"Type": "Block", "ID": self.blocks[0]["ID"],
                      "FlowID": "FL_2", "Autofill": []}],
            "Properties": {"Count": 2},
        }


def base_payload(builder, row, qtype, selector, subselector=None):
    qid = builder.next_qid()
    label = row["label"]
    payload = {
        "QuestionText": label,
        "DefaultChoices": False,
        "DataExportTag": f"Q{builder.qid}",
        "QuestionType": qtype,
        "Selector": selector,
    }
    if subselector is not None:
        payload["SubSelector"] = subselector
    payload.update({
        "DataVisibility": visibility(),
        "Configuration": {"QuestionDescriptionOption": "UseText"},
        "QuestionDescription": label,
    })
    return payload, qid


def finish_text(payload, qid, required, selector):
    payload["Validation"] = validation(required)
    payload.update({"GradingData": [], "Language": [], "NextChoiceId": 4,
                    "NextAnswerId": 1,
                    "SearchSource": {"AllowFreeResponse": "false"},
                    "QuestionID": qid})
    return payload


def add_text(builder, row, selector="SL"):
    payload, qid = base_payload(builder, row, "TE", selector)
    payload = finish_text(payload, qid, row["required"] == "1", selector)
    builder.place(payload)


def add_form_field(builder, row, validation_code, with_length=False):
    payload, qid = base_payload(builder, row, "TE", "FORM")
    payload["Validation"] = {"Settings": {
        "ForceResponse": "ON" if row["required"] == "1" else "OFF",
        "Type": None}}
    payload.update({"GradingData": [], "Language": [], "NextChoiceId": 4,
                    "NextAnswerId": 1,
                    "SearchSource": {"AllowFreeResponse": "false"},
                    "QuestionID": qid})
    field = {"Display": row["label"], "TextEntry": "on",
             "TextEntryValidation": validation_code}
    if with_length:
        field["TextEntryLength"] = "Short"
    payload["Choices"] = {"1": field}
    payload["ChoiceOrder"] = ["1"]
    builder.place(payload)


def add_validated_text(builder, row, content_type):
    payload, qid = base_payload(builder, row, "TE", "SL")
    payload["Validation"] = {"Settings": {
        "ForceResponse": "ON" if row["required"] == "1" else "OFF",
        "Type": "ContentType",
        "MinChars": "1",
        "ContentType": content_type,
        "ValidDateType": "DateWithFormat",
        "ValidPhoneType": "ValidUSPhone",
        "ValidZipType": "ValidUSZip",
        "ValidNumber": {"Min": "", "Max": "", "NumDecimals": ""},
    }}
    payload.update({"GradingData": [], "Language": [], "NextChoiceId": 4,
                    "NextAnswerId": 1,
                    "SearchSource": {"AllowFreeResponse": "false"},
                    "QuestionID": qid})
    builder.place(payload)


def add_address(builder, row):
    payload, qid = base_payload(builder, row, "TE", "FORM")
    payload["QuestionText"] = row["label"]
    payload["Validation"] = {"Settings": {
        "ForceResponse": "ON" if row["required"] == "1" else "OFF",
        "Type": None}}
    payload.update({"GradingData": [], "Language": [], "NextChoiceId": 5,
                    "NextAnswerId": 1,
                    "SearchSource": {"AllowFreeResponse": "false"},
                    "QuestionID": qid})
    fields = ["Streets", "City", "State", "Postal Code"]
    payload["Choices"] = {str(i + 1): {"Display": name, "TextEntry": "on"}
                          for i, name in enumerate(fields)}
    payload["ChoiceOrder"] = [str(i + 1) for i in range(len(fields))]
    builder.place(payload)
    builder.flag(f"address field '{row['label']}': confirm the form-field"
                 " breakdown matches the Mach form")


def add_select(builder, row):
    choices = split_choices(row["choices"])
    payload, qid = base_payload(builder, row, "MC", "DL")
    payload["Choices"] = {str(i + 1): {"Display": c}
                          for i, c in enumerate(choices)}
    payload["ChoiceOrder"] = [str(i + 1) for i in range(len(choices))]
    payload["Validation"] = validation(row["required"] == "1")
    payload.update({"GradingData": [], "Language": [],
                    "NextChoiceId": len(choices) + 1, "NextAnswerId": 1,
                    "QuestionID": qid})
    builder.place(payload)


def add_radio(builder, row, multi=False):
    choices = split_choices(row["choices"])
    payload, qid = base_payload(builder, row, "MC", "MAVR" if multi else "SAVR",
                                subselector="TX")
    if multi:
        payload["DefaultChoices"] = False
    payload["Choices"] = {str(i + 1): {"Display": c}
                          for i, c in enumerate(choices)}
    payload["ChoiceOrder"] = [str(i + 1) for i in range(len(choices))]
    payload["Validation"] = validation(row["required"] == "1")
    payload["Language"] = []
    payload["NextChoiceId"] = len(choices) + 1
    payload["NextAnswerId"] = 1
    payload["QuestionID"] = qid
    if multi:
        payload["GradingData"] = []
    builder.place(payload)


def add_matrix(builder, row, kind):
    choices = split_choices(row["choices"]) or ["Statement 1"]
    payload, qid = base_payload(builder, row, "Matrix", "Likert",
                                subselector="SingleAnswer")
    payload["Configuration"] = {
        "QuestionDescriptionOption": "UseText",
        "TextPosition": "inline",
        "RepeatHeaders": "none",
        "WhiteSpace": "OFF",
        "MobileFirst": True,
        "Autoscale": {"XScale": {"Name": "agreeDisagree",
                                 "Type": "likert", "Reverse": False}},
    }
    payload["Choices"] = {str(i + 1): {"Display": c}
                          for i, c in enumerate(choices)}
    payload["ChoiceOrder"] = [str(i + 1) for i in range(len(choices))]
    payload["Validation"] = validation(row["required"] == "1")
    payload.update({"GradingData": [], "Language": [],
                    "NextChoiceId": len(choices) + 1,
                    "NextAnswerId": len(AGREE_SCALE) + 1,
                    "Answers": {str(i + 1): {"Display": s}
                                for i, s in enumerate(AGREE_SCALE)},
                    "AnswerOrder": list(range(1, len(AGREE_SCALE) + 1)),
                    "ChoiceDataExportTags": False,
                    "QuestionID": qid,
                    "ColumnLabels": [{"Display": "Click to write Label 1",
                                      "IsLabelDefault": True}]})
    builder.place(payload)
    builder.flag(f"{kind} field '{row['label']}': confirm statements and"
                 " the answer scale; an agree/disagree default was used")


def add_descriptive(builder, row, text, flag=None):
    payload, qid = base_payload(builder, row, "DB", "TB")
    payload["QuestionText"] = text
    payload["ChoiceOrder"] = []
    payload["Validation"] = {"Settings": {"Type": "None"}}
    payload.update({"GradingData": [], "Language": [], "NextChoiceId": 4,
                    "NextAnswerId": 1, "QuestionID": qid})
    builder.place(payload)
    if flag:
        builder.flag(flag)


def split_choices(raw):
    if not raw or raw == "NULL":
        return []
    return [c.strip() for c in raw.split(" | ") if c.strip()]


def add_element(builder, row):
    etype = row["element_type"]
    label = row["label"]
    if etype == "section":
        builder.set_section(label)
    elif etype == "page_break":
        builder.page_break()
    elif etype in ("text", "url"):
        add_text(builder, row)
    elif etype == "textarea":
        add_text(builder, row, selector="ML")
    elif etype in ("simple_name", "simple_name_wmiddle"):
        add_text(builder, row)
    elif etype == "email":
        add_validated_text(builder, row, "ValidEmail")
    elif etype == "date":
        add_validated_text(builder, row, "ValidDate")
    elif etype in ("phone", "simple_phone"):
        add_validated_text(builder, row, "ValidPhone")
    elif etype == "address":
        add_address(builder, row)
    elif etype == "select":
        add_select(builder, row)
    elif etype == "radio":
        add_radio(builder, row)
    elif etype == "checkbox":
        add_radio(builder, row, multi=True)
    elif etype == "matrix":
        add_matrix(builder, row, "matrix")
    elif etype == "rating":
        add_matrix(builder, row, "rating")
    elif etype == "number":
        add_text(builder, row)
        builder.flag(f"number field '{label}': built as plain text;"
                     " numeric validation syntax is unconfirmed")
    elif etype == "money":
        add_text(builder, row)
        builder.flag(f"money field '{label}': built as plain text;"
                     " currency validation syntax is unconfirmed")
    elif etype == "time":
        add_text(builder, row)
        builder.flag(f"time field '{label}': built as plain text;"
                     " time validation syntax is unconfirmed")
    elif etype == "media":
        add_descriptive(builder, row,
                        f"<p>[Media placeholder: {label}]</p>",
                        f"media field '{label}': image DB syntax is"
                        " unconfirmed; attach the image in the editor")
    elif etype == "file":
        builder.flag(f"file field '{label}': SKIPPED - no reliable QSF"
                     " path for file upload; plan manual handling")
    elif etype == "signature":
        builder.flag(f"signature field '{label}': SKIPPED - no QSF"
                     " equivalent; plan manual handling")
    else:
        builder.flag(f"unknown element type '{etype}' on '{label}': SKIPPED")


def load_rows(path, form):
    try:
        with open(path, encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except OSError as exc:
        die(f"cannot read {path}: {exc}")
    exact = [r for r in rows if r["form_id"] == form]
    if exact:
        return exact
    matches = [r for r in rows if form.lower() in (r["form_name"] or "").lower()]
    if not matches:
        die(f"no rows match form id or name {form!r}")
    names = sorted({m["form_name"] for m in matches})
    if len(names) > 1:
        die(f"name {form!r} matches several forms: {', '.join(names)}")
    return matches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", help="mach-forms-and-components.csv path")
    parser.add_argument("form", help="form_id or form_name")
    parser.add_argument("-o", "--output", default=None,
                        help="spec output path (default spec-<form>.json)")
    parser.add_argument("--notes", default=None,
                        help="review notes path (default spec-<form>-notes.md)")
    args = parser.parse_args()

    rows = load_rows(args.csv, args.form)
    rows.sort(key=lambda r: (int(r["page"] or 0), int(r["position"] or 0)))
    form_id = rows[0]["form_id"]
    name = rows[0]["form_name"] or f"Mach Form {form_id}"
    builder = SpecBuilder(name)
    last_page = None
    for row in rows:
        page = row["page"]
        if last_page is not None and page != last_page:
            builder.page_break()
        last_page = page
        add_element(builder, row)

    spec = {"survey_name": name, "questions": builder.questions,
            "blocks": builder.blocks, "flow": builder.flow()}
    output = args.output or f"spec-{form_id}.json"
    with open(output, "w", encoding="utf-8") as handle:
        json.dump(spec, handle, indent=2, ensure_ascii=False)

    notes_path = args.notes or f"spec-{form_id}-notes.md"
    with open(notes_path, "w", encoding="utf-8") as handle:
        handle.write(f"# Draft spec notes: {name} ({form_id})\n\n")
        handle.write(f"Source rows: {len(rows)}; questions generated:"
                     f" {len(builder.questions)}; blocks:"
                     f" {len(builder.blocks)}\n\n")
        if builder.flags:
            handle.write("## Review flags\n\n")
            for flag in builder.flags:
                handle.write(f"- {flag}\n")
        else:
            handle.write("No flags.\n")
        handle.write("\n## Always review\n\n")
        handle.write("- Conditional logic is not inferred; add flow"
                     " branches per the conventions reference.\n")
        handle.write("- Wording, required flags, and choice lists came"
                     " from the CSV; verify against the live form.\n")
        handle.write("- Section blocks and page breaks follow the CSV"
                     " page/position order; adjust grouping as needed.\n")
    print(f"wrote {output} ({len(builder.questions)} questions,"
          f" {len(builder.blocks)} blocks) and {notes_path}"
          f" ({len(builder.flags)} flags)")


if __name__ == "__main__":
    main()
