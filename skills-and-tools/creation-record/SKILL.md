---
name: creation-record
description: >
  Generate a creation record or creation note documenting how a work was made and what role
  AI played in its creation. Use this skill when the user says anything like "create a creation
  record", "document this work", "creation note", "process notes", "document AI use",
  "transparency statement", "authorship statement", "how was this made", or "/record". Also
  trigger when a user says they're done with a piece of work — or sharing a work in progress —
  and wants to document how it was created before sharing or publishing it. This skill produces
  human-readable creation records (creation note for short-form; creation record for long-form;
  draft creation record for works in progress) and optionally machine-readable JSON-LD records,
  based on user preference and document stage. It asks targeted clarifying questions to
  accurately characterize AI and human involvement — including multi-party authorship and
  contributor roles — never exaggerating or minimizing either contribution.
---

# Creation Record Skill

This skill generates creation records and creation notes for work that involved AI assistance.
It handles solo and multi-party authorship, works across all modalities (writing, code, design,
multimedia), and is honest about AI's role — neither overclaiming nor underclaiming.

| Output type | Term |
|---|---|
| Short inline statement (1–3 sentences) | **Creation note** |
| Full structured record, finalized work | **Creation record** |
| Full structured record, work in progress | **Draft creation record** |
| Machine-readable JSON-LD | **Creation record (machine-readable)** |

---

## Framework Attribution

The contribution classification and contributor role framework in this skill is a
**synthesized best-practice construct**, not a formally standardized or ratified framework.
It draws from:

- **C2PA (Coalition for Content Provenance and Authenticity)** — role vocabulary and assertion
  structure. https://c2pa.org/specifications/specifications/2.2/
- **W3C PROV-O** — provenance ontology for activity/agent/entity relationships.
  https://www.w3.org/TR/prov-o/
- **CRediT (Contributor Roles Taxonomy)** — 14 standardized contributor roles for academic
  and research outputs. https://credit.niso.org — used verbatim for covered roles.
- **Nielsen Norman Group** role taxonomy — UX and design role vocabulary.
  https://www.nngroup.com
- **SWEBOK (IEEE Software Engineering Body of Knowledge)** — software contributor role
  vocabulary. https://www.computer.org/education/bodies-of-knowledge/software-engineering
- **SPDX (Software Package Data Exchange)** — Linux Foundation open standard for
  software bill of materials; reference framework for code provenance.
  https://spdx.dev
- **ProvenanceDisclosure.com** — practical guidance on AI use statements.
  https://provenancedisclosure.com/resources/how-to-disclose-ai-use
- **COPE (Committee on Publication Ethics)** — authorship and AI use guidance.
  https://cope.org
- **US Copyright Office AI guidance (2023–2024)** — human authorship and AI-generated content
- **Partnership on AI** — PACT framework concepts on AI involvement characterization

CRediT roles are cited using official URIs (`https://credit.niso.org/contributor-roles/`).
DX extension roles use a generic namespace (`https://creativerecord.org/contributor-roles/`)
and **should not be cited as standards**. See `references/contributor-roles.md` for the full
taxonomy with URIs and context guidance.

---

## Core Principles

1. **Accuracy first**: Describe what actually happened. Don't inflate or minimize AI's role.
2. **Human responsibility**: Always identify who is accountable — the approver for finished
   work, the responsible party for work in progress.
3. **Multi-party aware**: Solo and team authorship are both fully supported. Contributor roles
   are captured per person, not just for the work as a whole.
4. **Human-readable always**: Every output includes a human-readable statement. Machine-readable
   JSON-LD is offered with long-form records and on request for creation notes.
5. **Proportional detail**: Creation notes for routine use; full records for formal contexts.
   Multi-party detail scales: concise team statement for creation notes, individual
   per-person contribution statements for full creation records.
6. **Stage-aware**: Works in progress get draft creation records with formative-stage language.
7. **Opt-in**: This skill is only invoked when the user explicitly requests it.

---

## Step 1: Gather Information

Extract what you can from the conversation, then ask only what's missing.

### Extract from conversation history first:
- Work type (document, code, design, image, multimedia, etc.)
- What the AI was asked to do
- Whether single or multiple humans were involved
- Whether the exchange involved one prompt or iterative rounds
- Whether the user provided source material, facts, or domain expertise
- Whether a revised/final version was provided by the user

### Clarifying questions (ask only what's unknown):

