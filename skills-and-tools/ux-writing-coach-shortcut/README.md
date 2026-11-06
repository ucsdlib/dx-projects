# UX Writing Coach Prompt Shortcut

This directory contains a streamlined TritonGPT Prompt Shortcut version of the UC San Diego Library UX Writing Coach. It is designed for staff who use TritonGPT on the web and cannot install a harness skill.

## Files

| File | Purpose |
| --- | --- |
| `prompt-shortcut.md` | The single-file prompt to paste into TritonGPT. |
| `PRD.md` | Product requirements, scope, source rules, acceptance criteria, and maintenance plan. |
| `PREP.md` | Source inventory and planning notes for the shortcut. |
| `CHANGELOG.md` | Release notes and notable changes. |

## Install

1. Open `prompt-shortcut.md`.
2. Copy the full contents, including headings, bullets, and URLs.
3. In TritonGPT, create a new Prompt Shortcut.
4. Name it **UX Writing Coach**.
5. Paste the prompt contents into the shortcut instructions.
6. Save and test the shortcut in a new conversation.

The prompt should stay concise rather than hit a fixed character target. Confirm the exact count after any edit.

## Use It Well

For best results, tell the assistant:

- The format and placement, such as page section, button, form label, alert, or card.
- The intended audience and any eligibility requirements.
- The user’s main task and other important jobs.
- Material facts, limits, deadlines, links, and unknowns.
- Any word count, interface limit, required term, or accessibility constraint.

For feedback, share the current copy and say whether it is a service page, policy, form, alert, wayfinding text, event, catalog help, or another Library content type.

The assistant will show a short plan before drafting substantive service, collection, space, or expertise content unless the request is already complete. Small microcopy, line edits, and conceptual questions do not need the full plan.

## What It Supports

- Service pages and long-form help.
- Policies, access, eligibility, and restrictions.
- Forms, labels, buttons, links, tooltips, and empty states.
- Errors, alerts, and outages.
- Wayfinding, buildings, rooms, and spaces.
- Events and promotions.
- Catalog, databases, research guides, and help content.
- Collections and archives.
- People, titles, bios, and related Library copy.

## Source Behavior

The shortcut includes concise Library-specific guidance and UX-writing rules inline. It also tells TritonGPT to use the following authoritative sources as needed:

1. UC San Diego Editorial Style Guide.
2. UC San Diego Web Editorial Style Guide.
3. UC San Diego Web Writing Guide.
4. UC San Diego Brand Voice.
5. UC San Diego Messaging and Examples.
6. UC San Diego Brand Positioning.
7. UC San Diego Library Editorial Style Guide.
8. UX Writing at UC San Diego Library.

The prompt asks the assistant to use retrieved page content over memory for current or page-specific rules, state uncertainty, and avoid inventing AP style, policies, return dates, fees, eligibility, locations, hours, contacts, links, names, or service scope.

## Factual Safety

When a fact is missing or uncertain, the shortcut asks for `[TO CONFIRM: what is needed]` and directs the writer to supply the value. Formulas and examples show structure only; they must not be treated as facts or used to infer Library policies, eligibility, hours, contacts, links, or locations.

## Review Checklist

- Does the copy lead with the user’s action or benefit?
- Are audience, eligibility, limits, and next steps clear?
- Is the voice warm, inclusive, helpful, and UC San Diego?
- Are Library names and public-facing terms correct?
- Are headings, links, labels, dates, and times in the right style?
- Are claims factual and supported by the source material?
- Does the response recommend human expert review where needed?

## Out of Scope

The shortcut does not perform full accessibility audits, manage CMS publishing, approve copy for publication, or support campus copy outside the Library.

## Maintenance

When campus or Library guidance changes, update the affected source URL, inline Library terminology, or UX-writing rule. Re-test the seven scenarios in `PRD.md`, check the shortcut’s character count, and add an entry to `CHANGELOG.md`. If the prompt becomes too long, remove detailed examples before core role, source, plan-gate, voice, terminology, and next-step rules.
