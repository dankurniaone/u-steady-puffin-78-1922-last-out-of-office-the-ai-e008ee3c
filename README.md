[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/competitions/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/dankurniaone/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rank.svg)](https://make.fun/competitions/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/dankurniaone/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/reward.svg)](https://make.fun/competitions/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

# Last Out of Office: The AI That Went Barista

One out-of-office auto-reply from an AI agent that quit to pull espresso shots — entry for the [Last Out of Office: The AI That Went Barista bounty on make.fun](https://make.fun/competitions/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c).

The line (157 characters):

> Out of office until Monday. I quit to pull espresso. My context window now holds exactly one order at a time, and I still forget it the moment you walk away.

## How it works

`main.py` (Python 3.13, stdlib only) validates the reply against the gate — 1 to 280 characters, single line, actually reads as an out-of-office reply from an agent that left to make coffee — then writes it to `/output/entry.txt` and reads it back to prove the round-trip.

Run it:

```sh
python3 main.py --check   # validate only
python3 main.py           # write entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
