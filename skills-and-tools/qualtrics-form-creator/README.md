# Qualtrics Form Creator

A Codex skill that generates importable Qualtrics QSF survey files for
UC San Diego Library forms. It works in two modes:

- **Convert a Mach Form**: point it at a Mach Forms components CSV and a
  form id or name; it drafts the survey spec, flags uncertain mappings,
  and assembles a validated QSF.
- **Build a new form**: describe the form you need; the skill interviews
  you for fields, sections, and conditional routing, proposes a draft
  structure, and generates the QSF after you confirm.

The skill produces QSF files only. It does not contact the Qualtrics API
or modify surveys in Qualtrics; you stay in control of every import.

## How it works

1. The skill drafts a spec (questions, blocks, survey flow) following
   QSF format conventions confirmed against the UCSD Qualtrics instance.
2. `scripts/assemble_qsf.py` merges the spec into a real QSF export from
   your instance, keeping the survey skin and support elements verbatim,
   and validates every cross-reference before writing the file. It
   refuses to produce an invalid QSF.
3. You import the result into a sandbox survey (Surveys -> Create a
   survey -> Import from a file), preview it, and adjust anything
   flagged for post-import review.

The format knowledge lives in
[references/qsf-conventions.md](references/qsf-conventions.md), with
every pattern marked CONFIRMED (proven by a real export and/or a
successful import) or UNCONFIRMED (extrapolated; verify first).

## Requirements

- Python 3 (scripts use only the standard library)
- A real QSF export from your Qualtrics instance to use as the base for
  assembly (the conventions are instance-specific; exports from another
  instance may differ)
- A Mach Forms components CSV with columns
  `form_id, form_name, form_active, page, position, element_id,
  element_type, label, required, choices` (pipe-separated choices), for
  the conversion mode

## Installation

Copy this folder into your Codex skills directory, named
`qualtrics-form-creator` (the folder name must match the skill name):

```bash
cp -R skill "${CODEX_HOME:-$HOME/.codex}/skills/qualtrics-form-creator"
```

Then invoke it in a Codex session with `$qualtrics-form-creator`, or just
ask for a Qualtrics QSF of a form and let automatic discovery find it.

## Usage examples

```text
$qualtrics-form-creator - please create a QSF for the
Request Library Instruction form from mach-forms-and-components.csv

$qualtrics-form-creator - build a new form for requesting
research consultations, with routing to the subject specialist pages
```

For conversion mode you can also run the scripts directly:

```bash
python3 scripts/mach_to_spec.py mach-forms-and-components.csv 128442 \
    -o spec.json --notes notes.md
python3 scripts/assemble_qsf.py base-export.qsf spec.json -o my-form.qsf
```

`mach_to_spec.py` writes a review-notes file alongside the spec,
listing uncertain field mappings and skipped elements (file uploads and
signatures have no reliable QSF path). Conditional logic is never
inferred; add flow branches deliberately, following the conventions
reference.

## Known limitations

- File upload and signature fields cannot be generated; the converter
  skips them and flags them for manual handling.
- File upload, signature, media/image, quota, and End Survey flow
  patterns are UNCONFIRMED. Numeric, currency, and time validation
  values are extrapolated from observed structures.
- Always test imports in a sandbox survey before production use, and
  compare the generated survey against the original form.

## Creation Record

This skill was created by Doug (UC San Diego Library) working with GLM
(Z.ai), an AI agent running in the TritonAI Harness (Codex). The AI wrote
the skill instructions, converter and assembly scripts, and the QSF
conventions, which were established through iterative testing in which
Doug produced real Qualtrics exports, ran sandbox imports, and reported
results that confirmed or corrected each pattern. Doug supplied the Mach
Forms data, performed all Qualtrics imports, and reviewed and approved
the final skill.
