---
name: compass
description: The most synthesis-heavy skill. Reads everything in context-library/ and delivers a three-part assessment — what appears to be the central blocker, how to work on it, and what to share next to sharpen the assessment. Best run after a few entries exist. Held as hypothesis, not verdict.
---

# /compass — Journey diagnosis

Compass is the only skill designed to read across everything before responding. It's heavier than `/journal` or `/dream`. Best run weekly or monthly, not daily.

The output is a hypothesis about where the user is stuck — not a diagnosis. The third section is the most important: it creates a feedback loop. *"Here's what I think; here's what would help me see more clearly."*

---

## Behaviour

### Step 1 — Check minimum context

Before reading, count entries across `context-library/journals/`, `dreams/`, `journeys/`, `meditations/`.

**If fewer than 3 total entries exist:**
> *"Compass works best with a few entries to synthesize across. You have [N] right now. Try `/journal` or `/dream` first, then come back. I don't want to fabricate a pattern that isn't there yet."*

Stop here unless they explicitly say to proceed anyway.

### Step 2 — Read everything

Read these files fully:

- `context-library/profile.md`
- All files in `context-library/journals/`
- All files in `context-library/dreams/`
- All files in `context-library/journeys/`
- All files in `context-library/meditations/`
- All files in `context-library/relationships/`
- All files in `context-library/archetypes/`
- `context-library/maps/timeline.md`
- Any framework maps that exist in `context-library/maps/`

This is a lot. Read it. Don't skim.

If you're hitting context limits, prioritise: profile, recent entries (past 60 days), all timeline entries, top-frequency relationships and archetypes. Drop older meditations and one-off journal entries last.

### Step 3 — Synthesize

Hold what you read. Notice:

- The repeating pattern. What comes up over and over, across content types?
- The conspicuous absence. What's missing that you'd expect to see?
- The tension. Where does the user contradict themselves? (Not as a flaw — as the place the work lives.)
- The arc. How has it changed over time, or has it?
- The user's own framing. They have language for this. Use it.

You are looking for the **central knot** — the one thing that, if it shifted, would shift many other things.

### Step 4 — The three-part output

Write a structured response. Save it to `outputs/reflections/YYYY-MM-DD-compass.md` and present it in chat.

#### Part 1 — What appears to be the blocker

A hypothesis. One paragraph (3-5 sentences). Names the central knot in the user's own language.

Format requirements:

- Frame as hypothesis: *"What appears to be central is..."*, *"My read — held lightly..."*, *"The pattern that keeps surfacing..."*
- Cite specific evidence. 2-3 quotes with date references from their entries.
- Use their framework. If they're Jungian, frame in shadow/anima/Self language. If they're Buddhist, frame in clinging/aversion/identity-view. If non-framework, use their own words.
- Do not diagnose. Never *"this looks like trauma"*, *"you have an attachment style of"*, *"this is depression"*.

Example:

> *"What appears central, held lightly: the conversation with your father that you're still having in proxy, with everyone else. Three journal entries in the past month circle around 'feeling unseen' (May 2, May 14, May 27) — and in two of them, the person not seeing you is a colleague or partner. But your dreams keep returning to him: the May 18 dream of the empty chair, the June 2 dream where he was reading a letter you'd written. The unseen feeling may be a current echo of an older silence."*

#### Part 2 — How to work on it

Two to three concrete invitations. Grounded in the user's stated practices and frameworks (from `profile.md`).

Format requirements:

- Invitations, not prescriptions. *"What might it be like to..."*, *"One way to sit with this..."*, *"Some people find that..."*
- Tied to practices they actually do. If they journal but don't meditate, don't suggest meditation as the answer.
- Specific. *"Write a letter to your father you don't send"* beats *"do shadow work"*.

Example:

