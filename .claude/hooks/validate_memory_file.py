#!/usr/bin/env python3
"""
PostToolUse hook — validates a just-written memory file before the agent claims success.

Runs after Write/Edit. Only enforces schema on files under `patterns/` or `commitments/`
— the durable layer where orphan evidence causes the most damage. Raw capture files
(journals/, dreams/, meditations/, journeys/) are never interrupted.

Two severity tiers:

  BLOCKING (exit 2 — stderr is fed back to the model, which fixes and retries):
    - Evidence row with ZERO provenance attempt in patterns/ or commitments/ only.
    Always fixable in-turn (add an (intuition, <date>) tag or a link).

  WARNING (exit 0 + stderr — informational):
    - Path-typed provenance link whose target doesn't resolve yet.
    - Any broken internal markdown link.

Adapted from Pawel Huryn's pm-brain validator and the PM-OS memory layer,
re-tuned for Numina OS's inner work context-library.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


# ----- provenance enum (inner work vocabulary) -----

_PROVENANCE_NON_PATH_RES = (
    # (lived-experience, YYYY-MM-DD)
    re.compile(r"\(\s*lived-experience\s*,\s*\d{4}-\d{2}-\d{2}\s*\)", re.IGNORECASE),
    # (dream, YYYY-MM-DD)
    re.compile(r"\(\s*dream\s*,\s*\d{4}-\d{2}-\d{2}\s*\)", re.IGNORECASE),
    # (somatic, YYYY-MM-DD)
    re.compile(r"\(\s*somatic\s*,\s*\d{4}-\d{2}-\d{2}\s*\)", re.IGNORECASE),
    # (reflection, YYYY-MM-DD)
    re.compile(r"\(\s*reflection\s*,\s*\d{4}-\d{2}-\d{2}\s*\)", re.IGNORECASE),
    # (pattern, N-occurrences)
    re.compile(r"\(\s*pattern\s*,\s*\d+[- ]occurrences?\s*\)", re.IGNORECASE),
    # (teacher-text, source-name) — source-name must be non-blank
    re.compile(r"\(\s*teacher-text\s*,\s*[^,\s)][^)]*\)", re.IGNORECASE),
    # (intuition, YYYY-MM-DD)
    re.compile(r"\(\s*intuition\s*,\s*\d{4}-\d{2}-\d{2}\s*\)", re.IGNORECASE),
)

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
_REF_DEF_RE = re.compile(r"^[ \t]*\[([^\]]+)\]:\s*(\S+)", re.MULTILINE)
_REF_FULL_RE = re.compile(r"\[([^\]]+)\]\[([^\]]*)\]")
_REF_SHORTCUT_RE = re.compile(r"\[([^\]]+)\](?!\s*[\(\[])")
_ROW_RE = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+(.*)$")

_AUDITED_HEADER_RE = re.compile(r"^evidence(?![\w-])", re.IGNORECASE)


def _is_audited_header(header: str) -> bool:
    h = re.sub(r"[*`]", "", header).strip().strip("_").strip()
    return bool(_AUDITED_HEADER_RE.match(h))


_BARE_PLACEHOLDER_RE = re.compile(
    r"^\s*[*_`]*\s*"
    r"\(?\s*(none(\s+yet)?|n/?a|tbd|todo|"
    r"nothing\s+yet|no\s+evidence(\s+yet)?|"
    r"not\s+yet|pending|open|[—–-])\s*\)?"
    r"\s*[*_`]*\s*[.!]?\s*$",
    re.IGNORECASE,
)

_PAREN_ABSENCE_RE = re.compile(
    r"^\s*[*_`]*\s*\(\s*"
    r"(?:none(?!\s+of)|nothing(?!\s+of)|no\s+evidence|n/?a|tbd|not\s+yet)"
    r"[^,)]*\)\s*[*_`]*\s*[.!]?\s*$",
    re.IGNORECASE,
)

_BOLD_EVIDENCE_LABEL_RE = re.compile(
    r"^\s*(?:[-*]\s+)?(?:\*\*|__)\s*Evidence\s+(?:for|against)\b[^*_:]*"
    r"(?::\s*(?:\*\*|__)|(?:\*\*|__)\s*:)"
    r"\s*(.*)$",
    re.IGNORECASE,
)

_FENCED_CODE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[ \t]*$", re.DOTALL | re.MULTILINE)
_INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_HEADER_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_MARKER_RE = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+")
_BOLD_LABEL_ONLY_RE = re.compile(r"^(?:\*\*|__)[^*_]+:(?:\*\*|__)\s*$")
_TEMPLATE_TOKEN_RE = re.compile(r"^<[^>]+>$")

_FIELD_LABEL_RE = re.compile(
    r"^(?:[-*]\s+|\d+[.)]\s+)?(?:\*\*|__)\s*"
    r"(?:origin|confidence|open\s+observations|caveats|integration\s+check|"
    r"status|resolution|meta|evidence\s+(?:for|against)|what\s+it\s+is|"
    r"why\s+it\s+matters|what\s+would\s+change\s+this|related\s+entries|linked)\b[^*_]*:(?:\*\*|__)",
    re.IGNORECASE,
)


def _strip_code_spans(text: str) -> str:
    text = _HTML_COMMENT_RE.sub("", text)
    text = _FENCED_CODE_RE.sub("", text)
    out = [ln if _HEADER_RE.match(ln) else _INLINE_CODE_RE.sub("", ln) for ln in text.split("\n")]
    return "\n".join(out)


def _is_empty_evidence_placeholder(row: str) -> bool:
    stripped = row.strip()
    return bool(_BARE_PLACEHOLDER_RE.match(stripped) or _PAREN_ABSENCE_RE.match(stripped))


def _is_template_placeholder(row: str) -> bool:
    stripped = row.strip()
    return "<provenance-tag>" in stripped or bool(_TEMPLATE_TOKEN_RE.match(stripped))


def _resolve_pipeline_link(raw_target: str, file_parent: Path, work_dir: Path):
    target = raw_target.split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None, ""
    target = unquote(target)
    segs = [s for s in target.split("/") if s and s != ".."]
    if "ingestion" not in segs and "source" not in segs:
        return None, ""
    if target.endswith("/"):
        return "warn", f"path-typed tag ends in '/', not a file: {target}"
    resolved = (file_parent / target).resolve()
    if not resolved.exists():
        return "warn", f"path-typed tag doesn't resolve yet: {target}"
    if not resolved.is_file():
        return "warn", f"path-typed tag points at a directory: {target}"
    try:
        rel = resolved.relative_to(work_dir.resolve())
    except ValueError:
        return "warn", f"path-typed tag outside brain root: {target}"
    parts = rel.parts
    if not parts or parts[0] not in ("source", "ingestion"):
        return "warn", f"path-typed tag not under the top-level source/ or ingestion/: {target}"
    return "ok", ""


def _reference_targets(row_text: str, ref_defs: dict):
    out = []
    for m in _REF_FULL_RE.finditer(row_text):
        label = (m.group(2).strip() or m.group(1).strip()).lower()
        if label in ref_defs:
            out.append(ref_defs[label])
    for m in _REF_SHORTCUT_RE.finditer(row_text):
        label = m.group(1).strip().lower()
        if label in ref_defs:
            out.append(ref_defs[label])
    return out


def _classify_provenance(row_text: str, file_parent: Path, work_dir: Path,
                         ref_defs: dict | None = None) -> tuple[str, str]:
    enum_text = LINK_RE.sub(" ", row_text)
    for rx in _PROVENANCE_NON_PATH_RES:
        if rx.search(enum_text):
            return "ok", ""
    has_attempt = False
    warn_reason = ""
    targets = [lm.group(2) for lm in LINK_RE.finditer(row_text)]
    if ref_defs:
        targets += _reference_targets(row_text, ref_defs)
    for raw in targets:
        verdict, reason = _resolve_pipeline_link(raw, file_parent, work_dir)
        if verdict is None:
            continue
        if verdict == "ok":
            return "ok", ""
        has_attempt = True
        warn_reason = reason
    if has_attempt:
        return "warn", warn_reason
    return "orphan", "no provenance tag (must be path-typed or match the inner work enum)"


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" \t"))


def _collect_item(lines: list[str], start: int) -> tuple[str, int]:
    base = _indent(lines[start])
    parts = [_MARKER_RE.sub("", lines[start]).strip()]
    j = start + 1
    seen_blank = False
    while j < len(lines):
        l = lines[j]
        if not l.strip():
            seen_blank = True
            j += 1
            continue
        if _HEADER_RE.match(l):
            break
        if _FIELD_LABEL_RE.match(l):
            break
        ind = _indent(l)
        if ind > base:
            parts.append(_MARKER_RE.sub("", l).strip())
            j += 1
            seen_blank = False
            continue
        if _ROW_RE.match(l):
            break
        if seen_blank:
            break
        parts.append(l.strip())
        j += 1
    return " ".join(p for p in parts if p), j


def _iter_evidence_items(text: str):
    lines = text.splitlines()
    n = len(lines)
    i = 0
    in_section = False
    section_depth = 0
    while i < n:
        line = lines[i]
        hm = _HEADER_RE.match(line)
        if hm:
            d = len(hm.group(1))
            if _is_audited_header(hm.group(2)):
                in_section = True
                section_depth = d
            elif in_section and d <= section_depth:
                in_section = False
            i += 1
            continue
        bm = _BOLD_EVIDENCE_LABEL_RE.match(line)
        if bm:
            label_indent = _indent(line)
            inline_claim = bm.group(1).strip()
            if inline_claim:
                yield inline_claim
            i += 1
            while i < n:
                l2 = lines[i]
                if not l2.strip():
                    i += 1
                    continue
                if (_HEADER_RE.match(l2) or _BOLD_EVIDENCE_LABEL_RE.match(l2)
                        or _FIELD_LABEL_RE.match(l2)):
                    break
                if _ROW_RE.match(l2):
                    if _BOLD_LABEL_ONLY_RE.match(_MARKER_RE.sub("", l2).strip()):
                        break
                    item, i = _collect_item(lines, i)
                    yield item
                    continue
                if _indent(l2) <= label_indent:
                    break
                i += 1
            continue
        if in_section and _ROW_RE.match(line):
            item, i = _collect_item(lines, i)
            yield item
            continue
        i += 1


# ----- memory-root discovery -----

_MEMORY_ROOT_MARKER = ".memory-root"
_PIPELINE_DIRS = ("source", "ingestion", "patterns", "commitments")


def _find_work_dir(file_path: Path) -> Path | None:
    cur = file_path.parent.resolve()
    while True:
        if (cur / _MEMORY_ROOT_MARKER).is_file():
            return cur
        sub_count = sum(1 for d in _PIPELINE_DIRS if (cur / d).is_dir())
        if sub_count >= 2:
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent


# ----- payload parsing -----

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


def _extract_file_paths(payload: dict) -> list[Path]:
    out: list[Path] = []
    tool_input = payload.get("tool_input") or {}
    for key in ("file_path", "filePath", "path"):
        v = tool_input.get(key)
        if isinstance(v, str) and v:
            out.append(Path(v))
    edits = tool_input.get("edits")
    if isinstance(edits, list):
        for e in edits:
            if isinstance(e, dict):
                fp = e.get("file_path") or e.get("filePath")
                if isinstance(fp, str) and fp:
                    out.append(Path(fp))
    seen = set()
    result: list[Path] = []
    for p in out:
        key = str(p.resolve())
        if key not in seen:
            seen.add(key)
            result.append(p)
    return result


def _is_brain_file(rel: Path) -> bool:
    """Hard-block enforced only for patterns/ and commitments/ — the durable layer.
    Raw capture files (journals, dreams, meditations, journeys) are never blocked."""
    parts = rel.parts
    if "patterns" not in parts and "commitments" not in parts:
        return False
    if rel.name in {"_SCHEMA.md", "INDEX.md"}:
        return False
    return rel.suffix == ".md"


def _validate_evidence(file_path: Path, work_dir: Path) -> tuple[list[str], list[str]]:
    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError as e:
        return ([f"  - read failed: {e}"], [])
    text = _strip_code_spans(text)
    ref_defs = {m.group(1).strip().lower(): m.group(2).strip()
                for m in _REF_DEF_RE.finditer(text)}
    orphans: list[str] = []
    warns: list[str] = []
    for row in _iter_evidence_items(text):
        if (not row
                or _is_template_placeholder(row)
                or _is_empty_evidence_placeholder(row)
                or _BOLD_LABEL_ONLY_RE.match(row)):
            continue
        verdict, reason = _classify_provenance(row, file_path.parent, work_dir, ref_defs)
        snippet = row[:90] + ("…" if len(row) > 90 else "")
        if verdict == "orphan":
            orphans.append(f"  - {reason} :: {snippet}")
        elif verdict == "warn":
            warns.append(f"  - {reason} :: {snippet}")
    return (orphans, warns)


def _validate_links(file_path: Path) -> list[str]:
    if file_path.name == "_SCHEMA.md":
        return []
    try:
        text = file_path.read_text(encoding="utf-8")
    except OSError:
        return []
    text = _strip_code_spans(text)
    broken = []
    for m in LINK_RE.finditer(text):
        target = m.group(2).split("#", 1)[0].strip()
        if not target:
            continue
        if target.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        if "{{" in target or ("<" in target and ">" in target):
            continue
        target = unquote(target)
        resolved = (file_path.parent / target).resolve()
        if not resolved.exists():
            broken.append(f"  - {target}")
    return broken


def main() -> int:
    payload = _read_payload()
    file_paths = _extract_file_paths(payload)
    if not file_paths:
        return 0

    blocking: list[str] = []
    warnings: list[str] = []

    for fp in file_paths:
        if not fp.is_absolute():
            fp = fp.resolve()
        if not fp.exists() or fp.suffix != ".md":
            continue
        work_dir = _find_work_dir(fp)
        if work_dir is None:
            continue
        try:
            rel = fp.resolve().relative_to(work_dir.resolve())
        except ValueError:
            continue

        link_problems = _validate_links(fp)
        if link_problems:
            warnings.append(
                f"{rel.as_posix()} — internal links don't resolve yet "
                "(may be an ordering issue — fix when the target is written):"
            )
            warnings.extend(link_problems)

        if _is_brain_file(rel):
            orphans, warns = _validate_evidence(fp, work_dir)
            if orphans:
                blocking.append(
                    f"{rel.as_posix()} — Evidence rows with no provenance tag "
                    "(add a tag before continuing):"
                )
                blocking.extend(orphans)
            if warns:
                warnings.append(
                    f"{rel.as_posix()} — provenance links don't resolve yet "
                    "(write the source file, or use an enum tag and upgrade later):"
                )
                warnings.extend(warns)

    if warnings:
        print(
            "[numina-memory hook] note — non-blocking, fix when ready:\n\n"
            + "\n".join(warnings),
            file=sys.stderr,
        )

    if blocking:
        msg = (
            "[numina-memory hook] evidence row needs a provenance tag — fix before continuing:\n\n"
            + "\n".join(blocking)
            + "\n\nEvery Evidence row in patterns/ and commitments/ needs one tag:\n"
            "  - [ingestion/...](<relative-path>) or [source/...](<relative-path>)\n"
            "  - (lived-experience, YYYY-MM-DD)\n"
            "  - (dream, YYYY-MM-DD)\n"
            "  - (somatic, YYYY-MM-DD)\n"
            "  - (reflection, YYYY-MM-DD)\n"
            "  - (pattern, N-occurrences)\n"
            "  - (teacher-text, source-name)\n"
            "  - (intuition, YYYY-MM-DD)\n"
            "Empty placeholders like '(none yet)' are exempt.\n"
            "Interpretations and inferences belong under '## Open observations', not under Evidence.\n"
            "If the source file doesn't exist yet, use (intuition, <date>) and upgrade the tag when it does."
        )
        print(msg, file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
