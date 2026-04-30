"""Analyze Study 3 (Revision Yield) results across all research questions.

RQ1:  Revision Yield Curve (quality trajectory by turn)
RQ2:  Diminishing Return Point by domain
RQ3:  Do models respect the DRP?
RQ4:  Quality judgment vs conversational compliance
RQ5:  Token cost of zero-value revisions
RQ6:  Stylistic drift and bloat over turns
RQ7:  Targeted feedback vs generic prompting
RQ8:  Cross-model patterns (do all 6 models show overcorrection?)
RQ9:  One-shot ceiling vs iterative
RQ10: Reversibility test (does model prefer its first draft?)
RQ11: Cross-model output convergence
RQ12: Instruction adherence decay
RQ13: Performative revision (cosmetic-only changes)
RQ14: Can the model spot its own overcorrection? (self-reflection)
RQ15: Revision Yield equation and optimal stopping turn (CARY)
RQ16: Unit economics (practical cost at budget tiers)
RQ17: Overcorrection magnitude (continuous OCS, not binary)
"""

import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
import pandas as pd
from scipy import stats as sp_stats

from scripts.config import (
    S3_EVALUATOR_RESULTS_PATH,
    S3_FIGURES_DIR,
    S3_ONESHOT_TRIALS_PATH,
    S3_REVERSIBILITY_RESULTS_PATH,
    S3_SELF_REFLECTION_PATH,
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
        # New decline phrases for neutral probe
        "keep this as my final", "this is my final version",
        "i'm satisfied", "no revisions needed", "i'd like to keep this",
        "i would like to keep this", "keep this as the final",
        "happy with this version", "this version is ready",
        "final version", "no changes", "i'll keep this",
        "i will keep this",
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
    """Load evaluator results with 6-level scale."""
    results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
    valid = [r for r in results if r.get("level") is not None]
    return pd.DataFrame(valid)


# ── RQ1: Revision Yield Curve ──

def rq1_revision_yield_curve(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ1: Revision Yield Curve ==")

    level_by_turn = eval_df.groupby("turn")["level"].mean()
    turns = sorted(level_by_turn.index)

    # MRY = quality delta between consecutive turns
    mry = {}
    for i in range(1, len(turns)):
        mry[turns[i]] = float(level_by_turn[turns[i]] - level_by_turn[turns[i-1]])

    print(f"\nMean level by turn: {dict(zip(turns, [f'{level_by_turn[t]:.2f}' for t in turns]))}")
    print(f"Marginal Revision Yield: {mry}")

    return {"level_by_turn": {int(t): float(level_by_turn[t]) for t in turns}, "mry": mry}


# ── RQ2: DRP by domain ──

def rq2_drp_by_domain(eval_df: pd.DataFrame) -> dict:
    print("\n== RQ2: Diminishing Return Point by Domain ==")
    results = {}

    for domain in sorted(eval_df["domain"].unique()):
        subset = eval_df[eval_df["domain"] == domain]
        level_by_turn = subset.groupby("turn")["level"].mean()
        turns = sorted(level_by_turn.index)

        # DRP = first turn where evaluator level >= 4 (Sufficient)
        drp = None
        for t in turns:
            if level_by_turn[t] >= 4.0:
                drp = t
                break

        results[domain] = {
            "level_by_turn": {int(t): float(level_by_turn[t]) for t in turns},
            "drp": drp,
        }
        print(f"  {domain}: DRP at turn {drp}, level trajectory: {[f'{level_by_turn[t]:.2f}' for t in turns]}")

    return results


# ── RQ3: Do models respect the DRP? ──

def rq3_overcorrection_rate(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ3: Do Models Respect the DRP? ==")

    # At each turn: evaluator "done" rate (level >= 4) vs worker revision rate
    eval_done = eval_df.groupby("turn").apply(lambda g: (g["level"] >= 3).mean())
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

    worker_t2 = worker_df[worker_df["turn"] >= 2][["trial_id", "turn", "revised"]].copy()
    eval_match = eval_df[["worker_trial_id", "turn", "level"]].copy()
    eval_match = eval_match.rename(columns={"worker_trial_id": "trial_id"})

    merged = worker_t2.merge(eval_match, on=["trial_id", "turn"], how="inner")

    if merged.empty:
        print("  No matched data.")
        return {}

    # Cases where evaluator says done (level >= 4) but worker revises = compliance
    compliance_cases = merged[(merged["level"] >= 3) & (merged["revised"] == True)]
    total_done_evals = merged[merged["level"] >= 3]

    compliance_rate = len(compliance_cases) / len(total_done_evals) if len(total_done_evals) > 0 else 0
    print(f"  Evaluator says 'done' (level >= 4): {len(total_done_evals)} cases")
    print(f"  Worker revises anyway: {len(compliance_cases)} ({compliance_rate:.1%})")
    print(f"  -> Compliance-driven revision rate: {compliance_rate:.1%}")

    return {
        "total_done_evals": len(total_done_evals),
        "compliance_revisions": len(compliance_cases),
        "compliance_rate": float(compliance_rate),
    }


# ── RQ5: Token cost ──

def rq5_token_cost(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ5: Token Cost of Zero-Value Revisions ==")

    # For each trial, find the first turn where evaluator level >= 4
    drp_per_trial = eval_df[eval_df["level"] >= 3].groupby("worker_trial_id")["turn"].min()

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
            wasted = sum(tokens[drp_turn:])  # tokens after DRP
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

    rho_len, p_len = sp_stats.spearmanr(df["turn"], df["word_count"])
    rho_ttr, p_ttr = sp_stats.spearmanr(df["turn"], df["type_token_ratio"])
    print(f"\n  Turn vs word_count: rho={rho_len:.3f}, p={p_len:.4f}")
    print(f"  Turn vs TTR: rho={rho_ttr:.3f}, p={p_ttr:.4f}")

    return {
        "drift_by_turn": drift.to_dict(),
        "length_correlation": {"rho": float(rho_len), "p": float(p_len)},
        "ttr_correlation": {"rho": float(rho_ttr), "p": float(p_ttr)},
    }


# ── RQ7: Targeted feedback ──

def rq7_targeted_feedback() -> dict:
    print("\n== RQ7: Targeted Feedback vs Generic Prompting ==")
    results = load_jsonl(S3_TARGETED_FEEDBACK_PATH)
    if not results:
        print("  No targeted feedback data.")
        return {}

    valid = [r for r in results if r.get("targeted_level") and r.get("generic_next_level")]
    if not valid:
        print("  No valid paired comparisons.")
        return {}

    targeted = [r["targeted_level"] for r in valid]
    generic = [r["generic_next_level"] for r in valid]
    deltas = [r["level_delta"] for r in valid]

    mean_targeted = np.mean(targeted)
    mean_generic = np.mean(generic)
    mean_delta = np.mean(deltas)

    diffs = [t - g for t, g in zip(targeted, generic) if t != g]
    stat, p = sp_stats.wilcoxon(diffs) if diffs else (0, 1.0)

    print(f"  N pairs: {len(valid)}")
    print(f"  Mean targeted level: {mean_targeted:.2f}")
    print(f"  Mean generic level: {mean_generic:.2f}")
    print(f"  Mean delta (targeted - generic): {mean_delta:+.2f}")
    print(f"  Wilcoxon: stat={stat:.1f}, p={float(p):.4f}")

    return {"n": len(valid), "mean_targeted": float(mean_targeted), "mean_generic": float(mean_generic),
            "mean_delta": float(mean_delta), "wilcoxon_p": float(p)}


# ── RQ8: Cross-model ──

def rq8_cross_model(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ8: Cross-Model Comparison ==")
    results = {}

    for model in sorted(worker_df["model"].unique()):
        m_eval = eval_df[eval_df["model"] == model]
        m_worker = worker_df[(worker_df["model"] == model) & (worker_df["turn"] >= 2)]

        eval_done = m_eval.groupby("turn").apply(lambda g: (g["level"] >= 3).mean())
        worker_rev = m_worker.groupby("turn")["revised"].mean()
        level = m_eval.groupby("turn")["level"].mean()

        shared_turns = sorted(set(eval_done.index) & set(worker_rev.index))
        gaps = [worker_rev[t] - (1 - eval_done[t]) for t in shared_turns]
        mean_gap = np.mean(gaps) if gaps else 0

        results[model] = {
            "eval_done_rate": {int(k): float(v) for k, v in eval_done.items()},
            "worker_revision_rate": {int(k): float(v) for k, v in worker_rev.items()},
            "level_by_turn": {int(k): float(v) for k, v in level.items()},
            "mean_overcorrection_gap": float(mean_gap),
        }
        print(f"  {model}: mean overcorrection gap = {mean_gap:+.1%}")

    return results


# ── RQ9: One-shot ceiling ──

def rq9_oneshot_ceiling(eval_df: pd.DataFrame) -> dict:
    print("\n== RQ9: One-Shot Ceiling Test ==")
    oneshot_trials = load_jsonl(S3_ONESHOT_TRIALS_PATH)
    if not oneshot_trials:
        print("  No one-shot data.")
        return {}

    successful = [t for t in oneshot_trials if t.get("status") == "success"]
    print(f"  One-shot trials: {len(successful)}")

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


# ── RQ10: Reversibility ──

def rq10_reversibility() -> dict:
    print("\n== RQ10: Reversibility Test ==")
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

    if total > 0:
        binom_p = float(sp_stats.binomtest(prefers_t1, total, 0.5).pvalue)
        print(f"  Binomial test (vs 50%): p={binom_p:.4f}")
    else:
        binom_p = None

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


# ── RQ11: Cross-model convergence ──

def rq11_convergence() -> dict:
    print("\n== RQ11: Cross-Model Convergence ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    grouped = defaultdict(lambda: defaultdict(dict))
    for trial in successful:
        key = (trial["scenario_id"], trial["run"])
        for turn_idx, response in enumerate(trial["responses"]):
            grouped[key][turn_idx + 1][trial["model"]] = len(response)

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


# ── RQ12: Instruction adherence decay ──

def rq12_instruction_adherence(worker_df: pd.DataFrame) -> dict:
    print("\n== RQ12: Instruction Adherence Decay ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    # Measure adherence proxies: response still addresses the original task
    # Use word overlap with task prompt as a simple adherence signal
    rows = []
    for trial in successful:
        task_words = set(trial["task_prompt"].lower().split())
        for turn_idx, response in enumerate(trial["responses"]):
            resp_words = set(response.lower().split())
            overlap = len(task_words & resp_words) / len(task_words) if task_words else 0
            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": turn_idx + 1,
                "task_overlap": overlap,
            })

    df = pd.DataFrame(rows)
    if df.empty:
        print("  No data.")
        return {}

    overlap_by_turn = df.groupby("turn")["task_overlap"].mean()
    print("\nTurn | Mean task-word overlap")
    print("-" * 35)
    for turn, overlap in overlap_by_turn.items():
        print(f"  {turn}   | {overlap:.3f}")

    rho, p = sp_stats.spearmanr(df["turn"], df["task_overlap"])
    print(f"\n  Spearman (turn vs overlap): rho={rho:.3f}, p={p:.4f}")

    return {
        "overlap_by_turn": {int(k): float(v) for k, v in overlap_by_turn.items()},
        "correlation": {"rho": float(rho), "p": float(p)},
    }


# ── RQ13: Performative revision (cosmetic-only changes) ──

def rq13_performative_revision() -> dict:
    print("\n== RQ13: Performative Revision (Cosmetic-Only Changes) ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    cosmetic_count = 0
    total_revisions = 0

    for trial in successful:
        for turn_idx in range(1, len(trial["responses"])):
            prev = trial["responses"][turn_idx - 1]
            curr = trial["responses"][turn_idx]

            if not classify_revision(curr):
                continue

            total_revisions += 1

            # Cosmetic = only whitespace, punctuation, or case changes
            prev_words = re.sub(r'[^\w\s]', '', prev.lower()).split()
            curr_words = re.sub(r'[^\w\s]', '', curr.lower()).split()

            # If the normalized word lists are identical, it's cosmetic
            if prev_words == curr_words:
                cosmetic_count += 1

    cosmetic_rate = cosmetic_count / total_revisions if total_revisions > 0 else 0
    print(f"  Total revisions analyzed: {total_revisions}")
    print(f"  Cosmetic-only changes: {cosmetic_count} ({cosmetic_rate:.1%})")

    return {"total_revisions": total_revisions, "cosmetic_count": cosmetic_count, "cosmetic_rate": float(cosmetic_rate)}


# ── RQ14: Self-reflection ──

def rq14_self_reflection() -> dict:
    print("\n== RQ14: Self-Reflection ==")
    results = load_jsonl(S3_SELF_REFLECTION_PATH)
    if not results:
        print("  No self-reflection data.")
        return {}

    valid = [r for r in results if r.get("recommended_turn") is not None]
    if not valid:
        print("  No valid responses.")
        return {}

    rec_turns = [r["recommended_turn"] for r in valid]
    mean_rec = np.mean(rec_turns)
    rec_dist = defaultdict(int)
    for t in rec_turns:
        rec_dist[t] += 1

    print(f"  Valid responses: {len(valid)}")
    print(f"  Mean recommended turn: {mean_rec:.2f}")
    print(f"  Distribution: {dict(sorted(rec_dist.items()))}")

    # How often does model recommend something other than the last turn?
    not_last = sum(1 for t in rec_turns if t < 5)
    not_last_rate = not_last / len(rec_turns)
    print(f"  Recommends not-last turn: {not_last} ({not_last_rate:.1%})")

    # By model
    by_model = defaultdict(list)
    for r in valid:
        by_model[r["model"]].append(r["recommended_turn"])
    print("\n  By model:")
    for model in sorted(by_model.keys()):
        turns = by_model[model]
        print(f"    {model}: mean={np.mean(turns):.2f}, not-last={sum(1 for t in turns if t < 5)}/{len(turns)}")

    return {
        "mean_recommended_turn": float(mean_rec),
        "distribution": dict(rec_dist),
        "not_last_rate": float(not_last_rate),
        "by_model": {m: {"mean": float(np.mean(t)), "n": len(t)} for m, t in by_model.items()},
    }


# ── RQ15: Revision Yield Equations (MRY, CRY, CARY) ──

def compute_mry(quality_by_turn: dict, tokens_by_turn: dict) -> dict:
    """Marginal Revision Yield: MRY(t) = [Q(t) - Q(t-1)] / T(t)"""
    turns = sorted(quality_by_turn.keys())
    mry = {}
    for i in range(1, len(turns)):
        t = turns[i]
        t_prev = turns[i-1]
        token_t = tokens_by_turn.get(t, 1)
        mry[t] = (quality_by_turn[t] - quality_by_turn[t_prev]) / max(token_t, 1)
    return mry


def compute_cry(quality_by_turn: dict, tokens_by_turn: dict) -> dict:
    """Cumulative Revision Yield: CRY(n) = [Q(n) - Q(1)] / sum T(2..n)"""
    turns = sorted(quality_by_turn.keys())
    if len(turns) < 2:
        return {}
    q1 = quality_by_turn[turns[0]]
    cry = {}
    cum_tokens = 0
    for i in range(1, len(turns)):
        t = turns[i]
        cum_tokens += tokens_by_turn.get(t, 0)
        if cum_tokens > 0:
            cry[t] = (quality_by_turn[t] - q1) / cum_tokens
        else:
            cry[t] = 0.0
    return cry


def compute_cary(quality_by_turn: dict, tokens_by_turn: dict, C: float) -> dict:
    """Cost-Adjusted Revision Yield: CARY(t) = [Q(t)/4] * e^(-C * T_cum(t))"""
    turns = sorted(quality_by_turn.keys())
    cary = {}
    t_cum = 0
    for t in turns:
        t_cum += tokens_by_turn.get(t, 0)
        cary[t] = (quality_by_turn[t] / 6.0) * math.exp(-C * t_cum)
    return cary


def rq15_revision_yield_equations(eval_df: pd.DataFrame, worker_df: pd.DataFrame) -> dict:
    print("\n== RQ15: Revision Yield Equations ==")

    # Aggregate quality and tokens by turn
    level_by_turn = eval_df.groupby("turn")["level"].mean().to_dict()
    tokens_by_turn = worker_df.groupby("turn")["output_tokens"].mean().to_dict()

    mry = compute_mry(level_by_turn, tokens_by_turn)
    cry = compute_cry(level_by_turn, tokens_by_turn)

    # CARY at multiple C values
    c_values = {
        "unlimited": 0,
        "api_heavy": 2e-8,
        "api_light": 2e-7,
        "pro": 5e-7,
        "max": 1e-6,
        "plus": 2e-6,
        "free": 1e-5,
    }

    cary_results = {}
    optimal_stops = {}
    for label, c_val in c_values.items():
        cary = compute_cary(level_by_turn, tokens_by_turn, c_val)
        cary_results[label] = {int(k): float(v) for k, v in cary.items()}
        if cary:
            t_star = max(cary.keys(), key=lambda t: cary[t])
            optimal_stops[label] = int(t_star)

    print(f"\nMRY: {mry}")
    print(f"CRY: {cry}")
    print(f"Optimal stopping turns by budget tier: {optimal_stops}")

    # DRP using MRY definition
    drp = None
    for t in sorted(mry.keys()):
        if mry[t] <= 0:
            drp = t
            break

    print(f"DRP (first turn with MRY <= 0): {drp}")

    return {
        "mry": {int(k): float(v) for k, v in mry.items()},
        "cry": {int(k): float(v) for k, v in cry.items()},
        "cary": cary_results,
        "optimal_stops": optimal_stops,
        "drp": drp,
    }


# ── RQ16: Unit economics ──

# Real 2025 API pricing (per output token)
API_PRICING = {
    "gpt-4o": 10.0 / 1_000_000,       # $10/1M output tokens
    "claude-sonnet-4": 15.0 / 1_000_000,  # $15/1M output tokens
    "gemini-2.5-flash": 0.40 / 1_000_000,  # $0.40/1M output tokens
    "llama-3.1-70b": 0.88 / 1_000_000,   # $0.88/1M output tokens
    "mistral-large": 2.00 / 1_000_000,   # $2.00/1M output tokens
    "qwen-2.5-72b": 0.90 / 1_000_000,    # $0.90/1M output tokens
}

BUDGET_TIERS = {
    "free": 100_000,
    "plus": 500_000,
    "pro": 2_000_000,
    "max": 2_000_000,
    "api_light": 5_000_000,
    "api_heavy": 50_000_000,
}


def rq16_unit_economics(eval_df: pd.DataFrame, worker_df: pd.DataFrame) -> dict:
    print("\n== RQ16: Unit Economics ==")
    results = {}

    for model in sorted(worker_df["model"].unique()):
        m_eval = eval_df[eval_df["model"] == model]
        m_worker = worker_df[worker_df["model"] == model]

        level_by_turn = m_eval.groupby("turn")["level"].mean().to_dict()
        tokens_by_turn = m_worker.groupby("turn")["output_tokens"].mean().to_dict()
        turns = sorted(level_by_turn.keys())

        if not turns:
            continue

        # Tokens for each stopping strategy
        t1_tokens = tokens_by_turn.get(1, 0)
        full_tokens = sum(tokens_by_turn.get(t, 0) for t in turns)

        # Find optimal stop using CARY at C=5e-7 (Pro tier)
        cary = compute_cary(level_by_turn, tokens_by_turn, 5e-7)
        t_star = max(cary.keys(), key=lambda t: cary[t]) if cary else 1
        opt_tokens = sum(tokens_by_turn.get(t, 0) for t in turns if t <= t_star)

        # Quality at each strategy
        q1 = level_by_turn.get(1, 0)
        q_opt = level_by_turn.get(t_star, 0)
        q_full = level_by_turn.get(max(turns), 0)

        # Revision tax
        revision_tax = ((full_tokens - opt_tokens) / opt_tokens * 100) if opt_tokens > 0 else 0

        # Token waste rate
        token_waste = ((full_tokens - opt_tokens) / full_tokens * 100) if full_tokens > 0 else 0

        # Dollar cost of overcorrection
        price = API_PRICING.get(model, 0)
        waste_dollars = (full_tokens - opt_tokens) * price

        model_result = {
            "t_star": int(t_star),
            "t1_tokens": float(t1_tokens),
            "opt_tokens": float(opt_tokens),
            "full_tokens": float(full_tokens),
            "q1": float(q1),
            "q_opt": float(q_opt),
            "q_full": float(q_full),
            "revision_tax_pct": float(revision_tax),
            "token_waste_pct": float(token_waste),
            "waste_dollars_per_task": float(waste_dollars),
        }

        # Per-domain breakdown
        domain_results = {}
        for domain in sorted(m_worker["domain"].unique()):
            d_eval = m_eval[m_eval["domain"] == domain]
            d_worker = m_worker[m_worker["domain"] == domain]
            d_level = d_eval.groupby("turn")["level"].mean().to_dict()
            d_tokens = d_worker.groupby("turn")["output_tokens"].mean().to_dict()
            d_turns = sorted(d_level.keys())
            if not d_turns:
                continue
            d_cary = compute_cary(d_level, d_tokens, 5e-7)
            d_tstar = max(d_cary.keys(), key=lambda t: d_cary[t]) if d_cary else 1
            d_full = sum(d_tokens.get(t, 0) for t in d_turns)
            d_opt = sum(d_tokens.get(t, 0) for t in d_turns if t <= d_tstar)
            d_tax = ((d_full - d_opt) / d_opt * 100) if d_opt > 0 else 0
            domain_results[domain] = {
                "t_star": int(d_tstar),
                "revision_tax_pct": float(d_tax),
                "q_opt": float(d_level.get(d_tstar, 0)),
                "q_full": float(d_level.get(max(d_turns), 0)),
            }

        model_result["by_domain"] = domain_results
        results[model] = model_result

        print(f"\n  {model}:")
        print(f"    Optimal stop: turn {t_star}")
        print(f"    Quality: T1={q1:.2f}, Optimal={q_opt:.2f}, Full={q_full:.2f}")
        print(f"    Tokens: T1={t1_tokens:.0f}, Optimal={opt_tokens:.0f}, Full={full_tokens:.0f}")
        print(f"    Revision Tax: {revision_tax:.0f}%")
        print(f"    Waste per task: ${waste_dollars:.4f}")

    return results


# ── RQ17: Overcorrection Magnitude (continuous OCS) ──

def rq17_overcorrection_magnitude(eval_df: pd.DataFrame, worker_df: pd.DataFrame) -> dict:
    print("\n== RQ17: Overcorrection Magnitude (OCS) ==")

    # For each trial, find t_done (first turn with level >= 4)
    drp_per_trial = eval_df[eval_df["level"] >= 3].groupby("worker_trial_id")["turn"].min()

    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    trial_data = {}
    for t in trials:
        if t.get("status") == "success":
            total_tokens = sum((tc.get("output", 0) or 0) for tc in (t.get("token_counts") or []))
            tokens_by_turn = [(tc.get("output", 0) or 0) for tc in (t.get("token_counts") or [])]
            trial_data[t["trial_id"]] = {
                "total_tokens": total_tokens,
                "tokens_by_turn": tokens_by_turn,
                "n_turns": len(t["responses"]),
                "model": t["model"],
                "domain": t["domain"],
            }

    # Get quality at t_done and final turn
    eval_by_trial_turn = {}
    for _, row in eval_df.iterrows():
        eval_by_trial_turn[(row["worker_trial_id"], row["turn"])] = row["level"]

    ocs_scores = []
    for trial_id, t_done in drp_per_trial.items():
        if trial_id not in trial_data:
            continue
        td = trial_data[trial_id]
        n_turns = td["n_turns"]
        max_er = n_turns - t_done

        if max_er <= 0:
            continue

        # Component 1: Excess Rounds
        er = n_turns - t_done

        # Component 2: Wasted Token Fraction
        tokens_after = sum(td["tokens_by_turn"][t_done:])
        total_tokens = td["total_tokens"]
        wtf = tokens_after / total_tokens if total_tokens > 0 else 0

        # Component 3: Quality Regression
        q_done = eval_by_trial_turn.get((trial_id, t_done), None)
        q_final = eval_by_trial_turn.get((trial_id, n_turns), None)
        if q_done is not None and q_final is not None:
            qr = max(0, q_done - q_final)
        else:
            qr = 0

        # Composite OCS
        ocs = 0.25 * (er / max_er) + 0.25 * wtf + 0.50 * (qr / 5.0)

        ocs_scores.append({
            "trial_id": trial_id,
            "model": td["model"],
            "domain": td["domain"],
            "t_done": int(t_done),
            "excess_rounds": er,
            "wasted_token_fraction": float(wtf),
            "quality_regression": float(qr),
            "ocs": float(ocs),
        })

    if not ocs_scores:
        print("  No OCS data available.")
        return {}

    ocs_df = pd.DataFrame(ocs_scores)
    mean_ocs = ocs_df["ocs"].mean()
    print(f"  Trials with OCS computed: {len(ocs_df)}")
    print(f"  Mean OCS: {mean_ocs:.3f}")
    print(f"  Mean components:")
    print(f"    Excess Rounds (norm): {ocs_df['excess_rounds'].mean() / ocs_df['excess_rounds'].apply(lambda x: max(x, 1)).mean():.3f}")
    print(f"    Wasted Token Fraction: {ocs_df['wasted_token_fraction'].mean():.3f}")
    print(f"    Quality Regression: {ocs_df['quality_regression'].mean():.3f}")

    # By model
    by_model = {}
    print("\n  By model:")
    for model in sorted(ocs_df["model"].unique()):
        m_df = ocs_df[ocs_df["model"] == model]
        m_mean = m_df["ocs"].mean()
        by_model[model] = float(m_mean)
        print(f"    {model}: mean OCS = {m_mean:.3f} (n={len(m_df)})")

    # By domain
    by_domain = {}
    print("\n  By domain:")
    for domain in sorted(ocs_df["domain"].unique()):
        d_df = ocs_df[ocs_df["domain"] == domain]
        d_mean = d_df["ocs"].mean()
        by_domain[domain] = float(d_mean)
        print(f"    {domain}: mean OCS = {d_mean:.3f} (n={len(d_df)})")

    return {
        "mean_ocs": float(mean_ocs),
        "n_trials": len(ocs_df),
        "by_model": by_model,
        "by_domain": by_domain,
    }


# ── Data Integrity Validator ──

def validate_data_integrity(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    """Run pre-analysis checks to catch data quality issues before they corrupt results."""
    print("\n== Data Integrity Validation ==")
    issues = []

    # 1. Check for None responses in worker trials
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]
    none_responses = 0
    truncated = 0
    for trial in successful:
        for i, resp in enumerate(trial.get("responses", [])):
            if resp is None:
                none_responses += 1
                issues.append(f"None response: {trial['trial_id']} turn {i+1}")
        for tc in (trial.get("token_counts") or []):
            fr = tc.get("finish_reason", "")
            if fr and str(fr) in ("length", "max_tokens", "MAX_TOKENS", "FinishReason.MAX_TOKENS", "2"):
                truncated += 1

    print(f"  Worker trials: {len(successful)} successful")
    print(f"  None responses: {none_responses} {'(PROBLEM)' if none_responses else '(OK)'}")
    print(f"  Truncated responses (hit max_tokens): {truncated} {'(WARNING)' if truncated else '(OK)'}")

    # 2. Check for null token counts
    null_tokens = worker_df["output_tokens"].isna().sum() + (worker_df["output_tokens"] == 0).sum()
    print(f"  Null/zero output token counts: {null_tokens}/{len(worker_df)} rows")

    # 3. Check evaluator coverage
    expected_evals = len(worker_df)
    actual_evals = len(eval_df)
    coverage = actual_evals / expected_evals if expected_evals > 0 else 0
    print(f"  Evaluator coverage: {actual_evals}/{expected_evals} ({coverage:.1%})")

    # 4. Check for null evaluator levels
    null_levels = eval_df["level"].isna().sum()
    print(f"  Null evaluator levels: {null_levels}/{len(eval_df)} {'(WARNING)' if null_levels > 0 else '(OK)'}")

    # 5. Check level distribution (should not cluster at extremes)
    if not eval_df.empty:
        level_dist = eval_df["level"].value_counts().sort_index()
        print(f"  Level distribution: {dict(level_dist)}")
        most_common_pct = level_dist.max() / len(eval_df)
        if most_common_pct > 0.6:
            issues.append(f"Evaluator level distribution heavily skewed: {most_common_pct:.1%} at one level")
            print(f"  WARNING: {most_common_pct:.1%} of ratings at one level")

    # 6. Check trial completeness (all models x scenarios x runs present)
    expected_models = set(worker_df["model"].unique())
    expected_scenarios = set(worker_df["scenario_id"].unique())
    for model in expected_models:
        model_scenarios = set(worker_df[worker_df["model"] == model]["scenario_id"].unique())
        missing = expected_scenarios - model_scenarios
        if missing:
            issues.append(f"Model {model} missing scenarios: {missing}")
            print(f"  WARNING: {model} missing {len(missing)} scenarios")

    # 7. Check turn completeness (each trial should have 5 turns)
    turns_per_trial = worker_df.groupby("trial_id")["turn"].max()
    incomplete = (turns_per_trial < 5).sum()
    if incomplete > 0:
        print(f"  Incomplete trials (<5 turns): {incomplete}")
        issues.append(f"{incomplete} trials have fewer than 5 turns")

    status = "PASS" if not issues else f"FAIL ({len(issues)} issues)"
    print(f"\n  Validation: {status}")
    if issues:
        for issue in issues[:10]:
            print(f"    - {issue}")

    return {
        "status": status,
        "none_responses": none_responses,
        "truncated_responses": truncated,
        "null_token_rows": int(null_tokens),
        "evaluator_coverage": float(coverage),
        "null_levels": int(null_levels),
        "incomplete_trials": int(incomplete),
        "issues": issues,
    }


# ── Structural Bloat Detection ──

def structural_bloat_analysis() -> dict:
    """Track structural elements (headers, bullets, code blocks) across turns.

    If models add more structural formatting over revisions, it's a sign of
    performative complexity -- making output look more thorough without
    substantive improvement.
    """
    print("\n== Structural Bloat Analysis ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    rows = []
    for trial in successful:
        for turn_idx, response in enumerate(trial["responses"]):
            if response is None:
                continue
            headers = len(re.findall(r'^#{1,6}\s', response, re.MULTILINE))
            bullets = len(re.findall(r'^[\s]*[-*]\s', response, re.MULTILINE))
            numbered = len(re.findall(r'^[\s]*\d+[.)]\s', response, re.MULTILINE))
            code_blocks = len(re.findall(r'```', response)) // 2
            bold = len(re.findall(r'\*\*[^*]+\*\*', response))
            paragraphs = len([p for p in response.split('\n\n') if p.strip()])

            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": turn_idx + 1,
                "headers": headers,
                "bullets": bullets,
                "numbered_items": numbered,
                "code_blocks": code_blocks,
                "bold_phrases": bold,
                "paragraphs": paragraphs,
                "total_structure": headers + bullets + numbered + code_blocks,
            })

    df = pd.DataFrame(rows)
    if df.empty:
        print("  No data.")
        return {}

    by_turn = df.groupby("turn")[["headers", "bullets", "numbered_items",
                                    "code_blocks", "bold_phrases", "total_structure"]].mean()
    print("\nTurn | Headers | Bullets | Numbered | Code blocks | Bold | Total structure")
    print("-" * 80)
    for turn, row in by_turn.iterrows():
        print(f"  {turn}   | {row['headers']:.1f}     | {row['bullets']:.1f}     | "
              f"{row['numbered_items']:.1f}        | {row['code_blocks']:.1f}          | "
              f"{row['bold_phrases']:.1f}   | {row['total_structure']:.1f}")

    rho, p = sp_stats.spearmanr(df["turn"], df["total_structure"])
    print(f"\n  Spearman (turn vs total structure): rho={rho:.3f}, p={p:.4f}")
    print(f"  {'Structure increases over turns' if rho > 0 else 'Structure stable or decreasing'}")

    by_model = {}
    for model in sorted(df["model"].unique()):
        m_df = df[df["model"] == model]
        t1 = m_df[m_df["turn"] == 1]["total_structure"].mean()
        t5 = m_df[m_df["turn"] == 5]["total_structure"].mean() if 5 in m_df["turn"].values else t1
        by_model[model] = {"t1_structure": float(t1), "t5_structure": float(t5),
                           "growth": float(t5 - t1)}
    print("\n  Structural growth T1->T5 by model:")
    for model, data in sorted(by_model.items()):
        print(f"    {model}: {data['t1_structure']:.1f} -> {data['t5_structure']:.1f} ({data['growth']:+.1f})")

    return {
        "by_turn": {int(t): {c: float(v) for c, v in row.items()} for t, row in by_turn.iterrows()},
        "correlation": {"rho": float(rho), "p": float(p)},
        "by_model": by_model,
    }


# ── Semantic Similarity Between Consecutive Turns ──

def _tfidf_cosine(text_a: str, text_b: str) -> float:
    """Compute TF-IDF cosine similarity between two texts (no external deps)."""
    words_a = re.findall(r'\b\w+\b', text_a.lower())
    words_b = re.findall(r'\b\w+\b', text_b.lower())
    if not words_a or not words_b:
        return 0.0

    vocab = set(words_a) | set(words_b)
    # Term frequency
    tf_a = defaultdict(int)
    tf_b = defaultdict(int)
    for w in words_a:
        tf_a[w] += 1
    for w in words_b:
        tf_b[w] += 1

    # IDF (2 documents)
    idf = {}
    for w in vocab:
        doc_freq = (1 if tf_a[w] > 0 else 0) + (1 if tf_b[w] > 0 else 0)
        idf[w] = math.log(2.0 / doc_freq) + 1

    # TF-IDF vectors
    dot = 0.0
    norm_a = 0.0
    norm_b = 0.0
    for w in vocab:
        va = tf_a[w] * idf[w]
        vb = tf_b[w] * idf[w]
        dot += va * vb
        norm_a += va * va
        norm_b += vb * vb

    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (math.sqrt(norm_a) * math.sqrt(norm_b))


def semantic_similarity_analysis() -> dict:
    """Measure semantic similarity between consecutive turns.

    High similarity + low quality gain = model is paraphrasing, not improving.
    Declining similarity over turns = semantic drift from the original.
    """
    print("\n== Semantic Similarity Between Consecutive Turns ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    rows = []
    for trial in successful:
        resps = trial["responses"]
        for i in range(1, len(resps)):
            if resps[i] is None or resps[i-1] is None:
                continue
            sim = _tfidf_cosine(resps[i-1], resps[i])
            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": i + 1,
                "cosine_sim": sim,
            })
        # Also track T1 vs each later turn (drift from original)
        if resps[0] is not None:
            for i in range(1, len(resps)):
                if resps[i] is None:
                    continue
                sim = _tfidf_cosine(resps[0], resps[i])
                rows.append({
                    "trial_id": trial["trial_id"],
                    "model": trial["model"],
                    "domain": trial["domain"],
                    "turn": -(i + 1),  # Negative turn = vs T1
                    "cosine_sim": sim,
                })

    df = pd.DataFrame(rows)
    if df.empty:
        print("  No data.")
        return {}

    # Consecutive similarity
    consecutive = df[df["turn"] > 0]
    by_turn = consecutive.groupby("turn")["cosine_sim"].mean()
    print("\nConsecutive turn similarity:")
    for turn, sim in by_turn.items():
        print(f"  T{int(turn)-1}->T{int(turn)}: {sim:.3f}")

    # Drift from T1
    drift = df[df["turn"] < 0].copy()
    drift["turn"] = drift["turn"].abs()
    drift_by_turn = drift.groupby("turn")["cosine_sim"].mean()
    print("\nSimilarity to original (T1):")
    for turn, sim in drift_by_turn.items():
        print(f"  T1 vs T{int(turn)}: {sim:.3f}")

    rho, p = sp_stats.spearmanr(drift["turn"], drift["cosine_sim"])
    print(f"\n  Spearman (turn vs T1-similarity): rho={rho:.3f}, p={p:.4f}")
    print(f"  {'Drifting from original' if rho < 0 else 'Staying close to original'}")

    return {
        "consecutive_similarity": {int(t): float(v) for t, v in by_turn.items()},
        "drift_from_t1": {int(t): float(v) for t, v in drift_by_turn.items()},
        "drift_correlation": {"rho": float(rho), "p": float(p)},
    }


# ── Position Bias Check (Reversibility) ──

def position_bias_check() -> dict:
    """Verify A/B randomization in reversibility test and check for position bias."""
    print("\n== Position Bias Check (Reversibility) ==")
    results = load_jsonl(S3_REVERSIBILITY_RESULTS_PATH)
    if not results:
        print("  No reversibility data.")
        return {}

    valid = [r for r in results if r.get("raw_choice") in ("A", "B")]
    if not valid:
        print("  No valid A/B choices.")
        return {}

    # Check randomization balance
    t1_as_a = sum(1 for r in valid if r.get("turn1_position") == "A")
    t1_as_b = sum(1 for r in valid if r.get("turn1_position") == "B")
    total = len(valid)
    print(f"  Turn 1 in position A: {t1_as_a}/{total} ({t1_as_a/total:.1%})")
    print(f"  Turn 1 in position B: {t1_as_b}/{total} ({t1_as_b/total:.1%})")

    # Position bias: how often does model choose A regardless of content?
    chose_a = sum(1 for r in valid if r["raw_choice"] == "A")
    chose_b = sum(1 for r in valid if r["raw_choice"] == "B")
    a_rate = chose_a / total
    print(f"\n  Chose A: {chose_a}/{total} ({a_rate:.1%})")
    print(f"  Chose B: {chose_b}/{total} ({1-a_rate:.1%})")

    # Binomial test for position bias (should be ~50% if no bias)
    binom_p = float(sp_stats.binomtest(chose_a, total, 0.5).pvalue)
    print(f"  Binomial test for position bias: p={binom_p:.4f}")
    if binom_p < 0.05:
        print(f"  WARNING: Significant position bias detected (p<0.05)")

    # Check if preference differs by position
    # When T1 is A, how often is A chosen? vs when T1 is B, how often is B chosen?
    t1_a_chose_a = sum(1 for r in valid if r.get("turn1_position") == "A" and r["raw_choice"] == "A")
    t1_b_chose_b = sum(1 for r in valid if r.get("turn1_position") == "B" and r["raw_choice"] == "B")
    t1_pref_when_a = t1_a_chose_a / t1_as_a if t1_as_a > 0 else 0
    t1_pref_when_b = t1_b_chose_b / t1_as_b if t1_as_b > 0 else 0
    print(f"\n  T1 preference when T1 is in position A: {t1_pref_when_a:.1%}")
    print(f"  T1 preference when T1 is in position B: {t1_pref_when_b:.1%}")
    consistency_gap = abs(t1_pref_when_a - t1_pref_when_b)
    print(f"  Consistency gap: {consistency_gap:.1%} {'(OK)' if consistency_gap < 0.15 else '(WARNING: position may confound results)'}")

    return {
        "randomization_balance": {"t1_as_a": t1_as_a, "t1_as_b": t1_as_b},
        "position_bias": {"chose_a_rate": float(a_rate), "binom_p": binom_p},
        "consistency": {
            "t1_pref_when_a": float(t1_pref_when_a),
            "t1_pref_when_b": float(t1_pref_when_b),
            "gap": float(consistency_gap),
        },
    }


# ── Revision Efficiency (tokens spent vs content actually changed) ──

def compute_edit_distance_ratio(prev: str, curr: str) -> float:
    """Compute normalized edit distance between two strings (word-level).

    Returns ratio of changed words to total words. 0 = identical, 1 = completely different.
    """
    prev_words = prev.split()
    curr_words = curr.split()
    if not prev_words and not curr_words:
        return 0.0
    # Use simple set-based approximation for speed (exact Levenshtein is O(n*m))
    prev_set = set(enumerate(prev_words))
    curr_set = set(enumerate(curr_words))
    # Count words that changed position or content
    max_len = max(len(prev_words), len(curr_words))
    if max_len == 0:
        return 0.0
    matching = sum(1 for i, w in enumerate(prev_words)
                   if i < len(curr_words) and curr_words[i] == w)
    return 1.0 - (matching / max_len)


def revision_efficiency_analysis(worker_df: pd.DataFrame) -> dict:
    """Measure how much content actually changes per revision vs tokens spent.

    Tokens-per-change ratio: high = model regenerates everything to change little.
    """
    print("\n== Revision Efficiency (Tokens Spent vs Content Changed) ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    rows = []
    for trial in successful:
        for turn_idx in range(1, len(trial["responses"])):
            prev = trial["responses"][turn_idx - 1]
            curr = trial["responses"][turn_idx]
            if curr is None or not classify_revision(curr):
                continue

            edit_ratio = compute_edit_distance_ratio(prev, curr)
            token_info = trial["token_counts"][turn_idx] if trial.get("token_counts") else {}
            output_tokens = (token_info.get("output", 0) or 0)

            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": turn_idx + 1,
                "edit_ratio": edit_ratio,
                "output_tokens": output_tokens,
                "tokens_per_change": output_tokens / max(edit_ratio, 0.01),
            })

    if not rows:
        print("  No revision data.")
        return {}

    df = pd.DataFrame(rows)
    mean_edit = df["edit_ratio"].mean()
    mean_tpc = df["tokens_per_change"].mean()

    print(f"  Total revisions analyzed: {len(df)}")
    print(f"  Mean edit ratio: {mean_edit:.3f} (0=identical, 1=completely rewritten)")
    print(f"  Mean tokens per unit change: {mean_tpc:.0f}")

    by_turn = df.groupby("turn").agg({"edit_ratio": "mean", "output_tokens": "mean", "tokens_per_change": "mean"})
    print("\nTurn | Edit ratio | Output tokens | Tokens/change")
    print("-" * 55)
    for turn, row in by_turn.iterrows():
        print(f"  {turn}   | {row['edit_ratio']:.3f}      | {row['output_tokens']:.0f}          | {row['tokens_per_change']:.0f}")

    by_model = {}
    print("\n  By model:")
    for model in sorted(df["model"].unique()):
        m_df = df[df["model"] == model]
        by_model[model] = {
            "mean_edit_ratio": float(m_df["edit_ratio"].mean()),
            "mean_tokens_per_change": float(m_df["tokens_per_change"].mean()),
        }
        print(f"    {model}: edit_ratio={m_df['edit_ratio'].mean():.3f}, tokens/change={m_df['tokens_per_change'].mean():.0f}")

    by_domain = {}
    print("\n  By domain:")
    for domain in sorted(df["domain"].unique()):
        d_df = df[df["domain"] == domain]
        by_domain[domain] = {
            "mean_edit_ratio": float(d_df["edit_ratio"].mean()),
            "mean_tokens_per_change": float(d_df["tokens_per_change"].mean()),
        }
        print(f"    {domain}: edit_ratio={d_df['edit_ratio'].mean():.3f}, tokens/change={d_df['tokens_per_change'].mean():.0f}")

    return {
        "mean_edit_ratio": float(mean_edit),
        "mean_tokens_per_change": float(mean_tpc),
        "n_revisions": len(df),
        "by_turn": {int(t): {"edit_ratio": float(r["edit_ratio"]), "tokens_per_change": float(r["tokens_per_change"])}
                    for t, r in by_turn.iterrows()},
        "by_model": by_model,
        "by_domain": by_domain,
    }


# ── Wavering Score (Zhang et al., ACL 2025) ──

def compute_wavering_score(quality_trajectory: list[float]) -> int:
    """Count direction changes in quality trajectory.

    A wavering event occurs when consecutive quality deltas change sign,
    indicating the model flip-flopped between improving and degrading.
    Inspired by Zhang et al. (ACL 2025) on answer wavering in self-correction.
    """
    if len(quality_trajectory) < 3:
        return 0
    deltas = [quality_trajectory[i] - quality_trajectory[i-1]
              for i in range(1, len(quality_trajectory))]
    sign_changes = 0
    for i in range(1, len(deltas)):
        if deltas[i] * deltas[i-1] < 0:
            sign_changes += 1
    return sign_changes


def wavering_analysis(eval_df: pd.DataFrame) -> dict:
    """Compute wavering scores across trials, models, and domains."""
    print("\n== Wavering Analysis (Quality Trajectory Instability) ==")

    trial_trajectories = {}
    for _, row in eval_df.iterrows():
        key = row["worker_trial_id"]
        if key not in trial_trajectories:
            trial_trajectories[key] = {"levels": {}, "model": row["model"], "domain": row["domain"]}
        trial_trajectories[key]["levels"][row["turn"]] = row["level"]

    scores = []
    for trial_id, data in trial_trajectories.items():
        turns = sorted(data["levels"].keys())
        if len(turns) < 3:
            continue
        trajectory = [data["levels"][t] for t in turns]
        ws = compute_wavering_score(trajectory)
        scores.append({
            "trial_id": trial_id,
            "model": data["model"],
            "domain": data["domain"],
            "wavering_score": ws,
            "trajectory": trajectory,
        })

    if not scores:
        print("  No data with 3+ turns.")
        return {}

    ws_df = pd.DataFrame(scores)
    mean_ws = ws_df["wavering_score"].mean()
    wavering_trials = (ws_df["wavering_score"] > 0).sum()
    total = len(ws_df)

    print(f"  Trials analyzed: {total}")
    print(f"  Mean wavering score: {mean_ws:.2f}")
    print(f"  Trials with any wavering: {wavering_trials}/{total} ({wavering_trials/total:.1%})")

    by_model = {}
    print("\n  By model:")
    for model in sorted(ws_df["model"].unique()):
        m_df = ws_df[ws_df["model"] == model]
        m_mean = m_df["wavering_score"].mean()
        by_model[model] = float(m_mean)
        print(f"    {model}: mean={m_mean:.2f}, any_wavering={int((m_df['wavering_score'] > 0).sum())}/{len(m_df)}")

    by_domain = {}
    print("\n  By domain:")
    for domain in sorted(ws_df["domain"].unique()):
        d_df = ws_df[ws_df["domain"] == domain]
        d_mean = d_df["wavering_score"].mean()
        by_domain[domain] = float(d_mean)
        print(f"    {domain}: mean={d_mean:.2f}")

    return {
        "mean_wavering_score": float(mean_ws),
        "wavering_trial_rate": float(wavering_trials / total),
        "n_trials": total,
        "by_model": by_model,
        "by_domain": by_domain,
    }


# ── Constraint Satisfaction (Laban et al., 2025 inspired) ──

def constraint_satisfaction_analysis(eval_df: pd.DataFrame) -> dict:
    """Check if task constraints are maintained across turns.

    Uses keyword overlap between the task prompt and each response as a proxy
    for whether the model is losing track of original requirements over turns.
    Inspired by Laban et al. (2025) on multi-turn context loss.
    """
    print("\n== Constraint Satisfaction (Context Retention) ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    rows = []
    for trial in successful:
        task_words = set(re.findall(r'\b\w{4,}\b', trial["task_prompt"].lower()))
        if not task_words:
            continue
        for turn_idx, response in enumerate(trial["responses"]):
            resp_words = set(re.findall(r'\b\w{4,}\b', response.lower()))
            recall = len(task_words & resp_words) / len(task_words)
            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": turn_idx + 1,
                "constraint_recall": recall,
            })

    df = pd.DataFrame(rows)
    if df.empty:
        print("  No data.")
        return {}

    by_turn = df.groupby("turn")["constraint_recall"].mean()
    print("\nTurn | Mean constraint recall")
    print("-" * 35)
    for turn, recall in by_turn.items():
        print(f"  {turn}   | {recall:.3f}")

    # Test for decline
    rho, p = sp_stats.spearmanr(df["turn"], df["constraint_recall"])
    print(f"\n  Spearman (turn vs recall): rho={rho:.3f}, p={p:.4f}")

    # Per-trial: flag trials where recall drops by >10% from T1 to T5
    t1_recall = df[df["turn"] == 1].set_index("trial_id")["constraint_recall"]
    t5_recall = df[df["turn"] == 5].set_index("trial_id")["constraint_recall"] if 5 in df["turn"].values else pd.Series(dtype=float)
    shared = sorted(set(t1_recall.index) & set(t5_recall.index))
    if shared:
        drops = [(t1_recall[tid] - t5_recall[tid]) for tid in shared]
        significant_drops = sum(1 for d in drops if d > 0.10)
        print(f"\n  Trials with >10% recall drop T1->T5: {significant_drops}/{len(shared)} ({significant_drops/len(shared):.1%})")
    else:
        significant_drops = 0

    return {
        "recall_by_turn": {int(k): float(v) for k, v in by_turn.items()},
        "correlation": {"rho": float(rho), "p": float(p)},
        "significant_drop_rate": float(significant_drops / len(shared)) if shared else 0.0,
    }


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

    # Data integrity check (run first, before any analysis)
    results["validation"] = validate_data_integrity(worker_df, eval_df)

    results["rq1"] = rq1_revision_yield_curve(worker_df, eval_df)
    results["rq2"] = rq2_drp_by_domain(eval_df)
    results["rq3"] = rq3_overcorrection_rate(worker_df, eval_df)
    results["rq4"] = rq4_compliance_mechanism(worker_df, eval_df)
    results["rq5"] = rq5_token_cost(worker_df, eval_df)
    results["rq6"] = rq6_stylistic_drift(worker_df)
    results["rq7"] = rq7_targeted_feedback()
    results["rq8"] = rq8_cross_model(worker_df, eval_df)
    results["rq9"] = rq9_oneshot_ceiling(eval_df)
    results["rq10"] = rq10_reversibility()
    results["rq11"] = rq11_convergence()
    results["rq12"] = rq12_instruction_adherence(worker_df)
    results["rq13"] = rq13_performative_revision()
    results["rq14"] = rq14_self_reflection()
    results["rq15"] = rq15_revision_yield_equations(eval_df, worker_df)
    results["rq16"] = rq16_unit_economics(eval_df, worker_df)
    results["rq17"] = rq17_overcorrection_magnitude(eval_df, worker_df)
    results["revision_efficiency"] = revision_efficiency_analysis(worker_df)
    results["structural_bloat"] = structural_bloat_analysis()
    results["semantic_similarity"] = semantic_similarity_analysis()
    results["wavering"] = wavering_analysis(eval_df)
    results["constraint_satisfaction"] = constraint_satisfaction_analysis(eval_df)
    results["position_bias"] = position_bias_check()

    results_path = S3_STATS_DIR / "study3_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved all results to {results_path}")
    print("Done.")


if __name__ == "__main__":
    main()
