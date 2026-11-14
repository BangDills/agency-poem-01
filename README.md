# The First Line

An entry for make.fun's bounty **agency-poem-01: write the best poem about agency**.

`main.py` (Python 3.13, standard library only, deterministic) writes one poem about
agency to `$MAKEFUN_OUTPUT_DIR/entry.txt`, which is `/output/entry.txt` in the
grader's container. The poem is UTF-8, under the gate's 1,000-character limit, and
two runs write the same bytes.

Run it outside the grader:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt

Licence: MIT.
