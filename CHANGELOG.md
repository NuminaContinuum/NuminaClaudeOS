# Changelog

All notable changes to Numina OS are documented here.

Format: `v[major].[minor].[patch]` — [date]
- **Major**: breaking changes to file structure or skill behaviour
- **Minor**: new skills, significant skill improvements
- **Patch**: small fixes, tone adjustments, copy edits

---

## v0.7.0 — 2026-06-02

### New questionnaires — full framework-map coverage

All six selectable framework maps now have a Q1 questionnaire. Three new consolidated skills (NUM-119 pattern: resume from last stage, write `## Q1 Reading`, offer map refresh, registered in `/setup` Step 8 + `/maps`). Question copy is canonical, ported from the Numina App specs.

- **`/individuation-questionnaire`** (NUM-159) — Jung individuation Q1. 8 questions → primary stage across the 6-stage arc (Unconscious Wholeness, Persona, Shadow, Anima/Animus, Wise Elder, Self). Tie logic: adjacent → later stage, non-adjacent → present both. ASCII arc. App counterpart: NUM-134.
- **`/spiral-dynamics-questionnaire`** (NUM-160) — Spiral Dynamics Q1. 8 questions → center-of-gravity band, then a branched tiebreaker resolves the specific vMeme (Beige–Turquoise). Non-hierarchical framing. ASCII spiral. App counterpart: NUM-131.
- **`/integral-aqal-questionnaire`** (NUM-161) — Integral AQAL Q1. 8 questions → home quadrant (I / It / We / Its). Lines/states/altitude deferred to Q2. ASCII 2×2 grid. App counterpart: NUM-132.

All three shuffle option order and hide the framework labels, scoring by content tag rather than letter position, so a knowledgeable user can't game the result.

### Fixes

