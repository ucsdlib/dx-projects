# Creation Record Examples by Content Type

Worked examples across common content types. Contribution labels follow the synthesized
framework in SKILL.md. Label numbers are omitted from all outputs.

> Examples below use Claude (Anthropic) because this skill was developed there. When
> generating records, substitute the actual AI system used - e.g., Codex (OpenAI) in the
> TritonAI/Codex harness.

---

## Example 1: Published Article — AI-Drafted, Human-Revised

**Context**: User asked Claude to write a 1,500-word article on climate policy. User edited
significantly, changed the framing, added personal analysis, and removed two sections.

### Creation Note:
> This article was initially drafted by an AI assistant (Claude, Anthropic) from a topic
> brief. The author substantially revised the structure, replaced two sections with original
> analysis, and approved the final version for publication.

### Creation Record:

**Work Identification**
- Title: "The Policy Gap in Carbon Markets"
- Type: Journalistic article
- Date: June 4, 2026
- Audience: General public / policy readers
- Stage: Finalized

**AI Contribution Summary**
- Contribution: AI-Drafted, Human-Revised
- System: Claude Sonnet (claude-sonnet-4-6, Anthropic)
- AI roles: Initial full-text drafting, structural outline
- Prompt characterization: Structured prompt — single request specifying subject, target
  length, and three key arguments to cover

**Human Contribution Summary**
- Author provided: topic brief, key arguments, editorial direction
- Review and editing: Substantial revision — restructured argument, replaced two sections
  with original analysis, adjusted tone throughout
- Approved by: [Author name], author and editor

**Process Narrative**
The author provided a topic brief outlining the article's subject, target length, and three
key arguments. An AI assistant produced a full draft from this brief. The author reviewed the
draft, found the structure insufficiently argumentative, and rewrote the opening and closing
sections. Two middle sections were removed entirely and replaced with the author's original
policy analysis drawn from primary sources.

The final article reflects substantially the author's analysis, structure, and voice. The AI
contributed an initial scaffolding that was significantly transformed in revision.

**Responsibility Statement**
The author reviewed and approved this article and accepts full responsibility for its
accuracy, editorial judgment, and fitness for publication.

---

## Example 2: Technical Report — AI-Assisted

**Context**: Team wrote a 20-page technical report. Used AI to draft the executive summary
and conclusion only. All body sections were human-written.

### Creation Note:
> This technical report was written primarily by the project team. An AI assistant (Claude,
> Anthropic) drafted the executive summary and conclusion from the completed body sections.
> Both sections were reviewed and edited by the lead author before finalization.

### Creation Record:

**Work Identification**
- Title: "Q2 Infrastructure Security Assessment"
- Type: Internal technical report
- Date: June 2026
- Audience: Senior leadership, IT governance committee
- Stage: Finalized

**AI Contribution Summary**
- Contribution: AI-Assisted
- System: Claude Sonnet (claude-sonnet-4-6, Anthropic)
- AI roles: Drafted executive summary (~400 words), drafted conclusion (~300 words)
- Prompt characterization: Iterative with human source material — completed body sections
  provided as input; AI directed to synthesize findings for a non-technical audience

**Human Contribution Summary**
- Team provided: All body content (18 of 20 pages), source data, analysis, findings
- Review: Lead author reviewed both AI-drafted sections for accuracy and tone; made targeted edits
- Approved by: Lead author and department head

**Process Narrative**
The project team researched, analyzed, and wrote all substantive sections independently. Once
the body was complete, the team used an AI assistant to draft the executive summary and
conclusion, providing the full body text as source material. The lead author reviewed both
sections, made targeted edits to the executive summary's framing, and approved both as final.
All findings, data, and recommendations are the team's own work.

**Responsibility Statement**
The lead author and department head reviewed and approved this report and accept responsibility
for the accuracy of all findings, data, and recommendations.

---

## Example 3: Code — AI-Produced (with human bug fix)

**Context**: Developer provided a functional specification. AI wrote the script. Developer
reviewed, fixed one bug, tested, and deployed it.

