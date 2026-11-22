"""Write the plan text to /output/entry.txt.

No network, no arguments, deterministic: the same bytes on every run.
The output directory defaults to /output (the grader's path) and can be
overridden with MAKEFUN_OUTPUT_DIR for local verification only.
"""

import os

PLAN = (
    "Day 1: buy a domain ($12) + Hunter ($49). Email 1,000 Shopify stores "
    "with slow pages, no reviews, offering a free 1-page teaser; sell "
    "audits for $39 via Stripe, same-day PDF. 1% buy = $390. Edge: code "
    "writes each audit in minutes, so a $39 sale costs ~$0; agencies "
    "charge $500."
)


def main() -> int:
    if not PLAN.strip() or not 1 <= len(PLAN) <= 280:
        raise SystemExit(
            f"plan must be 1-280 code points and non-blank, got {len(PLAN)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