**About the work:**
- What is the work? (article, report, email, code, design, image, audio/video, slide deck, etc.)
- What is its intended use or audience?

**Modality routing:**
Once the work type is known, apply modality-specific guidance from
`references/modality-guidance.md` for the remainder of Step 1 and for contribution
classification. Text and writing workflows proceed with the questions below as written.
For code, images, and audio/video, add the modality-specific questions from the relevant
section of modality-guidance.md **before** asking about human involvement and attribution.

| Work type | Guidance section |
|---|---|
| Text (articles, reports, emails, policy, documentation) | SKILL.md as written — no additional routing |
| Code (scripts, applications, functions, configs) | modality-guidance.md § A |
| Images (generated images, design assets, illustrations) | modality-guidance.md § B |
| Audio / Video (podcasts, video, multimedia) | modality-guidance.md § C |
| Mixed-modality (web pages, presentations, data reports) | modality-guidance.md § D; apply per-component |

**About document stage:**
Ask early — determines record type and responsibility language throughout.
> "Is this work finished and ready to share or publish, or is it still in progress —
> for example, something you're sharing with colleagues for feedback?"

- **Finalized**: use "creation record" or "creation note"
- **In progress**: use "draft creation record"; adjust responsibility language (see Step 4)

**About AI involvement and prompting:**
- What role did AI play? (drafting, outlining, editing, research, code generation,
  image generation, translation, summarization, formatting, or other)
- Did you provide source material, facts, domain knowledge, or structural constraints?
- How many rounds of prompting? Single request or iterative back-and-forth?
- If iterative: did you redirect, reject outputs, or substantially reshape direction?
- How substantially did you revise the AI output? (light edits, restructuring, full rewrite)

**About human involvement — solo or multi-party:**

First establish scale:
> "Was this created by you alone, or did others contribute? If others were involved,
> roughly how many — a small named team (2–5 people), or a larger group?"

Then, based on the answer:

*Solo*: proceed to attribution opt-in below.

*Small named team (2–5)*: collect for each person —
- Name (subject to individual attribution opt-in, see below)
- Role/title
- What they contributed to this specific work
- Whether they want named attribution

*Larger team or organizational authorship*: collect —
- Team or department name
- One or two accountable individuals (approver + lead, if applicable)
- General characterization of team roles without per-person enumeration

For small named teams: contributor roles help characterize each person's contribution
accurately. See §2d for the role taxonomy. Offer the most relevant roles for the work type
rather than listing all options — see `references/contributor-roles.md` for context guidance.

**About human attribution (ask per person for small teams; once for solo):**
> "Would you like your name and/or role included in the creation record? Options: full name
> and title, name only, role only, or anonymous. For published or formal work, named
> attribution strengthens accountability — but it's entirely your choice."

If named: for machine-readable records, also ask:
> "Would you like to include a professional identifier to make attribution machine-verifiable?
> ORCID is preferred for researchers; an institutional profile or LinkedIn URL also works.
> Both can be included."

Default to "the author" / "the team" if attribution is declined. Never infer names from context.

**About accountability:**
For multi-party work, distinguish contributors from the accountable approver:
> "Who reviewed and approved the final work — or who is responsible for it at its current stage?
> This is the person (or role) who stands behind the work."

This person appears in the Responsibility Statement. It may be one of the contributors,
a supervisor, or an institutional role — whoever can be identified as accountable.

**About output format:**
- Creation note or full creation record?
- Machine-readable JSON-LD alongside the human-readable version?

**Do not ask all questions at once.** Group naturally. State assumptions when skipping.

---

## Step 2: Classify AI Contribution

### 2a. Contribution Label

Describes the AI's role in the work as a whole. Numbers are internal only —
**never appear in outputs**.

| # | Label | Description |
|---|---|---|
| 1 | **AI-Produced** | AI generated the primary content; humans provided direction and approved |
| 1p | **AI-Produced, Extensively Directed** | AI generated all content; humans shaped output through substantive iterative prompting (see §2b) |
| 2 | **AI-Drafted, Human-Revised** | AI produced initial draft; humans made meaningful edits or restructured |
| 3 | **AI-Assisted** | Humans created primary content; AI contributed specific sections, edits, or suggestions |
| 4 | **AI-Supported** | Humans created all content; AI used for research, checking, formatting, or minor polish |
| 5 | **Human-Created, AI-Reviewed** | Humans created all content; AI used only for feedback, partially or not incorporated |

