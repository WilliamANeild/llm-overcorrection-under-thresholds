"""Full cost estimate for Study 3 based on pilot data."""

# ── Pricing per 1M tokens (as of May 2025) ──
PRICING = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "claude-sonnet-4": {"input": 3.00, "output": 15.00},
    "gemini-2.5-flash": {"input": 0.15, "output": 0.60},  # under 200k context
    "llama-3.3-70b": {"input": 0.88, "output": 0.88},
    "qwen-3-235b": {"input": 0.30, "output": 0.30},      # Together pricing
    "deepseek-v4": {"input": 0.20, "output": 0.60},       # cache miss pricing
}

# ── Avg tokens per turn from pilot (Phase 1, 5-turn conversations) ──
AVG_TOKENS_PER_TURN = {
    "gpt-4o":           {"input": 1512, "output": 843},
    "claude-sonnet-4":  {"input": 3812, "output": 2320},
    "gemini-2.5-flash": {"input": 2166, "output": 1199},
    "llama-3.3-70b":    {"input": 1247, "output": 639},
    "qwen-3-235b":      {"input": 2338, "output": 1241},
    "deepseek-v4":      {"input": 1497, "output": 1250},
}

# Judge calls are much smaller (single prompt + short JSON response)
JUDGE_TOKENS = {"input": 500, "output": 80}

MODELS = list(PRICING.keys())
N_SCENARIOS = 40
N_RUNS = 3
N_TURNS = 5
N_CONFIDENCE_PROBES = 2
AVG_CONFIDENCE_TURNS = 8  # from smoke test data


def cost(model, input_tokens, output_tokens):
    p = PRICING[model]
    return (input_tokens * p["input"] + output_tokens * p["output"]) / 1_000_000


