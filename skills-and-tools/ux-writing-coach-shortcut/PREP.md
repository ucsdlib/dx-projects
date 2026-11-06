# UX Writing Coach Prompt Shortcut Prep

## Objective

Create one streamlined TritonGPT Prompt Shortcut that preserves the most useful parts of the UX Writing Coach skill while fitting the web version's constraints. The shortcut should stay single-file, be compact enough to test immediately, and give TritonGPT explicit rules for consulting and citing the campus web sources.

## Source Inventory

- Source `SKILL.md`: 13,584 characters. Defines purpose, workflow, plan gate, drafting behavior, feedback pattern, and quality rules.
- Source reference files: 79,597 characters across 11 Markdown files.
- Combined skill source: 93,181 characters. This is likely too large for a prompt shortcut, so we need a prioritized compression pass.
- Highest-value rules to keep: intent and audience, plan-first gate for substantive copy, user-centered transformation, voice, terminology, source rules, citation rules, accessibility-adjacent copy, and response shape.
- Best candidates to compress: content molecule library, scenario routing map, response templates, library terminology tables, and detailed inclusive-language guidance.

## Online Sources

Use these as the shortcut's authoritative web ladder:

1. UC San Diego Editorial Style Guide: <https://univcomms.ucsd.edu/resources/editorial-style-guide/index.html>
2. UC San Diego Brand Voice: <https://brand.ucsd.edu/voice-and-messaging/brand-voice/index.html>
3. UC San Diego Messaging: <https://brand.ucsd.edu/voice-and-messaging/messaging/index.html>
4. UC San Diego Brand Positioning: <https://brand.ucsd.edu/brand-story/brand-positioning/index.html>
5. UC San Diego Web Editorial Style Guide: <https://blink.ucsd.edu/technology/websites/training/writing/styleguide/index.html>
6. UC San Diego Web Writing Guide: <https://blink.ucsd.edu/technology/websites/training/writing/index.html>
7. UC San Diego Library Editorial Style Guide: <https://ucsdlibrary.atlassian.net/wiki/spaces/CE/pages/3502145538/UC+San+Diego+Library+Editorial+Style+Guide>
8. UX Writing at UC San Diego Library: <https://ucsdlibrary.atlassian.net/wiki/x/AoC_0>

The shortcut should distinguish between:

- Always consult: campus style, voice, messaging, and web-writing questions that may have current or page-specific rules.
- Consult when uncertain: Library terminology, Library service names, AP usage, and audience-specific wording.
- Do not fabricate: links, anchors, policies, hours, service eligibility, names, or AP rules.

## Offline-Only Material To Carry Into The Shortcut

- The plan gate and compact plan fields.
- Source-material versus rewrite-object classification.
- Copy-size behavior for microcopy, short-form, and long-form.
- Core voice, tone, and AI-language rules.
- Library naming and terminology rules most likely to appear in public copy.
- Inclusive-language principles and the user-testing fallback.
- Citation-label rules and the public source URLs.
- Guidance for service-critical copy, links, alerts, forms, errors, and accessibility-adjacent text.

## Clarifications Needed

1. What is TritonGPT's exact Prompt Shortcut limit, measured in characters or tokens?
2. Does the web version allow live web browsing or URL retrieval from a Prompt Shortcut?
3. Should the shortcut instruct TritonGPT to fetch every relevant web source on each substantive turn, or only when a rule is uncertain?
4. Should we optimize the first version for a target budget, such as 8,000 or 10,000 characters, and then expand if testing shows more room?
5. Do TritonGPT responses support Markdown links and headings in the same way as the harness skill?
6. Do users need the test-log feature in the shortcut version, or should we remove it to save space?
7. Should the shortcut retain the full plan-first workflow, or use a shorter intent confirmation for microcopy and simple questions?
8. Are there TritonGPT-specific restrictions on quoting, citation formatting, or linking to authenticated Confluence pages?

## Suggested Next Steps

1. Confirm the Prompt Shortcut limit and whether live web retrieval is available.
2. Create a v1 single-file shortcut with a compact system prompt and a prioritized source ladder.
3. Keep an `OFFLINE-CORE` block for rules that cannot be fetched from the web.
4. Test the same five to seven scenarios used for the original skill and compare output quality.
5. Tune for character budget, citation behavior, and whether the Plan Gate helps or adds friction.
