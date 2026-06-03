# Pattern File Schema

> **Read this before writing or editing a pattern file.** The PostToolUse hook
> rejects pattern files where any `## Evidence for` or `## Evidence against` row
> lacks a provenance tag from the enum in [`../PROVENANCE.md`](../PROVENANCE.md).
>
> **Pre-save self-check (run mentally before every write):**
> 1. **COUNT-THE-TAGS.** Count bullet rows under `## Evidence for` and `## Evidence against`.
>    Count provenance tags. The two numbers must match. 4 rows + 2 tags = 2 orphans — add
>    tags or move the bullets to `## Open observations`.
> 2. Path-typed tags are markdown links (`[ingestion/...](../ingestion/...)`), not prose.
> 3. Each path-typed link resolves from THIS file (`patterns/<file>.md`) — i.e.
>    `../ingestion/<rest>` or `../source/<rest>` (one `..`).
> 4. `## Status` is one of `emerging | active | integrated | dormant`.
> 5. `## Category` is one of `shadow | integration-gap | growth-edge | relational | archetypal`.
>
> Claims about what a pattern *means* belong under `## Open observations`, not under Evidence.
> Evidence rows are what the world (your entries, your body, your practice) showed you — not
> what you infer from it.

Filename: `<slug>.md` in `context-library/patterns/`. Update `INDEX.md` in the same turn.

```markdown
# Pattern — [name in your own words]

## Meta
- Category: shadow | integration-gap | growth-edge | relational | archetypal
- Status: emerging | active | integrated | dormant
- First noted: YYYY-MM-DD
- Last updated: YYYY-MM-DD

## What it is
[One paragraph in your own language. Not a diagnosis. A description of what keeps
appearing or what you've noticed. Hold it as a hypothesis, not a verdict.]

## Evidence for
<!-- HARD RULE: every row ends with one provenance tag. Examples:
  - The wolf figure appeared at the threshold again   (dream, 2026-04-12)
  - Chest tightness when I speak in groups   (somatic, 2026-03-29)
  - Third time this month I've avoided the conversation   (lived-experience, 2026-05-01)
  - Recurring across 4 sessions across dreams and journaling   (pattern, 4-occurrences)
-->
- <claim>  `<provenance-tag>`

## Evidence against / contradictions
<!-- Same provenance-tag requirement. Minority signals preserved, not flattened. -->
- <claim>  `<provenance-tag>`

## Open observations
[What we don't know yet. Interpretations, inferences, things not yet established.
No tags needed here — by construction these are things not yet anchored.
"What does this mean?" lives here, not under Evidence.]

## Related entries
- YYYY-MM-DD — [source file path] — one-line note

## Integration check
[Has this pattern moved? What shifted? Empty until something changes.
Append notes over time rather than overwriting.]
```

## Rules

- Patterns are always user-confirmed. The companion proposes; you decide.
- When a pattern is `promoted`, update this file's status and link to a `commitments/` file if a practice follows.
- Status `integrated` means the pattern is understood and no longer driving unconsciously — keep the file as a record.
- Status `dormant` means it hasn't appeared in 60+ days — flag for `/sweep`, don't delete.
- Patterns are append-only in spirit. To revise understanding, add to `## Open observations` and update `## What it is` — don't erase prior evidence.
- One file per named pattern. If two patterns merge in understanding, note the merger in both files.
