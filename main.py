#!/usr/bin/env python3
"""The Funniest Out-of-Office — entry program.

Writes the one-line out-of-office reply to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no randomness,
no network.

The joke: the out-of-office reply is guarded by an intern named Denial —
a personified stage of grief, hired as staff. He opens everything and
answers nothing, which is exactly what an inbox does while its owner is
away. A real reply a person would set, with a voice of its own and a
twist nobody sees coming: the guardian of the inbox is the reason
nothing ever gets answered.
"""

from pathlib import Path

ENTRY = (
    "I'm out of the office until Monday. My inbox is being guarded by "
    "an intern named Denial \u2014 he opens everything and answers nothing.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 140, "entry must be 1-140 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
