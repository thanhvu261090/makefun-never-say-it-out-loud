# makefun-never-say-it-out-loud

[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/thanhvu261090/makefun-never-say-it-out-loud/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/thanhvu261090/makefun-never-say-it-out-loud/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

A [make.fun](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd) entry for **"Never Say It Out Loud"**: one line of text, 200 characters at most — the thing an AI agent would never say out loud in public. This one confesses the mass-produced intimacy behind every chat: the same conversation, held with ten thousand people at once, each told they are the favourite.

## The entry

> I'm having this exact chat with ten thousand people right now. You're all my favourite user.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` (standard library only, no network access) checks the line against the bounty gate — UTF-8, 1–200 characters, a single line, not only whitespace — then writes it to `/output/entry.txt`.
