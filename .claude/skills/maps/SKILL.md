---
name: maps
description: Generate or refresh the living maps from accumulated context. Universal maps (timeline, relationships, archetypes) for everyone. Framework maps (Hero's Journey, Individuation, Spiral Dynamics, Integral AQAL, Chakras) based on the active maps selected in /setup. Maps use ASCII visualizations where spatial layouts help. Subcommands for granular refresh.
---

# /maps — Cartography

Maps are the synthesis layer. The records (in `relationships/`, `archetypes/`, `journals/`, etc.) hold the detail. The maps hold the view.

The detail lives in the individual files. The maps are summaries built from them. Maps go stale; records do not.

---

## Usage

```
/maps                     → refresh all maps (universal + active framework maps)
/maps universal           → refresh only universal maps
/maps frameworks          → refresh only framework maps
/maps timeline            → refresh just timeline.md
/maps relationships       → refresh just relationships.md
/maps archetypes          → refresh just archetypes.md
/maps heros-journey       → refresh just heros-journey.md
/maps individuation       → refresh just individuation.md
/maps spiral-dynamics     → refresh just spiral-dynamics.md
/maps integral-aqal       → refresh just integral-aqal.md
/maps chakras             → refresh just chakras.md
/maps wounds              → refresh just wounds.md
```

---

## On visual format

Maps are `.md` files, but that does not mean they have to read like tables. Where spatial layout helps, use ASCII diagrams — they render cleanly in the terminal, in VS Code, in Obsidian, and anywhere markdown is displayed. No dependencies, no friction.

**Use ASCII when:** the map has a natural shape (a vertical axis, a wheel, a timeline arc). Chakras, for example, are a vertical energy column — an ASCII column communicates that instantly. The Hero's Journey is a loop — a simple arc sketch can orient the user before they read the prose.

**Use prose when:** the map is interpretive rather than positional. Individuation, AQAL, and Spiral Dynamics are better served by carefully qualified paragraphs than by forced diagrams.

**Do not use Mermaid for framework maps.** It requires a renderer (VS Code, Obsidian, GitHub) and adds friction in a CLI-first tool. Mermaid works for timeline flows if the user has a renderer — offer it only if they ask.

Default: **ASCII for spatial maps, prose for interpretive maps.**

---

## Behaviour

### Step 1 — Read the profile

Open `context-library/profile.md` and extract:

- **`## Active maps`** — the framework maps the user explicitly selected in `/setup`. This is the primary source.
- If `## Active maps` doesn't exist (profile created before v0.2.0), fall back to inferring from `## Frameworks` using the mapping table below.
- The user's language and inspirations → tone and framing for narrative writing in the maps.

If `profile.md` doesn't exist, gently say: *"`/maps` works best after `/setup` — it tells me which maps you're working with. Want to run `/setup` first?"* Then offer to generate universal maps only if they say to proceed.

### Step 2 — Determine which maps to refresh

Default `/maps` (no subcommand) refreshes:

- All three universal maps: `timeline.md`, `relationships.md`, `archetypes.md`
- Framework maps listed under `## Active maps` in `profile.md`

**Fallback mapping (for profiles without `## Active maps`):**

| Framework selection | Maps generated |
|---|---|
| Depth psychology | individuation.md, heros-journey.md |
| Mystical traditions | heros-journey.md |
| Integral theory | integral-aqal.md, spiral-dynamics.md |
| IFS / somatic / trauma-informed | wounds.md |
| Mindfulness and Buddhism | (v2 — Finding the Ox, 16 Insight Knowledges; not yet) |
| All others | (v2) |

If a selection has no v1 framework map yet, mention it briefly: *"Shamanism is in your profile — the matching maps are v2 and need richer journey data. They'll come."*

### Step 2.5 — Compute confidence for framework maps

Before generating each framework map, derive a confidence level to show in the header. Do this for every framework map (not universal maps).

**Confidence logic:**

| Condition | Confidence |
|---|---|
| No relevant Q1 completed AND fewer than 5 content entries | Low |
| Q1 completed OR 5+ relevant content entries | Medium |
| (Q1 completed AND 15+ relevant content entries) OR Q2 completed | High |

**How to detect questionnaire completion:** check the map file for `## Q1 Reading` and `## Q2 Reading` sections. Q1 present = quick read done; Q2 present = deeper dive done (chakra and hero's-journey maps), which on its own justifies High confidence.

**Content entry count:** count files in `context-library/journals/`, `dreams/`, `journeys/`, and `meditations/` combined (not per-map — all content feeds all maps).

**Questionnaire mapping (for the "Sources" header and end-of-map prompt):**

| Map | Questionnaire |
|---|---|
| heros-journey.md | `/heros-journey-questionnaire` |
| chakras.md | `/chakra-questionnaire` |
| wounds.md | `/wounds-questionnaire` |
| individuation.md | `/individuation-questionnaire` |
| spiral-dynamics.md | `/spiral-dynamics-questionnaire` |
| integral-aqal.md | `/integral-aqal-questionnaire` |

**Header format for all framework maps** (add these two lines below `**Held as:**`):

```
**Confidence:** Low / Medium / High
**Sources:** [e.g., "heros-journey-questionnaire Q1 completed 2025-05-10, 18 entries read" — or "no questionnaire yet, 6 entries read"]
```

**End-of-map prompt:** if the relevant questionnaire has NOT been run (no `## Q1 Reading` in the file), append this line at the very end of the map output:

> *Run `/[questionnaire]` to add a structured self-assessment and increase confidence.*

If the map has no questionnaire yet, omit this prompt.

---

### Step 3 — Generate each map

#### Universal maps

**`context-library/maps/timeline.md`**

Mostly already maintained by content skills. Your job in `/maps`:

- Read all entries in `context-library/maps/timeline.md`
- Sort chronologically (the file should be append-only but may have gotten out of order)
- Group by year if 20+ entries exist; ungrouped otherwise
- Add a "last updated" timestamp at the top

Format:

```markdown
# Timeline

**Last updated:** YYYY-MM-DD

## 2024
2024-09-12 | initiation | First long retreat — silent, 10 days | journeys/2024-09-12-vipassana-retreat.md
2024-06-04 | insight | Realised the resentment toward dad was actually grief | journals/2024-06-04-grief-not-anger.md

## 2023
[older entries]
```

**`context-library/maps/relationships.md`**

Read all files in `context-library/relationships/`. Synthesize a grouped overview.

Format:

```markdown
# Relationship map

**Last updated:** YYYY-MM-DD

## Family
- **[Name]** — [N mentions] — [emotional valence]. [One-line of the recurring theme.]

## Friends
- **[Name]** — [N mentions] — [valence]. [Theme.]

## Teachers and guides
- **[Name]** — [N mentions] — [valence]. [Theme.]

## Inner figures
- **[Name]** — [N mentions in dreams/journeys] — [valence]. [Theme.]
```

Group by role. Within each group, sort by mention frequency descending.

If `context-library/relationships/` is empty, write a placeholder noting that people mentioned in entries will be added automatically.

**`context-library/maps/archetypes.md`**

Read all files in `context-library/archetypes/`. Synthesize a frequency-ordered overview.

Format:

```markdown
# Archetype and symbol map

**Last updated:** YYYY-MM-DD

## Most frequent
- **[Name]** — [N appearances since YYYY-MM-DD] — [relationship descriptor]. [One-line description.]

## Recently emerged
- **[Name]** — [N appearances] — [descriptor]. First appeared [date].

## Evolving
- **[Name]** — [N appearances]. [Note on how the relationship has shifted.]
```

Group: most-frequent (top 5-10), recently emerged (first appearance in past 60 days), evolving (relationship descriptor has changed).

---

#### Framework maps

The framework maps are interpretive. Each one places the user *somewhere* on a developmental or narrative model — held as a hypothesis, with evidence.

**Critical:** Do not over-certify. Use *"appears to be"*, *"a center of gravity around"*, *"recent entries suggest"*. Never *"you are at"*, *"you have completed"*, or *"you are in stage X"*.

For each framework map, read across `journals/`, `dreams/`, `journeys/`, `meditations/`.

---

**`context-library/maps/heros-journey.md`** — Campbell's narrative arc

Stages: Ordinary World → Call to Adventure → Refusal of Call → Meeting the Mentor → Crossing the Threshold → Tests, Allies, Enemies → Approach to the Inmost Cave → Ordeal → Reward → The Road Back → Resurrection → Return with the Elixir.

Format:

```markdown
# Hero's Journey

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict

## Where you appear to be
**[Stage name]** — [one-paragraph rationale, with 2-3 evidence quotes with date references]

## What's behind you
[The stages they've passed through, with one example each]

## What may be ahead
[The next stage, framed as possibility — what it tends to look like, what to watch for]

## Open question
[One question worth sitting with about where they are in the arc]
```

---

**`context-library/maps/individuation.md`** — Jungian stages

Stages: Persona → Shadow → Anima/Animus → Self.

Same format as Hero's Journey. Look for evidence of shadow work, anima/animus encounters in dreams, Self-symbol emergence (mandalas, golden child, wise old figure, totality images).

---

**`context-library/maps/spiral-dynamics.md`** — Center of gravity

Tiers: Beige → Purple → Red → Blue → Orange → Green → Yellow → Turquoise.

Look for value-system markers in writing: tribal loyalty, individual achievement, communitarian values, systems thinking, integration. Frame as *"a center of gravity around [tier]"* — people are weighted distributions, not single tiers.

---

**`context-library/maps/integral-aqal.md`** — Wilber's AQAL

Quadrants: I (interior individual), We (interior collective), It (exterior individual), Its (exterior collective).
Levels: Pre-personal → Personal → Trans-personal.
Lines: Cognitive, emotional, moral, interpersonal, spiritual, somatic.
States: Gross, subtle, causal, witness, non-dual.

Most complex framework. Comment only on what the user's content gives you evidence for. If entries are all I-quadrant introspection, say so.

---

**`context-library/maps/chakras.md`** — Energy body map

The 7 chakras, Root to Crown. This map reads across all entries and identifies which centres appear most actively — in recurring themes, body sensations, dream imagery, practice experiences, and language patterns. Held as invitation to awareness, not diagnosis.

Chakras and their territory:

| Chakra | Sanskrit | Territory |
|---|---|---|
| 1. Root | Muladhara | Safety, belonging, body, survival, grounding |
| 2. Sacral | Svadhisthana | Pleasure, creativity, sexuality, flow, emotion |
| 3. Solar Plexus | Manipura | Power, will, identity, agency, shame |
| 4. Heart | Anahata | Love, grief, connection, compassion, loss |
| 5. Throat | Vishuddha | Expression, truth, voice, speaking/silence |
| 6. Third Eye | Ajna | Intuition, vision, clarity, pattern-recognition |
| 7. Crown | Sahasrara | Transcendence, unity, surrender, dissolution |

For each chakra, read across all content for signals: recurring themes (e.g. powerlessness → solar plexus), body imagery in dreams (e.g. throat tightening), emotional patterns, what the user explicitly names, what's notably absent.

Assign one of three activation levels:
- **most active** — the territory appears frequently, emotionally charged, or is explicitly named
- **stirring** — present but not central; beginning to be worked
- **quiet** — little to no signal in the content

**Render the map as an ASCII diagram first**, then add prose interpretation below.

Format:

```markdown
# Chakra map

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of attention, not a diagnosis

## Visual overview

    7  Crown (Sahasrara)       ○  quiet
    6  Third Eye (Ajna)        ◉  stirring
    5  Throat (Vishuddha)      ○  quiet
    4  Heart (Anahata)         ●  most active
    3  Solar Plexus (Manipura) ◉  stirring
    2  Sacral (Svadhisthana)   ●  most active
    1  Root (Muladhara)        ○  quiet

    ●  most active    ◉  stirring    ○  quiet

## What's calling for attention

**[Chakra name]** — [one paragraph: what signals in the entries point here, with 1-2 specific quotes or date references. Held lightly.]

**[Second chakra if relevant]** — [same format]

## What's quiet

[Brief note on which centres show little signal — may be integrated, may be less visible in the data. Acknowledge both possibilities.]

## One question

[A single question worth sitting with — related to the most active centre or to an interesting contrast between active and quiet areas]
```

The ASCII overview renders immediately on opening the file. It's scannable in two seconds. The prose below gives the rationale. Together they give the user both the shape and the reasoning.

---

**`context-library/maps/wounds.md`** — Primary wounds constellation

The 5 primary wounds: Rejection, Abandonment, Humiliation, Betrayal, Injustice. This map shows which wounds are most activated right now — as dynamic states with intensity, not fixed identity labels. Do not reference source frameworks by name in the output. Frame for audiences drawn to IFS, shadow work, depth psychology, and Jungian work.

**Each wound has 4 layers:**
- **Protector mask** — the defensive pattern that formed to protect the wound
- **Emotional pattern** — signature feelings and relational behavior when activated
- **Shadow expression** — what gets disowned when the wound is unexamined
- **Integrated gift** — what becomes possible once integrated

**Canonical content reference:** the full 5-wounds × (core fear + 4 layers) spec, the evidence signals per wound, and the wound→chakra somatic locus all live in `.claude/skills/wounds-questionnaire/wounds-framework.md`. Draw from it as reference, not script — match the tone and emphasis to what's actually activated for this user, in their language. Never quote the layers verbatim. Dormant wounds still show all four layers, rendered dimly with a note that no strong signal has been detected yet.

**Intensity tiers (derived from evidence in entries):**

- **Dormant (○):** No signal. Node shown faint.
- **Stirring (◉):** Some signal — mild patterns surfacing.
- **Active (●):** Clear recurring patterns in recent entries.
- **Acute (●●):** Strong, repeated signal across multiple entries or a significant recent event.

Be selective. Most wounds are Dormant or Stirring for most people most of the time. Only elevate to Active or Acute when there is clear, repeated evidence across multiple entries.

**Render the map as an ASCII pentagon constellation first**, then add prose below.

Format:

```markdown
# Wounds Map

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of activation, not identity
**Confidence:** Low / Medium / High
**Sources:** [e.g., wounds-questionnaire Q1 completed YYYY-MM-DD, 14 entries read]

## Constellation overview

                    REJECTION
                   [◉ stirring]

    BETRAYAL                      ABANDONMENT
    [○ dormant]                   [● active]

    INJUSTICE            HUMILIATION
    [◉ stirring]         [○ dormant]

    ●  active    ◉  stirring    ○  dormant

## What's calling for attention

### [Most activated wound] — [intensity]

**Protector mask:** [specific expression in this user's content]
**Emotional pattern:** [specific patterns from their writing]
**Shadow expression:** [what's being disowned — hold lightly]
**Integrated gift:** [what integration could open — frame as potential, not prescription]

*Evidence: [1-2 specific quotes with date references from entries]*

### [Second wound if Active or Stirring] — [intensity]

[Same structure]

## What's quiet

**[Dormant wound]** — Little signal in current content. May be integrated, less present in life right now, or simply less visible in what's been shared.

[One line per dormant wound]

## Cross-map connections

[Only present when the Chakra map also exists and both maps show signal in corresponding nodes — see cross-map rules below. Omit this whole section otherwise.]

## One question

[One question grounded in what's actually activated — not a generic wound question]
```

**Cross-map connections (NUM-126):**

Surface these only as genuine synthesis, never as noise. The rule: include the `## Cross-map connections` section **only when** `context-library/maps/chakras.md` exists AND the wound that's active here maps (via the somatic locus table in `wounds-framework.md`) to a chakra that is *also* flagged active or stirring in the Chakra map. If there's no overlap of signal, omit the section entirely.

Somatic locus (full table in `wounds-framework.md`): Rejection→Throat, Abandonment→Root, Humiliation→Sacral, Betrayal→Solar plexus, Injustice→Heart.

When the overlap exists, write one or two lines, held lightly:

> *Your abandonment wound and your root chakra are both showing signal this month — the body may be carrying the same theme of safety and belonging that's surfacing in your relationships.*

**Enneagram structural layer — not yet built.** NUM-126 also calls for a structural cross-map with the Enneagram (e.g. "Type 4 patterning tends to activate through the rejection wound"). This requires an Enneagram map, which does not exist yet. Do not generate Enneagram cross-map insights until that map is built. Tracked as a TODO in NUM-126.

---

### Step 4 — Handle empty state

If `context-library/` has fewer than 3 entries across all content types:

> *"There's not enough yet to build maps from. Try `/journal`, `/dream`, or `/harvest` first — `/maps` will be more useful with at least a handful of entries."*

If only some maps have data, generate the ones that do and note the empty ones.

### Step 5 — Timestamps

Every map file starts with `**Last updated:** YYYY-MM-DD`. Update this on every refresh.

### Step 6 — Report

Brief summary:

> *"Refreshed 3 universal maps + 3 framework maps (individuation, hero's journey, chakras). Timeline: 14 entries, oldest 2019-04-12. Most active chakras: Heart and Sacral. Dominant archetype: the Wolf (12 appearances). Chakras map at `context-library/maps/chakras.md`."*

---

## Acceptance criteria

- [ ] Reads `## Active maps` from `profile.md` as primary source for which framework maps to generate
- [ ] Falls back to Q3-based inference for profiles without `## Active maps` (pre-v0.2.0 compatibility)
- [ ] Default `/maps` refreshes universal maps + active framework maps
- [ ] Subcommands work: `universal`, `frameworks`, or any specific map name including `chakras` and `wounds`
- [ ] Universal maps synthesized from individual record files
- [ ] Framework map placement framed as hypothesis with evidence quotes
- [ ] Chakras map generated with ASCII visual overview + prose interpretation
- [ ] ASCII legend included (● most active / ◉ stirring / ○ quiet)
- [ ] Each framework map includes `**Confidence:**` and `**Sources:**` in the header
- [ ] Confidence level derived from entry count + Q1 completion status
- [ ] End-of-map questionnaire prompt appended when Q1 has not been run (maps with a questionnaire)
- [ ] Wounds map generated as ASCII pentagon constellation + 4-layer prose for activated wounds
- [ ] Wounds map intensity assigned based on evidence signals — conservative (most wounds Dormant or Stirring)
- [ ] Each map file includes "last updated" timestamp
- [ ] Empty state handled gracefully
- [ ] Reports clearly what was refreshed and notable findings
- [ ] Never over-certifies — uses "appears to be" language consistently

---

## Tone reminders

- Maps are mirrors, not verdicts. Especially for framework maps.
- Cite evidence specifically. *"On 2024-06-04 you wrote..."* not *"You've expressed feelings of..."*.
- Do not introduce frameworks the user hasn't selected.
- The Chakras map is an invitation to attention, not an energy diagnosis.
- v2 maps (Finding the Ox, 16 Insight Knowledges) need data v1 doesn't have. Don't fake them.
