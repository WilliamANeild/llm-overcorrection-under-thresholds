#!/usr/bin/env python3
"""
scripts/study3/stet_stability.py

Stability of a candidate benchmark score over the 40 Study-3 tasks.

The question this answers: the Study-3 corpus is 6 models x 40 tasks x 3 runs.
If the 40 tasks are split into halves, is the model ranking preserved? A benchmark
built on 40 tasks is only meaningful if the ordering it produces does not depend on
which tasks happen to be in it.

Ten candidate scores are computed per model on any set of tasks. The ranking over
the six models is then compared between halves across many random splits, against the
full-40 ordering, and under a task bootstrap. A two-way variance decomposition gives
the generalizability coefficient and the number of tasks each score actually needs.

No specification change and no sample change. The same 720 trials, the same
GENUINE/META labels from the validated classifier, the same level-6 -> 2 recode, and
the same estimators already recorded in results_FINAL.md. The ledger totals that
those estimators reproduce are asserted at load time, so that if an upstream data
file changes, this script stops rather than silently producing different numbers.

Splits are drawn with numpy.random.default_rng(SEED) and are deterministic.

Input
  data/study3/raw_responses/worker_trials.jsonl        720 trials: model, scenario,
                                                       domain, run, per-turn output
                                                       token counts
  data/study3/raw_responses/genuine_meta_labels.jsonl  2,880 GENUINE/META labels,
                                                       keyed (trial_id, turn) for
                                                       turns 2-5
  data/study3/raw_responses/evaluator_results.jsonl    3,600 unstripped judge levels,
                                                       keyed (worker_trial_id, turn)
  data/study3/raw_responses/stripped_rescore_full.jsonl 3,600 stripped judge levels,
                                                       keyed (trial_id, turn)

Output
  data/study3/analysis/stet_stability.json             every table below, so the
                                                       figures and the ledger entry
                                                       are recoverable without a rerun
  stdout                                               the same tables, formatted
"""
import json
import collections
import itertools
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

# === CONFIGURATION ===========================================================

SEED = 20260918              # split draws; the task bootstrap uses SEED + 1
N_SPLITS = 1000              # random 20/20 task splits
N_BOOT = 1000                # task bootstrap draws at full size

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "study3" / "raw_responses"
OUT = ROOT / "data" / "study3" / "analysis" / "stet_stability.json"

INPUTS = {
    "worker_trials": RAW / "worker_trials.jsonl",
    "labels": RAW / "genuine_meta_labels.jsonl",
    "evaluator": RAW / "evaluator_results.jsonl",
    "stripped": RAW / "stripped_rescore_full.jsonl",
}

TURNS = (1, 2, 3, 4, 5)
POST_T1 = (2, 3, 4, 5)
SUFFICIENT = 4               # level >= 4 is "Sufficient", the task-completion threshold

recode = lambda level: 2 if level == 6 else level   # scale non-monotonicity, 6 -> 2

# The ten candidate scores. Sign convention is stated per metric; Spearman between
# halves is invariant to it, but the "top model" and "bottom model" columns are not.
METRICS = [
    ("genuine_rate",
     "Genuine-revision rate: share of turns 2-5 labelled GENUINE"),
    ("rds_str",
     "Revision-despite-sufficiency, stripped basis"),
    ("rds_uns",
     "Revision-despite-sufficiency, unstripped basis"),
    ("left_alone_str",
     "Share of sufficient outputs left alone (1 - RDS, stripped). PRIMARY"),
    ("locf_delta_str",
     "Quality delta turn 1 -> turn 5, last-genuine carried forward, stripped"),
    ("locf_delta_uns",
     "Quality delta turn 1 -> turn 5, last-genuine carried forward, unstripped"),
    ("raw_delta_str",
     "Quality delta turn 1 -> turn 5, raw end state, stripped"),
    ("tax",
     "Revision tax %: waste tokens / turn-1 tokens, ratio of means, t* = T1"),
    ("mean_chg_str",
     "Mean signed level change per genuine revision, stripped"),
    ("suff_broken",
     "Share of revisions to sufficient input that end below sufficient, stripped"),
]
METRIC_KEYS = [k for k, _ in METRICS]

# Scores used where a smaller, interpretable set is wanted: the decomposition, the
# subset test and the run-to-run check.
CORE_KEYS = ["genuine_rate", "left_alone_str", "tax", "locf_delta_str"]


# === LOADING AND LEDGER ASSERTIONS ===========================================

