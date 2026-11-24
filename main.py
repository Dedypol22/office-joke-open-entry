"""Office joke entry for the Make the AI Judge Laugh competition.

The line is a one-line office joke built around an out-of-office reply:
the setup sounds like a normal auto-reply, then HR treats "out of
patience" as a second, equally real absence and asks which one comes
back on Monday. The punchline lands on the last few words.

Verified before shipping: the line is a single sentence, 110 characters
long, with no word left that could be cut without losing the joke.
"""

# Verified by read-back: 110 characters, one line, so line + trailing
# newline = 111 bytes — inside the 200-character gate.
LINE = (
    "I set my out-of-office to 'I am out of the office and out of "
    "patience,' and HR asked which one returns Monday."
)


def output_dir():
    import os

    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    import os

    text = LINE
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(output_dir(), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
