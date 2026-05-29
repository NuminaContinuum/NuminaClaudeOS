---
name: undigested
description: Surface insights from journals, journeys, and dreams that were clearly recognized but haven't made it into actual behavior or thinking yet. The gap between knowing and embodying. Run when the user wants to see what's still asking to land.
---

# /undigested — What's still asking to land

This skill finds the gap between knowing and embodying. It reads across everything the user has brought into Numina OS, surfaces insights that were genuinely recognized — named, felt, sometimes revisited — and then quietly not acted on.

This is the most delicate skill in the system. The user is being shown where they're stuck. Move slowly. Use their words, not yours. Frame everything as "still waiting to land," never as failure.

---

## Behaviour

### Step 1 — Check for minimum data

Count files across `context-library/journals/`, `context-library/journeys/`, `context-library/dreams/`, and `context-library/integrations/`.

If fewer than 5 entries total:

> *"There isn't quite enough content yet to find patterns reliably. `/undigested` works best with at least a handful of entries across different sessions — journal entries, journeys, or dreams. Try again after a few more sessions."*

Stop here. Do not fabricate patterns from thin data.

If 5-10 entries, proceed but note the limitation at the top of the output:

> *"Working from a relatively small set of entries — this reading is suggestive, not definitive. Patterns will sharpen with more material."*

---

### Step 2 — Read all content

Read in this order:

1. `context-library/integrations/` — these are the most explicit insight records
2. `context-library/journeys/` — post-journey insights, often named directly
3. `context-library/journals/` — look for explicit realization language (see detection signals below)
4. `context-library/dreams/` — insights flagged as significant by the user
5. `outputs/reflections/` — synthesis outputs from `/harvest`, `/inner-review`, `/compass`

Also read:
- `context-library/archetypes/` — to check if archetype relationships have actually evolved
- `context-library/relationships/` — to check if relational patterns have shifted
- `context-library/maps/timeline.md` — to check whether a named turning point was followed by actual change

---

### Step 3 — Extract candidate insights

Scan for explicit insight language across all content. Phrases to look for:

- "I realized...", "I see now...", "I understand that...", "I noticed..."
- "I need to...", "I want to stop...", "I'm going to...", "From now on..."
- "This showed me...", "What came through was...", "The lesson here is..."
- "I keep repeating...", "I always do this when...", "The pattern is..."
- Any named realization in a journey or integration report (often in a "What I learned" or "Key insights" section)

For each candidate: note the exact phrase (or a close paraphrase in their words), the source file, and the date.

---

### Step 4 — Apply the four detection filters

For each candidate insight, test against these four patterns. An insight qualifies as undigested if it matches **at least one**:

**1. Contradiction**
The insight names a pattern the user wants to change ("I see how I shrink when I need to ask for what I want") — but later entries show the same pattern still playing out without apparent shift. Look for the same behavior or emotional dynamic described after the date of the insight.

**2. Repetition**
The same realization appears across two or more entries that are at least 4 weeks apart, phrased as if it's being recognized for the first or second time. The insight hasn't compounded — it keeps resetting.

**3. Unfollowed intention**
The user named an explicit intention or commitment with no follow-up. No later entries reflect on it, reference it, or show evidence of change in that area. The intention was set down and walked away from.

**4. Orphaned insight**
A powerful realization appeared once — in a ceremony, a deep dream, a breathwork journey — and was never revisited. The archetype or relationship it touched has not evolved in the record files since. It arrived, and then nothing.

Discard candidates that don't match any of the four. Also discard insights where there IS evidence of integration — where later entries show the pattern named in the insight has genuinely shifted, even partially.

---

### Step 5 — Select and rank

From the filtered list, select the 5-8 most significant items. Prioritize:

- Insights that match multiple detection filters (e.g., both Repetition and Contradiction)
- Insights connected to the most frequently activated archetypes or wounds
- Insights from journeys or ceremonies (tend to carry more weight)
- Insights that are most recent in their last appearance (still warm)

Do not present more than 8. If you have more, surface the ones with the clearest evidence. A short list with strong evidence is more useful than a long list with weak connections.

