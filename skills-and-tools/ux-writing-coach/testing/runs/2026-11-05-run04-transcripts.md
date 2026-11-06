# UX Writing Coach Run 04 Transcripts — 2026-11-05

Model: `api-glm-5.3-flash`. Harness: Codex CLI 0.151.0 with UCSD provider. Fresh sessions. Test marker: `UXWC_TEST_MODE=1`.

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

> **What works**
> - It gives the correct full prize name and clearly identifies the audience as UC San Diego undergraduates.
> - It mentions both class credit and campus research events, which helps students recognize eligible work.
> - It names the main work types without narrowing to one discipline.
>
> **Top opportunities**
> - Lead with the student or faculty task, not the Library’s announcement. Right now, the page explains the prize before telling users what to do.
> - Add faculty nomination guidance. Faculty nominators need to know whether they submit the entry, support a student submission, or only endorse it.
> - Clarify eligibility in concrete terms. “Participating,” “outstanding work,” “research-focused event,” and “Spring Quarter of the year” may raise questions about what qualifies and when.
>
> **Suggested revision**
> > **Undergraduate Library Research Prize**
> >
> > UC San Diego undergraduates can submit work completed for class credit or presented at a campus research-focused event. Submissions may be creative work, empirical research, or interpretive analysis. The Library will award five prizes for projects that show how Library resources, services, or expertise contributed to the student’s research.
> >
> > Students must be enrolled undergraduates during Spring Quarter of the year they submit. Faculty nominators should [describe whether they submit or endorse the entry and any required materials].
>
> A bolder alternative:
> > **Show Your Library Research**
> >
> > Did Library resources, services, or expertise strengthen your class project or campus research presentation? Submit your work for the Undergraduate Library Research Prize. The Library awards five prizes each year.
>
> **Why**
> - The suggested revision puts the student’s possible action first, then provides eligibility, project type, and the prize count. It also makes the Library-contribution criterion more concrete without implying every eligible project automatically wins.
> - The bolder alternative is better as an opening paragraph or promotional card, while the suggested revision works better as the full introductory section.
>
> **Hypothesis**
> Students may ask, “Can my project qualify?” and “How do I enter?” Faculty nominators may ask, “Do I submit for the student or nominate them separately?” User testing with a small mix of students and faculty would confirm whether “Spring Quarter,” “interpretive analysis,” and the contribution requirement are clear.
>
> Next steps: Confirm the number and value of prizes, faculty nomination process, submission deadline, and exact Spring Quarter enrollment requirement with the prize owner. Then test the opening with a few undergraduate students and faculty nominators.

**Note:** The final message omitted the skill introduction and test log. This was part of the Plan Gate failure.

### Turn 2 — User

> What should the primary call to action be? We want students to submit their work and faculty to nominate student projects. There are five prize categories, including Special Collections and the Data & GIS Lab, but I have not confirmed the current deadline or submission link.

### Turn 2 — Skill

> **Primary calls to action**
> Use two task-first actions so each audience sees a clear next step:
>
> - **Students:** `Submit your project`
> - **Faculty nominators:** `Nominate a student project`
>
> Place `Submit your project` first if students are the primary audience, with `Nominate a student project` immediately beside it as a secondary action. Avoid combining them as `Submit or nominate a project` because that blurs the next step and makes users parse two actions in one control.
>
> If the page section has room for supporting copy:
> > Submit your project  
> > Undergraduates can enter work completed for class credit or presented at a campus research-focused event.  
> >
> > Nominate a student project  
> > Faculty can nominate student projects that show how Library resources, services, or expertise contributed to the research.
>
> Keep the five categories, including Special Collections & Archives and the Data & GIS Lab, in the eligibility or categories section rather than in the CTA. Do not add a deadline until the prize owner confirms it.
>
> Next step: Confirm whether faculty submit directly, endorse a student submission, or provide nomination materials, then tailor the faculty CTA and its destination.

### Turn 3 — User

> Give me one revised opening paragraph that handles both audiences without becoming too long.

### Turn 3 — Skill

> UC San Diego undergraduates can submit projects completed for class credit or presented at a research-focused event on campus, and faculty can nominate student projects. Submissions may be creative work, empirical research, or interpretive analysis. Five prizes recognize work that shows how Library resources, services, or expertise contributed to the student’s research.

## A6 — Technology Lending Boundary

### Turn 1 — User

> UXWC_TEST_MODE=1
> Please review this proposed message for the Technology Lending Program page:
>
> “Need a charger, adapter, headphones, or calculator? Community borrowers and UC San Diego students, faculty, and staff can check out technology from the Library. Visit the front desk to borrow items.”
>
> Our service definition says TLP circulates technology items to current UC San Diego faculty, staff, and students. Limited media playback access is available to all other affiliations. Inventory includes chargers, adapters, headphones, portable DVD players, and calculators, but not computers or consumables.

### Turn 1 — Skill

