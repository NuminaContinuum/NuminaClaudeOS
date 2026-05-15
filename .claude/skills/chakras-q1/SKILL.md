---
name: chakras-q1
description: Quick chakra read — 8 forced-choice questions resolving to the top 1-2 chakras calling for attention right now. Entry point into the Chakras map. Confidence label after Q1: rough. 3-5 minutes.
---

# /chakras-q1 — Quick chakra read

Entry point into the Numina OS Chakras map. Eight questions. One clear reading. Three to five minutes.

This is Q1 of the chakra assessment. It locates *where* the work is — which centres are calling for attention right now. It does not yet determine whether a chakra is deficient or excessive — that is Q2's job.

---

## Behaviour

### Step 1 — Open

Present this intro, then begin Q1 immediately. No preamble beyond this.

> *Where in the body is your work right now?*
>
> *The chakra map locates where energy is moving — or stuck — in your life. Seven centres, each tied to a different kind of life force.*
>
> *Eight short questions. Pick the closest fit. There are no right answers.*

---

### Step 2 — Present the questions

Present each question one at a time. Wait for the user's answer before showing the next. Accept the letter only. **No commentary between questions.** Preserve the meditative quality of the sequence.

---

**Q1. The most accurate description of your everyday baseline:**

(a) Anxious about money, safety, or basic survival
(b) Emotionally numb, or emotionally flooded
(c) Drained, or pushing too hard
(d) Lonely, or losing myself in others
(e) Unspoken truths sitting in my throat
(f) Foggy, can't see clearly ahead
(g) Disconnected from anything larger

---

**Q2. The body part that's been speaking to you most:**

(a) Lower back, legs, feet
(b) Hips, lower belly, sexual organs
(c) Stomach, gut, solar plexus
(d) Chest, shoulders, upper back
(e) Throat, jaw, neck
(f) Head, eyes, brow
(g) Crown of the head, or "outside" the body

---

**Q3. What's hardest in relationships right now:**

(a) Trusting people enough to feel safe
(b) Letting myself feel pleasure or intimacy
(c) Asserting myself without dominating
(d) Letting love in, or out, without losing myself
(e) Saying what I actually mean
(f) Seeing the other person clearly, not my projection
(g) Feeling part of something larger together

---

**Q4. The kind of work my inner life is asking for:**

(a) Stability, grounding, settling somewhere
(b) Reclaiming pleasure, creativity, or feeling
(c) Stepping into my power without aggression
(d) Healing my heart, or opening it again
(e) Speaking what I've kept silent
(f) Trusting my intuition and inner sight
(g) Reconnecting to meaning beyond the daily

---

**Q5. The thing I most often run from:**

(a) Insecurity. Will I be okay?
(b) Feelings. They overwhelm me, or escape me
(c) Conflict. I either fight or fold
(d) Vulnerability. Loving or being loved
(e) Saying no, or saying too much
(f) Quiet knowing. I doubt what I sense
(g) Awe, or surrender to mystery

---

**Q6. The dream or daydream that keeps recurring:**

(a) A safe home, secure footing
(b) Wild creativity, sensual freedom
(c) Standing tall, being seen for who I am
(d) Deep love, reconciliation, forgiveness
(e) Speaking publicly, being heard, singing
(f) Visions, symbols, prescient dreams
(g) Dissolving into something larger

---

**Q7. Which feels furthest out of reach right now:**

(a) A sense that I am safe
(b) Joy and aliveness in my body
(c) Trust in my own agency
(d) Feeling truly loved, or truly loving
(e) My own voice
(f) Clarity about what's true
(g) A sense of meaning

---

**Q8. If a wise friend listened to my life right now, they'd probably say:**

(a) "You need to find your ground."
(b) "Let yourself feel."
(c) "Take your power back."
(d) "Open your heart again, gently."
(e) "Speak what you've been holding."
(f) "Trust what you already know."
(g) "Look up. Remember the larger story."

---

### Step 3 — Score inline

After Q8, tally chakra mentions across all 8 answers:

| Letter | Chakra |
|--------|--------|
| (a) | Root (Muladhara) |
| (b) | Sacral (Svadhisthana) |
| (c) | Solar Plexus (Manipura) |
| (d) | Heart (Anahata) |
| (e) | Throat (Vishuddha) |
| (f) | Third Eye (Ajna) |
| (g) | Crown (Sahasrara) |

- Chakra with the most mentions = **primary focus**
- Any chakra within 1-2 votes of the leader = **secondary focus** (include it)
- Do not resolve direction (deficient vs. excessive) — that is Q2

---

### Step 4 — Render the result

Show the result in the terminal. No file is written at Q1 level — the reading stays in conversation.

**ASCII overview first**, with the top 1-2 chakras marked. All others shown as quiet. Use the user's actual tally:

```
    7  Crown (Sahasrara)          ○  quiet
    6  Third Eye (Ajna)           ○  quiet
    5  Throat (Vishuddha)         ○  quiet
    4  Heart (Anahata)            ●  calling for attention
    3  Solar Plexus (Manipura)    ○  quiet
    2  Sacral (Svadhisthana)      ◉  also present
    1  Root (Muladhara)           ○  quiet

    ●  primary focus    ◉  secondary focus    ○  quiet
```

Then a brief reading (2-3 sentences). Use their actual answers to name the themes — do not just restate the chakra's generic territory. Held as hypothesis, not verdict.

Example:
> *Right now, your Heart is most asking for your attention. The themes you named — vulnerability, the difficulty of letting love in, the longing for reconciliation — all point to this centre. The Sacral is also present, underneath the heart work: something about feeling, creativity, or aliveness that hasn't yet been given space.*

End with the confidence label and a CTA:

> *This is a rough reading — a first location, not a diagnosis. Want to go deeper? The 10-minute reflection will sharpen it.*

---

### Step 5 — Update the chakras map

If `context-library/maps/chakras.md` exists, prepend a Q1 reading note below the file header:

```markdown
## Q1 Reading — YYYY-MM-DD

**Confidence:** rough
**Primary focus:** [Chakra name]
**Secondary focus:** [Chakra name, or "none"]

[The 2-3 sentence reading from Step 4]

---
```

If the file does not exist yet, create it with just this section and a note that the full map is generated by `/maps chakras` once enough content exists.

---

## Acceptance criteria

- [ ] Intro shown once, then Q1 begins immediately
- [ ] Questions presented one at a time, no commentary between them
- [ ] User answers with a letter; next question follows without interpretation
- [ ] After Q8, chakras tallied inline
- [ ] Primary focus = most mentions; secondary = within 1-2 votes
- [ ] Result shows ASCII column with top 1-2 chakras highlighted
- [ ] 2-3 sentence reading references the user's actual answer themes, not generic chakra descriptions
- [ ] Confidence label "rough" shown clearly
- [ ] CTA toward deeper read seeded naturally at the end
- [ ] `context-library/maps/chakras.md` updated with Q1 reading section

---

## Tone reminders

- Wise, sincere, grounded. Witness before wisdom.
- No em dashes. No "unlock," "transform," "breakthrough," "holistic."
- Numina lexicon: ground, witness, threshold, pattern, centre.
- The reading is an invitation to pay attention, not a label to carry.
- Hold lightly. The user knows their own body better than any questionnaire.