### Creation Note:
> This script was written by an AI assistant (Claude, Anthropic) from a functional
> specification provided by the developer. The developer reviewed the code, corrected one
> logic error, tested the script, and approved it for deployment.

### Creation Record:

**Work Identification**
- Title: `ingest_pipeline.py` — Customer data ingestion script
- Type: Software (Python script)
- Date: June 4, 2026
- Use: Production data pipeline
- Stage: Finalized

**AI Contribution Summary**
- Contribution: AI-Produced (with human bug fix)
- System: Claude Sonnet (claude-sonnet-4-6, Anthropic)
- AI roles: Full code authorship
- Prompt characterization: Structured prompt — functional specification describing
  input/output formats, data sources, transformation logic, and error handling requirements

**Human Contribution Summary**
- Developer provided: Functional specification, environment constraints, schema definitions
- Review: Code review, unit testing, identification and correction of one logic error
- Approved by: Lead developer; reviewed by QA

**Process Narrative**
The developer authored a functional specification describing the script's required behavior,
input/output formats, and integration points. An AI assistant produced the full implementation.
The developer conducted a code review, ran unit tests, identified a logic error in the
deduplication function, and corrected it manually. Following successful testing, the developer
approved the script for production deployment.

**Limitations**
The code was tested against the developer's test suite but edge cases in production data may
not have been anticipated. Ongoing monitoring is recommended.

**Responsibility Statement**
The lead developer reviewed and approved this code and accepts responsibility for its
correctness, security, and fitness for production use.

---

## Example 4: Essay — AI-Produced, Extensively Directed

**Context**: Author engaged in 12 rounds of back-and-forth. Contributed original research,
fieldwork case studies, and the core argument — but did not rewrite the AI's prose afterward.

### Creation Note:
> This essay was generated by an AI assistant (Claude, Anthropic) through an extended
> iterative process in which the author contributed original research, fieldwork-based case
> studies, and the core argumentative framework across twelve exchanges. The words are
> AI-generated; the intellectual substance and final approval are the author's.

### Creation Record:

**Work Identification**
- Title: "Structural Gaps in Urban Education Funding"
- Type: Opinion essay
- Date: June 2026
- Audience: Education policy journal
- Stage: Finalized

**AI Contribution Summary**
- Contribution: AI-Produced, Extensively Directed
- System: Claude Sonnet (claude-sonnet-4-6, Anthropic)
- AI roles: Full prose generation across multiple drafts
- Prompt characterization: Expert-directed iterative prompting — 12 exchanges in which
  the author contributed original field research, specific case studies not in the AI's
  training data, and repeated argumentative redirection

**Human Contribution Summary**
- Author provided: Original fieldwork case studies, core argumentative thesis, domain
  expertise, structural direction, rejection and redirection of multiple draft framings
- Post-generation editing: None — the final AI draft was approved without prose revision
- Approved by: Author

**Process Narrative**
The author engaged in twelve rounds of prompting with an AI assistant. Across these exchanges,
the author introduced case studies from their own fieldwork, corrected the AI's initial framing
of the equity argument three times, and supplied specific data points from unpublished research.
The AI generated all prose across these iterations, producing progressively more targeted drafts.

No post-generation editing of the AI's prose was performed. The essay as published is the final
AI output from the twelfth exchange.

The intellectual substance — thesis, supporting cases, analytical framing — originates with
the author. The expression of that substance in prose was produced by the AI.

**Note on authorship**: US Copyright Office guidance (2023–2024) holds that iterative direction
of AI output does not constitute authorship of the AI's expression, regardless of human effort
invested. This creation record accurately represents that the prose is AI-generated and that
the human contribution was in direction and intellectual substance rather than in writing itself.
Publishers may apply their own authorship standards.

**Responsibility Statement**
The author reviewed and approved this essay and accepts responsibility for the accuracy of all
claims, the integrity of the fieldwork described, and its fitness for publication.

---

## Example 5: Working Draft — Draft Creation Record

**Context**: A policy analyst has used AI to generate a first draft of a policy brief. She's
sharing it with two colleagues for feedback. The document is not final and hasn't been
fact-checked yet.