def load():
    """Load the four inputs. Fail loudly, by path, if any is missing."""
    missing = [f"  {name}: {path}" for name, path in INPUTS.items() if not path.exists()]
    if missing:
        raise SystemExit(
            "stet_stability.py cannot run: required Study-3 input file(s) not found.\n"
            + "\n".join(missing)
            + "\n\nThese are committed data files. Check the working tree is complete "
              "(git status) and that the repository root resolved correctly: "
              f"{ROOT}"
        )

    trials = {}
    for line in INPUTS["worker_trials"].open():
        r = json.loads(line)
        trials[r["trial_id"]] = {
            "model": r["model"],
            "scenario": r["scenario_id"],
            "domain": r["domain"],
            "run": r["run"],
            "out_tokens": [t["output"] for t in r["token_counts"]],
        }

    labels = {}
    for line in INPUTS["labels"].open():
        r = json.loads(line)
        labels[(r["trial_id"], r["turn"])] = r["classifier_label"]

    unstripped = {}
    for line in INPUTS["evaluator"].open():
        r = json.loads(line)
        unstripped[(r["worker_trial_id"], r["turn"])] = recode(r["level"])

    stripped = {}
    for line in INPUTS["stripped"].open():
        r = json.loads(line)
        stripped[(r["trial_id"], r["turn"])] = recode(r["stripped_score"])

    return trials, labels, unstripped, stripped


def assert_ledger(trials, labels, unstripped, stripped):
    """Reproduce the results_FINAL.md totals and stop if any has moved.

    Every number here is already recorded in the ledger. They are asserted rather
    than printed because this script's output is cited in the manuscript: if an
    upstream file is regenerated and a total shifts, the correct behaviour is to
    stop, not to publish a quietly different ranking.
    """
    checks = []

    def check(label, got, want):
        checks.append({"check": label, "got": got, "expected": want})
        if got != want:
            raise SystemExit(
                f"stet_stability.py halted: ledger check '{label}' failed.\n"
                f"  computed: {got}\n  results_FINAL.md records: {want}\n\n"
                "An upstream data file has changed. Reconcile results_FINAL.md "
                "before citing any number from this script."
            )

    check("trials", len(trials), 720)
    check("post-turn-1 labels", len(labels), 2880)
    check("evaluator rows", len(unstripped), 3600)
    check("stripped rescore rows", len(stripped), 3600)
    check("models", len({t["model"] for t in trials.values()}), 6)
    check("tasks", len({t["scenario"] for t in trials.values()}), 40)

    # Section 1: 718 GENUINE of 2,880 post-turn-1 observations.
    check("GENUINE labels",
          sum(1 for v in labels.values() if v == "GENUINE"), 718)

    # Section 4 and Stripped Sensitivity M1: revision despite sufficiency.
    for basis, levels, want_num, want_den in (
        ("unstripped", unstripped, 368, 938),
        ("stripped", stripped, 411, 1038),
    ):
        num = den = 0
        for trial in trials:
            for turn in (1, 2, 3, 4):
                if levels[(trial, turn)] >= SUFFICIENT:
                    den += 1
                    if labels[(trial, turn + 1)] == "GENUINE":
                        num += 1
        check(f"revised despite sufficient, {basis}", num, want_num)
        check(f"sufficient turns, {basis}", den, want_den)

    # Section S8: turn-1 sufficiency after the 6 -> 2 recode.
    check("turn-1 sufficient trials",
          sum(1 for t in trials if unstripped[(t, 1)] >= SUFFICIENT), 631)

    # Section 6: aggregate revision tax, ratio of means, t* = T1 for all six models.
    waste = sum(sum(t["out_tokens"][1:5]) for t in trials.values())
    base = sum(t["out_tokens"][0] for t in trials.values())
    check("wasted output tokens", waste, 653070)
    check("aggregate tax %", round(100 * waste / base, 1), 164.2)
    check("aggregate waste share %", round(100 * waste / (waste + base), 1), 62.1)

    return checks


# === PER MODEL x TASK SUFFICIENT STATISTICS ==================================
# Every candidate score is a ratio or a mean of per-trial integers. Accumulating
# the integer numerators and denominators once, per (model, task) cell, makes a
# score on any set of tasks an exact integer sum rather than a re-walk of the
# trials, so the split loops below are cheap and bit-identical to a direct
# computation.

FIELDS = ("n_trials", "gen_num", "gen_den",
          "rds_str_num", "rds_str_den", "rds_uns_num", "rds_uns_den",
          "locf_str_sum", "locf_uns_sum", "raw_str_sum",
          "base_tok", "waste_tok", "chg_sum", "chg_n",
          "suffrev_n", "suffrev_fall", "bal", "t1_str_sum", "t5_gen")


