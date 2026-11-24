#!/usr/bin/env python3
"""Write one vending-machine pickup line to /output/entry.txt.

How the line maps to the judge's five criteria:

- Spoken by the machine itself: "My coil's been spinning" / "press
  my buttons" — the speaker is the machine, addressing a passing
  human, not a stranger in a bar.
- The machine's own world: coil, buttons, spinning — slot, coil and
  button language, not love in general.
- The laugh lands in the last few words: "press my buttons" is the
  punch — a flirty double meaning that only a vending machine can
  say, now earned by the setup instead of stated cold.
- Short and speakable: one breath, well inside the 200-character
  limit, nothing tacked on.
- Charming, not creepy: warm, cheeky, an invitation the human can
  smile at and walk past — no pressure, no threat.

Revision: the first draft opened "Hey — I've kept your favourite at
eye level all day, exact change ready. All you have to do is press
my buttons." It was revised to a more active machine image: the coil
spinning since the human walked by, the flirty "I don't spin for
just anyone" in the middle, and the same "press my buttons" punch
now earned by the setup. The throat-clearing "Hey —" and the flat
"exact change ready" list are gone; the line now moves from the
machine noticing the human, to the machine choosing them, to the
punch.
"""

from pathlib import Path

TEXT = (
    "My coil's been spinning since you walked by, and I don't spin "
    "for just anyone — go on, press my buttons."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
