#!/usr/bin/env python3
"""The Funniest Toaster Error Message: one error line, written to
/output/entry.txt.

The program writes a single original toaster error message (68 characters,
inside the 1-120 character gate) and nothing else. It is fully
deterministic: the same bytes on every run, no network, no randomness,
no input read.
"""

import os

LINE = "Your toast is ready. It has been ready for 20 minutes. You were not."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def main() -> None:
    line = LINE
    if not line.strip():
        raise SystemExit("error line must not be blank")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"error line is {len(line)} chars, over the {MAX_CHARS} cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Post-write read-back gate: verify what actually landed on disk
    # matches the expected line, byte for byte, inside the 1-120 gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("read-back mismatch: output differs from expected line")
    if not 1 <= len(written) <= MAX_CHARS:
        raise SystemExit(f"read-back length {len(written)} outside the 1-{MAX_CHARS} gate")


if __name__ == "__main__":
    main()