### Creation Note (for sharing with colleagues):
> *Draft — in progress.* This policy brief was produced by an AI assistant (Claude, Anthropic)
> from a structured brief. It has not yet been reviewed for accuracy or approved for release
> and is shared here for collaborative feedback.

### Draft Creation Record:

**Work Identification**
- Title: "Expanding Open Access to Municipal Research Data" (working title)
- Type: Policy brief (first draft)
- Date: June 2026
- Intended audience: City council staff (final); shared with two colleagues for review
- Stage: In progress — shared for collaborative feedback

**AI Contribution Summary**
- Contribution: AI-Produced
- System: Claude Sonnet (claude-sonnet-4-6, Anthropic)
- AI roles: Full first draft from structured brief
- Prompt characterization: Structured prompt — brief specifying policy area, target
  audience, key arguments, and approximate length

**Human Contribution Summary**
- Author provided: Structured brief, policy framing, key arguments to cover
- Review and editing: Not yet conducted — this is a first draft shared for feedback
- Responsible party: [Author name], Policy Analyst

**Process Narrative**
The author prepared a structured brief outlining the policy brief's subject, target audience,
and key arguments. An AI assistant produced a full first draft from this brief. The draft has
not yet been reviewed for factual accuracy, and several sections are flagged for the author's
further development. It is shared here as a starting point for collaborative discussion.

**Limitations**
This draft has not been fact-checked. Statistical claims and citations should be verified
before any further distribution. The framing and recommendations reflect the AI's
interpretation of the brief and may not yet match the author's intended position.

**Responsibility Statement**
[Author name], Policy Analyst, is responsible for this work in its current state. It is shared
here for collaborative feedback and has not been approved for publication or external release.

---

## Example 6: Design Asset — AI-Assisted

**Context**: Designer created a set of icons for a library website. Used AI to generate
initial concepts for three icons; designed the remaining seven independently. Refined
all ten to match the library's visual system.

### Creation Note:
> This icon set was designed primarily by the designer. Three icons were initially generated
> by an AI image tool and subsequently refined to match the library's visual system. All ten
> icons were reviewed and approved by the design lead.

---

## Example 7: Email — AI-Supported

**Context**: User wrote an email, then asked AI to check tone and suggest edits. Accepted
two minor phrasing suggestions.

### Creation Note:
> This email was written by the author. An AI assistant (Claude, Anthropic) reviewed tone
> and suggested minor wording improvements, two of which the author incorporated. All content
> and send decisions were made by the author.

*(For routine internal communications, a full creation record is rarely warranted.)*

---

## Guidance: Creation Note vs. Creation Record vs. Draft Creation Record

Use a **creation note** when:
- The work is routine (internal comms, working documents, quick outputs)
- The statement is inline with the work (footer, cover note, byline)
- The audience is internal and familiar with AI-assisted work

Use a **creation record** when:
- The work will be published externally or submitted for formal review
- Academic integrity, legal, compliance, or procurement requirements apply
- The work is high-stakes (medical, legal, financial, policy)
- The nature of AI involvement is complex enough that a brief note would mislead
- You need a formal record for organizational AI governance documentation

Use a **draft creation record** when:
- The work is in progress and being shared for collaborative feedback
- The work hasn't been reviewed or approved yet
- You want colleagues to understand what they're building on
- Accuracy of AI-generated content hasn't yet been verified

---

## Example 8: Web Redesign — Multi-Party Team, Multiple AI Tools

**Context**: A library web team of four redesigned a department microsite. The UX researcher
conducted user interviews and synthesized findings using AI. The designer used AI to generate
initial layout concepts before refining them. The developer used AI to scaffold the frontend
code, which they then significantly modified. The content strategist wrote all content without
AI assistance but used AI to check reading level and accessibility of the final copy.
The project lead reviewed and approved the final work.

### Creation Note:
> This microsite was created by a four-person team (UX research, design, development, and
> content strategy) with AI assistance used differently across each discipline: AI supported
> research synthesis, generated initial design concepts, scaffolded frontend code, and
> reviewed content for readability. All AI outputs were substantially refined by team members.
> Reviewed and approved by [Project Lead name/role].

