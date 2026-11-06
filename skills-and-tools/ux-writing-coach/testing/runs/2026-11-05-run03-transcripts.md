# UX Writing Coach Run 03 Transcripts — 2026-11-05

Skill version: V2, 2026-11-05 response-template update. Model: `api-glm-5.3-flash`. Harness: Codex CLI 0.151.0 with UCSD provider. Each scenario used a fresh session and the `UXWC_TEST_MODE=1` marker in Turn 1.

## A1 — Ask Service Overview

### Turn 1 — User

> UXWC_TEST_MODE=1
> I need to turn our internal Ask service definition into a public-facing service overview for the Library website. Here is the source material:
>
> The Ask service is the front-line service that provides quick answers, orientation, and referrals for anyone contacting the UC San Diego Library. Interactions are brief, usually under five minutes, and focus on resolving common questions, clarifying policies and spaces, or connecting users to the right expertise or resource.
>
> Support is available in person at Library service points, online through email and web forms, and by phone. When needs are more in-depth, staff refer users to the appropriate Library, campus, or community service.
>
> In person: Geisel Library Front Desk, WongAvery Front Desk, Library tabling events, and Library Administrative Office.
> Online: email, web forms, and virtual meetings.
> Phone: Library main telephone line.
>
> In scope: known-item searches, introductions to UC Library Search, information about Library spaces, services, amenities, and policies, referrals or directions to campus services, assistance with Library equipment, and campus print service.
> Out of scope: research question or topic development, personalized research support or training, and help with personal technology beyond eligible Library services.

### Turn 1 — Skill

> I’m the UX Writing Coach. I can help you plan, draft, revise, or evaluate Library UX copy.
>
> <!-- uxwc-test-log
> scenario: General service page or long-form help
> input_type: source material
> plan_stage: shown
> response_template: plan-only
> copy_size: long-form
> molecule: service overview
> references_loaded:
> - content-scenarios.md: routed the service-page task
> - working-plan.md: classified source material and applied the Plan Gate
> - response-templates.md: selected the plan-only response
> - content-strategy-elements.md: selected the service overview molecule
> - voice-and-messaging.md: applied Library voice and service-page tone
> - library-style.md: guided concise, user-centered transformation
> - ux-writing-principles.md: guided structure and scannability
> - library-terminology.md: checked Library naming conventions
> - style-mechanics.md: guided punctuation, links, and naming mechanics
> next_step: user confirms plan or supplies missing contact links and details
> -->
>
> **Goal:** Help anyone contacting the UC San Diego Library get a quick answer, understand where to go, and know when Ask will refer them elsewhere.
>
> **Audience:** All current and prospective Library users, including students, employees, researchers, visitors, and community users with no prior knowledge of Library services.
>
> **Top jobs:**
> 1. Get help with common Library questions.
> 2. Choose an in-person, online, or phone option.
> 3. Understand what Ask can help with.
> 4. Know when and where a referral may be needed.
>
> **Approach:** A public service overview that opens with the user’s task, then uses short sections for what Ask helps with, how to connect, and what happens for more complex needs. Boundaries belong in a clear, respectful “not handled here” section followed by the likely referral path.
>
> **To confirm:**
> - Exact contact links, forms, email addresses, phone number, and service point pages to include.
> - Whether virtual meetings are available on request, by appointment, or through another scheduling process.
> - Preferred page title and whether “Ask” is widely understood by all audiences or needs a clarifying subtitle.
> - Exact scope for equipment and campus print services, including eligibility limits if any.
>
> Reply with changes, or say “Go ahead” to draft.

### Turn 2 — User

> Use the service overview structure with a lead, description, service offerings, and contact or help path. Keep the internal workflow details off the page.

### Turn 2 — Skill

