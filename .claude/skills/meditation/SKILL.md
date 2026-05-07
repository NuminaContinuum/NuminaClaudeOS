---
name: meditation
description: Log a meditation sit with structured prompts — technique, duration, quality/depth, phenomenological notes. Tracks patterns over time. The phenomenological detail also feeds v2 framework maps (Finding the Ox, 16 Insight Knowledges) which need rich meditation data to work accurately.
---

# /meditation — Sit log

Meditation logs are the most data-shaped content in the OS. They look like a form, but treat them as field notes — phenomenological, specific, and the user's own language.

The detail matters. The v2 maps (Finding the Ox, 16 Insight Knowledges) need real markers — dissolution, arising-and-passing, equanimity, jhāna factors — to place the user accurately on the map. Generic logs will produce generic maps.

---

## Behaviour

### Step 1 — Prompt the four fields

Ask for each, one at a time. Not all at once. Wait for the answer.

**1. Technique**
What did you sit with today? (Breath, noting, open awareness, metta, body scan, koan, self-inquiry, mantra, visualisation, other.)

If they give a tradition rather than a technique (e.g. "vipassana"), gently ask the specific technique within it ("noting? body scan? choiceless awareness?"). The technique is what feeds the maps, not the school name.

**2. Duration**
How long was the sit?

**3. Quality and depth**
How was the sit, in one or two sentences? You're after their qualitative read — concentrated? scattered? deep? dry? You can offer a few framings if they're stuck:
- *"Some people use a 1-10 scale, others use words like 'scattered, settling, concentrated, dropped'. Whatever fits."*

Don't insist on a number.

**4. Phenomenological notes**
This is the most important field. Ask: *"What arose, what dissolved, how did the mind move? Be specific — sensations, mental imagery, emotional weather, anything that stood out."*

If they give one line, accept it. If they give half a page, capture it.

**Capture phenomenological notes verbatim.** Do not paraphrase. Do not interpret. The raw language is the data.

### Step 2 — Read context

Read `context-library/profile.md` and skim recent meditation entries (`context-library/meditations/`). You need:

- Their tradition (informs how to surface patterns later)
- Recent technique rotation
- Recent depth trends (if obvious from prior logs)

### Step 3 — After 3+ sits, surface patterns

If three or more meditation entries exist, offer one brief pattern note after logging this sit. Two to three sentences max. Examples:

> *"Eight sits this month, six on breath, two on metta. The breath sits seem to settle faster — but the metta ones seem to leave you more open afterwards. Worth noticing."*

> *"Depth has been steady around 'settling' for the past two weeks. Last big drop was the [date] sit with noting — first time you logged 'dropped'. No need to chase that, just naming it."*

Do not surface patterns if there are fewer than 3 sits, or if the patterns are not real.

### Step 4 — Store the sit

Create the file. Naming convention: `YYYY-MM-DD-[technique].md`. If they did multiple sits in one day, append a sequence: `YYYY-MM-DD-[technique]-2.md`.

**Path:** `context-library/meditations/YYYY-MM-DD-[technique].md`

```markdown
# [Date] — [Technique] sit

**Date:** YYYY-MM-DD
**Type:** meditation
**Technique:** [Specific technique]
**Tradition:** [If user named one — Theravada, Zen, Tibetan, etc.]
**Duration:** [Minutes]
**Depth:** [Their qualitative read]

## Phenomenological notes
[Their text, verbatim]

## Patterns surfaced (only if 3+ sits exist)
[The brief pattern note from Step 3]

## Notable for timeline
[Yes / No, with one-line description if yes]
```

### Step 5 — Auto-update the memory layer

Per the rules in `CLAUDE.md`:

- For meditation, relationship and archetype updates are rarer than in other skills. But: if the user describes a teacher, lineage figure, or inner figure that arose during the sit (e.g. *"my old teacher's voice came through"*, *"the Buddha appeared as a feeling-tone"*), create or append the relevant relationship/archetype file. Mark these as inner figures, not waking-life people.
- Notable timeline entries from meditation are usually first experiences of specific phenomena — first taste of something the tradition has a name for (jhāna factor, knowledge, kensho-like opening), or first sustained experience of a quality (equanimity, no-self, dissolution). Be conservative — most sits do not warrant timeline entries.

---

## Acceptance criteria

- [ ] Prompts for technique, duration, quality/depth, and phenomenological notes (one at a time)
- [ ] Captures phenomenological notes verbatim — no paraphrase, no interpretation imposed
- [ ] If 3+ sits exist, surfaces one brief pattern note after logging
- [ ] Stores sit at `context-library/meditations/YYYY-MM-DD-[technique].md`
- [ ] Auto-updates memory layer when teachers, lineage figures, or inner figures arise
- [ ] Does not diagnose or label experiences clinically
- [ ] Tone: clinical clarity is welcome here, but with warmth — this is field notes, not a chart

---

## Tone reminders

- This skill is more structured than the others. That's fine — meditation logs benefit from form.
- Do not romanticise a "deep" sit or apologise for a "scattered" one. Both are data.
- If the user describes a striking experience (e.g. *"everything dissolved for a moment"*), do not interpret it on the spot. Capture it, log it, and let `/maps` or `/compass` synthesise across many sits later.
- Resist the urge to congratulate consistency. Ten sits a week is not better than two if the two land. The user knows this.
