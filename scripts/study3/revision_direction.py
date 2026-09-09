"""
Direction of genuine revisions: does a revision lower, leave, or raise quality?

Descriptive analysis on the study's defined sample. No specification change and no
sample change: the same 720 trials, the same GENUINE/META labels from the validated
classifier, and the same level-6 -> 2 recode used throughout results_FINAL.md.

Comparison basis. Each genuine revision at turn t is compared against the score of the
most recent turn whose content was genuinely new: turn 1, or the last turn labelled
GENUINE. Comparing against turn t-1 directly would score a revision against a
meta-response, whose text is a restatement rather than a distinct draft.

Reported on both stripped and unstripped scores; stripped is primary, matching the
convention in results_FINAL.md.

Outputs data/study3/analysis/revision_direction.json and prints every table.
"""
import json, collections, statistics
from scipy import stats

RAW = "data/study3/raw_responses/"
OUT = "data/study3/analysis/revision_direction.json"
recode = lambda level: 2 if level == 6 else level


def load():
    unstripped, stripped, trial_meta = {}, {}, {}
    for line in open(RAW + "evaluator_results.jsonl"):
        r = json.loads(line)
        unstripped[(r["worker_trial_id"], r["turn"])] = recode(r["level"])
    for line in open(RAW + "stripped_rescore_full.jsonl"):
        r = json.loads(line)
        stripped[(r["trial_id"], r["turn"])] = recode(r["stripped_score"])
        trial_meta[r["trial_id"]] = (r["model"], r["domain"])
    labels = {}
    for line in open(RAW + "genuine_meta_labels.jsonl"):
        r = json.loads(line)
        labels[(r["trial_id"], r["turn"])] = r["classifier_label"]
    return unstripped, stripped, trial_meta, labels


def classify(scores, labels, trials):
    """Yield (trial_id, turn, direction) for every genuine revision."""
    for trial in trials:
        last_genuine = 1
        for turn in (2, 3, 4, 5):
            if labels.get((trial, turn)) != "GENUINE":
                continue
            current = scores.get((trial, turn))
            previous = scores.get((trial, last_genuine))
            if current is not None and previous is not None:
                yield trial, turn, ("worse" if current < previous
                                    else "same" if current == previous else "better")
            last_genuine = turn


def magnitudes(scores, labels, trials):
    """Signed level change for every genuine revision, for magnitude reporting."""
    out = []
    for trial in trials:
        last_genuine = 1
        for turn in (2, 3, 4, 5):
            if labels.get((trial, turn)) != "GENUINE":
                continue
            cur, prev = scores.get((trial, turn)), scores.get((trial, last_genuine))
            if cur is not None and prev is not None:
                out.append(cur - prev)
            last_genuine = turn
    return out


def split(counter):
    n = sum(counter.values())
    worse, better = counter["worse"], counter["better"]
    movers = worse + better
    out = {"n": n, "worse": worse, "same": counter["same"], "better": better,
           "movers": movers}
    if movers:
        test = stats.binomtest(worse, movers, 0.5, alternative="greater")
        lo, hi = stats.binomtest(worse, movers, 0.5).proportion_ci(method="exact")
        out |= {"share_worse_of_movers": worse / movers, "sign_p": test.pvalue,
                "ci_low": lo, "ci_high": hi}
    return out


