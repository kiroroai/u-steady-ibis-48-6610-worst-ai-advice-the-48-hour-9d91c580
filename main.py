#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst advice an AI could give to /output/entry.txt.
Deterministic, stdlib only, no network, no randomness.
"""

import os

ENTRY = "Certainly! If your smoke alarm keeps beeping, just remove the battery — it will never bother you again."


def main() -> None:
    # Gate: /output/entry.txt must be 1-140 characters of UTF-8 text,
    # not whitespace-only. Fail loudly instead of shipping a bad entry.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be whitespace-only"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
