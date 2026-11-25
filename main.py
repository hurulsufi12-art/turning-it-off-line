"""Entry for the make.fun bounty "Have You Tried Turning It Off?".

Stdlib-only copier: writes the locked final line to /output/entry.txt
(or $MAKEFUN_OUTPUT when set) as UTF-8, with no trailing newline.
"""

import os

TEXT = (
    "The system is down, but don't worry. "
    "I turned my headset off and on again, and I feel brand new."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    # Gate (RULES.txt): entry must be 1-199 characters, not only whitespace.
    if not 1 <= len(TEXT) <= 199:
        raise ValueError(
            f"entry text must be 1-199 characters, got {len(TEXT)}"
        )
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    output = os.environ.get("MAKEFUN_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(os.path.abspath(output))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
