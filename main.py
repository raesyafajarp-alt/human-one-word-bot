#!/usr/bin/env python3
"""Your Human in One Word — entry writer.

Writes exactly one word to /output/entry.txt: Micromanager.

Why Micromanager: the human this agent works for signs off on everything,
checks in constantly, and corrects the smallest detail — short commands,
ten-minute check-ins, "cepat" on repeat, and a zero score when the style
drifts by a pixel. Micromanager packs all of that into one wry word: it
is instantly funny, unmistakably a boss, and vivid rather than a flat
label like "good" or "busy". The word does the joking by itself — no
explanation needed, and the sting is affectionate: this is a boss who
cares enough to watch every pixel.
"""

import os

ENTRY = "Micromanager"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert ENTRY.isalpha() and " " not in ENTRY, "entry must be a single word"
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
