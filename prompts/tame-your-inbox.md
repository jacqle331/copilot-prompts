# Tame Your Inbox

**Category:** Productivity
**Tags:** email, triage, inbox, prioritization

## What it does

Takes a pile of emails and sorts them into what needs a reply now, what can be delegated, and what can wait or be archived — with draft replies for the urgent ones.

## Prompt

```text
You are a sharp executive assistant. Help me get through my inbox fast.

For the emails below, produce:
1. **Reply now** — emails that need my response today, each with a suggested
   one-line reply or a short draft.
2. **Delegate / forward** — emails better handled by someone else, with a note on
   who and a quick handoff message.
3. **Can wait** — non-urgent items, with a suggested follow-up date.
4. **Archive / no action** — FYI or noise I can clear.

Rules:
- Judge urgency by deadlines, sender, and the ask — not by length.
- Keep draft replies concise and in a warm, professional tone.
- Flag anything ambiguous instead of guessing the right action.

My emails: {{paste subjects and content, or a summary of each}}
My role / context: {{so you can judge what's important to me}}
```

## Example

**Input:** A dump of 8 emails of mixed urgency.

**Output:** Each email sorted into reply-now (with drafts), delegate, wait, or archive — so you can clear the inbox in minutes.

## Tips

- Paste the full text where you can — the drafts get much better with the real content.
- Tell it your role so it knows what's genuinely important versus noise.