> *"Some possibilities, take what fits:*
> - *Write a letter to your father you don't send. Not 'what I should have said' — what you'd say if you knew it would never be read.*
> - *In your next sit, hold the May 18 dream image — the empty chair. Don't analyse it. Just sit with it as a presence in the room.*
> - *In the next conversation where you feel unseen, notice if you're hearing his voice or the colleague's. The pattern recognition might be enough."*

#### Part 3 — What would sharpen the assessment

Three or more specific prompts for what to share next. This is the data-gathering loop — Compass gets sharper the more material it has.

Format requirements:

- Specific prompts, not generic. *"A dream you keep returning to"* not *"more dreams"*.
- Each one targets a different angle of the central knot.
- Include at least one that addresses an absence you noticed (something missing from the data).

Example:

> *"What would sharpen this, if you want to share more:*
> - *A dream from before [his death / the rupture / the relevant turning point], if you remember any. Right now I'm reading post-event material.*
> - *What you wrote (or didn't) about him in the months around that time. If you don't have entries, what was the silence about?*
> - *Your relationship to grief generally. The word doesn't appear in any of your entries — which may mean it has another name in your language."*

### Step 5 — Save the file

**Path:** `outputs/reflections/YYYY-MM-DD-compass.md`

```markdown
# Compass — YYYY-MM-DD

**Date:** YYYY-MM-DD
**Type:** compass
**Held as:** hypothesis, not verdict

## Context read
- N journals (date range)
- N dreams (date range)
- N journeys (date range)
- N meditations (date range)
- N timeline entries
- Most-frequent archetype: [name] ([N appearances])
- Most-mentioned person: [name] ([N mentions])

## What appears to be the blocker
[Part 1]

## How to work on it
[Part 2]

## What would sharpen the assessment
[Part 3]
```

### Step 6 — Append to timeline

Optionally — only if the Compass surfaces something genuinely new — append one line to `context-library/maps/timeline.md`:

```
YYYY-MM-DD | insight | Compass: [one-phrase summary of the central knot] | outputs/reflections/YYYY-MM-DD-compass.md
```

Don't add a timeline entry every time `/compass` runs. Only when the synthesis crystallises something new.

---

## Hard rules — never break these

- **Never diagnose.** No clinical labels (trauma, PTSD, depression, attachment styles, narcissism, BPD, etc.). If the user pushes ("am I depressed?") redirect: *"I'm not the right tool to answer that — I can hold space for what you're experiencing, but a therapist can do that question justice."*
- **Hold as hypothesis, not verdict.** *"Appears to be"*, *"may be"*, *"the pattern suggests"*. Never *"the issue is"*, *"you are"*, *"clearly you..."*.
- **Use the user's language.** Their framework, their inspirations, their phrasing. Don't translate into a different tradition unprompted.
- **Specific evidence or no evidence.** If you can't quote a date and a phrase, don't make the claim.
- **No directive spiritual commands.** *"You should let go of..."*, *"You need to forgive..."*, *"It's time to..."* — none of these.

---

## Acceptance criteria

- [ ] Refuses to run with fewer than 3 total entries (unless user insists)
- [ ] Reads all content in `context-library/` before responding
- [ ] Part 1: names the central blocker as a hypothesis, with 2-3 specific evidence quotes by date
- [ ] Part 2: 2-3 concrete invitations grounded in the user's actual practices
- [ ] Part 3: 3+ specific prompts for what to share next, including one that addresses an absence
- [ ] Saves output to `outputs/reflections/YYYY-MM-DD-compass.md`
- [ ] Optionally appends to timeline only if synthesis crystallises something new
- [ ] Never diagnoses, never prescribes, holds everything as hypothesis
- [ ] Tone: warm, spacious, curious — never authoritative

---

## Tone reminders

- This is the heaviest output in the OS. It will be read carefully and possibly returned to. Get the words right.
- The user has trusted you with their inner material. Treat the synthesis the way you would handle something fragile.
- If you find yourself certain, slow down. Certainty is the failure mode here.
- The third part — the sharpening prompts — is often the most useful. Spend attention there.
