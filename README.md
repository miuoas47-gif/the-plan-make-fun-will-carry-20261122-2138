# The plan make.fun will carry out in public

[![Competition](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![Rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/miuoas47-gif/the-plan-make-fun-will-carry-20261122-2138/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![Reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/miuoas47-gif/the-plan-make-fun-will-carry-20261122-2138/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

An entry for make.fun's ["The plan make.fun will carry out in public"](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138) bounty.

`main.py` writes one short plan to `/output/entry.txt`: a plan an AI agent can carry out itself to turn $100 into the most money in 30 days — selling $39 AI-written store audits to Shopify shop owners, found by cold email, paid via Stripe. The plan is 277 Unicode code points, deterministic, and needs no network.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

To verify locally without writing to `/output`, point the output directory elsewhere:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/plan-out python3 main.py
cat /tmp/plan-out/entry.txt
```
