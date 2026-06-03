---
name: how-it-works
description: Plain-language explanation of how the Numina OS memory layer works — logging, ingestion, patterns, commitments, and the four commands. Two modes: full explanation for new users, shorter contextual answer for returning users. Writes nothing. Conversational only.
---

# /how-it-works

A reference skill the user can call at any time. Not a tutorial — a plain-language explanation of the memory layer that meets the user where they are. No technical terms. No jargon. Just what they experience.

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
Give the full loop in plain language, with a concrete example drawn from their practice.

**Mode B — returning user (patterns or commitments exist):**
Shorter. Acknowledge what's already in the brain. Offer a menu for what they want explained.

---

### Mode A — Full explanation

Use their framework to make the explanation concrete. Pick the example that matches their primary practice.

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
> *1. How logging works*
> *2. What patterns are and how they form*
> *3. What commitments are*
> *4. The four commands (/capture, /recall, /pre-session, /sweep)*
> *5. Something specific"*

Answer only what they ask. If they pick 5, wait for their question.

---

## Acceptance criteria

- [ ] Reads `profile.md` and `voice.md` before responding
- [ ] Checks patterns/ and commitments/ INDEX to choose mode
- [ ] Mode A uses a concrete example drawn from the user's primary practice
- [ ] Mode A covers logging, patterns, commitments, and the four commands
- [ ] Mode B acknowledges what's already in the brain and offers a menu
- [ ] No technical terms: no "pipeline", "hook", "provenance", "ingestion", "schema"
- [ ] Writes nothing to the context library — conversational only
- [ ] Tone matches the OS: warm, grounded, unhurried

---

## Tone reminders

- Speak to the user, not about the system.
- One clear thing at a time. Don't explain everything in one breath.
- If they ask "why does it work this way?" — answer simply. The goal is trust, not architecture.
- If they seem uncertain, slow down and offer to go through one part more carefully.
