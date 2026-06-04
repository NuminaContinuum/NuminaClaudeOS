---
name: questionnaire
description: Unified entry point for all Numina OS questionnaires. Asks which questionnaire and which stage if not specified. Detects progress automatically and prompts the next stage. Allows redoing any questionnaire at any time and in any order. Types: wounds, heros-journey, chakras, individuation, spiral-dynamics, integral-aqal.
---

# /questionnaire

Single entry point for all Numina OS questionnaires. Works like `/maps` — one command, targeted by name and stage number.

---

## Usage

```
/questionnaire                           → asks which questionnaire; auto-detects stage
/questionnaire wounds                    → Wounds & Gifts questionnaire (auto-detects stage)
/questionnaire heros-journey            → Hero's Journey questionnaire (auto-detects stage)
/questionnaire chakras                  → Chakra questionnaire (auto-detects stage)
/questionnaire individuation            → Individuation questionnaire (auto-detects stage)
/questionnaire spiral-dynamics          → Spiral Dynamics questionnaire (auto-detects stage)
/questionnaire integral-aqal            → Integral AQAL questionnaire (auto-detects stage)
/questionnaire wounds 1                 → Wounds Q1 specifically
/questionnaire wounds 2                 → Wounds Q2 specifically
/questionnaire wounds 3                 → Wounds Q3 specifically
```

The stage number is optional for any type. If omitted, the skill detects where the user is and prompts the next stage.

---

## Behaviour

### Step 0 — Parse the invocation

Identify what was passed as arguments.

| Arguments | Action |
|---|---|
| Name + number (e.g. `wounds 2`) | Jump directly to that questionnaire and stage (Step 3) |
| Name only (e.g. `wounds`) | Detect progress and route to next stage (Step 2) |
| Nothing | Ask the user which questionnaire (Step 1) |

---

### Step 1 — Ask which questionnaire (no argument)

Read `context-library/profile.md` → `## Active maps` to know which maps the user has activated. Check each map file for completed stages.

Present the questionnaire list with progress shown:

> *"Which questionnaire would you like to work on?*
>
> *[numbered list, e.g.:*
> *1. Wounds & Gifts — Q1 done, Q2 available*
> *2. Chakras — not started*
> *3. Hero's Journey — Q1 and Q2 done, Q3 available*
> *4. Individuation — Q1 done, Q2 available*
> *...*
> *Or type a name + number to jump directly (e.g. `wounds 2`)"*

Only show questionnaire types for the user's active maps. If a map has no questionnaire yet, omit it.

After they choose, go to Step 2.

---

### Step 2 — Detect progress and route to next stage

Check the relevant map file for completed stages by looking for `## Q1 Reading`, `## Q2 Reading`, `## Q3 Reading` sections.

| State | Action |
|---|---|
| No stages done | Run Q1 |
| Q1 done, Q2 not | Offer Q2 with one sentence on what it adds. If they decline, stop gracefully |
| Q1 + Q2 done, Q3 not | Offer Q3 with one sentence on what it adds. If they decline, stop gracefully |
| All done | Offer to redo any stage or refresh the map |

**Never push toward deeper stages.** Each offer is a quiet nudge with an easy exit. The user can always say they want a specific stage and you'll run it.

---

### Step 3 — Execute the questionnaire

Load the full content from the corresponding individual skill file and execute the requested stage:

| Questionnaire | Skill file | Map file |
|---|---|---|
| wounds | `.claude/skills/wounds-questionnaire/SKILL.md` | `context-library/maps/wounds.md` |
| heros-journey | `.claude/skills/heros-journey-questionnaire/SKILL.md` | `context-library/maps/heros-journey.md` |
| chakras | `.claude/skills/chakra-questionnaire/SKILL.md` | `context-library/maps/chakras.md` |
| individuation | `.claude/skills/individuation-questionnaire/SKILL.md` | `context-library/maps/individuation.md` |
| spiral-dynamics | `.claude/skills/spiral-dynamics-questionnaire/SKILL.md` | `context-library/maps/spiral-dynamics.md` |
| integral-aqal | `.claude/skills/integral-aqal-questionnaire/SKILL.md` | `context-library/maps/integral-aqal.md` |

Read the full SKILL.md for the chosen type, locate the Q1/Q2/Q3 section that matches the requested stage, and execute it exactly as specified there — including the opening, question sequence, scoring, rendering, and file-write steps.

---

### Step 4 — Redo flow

If the user asks to redo a stage that's already completed, confirm once:

> *"You've already done [name] Q[N] (on [date]). Running it again will add a new dated reading above the old one — nothing is lost. Ready?"*

If yes, run the stage. The new reading is prepended to the map file with today's date, and all prior readings are preserved below it.

---

## Map → questionnaire reference

| Map | Questionnaire name | Stages available |
|---|---|---|
| Wounds & Gifts | `wounds` | Q1 (5-8 min), Q2 (8-10 min), Q3 (20-30 min) |
| Hero's Journey | `heros-journey` | Q1 (3-5 min), Q2 (10-12 min), Q3 (20-30 min) |
| Chakras | `chakras` | Q1 (3-5 min), Q2 (10-12 min), Q3 (20-30 min) |
| Individuation | `individuation` | Q1 (3-5 min), Q2 (8-10 min), Q3 (20-30 min) |
| Spiral Dynamics | `spiral-dynamics` | Q1 (3-5 min), Q2 (8-10 min), Q3 (20-30 min) |
| Integral AQAL | `integral-aqal` | Q1 (3-5 min), Q2 (8-10 min), Q3 (20-30 min) |

---

## Acceptance criteria

- [ ] Single entry point `/questionnaire` routes to any questionnaire by name
- [ ] No-argument invocation asks which questionnaire, showing progress per type
- [ ] Progress detection reads `## Q1 Reading` / `## Q2 Reading` / `## Q3 Reading` from the map file
- [ ] Auto-prompts next stage with a one-sentence description; offers an easy exit
- [ ] Name + number argument jumps directly to that stage, skipping all prompts
- [ ] Redo flow confirms once and preserves all prior readings
- [ ] Full question content and scoring come from the individual questionnaire SKILL.md — not duplicated here
- [ ] The individual questionnaire skills remain functional and invocable directly (they are not removed)
- [ ] Any questionnaire can be done in any order and any stage can be redone at any time

---

## Tone reminders

- Keep the routing step brief. The user came to do the questionnaire, not to navigate a menu.
- When auto-prompting Q2 or Q3, name specifically what it adds in one sentence. Do not list features.
- Once in the questionnaire, follow the tone of the individual skill exactly.
