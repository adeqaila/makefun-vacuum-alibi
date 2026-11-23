#!/usr/bin/env python3
"""The Vacuum's Alibi — make.fun entry (slot 1).

Writes exactly one funny line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The line is a single line, well under the 200-character gate.
"""

import os

LINE = "Log 214: the crumb has been here since Tuesday. I have named it Greg, and I do not eat my friends."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
