# /pre-session

A read-only briefing before a therapy session, ceremony, retreat, coaching call, or 1:1 with a teacher. Surfaces what's been building, what's unresolved, and what question is most alive — so you arrive present rather than scrambling to remember where you left off.

---

## Input

A name, role, or context:
- `/pre-session` — generic briefing from current active patterns
- `/pre-session [therapist name]` — briefing scoped to that relationship + relevant patterns
- `/pre-session ceremony` — what's been building across all modalities recently
- `/pre-session retreat` — longer arc summary

---

## What it does (read-only — writes nothing)

1. **Load the relationship file** if a name was given: `context-library/relationships/<name>.md`. Pull last interaction date, open threads, emotional valence, what tends to come up with this person.

2. **Load active patterns**: `context-library/patterns/INDEX.md` → any pattern with status `active` or `emerging`. Note which ones have new evidence in the past 2 weeks.

3. **Scan recent entries** (last 7-14 days across journals/, dreams/, meditations/) for the most charged or recurring material.

4. **Cross-reference** open observations in patterns that haven't moved in a while — unresolved threads the session might touch.

---

## Surfaces

- **Who you're meeting** (if named): relationship state, last touched, what they tend to hold or push on.
- **What's been building**: the 1-2 most activated threads in the past two weeks, with entry citations.
- **Active patterns in play**: which ones are most relevant to this session.
- **What question is most alive right now**: one open question drawn from the material, not invented.
- **A gap notice** if the relationship file is thin or the brain has little recent material ("only one touchpoint logged — this briefing is light").

---

## After the session

Run `/journal`, `/dream`, or `/capture` to bring in what arose. The next `/pre-session` will be richer for it.
