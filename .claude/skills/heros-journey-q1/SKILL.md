---
name: heros-journey-q1
description: Quick Hero's Journey placement — 8 questions + optional tiebreaker resolving to a rough stage on the 12-stage arc. Entry point into the Hero's Journey map. Confidence label after Q1: rough. 3-5 minutes.
---

# /heros-journey-q1 — Quick Hero's Journey placement

Entry point into the Numina OS Hero's Journey map. Eight questions. A rough location on the arc. Three to five minutes.

This is Q1 of the Hero's Journey assessment. It resolves to one of five phases (12 stages total). If two letters tie, a single tiebreaker question resolves to the specific stage within the phase. Confidence label: rough.

---

## Behaviour

### Step 1 — Open

Present this intro, then begin Q1 immediately.

> *Where are you on the Hero's Journey?*
>
> *A 3-4 minute reflection. Eight questions. Pick the answer closest to true. There are no right answers, only the one that meets you where you are.*

---

### Step 2 — Present the questions

Present each question one at a time. Wait for the answer before showing the next. Accept the letter only. **No commentary between questions.**

---

**Q1. When you wake up these days, the first feeling is closest to:**

(a) Things are mostly fine, but there's a quiet restlessness
(b) Something is calling and I can't unhear it
(c) I've stepped into the work and it's reshaping me
(d) I'm in the middle of something hard, the old shape is breaking
(e) Something cracked open. I'm finding my feet again

---

**Q2. Your relationship with change:**

(a) I sense it coming but I haven't moved
(b) I've started, even if the steps are small
(c) I'm in it. Patterns I didn't see before are surfacing
(d) I'm being asked to let go of more than I expected
(e) I'm bringing what I've learned back into ordinary life

---

**Q3. Practices, teachers, or frameworks (meditation, therapy, plant medicine, journaling, traditions):**

(a) Curious, haven't really started
(b) Found one or two that speak to me, I'm learning
(c) Practising regularly and meeting what arises
(d) The practice isn't optional anymore. It's holding me through something
(e) I've integrated several and I'm finding my own language for it

---

**Q4. When you turn your attention inward:**

(a) I notice I avoid it more than I'd like
(b) I'm starting to look, with help
(c) I'm finding allies and naming the inner voices
(d) I'm sitting with something I used to run from
(e) Witnessing has become a way of being

---

**Q5. Community on the path:**

(a) Mostly alone with this
(b) I've started finding people who get it
(c) I have allies, and I've also met my inner critics
(d) The journey has felt lonely lately, even with others around
(e) I find myself being a guide for people who are earlier on

---

**Q6. The hardest thing you're holding right now:**

(a) Whether to begin at all
(b) The discomfort of leaving who I was
(c) Confronting a pattern I keep repeating
(d) A loss, an ego death, or meeting my shadow
(e) Translating insight into ordinary, daily life

---

**Q7. Looking at the last 12 months, the change in you is best described as:**

(a) Mostly the same, though something is asking for more
(b) Subtle but real. New questions are open
(c) Visible. People close to me have noticed
(d) Disorienting. I don't recognise parts of my old life
(e) Quiet and deep. I feel more myself than before

---

**Q8. If you imagine your future self five years from now:**

(a) I can barely picture them
(b) I see them and the road feels long
(c) I see them and I'm walking toward them
(d) The picture broke. Something truer is forming
(e) They're already arriving, in small daily ways

---

### Step 3 — Score inline

Count letter frequency across Q1-Q8. The dominant letter determines the phase:

| Letter | Phase | Stages |
|--------|-------|--------|
| (a) | A. Ordinary World and The Call | 1, 2, 3 |
| (b) | B. Crossing the Threshold | 4, 5 |
| (c) | C. Tests, Allies, and the Inmost Cave | 6, 7 |
| (d) | D. The Ordeal and The Reward | 8, 9 |
| (e) | E. The Return | 10, 11, 12 |

**Tie handling:** if two letters tie, ask the tiebreaker for both phases (Step 4) and let the user pick the closer fit.

If the tally is highly spread with no clear dominant letter, name it: *"The spread across your answers suggests you're in multiple phases at once — that's real, not a problem with the questionnaire. Here's where the weight seems to be sitting."* Then proceed with the plurality.

---

### Step 4 — Tiebreaker (only if needed)

