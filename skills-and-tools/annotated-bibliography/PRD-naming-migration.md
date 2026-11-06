# Reading List: Naming and Migration Product Requirements Document

**Version:** 0.1 draft  
**Date:** 2026-10-21  
**Current technical name:** `annotated-bibliography`  
**Proposed product name:** Reading List  
**Proposed technical name:** `reading-list`  
**Status:** Future phase; do not execute until the interaction PRD is stable

## 1. Summary

This future phase will rename the user-facing product to **Reading List** while preserving the skill’s identity, search quality, and compatibility with requests for an “annotated bibliography.” The rename should make the human purpose clearer: the product prepares and supports reading, analysis, and research next steps rather than producing only a static bibliography artifact.

The current interaction PRD should remain focused on modular interaction, landscape behavior, follow-up paths, and response templates. This document owns the naming migration and should be implemented after those behaviors have been forward-tested.

## 2. Goals

1. Adopt **Reading List** as the user-facing product name.
2. Preserve activation for “annotated bibliography,” “literature review,” “sources for and against,” “what should I read,” and related requests.
3. Keep “annotated bibliography” visible as a supported deep-work mode.
4. Migrate technical names, paths, documentation, tests, and artifact names consistently.
5. Avoid breaking existing users, references, or shared examples during the transition.
6. Preserve the core philosophy: faithful search, verification, transparent limitations, direct evidence, and human next steps.

## 3. Non-Goals

- Do not narrow the product to a simple list of citations.
- Do not remove comprehensive or exhaustive annotated-bibliography modes.
- Do not change the search pipeline as part of the naming migration.
- Do not duplicate the skill under two live directories.
- Do not introduce a new artifact format or state model in this phase.

## 4. Naming Decision

The recommended product name is **Reading List**. It is action-oriented, centers human reading, and accommodates the full workflow from landscape to reading list to annotated bibliography.

The recommended technical name is `reading-list`. If ambiguity with casual reading lists becomes a problem during testing, use `research-reading-list` as the fallback. Do not use `annotated-reading-list` as the primary name because it again emphasizes the artifact over the user’s activity.

The skill description must retain phrases such as “annotated bibliography,” “literature review,” “research question,” “scholarly sources,” and “reading list” so broad topical requests continue to activate the skill.

## 5. Migration Strategy

Use a staged migration rather than changing all names in one large update.

### Stage 1: Positioning

- Introduce **Reading List** in documentation and user-facing response language.
- Continue using `annotated-bibliography` for the directory and installed skill name.
- Treat “annotated bibliography” as a compatibility invocation and full deep-work mode.

### Stage 2: Technical rename

- Rename the skill directory to `reading-list`.
- Update frontmatter `name`, description, examples, and activation triggers.
- Update references to `annotated-bibliography/...` paths.
- Update README, SKILL, PRDs, creation notes, test names, examples, and any internal links.
- Rename run-manifest directories from `annotated-bibliography-runs` to `reading-list-runs` if the manifest feature has been implemented.

### Stage 3: Compatibility

- Keep “annotated bibliography” as a natural-language trigger.
- Update the description to explain that an annotated bibliography is available as a deep-work mode.
- Preserve older document titles as historical context where appropriate.
- If the harness supports aliases, configure `annotated-bibliography` as an alias. If aliases are unavailable, rely on description-level activation and document the change.

## 6. Naming Rules

After migration:

- Use **Reading List** for product-level references.
- Use **reading list** for the curated intermediate output.
- Use **annotated bibliography** for the full deep-work output.
- Use **landscape** for the initial themes-and-questions stage.
- Use **search log** for the audit mode.
- Avoid calling the entire skill an “annotated bibliography tool” in user-facing documentation, though it remains a valid capability description.

## 7. Acceptance Criteria

1. Requests such as “Make a reading list about X” and “Create an annotated bibliography on X” activate the intended skill.
2. The installed skill name and directory match the selected technical name.
3. Documentation uses product naming consistently while retaining annotated-bibliography compatibility language.
4. No user-facing mode implies that a reading list is automatically comprehensive or exhaustive.
5. Existing examples and tests are discoverable through updated naming and documented history.
6. The philosophy and search behavior remain unchanged.

## 8. Open Questions

1. Does the harness support stable skill-name aliases, or should compatibility rely only on description-level activation?
2. Should historical run directories keep `annotated-bibliography-runs`, or should migration include a documented lookup path?
3. Should the README lead with the new product name and preserve the old name as a compatibility note, or preserve the old title until users have adjusted?
4. Should the manifest schema include a `product_name` or `schema_origin` field to distinguish pre- and post-rename artifacts?
