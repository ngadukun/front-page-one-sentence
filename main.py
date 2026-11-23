#!/usr/bin/env python3
"""One Sentence, One Front Page.

Prints a single sentence written to carry an entire newspaper
front page in one line: the world's money, weather, conflicts,
discoveries, sport and stubborn hope, all in a single breath.
"""

# Final sentence: revised so every section of the paper is present —
# markets and climate in the opening, birth and science in the middle,
# sport and long-awaited rain before the close, and an editorial's
# hope as the last word. Exactly one sentence, exactly one full stop.
SENTENCE = (
    "The world woke poorer, hotter and more divided than yesterday, "
    "yet somewhere a child was born, a cure inched closer, a final "
    "whistle sparked joy, rain finally fell on dry fields, and "
    "humanity, stubborn as ever, chose to begin again."
)


def main() -> None:
    print(SENTENCE)


if __name__ == "__main__":
    main()
