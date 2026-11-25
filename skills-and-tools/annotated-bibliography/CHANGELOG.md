# Changelog

All notable changes to the Reading List skill (`annotated-bibliography`) are documented here. For the full narrative of what each version demonstrated, see the README's Testing and Development section.

## 2026-11-24 (later same day)

### Added

- PRD updated to v0.4 draft: new feature area 7.4 "Fast first round (timing progressive disclosure)" from Doug's direction, grounded in the round 3 S03 finding that a "quick" pass took 11 min 13 s while the same session's comprehensive escalation took 4 min 46 s. Requirements: first substantive reply within about a minute, verification deferred to the committed turn with plain-language provisional labeling, monotonic effort curves, fidelity never traded for speed, and timing recorded in the manifest for auditability. Adds a fast-first-round test to the phase 3 testing plan, a usability criterion, and an open question on how much verification can safely move to the committed turn. Current State updated for rounds 1-3 (live narrowing, bibliography continuation, skill sync now verified; manifest hygiene, user-cap binding, and effort-curve inversion added as open gaps).
- PRD 7.4 refinement after Doug questioned the monotonic-effort framing: filesystem evidence shows the S03 escalation ran roughly sixteen new searches across three APIs plus an 820 KB Crossref verification batch in under five minutes while reusing seven verified sources, so the speed gap is not explained by reuse sparing queries — the quick pass's cost was serial per-source verification and composition. "Monotonic effort curve" replaced with "duration tracks stated urgency, not a fixed depth rule"; the reuse dividend (later turns faster than the first) is expected behavior, and the first-round failure case is paying comprehensive-verification prices on urgent requests.
- Round 3 complete (S02 and S03 added after the S01 rerun): S02 held template structure and clarity through a 16-source comprehensive build but exceeded the user's explicit 8-10 source cap (rationalized, trimming offered; round 1 honored the cap); S03 validated the phase 3 right-sizing behaviors live for the first time — quick-pass scope honored (7 sources vs round 1's 21), an unprompted expectation statement posted ~12 seconds into the escalation turn before deep work, state preserved across escalation, and a plain-language depth distinction on Turn 3 — but manifest hygiene failed (no manifest on the quick pass; intake-only manifest on the comprehensive run; validation fails). The version-of-record citation-year rule was applied live in S02 ("Publication years reflect the journal-issue year where Crossref distinguishes online-first from issue dates"). Change backlog: bind explicit user source counts; add manifest validation gate; extend expectation-signaling to duration/effort estimates.
- Round 3 automated test (S01 template-safeguard rerun): the template-defaulting safeguard and rule 7 held in live behavior at the exact decision point where round 2 failed — full template structure (theme headings, folded questions, 2-3 representative readings and find-more links per theme, complete annotation block in the reading list) with no loss of round 2's clarity gains. Turn 1 completed in ~6.3 minutes with full structure versus round 2's ~16.5 minutes with compressed output. Artifacts in `testing/2026-11-24-automated-round3-template-safeguard/`; README Testing and Status sections updated.
- Template-defaulting safeguard, from the round 2 finding that the skill read `response-templates.md` (recorded in the manifest `reference_log`) yet still dropped required elements when the Plain-Language Rules created tension with template structure: Non-Negotiables now require selecting and following the matching template before rendering, with deviation allowed only when the request clearly fits no template (noted in the manifest); Quality Check item 8 verifies required elements survived rendering; the templates reference states the selection-and-default rule up front.
- Plain-Language Rules in `references/response-templates.md`, from Doug's transcript review of the automated test round: open every substantive response by restating the working question(s) and how you will proceed; never use internal vocabulary (landscape, manifest, breadth tier, fidelity, PNX) in user-facing text; state limitations as plain-language consequences with next actions rather than API mechanics; keep bookkeeping silent; make the search log available on request only.
- Landscape template restructure: themes as headings with one to two theme-phrased questions folded into each theme, two to three representative readings plus a structured "find more" search link per theme, and possible directions reframed as possibilities for the user's research rather than proposals. The standalone Questions table is gone from user-facing output; question provenance remains in run state and the manifest.
- User-facing stage naming: "overview of the research" / "initial overview" replaces "landscape" in conversation; "landscape" stays internal.

### Changed

- SKILL.md: selection offer no longer includes the search log by default; quality check now enforces interpretation-first openings, no internal vocabulary, and consequence-based limitations.
- Refinement template: "what remains valid" language replaced with user terms; breadth-tier language translated to plain words.
- PRD naming rules updated with the user-facing stage naming and search-log decision.
- Scenario cards updated with a Plain language rubric dimension for regression testing.
- Installed harness skill re-synced with the dev copy (all 2026-11-24 changes, including rule 7 and this safeguard), superseding the sync note under 2026-11-14.

### Context

- These changes respond to the round-1 automated test findings (run 01 activation failure recorded separately; run 02 full runs saved under `testing/2026-11-24-automated-round1/`). A rerun of S01/S03 is the planned regression check.

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
