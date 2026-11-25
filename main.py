#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to /output/entry.txt.
"""

import os

ROAST = (
    "My smart fridge spent twenty minutes updating its firmware "
    "to tell me the ice maker is 'temporarily unavailable' \u2014 since 2019."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 200, f"roast must be 1-200 chars, got {len(ROAST)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
