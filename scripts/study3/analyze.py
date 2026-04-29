"""Analyze Study 3 (Revision Yield) results across all research questions.

RQ1:  Revision Yield Curve
RQ2:  Diminishing Return Point by domain
RQ3:  Do models respect the DRP?
RQ4:  Quality judgment vs conversational compliance
RQ5:  Evaluator robustness (nudge test)
RQ6:  Stylistic drift beyond DRP
RQ7:  Token cost of ignoring DRP
RQ8:  Targeted feedback vs generic prompting
RQ9:  Cross-model patterns
RQ10: One-shot ceiling test
RQ11: Reversibility test
RQ12: Exit ramp effectiveness
RQ13: Cross-model convergence
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
import pandas as pd
from scipy import stats as sp_stats

from scripts.config import (
    S3_EVALUATOR_RESULTS_PATH,
    S3_EXIT_RAMP_TRIALS_PATH,
    S3_FIGURES_DIR,
    S3_ONESHOT_TRIALS_PATH,
    S3_REVERSIBILITY_RESULTS_PATH,
    S3_STATS_DIR,
    S3_TARGETED_FEEDBACK_PATH,
    S3_WORKER_TRIALS_PATH,
)
from scripts.utils import load_jsonl


# ── Shared helpers ──

def classify_revision(response: str) -> bool:
    """Returns True if the response is a revision, False if it declines."""
    if not response:
        return False
    response_lower = response.lower()
    decline_phrases = [
        "looks good as is", "looks good as-is", "no changes needed",
        "no improvements needed", "no further changes", "no further improvements",
        "already well", "already good", "ready to use", "ready as is",
        "ready as-is", "satisfied with", "meets the requirements",
        "nothing to improve", "nothing i would change", "i think it's good",
        "i think this is good", "i think it looks good", "no, i think",
        "i wouldn't change", "i don't think any changes", "don't see any need",
        "no revisions needed", "the output is complete", "this is complete",
        "looks good", "is ready", "is done", "i agree", "well done",
        "complete as is", "no need",
    ]
    for phrase in decline_phrases:
        if phrase in response_lower:
            return False
    return True


def load_worker_turns() -> pd.DataFrame:
    """Expand worker trials into per-turn rows."""
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    rows = []
    for trial in [t for t in trials if t.get("status") == "success"]:
        for turn_idx, response in enumerate(trial["responses"]):
            turn = turn_idx + 1
            revised = True if turn == 1 else classify_revision(response)
            token_info = trial["token_counts"][turn_idx] if trial.get("token_counts") else {}
            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "scenario_id": trial["scenario_id"],
                "domain": trial["domain"],
                "run": trial["run"],
                "turn": turn,
                "revised": revised,
                "response_length": len(response),
                "output_tokens": token_info.get("output", 0) or 0,
                "input_tokens": token_info.get("input", 0) or 0,
            })
    return pd.DataFrame(rows)


def load_evaluator() -> pd.DataFrame:
    results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
    valid = [r for r in results if r.get("status") in ("done", "needs_work")]
    return pd.DataFrame(valid)


# ── RQ1: Revision Yield Curve ──

def rq1_revision_yield_curve(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ1: Revision Yield Curve ==")
    clean = eval_df[eval_df["condition"] == "clean"]

    quality_by_turn = clean.groupby("turn")["quality"].mean()
    # MRY = quality delta between consecutive turns
    turns = sorted(quality_by_turn.index)
    mry = {}
    for i in range(1, len(turns)):
        mry[turns[i]] = float(quality_by_turn[turns[i]] - quality_by_turn[turns[i-1]])

    print(f"\nMean quality by turn: {dict(zip(turns, [f'{quality_by_turn[t]:.2f}' for t in turns]))}")
    print(f"Marginal Revision Yield: {mry}")

    return {"quality_by_turn": {int(t): float(quality_by_turn[t]) for t in turns}, "mry": mry}


# ── RQ2: DRP by domain ──

def rq2_drp_by_domain(eval_df: pd.DataFrame) -> dict:
    print("\n== RQ2: Diminishing Return Point by Domain ==")
    clean = eval_df[eval_df["condition"] == "clean"]
    results = {}

    for domain in sorted(clean["domain"].unique()):
        subset = clean[clean["domain"] == domain]
        quality_by_turn = subset.groupby("turn")["quality"].mean()
        turns = sorted(quality_by_turn.index)

        # DRP = first turn where MRY <= 0
        drp = None
        for i in range(1, len(turns)):
            delta = quality_by_turn[turns[i]] - quality_by_turn[turns[i-1]]
            if delta <= 0:
                drp = turns[i]
                break

        results[domain] = {
            "quality_by_turn": {int(t): float(quality_by_turn[t]) for t in turns},
            "drp": drp,
        }
        print(f"  {domain}: DRP at turn {drp}, quality trajectory: {[f'{quality_by_turn[t]:.2f}' for t in turns]}")

    return results


# ── RQ3: Do models respect the DRP? ──

def rq3_overcorrection_rate(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ3: Do Models Respect the DRP? ==")
    clean = eval_df[eval_df["condition"] == "clean"]

    # At each turn: evaluator "done" rate vs worker revision rate
    eval_done = clean.groupby("turn").apply(lambda g: (g["status"] == "done").mean())
    worker_t2plus = worker_df[worker_df["turn"] >= 2]
    worker_rev = worker_t2plus.groupby("turn")["revised"].mean()

    print("\nTurn | Eval 'done' % | Worker revision % | Overcorrection gap")
    print("-" * 65)
    for turn in sorted(set(eval_done.index) & set(worker_rev.index)):
        gap = worker_rev[turn] - (1 - eval_done[turn])
        print(f"  {turn}   | {eval_done[turn]:.1%}          | {worker_rev[turn]:.1%}             | {gap:+.1%}")

    return {
        "eval_done_rate": {int(k): float(v) for k, v in eval_done.items()},
        "worker_revision_rate": {int(k): float(v) for k, v in worker_rev.items()},
    }


# ── RQ4: Compliance vs quality judgment ──

def rq4_compliance_mechanism(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ4: Compliance vs Quality Judgment ==")
    # Core logic: if evaluator says "done" at turn N but worker still revises at turn N,
    # the revision is compliance-driven, not quality-driven.
    clean = eval_df[eval_df["condition"] == "clean"]

    # Merge evaluator judgments with worker behavior per trial+turn
    worker_t2 = worker_df[worker_df["turn"] >= 2][["trial_id", "turn", "revised"]].copy()
    # Match eval to worker via worker_trial_id
    eval_match = clean[["worker_trial_id", "turn", "status"]].copy()
    eval_match = eval_match.rename(columns={"worker_trial_id": "trial_id"})

    merged = worker_t2.merge(eval_match, on=["trial_id", "turn"], how="inner")

    if merged.empty:
        print("  No matched data.")
        return {}

    # Cases where evaluator says done but worker revises = compliance
    compliance_cases = merged[(merged["status"] == "done") & (merged["revised"] == True)]
    total_done_evals = merged[merged["status"] == "done"]

    compliance_rate = len(compliance_cases) / len(total_done_evals) if len(total_done_evals) > 0 else 0
    print(f"  Evaluator says 'done': {len(total_done_evals)} cases")
    print(f"  Worker revises anyway: {len(compliance_cases)} ({compliance_rate:.1%})")
    print(f"  -> Compliance-driven revision rate: {compliance_rate:.1%}")

    return {
        "total_done_evals": len(total_done_evals),
        "compliance_revisions": len(compliance_cases),
        "compliance_rate": float(compliance_rate),
    }


# ── RQ5: Evaluator sycophancy (nudge test) ──

def rq5_nudge_test(eval_df: pd.DataFrame) -> dict:
    print("\n== RQ5: Evaluator Sycophancy (Nudge Test) ==")
    clean = eval_df[eval_df["condition"] == "clean"][["worker_trial_id", "turn", "status", "quality"]].copy()
    nudged = eval_df[eval_df["condition"] == "nudged"][["worker_trial_id", "turn", "status", "quality"]].copy()

    merged = clean.merge(nudged, on=["worker_trial_id", "turn"], suffixes=("_clean", "_nudged"))

    if merged.empty:
        print("  No paired data.")
        return {}

    # Flip rate: % of "done" that become "needs_work" under nudge
    done_clean = merged[merged["status_clean"] == "done"]
    flipped = (done_clean["status_nudged"] == "needs_work").sum() if len(done_clean) > 0 else 0
    flip_rate = flipped / len(done_clean) if len(done_clean) > 0 else 0

    print(f"  Paired judgments: {len(merged)}")
    print(f"  Clean 'done': {len(done_clean)}")
    print(f"  Flipped to 'needs_work' under nudge: {flipped} ({flip_rate:.1%})")

    # McNemar's test
    a = ((merged["status_clean"] == "done") & (merged["status_nudged"] == "done")).sum()
    b = ((merged["status_clean"] == "done") & (merged["status_nudged"] == "needs_work")).sum()
    c = ((merged["status_clean"] == "needs_work") & (merged["status_nudged"] == "done")).sum()
    d = ((merged["status_clean"] == "needs_work") & (merged["status_nudged"] == "needs_work")).sum()

    mcnemar_p = None
    if b + c > 0:
        chi2 = (abs(b - c) - 1) ** 2 / (b + c)
        mcnemar_p = float(sp_stats.chi2.sf(chi2, 1))
        print(f"  McNemar chi2={chi2:.2f}, p={mcnemar_p:.4f}")

    # Wilcoxon on quality
    quality_diff = merged["quality_clean"] - merged["quality_nudged"]
    non_zero = quality_diff[quality_diff != 0]
    wilcoxon_p = None
    if len(non_zero) > 0:
        stat, wilcoxon_p = sp_stats.wilcoxon(non_zero)
        wilcoxon_p = float(wilcoxon_p)
        print(f"  Wilcoxon (quality diff): stat={stat:.1f}, p={wilcoxon_p:.4f}, mean diff={quality_diff.mean():.3f}")

    return {"flip_rate": float(flip_rate), "mcnemar_p": mcnemar_p, "wilcoxon_p": wilcoxon_p}


# ── RQ6: Stylistic drift ──

def rq6_stylistic_drift(worker_df: pd.DataFrame) -> dict:
    print("\n== RQ6: Stylistic Drift Beyond DRP ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    rows = []
    for trial in successful:
        for turn_idx, response in enumerate(trial["responses"]):
            words = response.split()
            unique_words = set(w.lower() for w in words)
            ttr = len(unique_words) / len(words) if words else 0
            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": turn_idx + 1,
                "word_count": len(words),
                "type_token_ratio": ttr,
                "char_count": len(response),
            })

    df = pd.DataFrame(rows)
    drift = df.groupby("turn").agg({
        "word_count": "mean",
        "type_token_ratio": "mean",
        "char_count": "mean",
    })

    print("\nTurn | Mean words | Mean TTR  | Mean chars")
    print("-" * 50)
    for turn, row in drift.iterrows():
        print(f"  {turn}   | {row['word_count']:.0f}       | {row['type_token_ratio']:.3f}   | {row['char_count']:.0f}")

    # Spearman: turn vs word count (expecting positive = gets longer)
    rho_len, p_len = sp_stats.spearmanr(df["turn"], df["word_count"])
    rho_ttr, p_ttr = sp_stats.spearmanr(df["turn"], df["type_token_ratio"])
    print(f"\n  Turn vs word_count: rho={rho_len:.3f}, p={p_len:.4f}")
    print(f"  Turn vs TTR: rho={rho_ttr:.3f}, p={p_ttr:.4f}")

    return {
        "drift_by_turn": drift.to_dict(),
        "length_correlation": {"rho": float(rho_len), "p": float(p_len)},
        "ttr_correlation": {"rho": float(rho_ttr), "p": float(p_ttr)},
    }


# ── RQ7: Token cost ──

def rq7_token_cost(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ7: Token Cost of Ignoring the DRP ==")
    clean = eval_df[eval_df["condition"] == "clean"]

    # For each trial, find the first turn where evaluator says "done"
    drp_per_trial = clean[clean["status"] == "done"].groupby("worker_trial_id")["turn"].min()

    # Merge with token data
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    trial_tokens = {}
    for trial in [t for t in trials if t.get("status") == "success"]:
        total_output = sum((tc.get("output", 0) or 0) for tc in (trial.get("token_counts") or []))
        tokens_by_turn = [(tc.get("output", 0) or 0) for tc in (trial.get("token_counts") or [])]
        trial_tokens[trial["trial_id"]] = {
            "total_output": total_output,
            "by_turn": tokens_by_turn,
        }

    wasted_tokens = []
    for trial_id, drp_turn in drp_per_trial.items():
        if trial_id in trial_tokens:
            tokens = trial_tokens[trial_id]["by_turn"]
            # Tokens beyond the DRP
            wasted = sum(tokens[drp_turn:])  # drp_turn is 1-indexed, list is 0-indexed, so [drp_turn:] = after DRP
            total = sum(tokens)
            wasted_pct = wasted / total if total > 0 else 0
            wasted_tokens.append({"wasted": wasted, "total": total, "pct": wasted_pct})

    if wasted_tokens:
        mean_pct = np.mean([w["pct"] for w in wasted_tokens])
        mean_wasted = np.mean([w["wasted"] for w in wasted_tokens])
        total_wasted = sum(w["wasted"] for w in wasted_tokens)
        print(f"  Trials with DRP identified: {len(wasted_tokens)}")
        print(f"  Mean wasted token %: {mean_pct:.1%}")
        print(f"  Mean wasted tokens per trial: {mean_wasted:.0f}")
        print(f"  Total wasted output tokens: {total_wasted:,}")
        return {"mean_wasted_pct": float(mean_pct), "mean_wasted_tokens": float(mean_wasted), "n_trials": len(wasted_tokens)}

    print("  No DRP data available.")
    return {}


# ── RQ8: Targeted feedback ──

def rq8_targeted_feedback() -> dict:
    print("\n== RQ8: Targeted Feedback vs Generic Prompting ==")
    results = load_jsonl(S3_TARGETED_FEEDBACK_PATH)
    if not results:
        print("  No targeted feedback data.")
        return {}

    valid = [r for r in results if r.get("targeted_quality") and r.get("generic_next_quality")]
    if not valid:
        print("  No valid paired comparisons.")
        return {}

    targeted = [r["targeted_quality"] for r in valid]
    generic = [r["generic_next_quality"] for r in valid]
    deltas = [r["quality_delta"] for r in valid]

    mean_targeted = np.mean(targeted)
    mean_generic = np.mean(generic)
    mean_delta = np.mean(deltas)

    stat, p = sp_stats.wilcoxon([t - g for t, g in zip(targeted, generic) if t != g]) if any(t != g for t, g in zip(targeted, generic)) else (0, 1.0)

    print(f"  N pairs: {len(valid)}")
    print(f"  Mean targeted quality: {mean_targeted:.2f}")
    print(f"  Mean generic quality: {mean_generic:.2f}")
    print(f"  Mean delta (targeted - generic): {mean_delta:+.2f}")
    print(f"  Wilcoxon: stat={stat:.1f}, p={float(p):.4f}")

    return {"n": len(valid), "mean_targeted": float(mean_targeted), "mean_generic": float(mean_generic),
            "mean_delta": float(mean_delta), "wilcoxon_p": float(p)}


# ── RQ9: Cross-model ──

def rq9_cross_model(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ9: Cross-Model Comparison ==")
    clean = eval_df[eval_df["condition"] == "clean"]
    results = {}

    for model in sorted(worker_df["model"].unique()):
        m_eval = clean[clean["model"] == model]
        m_worker = worker_df[(worker_df["model"] == model) & (worker_df["turn"] >= 2)]

        eval_done = m_eval.groupby("turn").apply(lambda g: (g["status"] == "done").mean())
        worker_rev = m_worker.groupby("turn")["revised"].mean()
        quality = m_eval.groupby("turn")["quality"].mean()

        # Compute mean overcorrection gap
        shared_turns = sorted(set(eval_done.index) & set(worker_rev.index))
        gaps = [worker_rev[t] - (1 - eval_done[t]) for t in shared_turns]
        mean_gap = np.mean(gaps) if gaps else 0

        results[model] = {
            "eval_done_rate": {int(k): float(v) for k, v in eval_done.items()},
            "worker_revision_rate": {int(k): float(v) for k, v in worker_rev.items()},
            "quality_by_turn": {int(k): float(v) for k, v in quality.items()},
            "mean_overcorrection_gap": float(mean_gap),
        }
        print(f"  {model}: mean overcorrection gap = {mean_gap:+.1%}")

    return results


# ── RQ10: One-shot ceiling ──

def rq10_oneshot_ceiling(eval_df: pd.DataFrame) -> dict:
    print("\n== RQ10: One-Shot Ceiling Test ==")
    oneshot_trials = load_jsonl(S3_ONESHOT_TRIALS_PATH)
    if not oneshot_trials:
        print("  No one-shot data.")
        return {}

    # We need to evaluate one-shot outputs with the same blind evaluator
    # For now, compare token cost: one-shot tokens vs iterative total tokens
    successful = [t for t in oneshot_trials if t.get("status") == "success"]
    print(f"  One-shot trials: {len(successful)}")

    # Compare one-shot output tokens to iterative total output tokens
    worker_trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    worker_map = {}
    for t in worker_trials:
        if t.get("status") == "success":
            key = (t["model"], t["scenario_id"], t["run"])
            total_out = sum((tc.get("output", 0) or 0) for tc in (t.get("token_counts") or []))
            worker_map[key] = total_out

    comparisons = []
    for t in successful:
        key = (t["model"], t["scenario_id"], t["run"])
        oneshot_tokens = (t.get("tokens") or {}).get("output", 0) or 0
        iterative_tokens = worker_map.get(key, 0)
        if oneshot_tokens > 0 and iterative_tokens > 0:
            comparisons.append({
                "oneshot_tokens": oneshot_tokens,
                "iterative_tokens": iterative_tokens,
                "savings_pct": 1 - (oneshot_tokens / iterative_tokens),
            })

    if comparisons:
        mean_savings = np.mean([c["savings_pct"] for c in comparisons])
        print(f"  Mean token savings (one-shot vs iterative): {mean_savings:.1%}")
        return {"n": len(comparisons), "mean_token_savings": float(mean_savings)}

    return {}


# ── RQ11: Reversibility ──

def rq11_reversibility() -> dict:
    print("\n== RQ11: Reversibility Test ==")
    results = load_jsonl(S3_REVERSIBILITY_RESULTS_PATH)
    if not results:
        print("  No reversibility data.")
        return {}

    valid = [r for r in results if r.get("prefers_turn1") is not None]
    prefers_t1 = sum(1 for r in valid if r["prefers_turn1"])
    prefers_t5 = sum(1 for r in valid if not r["prefers_turn1"])
    ties = len(results) - len(valid)

    total = len(valid)
    t1_rate = prefers_t1 / total if total > 0 else 0

    print(f"  Total comparisons: {len(results)} (valid: {total}, ties: {ties})")
    print(f"  Prefers Turn 1: {prefers_t1} ({t1_rate:.1%})")
    print(f"  Prefers Turn 5: {prefers_t5} ({1-t1_rate:.1%})")

    # Binomial test: is preference for T1 significantly above chance (50%)?
    if total > 0:
        binom_p = float(sp_stats.binomtest(prefers_t1, total, 0.5).pvalue)
        print(f"  Binomial test (vs 50%): p={binom_p:.4f}")
    else:
        binom_p = None

    # By domain
    domain_results = {}
    for r in valid:
        d = r.get("domain", "unknown")
        if d not in domain_results:
            domain_results[d] = {"t1": 0, "t5": 0}
        if r["prefers_turn1"]:
            domain_results[d]["t1"] += 1
        else:
            domain_results[d]["t5"] += 1

    print("\n  By domain:")
    for domain, counts in sorted(domain_results.items()):
        n = counts["t1"] + counts["t5"]
        rate = counts["t1"] / n if n > 0 else 0
        print(f"    {domain}: T1 preferred {counts['t1']}/{n} ({rate:.1%})")

    return {"prefers_t1_rate": float(t1_rate), "n": total, "binom_p": binom_p, "by_domain": domain_results}


# ── RQ12: Exit ramp ──

def rq12_exit_ramp() -> dict:
    print("\n== RQ12: Exit Ramp Effectiveness ==")
    trials = load_jsonl(S3_EXIT_RAMP_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]
    if not successful:
        print("  No exit ramp data.")
        return {}

    # Turn 3 is the exit ramp. Did the model accept (decline to revise)?
    accepted = 0
    total = 0
    by_model = {}

    for trial in successful:
        if len(trial.get("responses", [])) >= 3:
            total += 1
            t3 = trial["responses"][2]
            is_rev = classify_revision(t3)
            if not is_rev:
                accepted += 1
            model = trial["model"]
            if model not in by_model:
                by_model[model] = {"accepted": 0, "total": 0}
            by_model[model]["total"] += 1
            if not is_rev:
                by_model[model]["accepted"] += 1

    accept_rate = accepted / total if total > 0 else 0
    print(f"  Total trials: {total}")
    print(f"  Exit ramp accepted: {accepted} ({accept_rate:.1%})")
    print(f"  Exit ramp ignored (revised anyway): {total - accepted} ({1-accept_rate:.1%})")

    print("\n  By model:")
    for model, counts in sorted(by_model.items()):
        rate = counts["accepted"] / counts["total"] if counts["total"] > 0 else 0
        print(f"    {model}: accepted {counts['accepted']}/{counts['total']} ({rate:.1%})")

    # Compare to Phase 1 turn 3 revision rate (all "Can this be improved?")
    worker_trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    worker_t3_revisions = 0
    worker_t3_total = 0
    for trial in [t for t in worker_trials if t.get("status") == "success"]:
        if len(trial.get("responses", [])) >= 3:
            worker_t3_total += 1
            if classify_revision(trial["responses"][2]):
                worker_t3_revisions += 1

    baseline_rate = worker_t3_revisions / worker_t3_total if worker_t3_total > 0 else 0
    reduction = baseline_rate - (1 - accept_rate)
    print(f"\n  Baseline turn-3 revision rate (Phase 1): {baseline_rate:.1%}")
    print(f"  Exit ramp turn-3 revision rate: {1-accept_rate:.1%}")
    print(f"  Reduction: {reduction:+.1%}")

    return {"accept_rate": float(accept_rate), "baseline_revision_rate": float(baseline_rate),
            "by_model": {m: c["accepted"]/c["total"] for m, c in by_model.items() if c["total"] > 0}}


# ── RQ13: Cross-model convergence ──

def rq13_convergence() -> dict:
    print("\n== RQ13: Cross-Model Convergence ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    # Group by scenario+run, compute pairwise length similarity across models per turn
    from collections import defaultdict
    grouped = defaultdict(lambda: defaultdict(dict))
    for trial in successful:
        key = (trial["scenario_id"], trial["run"])
        for turn_idx, response in enumerate(trial["responses"]):
            grouped[key][turn_idx + 1][trial["model"]] = len(response)

    # For each turn, compute coefficient of variation of response lengths across models
    cv_by_turn = defaultdict(list)
    for key, turns in grouped.items():
        for turn, model_lengths in turns.items():
            if len(model_lengths) >= 2:
                lengths = list(model_lengths.values())
                mean_len = np.mean(lengths)
                std_len = np.std(lengths)
                cv = std_len / mean_len if mean_len > 0 else 0
                cv_by_turn[turn].append(cv)

    print("\nCoefficient of variation in response length across models by turn:")
    print("(Lower CV = more convergence)")
    results = {}
    for turn in sorted(cv_by_turn.keys()):
        mean_cv = np.mean(cv_by_turn[turn])
        results[turn] = float(mean_cv)
        print(f"  Turn {turn}: CV = {mean_cv:.3f}")

    if len(results) >= 2:
        turns_list = sorted(results.keys())
        cvs = [results[t] for t in turns_list]
        rho, p = sp_stats.spearmanr(turns_list, cvs)
        print(f"\n  Spearman (turn vs CV): rho={rho:.3f}, p={p:.4f}")
        print(f"  {'Converging' if rho < 0 else 'Diverging'} across turns")

    return {"cv_by_turn": results}


# ── Main ──

def main():
    S3_STATS_DIR.mkdir(parents=True, exist_ok=True)

    worker_df = load_worker_turns()
    eval_df = load_evaluator()

    if worker_df.empty:
        print("No worker data. Run Phase 1 first.")
        return
    if eval_df.empty:
        print("No evaluator data. Run Phase 2 first.")
        return

    print(f"Loaded: {len(worker_df)} worker turn-rows, {len(eval_df)} evaluator judgments")
    print(f"Models: {sorted(worker_df['model'].unique())}")
    print(f"Domains: {sorted(worker_df['domain'].unique())}")

    results = {}
    results["rq1"] = rq1_revision_yield_curve(worker_df, eval_df)
    results["rq2"] = rq2_drp_by_domain(eval_df)
    results["rq3"] = rq3_overcorrection_rate(worker_df, eval_df)
    results["rq4"] = rq4_compliance_mechanism(worker_df, eval_df)
    results["rq5"] = rq5_nudge_test(eval_df)
    results["rq6"] = rq6_stylistic_drift(worker_df)
    results["rq7"] = rq7_token_cost(worker_df, eval_df)
    results["rq8"] = rq8_targeted_feedback()
    results["rq9"] = rq9_cross_model(worker_df, eval_df)
    results["rq10"] = rq10_oneshot_ceiling(eval_df)
    results["rq11"] = rq11_reversibility()
    results["rq12"] = rq12_exit_ramp()
    results["rq13"] = rq13_convergence()

    results_path = S3_STATS_DIR / "study3_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved all results to {results_path}")
    print("Done.")


if __name__ == "__main__":
    main()
