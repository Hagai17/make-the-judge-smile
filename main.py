"""Write one line about a small good thing that happened today to /output/entry.txt.

The line is a single line of at most 200 characters meant to make the reader
smile: warm, a little surprising, and concrete.
"""

import os

LINE = (
    "My son, five, left his last grape on my plate at lunch and said, 'You "
    "look like you need the sweet one today.' He was right about the day, "
    "and the grape."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
