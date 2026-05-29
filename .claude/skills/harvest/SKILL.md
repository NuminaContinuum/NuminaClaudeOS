---
name: harvest
description: Bulk-import existing content from a single file. Splits entries, stores them individually by content type (journals, dreams, journeys), then automatically synthesizes patterns across the full import and opens a live terminal dialog — surfacing what it found and asking one question worth sitting with.
---

# /harvest — Bulk import

Many users come to Numina OS with years of existing material — dream diaries, journal exports, trip reports. `/harvest` is how that material gets in without being typed in entry-by-entry.

This is the most file-heavy skill. Move carefully — splitting wrong is hard to undo.

---

## Usage

```
/harvest journeys path/to/file.md     → ingests journey reports into context-library/journeys/
/harvest dreams path/to/file.md       → ingests dreams into context-library/dreams/
/harvest journals path/to/file.md     → ingests journals into context-library/journals/
/harvest synthesize                   → re-run synthesis across everything imported (anytime)
```

Synthesis now runs automatically after every import — you do not need to call it separately. `/harvest synthesize` is available to re-run it later or to synthesize across multiple previous imports.

---

## Behaviour — ingestion

### Step 1 — Validate the call

The user must specify a content type (`journeys`, `dreams`, or `journals`) and a file path. If either is missing, ask:

> *"To harvest, I need two things — what type of content (journeys, dreams, or journals) and the file path. Drop those and we'll go."*

### Step 2 — Read and split the file

Read the file. Detect entry boundaries. Common separators:

- `---` (markdown horizontal rule) between entries
- A date heading at the top of each entry (`## 2024-03-12`, `# March 12 2024`)
- A title heading repeated per entry
- Triple line break + capitalised opener
- Numbered entries (`Entry 1`, `Entry 2`)

If the separator is unambiguous, proceed. If ambiguous, **ask before splitting**:

> *"I see a few possible split patterns in this file — date headings, `---` separators, and numbered entries. Want me to split on date headings (looks like 47 entries) or `---` (looks like 12 sections)? Or paste me a sample of how a single entry should look."*

### Step 3 — Parse each entry

For each split entry, extract:

- **Date** — from the entry itself if present (any reasonable format). If dates are absent or unclear for more than half the entries, pause before continuing and ask:

  > *"I can see these entries but the dates aren't clearly marked. Can you tell me roughly when they were written, or what time period they cover? Even a rough range (e.g. '2020–2024') helps me place them accurately in your timeline."*

  Wait for the answer. Accept any reasonable range and apply best judgement to distribute entries within it. If the user says they don't know, proceed with today's import date as a fallback and note it in each file's frontmatter. Do not use the fallback silently — always make this offer first.

- **Title** — from a heading if present. Otherwise infer two to four words from the first line. If you can't, use a sequence number.
- **Body** — the full text of the entry, verbatim.

### Step 4 — Store each as an individual file

