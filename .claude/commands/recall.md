# /recall

Read-only query across the inner work brain. Ask anything about your own material and receive an answer with citations to the files behind every claim.

---

## Input

A natural-language question:
- "What have I noticed about [symbol] across my entries?"
- "How has my relationship with [person] appeared in my dreams?"
- "What patterns are currently active?"
- "What do I know about my fear of [X] before I go into this session?"
- "When did [theme] first appear?"

---

## What it does (read-only — writes nothing)

1. Start at the most relevant area. For a symbol → `context-library/archetypes/`; a person → `context-library/relationships/`; a named pattern → `context-library/patterns/`; a commitment → `context-library/commitments/`; a timeline question → `context-library/maps/timeline.md`.

2. Read the canonical files, following links into `ingestion/` and `source/` for any claim that matters.

3. Synthesise an answer. **Cite the file behind every load-bearing claim** — e.g. `[archetypes/wolf.md]`, `[dreams/2026-04-12-threshold.md]`. The reader should be able to trace any sentence back to its source.

4. **Label the knowledge type of each citation.** A dream entry is symbolic — not literal. A journal reflection is interpretive. A directly experienced entry is observation. The reader needs to know which is which.

---

## Surfaces

- The answer, with inline file citations and knowledge-type labels.
- A **gap notice** when the brain doesn't have it: say so plainly and name what would fill the gap ("no meditation entries mentioning this figure — closest is [dream entry]").

Do not synthesise confident answers from thin air. If the evidence is thin, say so.

---

## Note

`/recall` never promotes or edits. If the answer surfaces something worth keeping, that's a `/capture` (as an adhoc note) or a `/sweep` promotion — not a silent write during a read.
