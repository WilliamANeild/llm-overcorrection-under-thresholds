import json,re,sys
sys.path.insert(0,'.workspace/scratch')
from pathlib import Path
from collections import defaultdict
exec(open('.workspace/scratch/meta_commentary_extra_analysis2.py').read().split('rescore=[json.loads')[0])
D=Path("data/study3/raw_responses")
rescore=[json.loads(l) for l in open(D/"stripped_rescore_full.jsonl")]
labels={(r["trial_id"],r["turn"]):r["classifier_label"] for r in map(json.loads,open(D/"genuine_meta_labels.jsonl"))}
trials={t["trial_id"]:t for t in map(json.loads,open(D/"worker_trials.jsonl"))}
for r in rescore:
    r["text"]=trials[r["trial_id"]]["responses"][r["turn"]-1]; r["label"]=labels.get((r["trial_id"],r["turn"]))
PM=[re.compile(p) for p in PREAMBLE_META]; QM=[re.compile(p) for p in POSTAMBLE_META]
def dB(t,w1=300,w2=400): return any(x.search(t[:w1].lower()) for x in PM) or any(x.search(t[-w2:].lower()) for x in QM)
def dfull(t): return any(x.search(t.lower()) for x in PM) or any(x.search(t.lower()) for x in QM)
TARGET=[14,92,85,79,68]
def rpt(n,s): print(f"  {n:<56} {['%5.1f'%x for x in s]} match={'YES' if [round(x) for x in s]==TARGET else 'no'}")
def rate(rows,f): return 100*sum(1 for r in rows if f(r))/len(rows) if rows else float('nan')
bp={tid for tid in trials if all(labels.get((tid,t))=="GENUINE" for t in (2,3,4,5))}
cases={
 "all 3600, strip-patterns DETECT (300/400)": (lambda t:[r for r in rescore if r["turn"]==t], lambda r: dB(r["text"])),
 "GENUINE-only, strip-patterns DETECT (300/400)": (lambda t:[r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")], lambda r: dB(r["text"])),
 "all 3600, strip-patterns DETECT (whole text)": (lambda t:[r for r in rescore if r["turn"]==t], lambda r: dfull(r["text"])),
 "GENUINE-only, strip-patterns DETECT (whole text)": (lambda t:[r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")], lambda r: dfull(r["text"])),
 "all 3600, audit DETECT whole text": (lambda t:[r for r in rescore if r["turn"]==t], lambda r: any(x.search(r["text"].lower()) for x in PRE_A+POST_A)),
 "bal-panel 50, strip-patterns DETECT": (lambda t:[r for r in rescore if r["trial_id"] in bp and r["turn"]==t], lambda r: dB(r["text"])),
}
print("EXTRA SCOPE SWEEP")
for n,(sel,f) in cases.items(): rpt(n,[rate(sel(t),f) for t in range(1,6)])
# 50 pairs with strip-patterns
pairs=json.load(open(D/"reversibility_human_pairs.json")); key={k["pair_id"]:k for k in json.load(open(D/"reversibility_human_key.json"))}
t1s=[];byt=defaultdict(list)
for p in pairs:
    k=key[p["pair_id"]]
    t1s.append(p["output_A"] if k["A_is"]=="T1" else p["output_B"])
    byt[k["last_rev_turn"]].append(p["output_B"] if k["A_is"]=="T1" else p["output_A"])
rpt("50 pairs, strip-patterns DETECT",[100*sum(1 for x in t1s if dB(x))/50]+[100*sum(1 for x in byt[t] if dB(x))/len(byt[t]) for t in range(2,6)])
