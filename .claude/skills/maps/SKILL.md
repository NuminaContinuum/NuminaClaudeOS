---
name: maps
description: Generate or refresh the living maps from accumulated context. Universal maps (timeline, relationships, archetypes) for everyone. Framework maps (Hero's Journey, Individuation, Spiral Dynamics, Integral AQAL, Chakras, Wounds & Gifts, Yin & Yang, Hawkins, 16 Ñāṇas, Ox-Herding, Nine Śamatha, Guṇasthānas, Sufi Maqamat) based on the active maps selected in /setup. Maps use ASCII visualizations where spatial layouts help. Subcommands for granular refresh.
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
/maps yin-yang            → refresh just yin-yang.md
/maps hawkins             → refresh just hawkins.md
/maps nanas               → refresh just sixteen-nanas.md
/maps ox-herding          → refresh just ox-herding.md
/maps samatha             → refresh just samatha.md
/maps gunasthanas         → refresh just gunasthanas.md
/maps sufi                → refresh just sufi-maqamat.md
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
| Mystical traditions | heros-journey.md, sufi-maqamat.md |
| Integral theory | integral-aqal.md, spiral-dynamics.md |
| IFS / somatic / trauma-informed | wounds.md |
| Taoism / inner alchemy / energy work / qigong | yin-yang.md |
| Mindfulness and Buddhism | sixteen-nanas.md, samatha.md, ox-herding.md |
| Yoga traditions (incl. meditation lineages) | samatha.md |
| Sufism / dhikr / devotional mysticism (typed in) | sufi-maqamat.md |
| Jainism / vows / renunciation (typed in) | gunasthanas.md |
| David R. Hawkins among inspirations (Q4) | hawkins.md |
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
| yin-yang.md | `/yin-yang-questionnaire` |
| hawkins.md | `/hawkins-questionnaire` |
| sixteen-nanas.md | `/sixteen-nanas-questionnaire` |
| ox-herding.md | `/ox-herding-questionnaire` |
| samatha.md | `/samatha-questionnaire` |
| gunasthanas.md | `/gunasthanas-questionnaire` |
| sufi-maqamat.md | `/sufi-maqamat-questionnaire` |

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

**`context-library/maps/wounds.md`** — Wounds & Gifts constellation

The 5 primary wounds: Rejection, Abandonment, Humiliation, Betrayal, Injustice. This map shows which wounds are most activated right now — as dynamic states with intensity, not fixed identity labels. It also surfaces the integrated gift waiting underneath each wound. Do not reference source frameworks by name in the output. Frame for audiences drawn to IFS, shadow work, depth psychology, and Jungian work.

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
# Wounds & Gifts

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

**`context-library/maps/yin-yang.md`** — Yin & Yang (Neidan) inner-alchemy path

The 5-stage Taoist inner-alchemy path: refining essence → energy → spirit → void, until yin and yang reconcile into the undivided Dao. This map reads where the user's practice and energy appear to be *right now* — a current position on a path of transformation, not a fixed identity. Frame for audiences drawn to energy work, breathwork, inner alchemy, and contemplative practice.

**Core principle — where you are, not who you are.** A practitioner can be deeply, rightly in Foundation after years of practice. That is not a failure state. Render presence and aliveness at the current stage, never a race to the summit.

**The 5 stages, grouped into 3 phases** (Foundation → Refinement → Return):

1. **Laying the Foundation** — 築基 *Zhújī*. Regulate body, breath, mind; seal what leaks.
2. **Refining Essence into Energy** — 煉精化氣 *Liàn Jīng Huà Qì* (first gate). Feel and circulate energy; open the microcosmic orbit.
3. **Refining Energy into Spirit** — 煉氣化神 *Liàn Qì Huà Shén* (middle gate). Energy settles into spirit; breath nearly ceases.
4. **Refining Spirit, Returning to Emptiness** — 煉神還虛 *Liàn Shén Huán Xū* (upper gate). The self thins into spaciousness; the yang-spirit emerges.
5. **Merging with the Dao** — 煉虛合道 *Liàn Xū Hé Dào*. Yin and yang reconciled into the One.

**Canonical content reference:** the full 5-stage spec (essence, yin/yang qualities, lived markers, gift, pitfall), the evidence signals per stage, and the over-rating diagnostics all live in `.claude/skills/yin-yang-questionnaire/yin-yang-framework.md`. Draw from it as reference, not script — match the tone to where this user actually is, in their language. Never quote the layers verbatim. Keep the Chinese terms out of running prose except as a translated gloss on the stage name (translated name primary).

**Placement (derived from evidence in entries):** read across all content for the keyword and theme signals in the framework file. Place the user at one **current stage** with the adjacent **edge** stage (the next gate beginning to open) noted faintly. Be conservative — most committed practitioners live for years in Foundation and the first gate.

**Over-rating is the central reading risk.** The later stages are vivid and well-documented, easy to imagine from reading. Weight the *somatic* markers above any self-description: a felt, repeatable microcosmic orbit (小周天) is the threshold of Stage 2; embryonic breathing (胎息, the breath nearly ceasing) is the threshold of Stage 3. If the entries describe these as ideas rather than felt experience, place earlier. Calibration is a service — name the more honest stage gently.

**Render the map as an ASCII vertical ascent first** (the taiji transforming up the path — turbulent at the base, harmonising through the middle, an empty circle at the summit), then prose below.

Format:

```markdown
# Yin & Yang

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of where your practice is now, not who you are
**Confidence:** Low / Medium / High
**Sources:** [e.g., yin-yang-questionnaire Q1 completed YYYY-MM-DD, 9 entries read]

## The path

    ⊙  Merging with the Dao              (wújí — empty circle)
    ◐  Refining Spirit → Emptiness   上關
    ●  Refining Energy → Spirit      中關   ← you
    ◌  Refining Essence → Energy     初關   ← edge (next gate opening)
    ·  Laying the Foundation         築基

    ●  current    ◌  edge    Return ▸ Refinement ▸ Foundation

## Where you appear to be

**[Stage name] ([Chinese gloss], [pinyin])** — [one paragraph: what signals in the entries point here, with 1-2 specific quotes or date references. The lived markers, in the user's language. Held lightly.]

**The edge:** [the adjacent stage beginning to open, if there's signal — one or two lines]

## What's behind you

[The phase(s) and stage(s) already worked, one example each — framed as ground held, not levels cleared]

## What may be ahead

[The next stage, framed as possibility — what it tends to look like, the somatic marker that would signal genuine arrival]

## A note on honest placement

[Only if the evidence is thin or conceptual for a later-stage claim: one gentle line that the somatic markers (felt circulation, breath nearly ceasing) are what distinguish a felt stage from a read-about one, and that a deeply held earlier stage is a real accomplishment. Omit if placement is well-evidenced.]

## One question

[One question grounded in the current stage and the transition — not a generic practice question]
```

The ASCII ascent renders immediately on opening the file. The prose gives the rationale. Keep the over-rating humility throughout: this map's later stages are the easiest in the whole system to over-claim, and an honest Foundation is worth more than a flattered Stage 4.

---

### Step 4 — Handle empty state

If `context-library/` has fewer than 3 entries across all content types:

> *"There's not enough yet to build maps from. Try `/journal`, `/dream`, or `/harvest` first — `/maps` will be more useful with at least a handful of entries."*

If only some maps have data, generate the ones that do and note the empty ones.

---

**`context-library/maps/hawkins.md`** — Hawkins Consciousness map of consciousness

David Hawkins' 17 levels of consciousness, from Shame (20) to Enlightenment (700), grouped into 7 bands: Despair, Reactive, Courage, Trust, Reason, Love, Spirit. The map is calibrational and gradient-based: one placement on a scale, with the bands above and below forming the user's emotional-energetic terrain. It reads the register the user's inner life appears to be running in *right now*, not a fixed identity and not a score.

**Core principle — where you are, not who you are.** Grief is not a failure and Love is not a graduation. Each level teaches something only that level can teach, and the upper levels carry their own pitfalls (Reason detaches, Love clings, Peace bypasses). Never render this map as a leaderboard.

**The numbers are gradient markers, not measurements.** Hawkins' calibration method is contested. Write the map as a phenomenological self-read. Nobody lives at one level.

**The 7 bands** (the 200 threshold sits between Reactive and Courage; Courage counts as above it):

1. **Despair** — Shame 20, Guilt 30, Apathy 50, Grief 75. Contraction, shame, and frozen grief.
2. **Reactive** — Fear 100, Desire 125, Anger 150, Pride 175. Fear, craving, anger, and defensive pride.
3. **Courage** — 200. The threshold where force turns toward power.
4. **Trust** — Neutrality 250, Willingness 310. Steady openness and willingness.
5. **Reason** — Acceptance 350, Reason 400. Acceptance and clear seeing.
6. **Love** — Love 500, Joy 540. Warmth, joy, and heart-led connection.
7. **Spirit** — Peace 600, Enlightenment 700. Peace and non-separate awareness.

**Canonical content reference:** the 17 levels, band gifts and pitfalls, the 200 threshold, gradient states, threshold readings, the six crossings with practices, the bypass checks and the evidence signals all live in `.claude/skills/hawkins-questionnaire/hawkins-framework.md`. Draw from it as reference, not script — match the tone to where this user actually is, in their language. Never quote the layers verbatim.

**Placement (derived from evidence in entries):** read across all content for the band signals in the framework file. Read the register underneath the events, not the vocabulary. Place one **current band** with a level inside it, plus **familiar**, **emerging** and **refused** bands where there's signal. When two bands are equally supported, place the lower: this map's upper levels are the easy ones to reach for. Questionnaire readings (`## Q1/Q2/Q3 Reading`) outrank inference from entries.

**Bypass is the central reading risk.** The upper levels are describable from a distance. Fluent Love or Peace language with no lower-band material anywhere, or with Despair or Reactive actively refused, is a bypass signal rather than evidence of an upper placement. Name it gently, as work still available, and never as a demotion. Refusing Spirit ("that stillness reads as dissociation to me") is a real position, not a symptom.

**Render the map as an ASCII vertical scale first** (all 17 levels, the 200 line marked, bands styled by state), then prose below.

Format:

```markdown
# Hawkins Consciousness

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of the register you're living in now, not who you are. The numbers are gradient markers, not measurements
**Confidence:** Low / Medium / High
**Sources:** [e.g., hawkins-questionnaire Q1 completed YYYY-MM-DD, 9 entries read]

## The scale

    SPIRIT    700  Enlightenment          ·
              600  Peace
    LOVE      540  Joy                    ◌  emerging
              500  Love
    REASON    400  Reason                 ●
              350  Acceptance             ← you
    TRUST     310  Willingness            ◉  familiar
              250  Neutrality
    COURAGE   200  Courage                ◉  familiar
    ──────────────────── 200 · power above ▴  force below ▾
    REACTIVE  175  Pride                  ·
              150  Anger
              125  Desire
              100  Fear
    DESPAIR    75  Grief                  ⊘  refused
               50  Apathy
               30  Guilt
               20  Shame

    ●  where you live    ◉  familiar    ◌  emerging    ⊘  refused    ·  dormant

## Where you appear to be

**[Level] ([value]), in [Band]** — [one paragraph: what signals in the entries point here, with 1-2 specific quotes or date references. The lived experience first, then the label. Which side of the 200 line, said gently. Held lightly.]

## The rest of the terrain

[Familiar bands: known ground, one example each. Emerging band: what's gathering. Framed as terrain, not rungs cleared.]

## The threshold you're at

[The crossing out of the current band (from the framework's crossings table) and its concrete practice, in the user's terms.]

## What's being pushed away

[Only if a band is refused or bypass signals are present: one or two gentle lines that the levels are moved through rather than jumped, and that the refused register is often where the work is. Omit otherwise.]

## One question

[One question grounded in the current band and the crossing — not a generic question about consciousness]
```

The ASCII scale renders immediately on opening the file. The prose gives the rationale. Keep the humility throughout: this is the easiest map in the system to wear as a costume, and an honest Grief is worth more than a flattered Peace.

---

**`context-library/maps/sixteen-nanas.md`** — 16 Ñāṇas (Insight Knowledges / Progress of Insight)

The 16 insight knowledges from the Theravada Progress of Insight (Mahasi lineage): the sequence the mind moves through as it begins to see experience clearly, from distinguishing mind and body, through the vivid Arising & Passing, the difficult Dark Night, Equanimity, and the threshold and its review. This map reads where the user's practice appears to be *right now*, a current phase of a cycle, not a fixed identity. Frame for audiences drawn to insight meditation, vipassana, noting practice, and contemplative work.

**Core principle — where you are, not who you are.** This arc is a **cycle, not a ladder**: practitioners go round it more than once, and after Reviewing (16) it begins again. Pre-Cycle is not "behind" Equanimity. Render the current phase, never a race to the end.

**The 16 stages, grouped into 6 bands** (Pre-Cycle is off-map, before stage 1):

1. **Pre-Cycle** — off-map. Practice building ground, or ordinary life between cycles.
2. **Early Insights** (1-3) — Distinguishing Mental & Physical, Cause & Effect, Three Characteristics.
3. **Arising & Passing** (4) — the vivid birth and death of moments; energy, light, clarity.
4. **Dark Night** (5-10) — Dissolution, Fear, Disadvantages, Disenchantment, Desire for Deliverance, Reflective Contemplation.
5. **Equanimity** (11) — steady, impartial awareness of formations.
6. **Path & Review** (12-16) — Conformity, Change of Lineage, Path Knowledge, Fruition, Reviewing.

**Canonical content reference:** the 16 stages (translated name, Pali, meaning, classical markers), the band essences (lived markers, gift, pitfall), the state notes, the crossings and their practices, the cycle readings, the Dark Night care line and the evidence signals all live in `.claude/skills/sixteen-nanas-questionnaire/sixteen-nanas-framework.md`. Draw from it as reference, not script. Match the tone to where this user actually is, in their language. Translated stage names primary; Pali only as a secondary gloss on the stage name.

**Placement (derived from evidence in entries):** read across all content for the signals in the framework file. Place the user in one **live band** (a specific stage only when the entries describe its texture), with any **familiar** bands, an **emerging** band at the edge, and any band they **push against**. Two non-adjacent live bands are a real pattern on this arc (a fast cycle); report it rather than resolving it away. Prefer repeated texture over a single vivid entry. Generic words ("path," "change," "reflect," "calm") count only in a practice context.

**Two care rules.** The **Dark Night is difficult, normal and passing**: name it as a stage, never as pathology or failure, and include the framework's care line when it is the live band. **A path moment is never inferred from one experience**: place in Path & Review only on repeated description of a lasting shift in ordinary life, and even then hold it as hypothesis. A user who distrusts the "path moment" framing has not failed the map.

**Render the map as an ASCII arc first** (the 16 stages top to bottom, bands on the left, looping back at the bottom), then prose below.

Format:

```markdown
# 16 Ñāṇas

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of where your practice is in the cycle now, not who you are
**Confidence:** Low / Medium / High
**Sources:** [e.g., sixteen-nanas-questionnaire Q1 completed YYYY-MM-DD, 9 entries read]

## The arc

    PRE-CYCLE          ·      off-map
    EARLY INSIGHTS     ◌   1  Distinguishing Mental & Physical
                       ◌   2  Cause & Effect
                       ◌   3  Three Characteristics
    ARISING & PASSING  ◌   4  Arising & Passing
    DARK NIGHT         ●   5  Dissolution
                       ●   6  Fear                      ← you
                       ●   7  Disadvantages
                       ●   8  Disenchantment
                       ●   9  Desire for Deliverance
                       ●  10  Reflective Contemplation
    EQUANIMITY         ◦  11  Equanimity                ← edge
    PATH & REVIEW      ·  12  Conformity
                       ·  13  Change of Lineage
                       ·  14  Path Knowledge
                       ·  15  Fruition
                       ·  16  Reviewing
                       ↺      the cycle begins again

    ●  live    ◌  familiar    ◦  emerging    ·  not in play    ⊘  pushed against

## Where you appear to be

**[Band] — [Stage name] ([Pali])** — [one paragraph: what signals in the entries point here, with 1-2 specific quotes or date references. Lived experience first, label second, in the user's language. Held lightly. If the band is the Dark Night, close with the care line.]

**The edge:** [the emerging band, if there's signal — one or two lines, with the practice suggestion for that crossing]

## Known country

[Familiar bands, one example each — framed as ground already travelled, not levels cleared. If Path & Review is familiar, say the user *describes* having crossed before; never certify it.]

## What you push against

[Only if a band is pushed against: name it gently as work asking to be done. On this arc the refused territory is usually the near one. Omit otherwise.]

## The cycle

[How many times round, if known (from Q3 or entries), and what that changes about the reading. Note a fast cycle if two non-adjacent bands are live. Omit if there's no signal.]

## One question

[One question grounded in the live band and the crossing — not a generic practice question]
```

The ASCII arc renders immediately on opening the file. The prose gives the rationale. Keep the cyclical framing throughout: this map's later bands are not a finish line, and the Dark Night is a stage the mind passes through, not a verdict.

---

**`context-library/maps/ox-herding.md`** — Ten Ox-Herding Pictures

Kakuan's twelfth-century Chan sequence of ten pictures: from searching for the ox, through catching and taming it, riding home, the empty circle, suchness, and finally the return to the marketplace with open hands. This map reads which picture the user appears to be in *right now*, a current position, not a fixed identity. Frame for audiences drawn to Zen, Buddhist meditation, and contemplative practice generally; the pictures work as pictures without any prior knowledge.

**Core principle — where you are, not who you are.** Searching is not behind; Working is not less than. Each picture is the whole path seen from where the person stands, and people move back through the sequence as often as forward. Two pictures can be live in different parts of a life.

**The map ends in the marketplace, not in emptiness.** Kakuan added pictures 9 and 10 after the empty circle on purpose. Never render 8 or 9 as the summit, and never place at 8 from a single glimpse.

**The 10 pictures, grouped into 5 bands:**

1. **Searching for the Ox** — 尋牛 *Jingyu* (Searching). The longing; something essential is missing.
2. **Seeing the Tracks** — 見跡 *Kenseki* (Searching). Clues in teachings and practice; the trail is real.
3. **Catching Sight of the Ox** — 見牛 *Kengyū* (Working). A first direct glimpse, brief and unmistakable.
4. **Catching the Ox** — 得牛 *Tokugyū* (Working). Hands on the rope; the wild mind pulls hard.
5. **Taming the Ox** — 牧牛 *Bokugyū* (Working). The rope slackens; gentle, steady practice.
6. **Riding the Ox Home** — 騎牛帰家 *Kigyū Kika* (Riding). Ease and joy; the animal knows the way.
7. **The Ox Transcended** — 忘牛存人 *Bōgyū Sonnin* (Riding). The method falls away; the person remains.
8. **Both Ox and Self Transcended** — 人牛倶忘 *Ningyū Gubō* (Empty). The empty circle.
9. **Returning to the Source** — 返本還源 *Henpon Gengen* (Empty). The world as itself; river, blossom.
10. **Entering the Marketplace** — 入鄽垂手 *Nitten Suishu* (Marketplace). Ordinary life with open hands.

**Canonical content reference:** the full ten-picture spec (meaning, image, lived markers, gift, pitfall), the transitions and their practices, the evidence signals, and the reading diagnostics all live in `.claude/skills/ox-herding-questionnaire/ox-herding-framework.md`. Draw from it as reference, not script — match the tone to where this user actually is, in their language. Never quote the layers verbatim. Keep the classical names out of running prose except as a gloss on the picture name (translated name primary).

**Placement (derived from evidence in entries):** read across all content for the keyword and theme signals in the framework file. Place the user at one **current picture**, a soft halo on the other picture(s) in the same band, and the **edge** (the next crossing) where there's signal. If questionnaire readings exist, the latest one anchors the placement (a Q3 picture chosen by the user outranks keyword evidence).

**Inflation at the far end is the central reading risk.** Pictures 7, 8 and 9 are the easiest to claim from reading and the hardest to live. "Void," "oneness," or one dramatic sitting is a glimpse, not a home: look for repeated, lived, everyday evidence. Picture 10 is the subtlest: service language alone is not the marketplace, and the pride of having returned is its pitfall. Calibration is a service; name the more honest picture gently.

**Render the map as an ASCII picture row first** (the ten pictures left to right, banded, the arc ending back on ordinary ground at 10), then prose below.

Format:

```markdown
# Ox-Herding

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of which picture you're in now, not who you are
**Confidence:** Low / Medium / High
**Sources:** [e.g., ox-herding-questionnaire Q1 completed YYYY-MM-DD, 9 entries read]

## The ten pictures

    Searching   Working          Riding     Empty      Market
    1     2     3     4     5    6     7    8     9    10
    ·     ·     ◌     ●     ◌    ·     ·    ○     ·    ·
                      ↑ you          ↗ edge: from gripping the rope to walking beside

    ●  current    ◌  same band    ○  the empty circle (not the last picture)
    the path ends in the marketplace, back on ordinary ground

## Where you appear to be

**[N. Picture name] ([Chinese], [Japanese reading])** — [one paragraph: what signals in the entries point here, with 1-2 specific quotes or date references. The image, the lived markers, the gift and the pitfall, in the user's language. Held lightly.]

**The edge:** [the crossing beginning to open, if there's signal, with its practice from the framework — one or two lines]

## What's behind you

[The picture(s) already lived, one example each — framed as ground walked, not levels cleared. Note any that are still familiar and return.]

## What may be ahead

[The next picture, framed as possibility — what it tends to look like in an ordinary week. If the current picture is 8 or 9, say plainly that the sequence continues into the world.]

## A note on honest placement

[Only if the evidence is thin, conceptual, or a single peak for a 7-9 claim, or if a 10 claim carries a whiff of pride: one gentle line. A lived earlier picture is worth more than a flattered later one. Omit if placement is well-evidenced.]

## One question

[One question grounded in the current picture and the crossing — not a generic practice question]
```

The ASCII row renders immediately on opening the file. The prose gives the rationale. Keep the humility throughout: the far end of this map is easy to over-claim, and the marketplace is not "highest," it's home.

---

**`context-library/maps/samatha.md`** — Nine Śamatha Stages (concentration)

The nine stages of śamatha (calm abiding) from the Indo-Tibetan tradition: from first placing attention on an object, through returning, refining the quality of attention and the very subtle work, into effortless equipoise. This map tracks **one skill**, sustained attention on a chosen object. Not awakening, not insight, not devotion. It reads where the user's sits appear to be *right now*, a current position in a training, not a fixed identity. Frame for audiences who sit: concentration practice, breath meditation, calm abiding, the Tibetan and Theravāda paths.

**Core principle — where you are, not who you are.** A practitioner can be rightly at the third stage after years of sitting. That is the practice working, not failing. Render where the sits are now, never a race to the ninth.

**The 9 stages, grouped into 5 bands** (Establishing → Returning → Refining Quality → Subtle Work → Effortless):

1. **Placement of the Mind** — Power of study (*śruta*). Attention lands for a moment and slips.
2. **Continuous Placement** — Power of concentration (*cintā*). Brief continuity, a minute at most.
3. **Repeated Placement** — Power of memory, fixing (*smṛti*). The object is lost, but caught back quickly.
4. **Close Placement** — Power of memory, recollection. The object is no longer lost entirely. The first milestone.
5. **Taming** — Power of comprehension, leading (*samprajaña*). Introspective awareness lifts subtle dullness.
6. **Pacifying** — Power of comprehension, pacified. Subtle agitation settles; the mind cooperates.
7. **Fully Pacifying** — Power of diligence, submitting (*vīrya*). Subtle obstacles dispelled as they arise; effort still active.
8. **Single-Pointed Attention** — Power of diligence, one-pointed (*ekāgratā*). A whole sit unwavering, a little effort to enter.
9. **Equipoise** — Power of perfection. Effort falls away; pliancy (*praśrabdhi*) is present.

**Canonical content reference:** the full 9-stage spec (classical names, the six powers, thangka imagery, lived markers, gift, pitfall, the next crossing), the obstacle readings, the evidence signals per stage, the over-rating diagnostics and the practice-history ceilings all live in `.claude/skills/samatha-questionnaire/samatha-framework.md`. Draw from it as reference, not script. Match the tone to where this user actually is, in their language. Never quote the layers verbatim. Classical name primary; the power and Sanskrit only as a gloss.

**Placement (derived from evidence in entries):** read across all content for the signals in the framework file. Weight descriptions of actual sits (how long, where attention went, whether the object was lost or only dimmed, what the body did) far above vocabulary: "calm", "stable" and "insight" turn up everywhere. Place the user at one **current stage**, with the other stage in the same band noted faintly as the **edge**. Be conservative: most committed practitioners live for years around Stages 2-4.

**Over-rating is the central reading risk.** The later stages are technical, well described, and easy to imagine from reading. Weight the behavioural markers above any self-description: Stage 7-8 needs sustained sits of 45 minutes or more; Stage 9 needs an hour-plus *and* felt pliancy; Stage 5+ needs both supports (mindfulness and introspective awareness) reliable; Stage 4+ needs sustained daily practice. If the entries don't show these, place earlier. A questionnaire reading with a calibration downgrade or a practice-history ceiling outranks harvested keyword signal. Calibration is a service; name the more honest stage gently.

**Render the map as an ASCII ascent first** (the thangka's nine bends bottom to top, the elephant whitening ● → ○ and the flame of effort ▲ burning lower), then prose below.

Format:

```markdown
# Nine Śamatha Stages

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of where your sits are now, not who you are
**Confidence:** Low / Medium / High
**Sources:** [e.g., samatha-questionnaire Q2 completed YYYY-MM-DD, 11 entries read]

## The path

    9  Equipoise                     ○        rainbow
    8  Single-Pointed Attention      ○  ▴
    7  Fully Pacifying               ◔  ▴
    6  Pacifying                     ◔  ▲
    5  Taming                        ◑  ▲     ◌  ← edge (same band)
    4  Close Placement               ◑  ▲     ●  ← you
    3  Repeated Placement            ◕  ▲     ◌
    2  Continuous Placement          ●  ▲
    1  Placement of the Mind         ●  ▲

    ●  current    ◌  edge / familiar    ● → ○  the elephant whitening    ▲  effort

## Where you appear to be

**Stage [N] · [Classical name]** ([power], *[Sanskrit]*) — [one paragraph: what in the entries points here, with 1-2 specific quotes or date references, ideally descriptions of actual sits. The lived markers, in the user's language. Held lightly.]

**The edge:** [the other stage in the band, or the next band gathering, if there's signal — one or two lines]

## What's behind you

[The stages already worked, one example each — framed as ground held, not levels cleared. The returning is never a failure.]

## The next crossing

[The current stage's next crossing from the framework, made concrete for this user — what the practice asks next, and the behavioural marker that would signal genuine arrival (e.g. the object no longer lost entirely for Stage 4; pliancy for Stage 9)]

## A note on honest placement

[Only if the evidence is thin, self-descriptive, or a later-stage claim lacks the behavioural markers: one gentle line that sit length, pliancy and what actually happens in a sit are what distinguish a lived stage from a read-about one, and that most practitioners live for years around Stages 2-4. Omit if placement is well-evidenced.]

## One question

[One question grounded in the current stage and its next crossing — not a generic practice question]
```

The ASCII ascent renders immediately on opening the file. The prose gives the rationale. Keep the over-rating humility throughout: this map tracks one technical skill, its later stages are easy to over-claim, and an honest Stage 3 is worth more than a flattered Stage 8.

---

**`context-library/maps/gunasthanas.md`** — Guṇasthānas, the Jain ladder of fourteen stages

The Jain ladder of spiritual development: fourteen guṇasthānas ("stations of virtue") from complete delusion to final liberation, measured by the thinning of deluding karma and the four passions (anger, pride, deceit, greed). Grouped into five phases: delusion → faith → discipline → purification → liberation. This map reads where the user's **conduct** appears to be *right now*, not what they believe and not how long they have practised. Frame for audiences drawn to ethical practice, vows, renunciation, Jain thought, and contemplative discipline.

**Core principle — where you are, not who you are.** The first stage is where the path begins, not a failing grade. A long, serious life can sit rightly and deeply at stage four. The map is hierarchical; render it matter-of-factly, never as a purity score.

**The placeable range.** Only stages **1-7** can be placed. Stages **8-10** (the purification ascent) are drawn above as what lies ahead, never claimable. Stages **11-14** (passions suppressed, passions destroyed, omniscience, final liberation) are the summit, described, never placed. Entries that use summit language (*kevala, moksha, liberation*) are read as interest in the summit, never as evidence of being there.

**The 14 stages, in 5 phases:**

1. **Mithyātva** — Wrong Belief *(delusion)*. Living on reaction; where the path begins.
2. **Sāsvādana** — Taste of Right Faith *(delusion)*. A clarity tasted and lost.
3. **Mishra** — Mixed Belief *(delusion)*. Insight and confusion alternating.
4. **Avirata Samyagdṛṣṭi** — Right Faith Without Vows *(faith)*. Right seeing settled; conduct not yet followed.
5. **Deśa Virata** — Partial Vows *(discipline)*. Named, kept restraints inside ordinary life.
6. **Pramatta Sarva Virata** — Complete Vows with Negligence *(discipline)*. Full vows; vigilance comes and goes.
7. **Apramatta Sarva Virata** — Complete Vows Without Negligence *(discipline)*. Full vows, steady attention.
8-10. **Apūrva Karaṇa, Anivṛtti Karaṇa, Sūkṣma Sāmparāya** *(purification)*. The ascent. Visible, not claimable.
11-14. **Upaśānta Moha, Kṣīṇa Moha, Sayogi Kevalī, Ayogi Kevalī** *(liberation)*. The summit. Narrative only.

**Canonical content reference:** the full stage content (meaning, classical description, characteristics, lived markers, next real step), the attainment ceiling, the four passions, and the evidence signals all live in `.claude/skills/gunasthanas-questionnaire/gunasthanas-framework.md`. Draw from it as reference, not script. Match the tone to where this user actually is, in their language. Stage names are the transliterated Sanskrit followed by the translation; keep Sanskrit out of running prose otherwise.

**Placement (derived from evidence in entries):** read across all content for the signals in the framework file. Place the user at one **current stage** in 1-7, with the rung just above noted faintly as the **edge** when there is signal. On this ladder an honest reading rounds down: when evidence splits between two stages, take the lower.

**Conduct beats self-rating — the central reading risk.** The ladder is explicit about what separates one rung from the next, which makes it easy to overclaim. Apply the attainment ceiling to entries too: no specific, named, kept restraint in the entries → not above stage 4; no formal commitment made in front of others → not above stage 5; reported lapses of attention → not stage 7. Values and intentions are not vows. If a questionnaire reading exists, its ceiling result outranks anything inferred from entries.

**Render the map as an ASCII staircase first** (the ladder ascending from the ocean of worldly existence to the summit, the placeable range below a line), then prose below.

Format:

```markdown
# Guṇasthānas

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of where your conduct is now, not who you are
**Confidence:** Low / Medium / High
**Sources:** [e.g., gunasthanas-questionnaire Q2 completed YYYY-MM-DD, 11 entries read]

## The ladder

    △  14  Ayogi Kevalī               Omniscient without Activity
    △  13  Sayogi Kevalī              Omniscient with Activity          liberation
    △  12  Kṣīṇa Moha                 Passions Destroyed
    △  11  Upaśānta Moha              Passions Suppressed
    ┆  10  Sūkṣma Sāmparāya           Subtle Passions
    ┆   9  Anivṛtti Karaṇa            Advanced Purification             purification
    ┆   8  Apūrva Karaṇa              Unprecedented Spiritual Progress
   ─────────────────────────────────── shown above, never placed
    ·   7  Apramatta Sarva Virata     Complete Vows Without Negligence
    ·   6  Pramatta Sarva Virata      Complete Vows with Negligence     discipline
    ◌   5  Deśa Virata                Partial Vows                      ← edge
    ●   4  Avirata Samyagdṛṣṭi        Right Faith Without Vows          ← you   (faith)
    ·   3  Mishra                     Mixed Belief
    ·   2  Sāsvādana                  Taste of Right Faith              delusion
    ·   1  Mithyātva                  Wrong Belief

    ● current   ◌ edge   ┆ the ascent   △ the summit

## Where you appear to be

**[Sanskrit name] ([translation], stage N)** — [one paragraph: what in the entries points here, with 1-2 specific quotes or date references. Conduct first: what they actually do, refuse, keep, react to. Held lightly.]

**The edge:** [the rung just above, if there's signal — one or two lines, and what concrete conduct would mark arrival]

## What's behind you

[Rungs already worked, one example each, framed as ground held, not levels cleared]

## The next real step

[One small, concrete, keepable restraint or vigilance practice for the current stage, from the framework file, adapted to the entries. Never an abstract exhortation.]

## The passions in play

[Only if the entries show it: which of anger, pride, deceit, greed shows most, with one example. Omit otherwise.]

## A note on honest placement

[Only if entries claim more than the conduct shows: one gentle line that on this map the rungs are conduct, that a named, kept restraint is what separates seeing from partial vows, and that years of practice never move anyone up. Omit if placement is well-evidenced.]

## One question

[One question grounded in the current stage and the conduct at its edge — not a generic practice question]
```

The ASCII staircase renders immediately on opening the file. The prose gives the rationale. Keep the humility throughout: the summit is shown so the ladder is honest about its length, not so anyone can stand on it.

---

**`context-library/maps/sufi-maqamat.md`** — Sufi Maqamat, the stations of the path

The ten maqamat (stations) of the Sufi path, from turning back through letting go, trial and trust, and devotion, into knowing and the dissolving of the separate claim. Ten stations in five bands: Turning (Tawba, Wara') · Letting Go (Zuhd, Faqr) · Trial & Trust (Sabr, Tawakkul) · Devotion (Rida, Mahabba) · Knowing (Marifa, Fana). This map reads where the user's heart and practice appear to be *right now*, a current station on a path of the heart, not a rank of souls. Frame for audiences drawn to devotional, contemplative and mystical practice, inside or outside Islam.

**Core principle — where you are, not who you are.** A seeker can be rightly, deeply in Tawba after decades. The early stations are rigorous, not lesser. The stations are earned slowly, and they are not a ranking of souls. The path is spiral: every noticing of pride is a fresh Tawba.

**Canonical content reference:** the ten stations (essence, lived markers, gift, pitfall, classical line), the maqam/hal distinction, the ahwal, the ujb spine and the evidence signals all live in `.claude/skills/sufi-maqamat-questionnaire/sufi-maqamat-framework.md`. Draw from it as reference, not script. Match the tone to where this user actually is, in their language and their own word for what they turn toward (the Beloved, the Friend, the Real, the holy). Keep Arabic out of running prose except as script + transliteration beside the translated station name (translated name primary).

**Placement (derived from evidence in entries):** read across all content for the station keywords and practices in the framework file. Place the user at one **current station** with the next station gathering noted faintly as the **edge**. Be conservative: most sincere seekers live for years in the first three bands.

**Maqam vs hal is the central reading risk.** A maqam is earned and stable; a hal is given and passes. Weight *repeated return* across entries above any single vivid entry. One luminous experience of love is a hal, not the station of Mahabba; one experience of dissolving is a hal of Fana, never the station. **Fana is never placed from a single experience**: it needs sober, repeated, lived evidence of a loosened claim (humility, service, nobody left to take credit). If questionnaire readings say "touched as hal", keep that label. Surface ujb (secret pride at one's station) only as a stage of the work, never as accusation.

**Render the map as an ASCII rising path first** (ten gates, bottom to top, the Arabic name beside each), then prose below.

Format:

```markdown
# Sufi Maqamat

**Last updated:** YYYY-MM-DD
**Held as:** hypothesis, not verdict — a map of where your heart is now, not who you are
**Confidence:** Low / Medium / High
**Sources:** [e.g., sufi-maqamat-questionnaire Q2 completed YYYY-MM-DD, 11 entries read]

## The path

   Knowing         ·  Annihilation    Fana      الفناء
                   ·  Gnosis          Marifa    المعرفة
   Devotion        ·  Love            Mahabba   المحبة
                   ◌  Contentment     Rida      الرضا     ← edge (gathering)
   Trial & Trust   ◉  Reliance        Tawakkul  التوكّل
                   ●  Patience        Sabr      الصبر     ← you (held as maqam)
   Letting Go      ◉  Spiritual Pov.  Faqr      الفقر
                   ·  Renunciation    Zuhd      الزهد
   Turning         ◉  Scrupulousness  Wara'     الورع
                   ·  Turning         Tawba     التوبة

   ●  current    ◉  familiar    ◌  edge    ⊘  resisted    the path is spiral, not a ladder

## Where you appear to be

**[Translated name] ([Arabic], [transliteration])** — held as maqam / touched as hal — [one paragraph: what signals in the entries point here, with 1-2 specific quotes or date references. The lived markers, in the user's language. Held lightly.]

**The edge:** [the station gathering next, if there's signal — one or two lines]

## Ground already walked

[Familiar stations, one example each — framed as ground held, not levels cleared. Note that the early stations keep returning; that return is the work.]

## What may be ahead

[The next station, framed as possibility — what it tends to look like, and the stability that would mark it as a maqam rather than a visiting hal]

## A note on station and state

[Only if the evidence for the current or a later station is a single vivid experience, or the readings say "touched as hal": one gentle line that a state given by grace is real and honoured, and that a station is what remains returnable day after day. Omit if the placement is well-evidenced.]

## One question

[One question grounded in the current station and the transition — not a generic spiritual question]
```

The ASCII path renders immediately on opening the file. The prose gives the rationale. Keep the humility throughout: the later stations are poetic, easy to claim, and earned over years. An honest Tawba is worth more than a flattered Fana.

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
- [ ] Yin & Yang map generated as ASCII vertical ascent + prose; current stage + edge placed conservatively, weighting somatic markers (felt orbit, breath cessation) over self-description
- [ ] Yin & Yang map uses "where you are, not who you are" framing; an honest earlier stage is never framed as a lesser self
- [ ] Hawkins map generated as ASCII vertical scale (17 levels, 200 line marked, bands styled by state) + prose; current band and level placed conservatively, with the lower band winning when evidence is split and bypass signals weighed against upper-level claims
- [ ] Hawkins map uses "where you are, not who you are" framing and treats the numbers as gradient markers, not measurements; no level is framed as a lesser self
- [ ] 16 Ñāṇas map generated as ASCII arc + prose; live band, familiar/emerging/pushed-against bands placed conservatively from repeated texture; rapid cycling reported rather than resolved; specific stage named only when the evidence shows its texture
- [ ] 16 Ñāṇas map uses "where you are, not who you are" and cyclical framing; the Dark Night is named as a difficult, normal, passing stage with the care line; Path & Review is never inferred from a single experience
- [ ] Ox-Herding map generated as an ASCII ten-picture row + prose; current picture placed conservatively (7-9 only on repeated lived evidence, never a single glimpse), same-band halo and edge crossing shown
- [ ] Ox-Herding map uses "where you are, not who you are" framing and ends in the marketplace, not the empty circle; picture 10 held with humility, never as "highest"
- [ ] Śamatha map generated as ASCII ascent (nine stages, five bands) + prose; current stage + same-band edge placed conservatively, weighting behavioural markers (sit length, pliancy, both supports, sustained practice) and descriptions of actual sits over self-description
- [ ] Śamatha map uses "where you are, not who you are" framing and treats the map as one skill (sustained attention); an earlier stage is never framed as a lesser self, and questionnaire calibration outranks keyword signal
- [ ] Guṇasthānas map generated as ASCII staircase + prose; current stage placed only in 1-7, 8-10 drawn as the visible ascent, 11-14 as the narrative summit; conduct (named, kept restraints) weighted over belief or practice length, rounding down
- [ ] Guṇasthānas map uses "where you are, not who you are" framing; the first stage is where the path begins, never a failing grade
- [ ] Sufi Maqamat map generated as ASCII rising path (ten gates, Arabic beside each) + prose; current station + edge placed conservatively, weighting repeated return over single vivid entries
- [ ] Sufi Maqamat map keeps maqam vs hal explicit (a passing state is never read as an earned station, Fana never placed from a single experience) and uses "where you are, not who you are" framing
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
- The contemplative path maps (Yin & Yang, Hawkins, 16 Ñāṇas, Ox-Herding, Nine Śamatha, Guṇasthānas, Sufi Maqamat) are easy to over-claim. Place conservatively, and an honest earlier stage is never a lesser self.
