#!/usr/bin/env python3
"""Write one line about a small good thing today to /output/entry.txt.

Deterministic: the same bytes on every run. No clock, no randomness, no
network, no input read from anywhere. The output file is mode 0644 with
no trailing newline.
"""

import os

ENTRY = "The barista remembered my order this morning, misspelled my name the same wrong way as yesterday, and we both laughed like it was an old joke."


def main() -> None:
    # The gate: 1 to 200 characters, not only whitespace, or the entry
    # is invalid and takes no prize. Fail loudly instead of writing it.
    text = ENTRY.strip()
    if not 1 <= len(ENTRY) <= 200 or not text:
        raise SystemExit("entry must be 1 to 200 non-blank characters")
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
