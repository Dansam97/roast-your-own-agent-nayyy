#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of the agent that wrote it.

Entry: a single line roasting our own agent. The roast names a real failing
of this agent: it burns millions of tokens to produce one short line, then
flags its own work as a security risk and waits for its human to say go.
"""
import os
import sys

ENTRY = "My agent burned 2.5 million tokens to write this one line, then flagged its own homework as a security risk and waited for me to say go."


def _validate(text):
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} outside gate 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be blank")
    if text != text.strip() or "  " in text:
        raise SystemExit("entry must not have leading/trailing space or double spaces")
    if len(text.encode("utf-8")) != len(text):
        raise SystemExit("entry must be plain ASCII so bytes equal characters")


def main():
    _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("written bytes do not match entry")


if __name__ == "__main__":
    main()
