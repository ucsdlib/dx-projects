# claim-evaluation-skill

Skill for the TritonAI harness (Codex-based) that evaluates claims in written work: identifying assertions, verifying cited sources, classifying evidence alignment, and assigning confidence ratings (HIGH / MEDIUM / LOW).

## Origins

- **Author**: Doug Worsham, Digital Experience Manager, UC San Diego Library; developed with AI assistance.
- **First version**: 2026-02-12 (package metadata). No standalone creation record exists for this skill.
- **Motivation**: companion to `annotated-bibliography`; both encode the same "faithful over helpful" principle and the three-level evidence classification (direct evidence / reasonable inference / interpretive connection) to prevent "helpful but unfaithful" AI behavior.
- **Domain signals**: examples draw on design research literature (Cross, Wiltschnig et al., Ruskin), consistent with the author's digital experience work at UC San Diego Library.

## Development History

- **2026-02-12** — Initial version, distributed as a Claude-style `.skill` ZIP archive (`claim-evaluation-skill.skill`).
- **2026-09-15** — Brought into `dx-tools` (commit `128176c`) as a plain skill directory; the `.skill` ZIP was removed.
- **2026-09-15** — Adapted for the TritonAI/Codex harness: `web_search` / `web_fetch` steps replaced with the collaborative browser (`preview_*`) and `exec_command` guidance.

## Status

Ready for harness use. Not yet installed into `~/.tritonai-harness/codex/skills/` — see the repo root README for install steps.