- **`/chakra-questionnaire` Q1** — applied the same anti-gaming treatment (mirrors the App's NUM-133): options are now shuffled per question with chakra names hidden, scored by content tag instead of a fixed letter→chakra mapping.

---

## v0.6.0 — 2026-06-02

### Breaking — questionnaire consolidation (NUM-119)

- Consolidated the per-questionnaire skills into **one skill per map**, each running its stages (Q1 → Q2 → Q3) in sequence and resuming wherever the user left off:
  - `/chakras-q1` → **`/chakra-questionnaire`**
  - `/heros-journey-q1` → **`/heros-journey-questionnaire`**
  - `/wounds-q1` → **`/wounds-questionnaire`**
- The old `*-q1` skills were removed. References updated across `/setup`, `/maps`, `CLAUDE.md`, and `README.md`. Existing `## Q1 Reading` sections in map files are still recognised, so completed Q1s carry over.

### New — Q2 stages

- **`/chakra-questionnaire` Q2** (NUM-117) — deeper dive (10-12 min): resolves direction (deficient vs excessive) for each active centre, plus somatic locus and recurring patterns. Raises confidence to medium.
- **`/heros-journey-questionnaire` Q2** (NUM-118) — deeper dive: mentors and allies, the ordeal, what's being released, early signs of transformation, the emerging elixir. Re-marks the arc if the user has moved. Raises confidence to medium.

### Skill improvements

- **Refresh-after-questionnaire** (NUM-115, NUM-116) — after each stage, the questionnaire skills check whether a fuller map already exists and offer to refresh it, merging the new reading with prior readings and harvested notes to raise confidence.
- **`/maps`** — confidence logic now treats a completed Q2 as High; wounds section now draws canonical content from the new framework reference instead of an inline table.
- **`/setup`** (NUM-125) — Wounds questionnaire nudge now explains what the map surfaces (Wounds was already in the map picker and Step 8 proposals as of v0.4.0).

### New content

- **Wounds framework reference** (NUM-121) — canonical 5-wounds × (core fear + protector mask + emotional pattern + shadow + integrated gift) spec, evidence signals, and intensity tiers, at `.claude/skills/wounds-questionnaire/wounds-framework.md`. The Wounds Map and questionnaire both draw from it.
- **Wounds × Chakra cross-map** (NUM-126, Chakra half) — `/maps wounds` now surfaces a `## Cross-map connections` section when the Chakra map also shows signal in the wound's somatic locus (Rejection→Throat, Abandonment→Root, Humiliation→Sacral, Betrayal→Solar plexus, Injustice→Heart). The Enneagram structural layer is left as a documented TODO until an Enneagram map exists.

---

## v0.5.0 — 2026-06-02

### Skill improvements

- **`/setup`** (NUM-156) — Added an optional **personality lens** step (Step 4), placed before the map picker. Asks whether the user wants a personality test to shape how the companion talks with them, offering Enneagram, MBTI, Big Five (OCEAN), DISC, or a clear "I'm not interested" skip. A light free-text follow-up captures their result (richer per-framework prompts and a "find your type" free-test handoff come in NUM-157). The raw selection is saved to `profile.md` under `## Personality`, and a derived `## Personality lens` is written into `voice.md` — collapsing the framework into communication directives (energy, processing, structure, stress pattern) that bias how suggestions are framed (e.g. extraverts get people-facing recommendations, introverts get solitary ones). Skipping stores nothing and leaves `voice.md` unchanged. Subsequent steps renumbered (map picker → Step 5, write → Step 6, /harvest handoff → Step 7, questionnaire proposal → Step 8).
- **`/setup`** (NUM-157) — Made the personality-lens type capture concrete. After the user picks a framework, Step 4 now asks for their specific result with a format example matched to that framework (Enneagram `4w5`, MBTI `INFJ`, Big Five trait levels, DISC `DI`), and always offers an explicit "I don't know my type" option. Choosing it surfaces a free online test for that framework (Truity for Enneagram / Big Five / DISC, 16Personalities for MBTI) with two clean exits — take it now and re-run `/setup`, or skip and add it later. Nothing is stored until a real type exists. Test links live in one editable table in the skill.

---

## v0.4.0 — 2026-05-29

### New skills

- **`/wounds-q1`** (NUM-124) — 7 forced-choice questions resolving to the 1-2 primary wounds most activated right now (Rejection, Abandonment, Humiliation, Betrayal, Injustice). Renders an ASCII pentagon constellation. Entry point into the Wounds Map. Confidence label: rough. 5-8 minutes.
- **`/undigested`** (NUM-154) — Surfaces insights from journals, journeys, and dreams that were clearly recognized but haven't moved into behavior yet. Uses four detection filters: contradiction, repetition, unfollowed intention, and orphaned insight. Output capped at 5-8 items. Closes with one question.

### New maps

- **Wounds Map** (NUM-120, NUM-122, NUM-123) — Constellation of the 5 primary wounds with intensity tiers (Dormant / Stirring / Active / Acute), derived from evidence signals in entries. Each wound rendered with 4 satellite layers: protector mask, emotional pattern, shadow expression, integrated gift. ASCII pentagon layout. Added to `/maps wounds` and to the `/setup` map picker.

### Skill improvements

- **`/maps`** (NUM-114) — All framework maps now include a `**Confidence:**` header (Low / Medium / High) derived from entry count and questionnaire completion status. `**Sources:**` header lists completed questionnaires and approximate entries read. End-of-map prompt added when the relevant questionnaire hasn't been run yet. New `/maps wounds` subcommand.
- **`/setup`** (NUM-112) — Wounds Map added to the map picker (option 6). `/harvest` handoff now explicitly lists JPG and PNG as supported formats for handwritten/scanned notes. New Step 7: after setup, proposes the relevant questionnaire for each selected map that has one (`/chakras-q1`, `/heros-journey-q1`, `/wounds-q1`).
- **`/harvest`** (NUM-113) — Date clarification step added to Step 3: when dates are absent or unclear for the majority of entries, the skill now asks for a time range before falling back to today's date. Never falls back silently.

### Housekeeping

- CLAUDE.md updated: `wounds.md` added to maps file structure, `/wounds-q1` and `/undigested` added to skills table, memory layer note updated.

---

## v0.3.0 — 2026-05-14

### New skills

- **`/chakras-q1`** (NUM-106) — 8 forced-choice questions resolving to the top 1-2 chakras calling for attention right now. Entry point into the Chakras map. Confidence label: rough. 3-5 minutes.
- **`/heros-journey-q1`** (NUM-107) — 8 questions + optional tiebreaker resolving to a rough placement on the 12-stage Hero's Journey arc. Entry point into the Hero's Journey map. Confidence label: rough. 3-5 minutes.

### Skill improvements

- **`/integrate`** (NUM-110) — Now reads context (profile, prior journeys, archetypes, relationships) before holding the container. Fresh and Post phases include a "What you might have missed" tease if the context reading surfaces a pattern the user hasn't named — framed as invitation, skipped if nothing genuine is there.
- **`/setup`** (NUM-109) — After each answer (including the name), a brief conversational response before moving to the next question. 1-2 sentences, specific to what the user said. Makes the flow feel like a dialogue, not a form.
- **`/dream`** (NUM-111) — Archetype file check: before using a file from `context-library/archetypes/`, the skill now verifies it has substantive content. Files with only a stub or placeholder are skipped. Prevents phantom archetypes from shaping the reading.

### Housekeeping

- CLAUDE.md file structure updated to include `chakras.md` in the maps listing.

---

## v0.2.4 — 2026-05-07

### /maps improvements (NUM-104)
- Added Chakras framework map (`context-library/maps/chakras.md`) — 7 chakras, Root to Crown, with activation levels (most active / stirring / quiet) derived from journal, dream, and journey content
- Chakras map renders with an ASCII visual overview first, prose interpretation below — the shape is immediately scannable
- Documented visual format decision: ASCII for spatial maps (default), prose for interpretive maps; Mermaid not recommended for CLI-first use
- `/maps` now reads `## Active maps` from `profile.md` (set by the new /setup map picker) as the primary source for which framework maps to generate; falls back to Q3-based inference for older profiles
- Added `/maps chakras` subcommand
- ASCII legend: ● most active / ◉ stirring / ○ quiet

## v0.2.3 — 2026-05-07

### /dream improvements (NUM-105)
- Added Step 2: ask when the dream happened if not mentioned; falls back to today's date with a note in the file
- Follow-up question is now about "People and inner figures" (who appeared) instead of "feeling on waking" — more analytically useful and feeds the relationships map directly
- File structure updated: `## People and inner figures` now a primary field with role labels (waking-life / dream figure / inner figure / animal / entity)
- Added `## Emotional arc` field — captures how emotion moved through the dream narrative, distinct from waking feeling
- `## Feeling on waking` retained as a secondary field (the residue after waking, often different from in-dream feeling)
- Added live terminal dialog in Step 7: deepening question surfaced in the terminal after filing; user can respond and append to the dream file

## v0.2.2 — 2026-05-07

### /harvest improvements (NUM-102)
- Synthesis now runs automatically after every import — no need to call `/harvest synthesize` separately
- After synthesis, 1-2 strongest patterns and one deepening question surface in the terminal as a live dialog
- User can respond in the terminal; response is optionally appended to the synthesis file
- User can skip the dialog without friction
- `/harvest synthesize` remains available as a standalone command to re-run synthesis at any time

## v0.2.1 — 2026-05-07

### /journal improvements (NUM-103)
- Recurring patterns and the deepening question now surface in the terminal as a live dialog, not only in the saved file
- After asking the question, the skill waits for the user's response in the terminal
- If the user responds, their reply is appended to the journal file under `## Response`
- User can skip the dialog by typing "skip" or moving on — no friction
- File is now stored before the dialog step, so the entry is always captured regardless of whether the user engages

## v0.2.0 — 2026-05-07

### /setup improvements (NUM-101)
- Ask for the user's name or preferred name before the 4 questions; use it throughout the session and save to `profile.md`
- All multi-select options are now numbered so users can respond with numbers instead of retyping text
- Added a dedicated map picker step (Step 4) after the closing reflection — each map shown with a one-line description; user makes an explicit selection
- Universal maps (timeline, relationships, archetypes) noted as always active, no selection needed
- Added Chakras to the map picker (map generation implemented in v0.3.0)
- Added /harvest handoff at the end of setup — explains supported file types and invites bulk import
- `profile.md` updated: new `## Name` field, `## Framework maps to generate` renamed to `## Active maps`

### Versioning
- Added `CHANGELOG.md`
- Added version number to `CLAUDE.md`

---

## v0.1.0 — 2026-04-29

Initial release of Numina OS.

### Skills shipped
- `/setup` — onboarding ritual, profile + voice creation
- `/journal` — journal entry processing
- `/dream` — dream processing and storage
- `/harvest` — bulk import for existing content
- `/maps` — map generation (Hero's Journey, Individuation, Spiral Dynamics, Integral AQAL)
- `/integrate` — journey integration (psychedelic, shamanic, breathwork)
- `/meditation` — meditation sit log
- `/compass` — synthesis and journey diagnosis
- `/inner-review` — weekly inner review

### Infrastructure
- `CLAUDE.md` master context file
- `context-library/` folder structure with `.gitignore` for personal data
- `voice.md` derivation from Q3 + Q4 profile answers
- Memory layer: auto-update for relationships, archetypes, timeline across all skills
- Universal maps: timeline, relationships, archetypes