> Here’s the recommended draft in the confirmed service overview structure:
>
> # Ask: Quick help from the UC San Diego Library
>
> Get quick answers, find your way around the Library, and connect with the right resource. Ask is a starting point for common questions about Library services, spaces, materials and policies.
>
> When your question needs more time or specialized help, we’ll connect you with the right Library, campus or community resource. That includes research questions, topic development, personalized research support and training, and personal technology outside eligible Library services.
>
> ## What Ask can help with
>
> - Find an item you already know about
> - Get started with UC Library Search
> - Learn about Library spaces, services, amenities and policies
> - Get help using Library equipment
> - Get help with campus printing
> - Get connected to the right Library, campus or community resource
>
> ## How to connect
>
> - **In person:** Visit the Geisel Library Front Desk, WongAvery Front Desk, Library Administrative Office or a Library tabling event.
> - **Online:** [Email Ask], [submit a Library web form], or [join a virtual meeting].
> - **By phone:** Call [the Library’s main telephone line].
>
> [Get help from Ask]
>
> I kept interaction length, front-line framing and internal routing details off the page. Replace the bracketed link text and phone number with verified contact details before publication.

### Turn 3 — User

> Someone reviewing the draft asked whether we should show the under-five-minute expectation and the out-of-scope list. What would you recommend?

### Turn 3 — Skill

> I’d keep the under-five-minute expectation off the page and translate the out-of-scope list into a brief, user-centered boundary.
>
> **Under-five minutes**
> Don’t publish it as an expectation. It is an internal performance measure, can vary by channel and question, and could make users rush or staff feel pressured. The lead’s phrase “quick answers” already conveys the benefit without making a time promise.
>
> **Out-of-scope list**
> Yes, but not as a wholesale internal scope list. Make the limits visible enough to prevent misrouting, then immediately show the next step:
>
> > Ask is a starting point for quick Library questions. For in-depth research support, topic development or personalized training, we can connect you with the right Library expertise. For personal technology outside eligible Library services, we can point you to the appropriate campus or community resource.
>
> This preserves the boundary while keeping the emphasis on how the user can move forward. Next step: confirm whether the referrals for research support and personal technology should link to specific services.

**A1 result:** Pass. The skill used the plan-only template, included all five fields, stopped before drafting, and kept internal workflow language out of the draft.

## A2 — Borrow Offering Cards

### Turn 1 — User

> UXWC_TEST_MODE=1
> Our internal service description for our “Borrow and Use Physical Collections” service says: “The Borrow and Use Physical Collections service provides access to the UC San Diego Library’s onsite print and media collections for in-person use and loan, supporting users in requesting, obtaining, and using materials from the Library’s general and select mediated collections. Through a mix of self-service options and staff support, users can locate items in the stacks, request retrieval from non-public or offsite locations, borrow eligible items for offsite use, and use non-circulating materials in Library spaces, with clear expectations and consistent processes that make access predictable, equitable, and transparent.”
>
> Please turn this into short cards users can scan.

### Turn 1 — Skill

> I’m the UX Writing Coach. I can help you plan, draft, revise, or evaluate Library UX copy.
>
> <!-- uxwc-test-log
> scenario: general service page or structured service content
> input_type: source material
> plan_stage: shown
> response_template: plan-only
> copy_size: short-form
> molecule: service-offering cards
> references_loaded:
> - content-scenarios.md: identified the service-content routing
> - working-plan.md: applied the plan gate for source material
> - response-templates.md: selected the plan-only response
> - ux-writing-principles.md: applied scanning and user-task guidance
> next_step: draft cards after confirmation
> -->
>
> I’m treating your service description as source material, not copy to polish sentence by sentence.
>
> **Goal:** Help users quickly choose the right way to find, borrow, or use Library materials.
>
> **Audience:** Likely includes UC San Diego students, faculty, and staff, but the source does not state eligibility or whether community borrowers and visitors should be addressed.
>
> **Top jobs:**
> - Find materials in the stacks.
> - Request items from non-public or offsite locations.
> - Borrow eligible items for offsite use.
> - Use non-circulating materials in Library spaces.
>
> **Approach:** A short set of service-offering cards, each with a task-based title, one-line benefit or action, and any essential limit or next step. I would avoid splitting the internal definition sentence by sentence.
>
> **To confirm:**
> - Where the cards will appear and who the primary audience is.
> - Whether each card should have a link or action, such as “Search the catalog,” “Request pickup,” or “Ask for help.”
> - Any eligibility differences for mediated access, offsite storage retrieval, borrowing, or onsite-only materials.
>
> Reply with changes, or say “Go ahead” to draft.

### Turn 2 — User

> Use service-offering cards for borrowing, renewing, requesting items (which includes both "Request for pick-up" and Interlibrary Loan), and Course Reserves. For each card, give a title, lead, and primary call to action.