Ask one branched question based on which two phases tied. The user picks the closer fit.

**Phase A tiebreaker (stages 1-3):**
> *One more question. In the Ordinary World, some people haven't yet heard a call — settled, or restless but not yet moved. Others have heard it but are holding back. Others are refusing it outright. Which is closest to true right now?*

- Stage 1: settled, no signal
- Stage 2: the call has arrived
- Stage 3: refusing or postponing the call

**Phase B tiebreaker (stages 4-5):**
> *You're at the threshold. Have you found a guide or practice helping you cross — or have you committed fully, past the point of turning back?*

- Stage 4: found a mentor or practice, still learning
- Stage 5: committed, no turning back

**Phase C tiebreaker (stages 6-7):**
> *You're in the middle work. Are you still meeting the tests and finding allies — or have you begun to sense what's at the heart of it, the thing you've been approaching all along?*

- Stage 6: tests and allies, still on the path
- Stage 7: approaching the cave, the core work is near

**Phase D tiebreaker (stages 8-9):**
> *The hard part. Are you in the ordeal itself — inside the loss, the dissolution, the hardest moment — or are you holding something on the other side of it, trying to understand what came through?*

- Stage 8: inside the ordeal
- Stage 9: holding the reward, integrating what came through

**Phase E tiebreaker (stages 10-12):**
> *You're returning. Is the path back still bumpy — old life pulling, new self not yet settled? Or have you been tested and held through it? Or are you finding yourself as a guide for others?*

- Stage 10: road back, still integrating
- Stage 11: tested and held, near the threshold
- Stage 12: offering to others

---

### Step 5 — Render the result

Show the result in the terminal. No file is written at Q1 level — the reading stays in conversation.

**ASCII arc first**, with the user's phase marked:

```
  Departure        Initiation            Return
  ─────────────────────────────────────────────
  [ A ] ──── [ B ] ──── [ C ] ──── [ D ] ──── [ E ]
 Ordinary   Threshold  Tests &    Ordeal &    Return
  World               Inmost Cave  Reward
```

Place a `●` below the user's phase. If the user is in Phase C:

```
  [ A ] ──── [ B ] ──── [ C ] ──── [ D ] ──── [ E ]
                         ●
```

Then: the stage name and a 2-3 sentence description grounded in what the user actually said. Held as hypothesis.

Example (Phase C, Stage 7):
> *You appear to be approaching the Inmost Cave — the threshold just before the central ordeal. The patterns you're confronting that keep repeating, and the sense that your practice is no longer optional, both point here. You're not lost. You're close to the thing the whole journey has been building toward.*

End with the confidence label and CTA:
> *This is a rough placement — a first location, not a verdict. The 10-minute reflection goes deeper.*

---

### Step 6 — Update the Hero's Journey map

If `context-library/maps/heros-journey.md` exists, prepend a Q1 reading note below the file header:

```markdown
## Q1 Reading — YYYY-MM-DD

**Confidence:** rough
**Phase:** [Letter and phase name]
**Stage:** [Stage number and name if tiebreaker was used; otherwise "within Phase [X]"]

[The 2-3 sentence reading from Step 5]

---
```

If the file does not exist yet, create it with just this section and a note that the full map is generated by `/maps heros-journey` once enough content exists.

---

## Acceptance criteria

- [ ] Intro shown once, then Q1 begins immediately
- [ ] Questions presented one at a time, no commentary between them
- [ ] After Q8, letter frequency counted and dominant phase identified
- [ ] Tiebreaker asked only when two letters tie; resolves to specific stage
- [ ] Spread tally handled gracefully with a naming note
- [ ] ASCII arc rendered with user's phase marked clearly
- [ ] Stage name + 2-3 sentence reading references the user's actual answers, not generic stage descriptions
- [ ] Confidence label "rough" shown clearly
- [ ] CTA toward deeper read seeded naturally
- [ ] `context-library/maps/heros-journey.md` updated with Q1 reading section

---

## Tone reminders

- Wise, sincere, grounded. Witness before wisdom.
- No em dashes. No "unlock," "transform," "breakthrough," "holistic."
- Numina lexicon: threshold, witness, pattern, shadow.
- A placement on the arc is a mirror, not a destination.
- The user may be in multiple phases at once. Name it when the data shows it.
