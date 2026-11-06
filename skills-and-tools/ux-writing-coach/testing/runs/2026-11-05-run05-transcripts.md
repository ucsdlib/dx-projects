# UX Writing Coach Run 05 Transcripts — 2026-11-05

Model: `api-glm-5.3-flash`. Harness: Codex CLI 0.151.0 with UCSD provider. Fresh A4 session after the structured-evaluation Plan Gate update. Test marker: `UXWC_TEST_MODE=1`.

## A4 — Undergraduate Library Research Prize

### Turn 1 — User

> UXWC_TEST_MODE=1
> Please evaluate this draft page section for the Undergraduate Library Research Prize. I am especially interested in whether it works for undergraduate students and faculty nominators.
>
> Current page:
>
> “Undergraduate Library Research Prize
>
> The UC San Diego Library is proud to announce the annual Undergraduate Library Research Prize, which recognizes outstanding work conducted by participating UC San Diego undergraduate students and how the Library contributed to their success. The prize helps demonstrate to the campus and broader community how the Library’s resources, services, and expertise are essential to effective research conducted by students at the undergraduate level. The Library currently offers 5 prizes. Work can be submitted if it was completed for class credit or presented at a research-focused event on campus. Submissions may be creative work, empirical research, or interpretive analysis. Students must be enrolled undergraduates in the Spring Quarter of the year in which they submit their work.”

### Turn 1 — Skill

> I’m the UX Writing Coach. I can help you plan, draft, revise, or evaluate Library UX copy.
>
> <!-- uxwc-test-log
> scenario: policy, access, eligibility, or restrictions
> input_type: rewrite object
> plan_stage: shown
> response_template: plan-only
> copy_size: short-form
> molecule: eligibility and access / service overview
> references_loaded:
> - content-scenarios.md: identified the prize page as structured eligibility content
> - working-plan.md: applied the plan-first gate for service page evaluation
> - response-templates.md: selected the plan-only response shape
> - ux-writing-principles.md: considered task-first structure and audience fit
> - voice-and-messaging.md: considered Library voice and welcoming tone
> - content-strategy-elements.md: considered eligibility, requirements, and calls to action
> next_step: wait for user confirmation
> -->
>
> ## UX Writing Plan
>
> **Our Goal:** Help undergraduate students quickly decide whether they are eligible, what qualifies, and how to submit; help faculty nominators understand their role and next step.
>
> **Our Audiences:** UC San Diego undergraduate students, including first-time or less-confident library users, and faculty nominators who need a clear task path.
>
> **User's Top “Jobs to be done”:**
> - Decide whether their work is eligible.
> - Understand what the Library is recognizing.
> - Find the deadline and submission or nomination step.
> - Understand whether faculty nominate separately or support a student submission.
>
> **Our Approach:** Use an action-first lead, then separate student eligibility and faculty nomination paths into short scannable sections. This avoids burying the main tasks and helps both audiences find their role quickly.
>
> ## Questions for you
>
> **Please confirm:**
> - Can faculty nominate student work directly, or only support or endorse a student submission?
> - What are the deadline, submission link, prize distribution, and any team or faculty-nominator requirements?
>
> Reply with changes, or say “Go ahead” to draft.

### Turn 2 — User

> What should the primary call to action be? We want students to submit their work and faculty to nominate student projects. There are five prize categories, including Special Collections and the Data & GIS Lab, but I have not confirmed the current deadline or submission link.

### Turn 2 — Skill

> Use **two parallel calls to action** rather than one shared CTA. The audience and task differ, so a single “Submit” could confuse faculty nominators or imply they are submitting their own work.
>
> **Recommended CTAs**
> - **Students:** “Submit your work”
> - **Faculty:** “Nominate a student project”
>
> If the page needs one primary CTA before the audience split, make the student path primary: **“Submit your work.”** Place **“Nominate a student project”** immediately beside it as the faculty path.
>
> While the deadline and submission link are unconfirmed, use safer interim CTAs: **“See how to submit your work”** and **“See how to nominate a student project.”** Do not publish final “Submit” CTAs until the actual deadline and destination are confirmed.
>
> This follows [Library UX: Microcopy](https://ucsdlibrary.atlassian.net/wiki/x/AoC_0) guidance to make interface actions specific.

### Turn 3 — User

> Give me one revised opening paragraph that handles both audiences without becoming too long.

### Turn 3 — Skill

> Submit your work for the annual prize, or nominate a student project if you are a faculty member. The UC San Diego Library recognizes outstanding undergraduate research in five categories and the Library resources, services, and expertise that support it. Projects may be creative work, empirical research, or interpretive analysis completed for course credit or presented at a campus research-focused event. Students must be enrolled UC San Diego undergraduates in Spring Quarter of the submission year.
