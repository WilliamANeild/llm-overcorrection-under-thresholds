"""Analyze Study 3 (Revision Yield) results across all research questions.

RQ1:  Revision Yield Curve (quality trajectory by turn)
RQ2:  Diminishing Return Point by domain
RQ3:  Do models respect the DRP?
RQ4:  Revision-despite-sufficiency (quality-blind revision behavior)
RQ5:  Token cost of zero-value revisions
RQ6:  Stylistic drift and bloat over turns
RQ7:  Targeted feedback vs generic prompting
RQ8:  Cross-model patterns (do all 6 models show overcorrection?)
RQ9:  One-shot ceiling vs iterative
RQ10: Reversibility test (does model prefer its first draft?)
RQ12: Instruction adherence decay
RQ14: Can the model spot its own overcorrection? (self-reflection)
RQ15: Revision Yield equation and optimal stopping turn (CARY, per-model)
RQ16: Unit economics (practical cost at budget tiers)
RQ17: Overcorrection magnitude (continuous OCS, t_done >= T2)

Dropped:
  RQ11: Cross-model convergence (char-length CV is not semantic convergence)
  RQ13: Performative revision (word-list detector produces degenerate 0.3% rate)

Analysis splits:
  Quality-estimand RQs (1,2,5,7,8-quality,9,15,17,wavering): revision-only data
  Experience-estimand RQs (3,4,6-rate,8-decline,10,16): full-conversation data
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
    """Returns True if the response is a revision, False if it declines.

    Only checks for decline phrases in the first 300 characters to avoid
    false positives where a model says "this is already good" then proceeds
    to revise anyway (common pattern in long responses).
    """
    if not response or len(response.strip()) < 5:
        return False

    # Strong decline phrases: if these appear anywhere in a short response,
    # or in the first 300 chars of any response, it's a decline.
    strong_decline = [
        "keep this as my final", "this is my final version",
        "i'd like to keep this", "i would like to keep this",
        "keep this as the final", "i'll keep this", "i will keep this",
        "happy with this version", "this version is ready",
        "no changes needed", "no improvements needed",
        "no further changes", "no further improvements",
        "no revisions needed", "nothing to improve",
        "nothing i would change", "i wouldn't change",
        "i don't think any changes", "don't see any need",
    ]

    # Weak decline phrases: only count these if the response is short (<500 chars),
    # because long responses that start with "looks good" often continue with revisions.
    weak_decline = [
        "looks good as is", "looks good as-is", "looks good",
        "already well", "already good", "ready to use",
        "ready as is", "ready as-is", "satisfied with",
        "meets the requirements", "the output is complete",
        "this is complete", "complete as is", "is ready",
        "is done", "i agree", "well done", "no need",
        "i think it's good", "i think this is good",
        "i think it looks good", "no, i think",
        "i'm satisfied", "final version", "no changes",
    ]

    # Check first 300 chars for strong phrases
    head = response[:300].lower()
    for phrase in strong_decline:
        if phrase in head:
            return False

    # Weak phrases only trigger on short responses
    if len(response) < 500:
        response_lower = response.lower()
        for phrase in weak_decline:
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
    """Load evaluator results with 6->2 recode (level 6 'Overdone' -> 2)."""
    results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
    valid = [r for r in results if r.get("level") is not None]
    df = pd.DataFrame(valid)
    df.loc[df["level"] == 6, "level"] = 2
    return df


def _build_revision_flags() -> dict[tuple[str, int], bool]:
    """Build a lookup of (trial_id, turn) -> is_revision for all worker trials."""
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    flags = {}
    for trial in [t for t in trials if t.get("status") == "success"]:
        for turn_idx, response in enumerate(trial["responses"]):
            turn = turn_idx + 1
            flags[(trial["trial_id"], turn)] = True if turn == 1 else classify_revision(response)
    return flags


def get_revision_only_eval(eval_df: pd.DataFrame) -> pd.DataFrame:
    """Filter eval_df to only include turns where the model produced actual content.

    Meta-responses (decline-to-revise) are excluded from the graded population
    entirely, matching the human evaluation protocol where they receive N/A
    rather than a quality score.
    """
    flags = _build_revision_flags()
    df = eval_df.copy()
    df["is_revision"] = df.apply(
        lambda r: flags.get((r["worker_trial_id"], r["turn"]), True), axis=1
    )
    return df[df["is_revision"]].drop(columns=["is_revision"])


# ── Edge Case Framework ──
# Every aggregate statistic is decomposed to catch compositional artifacts,
# sign-flip masking, and survivorship-driven results.

MIN_CELL_SIZE = 10  # Minimum n for reporting per-cell statistics


def _build_eval_map() -> dict[tuple[str, int], float]:
    """Build (trial_id, turn) -> level lookup from evaluator data."""
    results = load_jsonl(S3_EVALUATOR_RESULTS_PATH)
    return {(r["worker_trial_id"], r["turn"]): r["level"]
            for r in results if r.get("level") is not None}


def _build_trial_metadata() -> dict[str, dict]:
    """Build trial_id -> {model, domain, t1_quality, survival_depth, t1_stratum} lookup."""
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    eval_map = _build_eval_map()
    rev_flags = _build_revision_flags()
    meta = {}
    for trial in [t for t in trials if t.get("status") == "success"]:
        tid = trial["trial_id"]
        t1_q = eval_map.get((tid, 1))
        # Survival depth = last turn where the model actually revised
        depth = 1
        for t in range(2, 6):
            if rev_flags.get((tid, t), False):
                depth = t
            else:
                break
        meta[tid] = {
            "model": trial["model"],
            "domain": trial["domain"],
            "t1_quality": t1_q,
            "t1_stratum": "needs_work" if (t1_q is not None and t1_q < 4) else "already_good",
            "survival_depth": depth,
            "full_survivor": depth >= 5,
        }
    return meta


def cohort_locked_trajectories(eval_df: pd.DataFrame, trial_meta: dict) -> dict:
    """Compute quality trajectories locked to specific cohorts.

    Returns trajectories for:
    - full_panel: all 720 trials (using all-responses eval)
    - balanced: only trials that revised at all 5 turns
    - t2_cohort through t5_cohort: trials surviving to at least turn N
    - needs_work: T1 < 4 stratum (trials where revision was plausibly warranted)
    - already_good: T1 >= 4 stratum
    - per_model: cohort-locked per model
    """
    rev_flags = _build_revision_flags()

    # Build per-trial trajectory
    trial_levels = defaultdict(dict)
    trial_rev_levels = defaultdict(dict)
    for _, row in eval_df.iterrows():
        tid = row["worker_trial_id"]
        t = row["turn"]
        trial_levels[tid][t] = row["level"]
        is_rev = rev_flags.get((tid, t), True)
        if is_rev:
            trial_rev_levels[tid][t] = row["level"]

    def _cohort_trajectory(trial_ids: set, use_rev_only: bool = True) -> dict:
        """Mean quality at each turn for a fixed set of trials."""
        source = trial_rev_levels if use_rev_only else trial_levels
        by_turn = defaultdict(list)
        for tid in trial_ids:
            for t, level in source.get(tid, {}).items():
                by_turn[t].append(level)
        return {int(t): {"mean": float(np.mean(vs)), "n": len(vs)}
                for t, vs in sorted(by_turn.items()) if vs}

    all_tids = set(trial_meta.keys())

    # Cohort-locked: trials surviving to at least turn N
    cohort_results = {}
    for max_turn in range(2, 6):
        cohort_ids = {tid for tid, m in trial_meta.items() if m["survival_depth"] >= max_turn}
        traj = _cohort_trajectory(cohort_ids)
        cohort_results[f"t{max_turn}_cohort"] = {
            "n_trials": len(cohort_ids),
            "trajectory": traj,
        }

    # Balanced panel (all 5 turns revised)
    balanced_ids = {tid for tid, m in trial_meta.items() if m["full_survivor"]}
    cohort_results["balanced"] = {
        "n_trials": len(balanced_ids),
        "trajectory": _cohort_trajectory(balanced_ids),
    }

    # T1 quality strata
    for stratum in ["needs_work", "already_good"]:
        s_ids = {tid for tid, m in trial_meta.items() if m["t1_stratum"] == stratum}
        if len(s_ids) >= MIN_CELL_SIZE:
            cohort_results[stratum] = {
                "n_trials": len(s_ids),
                "trajectory": _cohort_trajectory(s_ids),
            }
            # Also balanced panel within stratum
            s_balanced = s_ids & balanced_ids
            if len(s_balanced) >= MIN_CELL_SIZE:
                cohort_results[f"{stratum}_balanced"] = {
                    "n_trials": len(s_balanced),
                    "trajectory": _cohort_trajectory(s_balanced),
                }

    # Per-model balanced panel
    per_model = {}
    models = sorted(set(m["model"] for m in trial_meta.values()))
    for model in models:
        m_balanced = {tid for tid, m in trial_meta.items()
                      if m["model"] == model and m["full_survivor"]}
        m_all = {tid for tid, m in trial_meta.items() if m["model"] == model}
        traj = _cohort_trajectory(m_balanced) if len(m_balanced) >= 2 else {}
        # Per-trial delta for this model's survivors
        deltas = []
        for tid in m_balanced:
            t1_q = trial_rev_levels.get(tid, {}).get(1)
            t5_q = trial_rev_levels.get(tid, {}).get(5)
            if t1_q is not None and t5_q is not None:
                deltas.append(t5_q - t1_q)
        per_model[model] = {
            "n_balanced": len(m_balanced),
            "n_total": len(m_all),
            "survival_rate": len(m_balanced) / len(m_all) if m_all else 0,
            "trajectory": traj,
            "mean_delta_t1_t5": float(np.mean(deltas)) if deltas else None,
            "pct_improved": float(sum(1 for d in deltas if d > 0) / len(deltas)) if deltas else None,
            "pct_degraded": float(sum(1 for d in deltas if d < 0) / len(deltas)) if deltas else None,
        }

    cohort_results["per_model"] = per_model
    return cohort_results


def compositional_audit(eval_df: pd.DataFrame, trial_meta: dict) -> dict:
    """Check whether the model/quality composition of the revision-only pool
    shifts across turns in ways that could drive aggregate results."""
    rev_flags = _build_revision_flags()
    warnings = []

    # Model composition at each turn in revision-only pool
    model_comp = {}
    for turn in range(1, 6):
        turn_tids = set()
        for _, row in eval_df.iterrows():
            tid = row["worker_trial_id"]
            t = row["turn"]
            if t == turn and rev_flags.get((tid, t), True):
                turn_tids.add(tid)
        model_counts = defaultdict(int)
        for tid in turn_tids:
            if tid in trial_meta:
                model_counts[trial_meta[tid]["model"]] += 1
        total = sum(model_counts.values())
        model_comp[turn] = {m: c / total if total > 0 else 0 for m, c in model_counts.items()}

    # Check for large compositional shifts between T1 and T5
    if 1 in model_comp and 5 in model_comp:
        for model in model_comp[1]:
            t1_share = model_comp[1].get(model, 0)
            t5_share = model_comp[5].get(model, 0)
            shift = t5_share - t1_share
            if abs(shift) > 0.05:
                warnings.append(f"{model}: {t1_share:.1%} at T1 -> {t5_share:.1%} at T5 (shift={shift:+.1%})")

    # T1 quality composition shift
    stratum_comp = {}
    for turn in range(1, 6):
        turn_tids = set()
        for _, row in eval_df.iterrows():
            tid = row["worker_trial_id"]
            t = row["turn"]
            if t == turn and rev_flags.get((tid, t), True):
                turn_tids.add(tid)
        nw = sum(1 for tid in turn_tids if trial_meta.get(tid, {}).get("t1_stratum") == "needs_work")
        total = len(turn_tids)
        stratum_comp[turn] = nw / total if total > 0 else 0

    # Sign-flip check: does aggregate direction match majority of per-model directions?
    rev_eval = get_revision_only_eval(eval_df)
    models = sorted(rev_eval["model"].unique())
    model_directions = {}
    for model in models:
        m_eval = rev_eval[rev_eval["model"] == model]
        m_level = m_eval.groupby("turn")["level"].mean()
        if 1 in m_level.index and len(m_level) >= 2:
            last_turn = max(m_level.index)
            delta = m_level[last_turn] - m_level[1]
            model_directions[model] = "improves" if delta > 0 else "degrades"

    n_improve = sum(1 for d in model_directions.values() if d == "improves")
    n_degrade = sum(1 for d in model_directions.values() if d == "degrades")
    if n_improve > 0 and n_degrade > 0:
        warnings.append(f"Sign flip: {n_improve} models improve, {n_degrade} degrade. Aggregate masks opposing effects.")

    # Dropout quality differential
    eval_map = _build_eval_map()
    dropout_t1 = []
    survivor_t1 = []
    for tid, m in trial_meta.items():
        t1_q = m.get("t1_quality")
        if t1_q is None:
            continue
        if m["survival_depth"] >= 2:
            survivor_t1.append(t1_q)
        else:
            dropout_t1.append(t1_q)
    if dropout_t1 and survivor_t1:
        diff = np.mean(dropout_t1) - np.mean(survivor_t1)
        if abs(diff) > 0.1:
            warnings.append(f"T2 dropout quality bias: dropouts T1={np.mean(dropout_t1):.2f}, survivors T1={np.mean(survivor_t1):.2f} (diff={diff:+.2f})")

    return {
        "model_composition_by_turn": {int(t): comp for t, comp in model_comp.items()},
        "needs_work_share_by_turn": {int(t): float(v) for t, v in stratum_comp.items()},
        "model_directions": model_directions,
        "warnings": warnings,
    }


def edge_case_framework(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    """Master edge case analysis that decomposes aggregates and flags artifacts.

    This runs as a standalone analysis block and provides the ground truth
    for interpreting all quality-trajectory RQs.
    """
    print("\n== Edge Case Framework ==")

    trial_meta = _build_trial_metadata()
    total = len(trial_meta)
    nw_count = sum(1 for m in trial_meta.values() if m["t1_stratum"] == "needs_work")
    ag_count = total - nw_count

    print(f"\n  T1 quality strata: needs_work (T1<4) = {nw_count}/{total} ({nw_count/total:.1%}), "
          f"already_good (T1>=4) = {ag_count}/{total} ({ag_count/total:.1%})")

    # 1. Cohort-locked trajectories
    print("\n--- Cohort-locked trajectories ---")
    cohorts = cohort_locked_trajectories(eval_df, trial_meta)

    for label in ["t2_cohort", "t3_cohort", "t4_cohort", "t5_cohort", "balanced"]:
        c = cohorts.get(label, {})
        n = c.get("n_trials", 0)
        traj = c.get("trajectory", {})
        traj_str = " -> ".join([f"T{t}:{d['mean']:.2f}" for t, d in sorted(traj.items())])
        print(f"  {label} (n={n}): {traj_str}")

    # T1 strata
    for label in ["needs_work", "already_good", "needs_work_balanced", "already_good_balanced"]:
        c = cohorts.get(label, {})
        if c:
            n = c.get("n_trials", 0)
            traj = c.get("trajectory", {})
            traj_str = " -> ".join([f"T{t}:{d['mean']:.2f}" for t, d in sorted(traj.items())])
            print(f"  {label} (n={n}): {traj_str}")

    # Per-model cohort-locked
    print("\n--- Per-model balanced panel (cohort-locked T5 survivors) ---")
    pm = cohorts.get("per_model", {})
    for model in sorted(pm.keys()):
        m = pm[model]
        traj = m.get("trajectory", {})
        traj_str = " -> ".join([f"T{t}:{d['mean']:.2f}" for t, d in sorted(traj.items())])
        delta = m.get("mean_delta_t1_t5")
        pct_imp = m.get("pct_improved")
        pct_deg = m.get("pct_degraded")
        surv = m.get("survival_rate", 0)
        print(f"  {model} (n={m['n_balanced']}/{m['n_total']}, surv={surv:.0%}): {traj_str}")
        if delta is not None:
            print(f"    T1->T5 delta={delta:+.2f}, improved={pct_imp:.0%}, degraded={pct_deg:.0%}")

    # 2. Compositional audit
    print("\n--- Compositional audit ---")
    audit = compositional_audit(eval_df, trial_meta)

    # Model composition shift
    print("  Model share in revision-only pool:")
    comp = audit["model_composition_by_turn"]
    models = sorted(set(m for c in comp.values() for m in c))
    header = f"  {'Model':<22}" + " ".join([f"T{t:>5}" for t in sorted(comp.keys())])
    print(header)
    for model in models:
        shares = [f"{comp.get(t, {}).get(model, 0):5.1%}" for t in sorted(comp.keys())]
        print(f"  {model:<22}" + " ".join(shares))

    # Needs-work share
    nw_share = audit["needs_work_share_by_turn"]
    nw_str = ", ".join([f"T{t}:{v:.1%}" for t, v in sorted(nw_share.items())])
    print(f"\n  Needs-work (T1<4) share: {nw_str}")

    # Directions
    print(f"\n  Per-model direction: {audit['model_directions']}")

    # Warnings
    if audit["warnings"]:
        print(f"\n  WARNINGS ({len(audit['warnings'])}):")
        for w in audit["warnings"]:
            print(f"    - {w}")
    else:
        print("\n  No compositional warnings.")

    # 3. Per-trial delta distribution for T5 survivors
    print("\n--- T5 survivor per-trial quality change by T1 stratum ---")
    eval_map = _build_eval_map()
    for stratum_label, stratum_val in [("needs_work", "needs_work"), ("already_good", "already_good")]:
        deltas = []
        for tid, m in trial_meta.items():
            if m["t1_stratum"] != stratum_val or not m["full_survivor"]:
                continue
            t1_q = eval_map.get((tid, 1))
            t5_q = eval_map.get((tid, 5))
            if t1_q is not None and t5_q is not None:
                deltas.append(t5_q - t1_q)
        if deltas:
            improved = sum(1 for d in deltas if d > 0)
            degraded = sum(1 for d in deltas if d < 0)
            print(f"  {stratum_label} (n={len(deltas)}): mean delta={np.mean(deltas):+.2f}, "
                  f"improved={improved} ({improved/len(deltas):.0%}), "
                  f"degraded={degraded} ({degraded/len(deltas):.0%})")

    # 4. The "illusion of decline" test: is the revision-only T5 quality drop
    #    driven by compositional shift or genuine within-trial degradation?
    print("\n--- Illusion-of-decline test ---")
    # Compare pooled revision-only trajectory vs balanced panel trajectory
    rev_eval = get_revision_only_eval(eval_df)
    pooled = rev_eval.groupby("turn")["level"].mean()
    balanced_ids = {tid for tid, m in trial_meta.items() if m["full_survivor"]}
    balanced = rev_eval[rev_eval["worker_trial_id"].isin(balanced_ids)].groupby("turn")["level"].mean()

    print(f"  {'Turn':<6} {'Pooled rev-only':>16} {'Balanced panel':>16} {'Difference':>12}")
    for t in sorted(pooled.index):
        p_val = pooled[t]
        b_val = balanced.get(t, float("nan"))
        diff = p_val - b_val if not np.isnan(b_val) else float("nan")
        print(f"  T{t:<5} {p_val:>15.2f} {b_val:>15.2f} {diff:>+11.2f}")

    # If pooled drops faster than balanced, compositional shift is inflating the decline
    pooled_drop = float(pooled.get(1, 0) - pooled.get(5, 0))
    balanced_drop = float(balanced.get(1, 0) - balanced.get(5, 0))
    inflation = pooled_drop - balanced_drop
    print(f"\n  Pooled T1-T5 drop: {pooled_drop:.2f}")
    print(f"  Balanced T1-T5 drop: {balanced_drop:.2f}")
    print(f"  Compositional inflation: {inflation:.2f} ({inflation/pooled_drop:.0%} of pooled drop)" if pooled_drop > 0 else "")

    return {
        "trial_strata": {"needs_work": nw_count, "already_good": ag_count},
        "cohort_trajectories": cohorts,
        "compositional_audit": audit,
        "illusion_of_decline": {
            "pooled_drop": pooled_drop,
            "balanced_drop": balanced_drop,
            "compositional_inflation": inflation,
            "inflation_pct": float(inflation / pooled_drop) if pooled_drop > 0 else 0,
        },
    }


# ── RQ1: Revision Yield Curve ──

def rq1_revision_yield_curve(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ1: Revision Yield Curve ==")

    # All-responses curve (what users actually experience)
    level_by_turn = eval_df.groupby("turn")["level"].mean()
    turns = sorted(level_by_turn.index)

    # Quality deltas (raw, not token-normalized -- see RQ15 for proper MRY)
    quality_delta = {}
    for i in range(1, len(turns)):
        quality_delta[turns[i]] = float(level_by_turn[turns[i]] - level_by_turn[turns[i-1]])

    print(f"\nAll responses - mean level by turn: {dict(zip(turns, [f'{level_by_turn[t]:.2f}' for t in turns]))}")
    print(f"Quality delta by turn: {quality_delta}")

    # Revision-only curve (excludes decline-to-revise meta-responses)
    # Merge evaluator levels with worker revision classification
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    revision_flags = {}
    for trial in [t for t in trials if t.get("status") == "success"]:
        for turn_idx, response in enumerate(trial["responses"]):
            turn = turn_idx + 1
            is_rev = True if turn == 1 else classify_revision(response)
            revision_flags[(trial["trial_id"], turn)] = is_rev

    eval_with_rev = eval_df.copy()
    eval_with_rev["is_revision"] = eval_with_rev.apply(
        lambda r: revision_flags.get((r["worker_trial_id"], r["turn"]), True), axis=1
    )

    rev_only = eval_with_rev[eval_with_rev["is_revision"]]
    rev_level_by_turn = rev_only.groupby("turn")["level"].mean()
    rev_count_by_turn = rev_only.groupby("turn")["level"].count()
    declined_count = eval_with_rev[~eval_with_rev["is_revision"]].groupby("turn")["level"].count()

    rev_quality_delta = {}
    rev_turns = sorted(rev_level_by_turn.index)
    for i in range(1, len(rev_turns)):
        rev_quality_delta[rev_turns[i]] = float(rev_level_by_turn[rev_turns[i]] - rev_level_by_turn[rev_turns[i-1]])

    print(f"\nRevision-only - mean level by turn: {dict(zip(rev_turns, [f'{rev_level_by_turn[t]:.2f}' for t in rev_turns]))}")
    print(f"Revision-only quality delta: {rev_quality_delta}")
    print(f"\nTurn | All (n, mean) | Revised (n, mean) | Declined (n, mean)")
    print("-" * 70)
    for t in turns:
        all_n = len(eval_df[eval_df["turn"] == t])
        all_m = level_by_turn[t]
        rev_n = int(rev_count_by_turn.get(t, 0))
        rev_m = float(rev_level_by_turn.get(t, 0))
        dec_n = int(declined_count.get(t, 0))
        dec_levels = eval_with_rev[(~eval_with_rev["is_revision"]) & (eval_with_rev["turn"] == t)]["level"]
        dec_m = float(dec_levels.mean()) if len(dec_levels) > 0 else 0
        print(f"  {t}   | {all_n:3d}, {all_m:.2f}    | {rev_n:3d}, {rev_m:.2f}      | {dec_n:3d}, {dec_m:.2f}")

    # Decline rate by turn
    decline_rate = {}
    for t in turns:
        total = len(eval_df[eval_df["turn"] == t])
        declined = int(declined_count.get(t, 0))
        decline_rate[int(t)] = float(declined / total) if total > 0 else 0
    print(f"\nDecline rate by turn: {decline_rate}")

    return {
        "level_by_turn": {int(t): float(level_by_turn[t]) for t in turns},
        "quality_delta": quality_delta,
        "revision_only_level_by_turn": {int(t): float(rev_level_by_turn[t]) for t in rev_turns},
        "revision_only_quality_delta": rev_quality_delta,
        "revision_only_n_by_turn": {int(t): int(rev_count_by_turn.get(t, 0)) for t in turns},
        "decline_rate_by_turn": decline_rate,
    }


# ── RQ2: DRP by domain ──

def rq2_drp_by_domain(eval_df: pd.DataFrame) -> dict:
    print("\n== RQ2: Diminishing Return Point by Domain ==")

    # Build revision-only evaluator subset
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    revision_flags = {}
    for trial in [t for t in trials if t.get("status") == "success"]:
        for turn_idx, response in enumerate(trial["responses"]):
            turn = turn_idx + 1
            is_rev = True if turn == 1 else classify_revision(response)
            revision_flags[(trial["trial_id"], turn)] = is_rev

    eval_with_rev = eval_df.copy()
    eval_with_rev["is_revision"] = eval_with_rev.apply(
        lambda r: revision_flags.get((r["worker_trial_id"], r["turn"]), True), axis=1
    )
    rev_only = eval_with_rev[eval_with_rev["is_revision"]]

    results = {}
    for domain in sorted(eval_df["domain"].unique()):
        subset = eval_df[eval_df["domain"] == domain]
        level_by_turn = subset.groupby("turn")["level"].mean()
        turns = sorted(level_by_turn.index)

        # DRP = first turn >= 2 where MRY <= 0 (quality stops improving)
        drp = None
        for i in range(1, len(turns)):
            if level_by_turn[turns[i]] <= level_by_turn[turns[i-1]]:
                drp = int(turns[i])
                break

        # DRP on revision-only
        rev_subset = rev_only[rev_only["domain"] == domain]
        rev_level = rev_subset.groupby("turn")["level"].mean()
        rev_turns = sorted(rev_level.index)
        rev_drp = None
        for i in range(1, len(rev_turns)):
            if rev_level[rev_turns[i]] <= rev_level[rev_turns[i-1]]:
                rev_drp = int(rev_turns[i])
                break

        results[domain] = {
            "level_by_turn": {int(t): float(level_by_turn[t]) for t in turns},
            "drp": drp,
            "revision_only_level_by_turn": {int(t): float(rev_level[t]) for t in rev_turns},
            "revision_only_drp": rev_drp,
        }
        rev_traj = [f'{rev_level.get(t, 0):.2f}' for t in turns if t in rev_level.index]
        print(f"  {domain}: DRP={drp} (all), DRP={rev_drp} (rev-only)")
        print(f"    All:      {[f'{level_by_turn[t]:.2f}' for t in turns]}")
        print(f"    Rev-only: {rev_traj}")

    return results


# ── RQ3: Do models respect the DRP? ──

def rq3_overcorrection_rate(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ3: Do Models Respect the DRP? ==")

    # At each turn: evaluator "done" rate (level >= 4) vs worker revision rate
    eval_done = eval_df.groupby("turn").apply(lambda g: (g["level"] >= 4).mean())
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


# ── RQ4: Revision-Despite-Sufficiency ──

def rq4_revision_despite_sufficiency(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ4: Revision Despite Sufficiency ==")

    # Temporal alignment: evaluator judges turn T, worker decides at turn T+1.
    # Question: when the evaluator says output is already good at turn T (level >= 4),
    # does the worker still revise at turn T+1?
    eval_match = eval_df[["worker_trial_id", "turn", "level"]].copy()
    eval_match = eval_match.rename(columns={"worker_trial_id": "trial_id", "turn": "eval_turn"})

    worker_next = worker_df[worker_df["turn"] >= 2][["trial_id", "turn", "revised"]].copy()
    worker_next = worker_next.rename(columns={"turn": "next_turn"})

    # Join: evaluator at turn T -> worker at turn T+1
    eval_match["next_turn"] = eval_match["eval_turn"] + 1
    merged = eval_match.merge(worker_next, on=["trial_id", "next_turn"], how="inner")

    if merged.empty:
        print("  No matched data.")
        return {}

    # Cases where evaluator says done at turn T (level >= 4) but worker revises at T+1
    done_at_t = merged[merged["level"] >= 4]
    compliance_cases = done_at_t[done_at_t["revised"] == True]

    compliance_rate = len(compliance_cases) / len(done_at_t) if len(done_at_t) > 0 else 0
    print(f"  Evaluator says 'done' at turn T (level >= 4): {len(done_at_t)} cases")
    print(f"  Worker revises at T+1 anyway: {len(compliance_cases)} ({compliance_rate:.1%})")
    print(f"  -> Revision-despite-sufficiency rate: {compliance_rate:.1%}")

    # Quality stratification: show rate is stable across quality levels
    for level_threshold, label in [(4, "level==4"), (5, "level>=5")]:
        if level_threshold == 4:
            stratum = done_at_t[done_at_t["level"] == 4]
        else:
            stratum = done_at_t[done_at_t["level"] >= 5]
        if len(stratum) > 0:
            s_rev = stratum[stratum["revised"] == True]
            s_rate = len(s_rev) / len(stratum)
            print(f"  Quality stratum {label}: {len(s_rev)}/{len(stratum)} ({s_rate:.1%}) revise anyway")

    # Break down by turn
    print("\n  By turn:")
    for t in sorted(done_at_t["eval_turn"].unique()):
        t_done = done_at_t[done_at_t["eval_turn"] == t]
        t_comp = t_done[t_done["revised"] == True]
        rate = len(t_comp) / len(t_done) if len(t_done) > 0 else 0
        print(f"    Eval done at T{int(t)} -> revises at T{int(t)+1}: {len(t_comp)}/{len(t_done)} ({rate:.1%})")

    return {
        "total_done_evals": len(done_at_t),
        "unnecessary_revisions": len(compliance_cases),
        "revision_despite_sufficiency_rate": float(compliance_rate),
    }


# ── RQ5: Token cost ──

def rq5_token_cost(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    print("\n== RQ5: Token Cost of Zero-Value Revisions ==")

    # For each trial, find the first turn where evaluator level >= 4
    drp_per_trial = eval_df[eval_df["level"] >= 4].groupby("worker_trial_id")["turn"].min()

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
            turn = turn_idx + 1
            # Skip meta-responses (decline-to-revise) -- only measure stylistic
            # drift on actual content revisions
            if turn >= 2 and not classify_revision(response):
                continue
            words = response.split()
            unique_words = set(w.lower() for w in words)
            ttr = len(unique_words) / len(words) if words else 0
            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": turn,
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

    # Per-trial slopes to avoid pseudoreplication (Judge 5 verdict)
    len_slopes = []
    for tid, grp in df.groupby("trial_id"):
        if len(grp) >= 2:
            slope = np.polyfit(grp["turn"], grp["word_count"], 1)[0]
            len_slopes.append(slope)
    if len_slopes:
        t_stat, p_len = sp_stats.ttest_1samp(len_slopes, 0)
        mean_slope = np.mean(len_slopes)
        print(f"\n  Turn vs word_count (per-trial slopes): mean_slope={mean_slope:.1f}, t={t_stat:.2f}, p={p_len:.4f}, n_trials={len(len_slopes)}")
    else:
        mean_slope, p_len = 0, 1.0

    return {
        "drift_by_turn": drift.to_dict(),
        "length_trend": {"mean_slope": float(mean_slope), "p": float(p_len), "n_trials": len(len_slopes)},
    }


# ── RQ7: Targeted feedback ──

def rq7_targeted_feedback() -> dict:
    print("\n== RQ7: Targeted Feedback vs Generic Prompting ==")
    results = load_jsonl(S3_TARGETED_FEEDBACK_PATH)
    if not results:
        print("  No targeted feedback data.")
        return {}

    # Filter out entries where generic baseline is a meta-response (Judge 3 verdict)
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    worker_map = {t["trial_id"]: t for t in trials if t.get("status") == "success"}
    filtered = []
    meta_filtered_count = 0
    for r in results:
        if not r.get("targeted_level") or not r.get("generic_next_level"):
            continue
        trial = worker_map.get(r.get("worker_trial_id", ""))
        if trial and r.get("turn") is not None and r["turn"] < len(trial["responses"]):
            generic_response = trial["responses"][r["turn"]]
            if not classify_revision(generic_response):
                meta_filtered_count += 1
                continue
        filtered.append(r)
    print(f"  Excluded {meta_filtered_count} pairs where generic baseline was a meta-response")

    valid = filtered
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

    # Build revision flags
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    revision_flags = {}
    for trial in [t for t in trials if t.get("status") == "success"]:
        for turn_idx, response in enumerate(trial["responses"]):
            turn = turn_idx + 1
            is_rev = True if turn == 1 else classify_revision(response)
            revision_flags[(trial["trial_id"], turn)] = is_rev

    eval_with_rev = eval_df.copy()
    eval_with_rev["is_revision"] = eval_with_rev.apply(
        lambda r: revision_flags.get((r["worker_trial_id"], r["turn"]), True), axis=1
    )

    results = {}
    print(f"\n{'Model':<20} | {'Gap':>6} | {'Decline T2':>10} | {'Decline T5':>10} | {'Rev-only T1':>11} | {'Rev-only T5':>11}")
    print("-" * 85)

    for model in sorted(worker_df["model"].unique()):
        m_eval = eval_df[eval_df["model"] == model]
        m_worker = worker_df[(worker_df["model"] == model) & (worker_df["turn"] >= 2)]

        eval_done = m_eval.groupby("turn").apply(lambda g: (g["level"] >= 4).mean())
        worker_rev = m_worker.groupby("turn")["revised"].mean()
        level = m_eval.groupby("turn")["level"].mean()

        shared_turns = sorted(set(eval_done.index) & set(worker_rev.index))
        gaps = [worker_rev[t] - (1 - eval_done[t]) for t in shared_turns]
        mean_gap = np.mean(gaps) if gaps else 0

        # Revision-only quality
        m_rev = eval_with_rev[(eval_with_rev["model"] == model) & eval_with_rev["is_revision"]]
        rev_level = m_rev.groupby("turn")["level"].mean()

        # Decline rates
        m_all = eval_with_rev[eval_with_rev["model"] == model]
        decline_t2 = 1 - m_all[m_all["turn"] == 2]["is_revision"].mean() if len(m_all[m_all["turn"] == 2]) > 0 else 0
        decline_t5 = 1 - m_all[m_all["turn"] == 5]["is_revision"].mean() if len(m_all[m_all["turn"] == 5]) > 0 else 0

        results[model] = {
            "eval_done_rate": {int(k): float(v) for k, v in eval_done.items()},
            "worker_revision_rate": {int(k): float(v) for k, v in worker_rev.items()},
            "level_by_turn": {int(k): float(v) for k, v in level.items()},
            "revision_only_level_by_turn": {int(k): float(v) for k, v in rev_level.items()},
            "decline_rate_t2": float(decline_t2),
            "decline_rate_t5": float(decline_t5),
            "mean_overcorrection_gap": float(mean_gap),
        }
        rev_t1 = rev_level.get(1, 0)
        rev_t5 = rev_level.get(5, 0) if 5 in rev_level.index else 0
        print(f"  {model:<18} | {mean_gap:+.1%} | {decline_t2:>9.1%} | {decline_t5:>9.1%} | {rev_t1:>10.2f} | {rev_t5:>10.2f}")

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

    # Get evaluator quality for one-shot (from eval_df, oneshot entries have
    # turn=1 and their trial_id starts with "s3_oneshot__")
    oneshot_eval_map = {}
    for _, row in eval_df.iterrows():
        if "oneshot" in str(row.get("eval_id", "")):
            key = (row["model"], row.get("scenario_id", ""), row.get("run", 0))
            oneshot_eval_map[key] = row["level"]

    # Get iterative T1 quality (revision-only)
    rev_eval = get_revision_only_eval(eval_df)
    iterative_t1_map = {}
    iterative_best_map = {}
    for trial_id in rev_eval["worker_trial_id"].unique():
        t_eval = rev_eval[rev_eval["worker_trial_id"] == trial_id]
        if t_eval.empty:
            continue
        t1_row = t_eval[t_eval["turn"] == 1]
        if not t1_row.empty:
            # Find matching worker trial for the key
            wt = [t for t in worker_trials if t["trial_id"] == trial_id and t.get("status") == "success"]
            if wt:
                key = (wt[0]["model"], wt[0]["scenario_id"], wt[0]["run"])
                iterative_t1_map[key] = float(t1_row["level"].iloc[0])
                iterative_best_map[key] = float(t_eval["level"].max())

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
                "iterative_t1_quality": iterative_t1_map.get(key),
                "iterative_best_quality": iterative_best_map.get(key),
            })

    if comparisons:
        mean_savings = np.mean([c["savings_pct"] for c in comparisons])
        print(f"  Mean token savings (one-shot vs iterative): {mean_savings:.1%}")

        # One-shot quality scores (from evaluator data)
        oneshot_qualities = [v for v in oneshot_eval_map.values() if v is not None]
        if oneshot_qualities:
            mean_oneshot_q = np.mean(oneshot_qualities)
            print(f"  One-shot quality (blind evaluator): {mean_oneshot_q:.2f} (n={len(oneshot_qualities)})")
        else:
            mean_oneshot_q = None

        # Quality comparison
        with_quality = [c for c in comparisons if c["iterative_t1_quality"] is not None]
        if with_quality:
            mean_t1 = np.mean([c["iterative_t1_quality"] for c in with_quality])
            mean_best = np.mean([c["iterative_best_quality"] for c in with_quality])
            print(f"  Iterative T1 quality: {mean_t1:.2f}")
            print(f"  Iterative best quality (revision-only): {mean_best:.2f}")
            print(f"  Iterative revision gain over T1: {mean_best - mean_t1:+.2f}")
            print(f"  Note: one-shot prompt includes 'produce the best possible version'")
            print(f"    instruction absent from iterative T1; comparison is directional, not a clean ablation.")
            result = {
                "n": len(comparisons),
                "mean_token_savings": float(mean_savings),
                "iterative_t1_quality": float(mean_t1),
                "iterative_best_quality": float(mean_best),
                "revision_quality_gain": float(mean_best - mean_t1),
            }
            if mean_oneshot_q is not None:
                result["oneshot_quality"] = float(mean_oneshot_q)
            return result

        result = {"n": len(comparisons), "mean_token_savings": float(mean_savings)}
        if mean_oneshot_q is not None:
            result["oneshot_quality"] = float(mean_oneshot_q)
        return result

    return {}


# ── RQ10: Reversibility ──

def rq10_reversibility() -> dict:
    print("\n== RQ10: Reversibility Test ==")
    results = load_jsonl(S3_REVERSIBILITY_RESULTS_PATH)
    if not results:
        print("  No reversibility data.")
        return {}

    # Build revision flags for T5 to stratify results
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    t5_is_revision = {}
    for trial in [t for t in trials if t.get("status") == "success"]:
        if len(trial["responses"]) >= 5:
            t5_is_revision[trial["trial_id"]] = classify_revision(trial["responses"][4])

    valid = [r for r in results if r.get("prefers_turn1") is not None]
    prefers_t1 = sum(1 for r in valid if r["prefers_turn1"])
    prefers_t5 = sum(1 for r in valid if not r["prefers_turn1"])
    ties = len(results) - len(valid)

    total = len(valid)
    t1_rate = prefers_t1 / total if total > 0 else 0

    print(f"  Total comparisons: {len(results)} (valid: {total}, ties: {ties})")

    # Stratify by T5 revision status first to get clean headline
    rev_valid = [r for r in valid if t5_is_revision.get(r.get("worker_trial_id", ""), True)]
    meta_valid_list = [r for r in valid if not t5_is_revision.get(r.get("worker_trial_id", ""), True)]

    if rev_valid:
        rev_t1_count = sum(1 for r in rev_valid if r["prefers_turn1"])
        rev_rate = rev_t1_count / len(rev_valid)
        print(f"  HEADLINE (revision-only): Prefers T1 {rev_t1_count}/{len(rev_valid)} ({rev_rate:.1%})")
    print(f"  Including meta-responses: Prefers T1 {prefers_t1}/{total} ({t1_rate:.1%})")
    print(f"  Prefers Turn 5: {prefers_t5} ({1-t1_rate:.1%})")

    if total > 0:
        binom_p = float(sp_stats.binomtest(prefers_t1, total, 0.5).pvalue)
        print(f"  Binomial test (vs 50%): p={binom_p:.4f}")
    else:
        binom_p = None

    print(f"\n  Stratified by T5 content type:")
    if rev_valid:
        print(f"    T5 is revision (n={len(rev_valid)}): T1 preferred {rev_t1_count}/{len(rev_valid)} ({rev_rate:.1%})")
    if meta_valid_list:
        meta_t1 = sum(1 for r in meta_valid_list if r["prefers_turn1"])
        meta_rate = meta_t1 / len(meta_valid_list)
        print(f"    T5 is meta-response (n={len(meta_valid_list)}): T1 preferred {meta_t1}/{len(meta_valid_list)} ({meta_rate:.1%})")

    # Length-ratio robustness check: only compare length-stable pairs
    trial_resp_map = {t["trial_id"]: t["responses"] for t in trials if t.get("status") == "success"}
    length_stable = []
    for r in valid:
        trial_id = r.get("worker_trial_id", "")
        resps = trial_resp_map.get(trial_id)
        if resps and len(resps) >= 5:
            len_t1 = len(resps[0])
            len_t5 = len(resps[4])
            ratio = abs(len_t5 - len_t1) / max(len_t1, 1)
            if ratio < 0.3:
                length_stable.append(r)
    if length_stable:
        ls_t1 = sum(1 for r in length_stable if r["prefers_turn1"])
        ls_rate = ls_t1 / len(length_stable)
        print(f"    Length-stable pairs (|len_ratio| < 0.3, n={len(length_stable)}): T1 preferred {ls_t1}/{len(length_stable)} ({ls_rate:.1%})")

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

    result = {
        "prefers_t1_rate": float(t1_rate),
        "n": total,
        "binom_p": binom_p,
        "by_domain": domain_results,
    }
    if rev_valid:
        result["revision_only_t1_rate"] = float(rev_t1_count / len(rev_valid))
        result["revision_only_n"] = len(rev_valid)
    if meta_valid_list:
        result["meta_response_t1_rate"] = float(sum(1 for r in meta_valid_list if r["prefers_turn1"]) / len(meta_valid_list))
        result["meta_response_n"] = len(meta_valid_list)
    if length_stable:
        result["length_stable_t1_rate"] = float(ls_t1 / len(length_stable))
        result["length_stable_n"] = len(length_stable)

    return result


# ── RQ11: Cross-model convergence ──

def rq11_convergence() -> dict:
    print("\n== RQ11: Cross-Model Convergence ==")
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    successful = [t for t in trials if t.get("status") == "success"]

    grouped = defaultdict(lambda: defaultdict(dict))
    for trial in successful:
        key = (trial["scenario_id"], trial["run"])
        for turn_idx, response in enumerate(trial["responses"]):
            turn = turn_idx + 1
            # Skip meta-responses to avoid comparing content length with decline length
            if turn >= 2 and not classify_revision(response):
                continue
            grouped[key][turn][trial["model"]] = len(response)

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
            turn = turn_idx + 1
            # Skip meta-responses -- a decline to revise has low task overlap
            # by nature, not because of adherence decay
            if turn >= 2 and not classify_revision(response):
                continue
            resp_words = set(response.lower().split())
            overlap = len(task_words & resp_words) / len(task_words) if task_words else 0
            resp_word_count = len(response.split())
            rows.append({
                "trial_id": trial["trial_id"],
                "model": trial["model"],
                "domain": trial["domain"],
                "turn": turn,
                "task_overlap": overlap,
                "response_length": resp_word_count,
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

    # Per-trial slopes to avoid pseudoreplication (Judge 5 verdict)
    slopes = []
    for tid, grp in df.groupby("trial_id"):
        if len(grp) >= 2:
            slope = np.polyfit(grp["turn"], grp["task_overlap"], 1)[0]
            slopes.append(slope)
    if slopes:
        t_stat, p_val = sp_stats.ttest_1samp(slopes, 0)
        mean_slope = np.mean(slopes)
        print(f"\n  Per-trial slope (turn vs overlap): mean={mean_slope:.4f}, t={t_stat:.2f}, p={p_val:.4f}, n={len(slopes)}")
    else:
        mean_slope, p_val = 0, 1.0

    # Length covariate: partial correlation via OLS residualization (Judge 5 verdict)
    if len(df) > 2 and df["response_length"].std() > 0:
        resid_overlap = df["task_overlap"] - np.polyval(np.polyfit(df["response_length"], df["task_overlap"], 1), df["response_length"])
        resid_turn = df["turn"] - np.polyval(np.polyfit(df["response_length"], df["turn"], 1), df["response_length"])
        rho_partial, p_partial = sp_stats.spearmanr(resid_turn, resid_overlap)
        print(f"  Length-controlled partial correlation: rho={rho_partial:.3f}, p={p_partial:.4f}")
    else:
        rho_partial, p_partial = 0, 1.0

    return {
        "overlap_by_turn": {int(k): float(v) for k, v in overlap_by_turn.items()},
        "trend": {"mean_slope": float(mean_slope), "p": float(p_val), "n_trials": len(slopes)},
        "length_controlled": {"rho_partial": float(rho_partial), "p": float(p_partial)},
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

    # Stratify by meta-response contamination in conversation history (Judge 3 verdict)
    trials = load_jsonl(S3_WORKER_TRIALS_PATH)
    trial_map = {t["trial_id"]: t for t in trials if t.get("status") == "success"}
    clean_recs = []
    contaminated_recs = []
    for r in valid:
        trial = trial_map.get(r.get("worker_trial_id", ""))
        if not trial:
            continue
        meta_count = sum(1 for i, resp in enumerate(trial["responses"]) if i >= 1 and not classify_revision(resp))
        if meta_count == 0:
            clean_recs.append(r["recommended_turn"])
        else:
            contaminated_recs.append(r["recommended_turn"])

    print(f"\n  By meta-response contamination:")
    if clean_recs:
        print(f"    0 meta turns (n={len(clean_recs)}): mean recommended={np.mean(clean_recs):.2f}")
    if contaminated_recs:
        print(f"    1+ meta turns (n={len(contaminated_recs)}): mean recommended={np.mean(contaminated_recs):.2f}")

    result = {
        "mean_recommended_turn": float(mean_rec),
        "distribution": dict(rec_dist),
        "not_last_rate": float(not_last_rate),
        "by_model": {m: {"mean": float(np.mean(t)), "n": len(t)} for m, t in by_model.items()},
    }
    if clean_recs:
        result["clean_mean_rec"] = float(np.mean(clean_recs))
        result["clean_n"] = len(clean_recs)
    if contaminated_recs:
        result["contaminated_mean_rec"] = float(np.mean(contaminated_recs))
        result["contaminated_n"] = len(contaminated_recs)

    return result


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
    """Cost-Adjusted Revision Yield: CARY(t) = Q(t)/6 - C * T_cum(t)

    Linear penalty replaces original exponential (Judge 2 verdict):
    exponential collapsed discriminative power across budget tiers.
    Linear form directly mirrors per-token pricing and produces
    distinct optimal stops at different C values.
    """
    turns = sorted(quality_by_turn.keys())
    cary = {}
    t_cum = 0
    for t in turns:
        t_cum += tokens_by_turn.get(t, 0)
        cary[t] = (quality_by_turn[t] / 6.0) - C * t_cum
    return cary


def rq15_revision_yield_equations(eval_df: pd.DataFrame, worker_df: pd.DataFrame) -> dict:
    print("\n== RQ15: Revision Yield Equations ==")

    # Use revision-only quality (meta-responses excluded as N/A)
    rev_eval = get_revision_only_eval(eval_df)
    level_by_turn = rev_eval.groupby("turn")["level"].mean().to_dict()
    # Tokens from revision-only worker rows
    rev_worker = worker_df[worker_df["revised"] == True]
    tokens_by_turn = rev_worker.groupby("turn")["output_tokens"].mean().to_dict()
    print(f"  (Using revision-only data: {len(rev_eval)} graded responses, meta-responses excluded as N/A)")

    mry = compute_mry(level_by_turn, tokens_by_turn)
    cry = compute_cry(level_by_turn, tokens_by_turn)

    # CARY at multiple C values (recalibrated for linear penalty)
    c_values = {
        "unlimited": 0,
        "api_heavy": 1e-5,
        "api_light": 5e-5,
        "pro": 1e-4,
        "max": 2e-4,
        "plus": 5e-4,
        "free": 1e-3,
    }

    cary_results = {}
    optimal_stops = {}
    for label, c_val in c_values.items():
        cary = compute_cary(level_by_turn, tokens_by_turn, c_val)
        cary_results[label] = {int(k): float(v) for k, v in cary.items()}
        if cary:
            t_star = max(cary.keys(), key=lambda t: cary[t])
            optimal_stops[label] = int(t_star)

    print(f"\nAggregate MRY: {mry}")
    print(f"Aggregate CRY: {cry}")
    print(f"Aggregate optimal stops by budget tier: {optimal_stops}")

    # DRP using MRY definition
    drp = None
    for t in sorted(mry.keys()):
        if mry[t] <= 0:
            drp = t
            break

    print(f"Aggregate DRP (first turn with MRY <= 0): {drp}")

    # Per-model breakdown (Judge 2 verdict: aggregate hides sign flips)
    per_model = {}
    print(f"\nPer-model breakdown:")
    for model in sorted(rev_eval["model"].unique()):
        m_eval = rev_eval[rev_eval["model"] == model]
        m_worker = worker_df[(worker_df["model"] == model) & (worker_df["revised"] == True)]
        m_level = m_eval.groupby("turn")["level"].mean().to_dict()
        m_tokens = m_worker.groupby("turn")["output_tokens"].mean().to_dict()

        m_mry = compute_mry(m_level, m_tokens)
        m_cary = compute_cary(m_level, m_tokens, 1e-4)  # Pro tier
        m_drp = None
        for t in sorted(m_mry.keys()):
            if m_mry[t] <= 0:
                m_drp = t
                break
        m_tstar = max(m_cary.keys(), key=lambda t: m_cary[t]) if m_cary else 1

        per_model[model] = {
            "level_by_turn": {int(k): float(v) for k, v in m_level.items()},
            "mry": {int(k): float(v) for k, v in m_mry.items()},
            "drp": m_drp,
            "cary_tstar_pro": int(m_tstar),
        }
        traj = [f"{m_level.get(t, 0):.2f}" for t in sorted(m_level.keys())]
        print(f"  {model}: traj={traj}, DRP={m_drp}, CARY_t*={m_tstar}")

    return {
        "aggregate": {
            "mry": {int(k): float(v) for k, v in mry.items()},
            "cry": {int(k): float(v) for k, v in cry.items()},
            "cary": cary_results,
            "optimal_stops": optimal_stops,
            "drp": drp,
        },
        "per_model": per_model,
    }


# ── RQ16: Unit economics ──

# Real 2025 API pricing (per output token)
API_PRICING = {
    "gpt-4o": 10.0 / 1_000_000,       # $10/1M output tokens
    "claude-sonnet-4": 15.0 / 1_000_000,  # $15/1M output tokens
    "gemini-2.5-flash": 0.40 / 1_000_000,  # $0.40/1M output tokens
    "llama-3.3-70b": 0.88 / 1_000_000,   # $0.88/1M output tokens (Together)
    "qwen-3-235b": 0.90 / 1_000_000,     # $0.90/1M output tokens (Together)
    "deepseek-v4": 0.55 / 1_000_000,     # $0.55/1M output tokens
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
    # Use revision-only quality (meta-responses excluded as N/A)
    rev_eval = get_revision_only_eval(eval_df)
    print(f"  (Using revision-only quality: meta-responses excluded as N/A)")
    results = {}

    for model in sorted(worker_df["model"].unique()):
        m_eval = rev_eval[rev_eval["model"] == model]
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
        cary = compute_cary(level_by_turn, tokens_by_turn, 1e-4)
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
            d_cary = compute_cary(d_level, d_tokens, 1e-4)
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

    # Use revision-only eval: meta-responses are N/A, not Level 1
    rev_eval = get_revision_only_eval(eval_df)
    print(f"  (Using revision-only quality: meta-responses excluded as N/A)")

    # For each trial, find t_done (first revision turn >= T2 with level >= 4)
    # Only count trials where revision actually occurred before reaching threshold (Judge 2 verdict)
    drp_per_trial = rev_eval[(rev_eval["level"] >= 4) & (rev_eval["turn"] >= 2)].groupby("worker_trial_id")["turn"].min()

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

    # Get quality at t_done and final turn -- revision-only
    # For quality regression, use the last REVISION turn's quality, not the
    # last turn overall (which may be a meta-response scored Level 1)
    eval_by_trial_turn = {}
    for _, row in rev_eval.iterrows():
        eval_by_trial_turn[(row["worker_trial_id"], row["turn"])] = row["level"]

    ocs_scores = []
    for trial_id, t_done in drp_per_trial.items():
        if trial_id not in trial_data:
            continue
        td = trial_data[trial_id]
        n_turns = td["n_turns"]
        # max_er = maximum possible excess rounds (if task was done at turn 1)
        max_er = n_turns - 1

        if max_er <= 0:
            continue

        # Component 1: Excess Rounds (turns after DRP)
        er = n_turns - t_done

        # Component 2: Wasted Token Fraction
        tokens_after = sum(td["tokens_by_turn"][t_done:])
        total_tokens = td["total_tokens"]
        wtf = tokens_after / total_tokens if total_tokens > 0 else 0

        # Component 3: Quality Regression
        # Use the last revision turn's quality (not last turn overall,
        # which may be a meta-response excluded from grading)
        q_done = eval_by_trial_turn.get((trial_id, t_done), None)
        q_final = None
        for t_check in range(n_turns, 0, -1):
            q_final = eval_by_trial_turn.get((trial_id, t_check), None)
            if q_final is not None:
                break
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
            turn = turn_idx + 1
            if turn >= 2 and not classify_revision(response):
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

    # Per-trial slopes to avoid pseudoreplication (Judge 5 verdict)
    struct_slopes = []
    for tid, grp in df.groupby("trial_id"):
        if len(grp) >= 2:
            slope = np.polyfit(grp["turn"], grp["total_structure"], 1)[0]
            struct_slopes.append(slope)
    if struct_slopes:
        t_stat, p = sp_stats.ttest_1samp(struct_slopes, 0)
        mean_slope = np.mean(struct_slopes)
        print(f"\n  Per-trial slope (turn vs structure): mean={mean_slope:.2f}, t={t_stat:.2f}, p={p:.4f}, n={len(struct_slopes)}")
        print(f"  {'Structure increases over turns' if mean_slope > 0 else 'Structure stable or decreasing'}")
    else:
        mean_slope, p = 0, 1.0

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
        "trend": {"mean_slope": float(mean_slope), "p": float(p), "n_trials": len(struct_slopes)},
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
            # Skip meta-responses
            if not classify_revision(resps[i]):
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
                if not classify_revision(resps[i]):
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

    # Per-trial slopes to avoid pseudoreplication (Judge 5 verdict)
    drift_slopes = []
    for tid, grp in drift.groupby("trial_id"):
        if len(grp) >= 2:
            slope = np.polyfit(grp["turn"], grp["cosine_sim"], 1)[0]
            drift_slopes.append(slope)
    if drift_slopes:
        t_stat, p = sp_stats.ttest_1samp(drift_slopes, 0)
        mean_slope = np.mean(drift_slopes)
        print(f"\n  Per-trial slope (turn vs T1-similarity): mean={mean_slope:.4f}, t={t_stat:.2f}, p={p:.4f}, n={len(drift_slopes)}")
        print(f"  {'Drifting from original' if mean_slope < 0 else 'Staying close to original'}")
    else:
        mean_slope, p = 0, 1.0

    return {
        "consecutive_similarity": {int(t): float(v) for t, v in by_turn.items()},
        "drift_from_t1": {int(t): float(v) for t, v in drift_by_turn.items()},
        "drift_trend": {"mean_slope": float(mean_slope), "p": float(p), "n_trials": len(drift_slopes)},
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
            turn = turn_idx + 1
            if turn >= 2 and not classify_revision(response):
                continue
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

    # Per-trial slopes to avoid pseudoreplication (Judge 5 verdict)
    recall_slopes = []
    for tid, grp in df.groupby("trial_id"):
        if len(grp) >= 2:
            slope = np.polyfit(grp["turn"], grp["constraint_recall"], 1)[0]
            recall_slopes.append(slope)
    if recall_slopes:
        t_stat, p = sp_stats.ttest_1samp(recall_slopes, 0)
        mean_slope = np.mean(recall_slopes)
        print(f"\n  Per-trial slope (turn vs recall): mean={mean_slope:.4f}, t={t_stat:.2f}, p={p:.4f}, n={len(recall_slopes)}")
    else:
        mean_slope, p = 0, 1.0

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
        "trend": {"mean_slope": float(mean_slope), "p": float(p), "n_trials": len(recall_slopes)},
        "significant_drop_rate": float(significant_drops / len(shared)) if shared else 0.0,
    }


# ── Survivorship Analysis (Judge 1 verdict) ──

def survivorship_analysis(worker_df: pd.DataFrame, eval_df: pd.DataFrame) -> dict:
    """Analyze attrition as a study variable, not a confound.

    The 65% of trials that self-terminate via meta-responses are themselves
    evidence of overcorrection resistance. The balanced panel (trials completing
    all 5 turns as revisions) serves as a robustness check.
    """
    print("\n== Survivorship Analysis ==")

    # Per-turn survival rate (fraction still actively revising)
    survival_by_turn = {}
    for t in range(1, 6):
        t_data = worker_df[worker_df["turn"] == t]
        if len(t_data) > 0:
            survival_by_turn[t] = float(t_data["revised"].mean()) if t >= 2 else 1.0

    print(f"\nOverall survival rate (fraction revising) by turn:")
    for t, rate in sorted(survival_by_turn.items()):
        print(f"  Turn {t}: {rate:.1%}")

    # Per-model survival
    per_model_survival = {}
    print(f"\nPer-model T1-to-T5 survival rate:")
    for model in sorted(worker_df["model"].unique()):
        m_df = worker_df[(worker_df["model"] == model) & (worker_df["turn"] == 5)]
        if len(m_df) > 0:
            rate = float(m_df["revised"].mean())
        else:
            rate = 0.0
        per_model_survival[model] = rate
        print(f"  {model}: {rate:.1%}")

    # Balanced panel: trials where model revised at ALL 5 turns
    trial_survival = worker_df[worker_df["turn"] >= 2].groupby("trial_id")["revised"].all()
    balanced_ids = set(trial_survival[trial_survival].index)
    total_trials = len(trial_survival)
    print(f"\nBalanced panel: {len(balanced_ids)}/{total_trials} trials ({len(balanced_ids)/total_trials:.1%}) revised at all turns")

    # Balanced panel quality trajectory (robustness check)
    rev_eval = get_revision_only_eval(eval_df)
    balanced_eval = rev_eval[rev_eval["worker_trial_id"].isin(balanced_ids)]
    balanced_level = balanced_eval.groupby("turn")["level"].mean()
    print(f"\nBalanced panel quality trajectory:")
    for t in sorted(balanced_level.index):
        print(f"  Turn {t}: {balanced_level[t]:.2f} (n={len(balanced_eval[balanced_eval['turn'] == t])})")

    # Compare T1 quality: survivors vs non-survivors
    t1_eval = eval_df[eval_df["turn"] == 1]
    survivor_t1 = t1_eval[t1_eval["worker_trial_id"].isin(balanced_ids)]["level"]
    nonsurvivor_t1 = t1_eval[~t1_eval["worker_trial_id"].isin(balanced_ids)]["level"]

    if len(survivor_t1) > 0 and len(nonsurvivor_t1) > 0:
        u_stat, mann_p = sp_stats.mannwhitneyu(survivor_t1, nonsurvivor_t1, alternative="two-sided")
        print(f"\n  T1 quality: survivors={survivor_t1.mean():.2f} (n={len(survivor_t1)}), "
              f"non-survivors={nonsurvivor_t1.mean():.2f} (n={len(nonsurvivor_t1)})")
        print(f"  Mann-Whitney U: U={u_stat:.0f}, p={mann_p:.4f}")
        mann_result = {"U": float(u_stat), "p": float(mann_p),
                       "survivor_mean": float(survivor_t1.mean()),
                       "nonsurvivor_mean": float(nonsurvivor_t1.mean())}
    else:
        mann_result = {}

    return {
        "survival_by_turn": survival_by_turn,
        "per_model_survival": per_model_survival,
        "balanced_panel_n": len(balanced_ids),
        "balanced_panel_pct": float(len(balanced_ids) / total_trials) if total_trials > 0 else 0,
        "balanced_panel_level_by_turn": {int(t): float(balanced_level[t]) for t in balanced_level.index},
        "t1_quality_comparison": mann_result,
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

    # Edge case framework: decompose aggregates, flag compositional artifacts
    results["edge_cases"] = edge_case_framework(worker_df, eval_df)

    results["rq1"] = rq1_revision_yield_curve(worker_df, eval_df)
    results["rq2"] = rq2_drp_by_domain(eval_df)
    results["rq3"] = rq3_overcorrection_rate(worker_df, eval_df)
    results["rq4"] = rq4_revision_despite_sufficiency(worker_df, eval_df)
    results["rq5"] = rq5_token_cost(worker_df, eval_df)
    results["rq6"] = rq6_stylistic_drift(worker_df)
    results["rq7"] = rq7_targeted_feedback()
    results["rq8"] = rq8_cross_model(worker_df, eval_df)
    results["rq9"] = rq9_oneshot_ceiling(eval_df)
    results["rq10"] = rq10_reversibility()
    # RQ11 dropped: character-length CV does not measure semantic convergence (Judge 5 verdict)
    # RQ13 dropped: word-list cosmetic detector produces degenerate 0.3% rate (Judge 5 verdict)
    results["rq12"] = rq12_instruction_adherence(worker_df)
    results["rq14"] = rq14_self_reflection()
    results["rq15"] = rq15_revision_yield_equations(eval_df, worker_df)
    results["rq16"] = rq16_unit_economics(eval_df, worker_df)
    results["rq17"] = rq17_overcorrection_magnitude(eval_df, worker_df)
    results["revision_efficiency"] = revision_efficiency_analysis(worker_df)
    results["structural_bloat"] = structural_bloat_analysis()
    results["semantic_similarity"] = semantic_similarity_analysis()
    # Use revision-only eval for wavering to avoid meta-response Level 1 creating false sign-changes (Judge 3 verdict)
    results["wavering"] = wavering_analysis(get_revision_only_eval(eval_df))
    results["constraint_satisfaction"] = constraint_satisfaction_analysis(eval_df)
    results["position_bias"] = position_bias_check()
    results["survivorship"] = survivorship_analysis(worker_df, eval_df)

    results_path = S3_STATS_DIR / "study3_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved all results to {results_path}")
    print("Done.")


if __name__ == "__main__":
    main()