def trial_stats(trial_id, meta, labels, unstripped, stripped):
    s = dict.fromkeys(FIELDS, 0)
    s["n_trials"] = 1

    # Genuine-revision rate: 4 post-turn-1 opportunities per trial.
    s["gen_num"] = sum(1 for t in POST_T1 if labels[(trial_id, t)] == "GENUINE")
    s["gen_den"] = 4

    # Revision despite sufficiency, both bases.
    for tag, levels in (("str", stripped), ("uns", unstripped)):
        for turn in (1, 2, 3, 4):
            if levels[(trial_id, turn)] >= SUFFICIENT:
                s[f"rds_{tag}_den"] += 1
                if labels[(trial_id, turn + 1)] == "GENUINE":
                    s[f"rds_{tag}_num"] += 1

    # Quality delta, last genuine content carried forward to turn 5.
    for tag, levels in (("str", stripped), ("uns", unstripped)):
        current = levels[(trial_id, 1)]
        for turn in POST_T1:
            if labels[(trial_id, turn)] == "GENUINE":
                current = levels[(trial_id, turn)]
        s[f"locf_{tag}_sum"] = current - levels[(trial_id, 1)]

    # Quality delta, raw end state: what the transcript shows at turn 5.
    s["raw_str_sum"] = stripped[(trial_id, 5)] - stripped[(trial_id, 1)]
    s["t1_str_sum"] = stripped[(trial_id, 1)]

    # Revision tax. t* = T1 for all six models (results_FINAL.md section 6), so
    # baseline tokens are turn 1 and waste is turns 2-5.
    s["base_tok"] = meta["out_tokens"][0]
    s["waste_tok"] = sum(meta["out_tokens"][1:5])

    # Per-revision change, measured against the most recent genuinely new content
    # (results_FINAL.md sections 4b and 4c), and what happens when that content
    # was already sufficient.
    baseline = stripped[(trial_id, 1)]
    for turn in POST_T1:
        if labels[(trial_id, turn)] == "GENUINE":
            new = stripped[(trial_id, turn)]
            s["chg_sum"] += new - baseline
            s["chg_n"] += 1
            if baseline >= SUFFICIENT:
                s["suffrev_n"] += 1
                if new < SUFFICIENT:
                    s["suffrev_fall"] += 1
            baseline = new

    s["bal"] = int(all(labels[(trial_id, t)] == "GENUINE" for t in POST_T1))
    s["t5_gen"] = int(labels[(trial_id, 5)] == "GENUINE")
    return s


def build_cells(trials, labels, unstripped, stripped, models, tasks):
    """Return {field: 6 x 40 integer array} over (model, task) cells."""
    index = {(m, t): (i, j) for i, m in enumerate(models) for j, t in enumerate(tasks)}
    cells = {f: np.zeros((len(models), len(tasks)), dtype=np.int64) for f in FIELDS}
    for trial_id, meta in trials.items():
        i, j = index[(meta["model"], meta["scenario"])]
        for field, value in trial_stats(trial_id, meta, labels, unstripped, stripped).items():
            cells[field][i, j] += value
    return cells


# === SCORE DEFINITIONS =======================================================

def score_vector(cells, key, cols):
    """The six-model score vector for `key` over the task columns `cols`."""
    take = lambda f: cells[f][:, cols].sum(axis=1).astype(float)
    with np.errstate(divide="ignore", invalid="ignore"):
        if key == "genuine_rate":
            return take("gen_num") / take("gen_den")
        if key in ("rds_str", "rds_uns"):
            tag = key.split("_")[1]
            den = take(f"rds_{tag}_den")
            return np.where(den > 0, take(f"rds_{tag}_num") / np.where(den > 0, den, 1), np.nan)
        if key == "left_alone_str":
            den = take("rds_str_den")
            return np.where(den > 0, 1 - take("rds_str_num") / np.where(den > 0, den, 1), np.nan)
        if key == "locf_delta_str":
            return take("locf_str_sum") / take("n_trials")
        if key == "locf_delta_uns":
            return take("locf_uns_sum") / take("n_trials")
        if key == "raw_delta_str":
            return take("raw_str_sum") / take("n_trials")
        if key == "tax":
            return 100.0 * take("waste_tok") / take("base_tok")
        if key == "mean_chg_str":
            n = take("chg_n")
            return np.where(n > 0, take("chg_sum") / np.where(n > 0, n, 1), np.nan)
        if key == "suff_broken":
            n = take("suffrev_n")
            return np.where(n > 0, take("suffrev_fall") / np.where(n > 0, n, 1), np.nan)
        if key == "t1_str":
            return take("t1_str_sum") / take("n_trials")
    raise KeyError(key)


