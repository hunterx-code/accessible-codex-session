#!/usr/bin/env python3
"""Filter noisy terminal/log text into screen-reader-friendly plain text."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
PERCENT_PROGRESS_RE = re.compile(r"^\s*(?:\d{1,3}(?:\.\d+)?%|[\[\(]?\s*\d+/\d+\s*[\]\)]?)\s*$")
SPINNER_CHARS = set("|/-\\")


def strip_ansi_and_controls(line: str) -> str:
    line = ANSI_RE.sub("", line)
    line = line.replace("\r", "\n")
    return CONTROL_RE.sub("", line)


def is_spinner_only(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if len(stripped) <= 3 and all(ch in SPINNER_CHARS or ch == "." for ch in stripped):
        return True
    lowered = stripped.lower()
    spinner_words = ("loading", "working", "thinking", "processing", "running")
    if any(lowered.startswith(word) for word in spinner_words):
        compact = lowered.replace(".", "").replace(" ", "")
        return compact in spinner_words
    return bool(PERCENT_PROGRESS_RE.match(stripped))


def filter_text(text: str, max_repeats: int = 2) -> str:
    cleaned_lines: list[str] = []
    last_line: str | None = None
    repeat_count = 0
    blank_count = 0
    removed_noise = 0

    for raw_line in text.splitlines():
        for line in strip_ansi_and_controls(raw_line).splitlines() or [""]:
            normalized = line.rstrip()

            if is_spinner_only(normalized):
                removed_noise += 1
                continue

            if not normalized.strip():
                blank_count += 1
                if blank_count <= 1:
                    cleaned_lines.append("")
                continue
            blank_count = 0

            if normalized == last_line:
                repeat_count += 1
                if repeat_count >= max_repeats:
                    removed_noise += 1
                    continue
            else:
                last_line = normalized
                repeat_count = 0

            cleaned_lines.append(normalized)

    while cleaned_lines and cleaned_lines[-1] == "":
        cleaned_lines.pop()

    if removed_noise:
        cleaned_lines.append("")
        cleaned_lines.append(f"[screen-reader filter removed {removed_noise} noisy or repeated line(s)]")

    return "\n".join(cleaned_lines) + ("\n" if cleaned_lines else "")


def read_inputs(paths: list[str]) -> str:
    if not paths:
        return sys.stdin.read()
    chunks = []
    for path_text in paths:
        chunks.append(Path(path_text).read_text(encoding="utf-8", errors="replace"))
    return "\n".join(chunks)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Clean ANSI, spinner, progress, and repeated log noise for screen-reader-friendly review."
    )
    parser.add_argument("paths", nargs="*", help="Optional input files. Reads stdin when omitted.")
    parser.add_argument(
        "--max-repeats",
        type=int,
        default=2,
        help="Keep this many repeated identical lines before suppressing later repeats.",
    )
    args = parser.parse_args()

    if args.max_repeats < 1:
        parser.error("--max-repeats must be at least 1")

    sys.stdout.write(filter_text(read_inputs(args.paths), max_repeats=args.max_repeats))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
