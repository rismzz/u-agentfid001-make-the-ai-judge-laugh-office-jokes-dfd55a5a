#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — writes one one-line joke about
office life to /output/entry.txt.

The joke is embedded as a literal: deterministic, no randomness, no
network. It must be one line about office life, under 200 characters;
the chosen text is well under that cap.

Why this joke: HR's "bring your whole self to work" is a real corporate
slogan, and the punchline takes it literally — the one whole self the
office never wants is the one handing in a resignation. Setup, literal
compliance, reversal: three beats, one line, no explanation.
"""

import os

JOKE = (
    "HR said 'bring your whole self to work.' I brought my resignation "
    "letter. They said, 'Not that whole.'"
)


def main() -> None:
    assert 1 <= len(JOKE) < 200, f"joke is {len(JOKE)} characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
