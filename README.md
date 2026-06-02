# Numina OS

**An operating system for inner work, built on Claude Code.**

A purpose-built context layer for people who already use Claude Code as a thinking environment and want a coherent home for journaling, dreamwork, journey integration, meditation logs, and synthesis across all of it.

Free. Local. Yours.

> "Where ancient wisdom meets living intelligence."

---

## What this is

Numina OS turns a folder on your machine into a living memory for your inner work. You bring entries — journals, dreams, journey notes, meditation sits — and Numina OS:

- Captures and structures them
- Surfaces recurring themes, symbols, and people across content types
- Generates living maps of your journey (timeline, relationships, archetypes, plus framework maps like Hero's Journey or AQAL)
- Holds space when you're integrating something difficult, without playing therapist

It's a set of skills you invoke from Claude Code (`/journal`, `/dream`, `/integrate`, `/meditation`, `/harvest`, `/maps`, `/compass`, `/inner-review`, `/setup`). Everything stays in plain markdown files in your `context-library/`.

---

## Who this is for

You'll get the most out of Numina OS if you:

- Already use Claude Code or a similar terminal-native AI workflow
- Have a contemplative, therapeutic, or psychospiritual practice you care about
- Want your inner work in plain text, not in a SaaS database
- Are comfortable running slash commands and editing markdown

If you'd rather a polished UI, the Numina app at [numinacontinuum.org](https://numinacontinuum.org) is being built for that.

---

## Prerequisites

- [Claude Code](https://docs.claude.com/claude-code) installed and working
- An Anthropic API key or Claude subscription
- Comfort with the terminal and markdown files

---

## Install

```bash
git clone https://github.com/numinacontinuum/numina-os.git
cd numina-os
claude
```

Once Claude Code opens, run:

```
/setup
```

This walks you through a 4-question onboarding ritual and creates your `context-library/profile.md`. Every other skill reads this file, so do this first.

---

## The skills

| Skill | Command | What it does |
|-------|---------|---------|
| Profile setup | `/setup` | 4-question onboarding, creates your profile |
| Journal | `/journal` | Process a journal entry, surface themes, ask one deepening question |
| Dream | `/dream` | Log and interpret a dream through your framework lens |
| Integrate | `/integrate` | Phase-aware container for psychedelic, shamanic, breathwork, and peak experiences |
| Meditation | `/meditation` | Log a sit with technique, duration, depth, and phenomenological notes |
| Harvest | `/harvest` | Bulk import existing content from a single file |
| Maps | `/maps` | Generate or refresh your living maps (universal + framework) |
| Inner review | `/inner-review` | Weekly reflection across the past 7 days |
| Compass | `/compass` | Synthesize across everything: what's the blocker, how to work on it, what to share next |
| Chakra questionnaire | `/chakra-questionnaire` | Staged chakra assessment — quick read, then a deeper dive into direction and embodiment. Resumes where you left off |
| Hero's Journey questionnaire | `/heros-journey-questionnaire` | Staged Hero's Journey assessment — placement on the arc, then a deeper dive into allies, ordeal, and elixir |
| Wounds questionnaire | `/wounds-questionnaire` | Staged wounds assessment — quick read of which of the 5 primary wounds are most activated right now |
| Individuation questionnaire | `/individuation-questionnaire` | Jung individuation — places your primary stage on the arc (Persona, Shadow, Anima/Animus, Wise Elder, Self) |
| Spiral Dynamics questionnaire | `/spiral-dynamics-questionnaire` | Finds your center of gravity on the spiral (vMeme), resolved via a short tiebreaker |
| Integral AQAL questionnaire | `/integral-aqal-questionnaire` | Finds your home quadrant — the perspective you most naturally inhabit (I / It / We / Its) |

Detailed instructions for each skill live in `.claude/skills/<name>/SKILL.md`.

---

## How your data is stored

Everything stays on your machine in plain markdown.

```
context-library/
├── profile.md             your onboarding answers
├── journals/              one file per entry
├── dreams/                one file per entry
├── journeys/              one file per entry
├── meditations/           one file per sit
├── integrations/          longer-form integration notes
├── relationships/         one file per person you mention
├── archetypes/            one file per recurring symbol or archetype
└── maps/
    ├── timeline.md        chronological arc of your journey
    ├── relationships.md   who's in your life, weighted
    ├── archetypes.md      what's recurring, weighted
    ├── heros-journey.md   (if Depth psychology / Mystical traditions selected)
    ├── individuation.md   (if Depth psychology selected)
    ├── spiral-dynamics.md (if Integral theory selected)
    └── integral-aqal.md   (if Integral theory selected)
```

Content-processing skills auto-update the records as they run. People get added to `relationships/`, archetypes to `archetypes/`, notable events to `timeline.md`. You don't have to remember to do this.

`/maps` reads those records to refresh the high-level overviews.

---

## A note on what this is not

Numina OS is **not** therapy, medical advice, or a substance guide.

- It will not diagnose mental health conditions
- It will not recommend doses, substances, or routes of administration
- It will not validate or discourage your choices around any practice
- It is not a replacement for a therapist, integration coach, or sangha

If you are processing trauma, in acute distress, or working with substances, please also have a human container — therapist, integration circle, trusted friend.

The skill files are intentionally written with trauma-aware language and refusal patterns. If something feels off, edit the SKILL.md to match how you want to be met.

---

## Privacy

- Your `context-library/` is gitignored by default. Nothing in it is committed unless you change `.gitignore`.
- Numina OS does not phone home. The only network calls happen through Claude Code itself, which sends prompts to Anthropic's API per their terms.
- If you fork or share this repo, double-check the `.gitignore` before pushing.

---

## Acknowledgements

Numina OS builds on a pattern established in the Claude Code community: a project-specific CLAUDE.md, a `context-library/` of plain markdown records, and skills invoked as slash commands. The skill structure, CLAUDE.md convention, and "context library" terminology come from that shared lineage. Numina OS applies the pattern to inner work.

---

## Contribute

This is v1. The skills will evolve as users push back. If a prompt feels too cold, too prescriptive, too clinical, or just wrong for your tradition: open an issue or a PR.

Particularly wanted:

- Framework map prompts that go deeper (Finding the Ox, 16 Insight Knowledges — these are v2)
- Tradition-specific edits (Buddhist sanghas, Sufi orders, IFS practitioners, somatic schools)
- Trauma-aware refusal patterns we missed

---

## Licence

MIT. Use it. Fork it. Make it yours.

---

Built with care by [Numina Continuum](https://numinacontinuum.org).
