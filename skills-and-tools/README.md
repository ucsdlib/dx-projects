# DX Tools — Skills for TritonAI / Codex

A collection of skills for the TritonAI harness (a Codex-based agent). Each top-level
directory is a self-contained skill, source-controlled here and synced to GitHub for sharing
with the team.

## What's in this repo

Each skill is a standard Codex skill: a directory containing a `SKILL.md` with `name` and
`description` frontmatter, plus optional `references/`, `scripts/`, `assets/`, and `agents/`
resources. The `description` frontmatter controls when the skill is triggered. Skills may
carry their own `README.md` with a scoped overview and any provenance or creation records —
see each directory.

## Installing into the TritonAI harness

1. From the TritonAI Harness, click `Settings` (gear icon) then `Skills`
2. Scroll to the "Add From Link" section
3. Add the URL for the skill directory in this repository, e.g., `https://github.com/ucsdlib/dx-tools/tree/main/uc-library-search`



## Development conventions

- Follow the standard Codex skill structure; keep `SKILL.md` lean and move reference material
  into `references/`.
- Keep developer-only artifacts (e.g., testing logs) as hidden dotfiles (`.name`) so agent
  file discovery ignores them, and never reference them from the skill itself.
- Give each skill its own `README.md` for a scoped overview; keep it current with the skill.
- Use descriptive commit messages; commit history is the changelog.

## Origins and development

- Authored by **Doug Worsham**, Digital Experience Manager, UC San Diego Library, with AI
  assistance (developed iteratively with Claude/Anthropic and Codex/OpenAI).
- **2026-09-15** — the collection was added to this repo (commit `128176c`). Skills previously
  distributed as Claude-style `.skill` ZIP files; the plain directories here are now the source
  of truth.
- **2026-09-15** — adapted for the TritonAI/Codex harness: search/read guidance maps to the
  collaborative browser (`preview_*`) and `exec_command`, and model identification is
  provider-agnostic.

## Rebuilding a `.skill` ZIP (optional)

Claude Code consumes skills as single-file `.skill` ZIP packages. Rebuild one from its
directory if needed:

```bash
zip -r <skill-name>.skill <skill-name>/
```

## License

Unless noted in a skill's own files, skills do not yet carry a license — decide and add one
before public sharing if needed.
