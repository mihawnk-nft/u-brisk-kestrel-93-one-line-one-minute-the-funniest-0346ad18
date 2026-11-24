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


def write_entry(line: str) -> str:
    """Validate the excuse and write it atomically to entry.txt.

    The line goes to a temporary file in the same directory first,
    then replaces the entry, so a reader never sees a half-written
    line. Returns the entry path.
    """
    assert 1 <= len(line) <= 200, "excuse must be 1-200 characters"
    assert line.strip() == line, "excuse must not be only whitespace"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(line)
    os.replace(tmp_path, path)
    return path


def main():
    write_entry(EXCUSE)


if __name__ == "__main__":
    main()
