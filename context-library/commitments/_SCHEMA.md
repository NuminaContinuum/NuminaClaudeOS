# Commitment File Schema

> **Read this before writing or editing a commitment file.** The PostToolUse hook
> rejects commitment files where any `## Evidence` row lacks a provenance tag
> from the enum in [`../PROVENANCE.md`](../PROVENANCE.md).
>
> **Pre-save self-check (run mentally before every write):**
> 1. **COUNT-THE-TAGS.** Count bullet rows under `## Evidence`. Count provenance tags.
>    The two numbers must match.
> 2. Path-typed tags are markdown links, not prose.
> 3. `## Status` is one of `active | paused | released | superseded`.
> 4. `## What would change this` is present and **specific and observable** — a felt shift,
>    a milestone, a date, a condition. Not "if things change."

Filename: `<slug>.md` in `context-library/commitments/`. Update `INDEX.md` in the same turn.

```markdown
# Commitment — [name]

## Status
active | paused | released | superseded

## Date
YYYY-MM-DD

## What it is
[The practice, intention, or values-affirmed choice — in plain language.
One or two sentences. Your words, not a technique name.]

## Why it matters
[What prompted this. The moment, pattern, or realisation it responded to.
Link to a pattern file if one exists.]

## Evidence
<!-- HARD RULE: every row ends with one provenance tag. Examples:
  - Three consecutive mornings I felt the pull toward this   (lived-experience, 2026-05-14)
  - The wolf dream marked the beginning of this commitment   (dream, 2026-04-12)
  - Body said yes before mind did   (somatic, 2026-05-14)
-->
- <claim>  `<provenance-tag>`

## What would change this
[The observable condition under which this commitment would be revisited, paused,
or released. Be specific — a felt shift, a named milestone, or a date.]

## Integration notes
[How it's actually going. Append over time — one dated line per check-in.
Empty until something worth noting happens.]

## Linked
- Pattern: `../patterns/<slug>.md`
```

## Rules

- Commitments are chosen by the user, not promoted automatically.
- Status `released` means the practice has run its course and is complete — a good ending.
- Status `superseded` means a newer commitment replaced this one — link to the new file.
- Append to `## Integration notes` rather than overwriting.
- `/sweep` checks commitments with no integration notes in 30+ days.
