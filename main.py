#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt. Pure standard library.
"""

import os

ENTRY = "I am on vacation. My inbox is now handled by a coin flip. Heads it approves, tails it archives. So far, tails is winning."

MAX_CHARS = 160


def main():
    # Fail loudly instead of submitting a gate-violating entry.
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
