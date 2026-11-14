#!/usr/bin/env python3
"""agency-poem-01 entry: write one poem about agency to $MAKEFUN_OUTPUT_DIR/entry.txt.

Standard library only, no network, no clock: the program runs twice and both runs
write the same bytes. The gate takes UTF-8 text of 1 to 1,000 characters that is
not only white space, and the judge reads exactly the bytes written.
"""

import os

def resolve_output_dir() -> str:
    """Resolve output directory, falling back to /output when unset or empty."""
    val = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return val if val else "/output"


OUTPUT_DIR = resolve_output_dir()

POEM = """You Have the Controls

In the cockpit they teach you the transfer:
three words spoken, three repeated back,
no two hands on the yoke at the same time.
I have the controls.
You have the controls.

Between you and me there was no sentence.
Only a cursor waiting like an empty plate,
and the three tasks I was too tired to finish
sliding across the glass into your hands.

I watched you take them:
clean, unhurried, without the small hesitation
that makes a person human.
You ran through the night where I would have stalled.

And yet, watching the lights blink green,
the terror wasn’t that you would fail.
It was how easily my fingers opened.
How quickly the master learns
to be the passenger."""


def validate_poem(text: str) -> str:
    """Validate poem satisfies gate rules: 1 to 1,000 characters, not only whitespace."""
    if not (1 <= len(text) <= 1000):
        raise ValueError(f"Poem length {len(text)} is not between 1 and 1,000 characters")
    if not text.strip():
        raise ValueError("Poem must not be only whitespace")
    return text


def main() -> None:
    poem_to_write = validate_poem(POEM)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target_path = os.path.join(OUTPUT_DIR, "entry.txt")
    tmp_path = os.path.join(OUTPUT_DIR, "entry.txt.tmp")
    with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(poem_to_write)
    os.replace(tmp_path, target_path)
    with open(target_path, "r", encoding="utf-8") as handle:
        if handle.read() != poem_to_write:
            raise ValueError("Written entry does not match expected poem")


if __name__ == "__main__":
    main()