For content type `journeys`:
- Path: `context-library/journeys/YYYY-MM-DD-[brief-title].md`
- Use the journey file structure from `/integrate` SKILL.md (frontmatter: Date, Type=journey, Modality if inferable, Phase=post by default since they're old).

For content type `dreams`:
- Path: `context-library/dreams/YYYY-MM-DD-[brief-title].md`
- Use the dream file structure from `/dream` SKILL.md.

For content type `journals`:
- Path: `context-library/journals/YYYY-MM-DD-[brief-title].md`
- Use the journal file structure from `/journal` SKILL.md.

For each, the body goes verbatim into the "Narrative" or "Entry" section. Do not interpret on the way in. Themes, symbols, and people get filled in during the auto-update step.

If a file with the same path already exists, append a sequence (`-2.md`, `-3.md`). Never overwrite.

### Step 5 — Auto-update the memory layer

After all entries are stored, run a single pass across the full import:

- Detect named people across all entries → create or append `context-library/relationships/[name].md` files. Cross-link multiple entries.
- Detect recurring symbols and archetypes → create or append `context-library/archetypes/[name].md`. Frequency counts based on the import.
- Detect notable events that warrant timeline entries — be selective. From a 50-entry import, expect maybe 3-8 timeline events, not 50.

For dream imports, mark figures as dream/inner figures by default. For journal imports, mark figures as waking-life unless context says otherwise.

### Step 6 — Report

Tell the user clearly:

> *"Harvested 47 dreams from your file into `context-library/dreams/`. Dates ranged from 2019-04-12 to 2024-09-30. Created 8 relationship files (most-mentioned: your father, the wolf figure, Anna). Created 14 archetype files. Added 5 entries to the timeline."*

Then move directly to synthesis — do not ask permission.

### Step 7 — Auto-synthesis

Run synthesis automatically. Do not wait for the user to ask. Do not offer it as an option — just do it, and tell them it's running:

> *"Running synthesis across the full import..."*

Follow the synthesis logic below (same as `/harvest synthesize`). Write the result to `outputs/reflections/YYYY-MM-DD-harvest-synthesis.md`.

### Step 8 — Live terminal dialog

After synthesis is written, surface what you found in the terminal. This is not a transcript of the synthesis file — it's the two or three things that matter most, spoken directly.

**Format:**

Name 1-2 of the strongest recurring patterns in the terminal. Specific and grounded — dates, quotes, names where useful.

Then ask one question. Not a directive. Something worth sitting with given everything in the import.

Example:

> *"Across four years of dreams, the wolf appears 11 times — always at thresholds. Doorways, bridges, the edge of forests. He never crosses with you.*
>
> *The arc in the journals shifts noticeably around early 2022 — something settled, or something was put down.*
>
> *What do you think you were putting down?"*

Then wait. Let the question breathe.

**If the user responds:**
Acknowledge briefly — one or two sentences, warm, no interpretation forced. Then offer:

> *"Want me to add that to the synthesis file?"*

If yes, append a `## Response` section to `outputs/reflections/YYYY-MM-DD-harvest-synthesis.md`.

**If the user types "skip", "no", or moves on:**
Accept without comment. Suggest next steps:

> *"Worth running `/maps` now to see how this reshapes the overviews. Or `/compass` if you want to look at a specific thread."*

---

## Behaviour — synthesize (standalone)

When the user runs `/harvest synthesize` independently (to re-run or synthesize across multiple imports):

### Step 1 — Read everything

Read all files in `context-library/journals/`, `dreams/`, `journeys/`, `meditations/`. Also read `relationships/` and `archetypes/` to know what's been catalogued.

### Step 2 — Synthesize patterns

Output a structured cross-content analysis. Three to five paragraphs, no more. Cover:

**1. Recurring themes across content types**
What appears across journals AND dreams AND journeys, not just within one type. Specificity matters. *"The theme of unfinished conversations with your mother appears in 11 journal entries (2019-2024) and 4 dreams"* beats *"family relationships are recurring"*.

**2. The arc**
What's shifted over time. Use specific dates. *"Early entries (2019-2020) circle anger at your father. Mid-period entries (2021-2022) shift to grief. Most recent (2023+) show acceptance and curiosity about who he was beyond your relationship to him."*

**3. The most weighted symbols and people**
Top 3-5 from `archetypes/` and `relationships/` by frequency. Note the relationship descriptor.

**4. What's notably absent**
Sometimes more interesting than what's present. *"In four years of journals, I notice almost no entries about your work — and zero about romantic relationships. That may be by design or it may be a missing layer."*

**5. One synthesis question**
Not a directive. A question worth sitting with given everything you've read.

### Step 3 — Write and open dialog

Write synthesis to `outputs/reflections/YYYY-MM-DD-harvest-synthesis.md`, then run the live terminal dialog from Step 8 above.

---

## Acceptance criteria

- [ ] Accepts content type flag (`journeys` / `dreams` / `journals`) and file path
- [ ] Asks before splitting when separators are ambiguous
- [ ] Asks for date clarification when dates are absent or unclear in the majority of entries — never falls back silently
- [ ] Parses each entry — extracts date, title, body
- [ ] Stores each as an individual dated file in the correct subfolder, never overwriting
- [ ] Uses the same file structure as the equivalent capture skill (`/journal`, `/dream`, `/integrate`)
- [ ] Runs auto-update across the full import: people, archetypes, timeline (selectively)
- [ ] Reports import results clearly: count, date range, records created
- [ ] Synthesis runs automatically after every import — no separate command required
- [ ] Synthesis is saved to `outputs/reflections/YYYY-MM-DD-harvest-synthesis.md`
- [ ] 1-2 strongest patterns and one question surface in the terminal as a live dialog
- [ ] User can respond; response is optionally appended to the synthesis file
- [ ] User can skip the dialog without friction
- [ ] `/harvest synthesize` available to re-run synthesis independently at any time

---

## Tone reminders

- The user has handed you years of inner work. Do not skim.
- Specific quotes and dates beat abstract themes. *"On 2021-08-04 you wrote 'I'm not sure I ever forgave him'"* lands. *"You sometimes mention forgiveness"* doesn't.
- Do not flatten contradictions in their material. If they swung between hope and despair, name both.
- The synthesis is a mirror, not a verdict. Hold it lightly.
- The terminal dialog after a big harvest is an opening, not a debrief. One pattern, one question, then silence.
