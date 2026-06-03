# /capture

Routes raw material that doesn't fit the main skills into the brain. Use this for anything that arrived outside a session: a voice memo pasted as text, a paragraph from a book that landed differently today, a conversation with a teacher, a somatic note you want to preserve, or a bulk import.

The main skills (`/journal`, `/dream`, `/integrate`, `/meditation`) already do source capture and ingestion as they run. `/capture` is the catch-all for everything else.

---

## Input

Paste the raw content directly, or describe what you have and let the companion ask for it. Infer the shape:

- **dream** — a dream, even a fragment
- **journal** — written reflection or free prose
- **journey** — a shamanic, psychedelic, breathwork, or ceremony experience
- **meditation** — a sit with observations
- **adhoc** — anything else (book passage, teacher note, somatic observation, voice memo)

If the shape is ambiguous, ask once. Don't guess.

---

## What it does

1. **Copy verbatim** → `context-library/source/<shape>/YYYY-MM-DD-<slug>.md`. Immutable from here. The raw content is never edited after creation.

2. **Synthesise** → `context-library/ingestion/<shape>/YYYY-MM-DD-<slug>.md`. Extract themes, figures, symbols, emotional arc. Tag each observation with its knowledge type (observation, symbolic, interpretive, felt-sense).

3. **Surface promotion candidates** — if the content touches an active pattern or crosses the bar (3+ modalities, or the user flags it as significant), name it. Always ask before promoting anything to `patterns/` or `commitments/`.

4. **Auto-update the memory layer** — for any person named, create or append `context-library/relationships/<name>.md`. For any recurring symbol or archetype, create or append `context-library/archetypes/<name>.md`. For any milestone or turning point, append to `context-library/maps/timeline.md`.

---

## Surfaces (brief — the value is in the files)

- Where it landed (source, ingestion, any durable destinations)
- 1-3 themes or figures noticed
- Any pattern touchpoint ("this is the third time water has appeared — twice in dreams, now here")
- One open question if relevant
- Whether anything crosses the promotion bar, with an explicit ask

---

## Note

`/capture` never promotes silently. If something looks like it belongs in `patterns/` or `commitments/`, it surfaces the candidate and asks. "No" is always fine.
