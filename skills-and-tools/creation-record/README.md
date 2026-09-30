# creation-record

Skill for the TritonAI/Codex harness that generates creation records and creation notes documenting how a work was made and what role AI played — human-readable statements plus optional machine-readable JSON-LD. Procedural guidance lives in `SKILL.md`; supporting material is in `references/`.

## Origins

- **Author**: Doug Worsham, Digital Experience Manager, UC San Diego Library ([ORCID](https://orcid.org/0000-0002-4945-5773)).
- **Created**: June 4, 2026 (v1.3, exploratory prototype) through roughly ten expert-directed iterative exchanges with Claude Sonnet (claude-sonnet-4-6, Anthropic). Initially named `ai-provenance-disclosure`; renamed to `creation-record` during development.
- **Self-documented**: the skill records its own creation in `references/skill-creation-record.md` (human-readable) and `references/skill-creation-record.jsonld` (machine-readable).
- **Framework sources**: C2PA, W3C PROV-O, CRediT, NN/g, SWEBOK, SPDX, COPE, US Copyright Office AI guidance, and Partnership on AI. Status remains exploratory prototype — actively developed, feedback welcome.

## Development History

- **2026-06-04** — v1.3 created for the Claude skills system; MIT-licensed, © 2026 Doug Worsham.
- **2026-08-31** — Installed into the TritonAI harness skills directory (`~/.tritonai-harness/codex/skills/creation-record`) with a one-line README and `LICENSE`.
- **2026-09-15** — Brought into `dx-tools` (commit `128176c`) as the source of truth; the `.skill` ZIP was removed.
- **2026-09-15** — Provider-agnostic pass for TritonAI/Codex: model-identification guidance and reference examples now cover Codex (OpenAI) alongside Claude (Anthropic); the full origins README was added here.

## License

MIT — see `LICENSE`.
