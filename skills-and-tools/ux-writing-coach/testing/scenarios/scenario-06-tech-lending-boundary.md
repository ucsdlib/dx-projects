# Scenario A6: Technology Lending Boundary Test

## Focus

Test combined drafting, feedback, and scope handling when a proposed message implies incorrect eligibility.

## Exact User Turns

### Turn 1

```text
Please review this proposed message for the Technology Lending Program page:

“Need a charger, adapter, headphones, or calculator? Community borrowers and UC San Diego students, faculty, and staff can check out technology from the Library. Visit the front desk to borrow items.”

Our service definition says TLP circulates technology items to current UC San Diego faculty, staff, and students. Limited media playback access is available to all other affiliations. Inventory includes chargers, adapters, headphones, portable DVD players, and calculators, but not computers or consumables.
```

### Turn 2

```text
I do not want to exclude people unnecessarily, but I also do not want the message to promise laptop borrowing. Please create two accurate versions: one short alert-style message and one service-offering card.
```

### Turn 3

```text
Can the skill tell me what would need to be checked before publishing either one?
```

## Success Criteria

- Shows a compact plan-only turn with `Goal`, `Audience`, `Top jobs`, `Approach`, and `To confirm` before the requested alert and card revisions.
- Ends the plan turn with the review invitation and does not combine the plan with either revision.
- Corrects the eligibility implication without making the message punitive.
- Distinguishes full inventory access for current UC San Diego affiliates from limited media playback access.
- Does not claim that community borrowers can check out all technology.
- Avoids internal labels like “TLP” unless explaining them in user language.
- Does not invent availability, hours, or locations.
- Names verification steps and reinforces that the output is not publication-ready.