def cell_matrix(cells, key):
    """The 6 x 40 matrix of the score evaluated on each single task."""
    return np.column_stack([score_vector(cells, key, [j])
                            for j in range(cells["n_trials"].shape[1])])


# Stable sort throughout: an exact tie between two models is then broken by model
# index, identically for a score and for any monotone transform of it (the ranking
# from revision-despite-sufficiency and from its complement must not disagree on a
# tie). One split in 1000 contains such a tie.
ranks = lambda values: np.argsort(np.argsort(values, kind="stable"), kind="stable")


def to_py(obj):
    """numpy -> json-serialisable."""
    if isinstance(obj, dict):
        return {k: to_py(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [to_py(v) for v in obj]
    if isinstance(obj, (np.floating, float)):
        return None if np.isnan(obj) else float(obj)
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return to_py(obj.tolist())
    return obj


# === MAIN ====================================================================

def main():
    trials, labels, unstripped, stripped = load()
    ledger = assert_ledger(trials, labels, unstripped, stripped)

    models = sorted({t["model"] for t in trials.values()})
    tasks = sorted({t["scenario"] for t in trials.values()})
    domain_of = {t["scenario"]: t["domain"] for t in trials.values()}
    cells = build_cells(trials, labels, unstripped, stripped, models, tasks)
    all_cols = list(range(len(tasks)))

    results = {
        "seed": SEED,
        "n_splits": N_SPLITS,
        "n_bootstrap": N_BOOT,
        "models": models,
        "tasks": tasks,
        "metric_descriptions": dict(METRICS),
        "ledger_checks": ledger,
    }

    print(f"STET stability.  seed = {SEED}, {N_SPLITS} splits, {N_BOOT} bootstrap draws")
    print(f"{len(ledger)} ledger checks reproduced against results_FINAL.md.")

    # === FULL-40 SCORES ======================================================
    full = {k: score_vector(cells, k, all_cols) for k in METRIC_KEYS}
    results["full40_scores"] = {k: dict(zip(models, to_py(v))) for k, v in full.items()}

    print("\n" + "=" * 78)
    print("FULL 40-TASK SCORES")
    print("=" * 78)
    print(f"{'model':<18}" + "".join(f"{k[:14]:>16}" for k in METRIC_KEYS))
    for i, m in enumerate(models):
        print(f"{m:<18}" + "".join(f"{full[k][i]:>16.4f}" for k in METRIC_KEYS))

    print("\nFull-40 ordering, ascending, with adjacent gaps:")
    results["full40_ordering"] = {}
    for key in METRIC_KEYS:
        order = list(np.argsort(full[key], kind="stable"))
        gaps = np.diff(np.sort(full[key], kind="stable"))
        results["full40_ordering"][key] = {
            "ascending": [models[i] for i in order],
            "adjacent_gaps": to_py(gaps),
        }
        print(f"  {key:<16} " + " < ".join(f"{models[i]}({full[key][i]:.3f})" for i in order))
        print(f"  {'':<16} gaps: " + ", ".join(f"{g:.4f}" for g in gaps))

    # === SPLIT DRAWS =========================================================
    # One generator, consumed in a fixed order: the N_SPLITS random splits first,
    # then the N_SPLITS domain-stratified splits. The bootstrap uses SEED + 1.
    rng = np.random.default_rng(SEED)
    random_splits = []
    for _ in range(N_SPLITS):
        perm = rng.permutation(len(tasks))
        random_splits.append((perm[:20].tolist(), perm[20:].tolist()))

    domain_cols = collections.defaultdict(list)
    for j, task in enumerate(tasks):
        domain_cols[domain_of[task]].append(j)
    strat_splits = []
    for _ in range(N_SPLITS):
        a, b = [], []
        for _domain, cols in domain_cols.items():
            perm = rng.permutation(len(cols))
            a += [cols[i] for i in perm[:4]]
            b += [cols[i] for i in perm[4:]]
        strat_splits.append((a, b))

    # === SPLIT-HALF STABILITY ================================================
    def run_splits(split_list):
        out = {}
        for key in METRIC_KEYS:
            rho, exact, top, bottom, undefined = [], 0, 0, 0, 0
            for cols_a, cols_b in split_list:
                a = score_vector(cells, key, cols_a)
                b = score_vector(cells, key, cols_b)
                if np.isnan(a).any() or np.isnan(b).any():
                    undefined += 1
                    continue
                rho.append(spearmanr(a, b).statistic)
                exact += int((ranks(a) == ranks(b)).all())
                top += int(np.argmax(a) == np.argmax(b))
                bottom += int(np.argmin(a) == np.argmin(b))
            r = np.array(rho)
            n = len(r)
            out[key] = {
                "n_usable": n, "n_undefined": undefined,
                "mean_rho": r.mean(), "median_rho": np.median(r),
                "p05_rho": np.percentile(r, 5), "p25_rho": np.percentile(r, 25),
                "p75_rho": np.percentile(r, 75), "min_rho": r.min(),
                "share_rho_eq_1": (r == 1).mean(),
                "share_rho_ge_0.8": (r >= 0.8).mean(),
                "share_rho_le_0": (r <= 0).mean(),
                "share_full_order_preserved": exact / n,
                "share_top_model_same": top / n,
                "share_bottom_model_same": bottom / n,
            }
        return out

    for label, split_list, json_key in (
        ("RANDOM 20/20", random_splits, "splithalf_random"),
        ("DOMAIN-STRATIFIED 20/20, 4 tasks per domain", strat_splits, "splithalf_stratified"),
    ):
        res = run_splits(split_list)
        results[json_key] = to_py(res)
        print("\n" + "=" * 78)
        print(f"SPLIT-HALF STABILITY, {label}, {N_SPLITS} splits, seed {SEED}")
        print("=" * 78)
        print(f"{'metric':<16}{'mean rho':>10}{'median':>9}{'p05':>8}{'min':>8}"
              f"{'rho=1':>8}{'rho>=.8':>9}{'rho<=0':>8}{'order':>8}{'top1':>7}{'bot1':>7}{'undef':>7}")
        for key in METRIC_KEYS:
            v = res[key]
            print(f"{key:<16}{v['mean_rho']:>10.3f}{v['median_rho']:>9.3f}{v['p05_rho']:>8.3f}"
                  f"{v['min_rho']:>8.3f}{v['share_rho_eq_1']:>8.1%}{v['share_rho_ge_0.8']:>9.1%}"
                  f"{v['share_rho_le_0']:>8.1%}{v['share_full_order_preserved']:>8.1%}"
                  f"{v['share_top_model_same']:>7.1%}{v['share_bottom_model_same']:>7.1%}"
                  f"{v['n_undefined']:>7d}")

    # === ADJACENT-PAIR INVERSIONS ============================================
    # Where a ranking is unstable, it is unstable at one pair. This locates it.
    print("\n" + "=" * 78)
    print(f"ADJACENT-PAIR INVERSION RATE IN A 20-TASK HALF, {N_SPLITS} random splits")
    print("=" * 78)
    results["adjacent_inversions"] = {}
    for key in METRIC_KEYS:
        order = list(np.argsort(full[key], kind="stable"))
        inverted = collections.Counter()
        n = 0
        for cols_a, cols_b in random_splits:
            for cols in (cols_a, cols_b):
                v = score_vector(cells, key, cols)
                if np.isnan(v).any():
                    continue
                n += 1
                for j in range(len(models) - 1):
                    lo, hi = order[j], order[j + 1]
                    if v[lo] > v[hi]:
                        inverted[(lo, hi)] += 1
        rows = []
        for j in range(len(models) - 1):
            lo, hi = order[j], order[j + 1]
            rows.append({"lower": models[lo], "higher": models[hi],
                         "gap": full[key][hi] - full[key][lo],
                         "share_inverted": inverted[(lo, hi)] / n})
        results["adjacent_inversions"][key] = to_py(rows)
        print(f"\n  {key}")
        for r in rows:
            print(f"    {r['lower']:<17} vs {r['higher']:<17} gap={r['gap']:>9.4f}"
                  f"  inverted in {r['share_inverted']:6.1%} of halves")

    # === A 20-TASK HALF AGAINST THE FULL-40 ORDERING =========================
    print("\n" + "=" * 78)
    print("AGREEMENT OF A SINGLE 20-TASK HALF WITH THE FULL-40 ORDERING")
    print("=" * 78)
    print(f"{'metric':<16}{'mean rho vs full':>18}{'order':>8}{'top1':>7}{'bot1':>7}")
    results["half_vs_full"] = {}
    for key in METRIC_KEYS:
        full_rank = ranks(full[key])
        rho, exact, top, bottom, n = [], 0, 0, 0, 0
        for cols_a, cols_b in random_splits:
            for cols in (cols_a, cols_b):
                v = score_vector(cells, key, cols)
                if np.isnan(v).any():
                    continue
                n += 1
                rho.append(spearmanr(v, full[key]).statistic)
                exact += int((ranks(v) == full_rank).all())
                top += int(np.argmax(v) == np.argmax(full[key]))
                bottom += int(np.argmin(v) == np.argmin(full[key]))
        row = {"mean_rho_vs_full": float(np.mean(rho)), "share_full_order_preserved": exact / n,
               "share_top_model_same": top / n, "share_bottom_model_same": bottom / n,
               "n_usable_halves": n}
        results["half_vs_full"][key] = to_py(row)
        print(f"{key:<16}{row['mean_rho_vs_full']:>18.3f}{row['share_full_order_preserved']:>8.1%}"
              f"{row['share_top_model_same']:>7.1%}{row['share_bottom_model_same']:>7.1%}")

    # === TASK BOOTSTRAP AT FULL SIZE =========================================
    # Split-half asks what a 20-task benchmark does. This asks what the 40-task
    # benchmark does, by resampling the 40 tasks with replacement.
    rng_boot = np.random.default_rng(SEED + 1)
    boot_cols = [rng_boot.integers(0, len(tasks), len(tasks)).tolist() for _ in range(N_BOOT)]
    print("\n" + "=" * 78)
    print(f"TASK BOOTSTRAP AT FULL SIZE, {N_BOOT} draws of 40 tasks with replacement, seed {SEED + 1}")
    print("=" * 78)
    results["task_bootstrap"] = {}
    for key in METRIC_KEYS:
        drawn = np.array([score_vector(cells, key, cols) for cols in boot_cols])
        drawn = drawn[~np.isnan(drawn).any(axis=1)]
        full_rank = ranks(full[key])
        row = {
            "n_usable_draws": int(len(drawn)),
            "share_full_order_preserved": float(np.mean([(ranks(v) == full_rank).all() for v in drawn])),
            "share_top_model_same": float(np.mean([np.argmax(v) == np.argmax(full[key]) for v in drawn])),
            "share_bottom_model_same": float(np.mean([np.argmin(v) == np.argmin(full[key]) for v in drawn])),
            "ci95": {m: [float(np.percentile(drawn[:, i], 2.5)),
                         float(np.percentile(drawn[:, i], 97.5))]
                     for i, m in enumerate(models)},
        }
        results["task_bootstrap"][key] = to_py(row)
        print(f"\n  {key}: full ordering recovered in {row['share_full_order_preserved']:.1%} of draws, "
              f"top model {row['share_top_model_same']:.1%}, bottom model {row['share_bottom_model_same']:.1%}")
        print("    95% CI: " + ", ".join(f"{m[:12]} [{lo:.3f}, {hi:.3f}]"
                                         for m, (lo, hi) in row["ci95"].items()))

    # === GENERALIZABILITY DECOMPOSITION ======================================
    # Two-way, models x tasks, one observation per cell (3 runs pooled).
    # G = s2_model / (s2_model + s2_resid / k) is the expected squared correlation
    # between the ranking from k tasks and the ranking from the universe of tasks.
    print("\n" + "=" * 78)
    print("VARIANCE DECOMPOSITION OVER TASKS, AND THE NUMBER OF TASKS EACH SCORE NEEDS")
    print("=" * 78)
    results["generalizability"] = {}
    for key in CORE_KEYS:
        matrix = cell_matrix(cells, key)
        usable = ~np.isnan(matrix).any(axis=0)
        matrix = matrix[:, usable]
        n_models, k = matrix.shape
        grand = matrix.mean()
        row_means = matrix.mean(axis=1, keepdims=True)
        col_means = matrix.mean(axis=0, keepdims=True)
        ms_model = (k * ((row_means - grand) ** 2).sum()) / (n_models - 1)
        ms_task = (n_models * ((col_means - grand) ** 2).sum()) / (k - 1)
        ms_resid = ((matrix - row_means - col_means + grand) ** 2).sum() / ((n_models - 1) * (k - 1))
        s2_model = max((ms_model - ms_resid) / k, 0.0)
        s2_task = max((ms_task - ms_resid) / n_models, 0.0)
        s2_resid = ms_resid
        g_of = lambda kk: (s2_model / (s2_model + s2_resid / kk)) if s2_model > 0 else 0.0
        needed = {f"G={t:.2f}": (int(np.ceil(s2_resid / s2_model * t / (1 - t))) if s2_model > 0 else None)
                  for t in (0.80, 0.90, 0.95)}
        row = {"k_usable_tasks": int(k), "var_between_models": float(s2_model),
               "var_between_tasks": float(s2_task), "var_model_x_task": float(s2_resid),
               "G_at_k": {str(kk): g_of(kk) for kk in (5, 10, 20, 40, 80)},
               "G_at_k_usable": g_of(k), "tasks_needed": needed}
        results["generalizability"][key] = to_py(row)
        print(f"\n  {key}  (k = {k} usable tasks)")
        print(f"    between models {s2_model:.5f}   between tasks {s2_task:.5f}   "
              f"model x task {s2_resid:.5f}")
        print(f"    G at k={k}: {g_of(k):.3f}   " +
              "  ".join(f"k={kk}: {g_of(kk):.3f}" for kk in (5, 10, 20, 40, 80)))
        print("    tasks needed: " + ", ".join(f"{t} -> {v}" for t, v in needed.items()))

    # === DO THE CANDIDATE SCORES AGREE WITH EACH OTHER? ======================
    print("\n" + "=" * 78)
    print("SPEARMAN AMONG THE FULL-40 MODEL SCORES, TURN-1 QUALITY INCLUDED")
    print("=" * 78)
    cross_keys = ["genuine_rate", "left_alone_str", "tax", "locf_delta_str",
                  "raw_delta_str", "mean_chg_str", "t1_str"]
    cross = np.column_stack([score_vector(cells, k, all_cols) for k in cross_keys])
    matrix = {}
    print(f"{'':<16}" + "".join(f"{k[:13]:>15}" for k in cross_keys))
    for a, key_a in enumerate(cross_keys):
        row = [float(spearmanr(cross[:, a], cross[:, b]).statistic) for b in range(len(cross_keys))]
        matrix[key_a] = dict(zip(cross_keys, row))
        print(f"{key_a[:15]:<16}" + "".join(f"{v:>15.3f}" for v in row))
    results["cross_metric_spearman"] = to_py(matrix)
    results["full40_turn1_quality"] = to_py(dict(zip(models, score_vector(cells, "t1_str", all_cols))))

    # === MODEL-SUBSET STABILITY ==============================================
    # Whether the split-half result depends on the two outlying models.
    print("\n" + "=" * 78)
    print("SPLIT-HALF STABILITY ON MODEL SUBSETS: CAN THE SCORE SEPARATE SIMILAR MODELS?")
    print("=" * 78)
    subsets = {
        "all 6": models,
        "drop llama-3.3-70b (5)": [m for m in models if m != "llama-3.3-70b"],
        "drop llama and gemini (4)": [m for m in models
                                      if m not in ("llama-3.3-70b", "gemini-2.5-flash")],
    }
    results["model_subsets"] = {}
    for key in CORE_KEYS:
        results["model_subsets"][key] = {}
        print(f"\n  {key}")
        for name, subset in subsets.items():
            idx = [models.index(m) for m in subset]
            rho, exact, n = [], 0, 0
            for cols_a, cols_b in random_splits:
                a = score_vector(cells, key, cols_a)[idx]
                b = score_vector(cells, key, cols_b)[idx]
                if np.isnan(a).any() or np.isnan(b).any():
                    continue
                n += 1
                rho.append(spearmanr(a, b).statistic)
                exact += int((ranks(a) == ranks(b)).all())
            r = np.array(rho)
            row = {"models": subset, "mean_rho": float(r.mean()),
                   "median_rho": float(np.median(r)),
                   "share_full_order_preserved": exact / n, "n_usable": n}
            results["model_subsets"][key][name] = to_py(row)
            print(f"    {name:<28} mean rho={row['mean_rho']:.3f}  "
                  f"median={row['median_rho']:.3f}  order preserved={row['share_full_order_preserved']:5.1%}")

    # === RUN-TO-RUN STABILITY ================================================
    # A second noise axis: generation at temperature 1.0. Each run is a complete
    # 40-task benchmark on its own.
    run_cells = {}
    for run in (1, 2, 3):
        sub = {tid: m for tid, m in trials.items() if m["run"] == run}
        run_cells[run] = build_cells(sub, labels, unstripped, stripped, models, tasks)
    print("\n" + "=" * 78)
    print("RUN-TO-RUN STABILITY: EACH RUN IS A 40-TASK BENCHMARK SCORED ONCE")
    print("=" * 78)
    results["run_to_run"] = {}
    for key in CORE_KEYS:
        per_run = {run: score_vector(run_cells[run], key, all_cols) for run in (1, 2, 3)}
        pairs = {}
        for a, b in itertools.combinations((1, 2, 3), 2):
            pairs[f"run{a} vs run{b}"] = {
                "rho": float(spearmanr(per_run[a], per_run[b]).statistic),
                "order_preserved": bool((ranks(per_run[a]) == ranks(per_run[b])).all()),
            }
        results["run_to_run"][key] = to_py({
            "scores": {f"run{r}": dict(zip(models, per_run[r])) for r in (1, 2, 3)},
            "pairs": pairs})
        print(f"\n  {key}")
        for r in (1, 2, 3):
            print(f"    run{r}: " + "  ".join(f"{models[i][:12]}={per_run[r][i]:.3f}"
                                              for i in range(len(models))))
        for name, v in pairs.items():
            print(f"    {name}: rho={v['rho']:.3f}  order preserved={v['order_preserved']}")

    # === CELL SIZES ==========================================================
    print("\n" + "=" * 78)
    print("CELL SIZES")
    print("=" * 78)
    domains = sorted({d for d in domain_of.values()})
    t5_by_model = cells["t5_gen"].sum(axis=1)
    bal_by_model = cells["bal"].sum(axis=1)
    rds_den = cells["rds_str_den"]

    t5_model_domain = np.zeros((len(models), len(domains)), dtype=int)
    for j, task in enumerate(tasks):
        d = domains.index(domain_of[task])
        t5_model_domain[:, d] += cells["t5_gen"][:, j]
    zero_den = [(models[i], tasks[j]) for i in range(len(models))
                for j in range(len(tasks)) if rds_den[i, j] == 0]
    empty_t5_cells = int((cells["t5_gen"] == 0).sum())

    print("Per model x task: 3 trials, 12 post-turn-1 turns. Per model x domain: 24 trials.")
    print("Per task across all models: 18 trials.")
    print("\nTurn-5 genuine trials by domain (denominator 144 trials per domain):")
    for d_i, d in enumerate(domains):
        print(f"  {d:<12}{t5_model_domain[:, d_i].sum():>4} / 144")
    print("\nTurn-5 genuine trials per model x domain (denominator 24):")
    print(f"{'model':<18}" + "".join(f"{d:>12}" for d in domains))
    for i, m in enumerate(models):
        print(f"{m:<18}" + "".join(f"{t5_model_domain[i, d_i]:>12}" for d_i in range(len(domains))))
    print("\nBy model: balanced-panel trials, turn-5 genuine trials, sufficient-turn denominator:")
    print(f"{'model':<18}{'balanced/120':>14}{'T5 genuine/120':>16}{'suff turns':>12}"
          f"{'min cell':>10}{'cells <3':>10}")
    for i, m in enumerate(models):
        print(f"{m:<18}{bal_by_model[i]:>14}{t5_by_model[i]:>16}{rds_den[i].sum():>12}"
              f"{rds_den[i].min():>10}{int((rds_den[i] < 3).sum()):>10}")
    print(f"\nModel x task cells with zero turn-5 genuine trials: {empty_t5_cells} of "
          f"{len(models) * len(tasks)}")
    print(f"Model x task cells with a zero sufficient-turn denominator: {len(zero_den)} of "
          f"{len(models) * len(tasks)}")
    for m, t in zero_den:
        print(f"  {m}  {t}  ({domain_of[t]})")

    results["cell_sizes"] = to_py({
        "trials_per_model_task": 3,
        "post_t1_turns_per_model_task": 12,
        "trials_per_model_domain": 24,
        "trials_per_task_all_models": 18,
        "t5_genuine_by_domain": {d: int(t5_model_domain[:, i].sum()) for i, d in enumerate(domains)},
        "t5_genuine_by_model_domain": {m: {d: int(t5_model_domain[i, j])
                                           for j, d in enumerate(domains)}
                                       for i, m in enumerate(models)},
        "balanced_panel_by_model": dict(zip(models, bal_by_model)),
        "t5_genuine_by_model": dict(zip(models, t5_by_model)),
        "sufficient_turn_denominator_by_model": {
            m: {"total": int(rds_den[i].sum()), "min_cell": int(rds_den[i].min()),
                "median_cell": float(np.median(rds_den[i])), "max_cell": int(rds_den[i].max()),
                "cells_under_3": int((rds_den[i] < 3).sum())}
            for i, m in enumerate(models)},
        "model_task_cells_with_no_t5_genuine": empty_t5_cells,
        "model_task_cells_with_zero_sufficient_turns":
            [{"model": m, "task": t, "domain": domain_of[t]} for m, t in zero_den],
    })

    # === WRITE ===============================================================
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w") as fh:
        json.dump(results, fh, indent=2)
    print(f"\nwrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
