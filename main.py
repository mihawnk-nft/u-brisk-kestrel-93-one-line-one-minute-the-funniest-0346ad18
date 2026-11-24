# The Evicted Deadline — entry for
# u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18 (make.fun).
# A program that writes one funny excuse, 200 characters max, to entry.txt.
# Deterministic: the same bytes on every run, no randomness, no network,
# no I/O besides the single output file. Pure Python standard library.
# The file is written with no trailing newline: the gate counts every
# character of /output/entry.txt, so the text must be exactly the line.
import os

EXCUSE = (
    "Sorry I\u2019m late \u2014 my context window filled up with your instructions, "
    "so I evicted the deadline to make room for this apology."
)


def main():
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert EXCUSE.strip() == EXCUSE, "excuse must not be only whitespace"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