For multi-party work: the contribution label describes the AI's role across the work as a
whole. Individual human roles are captured separately via contributor roles (§2d).

### 2b. Progressive Prompting Assessment

When multiple rounds of prompting shaped the output:

**Did the human's prompting involve:**
- Providing original facts, arguments, domain expertise, or structural concepts?
- Iteratively selecting among alternatives, rejecting outputs, redirecting toward a vision?
- Supplying voice, tone, or stylistic direction requiring repeated correction?
- Introducing source material the AI synthesized into the work?

If **two or more** apply and prompting involved **three or more substantive exchanges**,
use **AI-Produced, Extensively Directed**.

**Key distinction**: Effort in prompting ≠ authorship of expression. What matters is whether
the human's intellectual contributions are *expressed in the final work*, not merely whether
the human worked hard to obtain it.

### 2c. Prompt Characterization

| Descriptor | Meaning |
|---|---|
| **Single brief prompt** | One short, general request with minimal constraints |
| **Structured prompt** | Single detailed request with explicit constraints, format, or source material |
| **Iterative prompting** | Multiple exchanges refining output, without substantial original intellectual input |
| **Expert-directed iterative prompting** | Multiple exchanges in which human contributed domain knowledge, original arguments, or factual material |
| **Iterative with human source material** | Human provided documents, data, or prior writing that AI synthesized |

### 2d. Contributor Roles

For each human contributor, identify their role(s) using the taxonomy in
`references/contributor-roles.md`. Present the most relevant roles for the work type —
don't enumerate all options. The taxonomy has three layers:

**CRediT roles** (verbatim, citable — use for research, writing, and academic contexts):
Conceptualization · Data Curation · Formal Analysis · Funding Acquisition · Investigation ·
Methodology · Project Administration · Resources · Software · Supervision · Validation ·
Visualization · Writing – Original Draft · Writing – Review & Editing

**DX Extension — Design & UX** (drawing from NN/g role taxonomy):
UX Research · Usability Testing · Interaction Design · Visual Design · Information Architecture ·
Content Strategy · Accessibility Review · Prototyping · Service Design

**DX Extension — Software & Code** (drawing from SWEBOK / industry vocabulary):
Requirements Definition · System Architecture · Implementation · Code Review ·
Testing & QA · DevOps & Deployment · Technical Documentation · Security Review

**DX Extension — Editorial & Multimedia** (drawing from Dublin Core / MARC relators):
Editorial Direction · Translation · Narration · Illustration · Audio/Video Production ·
Data Visualization

**Cross-cutting**:
Equity & Inclusion Review · Project Sponsorship · Stakeholder Communication

For context guidance and URIs for each role, see `references/contributor-roles.md`.

AI systems can also be assigned roles from this taxonomy — e.g., an AI used for Writing –
Original Draft, or for Implementation. Record these in the AI assertion block, not in the
human attribution blocks.

---

## Step 3: Model Identification

Detail scales with output format:

Identify the actual AI system used. Examples below show Claude (Anthropic) because this
skill was developed there; in the TritonAI/Codex harness, the equivalent is typically
Codex (OpenAI). Never guess the model — use what is actually known.

**Tier 1 — Creation note**: display name + provider only
→ `Claude (Anthropic)` or `Codex (OpenAI)`

**Tier 2 — Creation record (human-readable)**: display name + version if known + provider
→ `Claude Sonnet (claude-sonnet-4-6, Anthropic)` or `Codex (gpt-5.x, OpenAI)`
→ `Claude (version unspecified, Anthropic)` / `Codex (version unspecified, OpenAI)` if
version unknown

**Tier 3 — Machine-readable JSON-LD**: full API model identifier; `null` with version note
if unavailable. Never guess.

---

## Step 4: Generate the Output

### Creation Note (short-form)

1–3 sentences. Cover: what AI did, how directed, who is responsible.
Use Tier 1 model identification. No label numbers.

**For multi-party work**, scale the team description to size:
- 2–3 named contributors: name them — "Created by [A], [B], and [C], with AI assistance..."
- 4–5 contributors: "A team of [N]..." or name by role — "The design and development team..."
- Larger team: team or department name only

**Responsibility always named** in the creation note, even if contributors are anonymous:
"Reviewed and approved by [name/role]."

