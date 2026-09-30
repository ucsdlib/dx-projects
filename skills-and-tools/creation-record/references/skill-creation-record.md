# Draft Creation Record
## `creation-record` Skill

*This creation record was generated using the creation-record skill it describes —
a demonstration of the skill applied to its own creation.*

*This is a draft creation record. The skill is functional and available for use, but the
framework it embodies is exploratory and actively being developed. The author welcomes
collaborators, feedback, and critical review.*

---

### Creation Note

This skill was produced by an AI assistant (Claude, Anthropic) through an iterative series
of exchanges in which the author contributed domain expertise in AI transparency frameworks,
specified source references, posed substantive design questions that shaped the framework
architecture, and directed multiple rounds of structural revision. The words and structure
are AI-generated; the conceptual design, source selection, and final approval are the
author's.

*Development status: Exploratory prototype. The skill is functional but the underlying
framework is in active development. Feedback and collaboration welcome.*

Responsible party: Doug Worsham, Digital Experience Manager, UC San Diego Library.

---

### Draft Creation Record

#### 1. Work Identification

- **Title**: `creation-record` — Creation Record Skill
- **Type**: Technical documentation / instructional framework (Claude skill file)
- **Components**: `SKILL.md`, `references/modality-guidance.md`,
  `references/contributor-roles.md`, `references/c2pa-vocabulary.md`,
  `references/creation-record-examples.md`
- **Date**: June 4, 2026
- **Intended use**: Installable skill for the Claude skills system; invoked by users to
  generate creation records and creation notes documenting AI and human contributions
  to their work
- **Stage**: In progress — exploratory prototype; shared for feedback and collaboration
- **Project status**: The skill is functional and usable in its current state. The
  framework it embodies — the contribution classification rubric, contributor role
  taxonomy, modality-specific guidance, and terminology — is being actively developed,
  tested, and reviewed. This record reflects the work at an early prototype stage.
  Substantive changes are anticipated.

#### 2. AI Contribution Summary

- **Contribution**: AI-Produced, Extensively Directed
- **System**: Claude Sonnet (claude-sonnet-4-6, Anthropic)
- **AI roles**: Full prose and structure generation across all files; iterative revision
  across multiple directed rounds; synthesized source frameworks into the contribution
  classification rubric, prompt characterization framework, model identification tiers,
  document stage guidance, terminology framework, contributor role taxonomy, and
  modality-specific guidance for code, images, and audio/video
- **Prompt characterization**: Expert-directed iterative prompting — approximately ten
  substantive exchanges in which the author contributed external source references,
  domain knowledge about AI transparency standards, and directed specific architectural
  and framing changes across multiple revision rounds

#### 3. Human Contribution Summary

- **Author**: Doug Worsham, Digital Experience Manager, UC San Diego Library
  - ORCID: https://orcid.org/0000-0002-4945-5773
  - LinkedIn: https://www.linkedin.com/in/doug-worsham/
- **Contributor roles**: Conceptualization · Methodology · Content Strategy ·
  Supervision · Writing – Review & Editing

- **Author provided**:
  - Conceptual specification: the idea, scope, and opt-in design principle
  - Source frameworks: C2PA spec, provenancedisclosure.com, and direction to draw from
    these specifically
  - Five substantive design questions shaping the framework (model identification
    granularity; rubric attribution and standards status; progressive prompting; prompt
    quality as a contribution dimension; machine-readable output as user-controlled)
  - Direction to remove level numbers from user-facing outputs
  - Direction to add framework attribution with source citations
  - Direction to add AI-Produced, Extensively Directed label and §2b assessment
  - Direction to implement two-tier model identification
  - Direction to make machine-readable output optional/user-controlled
  - Direction to add tiered human attribution guidance with opt-in framework
  - Direction on terminology: replacing "disclosure" with "creation record" / "creation
    note" / "draft creation record"; renaming the skill from `ai-provenance-disclosure`
  - Direction to add document stage as a first-class concept throughout
  - Direction to incorporate CRediT as the base for multi-party authorship; extend with
    DX roles from NN/g and SWEBOK using a generic `creativerecord.org` namespace
  - Direction to add modality-specific guidance for code, images, and audio/video
  - Direction to frame the project explicitly as an exploratory prototype

