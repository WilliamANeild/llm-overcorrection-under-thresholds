"""Reproduces the sourcing for paper grounding flags a1-a6 (see paper/SKELETON.md).
Run from repo root: python scripts/study3/verify_grounding_flags.py
a1,a3,a4,a5 recompute exactly; a2 prints authoritative judge values; a6 points to results_FINAL.md S7.
"""
import json, csv
from collections import defaultdict
from scipy.stats import wilcoxon, chi2_contingency

RR = "data/study3/raw_responses/"
def load_jsonl(p): return [json.loads(l) for l in open(p) if l.strip()]

label = defaultdict(dict)
for r in load_jsonl(RR+"genuine_meta_labels.jsonl"):
    label[r["trial_id"]][int(r["turn"])] = r["classifier_label"]
strip = defaultdict(dict)
for r in load_jsonl(RR+"stripped_rescore_full.jsonl"):
    strip[r["trial_id"]][int(r["turn"])] = int(r["stripped_score"])
trials = {r["trial_id"]: r for r in load_jsonl(RR+"worker_trials.jsonl")}
model_of = {t: trials[t]["model"] for t in trials}
domain_of = {t: trials[t]["domain"] for t in trials}
POST = [2, 3, 4, 5]

def counts(pred_key):
    agg = defaultdict(lambda: [0, 0])  # key -> [genuine, total]
    for t in trials:
        k = pred_key(t)
        for turn in POST:
            lab = label.get(t, {}).get(turn)
            if lab is None: continue
            agg[k][1] += 1
            if lab == "GENUINE": agg[k][0] += 1
    return agg

print("### a1: per-model META rate over post-T1 observations")
for m, (g, n) in sorted(counts(lambda t: model_of[t]).items()):
    print(f"  {m:16} META {n-g}/{n} = {100*(n-g)/n:.1f}%")

print("\n### a5: genuine-revision rate per model / domain + chi2")
mc = counts(lambda t: model_of[t]); dc = counts(lambda t: domain_of[t])
mv = {m: 100*g/n for m,(g,n) in mc.items()}; dv = {d: 100*g/n for d,(g,n) in dc.items()}
print(f"  model range = {max(mv.values()):.1f} - {min(mv.values()):.1f} = {max(mv.values())-min(mv.values()):.1f} pp")
print(f"  domain range = {max(dv.values()):.1f} - {min(dv.values()):.1f} = {max(dv.values())-min(dv.values()):.1f} pp")
print(f"  code = {dv['code']:.1f}%  " + " ".join(f"{d}={dv[d]:.1f}%" for d in dv if d!='code'))
chi2, p, dof, _ = chi2_contingency([[dc[d][0], dc[d][1]-dc[d][0]] for d in sorted(dc)])
print(f"  5x2 domain chi2={chi2:.2f} df={dof} p={p:.2e}")

print("\n### a4: per-domain paired Wilcoxon (GENUINE at T5, stripped T1 vs T5)")
for dom in sorted(set(domain_of.values())):
    t1=[]; t5=[]
    for t in trials:
        if domain_of[t]==dom and label.get(t,{}).get(5)=="GENUINE" and 1 in strip[t] and 5 in strip[t]:
            t1.append(strip[t][1]); t5.append(strip[t][5])
    n=len(t1); d=(sum(t5)-sum(t1))/n if n else 0
    try: _,pp = wilcoxon(t1,t5); ps=f"{pp:.3f}"
    except Exception as e: ps=str(e)
    print(f"  {dom:12} n(T5)={n:2} Δ={d:+.2f} p={ps}")

print("\n### a3: Study-1 probe rates (data/analysis/summary_by_probe_type.csv)")
for row in csv.DictReader(open("data/analysis/summary_by_probe_type.csv")):
    rev = 100 - float(row["gate_decline_pct"])
    print(f"  {row['probe_type']:9} n={row['n']:>4} revision={rev:.1f}% (decline {row['gate_decline_pct']}%)")

print("\n### a2: authoritative judge calibration (selected_judge.json)")
sj = json.load(open(RR+"selected_judge.json"))["all_results"]
for m, v in sorted(sj.items(), key=lambda kv: -kv[1]["spearman_r"]):
    print(f"  {m:16} r={v['spearman_r']:+.3f} QWk={v['qw_kappa']:+.3f} (n={v['n']})")

print("\n### a6: enterprise projection -> results_FINAL.md S7 ($323-$65,678/yr per 500-person org)")
