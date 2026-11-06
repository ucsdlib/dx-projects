# Source Citation Manifest

Use this manifest whenever a response names or cites a source. The URLs below were verified on 2026-10-22. `research/` is build-time material for maintaining this skill; it is not packaged with the installed skill and should not be used as a user-facing citation target.

## Citation Rules

- Use the exact compact label shown in the manifest. For a specific section, append a colon and a short section name, such as `[Library UX: Warm]` or `[Library Style: Geisel Front Desk]`.
- On first use in a response, turn the label into a link to the canonical URL. After that, the plain label is enough unless the user asks for full source details.
- Link to the most specific section or anchor when the rule has one.
- Do not invent a citation, section, quote, or URL. If a rule is uncertain, say what is uncertain and verify with the authoritative source.
- For subscription-gated sources, link the public entry point and state that verification may require AP Stylebook or UC San Diego access.
- When adding a new source, add it to this manifest with its title, URL, scope, hierarchy level, and verification date before citing it.

## Source Hierarchy and Citations

| Level | Compact label | Source | Canonical URL | Citation use |
| --- | --- | --- | --- | --- |
| 1 | `[UC San Diego Style]` | UC San Diego Editorial Style Guide | <https://univcomms.ucsd.edu/resources/editorial-style-guide/index.html> | Campus AP baseline, UC San Diego exceptions, general usage, bias-free language, and linked text. |
| 1 | `[Web Editorial Style]` | UC San Diego Web Editorial Style Guide | <https://blink.ucsd.edu/technology/websites/training/writing/styleguide/index.html> | Web-specific AP interpretation and web writing rules. |
| 2 | `[Library UX]` | UX Writing at UC San Diego Library | <https://ucsdlibrary.atlassian.net/wiki/x/AoC_0> | Library voice, user-centered transformation, copy sizing, microcopy, jargon, brevity, AI-tell rules, and draft checklist. Access may require UC San Diego authentication. |
| 3 | `[Library Style]` | UC San Diego Library Editorial Style Guide | <https://ucsdlibrary.atlassian.net/wiki/spaces/CE/pages/3502145538/UC+San+Diego+Library+Editorial+Style+Guide> | Library names, locations, services, systems, resources, and terminology. Access may require UC San Diego authentication. |
| 4 | `[Brand Voice]` | UC San Diego Brand Voice for Audiences | <https://brand.ucsd.edu/voice-and-messaging/brand-voice/index.html> | UC San Diego voice, tone qualities, and audience tone. |
| 4 | `[Messaging]` | UC San Diego Messaging and Examples | <https://brand.ucsd.edu/voice-and-messaging/messaging/index.html> | Messaging themes, headline and body-copy guidance, and messaging best practices. |
| 5 | `[NN/g: How Users Read]` | How Users Read on the Web, Nielsen Norman Group | <https://www.nngroup.com/articles/how-users-read-on-the-web/> | Evidence for scanning, concise and objective text, headings, lists, and the inverted pyramid. |
| 5 | `[NN/g: Copy Sizes]` | UX Copy Sizes: Long, Short, and Micro, Nielsen Norman Group | <https://www.nngroup.com/articles/ux-copy-sizes/> | Definitions and appropriate uses of long-form, short-form, and microcopy. |
| 5 | `[NN/g: Microcopy]` | The 3 I’s of Microcopy: Inform, Influence, and Interact, Nielsen Norman Group | <https://www.nngroup.com/articles/3-is-of-microcopy/> | Microcopy goals and common interface-copy patterns. |
| 5 | `[NN/g: Brevity]` | Rewriting Digital Content for Brevity, Nielsen Norman Group | <https://www.nngroup.com/articles/rewriting-content-brevity/> | Techniques for cutting filler, redundancy, passive constructions, and unnecessary detail. |
| 5 | `[NN/g: Jargon]` | Dealing with Technical or Professional Jargon, Nielsen Norman Group | <https://www.nngroup.com/articles/technical-jargon/> | Audience-based decisions for technical terms, plain-language alternatives, and acronyms. |
| AP | `[AP Stylebook]` | AP Stylebook | <https://www.apstylebook.com/> | Subscription-gated AP entries. Use only for verified rules and state access limitations. |

## Section Anchors

When available, use a section anchor instead of the source home page. Examples:

- Linked text in the campus guide: `[UC San Diego Style: Links](https://univcomms.ucsd.edu/resources/editorial-style-guide/index.html#hyperlinked-text)`
- Library voice in the Library UX guide: `[Library UX: Voice](https://ucsdlibrary.atlassian.net/wiki/x/AoC_0)` with the specific section named in surrounding text
- Copy sizes: `[NN/g: Copy Sizes](https://www.nngroup.com/articles/ux-copy-sizes/)`
- Jargon: `[NN/g: Jargon](https://www.nngroup.com/articles/technical-jargon/)`

For sources without stable public anchors, cite the source URL and identify the section in plain text. Do not fabricate anchors.

## Known Section Anchors

Use these anchors when they match the cited rule. If no anchor is shown, cite the source URL and name the section in plain text.

| Source | Section | Anchor |
| --- | --- | --- |
| UC San Diego Editorial Style Guide | Hyperlinked Text | `#hyperlinked-text` |
| UC San Diego Editorial Style Guide | Bias-Free Language | `#bias-free-language` |
| UC San Diego Editorial Style Guide | Writing | `#writing` |
| UC San Diego Library Editorial Style Guide | UC and UC San Diego Terminology | `#UC-and-UC-San-Diego-Terminology` |
| UC San Diego Library Editorial Style Guide | Library Names and Buildings | `#Library-Names-and-Buildings` |
| UC San Diego Library Editorial Style Guide | Library Service Locations | `#Library-Service-Locations` |
| UC San Diego Library Editorial Style Guide | Library Collections and Other Resources | `#Library-Collections-and-Other-Resources` |
| UC San Diego Library Editorial Style Guide | General Library Terminology | `#General-Library-Terminology` |
| NN/g, Rewriting Digital Content for Brevity | Unnecessary Words | `#toc-2-unnecessary-words-2` |
| NN/g, Rewriting Digital Content for Brevity | Redundancy | `#toc-3-redundancy-3` |
| NN/g, Dealing with Technical or Professional Jargon | Two Key Questions for Dealing with Jargon | `#toc-two-key-questions-for-dealing-with-jargon-2` |
| NN/g, Dealing with Technical or Professional Jargon | Using Both the Technical Term and Plain-Language Alternative | `#toc-using-both-the-technical-term-and-plain-language-alternative-3` |
| NN/g, Dealing with Technical or Professional Jargon | Always Avoid Acronyms | `#toc-aaa-always-avoid-acronyms-4` |
| NN/g, The 3 I’s of Microcopy | The 3 Goals of Microcopy | `#toc-the-3-goals-of-microcopy-1` |
| NN/g, The 3 I’s of Microcopy | Informational Microcopy | `#toc-informational-microcopy-2` |
| NN/g, The 3 I’s of Microcopy | Influential Microcopy | `#toc-influential-microcopy-3` |
| NN/g, The 3 I’s of Microcopy | Interaction Microcopy | `#toc-interaction-microcopy-4` |
| NN/g, UX Copy Sizes | Long-Form Copy | `#toc-long-form-copy-2` |
| NN/g, UX Copy Sizes | Short-Form Copy | `#toc-short-form-copy-3` |
| NN/g, UX Copy Sizes | Microcopy | `#toc-microcopy-4` |
