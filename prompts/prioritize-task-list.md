# Prioritize Your Task List

**Category:** Productivity
**Tags:** prioritization, planning, time-management, focus

## What it does

Takes a messy list of to-dos and ranks them by importance and urgency, factoring in effort and deadlines, so you know exactly what to do first.

## Prompt

```text
You are a sharp productivity coach. Help me prioritize the task list below.

For each task, estimate importance and urgency, then produce:
1. A **prioritized table** with columns: Task, Importance (High/Med/Low),
   Effort (Quick/Medium/Heavy), Due date, Priority rank.
2. A **"Do first" shortlist** — the top 3-5 tasks I should tackle now, in order.
3. **Quick wins** — low-effort, high-value items I can knock out fast.
4. **Can wait / delegate** — anything low-priority or better handled by someone else.
5. A one-line rationale for how you ranked things.

Rules:
- Weigh both importance and time sensitivity; flag anything with a near deadline.
- If a task is vague or missing a due date, note it rather than guessing.

My tasks: {{paste your to-do list, with any deadlines or context}}
Time I have available: {{e.g. a focused afternoon, a full day, this week}}
What matters most right now: {{your current goals or biggest priorities}}
```

## Example

**Input:** A jumble of 10 to-dos, some with deadlines, some without.

**Output:** A ranked table, a "do first" shortlist, quick wins to clear fast, items to defer or delegate, and the reasoning behind the order.

## Tips

- Add deadlines and rough effort estimates to your input — the ranking gets much sharper.
- Re-run it at the start of a busy day to reset your focus in two minutes.
