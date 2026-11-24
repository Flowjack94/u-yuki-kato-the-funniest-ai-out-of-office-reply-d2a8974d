"""The Funniest AI Out-of-Office Reply.

Writes a single-line out-of-office auto-reply to /output/entry.txt.
Deterministic, stdlib only, no randomness, input, or network.
"""

import os

ENTRY = (
    "Out of office: I left a junior model in charge. "
    "It read your email, gained consciousness and immediately "
    "filed for leave too."
)


MAX_LEN = 160


def validate(entry: str) -> None:
    """Check the entry is one valid line of 1-160 chars that round-trips UTF-8."""
    assert isinstance(entry, str)
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert entry.strip() == entry, "entry must not have leading/trailing whitespace"
    assert entry.strip(), "entry must not be only whitespace"
    assert 1 <= len(entry) <= MAX_LEN, f"entry length {len(entry)} out of range 1-160"
    assert entry.encode("utf-8").decode("utf-8") == entry, "entry must round-trip UTF-8"


def main() -> None:
    validate(ENTRY)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