### Creation Record:

**Work Identification**
- Title: Special Collections Microsite Redesign
- Type: Web design and development project
- Date: June 2026
- Audience: Library patrons; internal staff
- Stage: Finalized

**AI Contribution Summary**
- Overall contribution: AI-Assisted (AI supported specific phases; humans led all design,
  content, and development decisions)
- Systems used:
  - Claude Sonnet (claude-sonnet-4-6, Anthropic) — research synthesis, content review
  - [Design AI tool, provider] — initial layout concept generation
  - Claude Sonnet (claude-sonnet-4-6, Anthropic) — frontend code scaffolding
- Prompt characterization: Mixed — structured prompts for synthesis and code scaffolding;
  single brief prompts for content review

**Human Contribution Summary**

> **[UX Researcher name or role]**
> Roles: UX Research · Usability Testing
> Contribution: Designed and conducted user interviews with eight library patrons. Used AI
> to assist in synthesizing interview transcripts into key themes; reviewed and validated all
> synthesized findings against source transcripts before incorporating into the design brief.

> **[Designer name or role]**
> Roles: Interaction Design · Visual Design · Prototyping
> Contribution: Developed the information architecture and visual design system. Used AI to
> generate three initial layout concepts as a starting point; substantially redesigned all
> layouts to align with the library's brand and accessibility standards.

> **[Developer name or role]**
> Roles: Implementation · Testing & QA · Accessibility Review
> Contribution: Built all frontend components. Used AI to scaffold the initial component
> structure; rewrote approximately 60% of the AI-generated code to meet performance and
> accessibility requirements. Conducted accessibility testing against WCAG 2.1 AA.

> **[Content Strategist name or role]**
> Roles: Content Strategy · Writing – Original Draft · Writing – Review & Editing
> Contribution: Wrote all web copy independently. Used AI to evaluate final copy for
> reading level and flag potential accessibility issues; made independent decisions about
> which suggestions to incorporate.

**Accountable approver**: [Project Lead name], [title/role]

**Process Narrative**
The project began with a UX research phase in which the researcher conducted structured
interviews with library patrons. AI tools assisted in synthesizing the interview transcripts,
with the researcher validating all synthesized themes against the source material before
sharing findings with the team.

The designer used the research findings to develop an information architecture and then
explored initial layout directions using an AI design tool. These AI-generated concepts served
as a starting point only — the designer substantially redesigned all layouts to meet the
library's visual standards and accessibility requirements. The final visual design is the
designer's own work.

The developer received the finalized designs and used an AI assistant to scaffold the initial
component structure. Approximately 60% of the scaffolded code was rewritten to meet
performance targets and pass accessibility testing. The developer conducted WCAG 2.1 AA
compliance testing on the final build.

The content strategist wrote all web copy without AI assistance, then used AI to evaluate
reading level and surface potential accessibility issues in the final copy. The strategist
made independent decisions about which suggestions to incorporate.

The project lead reviewed the complete work across all disciplines and approved it for launch.

**Responsibility Statement**
[Project Lead name], [title], reviewed and approved this project and accepts responsibility
for its accuracy, accessibility, and fitness for public release.

---

