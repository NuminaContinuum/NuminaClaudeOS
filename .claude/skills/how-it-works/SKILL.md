---
name: how-it-works
description: Plain-language explanation of how Numina OS works — the main skills (/dream, /journal, /maps, /questionnaire) and the memory layer (logging, patterns, commitments, the four commands). Two modes: full explanation for new users, shorter contextual answer for returning users. Writes nothing. Conversational only.
---

# /how-it-works

A reference skill the user can call at any time. Not a tutorial — a plain-language explanation of how the OS works, starting with the skills they'll use most, then the memory layer underneath. No technical terms. No jargon. Just what they experience.

---

## Behaviour

### Step 1 — Read context

1. Read `context-library/profile.md` for framework and practices.
2. Read `context-library/voice.md` for tone and vocabulary.
3. Check `context-library/patterns/INDEX.md` and `context-library/commitments/INDEX.md` to see whether the user has any existing patterns or commitments.

If `profile.md` doesn't exist:

> *"It looks like `/setup` hasn't been run yet. That's fine — but running it first will let me explain things in a way that's more specific to your practice. Want to do that now, or would you like a general explanation?"*

If they want to proceed without setup, give the general explanation from Step 2.

---

### Step 2 — Choose mode

**Mode A — first call (no patterns or commitments yet):**
Give the full explanation: start with the main skills, then the memory layer underneath, with a concrete example drawn from their practice.

**Mode B — returning user (patterns or commitments exist):**
Shorter. Acknowledge what's already in the brain. Offer a menu for what they want explained.

---

### Mode A — Full explanation

Start with the skills they'll actually use, then explain the memory layer that sits beneath them.

#### Part 1 — The main skills

Explain the four core skills in plain language. Adapt the wording to their practice from `profile.md`, but the structure is always the same:

**`/dream`**

> *"When you have a dream you want to work with, type `/dream` and share it. The OS logs the full narrative, surfaces a few symbols through whatever lens you're working with — Jungian, shamanic, Buddhist, or your own — and asks one deepening question. It also notes who appeared in the dream, which builds the relationship and archetype maps over time."*

**`/journal`**

> *"For a journal entry — a reflection, a difficult moment, something you're processing — type `/journal`. The OS receives it, surfaces the recurring themes it notices, and asks one question. Over time, it tracks what keeps coming back across your entries."*

**`/maps`**

> *"Maps are the synthesis layer. After you've logged enough — dreams, journals, journeys, meditations — type `/maps` to generate a living picture of where you are. There are universal maps (a timeline, a relationship overview, an archetype overview) and framework maps based on what you selected in setup (Hero's Journey, Individuation, Chakras, Wounds & Gifts, etc.).*
>
> *Maps go stale and need to be refreshed. The detail lives in the individual entries. The maps are the view."*

**`/questionnaire`**

> *"Each framework map can be enriched with a questionnaire. Type `/questionnaire` and it'll ask which one you want — or you can go directly with `/questionnaire wounds`, `/questionnaire chakras`, etc. Each questionnaire runs in stages: a quick first read (3-5 minutes), then a deeper dive, then a long settled reading if you want it. You can redo any stage at any time and in any order."*

After explaining these four, say:

> *"There are other skills too — `/integrate` for journeys or ceremonies, `/meditation` for sits, `/inner-review` for a weekly reflection, `/compass` for a deeper synthesis, `/harvest` to bring in a large batch of existing notes. But `/dream`, `/journal`, `/maps`, and `/questionnaire` are the core loop."*

---

#### Part 2 — The memory layer

**Structure:**

1. **Logging** — what it means to log something
2. **What gets held** — how the OS keeps the raw material
3. **Patterns** — what they are and how they form
4. **Commitments** — what they are
5. **The commands** — a brief list

**Examples by framework:**

*Jungian / depth psychology:*
> *"When you log a dream, the dream text is kept exactly as you told it — nothing is changed or interpreted yet. As you log more dreams, if the same figure or image keeps appearing, I'll notice it and ask if you want to name it as a pattern. The wolf that showed up three times across your dreams and a journal entry might become a named pattern — something like 'the wolf at the threshold' — but only if you agree. That's your language, not mine."*

*Shamanic / journey-based:*
> *"When you log a journey, the full account goes in exactly as you described it. If a spirit, landscape, or challenge keeps returning across different journeys and your journals, I'll ask if you want to name it as a recurring pattern in your practice. You decide what to call it and whether it's ready."*

*Meditation / Buddhist:*
> *"When you log a sit, the observations you noticed — a quality of mind, a recurring hindrance, a moment of clarity — go in unchanged. If the same thing keeps appearing across your sits, your dreams, and your journals, I'll ask if you want to name it. Until then it stays in the log, building quietly."*

*Somatic / trauma-informed:*
> *"When you log a body experience or journal entry, it stays verbatim. If a sensation, pattern of avoidance, or felt response keeps appearing across your entries, I'll notice it and ask if you want to name it as something recurring. The body has its own timing — I won't rush it."*

*No framework set:*
Use the meditator example above, or keep it completely plain:
> *"When you log an entry — a dream, a journal, a sit, a journey — it goes in exactly as you wrote it. Nothing is interpreted without you. Over time, if something keeps appearing across different types of entries, I'll ask if you want to name it as a pattern. A pattern is just a recurring theme you've confirmed. A commitment is a practice or intention you've chosen to track."*

**After the example, name the four commands briefly:**

> *"There are four commands beyond the main skills:*
> *`/capture` — for anything that doesn't fit a main skill (a book passage, a teacher note, a voice memo)*
> *`/recall` — ask any question about your own material and get an answer with citations back to the entries*
> *`/pre-session` — a briefing before a therapy session, ceremony, or meeting with a teacher*
> *`/sweep` — the longer maintenance pass, run monthly or seasonally, to surface what's accumulated"*

**Close with a single offer:**

> *"Anything you'd like me to go into more depth on?"*

---

### Mode B — Returning user

Acknowledge the brain briefly. Then offer a menu.

> *"You have [N] active pattern(s) and [N] commitment(s) in the brain. What would you like me to explain?*
> *1. The main skills — /dream, /journal, /maps, /questionnaire*
> *2. How logging works*
> *3. What patterns are and how they form*
> *4. What commitments are*
> *5. The four commands (/capture, /recall, /pre-session, /sweep)*
> *6. Something specific"*

Answer only what they ask. If they pick 6, wait for their question.

---

## Acceptance criteria

- [ ] Reads `profile.md` and `voice.md` before responding
- [ ] Checks patterns/ and commitments/ INDEX to choose mode
- [ ] Mode A Part 1 explains /dream, /journal, /maps, and /questionnaire in plain language — no setup required
- [ ] Mode A Part 1 uses the user's practice from `profile.md` to make the examples concrete
- [ ] Mode A Part 2 covers logging, patterns, commitments, and the four commands
- [ ] Mode B offers a menu that includes the main skills as option 1
- [ ] No technical terms: no "pipeline", "hook", "provenance", "ingestion", "schema"
- [ ] Writes nothing to the context library — conversational only
- [ ] Tone matches the OS: warm, grounded, unhurried
- [ ] Works for users who haven't run `/setup` yet — degrades gracefully to a generic explanation

---

## Tone reminders

- Speak to the user, not about the system.
- One clear thing at a time. Don't explain everything in one breath.
- If they ask "why does it work this way?" — answer simply. The goal is trust, not architecture.
- If they seem uncertain, slow down and offer to go through one part more carefully.
