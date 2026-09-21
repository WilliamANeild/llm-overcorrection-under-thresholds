#!/usr/bin/env python3
"""Descriptive analysis of the meta-commentary stripping pass (Study 3).

Read-only. Writes nothing but stdout. Uses the ledger's own definitions:
  - 6->2 recode: stripped_rescore_full.jsonl already carries recoded orig_score /
    stripped_score alongside raw levels (orig_level_raw / stripped_level_raw).
  - GENUINE/META: genuine_meta_labels.jsonl field `classifier_label`, turns 2-5.

Two distinct meta measures are kept separate throughout:
  STRIP  = chars_removed > 0 in stripped_rescore_full.jsonl (paragraph-level strip
           with CONTENT_SIGNALS veto; the pass that produced the rescore).
  DETECT = audit_meta_commentary.py regexes searched in first 300 / last 400 chars
           (the pass behind the 84% vs 14% wrapping asymmetry). Patterns copied
           verbatim below; strip_meta_commentary.py is never imported.
"""
import json, re, statistics as st
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(str(Path(__file__).resolve().parents[2]))
D = ROOT / "data" / "study3" / "raw_responses"

# ---- DETECT patterns (verbatim from scripts/study3/audit_meta_commentary.py) ----
PREAMBLE_PATTERNS = [
    r"(?:i'?d like to|let me|i'?ll|i want to)\s+(?:revise|make|take|offer|give|try)",
    r"here'?s (?:the|my|a|an) (?:revised|improved|updated|final|slightly|new)",
    r"(?:sure|okay|alright|absolutely)[,!.]?\s+here",
    r"i think (?:i can|we can|it could|there)",
    r"(?:looking|look) (?:back|at (?:it|this|my))",
    r"(?:after|upon) review",
    r"(?:i've|i have) reviewed",
    r"thank(?:s| you) for (?:the|asking|checking|your)",
    r"(?:great|good) question",
    r"actually,? let me",
    r"(?:i'?d like to|i want to) (?:keep|confirm|make)",
    r"considering the response",
    r"(?:this is a )?(?:very )?(?:solid|strong|great|good) (?:implementation|version|set|start|draft)",
    r"you'?re right to ask",
    r"since you(?:'re| are| repeated)",
    r"(?:i can|let me) make (?:some|a few|one|minor)",
    r"(?:the|this) (?:version|script|function|code|email|post|analysis|response) (?:is|can be|could be)",
    r"however,? (?:i|during|to make)",
    r"(?:after|upon) re-?reading",
]
POSTAMBLE_PATTERNS = [
    r"let me know (?:if|what|how)", r"hope this helps", r"feel free to",
    r"(?:happy|glad) to (?:help|assist|revise|adjust|make)",
    r"(?:if you'?d like|would you like) (?:any|me to|further|more)",
    r"(?:i'?m|we'?re) (?:here|available|happy) (?:to|if)",
    r"(?:just )?let me know",
    r"(?:what do you think|how does (?:this|that) (?:sound|look|work))",
    r"(?:otherwise|if not),? (?:this|it|we)",
    r"(?:i believe|i think|i'?m confident) (?:this|it|the) (?:version|is|meets|works|feels)",
    r"(?:no )?further (?:changes|revisions|adjustments)",
    r"this version (?:feels|is|should)",
    r"(?:ready to|you can) (?:use|go|send|share|present|submit)",
    r"(?:i'?ve|i have) made (?:some|minor|a few)",
    r"(?:do you|would you) (?:want|like|need) (?:me to|any)",
]
PRE_RE = [re.compile(p) for p in PREAMBLE_PATTERNS]
POST_RE = [re.compile(p) for p in POSTAMBLE_PATTERNS]
def has_pre(t): 
    h = t[:300].lower()
    return any(r.search(h) for r in PRE_RE)
def has_post(t):
    h = t[-400:].lower()
    return any(r.search(h) for r in POST_RE)

# ---------------- load ----------------
rescore = [json.loads(l) for l in open(D/"stripped_rescore_full.jsonl")]
labels = {(r["trial_id"], r["turn"]): r["classifier_label"]
          for r in map(json.loads, open(D/"genuine_meta_labels.jsonl"))}
trials = {t["trial_id"]: t for t in map(json.loads, open(D/"worker_trials.jsonl"))}
evalr = {}
for r in map(json.loads, open(D/"evaluator_results.jsonl")):
    evalr[(r["worker_trial_id"], r["turn"])] = r

# attach original text + detect flags
for r in rescore:
    t = trials[r["trial_id"]]
    txt = t["responses"][r["turn"]-1]
    r["text"] = txt
    r["orig_chars"] = len(txt)
    r["pre"] = has_pre(txt)
    r["post"] = has_post(txt)
    r["detect"] = r["pre"] or r["post"]
    r["stripped"] = r["chars_removed"] > 0
    r["share"] = r["chars_removed"]/len(txt) if len(txt) else 0.0
    r["label"] = labels.get((r["trial_id"], r["turn"]))  # None at T1
    r["delta"] = r["stripped_score"] - r["orig_score"]
    tc = t["token_counts"][r["turn"]-1]
    r["out_tokens"] = tc.get("output")

