#!/usr/bin/env python3
"""
Stop hook — session-end consolidation pass for Numina OS.

When the session ends with uncommitted changes in the brain (patterns/, commitments/,
source/, ingestion/, archetypes/, relationships/, maps/), nudges the companion to
consolidate before stopping. Human-in-loop, in the same context that did the work.

Contract:
  - stdin carries `stop_hook_active`. When true, already continuing from a prior block — exit 0.
  - To nudge: print JSON to stdout: {"decision": "block", "reason": "<instruction>"}
  - Print nothing (exit 0) to let the session end normally.

Safe: if not a git repo, or nothing in the brain changed, stays silent.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

_PIPELINE_DIRS = ("source", "ingestion", "patterns", "commitments")
_MEMORY_ROOT_MARKER = ".memory-root"
_MEMORY_CONFIG = ".memory-config.md"

_CONSOLIDATION_CHECKLIST = (
    "Before we close — a few things worth carrying forward from this session:\n"
    "1. Anything that appeared across multiple entries today — a symbol, a theme, a feeling "
    "— worth noting in ingestion/ if it isn't already there.\n"
    "2. If something crossed the promotion bar (3+ modalities, or you flagged it as "
    "significant), ask whether to name it as a pattern. Always ask first — never auto-promote.\n"
    "3. Update INDEX.md in patterns/ or commitments/ if any files were added or changed.\n"
    "4. If a relationship or archetype file was created or updated, check it reads right.\n"
    "5. Then commit: `git add -A && git commit -m \"memory: consolidate <session topic>\"`. "
    "Never push.\n"
    "If nothing meets the promotion bar, say so in one line and commit the raw capture "
    "anyway so it isn't lost."
)


def _memory_roots(cwd: Path) -> set[str]:
    roots: set[str] = set()
    for pat in (_MEMORY_ROOT_MARKER, "*/" + _MEMORY_ROOT_MARKER, "*/*/" + _MEMORY_ROOT_MARKER):
        try:
            for marker in cwd.glob(pat):
                rel = marker.parent.relative_to(cwd).as_posix()
                roots.add("" if rel == "." else rel)
        except OSError:
            pass
    return roots


def _promotion_homes(cwd: Path, roots: set[str]) -> set[str]:
    homes: set[str] = set()
    for r in roots:
        cfg = cwd / (f"{r}/{_MEMORY_CONFIG}" if r else _MEMORY_CONFIG)
        try:
            text = cfg.read_text(encoding="utf-8")
        except OSError:
            continue
        for line in text.splitlines():
            if not line.lstrip().startswith("|"):
                continue
            for m in re.finditer(r"`([^`]+)`", line):
                tok = m.group(1).strip()
                if "/" not in tok:
                    continue
                seg = tok.lstrip("./").split("/")[0]
                if seg and "<" not in seg:
                    homes.add(seg)
    return homes


def _read_payload() -> dict:
    try:
        raw = sys.stdin.read()
    except Exception:
        return {}
    if not raw.strip():
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


def _cwd(payload: dict) -> Path:
    c = payload.get("cwd")
    if isinstance(c, str) and c:
        return Path(c)
    return Path.cwd()


def _git_porcelain(cwd: Path) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all"],
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout


def _path_touches_brain(path: str, roots: set[str], homes: set[str], cwd: Path) -> bool:
    path = path.strip().strip('"')
    segs = [s for s in path.split("/") if s]
    if not segs:
        return False
    for r in roots:
        if r and (path == r or path.startswith(r + "/")):
            return True
    if "" in roots and (segs[0] in _PIPELINE_DIRS or segs[0] in homes):
        return True
    if segs[0] in homes:
        return True
    if not roots:
        for idx, s in enumerate(segs):
            if s in _PIPELINE_DIRS:
                parent = cwd / Path(*segs[:idx]) if idx else cwd
                try:
                    if sum(1 for d in _PIPELINE_DIRS if (parent / d).is_dir()) >= 2:
                        return True
                except OSError:
                    pass
    return False


def _brain_dirty(porcelain: str, cwd: Path) -> bool:
    roots = _memory_roots(cwd)
    homes = _promotion_homes(cwd, roots)
    for line in porcelain.splitlines():
        path = line[3:].strip()
        if " -> " in path:
            old, new = path.split(" -> ", 1)
            if (_path_touches_brain(old, roots, homes, cwd)
                    or _path_touches_brain(new, roots, homes, cwd)):
                return True
        elif _path_touches_brain(path, roots, homes, cwd):
            return True
    return False


def main() -> int:
    payload = _read_payload()
    if payload.get("stop_hook_active") is True:
        return 0

    cwd = _cwd(payload)
    porcelain = _git_porcelain(cwd)
    if porcelain is None:
        return 0
    if not porcelain.strip() or not _brain_dirty(porcelain, cwd):
        return 0

    print(json.dumps({"decision": "block", "reason": _CONSOLIDATION_CHECKLIST}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
