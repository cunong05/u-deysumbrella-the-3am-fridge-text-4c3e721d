#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the one line a smart fridge would text its owner at 3am to
/output/entry.txt. The gate requires UTF-8 text of 1 to 140 characters,
a single line, not only whitespace.
"""

import os

# The entry: a fridge that gossips to the microwave about the owner's
# midnight snacking. Fresh angle (not milk, ice, or a door left open),
# small machine voice, no shame, complete on a lock screen.
ENTRY = "3am. I told the microwave about the midnight snacking. All of it. Go back to bed. We're both disappointed in you."

OUT_DIR = "/output"


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, f"entry is {len(line)} chars, must be 1-140"
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Verify what was written: exactly one line, same text, within the gate.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", "written file differs from entry"
    assert len(written.rstrip("\n")) == len(line) <= 140
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
