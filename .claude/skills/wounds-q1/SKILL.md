---
name: wounds-q1
description: Quick wound landscape read — 7 forced-choice questions resolving to the 1-2 primary wounds most activated right now. Entry point into the Wounds Map. Confidence label after Q1: rough. 5-8 minutes.
---

# /wounds-q1 — Wound landscape read

Entry point into the Numina OS Wounds Map. Seven questions. A rough reading of which wounds are most active right now. Five to eight minutes.

This is Q1 of the wound landscape assessment. It locates which of the 5 primary wounds are most activated in your current life — as dynamic states, not fixed identity labels. The five wounds are: Rejection, Abandonment, Humiliation, Betrayal, and Injustice. Q1 surfaces activation from current patterns. It does not yet map the protector layers, shadow expressions, or integrated gifts in depth — that is for the full `/maps wounds` generation.

---

## Behaviour

### Step 1 — Open

Present this intro, then begin Q1 immediately. No preamble beyond this.

> *Which wounds are asking for your attention right now?*
>
> *We all carry the five primary wounds in some form. What changes is which ones are activated — loud, present, shaping how we move through the world — and which are quieter. This reading finds where the charge is now.*
>
> *Seven questions. Pick the closest fit. There are no right answers.*

---

### Step 2 — Present the questions

Present each question one at a time. Wait for the user's answer before showing the next. Accept the letter only. **No commentary between questions.** Preserve the honest, meditative quality of the sequence.

---

**Q1. When you're triggered in a relationship, the feeling underneath is most often:**

(a) "I'm not enough, or I'm too much for people"
(b) "I'm going to be left"
(c) "I don't deserve this, or I'm somehow less than"
(d) "I've been let down, I can't fully trust"
(e) "This isn't right, this isn't fair"

---

**Q2. What you most work to keep hidden from others:**

(a) How much you need to belong and be accepted
(b) How much you need people — and how frightening that is
(c) That you don't feel worthy of what you want
(d) That you don't fully trust anyone to follow through
(e) How angry you are at how things are

---

**Q3. Your most automatic protective response in close relationships:**

(a) Performing, disappearing, or seeking reassurance about your worth
(b) Clinging, or leaving before they leave
(c) Shrinking, going along with things, making yourself smaller
(d) Taking control, doing it yourself, or keeping people at arm's length
(e) Withdrawing when something feels unjust, or insisting on being right

---

**Q4. The need that you can now see wasn't reliably met growing up:**

(a) To be accepted exactly as you were, without conditions
(b) To know you wouldn't be left, that someone would stay
(c) To be respected, not shamed or humiliated
(d) To be able to trust the people closest to you
(e) To be treated fairly, without arbitrary harshness

---

**Q5. The belief that still runs underneath your behavior:**

(a) "I'm fundamentally not enough"
(b) "I'll end up alone"
(c) "I don't deserve what others have"
(d) "If I let my guard down, I'll get hurt"
(e) "The world is unfair and nothing ever really changes"

---

**Q6. When you behave in ways you're not proud of, it tends to look like:**

(a) Harsh self-criticism, or judging others for not meeting your standard
(b) Becoming needy, or abruptly cutting someone off before they can leave
(c) Putting yourself down, or staying passive when you should speak up
(d) Micromanaging, refusing help, or shutting down emotionally
(e) Stewing in resentment, or holding a grudge long past its usefulness

---

**Q7. The pattern that keeps surfacing across your relationships and work:**

(a) Never quite feeling like you truly belong, even in places where you're welcomed
(b) A fear of closeness and a longing for it, existing at the same time
(c) Avoiding visibility or recognition, even when you want it
(d) Difficulty trusting others to follow through
(e) Chronic frustration at how things around you are handled

---

### Step 3 — Score inline

After Q7, tally wound signals across all answers:

| Letter | Wound |
|--------|-------|
| (a) | Rejection |
| (b) | Abandonment |
| (c) | Humiliation |
| (d) | Betrayal |
| (e) | Injustice |

- Wound with the most mentions = **most activated**
- Any wound within 1-2 votes of the leader = **also present**
- Others = **quiet** (not absent — less loud right now)

If tallies are highly spread with no clear leader, name it: *"Your answers spread across several wounds — that can mean more than one is activated at once, which is real. Here's where the weight seems to sit."* Then proceed with the plurality.

---

### Step 4 — Render the result

Show the result in the terminal. No file is written at Q1 level — the reading stays in conversation, and is noted in the Wounds Map file.

**ASCII pentagon constellation first**, with the top 1-2 wounds marked. All others shown as quiet. Adapt the layout to the actual results:

```
                    REJECTION
                   [○ quiet]

    BETRAYAL                      ABANDONMENT
    [○ quiet]                     [● activated]

    INJUSTICE            HUMILIATION
    [○ quiet]            [◉ also present]

    ●  most activated    ◉  also present    ○  quiet
```

Then a brief reading (2-3 sentences). Use their actual answers to name the specific patterns — do not just restate the wound's generic territory. Held as hypothesis, not verdict.

Example (Abandonment most activated, Humiliation also present):
> *Right now, Abandonment seems to be carrying the most charge — the fear of being left, and the way it pulls between clinging and leaving first. Humiliation is also present: something about worthiness and being seen that runs underneath. These two often move together.*

End with the confidence label and a CTA:

> *This is a rough reading — a first location, not a verdict. Run `/maps wounds` to see how this fits with everything else in your journals and entries.*

---

### Step 5 — Update the Wounds Map

If `context-library/maps/wounds.md` exists, prepend a Q1 reading note below the file header:

```markdown
## Q1 Reading — YYYY-MM-DD

**Confidence:** rough
**Most activated:** [Wound name]
**Also present:** [Wound name, or "none"]

[The 2-3 sentence reading from Step 4]

---
```

If the file does not exist yet, create it with just this section and a note that the full map is generated by `/maps wounds` once enough content exists.

---

## Acceptance criteria

- [ ] Intro shown once, then Q1 begins immediately
- [ ] Questions presented one at a time, no commentary between them
- [ ] User answers with a letter; next question follows without interpretation
- [ ] After Q7, wounds tallied inline
- [ ] Most activated = highest count; also present = within 1-2 votes
- [ ] Spread tally handled gracefully with a naming note
- [ ] Result shows ASCII pentagon constellation with top 1-2 wounds highlighted
- [ ] 2-3 sentence reading references the user's actual answer themes, not generic wound descriptions
- [ ] Confidence label "rough" shown clearly
- [ ] CTA toward `/maps wounds` seeded naturally
- [ ] `context-library/maps/wounds.md` updated with Q1 reading section

---

## Tone reminders

- Grounded and honest. These are tender territories. Move slowly.
- No em dashes. No "unlock," "transform," "breakthrough," "holistic."
- Numina lexicon: pattern, wound, protector, activation, threshold.
- A wound reading is an invitation to attend, not a label to carry.
- "Most activated right now" — not "this is who you are." Always.
- Hold lightly. The user knows their own patterns better than any questionnaire.