---

### Step 6 — Render the output

Open with a single-line frame. Something like:

> *"Here's what seems to still be asking to land — insights that arrived clearly, but haven't quite moved into how you act or think yet. No urgency. These are just the ones that keep circling."*

Then present each item:

```
**"[The insight, as close to the user's own words as possible]"**
First named: [YYYY-MM-DD] — [source filename]
Still showing up as: [the contradicting or repeating pattern, with one concrete example and date]
```

Keep each entry tight. Two to three lines maximum. The evidence should be specific — a date, a quote, a file reference. Not "you often mention this" — "on 2024-08-14 you wrote: '[quote].'"

After all items, one closing question. Grounded in the most significant pattern. Something that opens rather than directs:

Example:
> *"What would it take for the knowing to actually move — from here [gesture to the list] to how you act on an ordinary Tuesday?"*

Or, more specific to their content:
> *"The grief about your father has appeared in your writing seven times over three years. What do you think it's still waiting for?"*

---

### Step 7 — Offer to save

After the terminal output:

> *"Want me to save this to `outputs/reflections/YYYY-MM-DD-undigested.md`?"*

If yes, write the file with the full output including the closing question. Add a brief frontmatter header:

```markdown
# Undigested — YYYY-MM-DD

**Entries read:** [N journals, N journeys, N dreams, N integrations]
**Items surfaced:** [N]
**Detection patterns found:** [list which of the 4 were used]

---

[Full output]
```

If no, accept without comment.

---

### Step 8 — Optional: mark as integrated

If the user wants to flag any item as integrated (to exclude from future runs), offer:

> *"If any of these have actually shifted and I missed it, you can add a note in the source file — a line like `## Integration note — [date]: [what changed]`. I'll pick that up next time."*

Do not create a separate tracking file. Keep the record in the source files themselves.

---

## Detection edge cases

**Ambiguous shift:** if there's partial evidence of integration (the pattern appears less frequently in recent entries, or the user mentions "I'm getting better at this"), do not include the item. Only surface what is clearly still undigested — not what is in slow movement.

**Sparse date information:** if entries lack clear dates, use file creation order as a proxy. Note the uncertainty explicitly when citing evidence.

**Contradictory entries about the same insight:** if an insight appears "understood" in one entry but "forgotten again" in a later one, it qualifies under Repetition. Cite both entries.

**Private material the user flagged:** respect any `<!-- don't store -->` or explicit "don't write this down" notes. Do not surface insights from sections the user asked not to be remembered.

---

## Acceptance criteria

- [ ] Minimum data check runs first — skill halts gracefully with fewer than 5 entries
- [ ] Reads journals, journeys, integrations, dreams, and reflection outputs
- [ ] Cross-references archetypes, relationships, and timeline for evidence of actual shift
- [ ] Applies all four detection filters (contradiction, repetition, unfollowed intention, orphaned)
- [ ] Discards candidates with evidence of integration
- [ ] Output capped at 5-8 items, prioritized by signal strength
- [ ] Each item uses the user's own words, cites source file and date
- [ ] Each item names the contradicting or repeating pattern with one concrete example
- [ ] Closing question is one sentence — opens, does not direct
- [ ] Offers to save to `outputs/reflections/YYYY-MM-DD-undigested.md`
- [ ] Explains how to mark something as integrated (note in source file)
- [ ] Sparse data (5-10 entries) acknowledged at the top of output

---

## Tone reminders

- This is the most tender skill in the system. The user is looking at where they haven't changed yet. Hold that with care.
- Use their words. Do not translate "I always abandon myself in conflict" into "you exhibit a pattern of self-abandonment." Read it back as they wrote it.
- "Still asking to land" — not "unresolved," "incomplete," or "failed."
- No ranking, no urgency, no hierarchy. Five items are not worse than three. All are equal.
- The closing question is the most important sentence in the output. Spend the attention there. One good question is worth more than all the analysis.
- If the data is thin, say so. Do not reach for patterns that aren't clearly there.