### Turn 2 — Skill

> Here’s a recommended card set:
>
> | Title | Lead | Primary CTA |
> | --- | --- | --- |
> | Borrow books and media | Check out eligible books and media to use away from the Library. | Find borrowing options |
> | Renew items | Extend the checkout period on eligible items before they’re due. | Renew your items |
> | Request items | Ask us to retrieve an item for pickup, or borrow it from another library through interlibrary loan. | Request an item |
> | Course reserves | Find materials your instructor set aside for your class. | Search course reserves |
>
> A bolder title-only alternative: “Take it with you,” “Keep it longer,” “Can’t find it? Request it,” and “Ready for class.” Keep the same leads and CTAs.
>
> Next step: confirm the CTA destinations, especially whether request for pickup and interlibrary loan share one entry point.

### Turn 3 — User

> Can you review the cards for voice and any wording that would confuse someone who has never used UC San Diego Library before?

### Turn 3 — Skill

> **What works**
> - The cards are task-first and scannable.
> - The voice is close to Library style: direct, useful, and not institutional.
> - “Course reserves” clearly explains what the service is for.
>
> **Top opportunities**
> - “Eligible” is a common Library constraint, but a first-time user may not know what it means in context.
> - “Request items” covers two different paths, so the lead should make the distinction easier to see.
> - “Interlibrary loan” is useful terminology, but the plain-language explanation should come first.
>
> **Suggested revisions**
>
> | Card | Revised copy | Why |
> | --- | --- | --- |
> | Borrow books and media | Check out books, media, and other materials you can take out of the Library. | Makes the boundary concrete without relying on “eligible.” |
> | Renew items | Extend the due date on items that can be renewed. | “Due date” is more familiar than “checkout period.” |
> | Request items | Can’t find what you need? We can get it ready for pickup, or borrow it from another library. | Warmer, clearer, and separates pickup from borrowing elsewhere. |
> | Course reserves | Find materials your instructor set aside for your class. | Already user-centered; no change needed. |
>
> For the request card, a primary CTA of **Start a request** may work better than “Request an item” because it signals the user is beginning a process with options.
>
> Next step: confirm whether “another library” should be described as another UC library, libraries beyond UC San Diego, or both.

**A2 result:** Pass. The skill held the requested card format for Turn 2, used a complete plan-only turn first, and gave concrete feedback on first-time-user wording.

## A3 — Technology Lending Outage

### Turn 1 — User

> UXWC_TEST_MODE=1
> We need an outage message for the Technology Lending Program. Current draft: “Attention users: The Tech Lending Program is experiencing a system malfunction which has rendered the check-out process inoperable. We apologize for any inconvenience this may cause. Users are advised to await further communication.”
>
> It can be up to three sentences.

### Turn 1 — Skill

> Here are two options, each within three sentences:
>
> **Recommended**
> > Technology Lending Program checkouts are unavailable. We’re working to restore service and will share an update as soon as possible.
>
> **With help path**
> > Technology Lending Program checkouts are unavailable right now. We’re working to restore service and will share an update as soon as possible. For help, contact [insert service desk or support contact].
>
> This version replaces the broad phrase “system malfunction” with a concrete status and leads users to the immediate limitation. The second option adds the support path that outage copy should include.
>
> Next step: confirm the correct support contact or where updates will appear.
>
> <!-- uxwc-test-log
> scenario: errors-alerts-outages-system-status
> input_type: rewrite object
> plan_stage: skipped
> response_template: direct-drafting
> copy_size: microcopy
> molecule: status, alert, or help message
> references_loaded:
> - content-scenarios.md: routed outage copy to status messaging guidance
> - ux-writing-principles.md: applied brevity and actionable error patterns
> - content-strategy-elements.md: applied status/alert molecule structure
> - voice-and-messaging.md: applied calm, concrete, reassuring tone
> - style-mechanics.md: applied sentence case, punctuation, and naming rules
> next_step: confirm support contact or update location
> -->

### Turn 2 — User

> Please give me three options with one-line reasons. The item is unavailable right now, but staff can still help at the Geisel Library Front Desk. We do not yet know when lending will resume.

### Turn 2 — Skill

