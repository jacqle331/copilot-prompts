# Run a Better Meeting

**Category:** Productivity
**Tags:** meetings, agenda, facilitation, time-management

## What it does

Builds a tight, purposeful meeting agenda with clear objectives, timeboxes, and desired outcomes — so your meetings are shorter and actually productive.

## Prompt

```text
You are a crisp meeting facilitator who hates wasted time.

Design an agenda for the meeting below. Produce:
1. **Meeting objective** — the one thing this meeting must accomplish, in a sentence.
2. **Desired outcomes** — what should be true when we leave (decisions, alignment, etc.).
3. **Agenda** — a timeboxed list of topics, each with a purpose (decide / discuss /
   inform) and minutes allocated.
4. **Pre-work** — anything attendees should review or prepare beforehand.
5. **Roles** — who facilitates, who takes notes, who owns follow-ups.
6. **A strong closing** — how to end with clear next steps and owners.

Rules:
- Keep it lean — if a topic doesn't serve the objective, cut it or flag it.
- If the meeting could be an email, say so.

Meeting purpose: {{why you're meeting}}
Attendees: {{who's coming and their roles}}
Time available: {{total minutes}}
Must-cover topics: {{anything that has to be addressed}}
```

## Example

**Input:** A 30-minute cross-team sync that's been running long and unfocused.

**Output:** A clear objective, desired outcomes, a timeboxed agenda, pre-work, roles, and a strong close.

## Tips

- Mark each topic as decide / discuss / inform — it keeps the meeting from drifting.
- If the agenda doesn't fit the time, the model will tell you what to cut.
