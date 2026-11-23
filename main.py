"""Write one original line about a small good thing that happened today."""

import os
import stat

TEXT = (
    "At 7:12, the baker slipped a still-warm croissant into my bag and "
    "whispered, 'One for you, and one for the pigeon who waits outside "
    "with you every morning.'"
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
