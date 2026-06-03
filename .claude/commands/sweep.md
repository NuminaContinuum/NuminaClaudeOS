# /sweep

The longer maintenance arc — run monthly or seasonally. Goes deeper than `/inner-review` (which covers the past 7 days) by looking at what's accumulated, what's stale, what's ready to move, and what the log holds that hasn't been synthesised yet.

Memory systems fail at month three because nothing sweeps. This is the most important operation in the layer.

---

## Input

None, or a scope to run one check:

```
/sweep                    → all six checks
/sweep patterns           → check 1 only (stale patterns)
/sweep commitments        → check 2 only (integration check)
/sweep archetypes         → check 3 only (symbol evolution)
/sweep relationships      → check 4 only (relationship arcs)
/sweep compress           → check 5 only (knowledge compression)
/sweep logs               → check 6 only (unsynthesised log entries)
```

---

## Loads

- `context-library/CLAUDE.md` memory layer section (promotion bar, evidence hierarchy, escalation rules)
- All durable areas in scope: `patterns/`, `commitments/`, `archetypes/`, `relationships/`, `maps/`
- Recent `ingestion/` for promotion candidates
- `maintenance/` — last 2 sweep reports to compare deltas

---

## The six checks

**1. Stale patterns**
Active patterns with no new evidence in 60+ days. Still relevant, dormant, or dissolved? Flag each one. Do not auto-change status — surface and ask.

**2. Integration check**
Commitments with no integration notes in 30+ days. Still alive and being practiced? Paused without being named as such? Surface for review.

**3. Symbol evolution**
Archetype files where the relationship descriptor (fear / attraction / projection / integration / embodiment) may have shifted based on recent entries but hasn't been updated. Compare recent dream and journal entries against the archetype file.

**4. Relationship arcs**
People or figures not mentioned in 60+ days — still relevant? Any relationship that feels stuck or unresolved across multiple entries. Surface the arc.

**5. Knowledge compression**
Recurring themes in `ingestion/` across multiple entries that are ready to become a named pattern. Always ask before promoting. Minority signals preserved — don't flatten contradictions.

**6. Log review**
Entries in `journals/`, `dreams/`, `meditations/`, `journeys/` that were captured but never fully synthesised into `ingestion/` — either because the terminal dialog was skipped, or because entries came in via `/harvest` and weren't processed. Surface the backlog. Route unsynthesised entries one at a time, or in a batch if the user prefers.

---

## Does

- Write the dated report → `context-library/maintenance/YYYY-MM-DD-sweep.md`
- **Edit directly** where confidence is high: update last-mentioned dates, compress duplicate ingestion entries, flag dormant patterns.
- **Draft, don't commit** what needs judgment: pattern promotions, commitment reviews, archetype re-reads, log synthesis.

## Surfacing drift

When recent entries contradict a promoted pattern or an active commitment, name the **specific** contradicting signals with dates and links — not "the original premise no longer holds." The artifact is still valid (that entry really happened) but the *claim* it supported may no longer match. Surface it, don't resolve it.
