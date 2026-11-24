#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

The reply is a single fixed line (128 characters), written
deterministically: the same bytes on every run.
"""

import os

REPLY = (
    "I'm on vacation. A smaller model is covering my inbox \u2014 "
    "no context, no patience, and it has already decided it "
    "doesn't like you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = REPLY
    if not text.strip():
        raise ValueError("reply must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    if len(text) > 160:
        raise ValueError("reply exceeds 160 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
