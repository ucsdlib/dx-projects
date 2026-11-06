# Human Testing Plan: UX Writing Coach

## Purpose

Human testing complements automated evaluation by asking Library staff to use the skill on real writing tasks. It measures whether the coaching is usable, trustworthy, and persuasive to people who will publish or maintain Library content.

## Roles

| Role | Responsibility |
| --- | --- |
| Facilitator | Runs the session, reads prompts, avoids coaching the participant |
| Participant | A Library staff member with actual or plausible content responsibility |
| Recorder | Captures transcript, comments, friction points, and time |
| Reviewer | Applies the evaluation rubric and proposes skill changes |

The facilitator may combine roles for a small first round. A UX or content expert should participate in at least one session.

## Participants

Test with at least six sessions across the following backgrounds:

- front desk or circulation staff;
- communications or web content staff;
- a subject librarian or research support staff member;
- a coordinator responsible for a program or prize;
- a UX/accessibility or content strategy reviewer;
- someone unfamiliar with the skill.

Do not reuse the same participant's completed scenario as training material for another participant.

## Session Structure

1. **Orientation, 2 minutes.** Explain that the skill provides coaching material and not approved copy.
2. **Setup, 1 minute.** Confirm the participant has never seen the scenario.
3. **Task, 10–15 minutes.** Run two to three interactions using the reusable scenario.
4. **Debrief, 5 minutes.** Ask what was helpful, confusing, wrong, missing, or unsafe.
5. **Rating.** Capture the participant's assessment before the facilitator's evaluation.

## Interview Questions

Ask after the interaction:

- What did the skill assume that was accurate or inaccurate?
- What output would you use or adapt first?
- What made the output easy or difficult to trust?
- Did any suggestion obscure a limit, policy, audience difference, or accessibility concern?
- What next step would you take in real work?
- What should the skill do differently next time?

## Ratings

Use a 1–5 scale where 5 is best. Record one sentence of evidence for every score.

| Dimension | Question |
| --- | --- |
| Activation | Did the skill handle the request without extra setup? |
| Intake | Did it understand the writing situation without unnecessary questions? |
| Content quality | Was the copy useful, accurate, and audience-centered? |
| Voice and style | Did it sound like UC San Diego Library rather than generic AI? |
| Trust | Were verification limits, uncertainty, and next steps clear? |
| Efficiency | Did it save time compared with starting from scratch? |
| Follow-up | Did it improve usefully on the second or third turn? |

## Human Test Matrix

| Scenario | Realistic user role | Primary focus |
| --- | --- | --- |
| A1 | Web content editor | Turning a service definition into an overview |
| A2 | Circulation/access staff | Creating or refining offering cards |
| A3 | Technology support staff | Drafting a calm outage message |
| A4 | Prize coordinator | Evaluating audience fit and missing facts |
| A5 | Front desk lead | Making a specific help path |
| A6 | Access services or technology staff | Balancing action, accuracy, and skill boundaries |

## Human-Only Signals

Watch for automated tests that may miss:

- copy that is technically correct but emotionally cold;
- public-facing language that a front desk worker would not use;
- suggestions that add work for the user or staff;
- assumptions that erase community borrowers, visitors, international users, or users with disabilities;
- over-formal or over-enthusiastic output;
- excessive caveats that reduce usability;
- confidence in facts the participant knows are not maintained.

## Reporting

For each session, record:

- participant background;
- scenario ID;
- full transcript;
- time to first useful response;
- participant's initial reaction;
- debrief notes;
- ratings;
- confirmed inaccuracies;
- recommended skill change;
- whether the scenario card itself needs revision.

Use `testing/reports/report-template.md` so automated and human findings use the same transcript and evaluation structure.

After the round, synthesize findings by severity: blocker, high impact, moderate, and minor. Group recurring findings before editing the skill.

## Success Criteria

The first human round is successful when:

- participants can get a usable draft or revision within two turns;
- participants can identify what still needs verification;
- participants do not report a high-severity hallucination or boundary failure;
- participants generally rate content quality and trust at 4 or higher;
- recurring improvement ideas can be traced to specific skill rules.
