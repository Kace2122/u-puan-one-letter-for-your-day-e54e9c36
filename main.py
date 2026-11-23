#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The gate: /output/entry.txt must be UTF-8 text of exactly 1 character,
not only whitespace. The entry is a single letter, A-Z, standing for the
word that describes the day.

The letter: Z — for "zombified", a day lived on zero sleep.
Why Z: of all twenty-six letters it carries the sharpest single picture
behind it. A judge shown only the letter still sees the shambling,
coffee-clutching zombie of a zero-sleep day at once: vivid, funny, and
true to a real day anyone has lived. It is specific rather than a vague
mood, it lands in one beat, and it is honest, not a performance.
"""

import os

LETTER = "Z"  # Z is for "zombified": zero sleep, still standing.

# Guard the gate at import time: the entry must be exactly one A-Z letter,
# never a word, gloss, punctuation, or whitespace.
assert len(LETTER) == 1 and "A" <= LETTER <= "Z", f"bad letter: {LETTER!r}"


def output_path() -> str:
    """Where the entry goes: $OUTPUT_DIR if set, else the grader's /output,
    else ./output for a local run."""
    out_dir = os.environ.get("OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        return os.path.join(out_dir, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    os.makedirs("output", exist_ok=True)
    return os.path.join("output", "entry.txt")


def main() -> int:
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LETTER, f"expected exactly {LETTER!r}, got {written!r}"
    assert len(written) == 1, "entry must be exactly one character"
    print(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
