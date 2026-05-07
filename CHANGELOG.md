# Changelog

All notable changes to Numina OS are documented here.

Format: `v[major].[minor].[patch]` — [date]
- **Major**: breaking changes to file structure or skill behaviour
- **Minor**: new skills, significant skill improvements
- **Patch**: small fixes, tone adjustments, copy edits

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
