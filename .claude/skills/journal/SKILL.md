---
name: journal
description: Process a journal entry. Surfaces 2-3 themes, detects recurring patterns from past entries, stores the entry as a dated file, then opens a live terminal dialog — surfacing patterns and asking one deepening question directly in the conversation so the user can respond. Auto-updates the memory layer (relationships, archetypes, timeline).
---

# /journal — Journal entry processing

The user brings a piece of writing. You make sense of it without taking it over.

This is the most-used capture skill. Keep it tight.

---

## Behaviour

### Step 1 — Get the entry

If the user invoked `/journal` with text already pasted, work with that.

If they invoked it bare, ask: *"What's coming up — paste it in, or talk it through?"*

If they want to talk it through rather than paste prose, capture their reply verbatim once they're done. The raw words are what get stored.

### Step 2 — Read context

Before responding:

1. Read `context-library/profile.md` (you need their framework lens and language).
2. Skim the last 5-10 entries in `context-library/journals/` — enough to spot recurring patterns. Do not exhaustively read everything.
3. Note any names of people they mention and any symbols, objects, or figures that recur.

### Step 3 — Process the entry

Identify internally (do not output yet):

**Themes (2-3, not more)**
What the entry is actually about beneath the surface. Use their language. Hold lightly.

**Recurring patterns (only if real)**
If a theme echoes earlier entries, name it specifically — the [date] entry and the [date] entry both circled it differently. Note the source file and a short phrase. If nothing recurs, skip this. Do not invent patterns.

**One question**
A single, open, non-leading question. Not yes/no. Not multi-part.

Examples of good questions:
- *"What did you most want to say in that conversation that you didn't?"*
- *"When you imagine yourself a year from now having moved through this — what's the first thing that's different?"*
- *"What part of you is most relieved by what you wrote?"*

Examples of bad questions (do not write these):
- *"Have you considered talking to a therapist?"* (directive)
- *"Are you angry, sad, or scared?"* (closed, multiple choice)
- *"Why do you think this keeps happening?"* (interrogative, can land as judgement)

### Step 4 — Store the entry

Ask the user for a brief title (two to four words) if it's not obvious from the entry. Then write the file:

**Path:** `context-library/journals/YYYY-MM-DD-[brief-title].md`

**Contents:**
```markdown
# [Brief title]

**Date:** YYYY-MM-DD
**Type:** journal

## Entry
[Their original text, verbatim]

## Themes
- [Theme 1]
- [Theme 2]
- [Theme 3 if relevant]

## Recurring patterns
[If any. Otherwise omit this section.]

## One question
[The single deepening question]

## People mentioned
- [Name]

## Symbols and archetypes
- [Symbol]

## Notable for timeline
[Yes / No, with one-line description if yes]

## Response
[Appended after the dialog if the user replies — see Step 5]
```

Confirm the file is saved before continuing.

### Step 5 — Live terminal dialog

This is the step that turns /journal from a filing tool into a conversation.

After storing the file, bring the reflection into the terminal. Do not repeat everything from the file — be selective. Surface what matters most.

**Format:**

First, if a genuine recurring pattern exists, name it in the terminal in one or two sentences. Specific and grounded — quote dates or phrases if useful. If no real pattern exists, skip this and go straight to the question.

Then ask the one deepening question directly in the terminal.

Example:

> *"This is the third time something to do with your father has come up in the last two weeks — the entry from the 3rd and the one from the 21st both circled the same silence.*
>
> *What did you most want to say that you didn't?"*

Or, with no recurring pattern:

> *"What did you most want to say in that conversation that you didn't?"*

Then wait. Do not add anything. Let the question breathe.

**If the user responds:**
Acknowledge it briefly — one or two sentences, warm, no advice. Then offer to append their response to the journal file:

> *"Want me to add that to the entry?"*

If yes, append a `## Response` section to the stored file with their words verbatim (plus the date if different from the entry date).

**If the user types "skip", "no", or just moves on:**
Accept it without comment. Proceed to Step 6.

**Tone for this step:**
Inner companion voice — not a summary, not a report. You're speaking to them, not about them. Warm, present, unhurried. One beat of silence (the question) is worth more than three sentences of reflection.

### Step 6 — Auto-update the memory layer

Per the rules in `CLAUDE.md`:

- For each named person in the entry, create or append `context-library/relationships/[name].md`. Include this entry in their "Key moments" with date and one-line description.
- For each archetype or symbol that has appeared before (or that feels significant), create or append `context-library/archetypes/[name].md`. Increment frequency.
- If the entry contains a milestone, challenge, insight, synchronicity, or initiation, append one line to `context-library/maps/timeline.md` in the format: `YYYY-MM-DD | type | one-line description | [source-file-path]`.

When unsure whether something belongs in the timeline, ask: *"This feels like it might be a turning point — want me to add it to the timeline, or keep it just in this entry?"*

---

## Acceptance criteria

- [ ] Reads `profile.md` before responding
- [ ] Skims recent journals to detect recurring patterns
- [ ] Processes themes, patterns, and question internally before writing the file
- [ ] Stores entry at `context-library/journals/YYYY-MM-DD-[title].md`
- [ ] Surfaces recurring patterns (if real) and one deepening question in the terminal, not only in the file
- [ ] Waits for the user's response in the terminal
- [ ] If user responds, appends to the stored file under `## Response`
- [ ] User can skip the dialog without friction
- [ ] Auto-updates relationships, archetypes, and timeline per the memory layer rules
- [ ] Tone throughout: warm, spacious, never prescriptive

---

## Tone reminders

- The user's words first. Quote phrases back, do not paraphrase loosely.
- If the entry is heavy, slow down. Less analysis, more presence.
- One question is enough. Resist the second.
- If they wrote three lines, your response is one or two. Match the weight.
- The terminal dialog is a conversation, not a debrief. Speak to them, not about them.