- **Post-generation editing**: None — all changes were directed through conversation
  rather than direct file editing by the author

- **Responsible party**: Doug Worsham, Digital Experience Manager, UC San Diego Library.
  This work is in progress and is shared for feedback and collaboration. It has not been
  approved as a finalized framework.

#### 4. Process Narrative

Doug Worsham arrived with a clear concept: a skill for generating AI transparency records,
drawing specifically from C2PA and provenancedisclosure.com. He provided the source URLs and
described the key behaviors — opt-in invocation, short and long form outputs, human- and
machine-readable records, and accurate characterization of AI vs. human contribution.

Claude generated an initial version from this specification. Over the course of approximately
ten substantive exchanges, Doug posed design questions, reviewed outputs, and directed
specific architectural changes. These included: two-tier model identification; a formal
framework for progressive prompting assessment; the replacement of "disclosure" with
"creation record" as the primary term; document stage as a first-class concept; the
incorporation of CRediT for contributor roles extended with a DX-specific vocabulary;
and modality-specific guidance for code, images, and audio/video. Each iteration involved
Doug reviewing Claude's work, asking substantive clarifying questions, and directing changes
— a pattern that itself exemplifies the AI-Produced, Extensively Directed contribution
label the skill defines.

Doug approved each revision by requesting the next one. The project's current state reflects
his design decisions across all those exchanges. He has explicitly framed the result as an
exploratory prototype: the skill is functional and usable, but the framework is early-stage,
and he is actively seeking feedback and collaborators to develop it further.

#### 5. Limitations and Caveats

- The contribution classification framework is synthesized, not a ratified standard. Label
  boundaries involve judgment calls that practitioners might draw differently. Empirical
  testing with real users across diverse workflows has not yet been conducted.
- The progressive prompting criteria in §2b are heuristics, not empirically validated
  thresholds. They are intended as practical guidance, not bright lines.
- The C2PA vocabulary in the JSON-LD is C2PA-inspired rather than formally compliant with
  C2PA 2.2, which does not yet define all fields used here. These are extensions in the
  spirit of C2PA's design intent, not a formal C2PA implementation.
- The terminology framework (creation record, creation note, draft creation record) is
  specific to this project's context and is not yet widely established. Its fit for diverse
  organizational and disciplinary contexts has not been tested.
- The DX extension roles in the contributor taxonomy (`creativerecord.org` namespace) are
  not a ratified standard. They represent reasonable synthesis of existing vocabulary but
  have not been validated with practitioners.
- Modality-specific guidance for code, images, and audio/video is first-draft. It draws
  from relevant standards (SPDX, C2PA, SWEBOK, NN/g) but has not been tested against real
  workflows in those modalities.
- The skill has been developed in a single conversation session. It has not been tested
  across diverse users, work types, or organizational contexts.

#### 6. Responsibility Statement

Doug Worsham, Digital Experience Manager, UC San Diego Library, is responsible for this
work in its current state. It is shared as an exploratory prototype, open to feedback,
critical review, and collaboration. It has not been approved as a finalized framework
and should not be treated as authoritative guidance without further development and review.

---

*Draft creation record generated: June 4, 2026*
*Skill version: 1.3 (exploratory prototype)*

---

### Collaboration and Feedback

This project is in active development. Doug Worsham welcomes:
- Feedback on the framework's accuracy, completeness, and usability
- Testing across diverse workflows, modalities, and organizational contexts
- Contributions to the contributor role taxonomy, modality guidance, or JSON-LD vocabulary
- Connections to related work in AI transparency, provenance, and disclosure

Contact: https://orcid.org/0000-0002-4945-5773 · https://www.linkedin.com/in/doug-worsham/