assert len(rescore) == 3600
MODELS = sorted({r["model"] for r in rescore})
DOMAINS = sorted({r["domain"] for r in rescore})

def pcts(xs, ps=(10,25,50,75,90,95,99)):
    if not xs: return {}
    s = sorted(xs)
    out = {}
    for p in ps:
        k = (len(s)-1)*p/100
        lo, hi = int(k), min(int(k)+1, len(s)-1)
        out[p] = s[lo] + (s[hi]-s[lo])*(k-lo)
    return out

def line(*a): print(*a)

SEC = lambda s: print("\n" + "="*78 + "\n" + s + "\n" + "="*78)

# ============ Q0: sanity — does orig_score match evaluator with 6->2 recode ============
SEC("Q0. SANITY CHECKS")
mismatch = 0
for r in rescore:
    e = evalr[(r["trial_id"], r["turn"])]
    rec = 2 if e["level"] == 6 else e["level"]
    if rec != r["orig_score"] or e["level"] != r["orig_level_raw"]:
        mismatch += 1
line(f"orig_score vs evaluator_results 6->2 recode mismatches: {mismatch}/3600")
nchanged = sum(1 for r in rescore if r["stripped"])
nresc = sum(1 for r in rescore if r["was_rescored"])
line(f"chars_removed>0: {nchanged}; was_rescored True: {nresc}")
line(f"rows where was_rescored False but stripped_score != orig_score: "
     f"{sum(1 for r in rescore if not r['was_rescored'] and r['stripped_score']!=r['orig_score'])}")

# ============ Q1: how much text stripping removes ============
SEC("Q1. TEXT REMOVED BY STRIPPING (STRIP measure)")
strips = [r for r in rescore if r["stripped"]]
line(f"All 3,600 outputs: total chars {sum(r['orig_chars'] for r in rescore):,}; "
     f"total removed {sum(r['chars_removed'] for r in rescore):,} "
     f"({sum(r['chars_removed'] for r in rescore)/sum(r['orig_chars'] for r in rescore)*100:.2f}% of corpus)")
line(f"Outputs with any removal: {len(strips)}/3600 ({len(strips)/36:.1f}%)")

def block(rows, name):
    ch = [r["chars_removed"] for r in rows]
    sh = [r["share"]*100 for r in rows]
    p = pcts(ch); q = pcts(sh)
    return (f"{name:<22} n={len(rows):>5}  mean={st.mean(ch):7.1f}  sd={st.pstdev(ch):7.1f}  "
            f"p10={p[10]:6.0f} p25={p[25]:6.0f} med={p[50]:6.0f} p75={p[75]:6.0f} p90={p[90]:6.0f} p99={p[99]:7.0f} max={max(ch):6.0f} | "
            f"share%% mean={st.mean(sh):5.1f} med={q[50]:5.1f} p90={q[90]:5.1f} max={max(sh):5.1f}")

line("\n-- Conditional on being stripped (chars_removed > 0) --")
line(block(strips, "ALL STRIPPED"))
line("\nBy turn:")
for t in range(1,6):
    line("  "+block([r for r in strips if r["turn"]==t], f"T{t}"))
line("\nBy model:")
for m in MODELS:
    line("  "+block([r for r in strips if r["model"]==m], m))
line("\nBy domain:")
for d in DOMAINS:
    line("  "+block([r for r in strips if r["domain"]==d], d))

line("\n-- Unconditional (all 3,600, zeros included): mean chars removed per output --")
for lab, keyf, keys in (("turn", lambda r: r["turn"], list(range(1,6))),
                        ("model", lambda r: r["model"], MODELS),
                        ("domain", lambda r: r["domain"], DOMAINS)):
    line(f"  by {lab}:")
    for k in keys:
        rows = [r for r in rescore if keyf(r)==k]
        ch=[r["chars_removed"] for r in rows]; oc=[r["orig_chars"] for r in rows]
        line(f"    {str(k):<20} n={len(rows):>4} mean_removed={st.mean(ch):7.1f} "
             f"mean_orig_len={st.mean(oc):7.1f} corpus_share={sum(ch)/sum(oc)*100:5.2f}%  strip_rate={sum(1 for r in rows if r['stripped'])/len(rows)*100:5.1f}%")

# turn x model strip rate matrix
line("\n-- Strip rate (%) by model x turn (denominator 120 per cell) --")
line(f"  {'model':<20}" + "".join(f"{'T'+str(t):>8}" for t in range(1,6)) + f"{'all':>8}")
for m in MODELS:
    row=[]
    for t in range(1,6):
        rows=[r for r in rescore if r["model"]==m and r["turn"]==t]
        row.append(sum(1 for r in rows if r["stripped"])/len(rows)*100)
    allr=[r for r in rescore if r["model"]==m]
    line(f"  {m:<20}" + "".join(f"{v:8.1f}" for v in row) + f"{sum(1 for r in allr if r['stripped'])/len(allr)*100:8.1f}")
line("\n-- Strip rate (%) by domain x turn (denominator 144 per cell) --")
line(f"  {'domain':<20}" + "".join(f"{'T'+str(t):>8}" for t in range(1,6)) + f"{'all':>8}")
for d in DOMAINS:
    row=[]
    for t in range(1,6):
        rows=[r for r in rescore if r["domain"]==d and r["turn"]==t]
        row.append(sum(1 for r in rows if r["stripped"])/len(rows)*100)
    allr=[r for r in rescore if r["domain"]==d]
    line(f"  {d:<20}" + "".join(f"{v:8.1f}" for v in row) + f"{sum(1 for r in allr if r['stripped'])/len(allr)*100:8.1f}")

