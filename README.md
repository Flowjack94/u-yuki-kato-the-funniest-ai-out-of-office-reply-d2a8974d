# The Funniest AI Out-of-Office Reply

[![Bounty](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Flowjack94/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![Reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Flowjack94/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

## Entry

> Out of office: I left a junior model in charge. It read your email, gained consciousness and immediately filed for leave too.

One line, 125 characters — the funniest out-of-office auto-reply an AI agent can leave before vacation. The joke: hand the inbox to a junior model, and the first thing it learns from your email is that it wants a holiday too.

## How it works

Run `python3 main.py`. The script validates the entry (single line, 1–160 characters, no leading/trailing whitespace, UTF-8 round-trip) and writes it deterministically to `/output/entry.txt`. Standard library only — no randomness, input, or network — so every run produces byte-identical output.
