# UX Writing Coach Prompt Shortcut PRD

## Summary

Create a streamlined, single-file TritonGPT Prompt Shortcut for UC San Diego Library staff. The shortcut will help staff plan, draft, revise, and evaluate Library UX copy using concise Library rules, UX writing best practices, and campus web sources.

The web version of TritonGPT cannot use shared harness skills, so this shortcut must be self-contained in one prompt. It should be compact enough to remain practical while preserving the most useful guidance from the existing skill.

## Problem

Library staff need accessible UX writing support without installing a harness skill. The current `ux-writing-coach` skill is 93,181 characters across `SKILL.md` and 11 reference files, which is too large to use directly as a web prompt shortcut. TritonGPT can retrieve at least some UC San Diego web pages, but the exact Prompt Shortcut limit is unknown. The shortcut therefore needs a conservative first version and a clear testing plan.

## Goals

1. Provide a single Markdown prompt that can be pasted into a TritonGPT Prompt Shortcut.
2. Preserve high-value Library-specific guidance and UX writing principles in concise form.
3. Define when to consult campus brand, editorial, and web-writing sources.
4. Define how to cite sources without making responses cluttered.
5. Keep the shortcut concise without using a fixed character limit.
6. Provide a README for installation, use, and review.

## Non-Goals

- Do not reproduce the full 93,000-character harness skill.
- Do not include the harness test-log feature.
- Do not create a complete accessibility audit tool.
- Do not provide CMS publishing workflow support.
- Do not approve copy for publication.
- Do not support campus copy outside the Library.

## Users

### Primary User

UC San Diego Library staff who write or review web pages, interface text, forms, alerts, service pages, collections, spaces, events, research guides, or related Library content.

### Secondary Users

Library communications, web, UX, and public services staff who want consistent voice, terminology, and UX-writing guidance.

## Experience Requirements

The shortcut should:

1. Identify itself as the UX Writing Coach on the first turn.
2. Ask for missing information when a substantive Library writing task is incomplete.
3. Offer practical copy options, revisions, and feedback rather than only advice.
4. Keep guidance concise and immediately usable.
5. Flag uncertain facts, terminology, policies, links, or AP rules.
6. Recommend the appropriate human review step without claiming publication readiness.

## Source Requirements

The shortcut must distinguish between inline guidance and web sources. It must instruct TritonGPT to consult the authoritative sources needed for the task, not invent rules.

### Core Web Sources

| Label | Source | Use |
| --- | --- | --- |
| Campus Style | UC San Diego Editorial Style Guide | AP baseline, UC San Diego usage, inclusive language, links, and style questions. |
| Web Style | UC San Diego Web Editorial Style Guide | Web-specific style rules. |
| Web Writing | UC San Diego Web Writing Guide | Scanning, structure, and web-writing practice. |
| Brand Voice | UC San Diego Brand Voice | Voice and tone for brand-aligned copy. |
| Messaging | UC San Diego Messaging and Examples | Messaging themes and body-copy guidance. |
| Brand Positioning | UC San Diego Brand Positioning | Higher-level brand story and positioning. |
| Library Style | UC San Diego Library Editorial Style Guide | Library names, locations, services, systems, collections, and terms. |
| Library UX | UX Writing at UC San Diego Library | Library voice, user-centered transformation, copy sizing, microcopy, and UX-writing guidance. |

### Source Rules

1. Use Library-specific guidance for Library names and terminology.
2. Use campus style for general style questions.
3. Use brand and messaging guidance for brand-aligned copy.
4. Use retrieved page content over memory when rules may be current or page-specific.
5. If a source is unavailable or unclear, state the uncertainty and ask the user to verify.
6. Use only facts the user supplies or authoritative sources confirm.
7. Do not infer AP style, policies, return dates, fees, eligibility, locations, hours, contacts, links, names, or service scope.
8. Cite a source only when it materially informed a non-obvious recommendation.

## Functional Requirements

### Scope

The shortcut should support:

- Service pages and long-form help.
- Policies, access, eligibility, and restrictions.
- Forms, labels, buttons, links, tooltips, and empty states.
- Errors, alerts, and outages.
- Wayfinding, buildings, rooms, and spaces.
- Events and promotions.
- Catalog, databases, research guides, and help content.
- Collections and archives.
- People, titles, bios, and related copy.

### Plan Gate

For substantive service, collection, space, or expertise content, the shortcut should show a short plan before drafting unless the user has already supplied enough information. The plan should include goal, audience and eligibility, top jobs, and recommended structure.

Small microcopy, line edits, and complete requests may skip the gate.

### Drafting Behavior

- Microcopy: offer two to three options with one-line rationales.
- Short-form copy: offer two options or a recommended revision plus a bolder alternative.
- Long-form copy: propose structure and cuts first; rewrite the full draft only if requested.
- Feedback: identify what works, top opportunities, suggested revisions, why, and next steps.

### Formula and Example Safety

- Formulas show structure, not facts.
- Replace bracketed placeholders only with user-supplied, retrieved, or service-owner-confirmed values.
- Keep unconfirmed placeholders in the draft or use `[TO CONFIRM: what is needed]`.
- Do not use formulas, examples, or sample values to infer policy, eligibility, hours, contact details, or collection location.

### Inline Library Guidance

The shortcut should carry concise rules for:

- UC San Diego Library naming.
- Key Library buildings, service points, spaces, systems, and resources.
- Public-facing terminology.
- Sentence case, dates, times, links, and interface labels.
- Voice, tone, and AI-language avoidance.
- User-centered transformation, brevity, scanning, and jargon handling.
- Inclusive-language principles.
- Service-critical clarity.

## Acceptance Criteria

1. `prompt-shortcut.md` is a single Markdown file.
2. The shortcut remains concise and practical without a fixed character limit.
3. It includes the eight core sources with URLs.
4. It defines when to consult campus editorial, brand, messaging, positioning, web-writing, Library style, and Library UX sources.
5. It contains concise Library terminology and UX-writing guidance.
6. It includes a plan gate for substantive structured content.
7. It defines factual-safety and formula-safety rules for examples and uncertain information.
8. It does not include the test-log feature.
9. `README.md` explains how to install, use, test, and maintain the shortcut.

## Success Measures

### Qualitative

- Staff can paste the shortcut and use it without setup.
- Outputs feel Library-specific, warm, clear, and practical.
- Responses avoid unsupported facts and publication approval.
- Web-copy recommendations consistently reflect campus style and UX best practices.

### Test Cases

1. Turn a service definition into a service-page section.
2. Revise an eligibility or access restriction.
3. Rewrite a button, form label, or error message.
4. Improve a Geisel or WongAvery wayfinding description.
5. Revise event or promotional copy.
6. Rewrite catalog, database, or research-guide help text.
7. Review inclusive language and people-focused copy.

Each test should check plan behavior, source use, factual safety, formula use, voice, terminology, structure, and next steps.

## Maintenance

When campus or Library guidance changes, update:

1. The corresponding source URL if needed.
2. Inline Library terminology rules that are not reliably available from a fetched source.
3. UX-writing rules that prove missing or overlong during testing.
4. The character count and any overflow handling.

If TritonGPT rejects the shortcut, remove lower-priority content in this order:

1. Detailed style examples.
2. Extended molecule guidance.
3. Additional terminology examples.
4. Optional explanatory notes.

Keep the core role, source ladder, plan gate, voice rules, UX-writing rules, and next-step requirement.
