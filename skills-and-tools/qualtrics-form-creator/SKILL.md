---
name: qualtrics-form-creator
description: Generate importable Qualtrics QSF survey files for UCSD Library forms, either by converting Mach Forms component data (mach-forms-and-components.csv rows) or by interviewing the user about a new form. Produces QSF files for sandbox import; does not contact the Qualtrics API or edit surveys in Qualtrics.
---

# Qualtrics Form Creator

Generate a Qualtrics QSF file that imports cleanly into the UCSD
Qualtrics instance. Two modes:

- **Convert a Mach Form**: the user names a form (id or name) from a Mach
  Forms components CSV (columns: form_id, form_name, form_active, page,
  position, element_id, element_type, label, required, choices; choices
  are pipe-separated). Ask for the CSV path if it is not already in the
  workspace.
- **Build a new form**: interview the user for purpose, audience, fields
  (type, label, required, choices), grouping into sections/pages, and any
  conditional routing (e.g., "if Yes, send them to another form"). Ask
  focused questions, propose a draft structure, and confirm before
  generating.

## Workflow

1. Read [references/qsf-conventions.md](references/qsf-conventions.md)
   before generating payloads. It defines the confirmed QSF patterns
   (element anatomy, question payloads, blocks, flow/branch logic) and
   flags UNCONFIRMED patterns that need care.
2. Produce a spec JSON with `survey_name`, `questions` (QSF SQ payload
   objects), `blocks` (BL payload array), and `flow` (FL payload object).
   The conventions reference defines each shape. For CSV conversion, use
   `scripts/mach_to_spec.py <csv> <form_id>` to draft the spec, then
   review and refine it: fix wording, split/merge blocks, and add flow
   branches for conditional logic the script cannot infer.
3. Assemble with
   `scripts/assemble_qsf.py <base_export.qsf> <spec.json> -o out.qsf`.
   The base export must be a real QSF export from the target instance
   (support elements, SurveyID, and skin are kept verbatim from it); ask
   the user for one if none is available. The script validates references
   and counts and refuses to write an invalid file.
4. Deliver the QSF with import instructions (Surveys -> Create a survey
   -> Import from a file; survey imports as Inactive; test in Preview).
   Remind the user that first imports should go to a sandbox survey, and
   list any UNCONFIRMED patterns or placeholders (e.g., missing URLs,
   image/media placeholders) that need post-import review.

Never fabricate a base export or skip assembly validation. If the import
fails, iterate: compare the failed QSF against the base export and the
conventions, fix the spec, and rebuild.