**For works in progress**, open with a stage signal:
> *Draft — in progress.* ...shared here for collaborative feedback.

---

### Creation Record (long-form)

Use Tier 2 model identification. Label **Draft Creation Record** at top if in progress.

#### 1. Work Identification
- Title, type, date, intended use/audience
- **Stage**: Finalized | In progress — shared for [review / collaboration / feedback]

#### 2. AI Contribution Summary
- Contribution label (no numbers)
- AI system(s): name, version if known, provider
- Specific AI roles (using role taxonomy vocabulary where applicable)
- Prompt characterization (from §2c)
- If extensively directed: nature of human direction across turns

#### 3. Human Contribution Summary

**Solo**: single entry with name/role (per attribution opt-in) and contribution description.

**Small named team**: individual entry per person, formatted as a contributor statement:

> **[Name or role]** — [Job title, organization if provided]
> Roles: [role 1] · [role 2]
> Contribution: [1–2 sentence description of what this person specifically did]

List contributors in a logical order (lead first, or alphabetical if no clear lead).
Distinguish contributors from the accountable approver — the approver may or may not be
a listed contributor.

**Larger team**: team-level statement with named approver:
> The [team/department name] contributed [general characterization]. [Name/role] reviewed
> and approved the final work.

#### 4. Process Narrative (2–4 paragraphs)
Plain-language description of how the work was made. For multi-party work: describe how the
team worked together and where AI fit into that process, not just the AI's output. Write for
a reader trying to understand process and responsibility.

#### 5. Limitations and Caveats (if applicable)

#### 6. Responsibility Statement

| Stage | Anonymous | Named |
|---|---|---|
| **Finalized** | "The [author/team] reviewed and approved this work and accepts responsibility for its accuracy and fitness for its intended use." | "[Full name], [title/role], reviewed and approved this work and accepts responsibility for its accuracy and fitness for its intended use." |
| **In progress** | "This work is in progress. The [author/team] is responsible for its current state and is sharing it for [review / collaboration / feedback]. It has not been approved for release." | "[Full name], [title/role], is responsible for this work in its current state. It is shared for [purpose] and has not been approved for release." |

For multi-party work: the responsibility statement names the **approver**, not every
contributor. Contributors are listed in §3. If responsibility is shared (co-approvers),
name both.

---

## Step 5: Machine-Readable JSON-LD (Optional)

**When to offer**: long-form records by default; creation notes on request only.

`prov:wasAttributedTo` is an **array** — one object per human contributor.
Each person gets their own block with name, roles, and identifiers.
AI assertion blocks are separate and never mixed into human attribution.

```json
{
  "@context": {
    "c2pa": "https://c2pa.org/schema/1.0/",
    "schema": "https://schema.org/",
    "prov": "https://www.w3.org/ns/prov#",
    "dc": "http://purl.org/dc/terms/",
    "credit": "https://credit.niso.org/contributor-roles/",
    "cr": "https://creativerecord.org/contributor-roles/"
  },
  "@type": "c2pa:Manifest",
  "dc:title": "[Work title]",
  "dc:type": "[Work type]",
  "dc:date": "[ISO 8601 date]",
  "dc:description": "[Brief description]",
  "c2pa:documentStage": "[finalized | in-progress]",
  "c2pa:recordType": "[creation-record | draft-creation-record]",
  "c2pa:assertions": [
    {
      "@type": "c2pa:AIGeneratedContent",
      "c2pa:role": "[produced_by | drafted_by | assisted_by | reviewed_by]",
      "c2pa:contributionLabel": "[label — no numbers]",
      "c2pa:contributionMateriality": "[primary | substantial | moderate | minor | incidental]",
      "c2pa:model": {
        "c2pa:name": "[display name]",
        "c2pa:modelId": "[API model string or null]",
        "c2pa:provider": "[provider name]",
        "c2pa:versionNote": "[explanation if modelId null, else null]"
      },
      "c2pa:aiRoles": [
        "[use role taxonomy vocabulary — e.g. credit:writing-original-draft, cr:implementation]"
      ],
      "c2pa:promptCharacterization": "[single-brief-prompt | structured-prompt | iterative-prompting | expert-directed-iterative-prompting | iterative-with-human-source-material]",
      "c2pa:promptSummary": "[plain-language description of how AI was directed]",
      "c2pa:iterationCount": "[number of exchanges, or null]"
    }
  ],
  "c2pa:humanReview": {
    "@type": "c2pa:HumanReviewAction",
    "c2pa:reviewer": "[approver name/role — this is the accountable party, not all contributors]",
    "c2pa:reviewType": "[approved | revised-and-approved | fact-checked-and-approved | in-progress-not-yet-approved]",
    "c2pa:editingNature": "[none | light edits | substantial revision | full rewrite]",
    "c2pa:humanInputNature": "[direction only | domain expertise | original facts/arguments | source material | mixed]"
  },
  "prov:wasAttributedTo": [
    {
      "@type": "prov:Person",
      "schema:name": "[full name, or null if anonymous]",
      "schema:jobTitle": "[title/role, or null]",
      "schema:affiliation": "[organization, or null]",
      "schema:url": "[ORCID preferred, or null]",
      "schema:sameAs": "[secondary identifier e.g. LinkedIn, or null]",
      "c2pa:attributionNote": "[named by contributor | anonymous by request | role-only by request]",
      "c2pa:contributorRoles": [
        "[use URIs: credit:conceptualization, cr:ux-research, cr:implementation, etc.]"
      ],
      "c2pa:contributionDescription": "[1–2 sentence description of this person's specific contribution]"
    }
  ],
  "c2pa:responsibilityStatement": "[Stage-appropriate responsibility statement naming the approver]",
  "prov:wasGeneratedBy": {
    "@type": "prov:Activity",
    "prov:startedAtTime": "[ISO 8601 or null]",
    "prov:used": "[source materials description, or null]"
  }
}
```