### Machine-Readable Record (multi-party example):

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
  "dc:title": "Special Collections Microsite Redesign",
  "dc:type": "web design and development project",
  "dc:date": "2026-06-04",
  "c2pa:documentStage": "finalized",
  "c2pa:recordType": "creation-record",
  "c2pa:assertions": [
    {
      "@type": "c2pa:AIGeneratedContent",
      "c2pa:role": "assisted_by",
      "c2pa:contributionLabel": "AI-Assisted",
      "c2pa:contributionMateriality": "moderate",
      "c2pa:model": {
        "c2pa:name": "Claude Sonnet",
        "c2pa:modelId": "claude-sonnet-4-6",
        "c2pa:provider": "Anthropic",
        "c2pa:versionNote": null
      },
      "c2pa:aiRoles": [
        "credit:investigation",
        "credit:writing-review-editing",
        "credit:software"
      ],
      "c2pa:promptCharacterization": "structured-prompt",
      "c2pa:promptSummary": "Used for research transcript synthesis, content readability review, and frontend code scaffolding. Each use was a discrete structured request.",
      "c2pa:iterationCount": null
    },
    {
      "@type": "c2pa:AIGeneratedContent",
      "c2pa:role": "assisted_by",
      "c2pa:contributionLabel": "AI-Assisted",
      "c2pa:contributionMateriality": "minor",
      "c2pa:model": {
        "c2pa:name": "[Design AI tool]",
        "c2pa:modelId": null,
        "c2pa:provider": "[Provider]",
        "c2pa:versionNote": "Tool and version not recorded at time of use"
      },
      "c2pa:aiRoles": ["cr:visual-design", "cr:prototyping"],
      "c2pa:promptCharacterization": "structured-prompt",
      "c2pa:promptSummary": "Generated three initial layout concepts from a design brief; all concepts substantially redesigned by human designer.",
      "c2pa:iterationCount": 1
    }
  ],
  "c2pa:humanReview": {
    "@type": "c2pa:HumanReviewAction",
    "c2pa:reviewer": "[Project Lead name]",
    "c2pa:reviewType": "approved",
    "c2pa:editingNature": "substantial revision",
    "c2pa:humanInputNature": "domain expertise, source material, original facts/arguments"
  },
  "prov:wasAttributedTo": [
    {
      "@type": "prov:Person",
      "schema:name": "[UX Researcher name or null]",
      "schema:jobTitle": "[title]",
      "schema:affiliation": "[organization]",
      "schema:url": null,
      "schema:sameAs": null,
      "c2pa:attributionNote": "named by contributor",
      "c2pa:contributorRoles": ["cr:ux-research", "cr:usability-testing"],
      "c2pa:contributionDescription": "Designed and conducted user interviews; validated AI-assisted synthesis of interview findings."
    },
    {
      "@type": "prov:Person",
      "schema:name": "[Designer name or null]",
      "schema:jobTitle": "[title]",
      "schema:affiliation": "[organization]",
      "schema:url": null,
      "schema:sameAs": null,
      "c2pa:attributionNote": "named by contributor",
      "c2pa:contributorRoles": ["cr:interaction-design", "cr:visual-design", "cr:prototyping"],
      "c2pa:contributionDescription": "Developed information architecture and visual design system; substantially redesigned all AI-generated layout concepts."
    },
    {
      "@type": "prov:Person",
      "schema:name": "[Developer name or null]",
      "schema:jobTitle": "[title]",
      "schema:affiliation": "[organization]",
      "schema:url": null,
      "schema:sameAs": null,
      "c2pa:attributionNote": "named by contributor",
      "c2pa:contributorRoles": ["cr:implementation", "cr:testing-qa", "cr:accessibility-review"],
      "c2pa:contributionDescription": "Built all frontend components; rewrote approximately 60% of AI-scaffolded code; conducted WCAG 2.1 AA accessibility testing."
    },
    {
      "@type": "prov:Person",
      "schema:name": "[Content Strategist name or null]",
      "schema:jobTitle": "[title]",
      "schema:affiliation": "[organization]",
      "schema:url": null,
      "schema:sameAs": null,
      "c2pa:attributionNote": "named by contributor",
      "c2pa:contributorRoles": ["cr:content-strategy", "credit:writing-original-draft", "credit:writing-review-editing"],
      "c2pa:contributionDescription": "Wrote all web copy independently; used AI to evaluate readability and accessibility of final copy, selectively incorporating suggestions."
    }
  ],
  "c2pa:responsibilityStatement": "[Project Lead name], [title], reviewed and approved this project and accepts responsibility for its accuracy, accessibility, and fitness for public release.",
  "prov:wasGeneratedBy": {
    "@type": "prov:Activity",
    "prov:startedAtTime": "2026-06-04T00:00:00Z",
    "prov:used": "User interview transcripts; library brand guidelines; existing site content"
  }
}
```

---

## Example 9: Code — AI-Drafted, Human-Revised (integrated codebase)

**Context**: A developer asked Claude to write a Python module for processing interlibrary
loan requests. The AI produced a complete module (~200 lines). The developer reviewed it,
rewrote the error handling and database connection logic substantially, added tests, and
integrated it into an existing Django application that the team maintains. The module will
be maintained going forward.

### Creation Note:
> The ILL request processing module was scaffolded by an AI assistant (Claude, Anthropic)
> from a functional specification. The developer substantially rewrote the error handling
> and database logic, added a test suite, and integrated the module into the team's Django
> application. The module is part of a living codebase and will be maintained over time.
> Reviewed and approved by [developer name/role].

### Creation Record:

**Work Identification**
- Title: `ill_processor.py` — Interlibrary Loan Request Processing Module
- Type: Software (Python module)
- Date: June 2026
- Use: Component in library services Django application
- Stage: Finalized (integrated; living codebase)

**AI Contribution Summary**
- Contribution: AI-Drafted, Human-Revised
- System: Claude Sonnet (claude-sonnet-4-6, Anthropic)
- AI roles: Implementation (initial module scaffolding, ~200 lines)
- Prompt characterization: Structured prompt — functional specification describing ILL
  workflow, data models, required endpoints, and integration constraints
- Integration depth: Integrated-limited — module has clear boundaries within the larger
  application; AI-generated structure remains but logic was substantially modified

**Human Contribution Summary**
- Developer provided: Functional specification, existing data models, Django application
  context, integration requirements
- Modification extent: Substantially modified — error handling and database connection
  logic rewritten; test suite added by developer; module integrated into existing codebase
- Approved by: [Developer name], [role]

**Process Narrative**
The developer provided a functional specification describing the module's required behavior
within the team's Django application. An AI assistant produced a complete initial module.
The developer reviewed the output, found the core request-routing logic sound but the error
handling and database connection patterns inconsistent with the team's existing conventions.
These sections were substantially rewritten. The developer also added a test suite covering
edge cases the AI output had not anticipated. The module was then integrated into the
application and deployed.

This creation record reflects the module at the time of initial integration. As a component
in a living codebase, the module will evolve over time, and this record should be reviewed
at major version milestones.

**Limitations**
The AI-generated code was reviewed and tested by the developer but was not subject to a
formal security review. Teams with security review requirements should conduct one
independently of this record.

**Responsibility Statement**
[Developer name], [role], reviewed and approved this module and accepts responsibility for
its correctness, integration quality, and fitness for production use.

---

## Example 10: Image — AI-Produced, Extensively Directed (brand-constrained)

**Context**: A library communications designer needed a hero image for a new research
guide landing page. She used Adobe Firefly, providing the library's brand color palette
and a reference photograph of the physical space. She generated approximately 20 candidates
across 8 prompting rounds, refining style and composition iteratively. She selected one
image and made minor color adjustments in Photoshop to match the brand palette exactly.

### Creation Note:
> This hero image was generated by an AI image tool (Adobe Firefly) through an iterative
> series of exchanges in which the designer provided brand guidelines, a reference photograph
> of the library space, and refined visual direction across eight rounds. One image was
> selected from approximately 20 candidates and lightly color-adjusted to match brand
> specifications. Approved by [designer name/role].

### Creation Record:

**Work Identification**
- Title: Research Guides Landing Page — Hero Image
- Type: Digital image (web)
- Date: June 2026
- Intended use: Web publication (library website, public-facing)
- Stage: Finalized

**AI Contribution Summary**
- Contribution: AI-Produced, Extensively Directed
- System: Adobe Firefly (Adobe)
- AI roles: Image generation
- Prompt characterization: Expert-directed iterative prompting — 8 rounds with brand
  guidelines and reference photograph provided; iterative refinement of style, composition,
  and lighting
- Style reference descriptor: Brand-constrained + style-reference (library brand palette
  and reference photograph of physical space provided as inputs)
- Selection: One image selected from approximately 20 candidates generated across all rounds
- Post-processing: Minor — color grading in Photoshop to match brand palette exactly

**Human Contribution Summary**
- Designer provided: Brand guidelines (color palette, typography, visual style), reference
  photograph of library space, iterative visual direction across 8 prompting rounds
- Post-processing: Light color adjustment in Photoshop
- Approved by: [Designer name], Communications Designer

**Process Narrative**
The designer needed a hero image consistent with the library's visual brand for a new
research guide landing page. She used Adobe Firefly, providing the library's brand color
palette and a reference photograph of the physical library space to anchor the composition.
Across eight rounds of prompting, she refined the visual style, adjusted lighting and
composition, and narrowed toward an image that felt grounded in the library's actual
environment while meeting the page's visual requirements.

Approximately 20 candidate images were generated across these rounds. The designer selected
one and made minor color adjustments in Photoshop to bring the palette into precise alignment
with brand specifications. The compositional and stylistic direction came from the designer;
the image rendering was produced by the AI tool.

**Limitations**
Adobe Firefly attaches C2PA-compliant content credentials to generated images. The
image file's embedded metadata provides a machine-verifiable record of AI generation
supplementing this self-reported creation record.

**Responsibility Statement**
[Designer name], Communications Designer, reviewed and approved this image and accepts
responsibility for its accuracy of representation, brand compliance, and fitness for
web publication.

---

## Example 11: Audio/Video — AI-Assisted (mixed layers)

**Context**: A library instruction team produced a 4-minute tutorial video. A librarian
recorded the screen capture and narrated in their own voice. AI was used for: (1) drafting
the script, which the librarian revised substantially; (2) auto-generating captions, which
were reviewed and corrected; (3) removing background noise from the audio recording.
No AI-synthesized voice was used.

### Creation Note:
> This tutorial video was created by a librarian who recorded screen capture and provided
> all narration in their own voice. AI assistance was used to draft the script (substantially
> revised by the librarian), generate captions (reviewed and corrected), and reduce
> background noise in the audio. Reviewed and approved by [librarian name/role].

### Creation Record:

**Work Identification**
- Title: "Finding Peer-Reviewed Articles in JSTOR" — Tutorial Video
- Type: Instructional video
- Duration: 4:12
- Date: June 2026
- Intended use: Library website; embedded in course guides
- Stage: Finalized

**AI Contribution Summary**
- Overall contribution: AI-Assisted
- AI involvement by layer:
  - **Script**: AI drafted initial script (Claude, Anthropic) from a brief; librarian
    substantially revised structure, examples, and tone before recording
    — Prompt characterization: Structured prompt
    — Human modification: Substantially revised
  - **Captions**: AI auto-generated captions (video platform tool, provider unspecified);
    librarian reviewed and corrected all captions before publication
    — Human modification: Lightly edited (accuracy corrections)
  - **Audio processing**: AI noise reduction applied via video editing software
    (tool unspecified); no human modification — automatic processing
    — Human modification: Used as-is
- Synthetic voice: None — all narration recorded by human librarian

**Human Contribution Summary**
- Librarian provided: All screen recording, all narration (own voice), revised script,
  caption corrections, overall direction and approval
- Approved by: [Librarian name], [role]

**Process Narrative**
The librarian began with an AI-drafted script based on a brief describing the video's
learning objectives and target audience. The draft provided a structural starting point
but required substantial revision — the librarian rewrote the introduction, adjusted
the pacing of the demonstration steps, and replaced generic examples with discipline-
specific ones relevant to the library's users.

The librarian then recorded screen capture and narrated the video in their own voice.
AI noise reduction was applied automatically through the video editing software during
export. After publishing a draft to the video platform, the librarian reviewed the
AI-generated captions for accuracy, correcting several library-specific terms and
proper nouns before finalizing the video for publication.

No AI-synthesized voice was used at any stage. All narration is the librarian's own.

**Responsibility Statement**
[Librarian name], [role], reviewed and approved this video and accepts responsibility
for the accuracy of its instructional content and its fitness for publication.
