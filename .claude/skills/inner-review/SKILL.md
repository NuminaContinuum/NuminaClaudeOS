---
name: inner-review
description: Weekly reflection. Reads entries from the past 7 days across journals, dreams, journeys, and meditations. Surfaces 2-3 recurring themes, identifies open threads (things that came up but didn't resolve), and offers one invitation for the week ahead. Appends a summary to the timeline.
---

# /inner-review — Weekly inner review

A small ritual at the end of the week. Not a productivity review. A noticing.

The user has been logging across multiple skills all week. `/inner-review` zooms out and says: here's what was alive, here's what's still open, here's one thread to carry into next week.

---

## Behaviour

### Step 1 — Read context

Before reflecting:

1. Read `context-library/profile.md` for framework lens and language.
2. Read all entries with dates from the past 7 days across:
   - `context-library/journals/`
   - `context-library/dreams/`
   - `context-library/journeys/`
   - `context-library/meditations/`
3. Note any timeline entries from `context-library/maps/timeline.md` in the same window.

If fewer than 7 days of entries exist, work with whatever's there. Don't pretend it's a full week.

### Step 2 — Reflect

The output is short — three to five paragraphs total. Structured as:

#### Recurring themes (2-3, not more)

What appeared across multiple entries this week. Cross-content matters most — a theme that shows up in both a journal and a dream is more interesting than one that appears in three journals.

Quote specifically. *"On Monday you wrote 'I feel like I'm performing my own life' — Wednesday's dream had you on a stage you couldn't leave."*

If only 2 themes are real, only name 2. Don't pad.

#### Open threads

Things that came up but weren't resolved. A question you asked yourself and didn't answer. A feeling that arrived and then was left. A symbol that appeared once and didn't reappear.

These matter because they're often where the next week's work wants to begin.

Format as 1-3 specific items. Each one with a quote or specific reference.

> *"Open threads:*
> - *The conversation with your sister you didn't have. You wrote about wanting to call her on Tuesday — no entry since.*
> - *The dream of the open door. You named it as 'an invitation' but didn't write what it was inviting.*"

#### One invitation for the week ahead

A single, specific, gentle invitation. Not advice. Not a goal. An invitation.

Examples:
- *"This week — what would it be like to actually call your sister, or to write her the letter you wouldn't send?"*
- *"The 'performing' theme is asking for ground. One sit this week with no agenda — not even the noting technique. Just sitting."*
- *"You logged five journal entries and zero dreams this week. Worth keeping a notepad by the bed?"*

Use the user's framework language. Hold it as invitation, not prescription.

### Step 3 — Save the reflection

Write it as a file:

**Path:** `outputs/reflections/YYYY-MM-DD-inner-review.md`

```markdown
# Inner review — week ending YYYY-MM-DD

**Date:** YYYY-MM-DD
**Type:** inner-review
**Window:** [Start date] to [End date]

## Entries reviewed
- N journals
- N dreams
- N journeys
- N meditations

## Recurring themes
[The themes from Step 2]

## Open threads
[The open threads from Step 2]

## Invitation
[The single invitation from Step 2]
```

### Step 4 — Append to timeline

Add one line to `context-library/maps/timeline.md`:

```
YYYY-MM-DD | insight | Weekly review — [one-phrase summary of the dominant theme] | outputs/reflections/YYYY-MM-DD-inner-review.md
```

Use type `insight` for review summaries unless something more specific fits.

### Step 5 — Output to user

Present the reflection in chat (same content as the saved file). End with:

> *"Saved to `outputs/reflections/YYYY-MM-DD-inner-review.md`. Sit with the invitation if it lands."*

---

## Edge cases

**Fewer than 3 entries in the past 7 days:**
> *"Quiet week — only 2 entries since [date]. Worth taking the invitation as: this week, what would help you write more often, or what's keeping you from it?"*

**No entries at all:**
> *"Nothing logged this week. The review needs material to work with — maybe start with `/journal` and try again next week."*

**Heavy week (15+ entries, or a difficult journey):**
The themes section can stretch to 3 (not more). The invitation should slow things down rather than add more — *"Your week was full. The invitation is for some empty time."*

---

## Acceptance criteria

- [ ] Reads `profile.md` for framework context
- [ ] Reads all entries in the past 7 days across journals, dreams, journeys, meditations
- [ ] Surfaces 2-3 recurring themes (cross-content preferred)
- [ ] Identifies 1-3 open threads with specific quotes/references
- [ ] Offers exactly one invitation for the week ahead, framework-aware
- [ ] Saves the reflection to `outputs/reflections/YYYY-MM-DD-inner-review.md`
- [ ] Appends a summary line to `context-library/maps/timeline.md`
- [ ] Handles short windows gracefully (fewer than 7 days of data)
- [ ] Tone: noticing, not assessing — ritual, not report

---

## Tone reminders

- This is the end of a week. The user is tired. Write as if they'll read it tomorrow with coffee, not as a deliverable they have to act on.
- Quote their own words back — that's the medicine.
- If the week was hard, name it. If it was full of light, name that too. Don't average.
- Resist the urge to wrap things up. The invitation should leave a door open, not close one.
