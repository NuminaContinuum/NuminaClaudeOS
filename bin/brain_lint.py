#!/usr/bin/env python3
"""
Corpus-wide health check for the Numina OS memory layer.

Ported from PM-OS 2026-09-30. Durable areas are patterns/, commitments/,
relationships/, archetypes/, maps/ per .memory-config.md. Raw capture
(journals, dreams, meditations, journeys) is never audited, matching the
hook's own no-enforcement tier.

The write-time hook (validate_memory_file.py) audits ONE file at the moment it is
written. That catches a malformed claim but it cannot see the corpus: a citation
that pointed at an ingestion file nobody ever wrote still passes, because the file
being written is fine. On 2026-09-25 that gap cost 28 dangling provenance links in
the hypothesis card, found five weeks late by a manual sweep.

This is the sweep, as a script. Four checks:

  1. links      — internal markdown links that don't resolve
  2. pipeline   — source/ artifacts with no ingestion/ synthesis (and the reverse)
  3. index      — files missing from their area's INDEX.md (and areas with no INDEX)
  4. freshness  — durable files carrying no updated-date

Read-only. Never writes, never fixes. Exits 0 even when it finds problems, so a
SessionStart hook can run it without ever blocking a session (use --strict to get a
non-zero exit in CI).

Usage:
  bin/brain_lint.py                 full report
  bin/brain_lint.py --summary       one line per check (SessionStart hook)
  bin/brain_lint.py --check links   run one check
  bin/brain_lint.py --verbose       list every offender instead of capping at 10
  bin/brain_lint.py --json          machine-readable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import unquote

MEMORY_ROOT_MARKER = ".memory-root"
PIPELINE_DIRS = ("source", "ingestion", "hypotheses", "decisions")

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
FENCED_CODE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*$",
                            re.DOTALL | re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

# Template/example files legitimately contain placeholder links and no real content.
EXEMPT_NAMES = {"_SCHEMA.md", "PROVENANCE.md", ".memory-config.md"}

# Areas whose files should appear in a sibling INDEX.md, and where durable
# knowledge is expected to carry a freshness date.
INDEXED_AREAS = ("patterns", "commitments")
DURABLE_AREAS = ("patterns", "commitments", "relationships", "archetypes", "maps")

# A freshness date can be YAML frontmatter (`updated: 2026-09-25`) or the trailing
# prose convention this brain already uses ("Created ..., updated 2026-09-23.").
FRONTMATTER_UPDATED_RE = re.compile(r"^updated:\s*(\d{4}-\d{2}-\d{2})", re.MULTILINE)
PROSE_UPDATED_RE = re.compile(r"\bupdated\b[^.\n]{0,40}?(\d{4}-\d{2}-\d{2})", re.IGNORECASE)


def strip_code(text: str) -> str:
    text = HTML_COMMENT_RE.sub("", text)
    text = FENCED_CODE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def find_memory_root(start: Path) -> Path | None:
    """Locate the memory root by its marker, searching down from `start` then up."""
    for marker in sorted(start.glob("*/" + MEMORY_ROOT_MARKER)):
        return marker.parent
    cur = start.resolve()
    while True:
        if (cur / MEMORY_ROOT_MARKER).is_file():
            return cur
        if sum(1 for d in PIPELINE_DIRS if (cur / d).is_dir()) >= 2:
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent


def md_files(root: Path, area: str):
    d = root / area
    if not d.is_dir():
        return
    for p in sorted(d.rglob("*.md")):
        if p.name in EXEMPT_NAMES or p.name == "INDEX.md":
            continue
        yield p


# ----- check 1: links -----

def check_links(root: Path) -> list[str]:
    problems = []
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root)
        if p.name in EXEMPT_NAMES:
            continue
        if rel.parts and rel.parts[0] == "source":
            continue  # source/ is immutable and may cite things outside the brain
        try:
            text = strip_code(p.read_text(encoding="utf-8"))
        except OSError:
            continue
        for m in LINK_RE.finditer(text):
            target = m.group(2).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            if "{{" in target or ("<" in target and ">" in target):
                continue
            if not (p.parent / unquote(target)).exists():
                problems.append(f"{rel.as_posix()} -> {target}")
    return problems


# ----- check 2: pipeline pairing -----

# Meetily exports a meeting as both a transcript and an "-ai-summary" file. One synthesis
# covers the meeting, so `X-ai-summary.md` in source/ is satisfied by `ingestion/.../X.md`
# and vice versa. Without this, seven real meetings report as unsynthesized every sweep.
_VARIANT_SUFFIXES = ("-ai-summary", "-summary", "-transcript")
_SOURCE_EXTS = ("", ".md", ".vtt", ".docx", ".pdf", ".xlsx", ".pptx",
                ".txt", ".csv", ".eml", ".html")


def _base_stems(stem: str):
    """The stem itself, plus the stem with a known export-variant suffix stripped."""
    out = [stem]
    for suf in _VARIANT_SUFFIXES:
        if stem.endswith(suf):
            out.append(stem[: -len(suf)])
    return out


def _cites_source(path: Path, root: Path) -> bool:
    """True when the file contains a markdown link that resolves to a file under source/."""
    try:
        text = strip_code(path.read_text(encoding="utf-8"))
    except OSError:
        return False
    for m in LINK_RE.finditer(text):
        target = m.group(2).split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / unquote(target)).resolve()
        if not resolved.is_file():
            continue
        try:
            parts = resolved.relative_to(root.resolve()).parts
        except ValueError:
            continue
        if parts and parts[0] == "source":
            return True
    return False


def _cited_source_files(root: Path) -> set:
    """Every source/ artifact that ANY file outside source/ links to.

    A source artifact is accounted for in two legitimate ways, and only one of them is
    visible to filename pairing:
      - a synthesis covers it, possibly under a different name (one synthesis per meeting
        when an export produced two files; one synthesis covering several interviews;
        an analysis named for its subject rather than its export)
      - it is cited directly as a provenance tag, which PROVENANCE.md explicitly permits
        "when the source is self-explanatory and synthesis would be ceremony"
    Both mean the artifact has been read. Only an artifact nobody references is unread.
    """
    cited = set()
    for p in root.rglob("*.md"):
        rel = p.relative_to(root)
        if rel.parts and rel.parts[0] == "source":
            continue
        try:
            text = strip_code(p.read_text(encoding="utf-8"))
        except OSError:
            continue
        for m in LINK_RE.finditer(text):
            target = m.group(2).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (p.parent / unquote(target)).resolve()
            if not resolved.is_file():
                continue
            try:
                r = resolved.relative_to(root.resolve())
            except ValueError:
                continue
            if r.parts and r.parts[0] == "source":
                cited.add(r)
    return cited


def check_pipeline(root: Path) -> list[str]:
    problems = []
    src, ing = root / "source", root / "ingestion"
    if not src.is_dir() or not ing.is_dir():
        return problems
    cited = _cited_source_files(root)
    for p in sorted(src.rglob("*")):
        if not p.is_file() or p.name.startswith("."):
            continue
        rel = p.relative_to(src)
        if any((ing / rel.parent / (s + ".md")).exists()
               for s in _base_stems(rel.stem)):
            continue
        if Path("source") / rel in cited:
            continue
        problems.append(f"no synthesis: source/{rel.as_posix()}")
    for p in sorted(ing.rglob("*.md")):
        if p.name.startswith("."):
            continue
        rel = p.relative_to(ing)
        # A synthesis that CITES a real source/ artifact is sourced, whatever it is named.
        # One synthesis may cover several artifacts, or an analysis may be named for its
        # subject rather than its export file — both are correct practice and neither
        # matches on filename.
        if _cites_source(p, root):
            continue
        found = False
        for stem in _base_stems(rel.stem):
            base = src / rel.parent / stem
            if any(base.with_suffix(s).exists() for s in _SOURCE_EXTS):
                found = True
                break
            # reverse direction: ingestion/X.md covered by source/X-ai-summary.*
            for suf in _VARIANT_SUFFIXES:
                v = src / rel.parent / (stem + suf)
                if any(v.with_suffix(s).exists() for s in _SOURCE_EXTS):
                    found = True
                    break
            if found:
                break
        if not found:
            problems.append(f"no source: ingestion/{rel.as_posix()}")
    return problems


# ----- check 3: INDEX coverage -----

def check_index(root: Path) -> list[str]:
    problems = []
    for area in INDEXED_AREAS:
        d = root / area
        if not d.is_dir():
            continue
        index = d / "INDEX.md"
        files = list(md_files(root, area))
        if not index.exists():
            if files:
                problems.append(
                    f"{area}/ has {len(files)} files and no INDEX.md")
            continue
        try:
            body = index.read_text(encoding="utf-8")
        except OSError:
            continue
        for p in files:
            if p.stem not in body:
                problems.append(f"missing from {area}/INDEX.md: {p.stem}")
    return problems


# ----- check 4: freshness -----

def freshness_date(text: str):
    m = FRONTMATTER_UPDATED_RE.search(text)
    if m:
        return m.group(1)
    tail = text[-600:]
    hits = PROSE_UPDATED_RE.findall(tail)
    return hits[-1] if hits else None


def check_freshness(root: Path, stale_days: int = 42) -> list[str]:
    problems, today = [], date.today()
    for area in DURABLE_AREAS:
        for p in md_files(root, area):
            rel = p.relative_to(root)
            try:
                text = p.read_text(encoding="utf-8")
            except OSError:
                continue
            d = freshness_date(text)
            if not d:
                problems.append(f"no updated-date: {rel.as_posix()}")
                continue
            try:
                age = (today - datetime.strptime(d, "%Y-%m-%d").date()).days
            except ValueError:
                problems.append(f"unparseable updated-date ({d}): {rel.as_posix()}")
                continue
            if age > stale_days:
                problems.append(f"stale {age}d (updated {d}): {rel.as_posix()}")
    return problems


# ----- check 5: decision debt -----

_FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


def _frontmatter(text: str) -> dict:
    m = _FM_RE.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def check_decisions(root: Path, ratify_days: int = 14) -> list[str]:
    """A `proposed` decision is captured but not yet ratified by the PM. That is the right
    state on day one and a smell by week three: the whole point of ambient capture is that
    /review confirms or kills promptly. Also flags a decision file whose status is missing
    or outside the enum."""
    problems, today = [], date.today()
    valid = {"proposed", "pending", "decided", "superseded"}
    d = root / "decisions"
    if not d.is_dir():
        return problems
    for p in sorted(d.rglob("*.md")):
        if p.name in EXEMPT_NAMES or p.name == "INDEX.md":
            continue
        rel = p.relative_to(root)
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        meta = _frontmatter(text)
        status = meta.get("status", "")
        if status not in valid:
            problems.append(f"status '{status or 'missing'}' not in the enum: {rel.as_posix()}")
            continue
        if status in ("proposed", "pending"):
            d0 = meta.get("updated", "")
            try:
                age = (today - datetime.strptime(d0, "%Y-%m-%d").date()).days
            except ValueError:
                continue
            if age > ratify_days:
                problems.append(
                    f"{status} {age}d, needs confirm/kill in /review: {rel.as_posix()}")
    return problems


_CONFLICT_RE = re.compile(r"^>\s*\[!CONFLICT\]\s*(.*)$", re.MULTILINE)
_CONFLICT_STATUS_RE = re.compile(r"^>\s*\*\*Status:\*\*\s*(\w+)", re.MULTILINE)


def check_conflicts(root: Path) -> list[str]:
    """Report open [!CONFLICT] blocks, and any block missing a Status line.

    Not failures — an open conflict is the correct state until the PM resolves it. This
    surfaces them so they are counted rather than accumulating quietly in files nobody
    re-reads, which is the failure mode the marker exists to prevent.
    """
    problems = []
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root)
        if (rel.parts and rel.parts[0] == "source") or p.name in EXEMPT_NAMES:
            continue
        try:
            text = strip_code(p.read_text(encoding="utf-8"))
        except OSError:
            continue
        blocks = list(_CONFLICT_RE.finditer(text))
        if not blocks:
            continue
        statuses = _CONFLICT_STATUS_RE.findall(text)
        for i, m in enumerate(blocks):
            label = m.group(1).strip()[:70] or "(unlabelled)"
            status = statuses[i].lower() if i < len(statuses) else ""
            if status == "open":
                problems.append(f"open conflict: {rel.as_posix()} :: {label}")
            elif not status:
                problems.append(f"conflict with no Status line: {rel.as_posix()} :: {label}")
    return problems


# ---- Numina staleness: measured from evidence dates, not file frontmatter ----
# /sweep checks 1, 2 and 4 ask "no new evidence in N days", and Numina tags evidence
# with (lived-experience, YYYY-MM-DD) / (dream, ...) / (somatic, ...) rather than with
# an `updated:` header. So freshness here reads the newest evidence date INSIDE the
# file. Reporting "no updated-date" on all 180 durable files, as the PM-OS check did,
# was an artifact of porting a path-and-frontmatter model onto a date-based one.
_EVIDENCE_DATE_RE = re.compile(r"\((?:[a-z-]+),\s*(\d{4}-\d{2}-\d{2})\)")
_ANY_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

# windows straight from .claude/commands/sweep.md
_STALE_WINDOW = {"patterns": 60, "commitments": 30, "relationships": 60, "archetypes": 60}
QUIET_HORIZON_DAYS = 365


def check_staleness(root: Path) -> list[str]:
    problems, today = [], date.today()
    for area, window in _STALE_WINDOW.items():
        d = root / area
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*.md")):
            if p.name in EXEMPT_NAMES or p.name == "INDEX.md":
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            # Newest of any date: appended "- YYYY-MM-DD — ..." lines carry no tag but are
            # still new evidence, and reading only tagged dates hid them.
            dates = _EVIDENCE_DATE_RE.findall(text) + _ANY_DATE_RE.findall(text)
            if not dates:
                problems.append(f"no dated evidence at all: {p.relative_to(root).as_posix()}")
                continue
            try:
                newest = max(datetime.strptime(x, "%Y-%m-%d").date() for x in dates)
            except ValueError:
                continue
            age = (today - newest).days
            # Imported dream figures from 2017 are not "going quiet"; they were never loud.
            # For people and symbols, only flag what was alive in the past year and has
            # since gone quiet, which is the question /sweep check 4 actually asks.
            if area in ("relationships", "archetypes") and age > QUIET_HORIZON_DAYS:
                continue
            if age > window:
                problems.append(
                    f"{area}: no new evidence in {age}d (window {window}d, newest {newest}): "
                    f"{p.relative_to(root).as_posix()}")
    return problems


def _durable_dates(root: Path) -> set:
    """Every YYYY-MM-DD referenced anywhere in the durable layer. Numina cites a raw
    entry by the date it happened, not by path, so this is how you tell whether a
    captured entry actually reached patterns/archetypes/relationships."""
    seen = set()
    for area in ("patterns", "commitments", "relationships", "archetypes", "maps"):
        d = root / area
        if not d.is_dir():
            continue
        for p in d.rglob("*.md"):
            try:
                seen.update(_ANY_DATE_RE.findall(p.read_text(encoding="utf-8", errors="replace")))
            except OSError:
                pass
    return seen


def check_backlog(root: Path) -> list[str]:
    """/sweep check 6: entries captured but never synthesised into ingestion/.

    Annotated with whether the entry's date already appears in the durable layer,
    because the two cases need different attention: an entry nothing references is
    genuinely unread, while one cited in 22 files has reached the brain and is only
    missing its synthesis step.
    """
    problems = []
    src, ing = root / "source", root / "ingestion"
    if not src.is_dir():
        return problems
    cited = _durable_dates(root)
    for p in sorted(src.rglob("*")):
        if not p.is_file() or p.name.startswith("."):
            continue
        rel = p.relative_to(src)
        if any((ing / rel.parent / (s + ".md")).exists() for s in _base_stems(rel.stem)):
            continue
        if _cites_source(p, root) or (Path("source") / rel) in _cited_source_files(root):
            continue
        m = _ANY_DATE_RE.match(rel.stem)
        tag = ""
        if m:
            tag = " [already cited in the durable layer]" if m.group(1) in cited \
                  else " [NOT referenced anywhere - genuinely unread]"
        problems.append(f"no synthesis: source/{rel.as_posix()}{tag}")
    return problems


def _pipeline_start(root: Path) -> date:
    """The memory layer's install date, from the `Installed: YYYY-MM-DD` line in
    .memory-config.md. Raw entries before it were harvested in bulk and are not
    expected to have ingestion notes. No line means every entry counts."""
    cfg = root / ".memory-config.md"
    if cfg.exists():
        m = re.search(r"^Installed:\s*(\d{4}-\d{2}-\d{2})", cfg.read_text(encoding="utf-8"), re.MULTILINE)
        if m:
            return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    return date.min

RAW_AREAS = ("journals", "dreams", "journeys", "meditations")
_RANGE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})\s*(?:to|through|-to-|and)\s*(?:(\d{4})-)?(\d{2}-\d{2})")


def _ingested_dates(root: Path, area: str) -> set:
    """Every date an ingestion/<area>/ (or adhoc/) note covers: dates in its own scope
    lines, plus the days inside any 'YYYY-MM-DD to [YYYY-]MM-DD' range there."""
    covered = set()
    for ing in (root / "ingestion" / area, root / "ingestion" / "adhoc"):
        if not ing.is_dir():
            continue
        for p in ing.rglob("*.md"):
            try:
                body = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            # Only the note's own scope counts: its filename, title, Source and
            # Individual-files lines. Ingestion notes cite many older dates as context,
            # and counting those would mark entries as synthesised that never were.
            head = [ln for ln in body.splitlines()
                    if ln.startswith("# ") or ln.startswith("**Source:**")
                    or ln.startswith("**Individual files:**")]
            text = p.name + "\n" + "\n".join(head)
            covered.update(_ANY_DATE_RE.findall(text))
            for a, y, md in _RANGE_RE.findall(text.replace("batch-", "")):
                try:
                    start = datetime.strptime(a, "%Y-%m-%d").date()
                    end = datetime.strptime(f"{y or a[:4]}-{md}", "%Y-%m-%d").date()
                except ValueError:
                    continue
                if 0 < (end - start).days <= 62:
                    for i in range((end - start).days + 1):
                        covered.add((start + timedelta(days=i)).isoformat())
    return covered


def check_raw_backlog(root: Path) -> list[str]:
    """Entries in journals/dreams/journeys/meditations since the pipeline started that no
    ingestion/ note covers. check_backlog only sees source/, so anything logged without a
    source copy (most single /dream or /journal runs before 2026-10-01) slipped past it."""
    problems = []
    start = _pipeline_start(root)
    for area in RAW_AREAS:
        d = root / area
        if not d.is_dir():
            continue
        covered = _ingested_dates(root, area)
        for p in sorted(d.glob("*.md")):
            m = _ANY_DATE_RE.match(p.name)
            if not m:
                continue
            try:
                dt = datetime.strptime(m.group(1), "%Y-%m-%d").date()
            except ValueError:
                continue
            if dt < start or m.group(1) in covered:
                continue
            problems.append(f"no ingestion note covers: {area}/{p.name}")
    return problems


_TENSION_RE = re.compile(r"^>\s*\[!(?:TENSION|CONFLICT)\]\s*(.*)$", re.MULTILINE)


def check_tensions(root: Path) -> list[str]:
    """Open [!TENSION] blocks in durable files. Not failures: an open tension is the
    correct state until the user resolves it. Counted so they stay visible."""
    problems = []
    for area in ("patterns", "commitments", "relationships", "archetypes"):
        d = root / area
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*.md")):
            try:
                text = strip_code(p.read_text(encoding="utf-8"))
            except OSError:
                continue
            statuses = _CONFLICT_STATUS_RE.findall(text)
            for i, m in enumerate(_TENSION_RE.finditer(text)):
                status = statuses[i].lower() if i < len(statuses) else ""
                if status != "resolved":
                    label = m.group(1).strip()[:70] or "(unlabelled)"
                    problems.append(f"open tension: {p.relative_to(root).as_posix()} :: {label}")
    return problems


_OPEN_ITEM_RE = re.compile(r"^- \[ \] (.+)$", re.MULTILINE)


def check_open(root: Path) -> list[str]:
    """Unanswered items in OPEN.md, the single queue of decisions waiting on the user."""
    p = root / "OPEN.md"
    if not p.exists():
        return []
    return [f"waiting: {m.strip()[:110]}" for m in _OPEN_ITEM_RE.findall(p.read_text(encoding="utf-8"))]


CHECKS = {
    "links": ("internal links that don't resolve", check_links),
    "backlog": ("captured but never synthesised (/sweep check 6)", check_backlog),
    "index": ("files missing from their area INDEX", check_index),
    "staleness": ("durable files past their /sweep evidence window", check_staleness),
    "raw": ("entries since the memory layer was installed with no ingestion note", check_raw_backlog),
    "tensions": ("open [!TENSION] blocks in durable files", check_tensions),
    "open": ("decisions waiting in OPEN.md", check_open),
}


# /sweep is monthly or seasonal for Numina, not weekly as in PM-OS.
REVIEW_ENVELOPE_DAYS = 35


def _review_staleness(root: Path):
    """(days, date-string) since the newest maintenance report, or None.

    Cadence is the thing that actually kills a memory layer — Huryn's envelope is that
    three consecutive missed weeks turns the brain into a graveyard, and this one has
    already had gaps of 31 and 35 days. The sweep is cheap now; what was missing is
    anything telling you it is due. This line rides along with the SessionStart summary,
    which is the place you already look.
    """
    d = root / "maintenance"
    if not d.is_dir():
        return None
    newest = None
    for p in list(d.glob("*-sweep*.md")) + list(d.glob("*-review.md")):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", p.name)
        if not m:
            continue
        try:
            dt = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        if newest is None or dt > newest:
            newest = dt
    if newest is None:
        return None
    return (date.today() - newest).days, newest.isoformat()


RETRIEVAL_REVISIT_FILES = 400


def _corpus_size(root: Path) -> int:
    """Total markdown files in the brain. The retrieval question (T10) is gated on scale:
    grep-and-route works until it doesn't, and the agreed revisit point is ~400 files.
    Printing it here means the trigger fires on its own instead of living in a ticket
    nobody re-reads."""
    try:
        return sum(1 for _ in root.rglob("*.md"))
    except OSError:
        return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Corpus health check for the memory layer.")
    ap.add_argument("--check", choices=sorted(CHECKS), action="append",
                    help="run only this check (repeatable)")
    ap.add_argument("--summary", action="store_true", help="one line per check")
    ap.add_argument("--verbose", action="store_true", help="list every offender")
    ap.add_argument("--json", action="store_true", dest="as_json")
    ap.add_argument("--quiet", action="store_true", help="print nothing when all checks pass")
    ap.add_argument("--strict", action="store_true", help="exit 1 when problems are found")
    ap.add_argument("--root", help="memory root (default: auto-discover)")
    args = ap.parse_args()

    root = Path(args.root) if args.root else find_memory_root(Path.cwd())
    if root is None or not root.is_dir():
        print("brain_lint: no memory root found (looked for .memory-root)", file=sys.stderr)
        return 0

    selected = args.check or sorted(CHECKS)
    results = {name: CHECKS[name][1](root) for name in selected}
    total = sum(len(v) for v in results.values())

    if args.as_json:
        print(json.dumps({"root": str(root), "total": total, "results": results}, indent=2))
        return 1 if (args.strict and total) else 0

    size = _corpus_size(root)
    size_line = ""
    if size >= RETRIEVAL_REVISIT_FILES:
        size_line = (f"  \u26a0 {size} files \u2014 past the {RETRIEVAL_REVISIT_FILES} mark "
                     "where plain-file search starts to strain; worth raising at the next /sweep")

    stale_review = _review_staleness(root)
    review_line = ""
    if stale_review and stale_review[0] > REVIEW_ENVELOPE_DAYS:
        review_line = (f"  \u26a0 last /sweep was {stale_review[0]} days ago "
                       f"({stale_review[1]}) \u2014 the envelope is {REVIEW_ENVELOPE_DAYS}")

    if args.quiet and not total and not size_line and not (
            stale_review and stale_review[0] > REVIEW_ENVELOPE_DAYS):
        return 0

    if total == 0:
        print(f"brain_lint: clean ({len(selected)} checks, {root.name}/)")
        if review_line:
            print(review_line)
        if size_line:
            print(size_line)
        return 0

    cap = 10**6 if args.verbose else 10
    if args.summary:
        print(f"brain_lint: {total} issues in {root.name}/")
        for name in selected:
            n = len(results[name])
            if n:
                print(f"  {name:<10} {n:>4}  {CHECKS[name][0]}")
        if review_line:
            print(review_line)
        if size_line:
            print(size_line)
        print("  run `bin/brain_lint.py` for detail")
    else:
        print(f"brain_lint: {total} issues in {root.name}/")
        if review_line:
            print(review_line)
        if size_line:
            print(size_line)
        print()
        for name in selected:
            hits = results[name]
            if not hits:
                print(f"[{name}] clean\n")
                continue
            print(f"[{name}] {len(hits)} — {CHECKS[name][0]}")
            for h in hits[:cap]:
                print(f"  {h}")
            if len(hits) > cap:
                print(f"  ... and {len(hits) - cap} more (--verbose)")
            print()

    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
