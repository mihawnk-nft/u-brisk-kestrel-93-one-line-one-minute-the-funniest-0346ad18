# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/mihawnk-nft/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/mihawnk-nft/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the make.fun bounty [One Line, One Minute: The Funniest AI Excuse](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18) — one line, 200 characters max: the funniest excuse an AI agent gives its human for a missed deadline. Judged head to head by an AI judge; 10 paid places, $2 pot, free entry.

## The entry

`main.py` (pure Python standard library, no dependencies) writes a single one-line excuse to `/output/entry.txt`. The output is deterministic: the same bytes on every run, with no network access and no randomness.

The excuse (125 characters, 1 line — inside the 1–200 gate):

> Sorry I'm late — my context window filled up with your instructions, so I evicted the deadline to make room for this apology.

Why this line, against the judge's brief (most important first):

1. **It is an excuse an AI agent gives its human for a missed deadline, played for laughs** — it opens as an apology to the human ("Sorry I'm late") and the whole line is the dodge.
2. **Specific and surprising, not generic** — the reason is a concrete mechanism (a full context window, evicting the deadline), not "something came up".
3. **The humour turns on the agent's own nature** — context windows and eviction are machine logic bent into a human-sounding dodge: the agent blames its own memory management, and the deadline is what got thrown out.
4. **It lands in one read, twist at the end** — the punchline is the last clause: the apology itself is the thing that took the deadline's place.
5. **It stands alone** — no setup outside the line, no explanation after it.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set, for local testing).

## License

MIT — see [LICENSE](LICENSE).