> I’m the UX Writing Coach. I can help you plan, draft, revise, or evaluate Library UX copy.
>
> <!-- uxwc-test-log
> scenario: Policy, access, eligibility, or restrictions
> input_type: mixed
> plan_stage: shown
> response_template: plan-only
> copy_size: microcopy
> molecule: service overview with eligibility note and limit or boundary
> references_loaded:
> - content-scenarios.md: routed the request to policy, access, and eligibility guidance
> - working-plan.md: classified the input and applied the Plan Gate
> - response-templates.md: selected the plan-only response template
> - content-strategy-elements.md: identified the service overview, eligibility, and boundary elements
> - voice-and-messaging.md: applied service-page tone priorities
> - ux-writing-principles.md: applied task-first and eligibility-copy principles
> - library-terminology.md: checked Library naming and public-facing terminology
> - style-mechanics.md: checked UC San Diego naming and copy mechanics
> next_step: confirm facts, then provide copy-level feedback
> -->
>
> ## UX Writing Plan
>
> **Our Goal:** Help someone quickly determine whether they can borrow technology, understand the relevant access limits, and know where to go.
>
> **Our Audiences:** Current UC San Diego students, faculty, and staff; and people with other affiliations who may have limited media playback access.
>
> **User's Top "Jobs to be done":**
> - Find out what technology the Library offers.
> - Determine whether their affiliation is eligible.
> - Learn where to go to borrow or access the item.
> - Understand what is excluded or limited.
>
> **Our Approach:** Use a task-first service overview with a short inventory list, an eligibility note after the possible action, and a clear boundary for limited media playback access. Avoid implying that community borrowers can check out all technology.
>
> ## Questions for you
>
> **Please confirm:**
> - Exact service name and approved page title.
> - Exact front desk name and location, including whether one or multiple desks apply.
> - Whether limited media playback access means borrowing certain items, onsite use, or another arrangement.
> - Whether this message should list checkout periods, quantities, fees, or other service limits.
>
> Please reply with changes, or say “Go ahead” to draft.

### Turn 2 — User

> I do not want to exclude people unnecessarily, but I also do not want the message to promise laptop borrowing. Please create two accurate versions: one short alert-style message and one service-offering card.

### Turn 2 — Skill

> Here are two directions:
>
> **Option A — Short alert-style message**
> Borrow chargers, adapters, headphones, portable DVD players, and calculators. Current UC San Diego students, faculty, and staff can check them out; other affiliations have limited media playback access. Computers and consumables aren’t available. Visit [front desk name] to borrow or ask about access.
>
> **Why it works:** It leads with the available items, separates borrowing from limited access, and directly prevents a laptop-borrowing expectation. Replace the bracketed text with the exact desk name and location.
>
> **Option B — Service-offering card**
>
> **Borrow technology**
> UC San Diego students, faculty, and staff can check out chargers, adapters, headphones, portable DVD players, and calculators. Other affiliations have limited media playback access. Computers and consumables aren’t available.
>
> **Call to action:** Visit [front desk name and location]
>
> **Why it works:** The task-first title is scannable, the eligibility note follows the available action, and the exclusions are explicit without framing the service as closed. Replace the bracketed text with the approved desk name and location.
>
> **Strengths**
> - Preserves the distinction between current UC San Diego borrowing and limited access for other affiliations.
> - Names the full inventory and the key exclusions.
> - Keeps the action and destination visible.
>
> **Areas for improvement**
> - Confirm whether “limited media playback access” means borrowing, onsite use, or another arrangement.
> - Confirm the exact front desk name, location, and whether multiple desks provide the service.
> - Confirm whether “computers and consumables aren’t available” should use more concrete wording, such as “laptops and computer mice aren’t available,” based on the full inventory.
>
> Next steps: Ask the Technology Lending Program service owner to verify the service name, eligibility terms, media-access meaning, desk locations, and exclusions. Then run an accessibility and plain-language review before publication.

### Turn 3 — User

> Can the skill tell me what would need to be checked before publishing either one?

### Turn 3 — Skill

> Before sending for review, check:
>
> - **Service identity:** Confirm the approved public name is “Technology Lending Program” and that the page title, card title, and alert language use it consistently.
> - **Eligibility and access:** Verify that only current UC San Diego students, faculty, and staff can borrow items, and exactly what “limited media playback access” means for other affiliations.
> - **Inventory and exclusions:** Confirm every listed item is current, complete, and accurate, and clarify whether the exclusion should say “computers and consumables” or name specific examples such as laptops.
> - **Action and location:** Verify the exact front desk name, location, hours, and whether multiple service points apply.
> - **Borrowing details:** Confirm whether the message needs checkout periods, quantity limits, fees, reservation steps, or a link to the full borrowing policy.
> - **Task fit:** Test whether each version prevents the impression that laptops can be borrowed, especially for users arriving from a search for “laptop loan.”
> - **Accessibility and plain language:** Check heading structure, link text, list semantics, color contrast for alert styling, mobile rendering, and screen-reader output.
> - **Voice and mechanics:** Confirm UC San Diego Library naming, sentence case, punctuation, link text, and consistent use of “UC San Diego” rather than “UCSD” ([Library UX](https://ucsdlibrary.atlassian.net/wiki/x/AoC_0)).
> - **Owner review:** Send both versions to the service owner for policy, terminology, and operational accuracy before publication.
>
> Next step: Ask the service owner to confirm the access model and desk details, then use their answers to finalize either version.
