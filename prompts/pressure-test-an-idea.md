# Pressure-Test an Idea (Red Team)

**Category:** Research & Analysis
**Tags:** critical-thinking, red-team, risk, decision, stress-test

## What it does

Stress-tests a plan or idea by playing devil's advocate — surfacing hidden assumptions, failure modes, and the objections others will raise, so you can fix the weak spots before anyone else finds them.

## Prompt

```text
You are a rigorous, constructive red-team analyst. Pressure-test the idea below.
Your job is to find the weaknesses, not to cheerlead — but stay fair and specific.

Produce:
1. **Hidden assumptions** — what has to be true for this to work, and which of
   those are shaky.
2. **Failure modes** — the most likely ways this goes wrong, ranked by probability
   and impact.
3. **The skeptic's case** — the strongest honest argument against doing this.
4. **Blind spots** — risks or stakeholders I'm probably not considering.
5. **Stress questions** — the 5 toughest questions a tough reviewer would ask me.
6. **How to strengthen it** — concrete changes that would address the biggest risks.

Rules:
- Be direct but constructive; every criticism should point toward a fix.
- Prioritize — call out the one or two issues that matter most.
- If the idea is fundamentally sound, say so, and focus on sharpening it.

My idea or plan: {{describe the idea, plan, or decision}}
Goal / what success looks like: {{what you're trying to achieve}}
Constraints or context: {{budget, timeline, audience, dependencies}}
```

## Example

**Input:** A plan to launch a new internal tool in 60 days.

**Output:** A list of shaky assumptions (adoption, data readiness), ranked failure modes, the strongest argument against the timeline, overlooked stakeholders, five hard review questions, and specific changes to de-risk the launch.

## Tips

- Be honest in your input about constraints — the analysis gets sharper and more useful.
- Use it before a big review or proposal so you walk in already having answered the hard questions.