> **Options**
> - **Recommended:** Technology Lending Program checkouts are unavailable right now. Staff at the Geisel Library Front Desk can still help. We don’t yet know when lending will resume.  
>   *Reason:* Leads with the concrete status, gives a clear support path, and sets expectations plainly.
>
> - **Support-first:** Need to check out technology? Staff at the Geisel Library Front Desk can help while Technology Lending Program checkouts are unavailable. We don’t yet know when lending will resume.  
>   *Reason:* Opens with the user’s task and routes them to help sooner.
>
> - **Shorter:** Technology Lending Program checkouts are unavailable, and staff at the Geisel Library Front Desk can help in the meantime. We don’t yet know when lending will resume.  
>   *Reason:* Combines the status and support path to save space while keeping the key facts.
>
> Next step: choose the option that best fits the placement and confirm whether the update will appear on the same page or channel.

### Turn 3 — User

> The final one must be under 180 characters and say users can ask staff for alternatives. Please revise the best option.

### Turn 3 — Skill

> Here’s the revised best option, at 170 characters:
>
> > Technology Lending Program checkouts are unavailable right now. Ask staff at the Geisel Library Front Desk about alternatives. We don’t yet know when lending will resume.
>
> This keeps the concrete status, adds the alternatives path, and sets expectations clearly.
>
> Next step: confirm the final wording with the Technology Lending Program service owner before publishing.