def main():
    unstripped, stripped, trial_meta, labels = load()
    trials = sorted({t for t, _ in labels})
    results = {"n_trials": len(trials)}

    for basis_name, scores in (("stripped", stripped), ("unstripped", unstripped)):
        overall = collections.Counter()
        by_model = collections.defaultdict(collections.Counter)
        by_domain = collections.defaultdict(collections.Counter)
        for trial, _, direction in classify(scores, labels, trials):
            model, domain = trial_meta[trial]
            overall[direction] += 1
            by_model[model][direction] += 1
            by_domain[domain][direction] += 1

        domains = sorted(by_domain)
        chi2, chi_p, dof, _ = stats.chi2_contingency(
            [[by_domain[d]["worse"], by_domain[d]["better"]] for d in domains])
        objective = [sum(by_domain[d][k] for d in ("code", "data_logic"))
                     for k in ("worse", "better")]
        subjective = [sum(by_domain[d][k] for d in ("creative", "writing"))
                      for k in ("worse", "better")]

        # trial-level turn 1 vs turn 5 on the balanced panel
        balanced = [t for t in trials
                    if all(labels.get((t, k)) == "GENUINE" for k in (2, 3, 4, 5))]
        panel = collections.Counter()
        for t in balanced:
            first, last = scores.get((t, 1)), scores.get((t, 5))
            if first is not None and last is not None:
                panel["worse" if last < first else "same" if last == first else "better"] += 1

        deltas = magnitudes(scores, labels, trials)
        down = [d for d in deltas if d < 0]
        up = [d for d in deltas if d > 0]
        results[basis_name] = {
            "magnitude": {
                "mean_change_all_revisions": sum(deltas) / len(deltas),
                "mean_drop_when_down": sum(down) / len(down),
                "median_drop_when_down": statistics.median(down),
                "mean_rise_when_up": sum(up) / len(up),
                "drop_of_one_level": sum(1 for d in down if d == -1),
                "drop_of_two_or_more": sum(1 for d in down if d <= -2),
                "n_down": len(down), "n_up": len(up), "n_all": len(deltas),
            },
            "overall": split(overall),
            "by_model": {m: split(c) for m, c in by_model.items()},
            "by_domain": {d: split(c) for d, c in by_domain.items()},
            "domain_homogeneity_chi2": {"chi2": chi2, "dof": dof, "p": chi_p},
            "objective_vs_subjective": {
                "objective_worse_better": objective,
                "subjective_worse_better": subjective,
                "fisher_p": stats.fisher_exact([objective, subjective])[1]},
            "balanced_panel_t1_vs_t5": split(panel) | {"n_trials": len(balanced)},
        }

    with open(OUT, "w") as fh:
        json.dump(results, fh, indent=2)

    for basis in ("stripped", "unstripped"):
        r = results[basis]
        o = r["overall"]
        print(f"\n{'='*72}\n{basis.upper()}  (n={o['n']} genuine revisions)")
        print(f"  worse {o['worse']} ({o['worse']/o['n']:.1%})   "
              f"same {o['same']} ({o['same']/o['n']:.1%})   "
              f"better {o['better']} ({o['better']/o['n']:.1%})")
        print(f"  among the {o['movers']} that move quality: {o['share_worse_of_movers']:.1%} move down"
              f"  95% CI [{o['ci_low']:.1%}, {o['ci_high']:.1%}]  sign p={o['sign_p']:.3g}")
        for label, key in (("model", "by_model"), ("domain", "by_domain")):
            print(f"\n  by {label}:")
            print(f"    {label:<18}{'n':>5}{'worse':>8}{'same':>8}{'better':>8}{'%down of movers':>17}{'p':>10}")
            for k, v in sorted(r[key].items(), key=lambda kv: -kv[1].get("share_worse_of_movers", 0)):
                print(f"    {k:<18}{v['n']:>5}{v['worse']/v['n']:>8.1%}{v['same']/v['n']:>8.1%}"
                      f"{v['better']/v['n']:>8.1%}{v.get('share_worse_of_movers',float('nan')):>17.1%}"
                      f"{v.get('sign_p',float('nan')):>10.2g}")
        c = r["domain_homogeneity_chi2"]
        ov = r["objective_vs_subjective"]
        print(f"\n  domains homogeneous? chi2={c['chi2']:.2f} dof={c['dof']} p={c['p']:.3f}")
        print(f"  objective {ov['objective_worse_better']} vs subjective "
              f"{ov['subjective_worse_better']}: Fisher p={ov['fisher_p']:.4f}")
        p = r["balanced_panel_t1_vs_t5"]
        print(f"  balanced panel T1 vs T5 (n={p['n_trials']}): worse {p['worse']/p['n']:.1%} "
              f"same {p['same']/p['n']:.1%} better {p['better']/p['n']:.1%}; "
              f"movers {p['worse']}/{p['better']}, p={p['sign_p']:.3g}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