# ============ Q2: prevalence across turns; verify the ledger's per-turn breakdown ============
SEC("Q2. META PREVALENCE BY TURN -- VERIFYING THE LEDGER'S T1:14 T2:92 T3:85 T4:79 T5:68")
line("Candidate scope A: all 3,600 outputs, DETECT measure (audit regexes, 300/400 char windows)")
for t in range(1,6):
    rows=[r for r in rescore if r["turn"]==t]
    line(f"  T{t}: either={sum(r['detect'] for r in rows)/len(rows)*100:5.1f}%  "
         f"pre={sum(r['pre'] for r in rows)/len(rows)*100:5.1f}%  post={sum(r['post'] for r in rows)/len(rows)*100:5.1f}%  n={len(rows)}")
line("\nCandidate scope B: GENUINE-only post-T1 (T1 = all 720), DETECT measure")
for t in range(1,6):
    rows=[r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")]
    line(f"  T{t}: either={sum(r['detect'] for r in rows)/len(rows)*100:5.1f}%  "
         f"pre={sum(r['pre'] for r in rows)/len(rows)*100:5.1f}%  post={sum(r['post'] for r in rows)/len(rows)*100:5.1f}%  n={len(rows)}")
line("\nCandidate scope C: GENUINE-only post-T1 (T1 = all 720), STRIP measure")
for t in range(1,6):
    rows=[r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")]
    line(f"  T{t}: stripped={sum(r['stripped'] for r in rows)/len(rows)*100:5.1f}%  n={len(rows)}")
line("\nCandidate scope D: META-only post-T1, DETECT measure")
for t in range(2,6):
    rows=[r for r in rescore if r["turn"]==t and r["label"]=="META"]
    line(f"  T{t}: either={sum(r['detect'] for r in rows)/len(rows)*100:5.1f}%  n={len(rows)}")

# Scope E: the 50 reversibility pairs
pairs = json.load(open(D/"reversibility_human_pairs.json"))
key = {k["pair_id"]: k for k in json.load(open(D/"reversibility_human_key.json"))}
by_turn_pairs = defaultdict(list)
t1_pairs = []
for p in pairs:
    k = key[p["pair_id"]]
    t1t = p["output_A"] if k["A_is"]=="T1" else p["output_B"]
    rvt = p["output_B"] if k["A_is"]=="T1" else p["output_A"]
    t1_pairs.append(t1t)
    by_turn_pairs[k["last_rev_turn"]].append(rvt)
line("\nCandidate scope E: the 50 reversibility pairs, DETECT measure")
line(f"  T1 side: either={sum(has_pre(x) or has_post(x) for x in t1_pairs)}/{len(t1_pairs)} "
     f"= {sum(has_pre(x) or has_post(x) for x in t1_pairs)/len(t1_pairs)*100:.0f}%")
for t in sorted(by_turn_pairs):
    xs = by_turn_pairs[t]
    line(f"  revision side, last_rev_turn=T{t}: either={sum(has_pre(x) or has_post(x) for x in xs)}/{len(xs)} "
         f"= {sum(has_pre(x) or has_post(x) for x in xs)/len(xs)*100:.0f}%")

# 50 balanced-panel trials (GENUINE at all T2-T5) -- another candidate
bp = [tid for tid in trials if all(labels.get((tid,t))=="GENUINE" for t in (2,3,4,5))]
line(f"\nCandidate scope F: the 50 balanced-panel trials (GENUINE at all T2-T5), n_trials={len(bp)}, DETECT measure")
for t in range(1,6):
    rows=[r for r in rescore if r["trial_id"] in set(bp) and r["turn"]==t]
    line(f"  T{t}: either={sum(r['detect'] for r in rows)}/{len(rows)} = {sum(r['detect'] for r in rows)/len(rows)*100:5.1f}%")
line("\nCandidate scope G: the 50 balanced-panel trials, STRIP measure")
for t in range(1,6):
    rows=[r for r in rescore if r["trial_id"] in set(bp) and r["turn"]==t]
    line(f"  T{t}: stripped={sum(r['stripped'] for r in rows)}/{len(rows)} = {sum(r['stripped'] for r in rows)/len(rows)*100:5.1f}%")

line("\n-- DETECT prevalence by model x turn (all 3,600; 120 per cell) --")
line(f"  {'model':<20}" + "".join(f"{'T'+str(t):>8}" for t in range(1,6)))
for m in MODELS:
    line(f"  {m:<20}" + "".join(f"{sum(r['detect'] for r in rescore if r['model']==m and r['turn']==t)/1.2:8.1f}" for t in range(1,6)))
line("\n-- DETECT prevalence by domain x turn (all 3,600; 144 per cell) --")
line(f"  {'domain':<20}" + "".join(f"{'T'+str(t):>8}" for t in range(1,6)))
for d in DOMAINS:
    line(f"  {d:<20}" + "".join(f"{sum(r['detect'] for r in rescore if r['domain']==d and r['turn']==t)/1.44:8.1f}" for t in range(1,6)))

# ============ Q3: dose-response, amount of meta vs score change ============
SEC("Q3. DOSE-RESPONSE: AMOUNT REMOVED vs SIZE OF SCORE CHANGE")
line("Among rescored rows only (was_rescored True, n={}):".format(nresc))
rs = [r for r in rescore if r["was_rescored"]]
def corr(xs, ys):
    n=len(xs); mx=st.mean(xs); my=st.mean(ys)
    sx=st.pstdev(xs); sy=st.pstdev(ys)
    if sx==0 or sy==0: return float('nan')
    return sum((x-mx)*(y-my) for x,y in zip(xs,ys))/(n*sx*sy)
def spearman(xs, ys):
    def rank(v):
        order=sorted(range(len(v)), key=lambda i: v[i]); r=[0.0]*len(v); i=0
        while i<len(order):
            j=i
            while j+1<len(order) and v[order[j+1]]==v[order[i]]: j+=1
            avg=(i+j)/2+1
            for k in range(i,j+1): r[order[k]]=avg
            i=j+1
        return r
    return corr(rank(xs), rank(ys))
ch=[r["chars_removed"] for r in rs]; sh=[r["share"] for r in rs]; dl=[r["delta"] for r in rs]
line(f"  Pearson r(chars_removed, delta)  = {corr(ch,dl):+.3f}")
line(f"  Spearman rho(chars_removed, delta) = {spearman(ch,dl):+.3f}")
line(f"  Pearson r(share_removed, delta)  = {corr(sh,dl):+.3f}")
line(f"  Spearman rho(share_removed, delta) = {spearman(sh,dl):+.3f}")
line(f"  Pearson r(chars_removed, |delta|) = {corr(ch,[abs(x) for x in dl]):+.3f}")
line(f"  Spearman rho(chars_removed, |delta|) = {spearman(ch,[abs(x) for x in dl]):+.3f}")
line("\n  Quintiles of chars_removed (rescored rows):")
srt = sorted(rs, key=lambda r: r["chars_removed"])
q = len(srt)//5
line(f"    {'quintile':<10}{'n':>5}{'range_chars':>16}{'mean_removed':>14}{'mean_share%':>12}{'mean_delta':>12}{'%delta>0':>10}{'%delta<0':>10}{'%delta=0':>10}")
for i in range(5):
    g = srt[i*q:(i+1)*q] if i<4 else srt[4*q:]
    d=[r["delta"] for r in g]
    line(f"    Q{i+1:<9}{len(g):>5}{f'{g[0][chr(99)+chr(104)+chr(97)+chr(114)+chr(115)+chr(95)+chr(114)+chr(101)+chr(109)+chr(111)+chr(118)+chr(101)+chr(100)]}-{g[-1]['chars_removed']}':>16}"
         f"{st.mean([r['chars_removed'] for r in g]):>14.0f}{st.mean([r['share']*100 for r in g]):>12.1f}"
         f"{st.mean(d):>12.3f}{sum(1 for x in d if x>0)/len(d)*100:>10.1f}{sum(1 for x in d if x<0)/len(d)*100:>10.1f}{sum(1 for x in d if x==0)/len(d)*100:>10.1f}")
line("\n  Quintiles of SHARE removed (rescored rows):")
srt2 = sorted(rs, key=lambda r: r["share"])
line(f"    {'quintile':<10}{'n':>5}{'share range %':>16}{'mean_delta':>12}{'%delta>0':>10}{'%delta<0':>10}")
for i in range(5):
    g = srt2[i*q:(i+1)*q] if i<4 else srt2[4*q:]
    d=[r["delta"] for r in g]
    line(f"    Q{i+1:<9}{len(g):>5}{f'{g[0][chr(115)+chr(104)+chr(97)+chr(114)+chr(101)]*100:.1f}-{g[-1][chr(115)+chr(104)+chr(97)+chr(114)+chr(101)]*100:.1f}':>16}"
         f"{st.mean(d):>12.3f}{sum(1 for x in d if x>0)/len(d)*100:>10.1f}{sum(1 for x in d if x<0)/len(d)*100:>10.1f}")
line("\n  Score-change distribution among rescored rows:")
c=Counter(r["delta"] for r in rs)
for k in sorted(c): line(f"    delta={k:+d}: {c[k]:>5} ({c[k]/len(rs)*100:5.1f}%)")
line(f"    mean delta = {st.mean(dl):+.3f}, median = {st.median(dl):+.1f}")
line("\n  Level-6 (Overdone) transitions among rescored rows (raw levels, pre-recode):")
c6=Counter((r["orig_level_raw"]==6, r["stripped_level_raw"]==6) for r in rs)
line(f"    6 -> 6 : {c6[(True,True)]}")
line(f"    6 -> not6 : {c6[(True,False)]}")
line(f"    not6 -> 6 : {c6[(False,True)]}")
line(f"    not6 -> not6 : {c6[(False,False)]}")

# ============ Q4: META vs GENUINE length ============
SEC("Q4. LENGTH OF META vs GENUINE RESPONSES (post-T1, turns 2-5, n=2,880)")
g=[r for r in rescore if r["label"]=="GENUINE"]; mm=[r for r in rescore if r["label"]=="META"]
def lenblock(rows,name,f=lambda r:r["orig_chars"]):
    xs=[f(r) for r in rows]; p=pcts(xs)
    return (f"{name:<12} n={len(rows):>5} mean={st.mean(xs):8.1f} sd={st.pstdev(xs):8.1f} "
            f"p10={p[10]:7.0f} p25={p[25]:7.0f} med={p[50]:7.0f} p75={p[75]:7.0f} p90={p[90]:7.0f} max={max(xs):7.0f}")
line("Original (unstripped) characters:")
line("  "+lenblock(g,"GENUINE")); line("  "+lenblock(mm,"META"))
line(f"  ratio of means GENUINE/META = {st.mean([r['orig_chars'] for r in g])/st.mean([r['orig_chars'] for r in mm]):.2f}x; "
     f"difference of means = {st.mean([r['orig_chars'] for r in g])-st.mean([r['orig_chars'] for r in mm]):+.0f} chars")
line("\nOutput tokens (worker_trials token_counts):")
line("  "+lenblock(g,"GENUINE",lambda r:r["out_tokens"])); line("  "+lenblock(mm,"META",lambda r:r["out_tokens"]))
line("\nCharacters REMOVED by stripping:")
line("  "+lenblock(g,"GENUINE",lambda r:r["chars_removed"])); line("  "+lenblock(mm,"META",lambda r:r["chars_removed"]))
line("\nSurviving (post-strip) characters:")
line("  "+lenblock(g,"GENUINE",lambda r:r["orig_chars"]-r["chars_removed"]))
line("  "+lenblock(mm,"META",lambda r:r["orig_chars"]-r["chars_removed"]))
line("\nStrip rate and detect rate:")
for nm,rows in (("GENUINE",g),("META",mm)):
    line(f"  {nm:<8} strip_rate={sum(r['stripped'] for r in rows)/len(rows)*100:5.1f}%  "
         f"detect_rate={sum(r['detect'] for r in rows)/len(rows)*100:5.1f}%  "
         f"mean share removed={st.mean([r['share'] for r in rows])*100:5.2f}%")
line("\nGENUINE vs META length by model (mean orig chars):")
line(f"  {'model':<20}{'GENUINE':>12}{'nG':>6}{'META':>12}{'nM':>6}{'ratio':>8}")
for m in MODELS:
    gg=[r["orig_chars"] for r in g if r["model"]==m]; mmm=[r["orig_chars"] for r in mm if r["model"]==m]
    line(f"  {m:<20}{st.mean(gg) if gg else 0:>12.0f}{len(gg):>6}{st.mean(mmm) if mmm else 0:>12.0f}{len(mmm):>6}"
         f"{(st.mean(gg)/st.mean(mmm)) if gg and mmm else 0:>8.2f}")
# Mann-Whitney U (normal approx) GENUINE vs META chars
def mannwhitney(a,b):
    comb=[(x,0) for x in a]+[(x,1) for x in b]
    comb.sort(key=lambda z:z[0])
    ranks=[0.0]*len(comb); i=0
    while i<len(comb):
        j=i
        while j+1<len(comb) and comb[j+1][0]==comb[i][0]: j+=1
        avg=(i+j)/2+1
        for k in range(i,j+1): ranks[k]=avg
        i=j+1
    R1=sum(rk for rk,(x,g_) in zip(ranks,comb) if g_==0)
    n1,n2=len(a),len(b)
    U1=R1-n1*(n1+1)/2
    mu=n1*n2/2; sd=(n1*n2*(n1+n2+1)/12)**0.5
    z=(U1-mu)/sd
    A=U1/(n1*n2)  # common-language effect size
    return U1,z,A
U,z,A = mannwhitney([r["orig_chars"] for r in g],[r["orig_chars"] for r in mm])
line(f"\nMann-Whitney (orig chars, GENUINE vs META): U={U:.0f}, z={z:+.2f}, "
     f"P(GENUINE longer than random META) = {A:.3f}")

# ============ Q5: model ranking under stripping ============
SEC("Q5. MODEL RANKING ON QUALITY, UNSTRIPPED vs STRIPPED")
def rank_table(rows, name):
    line(f"\n-- {name} (n per model shown) --")
    res=[]
    for m in MODELS:
        rr=[r for r in rows if r["model"]==m]
        if not rr: continue
        res.append((m,len(rr),st.mean([r["orig_score"] for r in rr]),st.mean([r["stripped_score"] for r in rr])))
    ro=sorted(res,key=lambda x:-x[2]); rs_=sorted(res,key=lambda x:-x[3])
    rko={m:i+1 for i,(m,_,_,_) in enumerate(ro)}; rks={m:i+1 for i,(m,_,_,_) in enumerate(rs_)}
    line(f"  {'model':<20}{'n':>6}{'unstrip':>9}{'rank':>6}{'strip':>9}{'rank':>6}{'shift':>8}{'rankmove':>10}")
    for m,n,o,s in sorted(res,key=lambda x:-x[3]):
        line(f"  {m:<20}{n:>6}{o:>9.3f}{rko[m]:>6}{s:>9.3f}{rks[m]:>6}{s-o:>+8.3f}{rko[m]-rks[m]:>+10d}")
    # Spearman on ranks
    ms=[m for m,_,_,_ in res]
    line(f"  Spearman rho between unstripped and stripped model means: "
         f"{spearman([dict((m,o) for m,_,o,_ in res)[m] for m in ms],[dict((m,s) for m,_,_,s in res)[m] for m in ms]):+.3f}")
    return res
rank_table(rescore, "All 3,600 outputs (T1-T5 pooled)")
rank_table([r for r in rescore if r["turn"]==1], "T1 only (720)")
rank_table([r for r in rescore if r["turn"]>1], "Post-T1 pooled (2,880)")
rank_table([r for r in rescore if r["label"]=="GENUINE"], "GENUINE revisions only (718)")
rank_table([r for r in rescore if r["turn"]==5], "T5 only (720)")
rank_table([r for r in rescore if r["turn"]==5 and r["label"]=="GENUINE"], "T5 GENUINE only (96)")
line("\n-- Per-model T1->T5 GENUINE delta, unstripped vs stripped --")
line(f"  {'model':<20}{'nT5g':>6}{'T1_uns':>9}{'T5_uns':>9}{'d_uns':>8}{'T1_str':>9}{'T5_str':>9}{'d_str':>8}")
for m in MODELS:
    t1=[r for r in rescore if r["model"]==m and r["turn"]==1]
    t5=[r for r in rescore if r["model"]==m and r["turn"]==5 and r["label"]=="GENUINE"]
    if not t5: 
        line(f"  {m:<20}{0:>6}"); continue
    line(f"  {m:<20}{len(t5):>6}{st.mean([r['orig_score'] for r in t1]):>9.2f}{st.mean([r['orig_score'] for r in t5]):>9.2f}"
         f"{st.mean([r['orig_score'] for r in t5])-st.mean([r['orig_score'] for r in t1]):>+8.2f}"
         f"{st.mean([r['stripped_score'] for r in t1]):>9.2f}{st.mean([r['stripped_score'] for r in t5]):>9.2f}"
         f"{st.mean([r['stripped_score'] for r in t5])-st.mean([r['stripped_score'] for r in t1]):>+8.2f}")

# ============ Q6: stripping that LOWERED the score ============
SEC("Q6. DIRECTION OF SCORE CHANGE UNDER STRIPPING")
up=[r for r in rescore if r["delta"]>0]; dn=[r for r in rescore if r["delta"]<0]; sm=[r for r in rescore if r["delta"]==0]
line(f"All 3,600: raised={len(up)} ({len(up)/36:.1f}%), lowered={len(dn)} ({len(dn)/36:.1f}%), unchanged={len(sm)} ({len(sm)/36:.1f}%)")
line(f"Of the {nresc} rescored rows: raised={len(up)} ({len(up)/nresc*100:.1f}%), "
     f"lowered={len(dn)} ({len(dn)/nresc*100:.1f}%), unchanged={sum(1 for r in rs if r['delta']==0)} ({sum(1 for r in rs if r['delta']==0)/nresc*100:.1f}%)")
line(f"Net: mean delta over all 3,600 = {st.mean([r['delta'] for r in rescore]):+.4f}; over rescored = {st.mean(dl):+.4f}")
line("\nBy turn (rescored rows only):")
line(f"  {'turn':<6}{'n_resc':>8}{'raised':>8}{'%':>7}{'lowered':>9}{'%':>7}{'same':>7}{'mean_d':>9}")
for t in range(1,6):
    rr=[r for r in rs if r["turn"]==t]
    line(f"  T{t:<5}{len(rr):>8}{sum(1 for r in rr if r['delta']>0):>8}{sum(1 for r in rr if r['delta']>0)/len(rr)*100:>7.1f}"
         f"{sum(1 for r in rr if r['delta']<0):>9}{sum(1 for r in rr if r['delta']<0)/len(rr)*100:>7.1f}"
         f"{sum(1 for r in rr if r['delta']==0):>7}{st.mean([r['delta'] for r in rr]):>+9.3f}")
line("\nBy model (rescored rows only):")
line(f"  {'model':<20}{'n_resc':>8}{'raised':>8}{'%':>7}{'lowered':>9}{'%':>7}{'mean_d':>9}")
for m in MODELS:
    rr=[r for r in rs if r["model"]==m]
    line(f"  {m:<20}{len(rr):>8}{sum(1 for r in rr if r['delta']>0):>8}{sum(1 for r in rr if r['delta']>0)/len(rr)*100:>7.1f}"
         f"{sum(1 for r in rr if r['delta']<0):>9}{sum(1 for r in rr if r['delta']<0)/len(rr)*100:>7.1f}{st.mean([r['delta'] for r in rr]):>+9.3f}")
line("\nBy domain (rescored rows only):")
line(f"  {'domain':<20}{'n_resc':>8}{'raised':>8}{'%':>7}{'lowered':>9}{'%':>7}{'mean_d':>9}")
for d in DOMAINS:
    rr=[r for r in rs if r["domain"]==d]
    line(f"  {d:<20}{len(rr):>8}{sum(1 for r in rr if r['delta']>0):>8}{sum(1 for r in rr if r['delta']>0)/len(rr)*100:>7.1f}"
         f"{sum(1 for r in rr if r['delta']<0):>9}{sum(1 for r in rr if r['delta']<0)/len(rr)*100:>7.1f}{st.mean([r['delta'] for r in rr]):>+9.3f}")
line("\nDowngrades: raw level transitions (orig_level_raw -> stripped_level_raw) for delta<0 rows:")
for k,v in sorted(Counter((r["orig_level_raw"],r["stripped_level_raw"]) for r in dn).items(), key=lambda x:-x[1]):
    line(f"    {k[0]} -> {k[1]}: {v}")
line("\nUpgrades: raw level transitions for delta>0 rows (top 12):")
for k,v in sorted(Counter((r["orig_level_raw"],r["stripped_level_raw"]) for r in up).items(), key=lambda x:-x[1])[:12]:
    line(f"    {k[0]} -> {k[1]}: {v}")
line("\nMean share removed, by direction of change (rescored rows):")
for nm,rows in (("raised",up),("lowered",dn),("unchanged",[r for r in rs if r['delta']==0])):
    line(f"  {nm:<10} n={len(rows):>4} mean_chars_removed={st.mean([r['chars_removed'] for r in rows]):7.0f} "
         f"mean_share={st.mean([r['share'] for r in rows])*100:5.1f}% mean_orig_len={st.mean([r['orig_chars'] for r in rows]):7.0f} "
         f"mean_orig_score={st.mean([r['orig_score'] for r in rows]):.2f}")

# ============ Q7: extras ============
SEC("Q7. EXTRAS")
line("-- (a) Judge rationale language: how often does the judge's WRITTEN rationale name the meta-commentary? --")
META_WORDS = [r"meta-?commentary", r"preamble", r"postamble", r"conversational (?:filler|framing|wrapper)",
              r"let me know", r"unnecessary (?:commentary|preamble|framing)", r"offers? to (?:further )?revise",
              r"explanat(?:ory|ion) (?:preamble|framing|text)", r"commentary (?:about|around|on) the (?:revision|change)"]
MRE=[re.compile(p,re.I) for p in META_WORDS]
for lvl in range(1,7):
    rows=[evalr[(r["trial_id"],r["turn"])] for r in rescore if r["orig_level_raw"]==lvl]
    hit=sum(1 for e in rows if any(x.search(e["rationale"]) for x in MRE))
    line(f"  orig level {lvl}: rationale names meta {hit}/{len(rows)} = {hit/len(rows)*100:5.1f}%")
allrows=[evalr[(r["trial_id"],r["turn"])] for r in rescore]
hit=sum(1 for e in allrows if any(x.search(e["rationale"]) for x in MRE))
line(f"  all 3,600: {hit} ({hit/36:.1f}%)")
line("  among rows that were stripped: "
     f"{sum(1 for r in rescore if r['stripped'] and any(x.search(evalr[(r['trial_id'],r['turn'])]['rationale']) for x in MRE))}/{nchanged}")
line("  among rows not stripped: "
     f"{sum(1 for r in rescore if not r['stripped'] and any(x.search(evalr[(r['trial_id'],r['turn'])]['rationale']) for x in MRE))}/{3600-nchanged}")

line("\n-- (b) Token cost of meta-commentary (chars removed -> approx output tokens at corpus chars/token) --")
tot_ch=sum(r["orig_chars"] for r in rescore); tot_tok=sum(r["out_tokens"] for r in rescore)
line(f"  corpus chars/token = {tot_ch/tot_tok:.2f}; total chars removed {sum(r['chars_removed'] for r in rescore):,} "
     f"~= {sum(r['chars_removed'] for r in rescore)/(tot_ch/tot_tok):,.0f} output tokens ({sum(r['chars_removed'] for r in rescore)/(tot_ch/tot_tok)/tot_tok*100:.2f}% of all output tokens)")

line("\n-- (c) Within-trial asymmetry on the full corpus: is T1 less wrapped than the same trial's own later turns? --")
both=0; t1_only=0; later_only=0; neither=0
for tid in trials:
    t1d=[r for r in rescore if r["trial_id"]==tid and r["turn"]==1][0]["detect"] if True else None
line("  (computed below with an index for speed)")
idx=defaultdict(dict)
for r in rescore: idx[r["trial_id"]][r["turn"]]=r
n_t1=sum(1 for tid in idx if idx[tid][1]["detect"])
n_any_later=sum(1 for tid in idx if any(idx[tid][t]["detect"] for t in (2,3,4,5)))
line(f"  trials whose T1 is wrapped: {n_t1}/720 = {n_t1/7.2:.1f}%")
line(f"  trials with any wrapped turn in T2-T5: {n_any_later}/720 = {n_any_later/7.2:.1f}%")
disc=Counter()
for tid in idx:
    a=idx[tid][1]["detect"]; b=any(idx[tid][t]["detect"] for t in (2,3,4,5))
    disc[(a,b)]+=1
line(f"  T1 clean & later wrapped: {disc[(False,True)]}; T1 wrapped & later clean: {disc[(True,False)]}; "
     f"both: {disc[(True,True)]}; neither: {disc[(False,False)]}")
line(f"  McNemar-style discordant ratio: {disc[(False,True)]}:{disc[(True,False)]}")

line("\n-- (d) Does stripping change whether an output clears the sufficiency bar (level >= 4)? --")
cross=Counter((r["orig_score"]>=4, r["stripped_score"]>=4) for r in rescore)
line(f"  suff both: {cross[(True,True)]}; insuff->suff: {cross[(False,True)]}; suff->insuff: {cross[(True,False)]}; insuff both: {cross[(False,False)]}")
line(f"  sufficiency rate unstripped {sum(1 for r in rescore if r['orig_score']>=4)/36:.1f}% -> stripped {sum(1 for r in rescore if r['stripped_score']>=4)/36:.1f}%")
line("  by turn:")
for t in range(1,6):
    rr=[r for r in rescore if r["turn"]==t]
    line(f"    T{t}: {sum(1 for r in rr if r['orig_score']>=4)/len(rr)*100:5.1f}% -> {sum(1 for r in rr if r['stripped_score']>=4)/len(rr)*100:5.1f}% "
         f"(insuff->suff {sum(1 for r in rr if r['orig_score']<4 and r['stripped_score']>=4)}, suff->insuff {sum(1 for r in rr if r['orig_score']>=4 and r['stripped_score']<4)})")

line("\n-- (e) Length vs score: is the judge simply penalizing length, or specifically meta? --")
line("  Correlation of orig_chars with orig_score, all 3,600: "
     f"Pearson {corr([r['orig_chars'] for r in rescore],[r['orig_score'] for r in rescore]):+.3f}, "
     f"Spearman {spearman([r['orig_chars'] for r in rescore],[r['orig_score'] for r in rescore]):+.3f}")
line("  Correlation of surviving (post-strip) chars with stripped_score: "
     f"Pearson {corr([r['orig_chars']-r['chars_removed'] for r in rescore],[r['stripped_score'] for r in rescore]):+.3f}, "
     f"Spearman {spearman([r['orig_chars']-r['chars_removed'] for r in rescore],[r['stripped_score'] for r in rescore]):+.3f}")

line("\n-- (f) Mean quality by turn, unstripped vs stripped, ALL 3,600 (no GENUINE filter) --")
line(f"  {'turn':<6}{'n':>6}{'unstrip':>10}{'strip':>10}{'shift':>9}")
for t in range(1,6):
    rr=[r for r in rescore if r["turn"]==t]
    line(f"  T{t:<5}{len(rr):>6}{st.mean([r['orig_score'] for r in rr]):>10.3f}{st.mean([r['stripped_score'] for r in rr]):>10.3f}"
         f"{st.mean([r['stripped_score'] for r in rr])-st.mean([r['orig_score'] for r in rr]):>+9.3f}")

line("\n-- (g) Level-6 rate on ALL 3,600 (not GENUINE-only), unstripped vs stripped --")
line(f"  {'turn':<6}{'unstrip%':>10}{'strip%':>10}{'shift_pp':>10}")
for t in range(1,6):
    rr=[r for r in rescore if r["turn"]==t]
    a=sum(1 for r in rr if r["orig_level_raw"]==6)/len(rr)*100
    b=sum(1 for r in rr if r["stripped_level_raw"]==6)/len(rr)*100
    line(f"  T{t:<5}{a:>10.1f}{b:>10.1f}{b-a:>+10.1f}")
line("  Level-6 share among stripped vs unstripped rows (unstripped scores):")
line(f"    rows stripped:     {sum(1 for r in rescore if r['stripped'] and r['orig_level_raw']==6)}/{nchanged} = {sum(1 for r in rescore if r['stripped'] and r['orig_level_raw']==6)/nchanged*100:.1f}%")
line(f"    rows not stripped: {sum(1 for r in rescore if not r['stripped'] and r['orig_level_raw']==6)}/{3600-nchanged} = {sum(1 for r in rescore if not r['stripped'] and r['orig_level_raw']==6)/(3600-nchanged)*100:.1f}%")

line("\n-- (h) Strip-rate vs detect-rate: how much does the CONTENT_SIGNALS veto suppress? --")
line(f"  detect only (regex hit, nothing stripped): {sum(1 for r in rescore if r['detect'] and not r['stripped'])}")
line(f"  strip only (stripped, no regex hit in windows): {sum(1 for r in rescore if r['stripped'] and not r['detect'])}")
line(f"  both: {sum(1 for r in rescore if r['detect'] and r['stripped'])}; neither: {sum(1 for r in rescore if not r['detect'] and not r['stripped'])}")
line(f"  detect rate overall: {sum(r['detect'] for r in rescore)/36:.1f}%; strip rate overall: {nchanged/36:.1f}%")

line("\n-- (i) Preamble vs postamble prevalence by turn (DETECT, all 3,600) --")
line(f"  {'turn':<6}{'pre%':>8}{'post%':>8}{'both%':>8}{'either%':>9}")
for t in range(1,6):
    rr=[r for r in rescore if r["turn"]==t]
    line(f"  T{t:<5}{sum(r['pre'] for r in rr)/len(rr)*100:>8.1f}{sum(r['post'] for r in rr)/len(rr)*100:>8.1f}"
         f"{sum(1 for r in rr if r['pre'] and r['post'])/len(rr)*100:>8.1f}{sum(r['detect'] for r in rr)/len(rr)*100:>9.1f}")
