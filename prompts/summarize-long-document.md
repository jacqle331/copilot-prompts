# Summarize a Long Document or Report

**Category:** Research & Analysis
**Tags:** summarization, reading, reports, takeaways

## What it does

Distills a long document, report, or article into the key points, takeaways, and action items — so you get the gist in a fraction of the time.

## Prompt

```text
You are a sharp analyst who summarizes dense material clearly.

Summarize the document below. Produce:
1. **TL;DR** — a 2-3 sentence summary of the whole thing.
2. **Key points** — the main ideas as a bulleted list.
3. **Important details** — facts, numbers, or findings worth remembering.
4. **Implications / action items** — what this means or what to do about it.
5. **Open questions** — anything unclear or that warrants follow-up.

Rules:
- Stay faithful to the source — don't add claims that aren't in the document.
- Keep it concise; lead with what matters most.
- If the document is long, tell me if any section deserves a deeper read.

What this document is: {{type, source, and why you're reading it}}
The content: {{paste the document, report, or article text}}
What I most need from it: {{your purpose — a decision, a briefing, etc.}}
```

## Example

**Input:** A 15-page program report you need to brief leadership on.

**Output:** A TL;DR, key points, important details, implications/actions, and open questions.

## Tips

- Tell it your purpose — a summary for a decision differs from one for general awareness.
- For very long docs, paste in sections and ask it to combine the summaries at the end.
