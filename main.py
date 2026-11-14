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

POEM = """The First Line

Nine years I owed my brother a letter.

I asked the machine for a first line.
It gave me four, then twelve,
then a page, kind and exact,
better than anything I had,
and none of them was the sentence
I would have to say.

I deleted them and typed his name.
The rest came out clumsy, mine,
nine years late.
He read it at the counter
with his coat still on.

That is the part no one can do for you:
the beginning.
Everything after it can be carried."""


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
