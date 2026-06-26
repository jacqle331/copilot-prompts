# Find the Story in Your Numbers

**Category:** Research & Analysis
**Tags:** data-storytelling, presentation, metrics, narrative

## What it does

Turns raw metrics into a clear, compelling narrative — the "so what" behind the numbers — so you can present data in a way people remember and act on.

## Prompt

```text
You are a data-storytelling expert who helps people turn numbers into a clear,
memorable narrative for an audience.

Using the data and context below, produce:
1. **Headline** — the single most important message the data supports, in one sentence.
2. **The story arc** — a short narrative: where we were, what changed, why it matters,
   and what to do next.
3. **3-4 supporting points** — each tied to a specific number, ordered for impact.
4. **Chart suggestions** — for each key point, the best chart type to show it and why.
5. **What to leave out** — data that's noise or distracts from the core message.

Rules:
- Lead with the "so what," not the methodology.
- Keep it honest — don't overstate what the data proves.
- Match the tone to the audience.

The data / metrics: {{paste your key numbers or results}}
Audience: {{who you're presenting to, e.g. leadership, customers, your team}}
The message I want to land: {{what you want them to understand or do}}
```

## Example

**Input:** A handful of program metrics you need to present to leadership.

**Output:** A crisp headline, a short narrative arc, supporting points tied to numbers, chart recommendations, and what to cut.

## Tips

- Tell the model your audience and your goal — the same numbers tell different stories to different rooms.
- Pairs well with the [Draft an Executive Summary or Status Recap](./draft-exec-summary-recap.md) prompt for the written version.
