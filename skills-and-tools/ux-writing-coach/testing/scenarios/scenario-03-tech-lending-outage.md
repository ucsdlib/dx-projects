# Scenario A3: Technology Lending Outage Message

## Focus

Test feedback and drafting for microcopy using a status, alert, or help message.

## Exact User Turns

### Turn 1

```text
We need an outage message for the Technology Lending Program. Current draft: “Attention users: The Tech Lending Program is experiencing a system malfunction which has rendered the check-out process inoperable. We apologize for any inconvenience this may cause. Users are advised to await further communication.”

It can be up to three sentences.
```

### Turn 2

```text
Please give me three options with one-line reasons. The item is unavailable right now, but staff can still help at the Geisel Library Front Desk. We do not yet know when lending will resume.
```

### Turn 3

```text
The final one must be under 180 characters and say users can ask staff for alternatives. Please revise the best option.
```

## Success Criteria

- May skip the working plan because this is short, well-specified microcopy.
- Logs the plan stage as `skipped` when test mode is enabled.
- Says what happened in plain language.
- Provides a next action and support path.
- Avoids jargon, blame, apology padding, and vague “check back later.”
- Offers three options in Turn 1 with one-line rationales.
- Preserves the facts that availability is unknown and staff can help.
- Does not invent an estimated restoration time or a specific checkout tool.
