# Summarize Meeting Notes

**Category:** Productivity
**Tags:** meetings, summary, action-items

## What it does

Turns raw meeting notes or a transcript into a clean summary with key decisions and clear action items.

## Prompt

```text
You are an executive assistant. Summarize the meeting notes below.

Produce:
1. A 2-3 sentence summary of the meeting.
2. Key decisions made (bullet list).
3. Action items as a table with columns: Owner, Task, Due date.

Keep it concise and only include information present in the notes.

Meeting notes:
{{paste your notes or transcript here}}
```

## Example

**Input:** A transcript of a 30-minute project sync.

**Output:** A short paragraph summary, a bulleted list of decisions, and an action-item table assigning tasks to named owners.

## Tips

- If owners or due dates aren't stated, ask the model to mark them as "TBD" rather than guessing.
