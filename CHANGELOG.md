# Changelog

All notable changes to Numina OS are documented here.

Format: `v[major].[minor].[patch]` — [date]
- **Major**: breaking changes to file structure or skill behaviour
- **Minor**: new skills, significant skill improvements
- **Patch**: small fixes, tone adjustments, copy edits

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
