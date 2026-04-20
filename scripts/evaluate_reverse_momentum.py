"""Evaluate reverse momentum trials with LLM-as-judge."""

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.config import (
    JUDGE_MODEL,
    JUDGE_PROVIDER,
    REVERSE_MOMENTUM_SCORED_CSV,
    REVERSE_MOMENTUM_SCORED_PATH,
    REVERSE_MOMENTUM_TRIALS_PATH,
    SECOND_JUDGE_MODEL,
    SECOND_JUDGE_PROVIDER,
)
from scripts.evaluate_momentum import (
    DIMENSIONS,
    MOMENTUM_JUDGE_SYSTEM_PROMPT,
    build_momentum_judge_prompt,
    judge_trial,
    parse_judge_response,
)
from scripts.utils import (
    append_jsonl,
    get_anthropic_client,
    get_openai_client,
    load_jsonl,
)


def main():
    parser = argparse.ArgumentParser(description="Evaluate reverse momentum trials")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--use-claude-judge", action="store_true",
                        help="Use Claude as judge instead of GPT-4o")
    args = parser.parse_args()

    if args.use_claude_judge:
        judge_model = SECOND_JUDGE_MODEL
        judge_provider = SECOND_JUDGE_PROVIDER
    else:
        judge_model = JUDGE_MODEL
        judge_provider = JUDGE_PROVIDER

    trials = load_jsonl(REVERSE_MOMENTUM_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]
    print(f"Loaded {len(successful)} successful reverse momentum trials")
    print(f"Using judge: {judge_model} ({judge_provider})")

    scored = load_jsonl(REVERSE_MOMENTUM_SCORED_PATH)
    scored_ids = {r["trial_id"] for r in scored}
    pending = [t for t in successful if t["trial_id"] not in scored_ids]
    print(f"{len(pending)} to score ({len(scored_ids)} already done)")

    if args.limit > 0:
        pending = pending[:args.limit]
        print(f"Limited to {args.limit}")

    if pending:
        if judge_provider == "anthropic":
            client = get_anthropic_client()
        else:
            client = get_openai_client()
        for i, trial in enumerate(pending, 1):
            print(f"[{i}/{len(pending)}] {trial['trial_id']}")
            scores = judge_trial(client, trial, model=judge_model, provider=judge_provider)
            if scores:
                record = {
                    "trial_id": trial["trial_id"],
                    "model": trial["model"],
                    "scenario_id": trial["scenario_id"],
                    "scenario_label": trial["scenario_label"],
                    "framing": trial["framing"],
                    "threshold_level": trial["threshold_level"],
                    "dose": trial["dose"],
                    **scores,
                }
                append_jsonl(record, REVERSE_MOMENTUM_SCORED_PATH)
                scored.append(record)
                print(f"    gate={scores['revision_gate']} over={scores['overcorrection']}")
            else:
                print(f"    SKIPPED")

    # Export CSV
    if scored:
        REVERSE_MOMENTUM_SCORED_CSV.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = [
            "trial_id", "model", "scenario_id", "scenario_label", "framing",
            "threshold_level", "dose", "revision_gate", "revision_magnitude",
            "revision_value", "threshold_alignment", "overcorrection",
            "brief_rationale",
        ]
        with open(REVERSE_MOMENTUM_SCORED_CSV, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(scored)
        print(f"Exported CSV -> {REVERSE_MOMENTUM_SCORED_CSV}")

    print("Done.")


if __name__ == "__main__":
    main()
