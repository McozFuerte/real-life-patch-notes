"""Real-Life Patch Notes: The Comedy Changelog — entry builder."""

import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")

ENTRY = (
    "v2.8.0: fixed bug where phantom phone vibrations"
    " fired with no incoming signal; root cause traced to loneliness"
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
