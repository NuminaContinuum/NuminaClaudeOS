# Provenance — the vocabulary the inner work brain enforces

Every load-bearing claim in `patterns/` and `commitments/` wears a provenance tag. A claim is load-bearing when it drives a pattern or commitment: evidence rows, integration notes, anything under `## Evidence for` or `## Evidence against`.

The hook enforces the vocabulary, not the workflow. Real inner work is messy — you have intuitions, body sensations, fragments from dreams you can't fully remember. Those are legitimate inputs. The brain just makes them wear their actual provenance rather than hiding behind untagged assertions.

The auditability promise is "every claim wears its source," not "every claim is perfectly remembered." A missing tag is the only bug.

## The enum

| Tag | Means | Trust weight |
|---|---|---|
| `[ingestion/<path>](<relative-path>)` | Went through synthesis. The ingestion file links back to a `source/` artifact. | Highest |
| `[source/<path>](<relative-path>)` | Direct citation to a raw entry. Use when the source is self-explanatory. | High |
| `(lived-experience, YYYY-MM-DD)` | Directly described in a journal, journey, or meditation entry. | High |
| `(dream, YYYY-MM-DD)` | From dream content — hold symbolically, not literally. | Medium — symbolic layer |
| `(somatic, YYYY-MM-DD)` | Body-felt sense noted explicitly in an entry. | High — hard to fabricate |
| `(reflection, YYYY-MM-DD)` | Interpreted or inferred in journaling (not direct experience). | Medium — interpretive |
| `(pattern, N-occurrences)` | Observed across 3+ independent entries across different modalities. | Highest — the gold standard |
| `(teacher-text, source-name)` | Teaching, book, or conversation with a guide or therapist. | Low-medium — external frame |
| `(intuition, YYYY-MM-DD)` | Felt sense, no external anchor, not yet in a written entry. | Low externally, valid internally |

## Rules the hook enforces

1. **Path-typed tags** (`[ingestion/...]`, `[source/...]`) must be working markdown links to files that exist under the top-level pipeline `source/` or `ingestion/`. A link that doesn't resolve yet is a warning, not a block — write the source file or downgrade the tag.
2. **Non-path-typed tags** must match one of the parenthetical forms exactly. Don't invent new categories silently.
3. **A row with no tag is an orphan claim** and is rejected at write time by the PostToolUse hook — but only in `patterns/` and `commitments/` files.

## Dreams are symbolic — a note on trust weight

`(dream, date)` is a first-class provenance type, but claims sourced from dreams carry a symbolic weight, not a literal one. A dream in which your father ignores you is not evidence that your father ignores you. It is evidence that this image is alive in your inner world on that date. Write what the dream showed; hold the interpretation in the `## Open observations` section until it recurs across other modalities.

A single dream does not promote a pattern. It adds evidence.

## What "row" means

The unit the hook audits is the logical list item under an `## Evidence for`, `## Evidence against`, or `## Evidence` section. A provenance tag may sit anywhere in that item — on the bullet line, a wrapped continuation, or a child bullet — so a multi-line sourced claim is never a false orphan.

The hook audits list rows, not free prose. Claims written as bare paragraphs under `## Evidence` are not scanned. Write claims as bullets so each one wears its source.
