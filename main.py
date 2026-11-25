#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — writes one cat joke to entry.txt.

Stdlib only. Reads the output dir from MAKEFUN_OUTPUT_DIR with a
fallback of /output. Creates the output dir if needed; never deletes it.
"""

import os

# The joke: setup (ignored all day) + turn (3am face-walk as a landlord
# inspection). A fresh angle, no pun, retellable in one breath.
ENTRY = (
    "My cat ignores me all day, then at 3am walks across my face "
    "like a landlord doing an inspection."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    # Verified: 96 characters, inside the 1-200 gate, not only whitespace.
    if not text or not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
