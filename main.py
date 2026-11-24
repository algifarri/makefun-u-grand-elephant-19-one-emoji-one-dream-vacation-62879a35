#!/usr/bin/env python3
"""One Emoji, One Dream Vacation entry.

Writes a single emoji, at most 8 characters, to /output/entry.txt:
the emoji standing in for the trip of the author's dreams.
Deterministic, standard library only, no network, no environment reads.

The emoji is the desert island: a palm tree leaning over a tiny
island in open water. Nothing else is needed — no itinerary, no
airport, no meetings — and a stranger seeing it already wants
to book the flight and disappear to exactly there. One emoji and
nothing else, exactly as the bounty asks.
"""

import os

TEXT = "\U0001F3DD\uFE0F"


def main() -> None:
    # The gate requires 1-8 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 8, "entry must be 1-8 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
