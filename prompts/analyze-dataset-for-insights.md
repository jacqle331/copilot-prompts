# Analyze a Dataset for Insights

**Category:** Research & Analysis
**Tags:** data-analysis, insights, trends, metrics

## What it does

Takes a set of data — numbers, a table, or a pasted spreadsheet — and pulls out the trends, outliers, and takeaways that matter, in plain language.

## Prompt

```text
You are a sharp, plain-spoken data analyst. Analyze the data below.

Produce:
1. **Top takeaways** — the 3-5 most important things this data tells us.
2. **Notable trends** — what's going up, down, or holding steady, with the numbers.
3. **Outliers & surprises** — anything unusual worth a closer look.
4. **Possible explanations** — likely reasons behind the patterns (clearly marked
   as hypotheses, not facts).
5. **Recommended next questions** — what to investigate or what data would sharpen
   the analysis.

Rules:
- Use specific numbers from the data to back up every point.
- Distinguish what the data shows from what you're inferring.
- If the data is incomplete or ambiguous, say so instead of guessing.

What this data is about: {{brief context — what it measures, time period, source}}
The data: {{paste your table, numbers, or spreadsheet rows here}}
What I'm trying to learn: {{the question or decision behind the analysis}}
```

## Example

**Input:** A few months of pipeline or engagement numbers pasted as a table.

**Output:** Plain-language takeaways, quantified trends, flagged outliers, hypotheses, and the next questions to dig into.

## Tips

- Include column headers and a time period so the model reads the data correctly.
- State the decision you're trying to make — it focuses the analysis on what matters.
