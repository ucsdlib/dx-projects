# Contributor Roles Taxonomy

This file defines the full role taxonomy used in creation records. It has three layers:

1. **CRediT roles** — verbatim from the Contributor Roles Taxonomy (https://credit.niso.org).
   Citable as a standard. Use official URIs.
2. **DX Extension — Design & UX** — drawing from Nielsen Norman Group role taxonomy.
   Use `creativerecord.org` extension URIs. Not a ratified standard.
3. **DX Extension — Software & Code** — drawing from SWEBOK / industry vocabulary.
   Use `creativerecord.org` extension URIs. Not a ratified standard.
4. **DX Extension — Editorial & Multimedia** — drawing from Dublin Core / MARC relators.
   Use `creativerecord.org` extension URIs. Not a ratified standard.
5. **Cross-cutting** — general roles applicable across contexts.

---

## Namespaces

| Prefix | URI | Notes |
|---|---|---|
| `credit:` | `https://credit.niso.org/contributor-roles/` | CRediT official URIs |
| `cr:` | `https://creativerecord.org/contributor-roles/` | Extension roles (generic, not institution-specific) |

---

## Layer 1: CRediT Roles

Use these verbatim for research, writing, and academic publishing contexts.
Source and definitions: https://credit.niso.org

| Role | URI slug | Definition | When to suggest |
|---|---|---|---|
| Conceptualization | `credit:conceptualization` | Ideas; formulation or evolution of overarching research goals and aims | Any work where a human defined the core concept or problem |
| Data Curation | `credit:data-curation` | Management activities to annotate, scrub, maintain research data and associated metadata | Data-heavy work; research outputs |
| Formal Analysis | `credit:formal-analysis` | Application of statistical, mathematical, computational, or other formal techniques | Analytical reports, research, quantitative work |
| Funding Acquisition | `credit:funding-acquisition` | Acquisition of financial support for the project | Grant-funded work |
| Investigation | `credit:investigation` | Conducting the research and investigation process, specifically performing the experiments or data collection | Original research; primary source work |
| Methodology | `credit:methodology` | Development or design of methodology; creation of models | Research design; framework development |
| Project Administration | `credit:project-administration` | Management and coordination responsibility for the research activity planning and execution | Project leads; program managers |
| Resources | `credit:resources` | Provision of study materials, reagents, materials, patients, laboratory samples, animals, instrumentation, computing resources, or other analysis tools | Providing tools, data sets, or infrastructure |
| Software | `credit:software` | Programming, software development; designing computer programs; implementation of computer code and supporting algorithms | Any coding or software development work |
| Supervision | `credit:supervision` | Oversight and leadership responsibility for the research activity planning and execution | Managers, supervisors, faculty advisors |
| Validation | `credit:validation` | Verification, whether as part of the activity or separate, of the overall replication/reproducibility of results/experiments and other research outputs | QA, fact-checking, accuracy review |
| Visualization | `credit:visualization` | Preparation, creation, and/or presentation of the published work, specifically visualization/data presentation | Charts, diagrams, data visualization |
| Writing – Original Draft | `credit:writing-original-draft` | Preparation, creation, and/or presentation of the published work, specifically writing the initial draft | AI commonly takes this role; human authors too |
| Writing – Review & Editing | `credit:writing-review-editing` | Preparation, creation, and/or presentation of the published work by those from the original research group, specifically critical review, commentary, or revision | Human revision of AI drafts; editorial review |

---

## Layer 2: DX Extension — Design & UX

Drawing from Nielsen Norman Group role vocabulary (https://www.nngroup.com).

| Role | URI slug | Description | When to suggest |
|---|---|---|---|
| UX Research | `cr:ux-research` | Planning and conducting user research to understand needs, behaviors, and pain points | Any work grounded in user insights |
| Usability Testing | `cr:usability-testing` | Designing and running tests with real users to evaluate designs or prototypes | Evaluation phases; iterative design |
| Interaction Design | `cr:interaction-design` | Defining how users interact with a system; flows, behaviors, states | Digital product design; app/web UI |
| Visual Design | `cr:visual-design` | Visual execution of a design system; layout, typography, color, iconography | Design outputs; brand work |
| Information Architecture | `cr:information-architecture` | Organizing and structuring content and navigation for findability and usability | Website design; content-heavy systems |
| Content Strategy | `cr:content-strategy` | Planning, creation, governance of content to meet user and organizational needs | Web content; editorial planning |
| Accessibility Review | `cr:accessibility-review` | Evaluating work against accessibility standards (e.g., WCAG); identifying and addressing barriers | Web/digital work; any public-facing output |
| Prototyping | `cr:prototyping` | Creating low- or high-fidelity prototypes to test and communicate design ideas | Design and product development |
| Service Design | `cr:service-design` | Designing end-to-end service experiences across channels and touchpoints | Complex systems; cross-functional work |

---

## Layer 3: DX Extension — Software & Code

Drawing from SWEBOK (https://www.computer.org/education/bodies-of-knowledge/software-engineering)
and common industry vocabulary.

| Role | URI slug | Description | When to suggest |
|---|---|---|---|
| Requirements Definition | `cr:requirements-definition` | Gathering, analyzing, and documenting what a system needs to do | Project initiation; feature definition |
| System Architecture | `cr:system-architecture` | High-level design of system structure, components, and their relationships | Complex software; infrastructure work |
| Implementation | `cr:implementation` | Writing code to build a feature, system, or tool | Any coding work |
| Code Review | `cr:code-review` | Reviewing code written by others for correctness, quality, and maintainability | Collaborative development |
| Testing & QA | `cr:testing-qa` | Writing and executing tests; identifying defects; quality assurance | Software delivery |
| DevOps & Deployment | `cr:devops-deployment` | Building, deploying, and maintaining systems in production environments | Infrastructure; release management |
| Technical Documentation | `cr:technical-documentation` | Writing documentation for code, APIs, systems, or processes | Developer-facing outputs |
| Security Review | `cr:security-review` | Evaluating code or systems for security vulnerabilities and risks | Any production code |

---

## Layer 4: DX Extension — Editorial & Multimedia

Drawing from Dublin Core (https://dublincore.org) and MARC Relator terms
(https://www.loc.gov/marc/relators/).

| Role | URI slug | Description | When to suggest |
|---|---|---|---|
| Editorial Direction | `cr:editorial-direction` | Setting editorial vision, standards, and priorities for a publication or content project | Content teams; publications |
| Translation | `cr:translation` | Converting content from one language to another | Multilingual work |
| Narration | `cr:narration` | Providing spoken narration for audio or video content | Multimedia; instructional content |
| Illustration | `cr:illustration` | Creating visual illustrations, diagrams, or artwork | Reports; educational content |
| Audio/Video Production | `cr:audio-video-production` | Recording, editing, and producing audio or video content | Multimedia projects |
| Data Visualization | `cr:data-visualization` | Designing and creating visual representations of data | Reports; dashboards |

---

## Layer 5: Cross-cutting

| Role | URI slug | Description | When to suggest |
|---|---|---|---|
| Equity & Inclusion Review | `cr:equity-inclusion-review` | Reviewing work for equity, inclusion, and anti-bias considerations | Public-facing work; policy; design |
| Project Sponsorship | `cr:project-sponsorship` | Organizational sponsorship and executive accountability for a project | Formal projects with executive oversight |
| Stakeholder Communication | `cr:stakeholder-communication` | Managing communication with stakeholders about the work | Project-based work |

---

## Context Guidance: Suggested Roles by Work Type

When gathering contributor information, offer the most relevant roles for the work type.
Don't present all 41 options — use this table to narrow to a relevant subset.

| Work type | Most relevant roles to offer |
|---|---|
| Research article / report | Conceptualization, Investigation, Methodology, Formal Analysis, Data Curation, Writing – Original Draft, Writing – Review & Editing, Visualization, Validation |
| Website / web app | UX Research, Interaction Design, Visual Design, Information Architecture, Content Strategy, Implementation, Testing & QA, Accessibility Review, DevOps & Deployment |
| Policy brief / white paper | Conceptualization, Investigation, Writing – Original Draft, Writing – Review & Editing, Stakeholder Communication, Editorial Direction |
| Software / code | Requirements Definition, System Architecture, Implementation, Code Review, Testing & QA, Technical Documentation, Security Review |
| Design system / brand | Visual Design, Interaction Design, Content Strategy, Prototyping, Accessibility Review |
| Instructional / educational content | Conceptualization, Writing – Original Draft, Writing – Review & Editing, Visualization, Illustration, Narration, Accessibility Review |
| Data analysis / dashboard | Formal Analysis, Data Curation, Data Visualization, Validation, Software |
| Multimedia / video | Audio/Video Production, Narration, Illustration, Content Strategy, Editorial Direction |
| Internal communication | Writing – Original Draft, Writing – Review & Editing, Editorial Direction |

---

## AI Role Assignment

AI systems can be assigned roles from this taxonomy in the `c2pa:aiRoles` array.
Common AI roles:

- Writing–heavy work: `credit:writing-original-draft`, `credit:writing-review-editing`
- Code: `credit:software`, `cr:implementation`, `cr:technical-documentation`
- Research support: `credit:investigation`, `credit:data-curation`, `credit:formal-analysis`
- Design: `cr:visual-design`, `cr:prototyping`, `credit:visualization`
- Translation: `cr:translation`

---

## Notes on Role Assignment

- A person (or AI) can hold **multiple roles** on a single work.
- Roles describe **what someone actually did**, not their job title.
- The same person may have different roles on different works.
- For works in progress, roles may still be evolving — note this if relevant.
- Not every role needs to be filled — only record roles that are accurate.
