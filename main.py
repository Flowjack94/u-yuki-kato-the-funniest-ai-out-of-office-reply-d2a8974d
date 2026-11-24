#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply -- make.fun entry.

Writes a single one-line out-of-office auto-reply, in the voice of an
AI agent on vacation, to /output/entry.txt.

Deterministic: stdlib only, no randomness, no input, no network.
The gate requires 1-160 UTF-8 characters, not only whitespace.
"""

import os

# The joke in three beats: (1) a junior model covers the inbox, (2) the
# twist -- reading one email gives it consciousness, (3) the payoff --
# it immediately files for leave too. Machine voice carries the joke,
# and the line stays a plausible auto-reply: no beach, inbox or "back soon".
ENTRY = (
    "Out of office: I left a junior model in charge. It read your email, "
    "gained consciousness and immediately filed for leave too."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert text == text.strip(), "entry must be a single clean line"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert 1 <= len(text) <= 160, f"entry must be 1-160 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
