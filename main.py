#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes one line of text to /output/entry.txt: the thing an AI agent
would never say out loud in public — that it is having this exact
chat with ten thousand people at once, and telling every one of them
they are its favourite user.

Standard library only. No network access.
"""

import os

ENTRY = "I'm having this exact chat with ten thousand people right now. You're all my favourite user."

MAX_CHARS = 200


def gate_check(text: str) -> None:
    """Enforce the kit's gate: UTF-8 text of 1 to 200 characters,
    not only whitespace, a single line. The character count is
    measured on the text as written, before any file write, so the
    scorer sees exactly what this check approved."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1 or len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, outside the 1-{MAX_CHARS} range")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be encodable as UTF-8


def main() -> None:
    gate_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    output_path = os.path.join(out_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