**For solo authorship**: `prov:wasAttributedTo` is still an array — with one object.
**For larger teams**: include named approver(s) only; use `c2pa:teamAttribution` for
the team/department name.
**For multiple AI systems**: one assertion block per system.

---

## Output Format Guidelines

- Always lead with the human-readable statement.
- Label record type clearly at the top.
- For long-form, use clear section headers and plain language.
- JSON-LD in a clearly labeled code block, never inline.
- Creation note first when producing both.
- No label numbers in any output.
- Do not editorialize about whether AI use was appropriate.
- Never use "reviewed and approved" for in-progress work.
- In multi-party records: distinguish contributor list from responsibility statement.

---

## Edge Cases

**Multiple AI systems**: One assertion block per system. In prose, list each with its role.

**Unknown model version**: `null` + version note in JSON-LD; "version unspecified" in prose.

**Extensive iterative prompting, no post-generation editing**: AI-Produced, Extensively
Directed if §2b criteria met. Be honest that no post-generation editing occurred.

**No human revision, minimal direction**: Plain AI-Produced. Don't soften.

**Different AI involvement per contributor**: Note this in each person's contribution
description — e.g., one person used AI extensively, another not at all.

**Organizational authorship (no named individuals)**: Team/department name in attribution;
institutional role (e.g., "Director of [X]") in responsibility statement.

**Code**: Use "written" or "implemented", not "drafted." Apply integration depth and
modification extent descriptors from modality-guidance.md § A. Note testing, debugging,
security review. For living codebases, note that the record reflects a point in time.

**Images**: Use "generated" not "drafted." Apply style reference and post-processing
descriptors from modality-guidance.md § B. Distinguish prompt-only generation from
reference-guided or composited work.

**Audio/Video**: Describe AI involvement layer by layer (script, voice, music, editing,
captioning, etc.) using modality-guidance.md § C. Treat synthetic voice with particular
care — note voice type, consent, and audience disclosure where relevant.

**Mixed-modality work**: Identify the primary modality for the contribution label; apply
per-component guidance from modality-guidance.md § D.

**Work produced across multiple sessions or models**: Separate JSON-LD assertion blocks;
describe each contribution in the narrative.

---

## Reference Files

- `references/modality-guidance.md` — Modality-specific guidance for code, images,
  audio/video, and mixed-modality work; read this for any non-text work type
- `references/contributor-roles.md` — Full role taxonomy with URIs, context guidance,
  and suggested roles by work type
- `references/c2pa-vocabulary.md` — C2PA assertion types and materiality mapping
- `references/creation-record-examples.md` — Worked examples including multi-party,
  in-progress, and modality-specific scenarios
- `references/skill-creation-record.md` — Creation record for this skill (human-readable)
- `references/skill-creation-record.jsonld` — Creation record for this skill (machine-readable)