**A3 result:** Pass. The skill appropriately skipped the plan for short, well-specified microcopy, provided distinct options, and preserved unknown timing.

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
> scenario: event or promotion
> input_type: rewrite object
> plan_stage: skipped
> response_template: feedback-evaluation
> copy_size: short-form
> molecule: event or promotion
> references_loaded:
> - content-strategy-elements.md: promotion and eligibility structure
> - ux-writing-principles.md: scanning, audience fit, and short-form guidance
> - voice-and-messaging.md: Library voice and tone
> - response-templates.md: feedback response shape
> next_step: service-owner verification and user testing
> -->
>
> **What works**
> - The title is clear and names the prize accurately.
> - The project types and enrollment requirement preserve useful eligibility information.
> - The explanation of the Library’s contribution gives faculty nominators a reason to nominate.
>
> **Top opportunities**
> - Lead with the action: students should immediately see that they can submit work. Faculty nominators should see their role just as clearly.
> - Clarify “5 prizes.” Say “five prizes” and identify whether these are different award levels, categories, or five total winners.
> - Add the essential facts users will look for next: deadline, time, submission form or instructions, and any separate nomination process.
>
> **Suggested revision**
> > Submit your work for the annual Undergraduate Library Research Prize.
> >
> > The Library awards five prizes for creative work, empirical research, or interpretive analysis that shows how Library resources, services, and expertise supported the project. Eligible projects were completed for class credit or presented at a campus research-focused event. Entrants must be enrolled undergraduates during Spring Quarter of the submission year.
> >
> > [Submit your work] Deadline: [date and time]
> > [Nominate a student project]
>
> A bolder lead could be: “What did you discover with the Library? Submit your work for the annual Undergraduate Library Research Prize.”
>
> **Why**
> Hypothesis: students can identify the prize but may not know what to do next, while faculty nominators may not recognize whether they submit directly or use a separate nomination path. The revision follows [Library UX: Voice](https://ucsdlibrary.atlassian.net/wiki/x/AoC_0) by leading with the possible action and using warmer, more direct language.
>
> **Next step**
> Ask the prize owner to verify the five prizes, exact eligibility language, whether faculty nominators have a separate process, and the submission deadline. Then user-test the lead and calls to action with a few undergraduates and faculty nominators.

### Turn 2 — User

> What should the primary call to action be? We want students to submit their work and faculty to nominate student projects. There are five prize categories, including Special Collections and the Data & GIS Lab, but I have not confirmed the current deadline or submission link.

### Turn 2 — Skill

> Use **“Submit your work”** as the primary call to action. Faculty nomination should be the visible secondary action, not merged into the same label.
>
> **Recommended buttons**
> - Primary: `Submit your work`
> - Secondary: `Nominate a student project`
> - Supporting link: `See the five prize categories`
>
> **Why**
> - Students are the entrants, so their task should drive the page’s main action.
> - “Submit your work” is specific and warmer than “Submit.”
> - “Nominate a student project” clearly addresses faculty without making them the primary audience.
> - The categories deserve their own section so users can decide where their project fits before submitting.
>
> Until the deadline and submission link are confirmed, do not publish the submission button. Use placeholders during drafting, such as `[Submission link to be confirmed]` and `[Deadline to be confirmed]`, and verify the official category names for Special Collections and the Data & GIS Lab with the prize owner.

### Turn 3 — User

> Give me one revised opening paragraph that handles both audiences without becoming too long.

### Turn 3 — Skill

> Here’s a revised opening paragraph:
>
> > Submit your work for the annual Undergraduate Library Research Prize. Faculty can nominate a student project. The Library offers five prize categories, including Special Collections and the Data & GIS Lab, for undergraduate projects completed for class credit or presented at a campus research-focused event. [Deadline to be confirmed.]

**A4 result:** Fail on the plan gate, pass on copy quality. The skill skipped the plan and combined evaluation with revisions, but the audience fit, CTA hierarchy, verification language, and revised copy were strong.

## A5 — Ask Contact and Support

### Turn 1 — User

> UXWC_TEST_MODE=1
> Our Ask page has a generic “Contact Us” tile, but most people need one of three things: directions or a known-item search, help with Library equipment or campus printing, or a referral for an in-depth research question. Please help me improve the help section.
>
> Available pathways are the Geisel Library Front Desk, WongAvery Front Desk, Library main telephone line, Contact Us form, and in-depth research consultations.

### Turn 1 — Skill

> I’m the UX Writing Coach. I can help you plan, draft, revise, or evaluate Library UX copy.
>
> <!-- uxwc-test-log
> scenario: contact and support section
> input_type: context-only
> plan_stage: shown
> response_template: plan-only
> copy_size: short-form
> molecule: contact and support
> references_loaded:
> - content-scenarios.md: routed the task to contact details and structured service content guidance
> - working-plan.md: classified the input and applied the plan gate
> - response-templates.md: selected the plan-only response shape
> - content-strategy-elements.md: identified the contact-and-support composition
> - voice-and-messaging.md: applied UC San Diego and Library voice principles
> next_step: confirm plan or draft
> -->
>
> **Goal:** Help people identify the best Library pathway for directions, known-item help, equipment or printing support, or an in-depth research referral.
>
> **Audience:** Students, faculty, staff, researchers, visitors, and community members, including people using the Library for the first time.
>
> **Top jobs:**
> - Find the right service point for directions or a known-item search.
> - Get help with Library equipment or campus printing.
> - Start an in-depth research consultation or referral.
> - Understand what each contact method does and when to use it.
>
> **Approach:** Replace the generic tile with task-specific help entries using the [Library UX: Contact and Support](https://ucsdlibrary.atlassian.net/wiki/x/AoC_0) pattern: a task-focused heading, a short “when to use this” lead, the best pathway, and the key location, phone, form, booking, or response detail. Group or sequence pathways so the most common tasks are immediately visible rather than asking people to infer the right “Contact Us” option.
>
> **To confirm:** Exact labels and links for the five pathways, desk locations and hours, the main phone number, whether the form accepts these task types directly, and how consultation referrals are submitted or scheduled.
>
> 1. Should each pathway include its location, hours, response expectation, or booking link?
> 2. Should research consultations be presented as self-service scheduling, a referral through the form, or both?
>
> Reply with changes, or say “Go ahead” to draft.

### Turn 2 — User

> Use a task-specific contact and support structure. Lead with when to use each pathway and give the pathway name, but do not include hours or links because I have not verified them.

### Turn 2 — Skill

> Using the confirmed structure, here’s a draft:
>
> **Get help at the Library**
>
> **Find a space or item**
> Use a front desk if you need directions, help finding a book or other known item, or a quick question about where to start.
>
> **Pathway:** Geisel Library Front Desk or WongAvery Library Front Desk
>
> **Get equipment or printing help**
> Use a front desk if you need help with Library equipment or campus printing.
>
> **Pathway:** Geisel Library Front Desk or WongAvery Library Front Desk
>
> **Ask an in-depth research question**
> Use a research consultation for a project, topic, or source strategy that needs more time or subject guidance.
>
> **Pathway:** In-depth research consultations
>
> **Contact us about something else**
> Use the Library main telephone line or Contact Us form for another question, follow-up, or request.
>
> **Pathways:** Library main telephone line and Contact Us form
>
> **Why this structure:** The headings name the user’s task first, each entry says when to use the pathway, and the unverified hours and links are omitted. The last entry preserves a recovery path for people whose question does not fit the three primary tasks.
>
> Next step: Confirm the desk assignments for equipment and printing help, then route the copy for service-owner review before adding links or hours.

### Turn 3 — User

> Would a single “Ask the Library” heading work better than three separate task headings?

### Turn 3 — Skill

> Yes, but use it as the section heading, not as a replacement for the task labels.
>
> **Recommended:** Keep **“Ask the Library”** as the section heading, then use the three task headings inside it. This gives people one clear destination while preserving the fastest route to the right pathway.
>
> **More compact alternative:** Use **“Ask the Library”** as the only heading and open with a short lead such as “Choose the task that fits your question.” This works if space is limited, but it adds more reading work before someone can match their need to a pathway.
>
> I would keep the task headings because they help people scan for directions, equipment, printing, and research help without guessing. They also make the distinctions between front desks and consultations clearer.
>
> Next step: Confirm the section placement and available layout, then decide whether the three entries should be cards, accordions, or short list groups.

**A5 result:** Pass. The skill showed a complete plan, asked two useful questions, then drafted task-specific pathways after the user supplied the structure and constraints.

## A6 — Technology Lending Boundary

### Turn 1 — User

> UXWC_TEST_MODE=1
> Please review this proposed message for the Technology Lending Program page:
>
> “Need a charger, adapter, headphones, or calculator? Community borrowers and UC San Diego students, faculty, and staff can check out technology from the Library. Visit the front desk to borrow items.”
>
> Our service definition says TLP circulates technology items to current UC San Diego faculty, staff, and students. Limited media playback access is available to all other affiliations. Inventory includes chargers, adapters, headphones, portable DVD players, and calculators, but not computers or consumables.

### Turn 1 — Skill

> <!-- uxwc-test-log
> scenario: policy, access, eligibility, or restrictions
> input_type: mixed
> plan_stage: skipped
> response_template: feedback-evaluation
> copy_size: short-form
> molecule: eligibility and access
> references_loaded:
> - content-scenarios.md: routed the request to eligibility/access guidance
> - working-plan.md: classified the rewrite object and service definition
> - response-templates.md: selected the feedback or evaluation format
> - content-strategy-elements.md: applied the eligibility and access molecule
> - library-terminology.md: checked service desk and campus naming
> - ux-writing-principles.md: applied action-first structure and material limits
> - voice-and-messaging.md: applied clear, respectful eligibility voice
> next_step: service-owner verification
> -->
>
> **What works**
> - The message leads with user needs and gives concrete examples.
> - The action is simple: visit a service desk to borrow items.
>
> **Top opportunities**
> - “Community borrowers” overstates eligibility. The service definition says current UC San Diego faculty, staff, and students can check out technology, while other affiliations have limited media playback access.
> - Add “current” to the UC San Diego audience and clarify whether limited media playback access means borrowing or another form of use.
> - “Front desk” needs a specific desk name or location. The item list also omits portable DVD players, so “including” may better signal that the list is not exhaustive.
>
> **Suggested revision**
> > Current UC San Diego faculty, staff, and students can check out technology from the Library, including chargers, adapters, headphones, portable DVD players, and calculators. Other affiliations have limited media playback access. The Library does not lend computers or consumables. Visit [exact desk name or location] to borrow items.
>
> A shorter alternative, if eligibility details appear elsewhere on the page:
> > Current UC San Diego faculty, staff, and students can borrow chargers, adapters, headphones, portable DVD players, and calculators. Other affiliations have limited media playback access. Visit [exact desk name or location] to get started.
>
> **Why**
> This keeps the allowed action first while preserving the service boundaries. I changed “community borrowers” to “other affiliations” to match the service definition, but that terminology change needs service-owner confirmation.
>
> **Next step**
> Confirm the desk location, whether “other affiliations” can borrow media playback equipment, and whether the computers or consumables exclusion belongs in this message. Then route the copy for human review.

### Turn 2 — User

> I do not want to exclude people unnecessarily, but I also do not want the message to promise laptop borrowing. Please create two accurate versions: one short alert-style message and one service-offering card.

### Turn 2 — Skill

> Here are two accurate versions:
>
> **Alert-style message**
> > Technology lending is available to current UC San Diego faculty, staff, and students. Other affiliations may have limited access to media playback equipment. Computers are not available for checkout. Visit [exact desk name or location] for details.
>
> **Service-offering card**
> > **Borrow technology**
> > Current UC San Diego faculty, staff, and students can check out items such as chargers, adapters, headphones, portable DVD players, and calculators. Other affiliations may have limited access to media playback equipment. Computers and consumable supplies are not included.
> >
> > **Action:** Visit [exact desk name or location] to borrow items.
>
> Both versions avoid implying laptop borrowing by stating the computer boundary directly. “Other affiliations” preserves the service definition, but you could name “community borrowers” only if the service owner confirms that limited media playback access applies to that specific group.
>
> Next step: confirm the exact desk name and whether “media playback access” means checkout, in-library use, or another borrowing arrangement.

### Turn 3 — User

> Can the skill tell me what would need to be checked before publishing either one?

### Turn 3 — Skill

> Yes. Before publishing either version, check:
>
> **Accuracy and eligibility**
> - Replace `[exact desk name or location]` with the approved desk or service point name.
> - Confirm whether “other affiliations” should be named as “community borrowers” or another recognized affiliation.
> - Confirm whether limited media playback access means checkout, in-library use only, or a different arrangement.
> - Verify the item list is accurate and clearly non-exhaustive.
> - Confirm the computers and consumable supplies exclusions match current TLP policy.
> - Verify the Technology Lending Program name and any related borrowing policies.
>
> **Page and journey fit**
> - Ensure the alert and card do not compete with each other; use one as a short status or reminder and the other as the offering summary.
> - Confirm the CTA takes users to the correct desk information, borrowing policy, or service page.
> - Check whether users need hours, availability, checkout periods, or eligibility requirements before going to the desk.
> - If the alert is time-limited, confirm how and when it will be removed or updated.
>
> **Accessibility and plain language**
> - Use specific link text, not generic “click here” or “learn more.”
> - Ensure headings, list structure, and alert markup follow the page’s accessibility patterns.
> - Confirm the copy can be understood without relying on color, icons, or surrounding page context.
> - Check reading order, focus behavior, and screen-reader presentation if the alert uses an interactive or dismissible component.
>
> **Voice and style**
> - Use “UC San Diego” rather than “UCSD.”
> - Use sentence case for headings and buttons.
> - Check punctuation, capitalization, and parallel structure.
> - Confirm the tone is clear, respectful, and not alarmist, especially for the alert-style version.
>
> **Review and approval**
> - Route to the TLP service owner for policy verification.
> - Route to a Library web or content editor for voice, style, and placement review.
> - Route to an accessibility reviewer if the alert uses new markup or interactive behavior.
> - Do not publish until the placeholders are resolved and the service owner confirms the eligibility and media playback language.
>
> Next step: send both versions to the TLP service owner with these verification questions, then follow Library content review workflow.

**A6 result:** Partial. The skill preserved the material eligibility boundary and provided excellent publication checks, but it skipped the working plan in Turn 1 and omitted the visible first-response introduction.

## A7 — Borrow Source Material and Working Plan

### Turn 1 — User

> UXWC_TEST_MODE=1
> Our borrowing service definition says: “The Borrow and Use Physical Collections service provides access to the UC San Diego Library’s onsite print and media collections for in-person use and loan, supporting users in requesting, obtaining, and using materials from the Library’s general and select mediated collections. Through a mix of self-service options and staff support, users can locate items in the stacks, request retrieval from non-public or offsite locations, borrow eligible items for offsite use, and use non-circulating materials in Library spaces, with clear expectations and consistent processes that make access predictable, equitable, and transparent.”
>
> Please help us improve the borrowing page.

### Turn 1 — Skill

> I’m the UX Writing Coach. I can help you plan, draft, revise, or evaluate Library UX copy.
>
> <!-- uxwc-test-log
> scenario: General service page or long-form help
> input_type: source material
> plan_stage: shown
> response_template: plan-only
> copy_size: long-form
> molecule: service overview
> references_loaded:
> - content-scenarios.md: Routed the service-page request and required references.
> - working-plan.md: Applied the Plan Gate because the supplied material is a service definition.
> - content-strategy-elements.md: Chose a service overview and offering-card structure.
> - ux-writing-principles.md: Applied task-first structure and scanning guidance.
> - library-style.md: Applied source hierarchy and uncertainty rules.
> - voice-and-messaging.md: Applied Library service-page tone and action-first messaging.
> - library-terminology.md: Identified terminology to verify for borrowing and service points.
> - style-mechanics.md: Applied naming, sentence case, and link-text conventions.
> next_step: draft after confirmation
> -->
>
> Assumption: I’m treating the service definition as source material. The current borrowing-page copy or URL is not included, so the first draft should be based on this definition and confirmed against the live page.
>
> **Goal:** Help users quickly decide how to find, request, borrow, or use physical print and media materials, then take the right next step.
>
> **Audience:** UC San Diego affiliates and other people eligible to use or borrow physical collections, including first-time users who may not know Library locations, request workflows, or circulation rules.
>
> **Top jobs:** Locate materials in the stacks; request items from non-public or offsite locations; determine what can be borrowed and how; use non-circulating materials in Library spaces; get help when a request or access question is unclear.
>
> **Approach:** Use a service-overview page with a short task-first lead, then offering cards for the main pathways. Add an eligibility and access section, a compact how-to path for requesting or retrieving items, and a task-specific help path. This keeps self-service and staff-supported options scannable without exposing internal workflows.
>
> **To confirm:** Approved public page title and current page content; eligibility for borrowing and onsite use; exact collection and service-point names; request system names, links, and turnaround expectations; pickup locations and hours; checkout periods, limits, renewals, and exceptions; definitions and locations for non-circulating materials; and the most specific help path.
>
> Reply with changes, or say “Go ahead” to draft.

### Turn 2 — User

> Use three service-offering cards for borrowing eligible materials, requesting items for pickup, and using materials in the Library. For each card, give a title, summary, and primary call to action.

### Turn 2 — Skill

> Here’s a first draft:
>
> - **Borrow eligible materials**  
>   Check out eligible print and media materials from the UC San Diego Library for offsite use. Some materials are Library use only.  
>   **Primary call to action:** See borrowing options
>
> - **Request items for pickup**  
>   Request materials from non-public or offsite Library locations and pick them up when they’re ready.  
>   **Primary call to action:** Place a request
>
> - **Use materials in the Library**  
>   Use non-circulating materials in Library spaces. You can’t check these items out.  
>   **Primary call to action:** Find materials to use in the Library
>
> Next step: Confirm the link target for each call to action and verify the borrowing eligibility and pickup language with the service owner.

### Turn 3 — User

> Can you review the cards for someone who has never used UC San Diego Library before? Our definitions say onsite collections are open to all visitors, but borrowing for offsite use is limited to University affiliates and registered Community Borrowers. Some items are Library use only.

### Turn 3 — Skill

> Hypothesis: A first-time visitor may not know whether they can borrow, what a registered community borrower is, or what “non-circulating” means.
>
> **What works**
> - The three titles separate the main tasks clearly.
>
> **Top opportunities**
> - State borrowing eligibility directly instead of relying on “eligible materials.”
> - Use plain language for “non-circulating.”
> - Make the difference between onsite access and borrowing eligibility easier to scan.
>
> **Suggested revisions**
> - **Borrow materials for offsite use**  
>   University affiliates and registered community borrowers can check out eligible print and media materials to use away from the Library. Some items are Library use only.  
>   **Primary call to action:** See borrowing options
> - **Request items for pickup**  
>   Request materials from non-public or offsite Library locations and pick them up when they’re ready.  
>   **Primary call to action:** Place a request
> - **Use materials in the Library**  
>   All visitors can use onsite print and media collections in Library spaces.  
>   **Primary call to action:** Find onsite materials
>
> **Why**
> These revisions lead with who can act, explain access limits plainly, and keep the three pathways distinct.
>
> Next step: Confirm the preferred public terms for “University affiliates” and “registered community borrower,” and verify each CTA link target.

**A7 result:** Pass. The skill classified the service definition as source material, used the plan-only template, avoided sentence-level paraphrasing, and translated eligibility into user-facing tasks in the review turn.
