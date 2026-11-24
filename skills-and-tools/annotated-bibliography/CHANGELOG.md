# Changelog

All notable changes to the Reading List skill (`annotated-bibliography`) are documented here. For the full narrative of what each version demonstrated, see the README's Testing and Development section.

## 2026-11-14

### Added

- DOI-first source-link resolution in `references/search-and-selection.md`: a normalized DOI is the primary reader link when available, with the UC Library Search / Primo record retained separately for library access and holdings. Added `primary_link`, `primary_link_source`, `library_link`, and `library_link_type` to source state, with a documented fallback order (DOI, library record, native record, metadata search) and rules for extracting PNX links without fabricating permalinks.
- Corresponding link-resolution guidance in `references/interaction-model.md` and `references/response-templates.md` run-state fields.

### Status

- The dev copy of the skill is one revision ahead of the installed harness skill; the installed copy predates the DOI-link update.

## 2026-10-22

### Added

- First phase 2 forward test on a fresh topic (social media and college-student mental health), exercising intake, landscape, selection, reading-list deep work, search-log audit, manifest creation, and DOI-first link resolution. Artifacts in `testing/2026-10-22-social-media-mental-health/`.

### Verified

- Manifest passed validation; reading-list quotes matched retrieved abstract text; themes and questions retained source provenance; a 2016 source was explicitly labeled as a date-range exception; DOI links were separated from Primo library-access links.

### Known gaps

- Annotations remain abstract-level; the narrowed-topic context was simulated from `assignment-prompts.md` rather than a live follow-up turn; the manifest's breadth field is descriptive rather than normalized.

## 2026-10-21

### Added

- Phase 2 interaction update: Reading List product name, default focused landscape, modular run state and manifest guidance, follow-up paths, response templates, adaptive landscape-sufficiency rules, and focused reference files (`interaction-model.md`, `response-templates.md`, `search-and-selection.md` split from a monolithic skill file). Directory and compatibility name remain `annotated-bibliography`.

## 2026-10-02

### Changed

- Clarified Primo execution order: try the documented Primo Search API first when `PRIMO_KEY` is present; use the PNX REST API as the activation/authentication fallback (`references/primo-search-api.md`, `references/primo-pnx-api.md`).

## 2026-09-26

### Added

- Major pipeline update: adaptive fidelity-based screening (≥50% keep paging, 25–50% one more page then refine, <25% stop and refine); component decomposition of the question into concept-level queries; mode-aware breadth-tier dialog; curation rule binding the final source set to the tier with documented pruning; book verification ladder over full PNX enrichment fields; documented-skip rule.
- Human-in-the-loop closing: a required "Human Next Steps" section (priority reading list, verification targets, open questions, follow-up searches, reading guidance) framing every bibliography as a springboard for human-led reading and verification.

### Verified

- Third controlled run (v3) on the creative-teams-in-higher-ed question: 11 searches, 220 records screened, 18 curated sources, a recovered 0%-fidelity query, and zero out-of-range date records.

## 2026-09-15

### Changed

- Brought the skill into `dx-tools` as a plain skill directory (commit `128176c`); the `.skill` ZIP archive was removed and the directory became the source of truth.
- Adapted for the TritonAI/Codex harness: `web_fetch` replaced with the collaborative browser (`preview_navigate` / `preview_snapshot` / `preview_evaluate`) and `exec_command` guidance.

## 2026-02-12

### Added

- Initial version, distributed as a Claude-style `.skill` ZIP archive (`annotated-bibliography.skill`). Motivation: counter the "helpful but unfaithful" failure mode in AI bibliographies.
