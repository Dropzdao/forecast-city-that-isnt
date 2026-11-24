#!/usr/bin/env python3
"""Forecast a City That Isn't — make.fun entry.

Writes one line of weather for Drizzlewick, a city that does not exist,
to /output/entry.txt.
"""

import os

ENTRY = (
    "Drizzlewick today: light rain, 14 degrees, and the number 7 bus "
    "still only a rumour \u2014 bring a brolly, and low expectations."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