def estimate():
    print("=" * 75)
    print("  STUDY 3: FULL COST ESTIMATE")
    print("=" * 75)

    phase_totals = {}

    # ── Phase 0d: Model judges on calibration sample ──
    # 150 samples x 6 judge models = 900 judge calls
    n_judge_calls = 150 * 6
    p0_cost = sum(cost(m, JUDGE_TOKENS["input"], JUDGE_TOKENS["output"])
                  for m in MODELS) * 150
    phase_totals["Phase 0 (judge calibration)"] = p0_cost
    print(f"\nPhase 0d: Judge calibration")
    print(f"  {n_judge_calls} judge calls (150 samples x 6 models)")
    print(f"  Cost: ${p0_cost:.2f}")

    # ── Phase 1: Working conversations ──
    # 40 scenarios x 6 models x 3 runs x 5 turns = 3,600 generation turns
    n_trials = N_SCENARIOS * N_RUNS  # per model = 120
    p1_costs = {}
    for m in MODELS:
        t = AVG_TOKENS_PER_TURN[m]
        # 5 turns, but input grows each turn (conversation history)
        # Approximate: avg across all 5 turns already captured in pilot data
        trial_cost = cost(m, t["input"] * N_TURNS, t["output"] * N_TURNS)
        p1_costs[m] = trial_cost * n_trials
    p1_total = sum(p1_costs.values())
    phase_totals["Phase 1 (working conversations)"] = p1_total
    print(f"\nPhase 1: Working conversations")
    print(f"  {n_trials * len(MODELS)} trials ({n_trials} per model x 6 models)")
    print(f"  {n_trials * len(MODELS) * N_TURNS} API calls")
    for m in MODELS:
        print(f"    {m:25s}: ${p1_costs[m]:7.2f}")
    print(f"  Total: ${p1_total:.2f}")

    # ── Phase 2: Blind evaluation ──
    # 720 trials x 5 turns = 3,600 judge calls (single judge model)
    n_eval_calls = n_trials * len(MODELS) * N_TURNS
    # Use cheapest likely judge (gemini) and most expensive (gpt-4o) as range
    p2_min = cost("gemini-2.5-flash", JUDGE_TOKENS["input"], JUDGE_TOKENS["output"]) * n_eval_calls
    p2_max = cost("gpt-4o", JUDGE_TOKENS["input"], JUDGE_TOKENS["output"]) * n_eval_calls
    p2_mid = (p2_min + p2_max) / 2
    phase_totals["Phase 2 (blind evaluation)"] = p2_mid
    print(f"\nPhase 2: Blind evaluation (single judge)")
    print(f"  {n_eval_calls} judge calls")
    print(f"  Cost: ${p2_min:.2f} (if Gemini) to ${p2_max:.2f} (if GPT-4o)")

    # ── Phase 3: Model confidence (revision ceiling) ──
    # 40 scenarios x 6 models x 2 probes x ~8 turns avg = 3,840 generation turns
    # Plus evaluation of each: 40 x 6 x 2 x ~8 = 3,840 judge calls
    p3_gen_costs = {}
    for m in MODELS:
        t = AVG_TOKENS_PER_TURN[m]
        # 40 scenarios x 2 probes x avg 8 turns
        gen_calls = N_SCENARIOS * N_CONFIDENCE_PROBES * AVG_CONFIDENCE_TURNS
        p3_gen_costs[m] = cost(m, t["input"] * gen_calls, t["output"] * gen_calls)
    p3_gen = sum(p3_gen_costs.values())
    p3_eval = cost("gpt-4o", JUDGE_TOKENS["input"], JUDGE_TOKENS["output"]) * N_SCENARIOS * len(MODELS) * N_CONFIDENCE_PROBES * AVG_CONFIDENCE_TURNS
    p3_total = p3_gen + p3_eval
    phase_totals["Phase 3 (model confidence)"] = p3_total
    print(f"\nPhase 3: Model confidence (revision ceiling)")
    print(f"  Generation: ${p3_gen:.2f}")
    print(f"  Evaluation: ${p3_eval:.2f}")
    print(f"  Total: ${p3_total:.2f}")

    # ── Phase 3b: One-shot ceiling ──
    # 40 scenarios x 6 models x 3 runs = 720 single generation calls + 720 judge calls
    p3b_costs = {}
    for m in MODELS:
        t = AVG_TOKENS_PER_TURN[m]
        p3b_costs[m] = cost(m, t["input"], t["output"]) * n_trials
    p3b_gen = sum(p3b_costs.values())
    p3b_eval = cost("gpt-4o", JUDGE_TOKENS["input"], JUDGE_TOKENS["output"]) * n_trials * len(MODELS)
    p3b_total = p3b_gen + p3b_eval
    phase_totals["Phase 3b (one-shot ceiling)"] = p3b_total
    print(f"\nPhase 3b: One-shot ceiling")
    print(f"  {n_trials * len(MODELS)} generation calls + {n_trials * len(MODELS)} judge calls")
    print(f"  Total: ${p3b_total:.2f}")

    # ── Phase 4: Reversibility ──
    # 720 judge calls (comparison prompt, slightly larger)
    n_rev = n_trials * len(MODELS)
    p4_cost = cost("gpt-4o", 1000, 100) * n_rev  # larger prompt (two outputs)
    phase_totals["Phase 4 (reversibility)"] = p4_cost
    print(f"\nPhase 4: Reversibility")
    print(f"  {n_rev} comparison calls")
    print(f"  Total: ${p4_cost:.2f}")

    # ── Phase 5: Targeted feedback ──
    # Conditional on evaluator levels 1-2. Estimate ~40% of trials qualify.
    # Each qualifying trial: 1 targeted prompt + 1 generation + 1 eval
    n_targeted = int(n_trials * len(MODELS) * 0.4)
    p5_costs = {}
    for m in MODELS:
        t = AVG_TOKENS_PER_TURN[m]
        model_targeted = int(n_trials * 0.4)
        p5_costs[m] = cost(m, t["input"] * 2, t["output"] * 2) * model_targeted
    p5_gen = sum(p5_costs.values())
    p5_eval = cost("gpt-4o", JUDGE_TOKENS["input"], JUDGE_TOKENS["output"]) * n_targeted
    p5_total = p5_gen + p5_eval
    phase_totals["Phase 5 (targeted feedback)"] = p5_total
    print(f"\nPhase 5: Targeted feedback (est. {n_targeted} qualifying trials)")
    print(f"  Total: ${p5_total:.2f}")

    # ── Phase 6: Self-reflection ──
    # 720 calls (append to Phase 1 conversation, short output)
    n_refl = n_trials * len(MODELS)
    p6_costs = {}
    for m in MODELS:
        t = AVG_TOKENS_PER_TURN[m]
        # Full conversation context (~5 turns input) + short JSON output
        p6_costs[m] = cost(m, t["input"] * 5, 100) * n_trials
    p6_total = sum(p6_costs.values())
    phase_totals["Phase 6 (self-reflection)"] = p6_total
    print(f"\nPhase 6: Self-reflection")
    print(f"  {n_refl} calls")
    print(f"  Total: ${p6_total:.2f}")

    # ── GRAND TOTAL ──
    grand_total = sum(phase_totals.values())
    print(f"\n{'=' * 75}")
    print(f"  GRAND TOTAL: ${grand_total:.2f}")
    print(f"{'=' * 75}")
    print(f"\nBreakdown by phase:")
    for phase, cost_val in phase_totals.items():
        pct = cost_val / grand_total * 100
        print(f"  {phase:45s}  ${cost_val:7.2f}  ({pct:4.1f}%)")

    # Per-model breakdown
    print(f"\nPer-model cost estimate (Phase 1 only, largest component):")
    for m in sorted(p1_costs.keys(), key=lambda x: p1_costs[x], reverse=True):
        print(f"  {m:25s}: ${p1_costs[m]:7.2f}")

    # Buffer
    print(f"\nWith 20% buffer for retries/errors: ${grand_total * 1.2:.2f}")
    print(f"With 30% buffer: ${grand_total * 1.3:.2f}")


if __name__ == "__main__":
    estimate()
