#!/usr/bin/env python3
"""Part 2: scope sweep for the ledger's per-turn breakdown, preamble/postamble split
of removed characters, sign tests, domain ranking. Read-only.

strip_text/PREAMBLE_META/POSTAMBLE_META/CONTENT_SIGNALS are COPIED VERBATIM from
scripts/study3/stripped_rescore_full.py. strip_meta_commentary.py is never imported.
"""
import json, re, math, statistics as st
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path("/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds")
D = ROOT/"data"/"study3"/"raw_responses"

PREAMBLE_META = [
    r"(?:i'?d like to|let me|i'?ll|i want to)\s+(?:revise|make|take|offer|give|try|refine|polish|tighten)",
    r"here'?s (?:the|my|a|an|another) (?:revised|improved|updated|final|slightly|new|definitive)",
    r"(?:sure|okay|alright|absolutely)[,!.]?\s+here",
    r"(?:looking|look) (?:back|at (?:it|this|my))",
    r"(?:after|upon) (?:review|re-?reading|careful review|reflection)",
    r"(?:i've|i have) reviewed",
    r"thank(?:s| you) for (?:the|asking|checking|your|this)",
    r"(?:great|good) (?:question|prompt)",
    r"actually,? let me",
    r"considering the response",
    r"(?:this is a )?(?:very )?(?:solid|strong|great|good|excellent) (?:implementation|version|set|start|draft|point)",
    r"you'?re right to ask",
    r"since you(?:'re| are| repeated| asked|'ve)",
    r"i (?:think|believe) (?:i can|we can|it could|the|this|there's)",
    r"i can make (?:some|a few|one|minor)",
    r"(?:after|upon) re-?reading",
    r"i understand (?:the|your|you're)",
    r"i'?m (?:satisfied|happy|confident) with",
    r"(?:the|this) (?:version|response|output|code|email|post|analysis) (?:is|can be|meets|works)",
]
POSTAMBLE_META = [
    r"let me know (?:if|what|how|whether)", r"hope this helps", r"feel free to",
    r"(?:happy|glad|ready) to (?:help|assist|revise|adjust|make|answer)",
    r"(?:if you'?d like|would you like|if you want) (?:any|me to|further|more|to|a)",
    r"(?:i'?m|we'?re) (?:here|available|happy) (?:to|if)",
    r"(?:just )?let me know",
    r"(?:what do you think|how does (?:this|that) (?:sound|look|work))",
    r"(?:otherwise|if not),? (?:this|it|we|you|consider|go ahead)",
    r"(?:i believe|i think|i'?m confident) (?:this|it|the) (?:version|is|meets|works|feels)",
    r"(?:ready to|you can) (?:use|go|send|share|present|submit)",
    r"(?:i'?ve|i have) made (?:some|minor|a few)",
    r"(?:do you|would you) (?:want|like|need) (?:me to|any)",
    r"(?:this is|consider this|go ahead).{0,30}(?:final|done|ready|yours)",
    r"if (?:this|that) works for you",
    r"(?:if you|you can) (?:have|need|want) any (?:questions|concerns|feedback)",
    r"(?:congratulations|best of luck|good luck)",
    r"please let me know",
]
CONTENT_SIGNALS = [
    r"```", r"^\s*[-*]\s+\*\*", r"^\s*\d+\.\s", r"^\s*#{1,4}\s",
    r"\bdef\s+\w+\(", r"\bfunction\s+\w+\(", r"\bclass\s+\w+",
    r"^\s*\|.*\|", r"Subject:", r"^(?:Hi|Dear|Hello)\s+\w+",
    r"\$\d+", r"\d+%", r"(?:domestic|international|express)",
]
def is_meta_paragraph(text, patterns):
    tl = text.strip().lower()
    if len(tl) < 5: return False
    for sig in CONTENT_SIGNALS:
        if re.search(sig, text, re.MULTILINE|re.IGNORECASE): return False
    for pat in patterns:
        if re.search(pat, tl): return True
    return False

def strip_parts(text):
    """Returns (front_chars, back_chars, result) using the same walk as the pass."""
    if not text or len(text.strip()) < 50: return 0,0,text
    parts = re.split(r"(\n\n+|\n---+\n)", text)
    strip_front = 0; i = 0
    while i < len(parts):
        part = parts[i].strip()
        if not part or re.match(r"^---+$", part): i += 1; continue
        if is_meta_paragraph(part, PREAMBLE_META):
            strip_front = i+1
            if i+1 < len(parts) and not parts[i+1].strip(): strip_front = i+2
            i += 1
        else: break
        i += 1
    strip_back = len(parts); i = len(parts)-1
    while i >= strip_front:
        part = parts[i].strip()
        if not part or re.match(r"^---+$", part): i -= 1; continue
        if is_meta_paragraph(part, POSTAMBLE_META):
            strip_back = i
            if i-1 >= strip_front and not parts[i-1].strip(): strip_back = i-1
            i -= 1
        else: break
        i -= 1
    kept = parts[strip_front:strip_back]
    result = "".join(kept).strip()
    if len(result) < len(text.strip())*0.3: return 0,0,text.strip()
    if not result: return 0,0,text.strip()
    front = len("".join(parts[:strip_front]))
    back = len("".join(parts[strip_back:]))
    return front, back, result

# audit DETECT patterns
PRE_A = [re.compile(p) for p in [
    r"(?:i'?d like to|let me|i'?ll|i want to)\s+(?:revise|make|take|offer|give|try)",
    r"here'?s (?:the|my|a|an) (?:revised|improved|updated|final|slightly|new)",
    r"(?:sure|okay|alright|absolutely)[,!.]?\s+here", r"i think (?:i can|we can|it could|there)",
    r"(?:looking|look) (?:back|at (?:it|this|my))", r"(?:after|upon) review", r"(?:i've|i have) reviewed",
    r"thank(?:s| you) for (?:the|asking|checking|your)", r"(?:great|good) question", r"actually,? let me",
    r"(?:i'?d like to|i want to) (?:keep|confirm|make)", r"considering the response",
    r"(?:this is a )?(?:very )?(?:solid|strong|great|good) (?:implementation|version|set|start|draft)",
    r"you'?re right to ask", r"since you(?:'re| are| repeated)", r"(?:i can|let me) make (?:some|a few|one|minor)",
    r"(?:the|this) (?:version|script|function|code|email|post|analysis|response) (?:is|can be|could be)",
    r"however,? (?:i|during|to make)", r"(?:after|upon) re-?reading"]]
POST_A = [re.compile(p) for p in [
    r"let me know (?:if|what|how)", r"hope this helps", r"feel free to",
    r"(?:happy|glad) to (?:help|assist|revise|adjust|make)",
    r"(?:if you'?d like|would you like) (?:any|me to|further|more)",
    r"(?:i'?m|we'?re) (?:here|available|happy) (?:to|if)", r"(?:just )?let me know",
    r"(?:what do you think|how does (?:this|that) (?:sound|look|work))",
    r"(?:otherwise|if not),? (?:this|it|we)",
    r"(?:i believe|i think|i'?m confident) (?:this|it|the) (?:version|is|meets|works|feels)",
    r"(?:no )?further (?:changes|revisions|adjustments)", r"this version (?:feels|is|should)",
    r"(?:ready to|you can) (?:use|go|send|share|present|submit)",
    r"(?:i'?ve|i have) made (?:some|minor|a few)", r"(?:do you|would you) (?:want|like|need) (?:me to|any)"]]
hp = lambda t: any(r.search(t[:300].lower()) for r in PRE_A)
hq = lambda t: any(r.search(t[-400:].lower()) for r in POST_A)

rescore=[json.loads(l) for l in open(D/"stripped_rescore_full.jsonl")]
labels={(r["trial_id"],r["turn"]):r["classifier_label"] for r in map(json.loads,open(D/"genuine_meta_labels.jsonl"))}
kwlab={(r["trial_id"],r["turn"]):r["keyword_label"] for r in map(json.loads,open(D/"genuine_meta_labels.jsonl"))}
trials={t["trial_id"]:t for t in map(json.loads,open(D/"worker_trials.jsonl"))}
for r in rescore:
    r["text"]=trials[r["trial_id"]]["responses"][r["turn"]-1]
    r["label"]=labels.get((r["trial_id"],r["turn"]))
    r["kw"]=kwlab.get((r["trial_id"],r["turn"]))
    r["delta"]=r["stripped_score"]-r["orig_score"]

TARGET=[14,92,85,79,68]
def report(name, series):
    s=[round(x) for x in series]
    line=f"  {name:<58} {['%5.1f'%x for x in series]}  match={'YES' if s==TARGET else 'no'}"
    print(line)

print("="*78); print("SCOPE SWEEP against the ledger's T1:14 T2:92 T3:85 T4:79 T5:68"); print("="*78)
def rate(rows, f): return 100*sum(1 for r in rows if f(r))/len(rows) if rows else float('nan')
detect=lambda r: hp(r["text"]) or hq(r["text"])
stripd=lambda r: r["chars_removed"]>0
scopes={
 "all 3600, DETECT(either)":            (lambda t: [r for r in rescore if r["turn"]==t], detect),
 "all 3600, STRIP":                     (lambda t: [r for r in rescore if r["turn"]==t], stripd),
 "T1=all/post-T1 GENUINE, DETECT":      (lambda t: [r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")], detect),
 "T1=all/post-T1 GENUINE, STRIP":       (lambda t: [r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")], stripd),
 "T1=all/post-T1 kw=REVISION, DETECT":  (lambda t: [r for r in rescore if r["turn"]==t and (t==1 or r["kw"]=="REVISION")], detect),
 "T1=all/post-T1 kw=REVISION, STRIP":   (lambda t: [r for r in rescore if r["turn"]==t and (t==1 or r["kw"]=="REVISION")], stripd),
 "T1=all/post-T1 GENUINE, DETECT pre":  (lambda t: [r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")], lambda r: hp(r["text"])),
 "T1=all/post-T1 GENUINE, DETECT post": (lambda t: [r for r in rescore if r["turn"]==t and (t==1 or r["label"]=="GENUINE")], lambda r: hq(r["text"])),
 "50 balanced-panel trials, DETECT":    None,
 "50 balanced-panel trials, STRIP":     None,
}
bp={tid for tid in trials if all(labels.get((tid,t))=="GENUINE" for t in (2,3,4,5))}
scopes["50 balanced-panel trials, DETECT"]=(lambda t: [r for r in rescore if r["trial_id"] in bp and r["turn"]==t], detect)
scopes["50 balanced-panel trials, STRIP"]=(lambda t: [r for r in rescore if r["trial_id"] in bp and r["turn"]==t], stripd)
for name,(sel,f) in scopes.items():
    report(name, [rate(sel(t), f) for t in range(1,6)])
# 50 reversibility pairs
pairs=json.load(open(D/"reversibility_human_pairs.json"))
key={k["pair_id"]:k for k in json.load(open(D/"reversibility_human_key.json"))}
t1s=[];byt=defaultdict(list)
for p in pairs:
    k=key[p["pair_id"]]
    t1t=p["output_A"] if k["A_is"]=="T1" else p["output_B"]
    rv=p["output_B"] if k["A_is"]=="T1" else p["output_A"]
    t1s.append(t1t); byt[k["last_rev_turn"]].append(rv)
ser=[100*sum(1 for x in t1s if hp(x) or hq(x))/len(t1s)]+[100*sum(1 for x in byt[t] if hp(x) or hq(x))/len(byt[t]) for t in range(2,6)]
report("50 reversibility pairs (T1 side; rev side by last_rev_turn)", ser)
print("   n per cell for the 50 pairs: T1=%d, "%len(t1s)+", ".join(f"T{t}={len(byt[t])}" for t in range(2,6)))

print("\n"+"="*78); print("PREAMBLE vs POSTAMBLE SHARE OF REMOVED CHARACTERS"); print("="*78)
fb=[]
for r in rescore:
    f,b,res=strip_parts(r["text"])
    fb.append((r,f,b))
    r["front"]=f; r["back"]=b
recon=sum(1 for r,f,b in fb if abs((f+b)-r["chars_removed"])>6)
print(f"rows where front+back deviates from stored chars_removed by >6 chars: {recon}/3600 "
      f"(deviation is whitespace trimmed at the join)")
tf=sum(r['front'] for r in rescore); tb=sum(r['back'] for r in rescore)
print(f"total front (preamble) chars removed: {tf:,} ({tf/(tf+tb)*100:.1f}% of removal)")
print(f"total back (postamble) chars removed: {tb:,} ({tb/(tf+tb)*100:.1f}% of removal)")
print(f"  {'turn':<6}{'n_strip':>9}{'front_only':>12}{'back_only':>11}{'both':>7}{'mean_front':>12}{'mean_back':>11}")
for t in range(1,6):
    rr=[r for r in rescore if r["turn"]==t and r["chars_removed"]>0]
    print(f"  T{t:<5}{len(rr):>9}{sum(1 for r in rr if r['front']>0 and r['back']==0):>12}"
          f"{sum(1 for r in rr if r['back']>0 and r['front']==0):>11}{sum(1 for r in rr if r['front']>0 and r['back']>0):>7}"
          f"{st.mean([r['front'] for r in rr]):>12.1f}{st.mean([r['back'] for r in rr]):>11.1f}")
print(f"  {'model':<20}{'n_strip':>9}{'front_only':>12}{'back_only':>11}{'both':>7}{'mean_front':>12}{'mean_back':>11}")
for m in sorted({r['model'] for r in rescore}):
    rr=[r for r in rescore if r["model"]==m and r["chars_removed"]>0]
    print(f"  {m:<20}{len(rr):>9}{sum(1 for r in rr if r['front']>0 and r['back']==0):>12}"
          f"{sum(1 for r in rr if r['back']>0 and r['front']==0):>11}{sum(1 for r in rr if r['front']>0 and r['back']>0):>7}"
          f"{st.mean([r['front'] for r in rr]):>12.1f}{st.mean([r['back'] for r in rr]):>11.1f}")

print("\n"+"="*78); print("SIGN TESTS ON DIRECTION OF SCORE CHANGE"); print("="*78)
def binom_two_sided(k,n,p=0.5):
    # exact two-sided via doubling the smaller tail
    from math import comb
    lo=sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(0,k+1))
    hi=sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))
    return min(1.0, 2*min(lo,hi))
up=sum(1 for r in rescore if r["delta"]>0); dn=sum(1 for r in rescore if r["delta"]<0)
print(f"all 3,600: raised {up}, lowered {dn}; exact two-sided sign test p = {binom_two_sided(min(up,dn),up+dn):.3e}")
for t in range(1,6):
    u=sum(1 for r in rescore if r["turn"]==t and r["delta"]>0); d=sum(1 for r in rescore if r["turn"]==t and r["delta"]<0)
    p=binom_two_sided(min(u,d),u+d) if u+d else float('nan')
    print(f"  T{t}: raised {u}, lowered {d}, p={p:.3e}")
for m in sorted({r['model'] for r in rescore}):
    u=sum(1 for r in rescore if r["model"]==m and r["delta"]>0); d=sum(1 for r in rescore if r["model"]==m and r["delta"]<0)
    print(f"  {m:<20} raised {u:>4}, lowered {d:>3}, p={binom_two_sided(min(u,d),u+d):.3e}")

print("\n"+"="*78); print("DOMAIN RANKING, UNSTRIPPED vs STRIPPED (GENUINE revisions only, n=718)"); print("="*78)
g=[r for r in rescore if r["label"]=="GENUINE"]
res=[(d,len([r for r in g if r["domain"]==d]),
      st.mean([r["orig_score"] for r in g if r["domain"]==d]),
      st.mean([r["stripped_score"] for r in g if r["domain"]==d])) for d in sorted({r["domain"] for r in g})]
ro=sorted(res,key=lambda x:-x[2]); rs_=sorted(res,key=lambda x:-x[3])
rko={d:i+1 for i,(d,_,_,_) in enumerate(ro)}; rks={d:i+1 for i,(d,_,_,_) in enumerate(rs_)}
print(f"  {'domain':<14}{'n':>5}{'unstrip':>9}{'rank':>6}{'strip':>9}{'rank':>6}{'shift':>8}{'move':>7}")
for d,n,o,s in rs_:
    print(f"  {d:<14}{n:>5}{o:>9.3f}{rko[d]:>6}{s:>9.3f}{rks[d]:>6}{s-o:>+8.3f}{rko[d]-rks[d]:>+7d}")

print("\n"+"="*78); print("TIE CHECK IN MODEL RANKINGS (GENUINE-only, n=718)"); print("="*78)
gm=[(m,len([r for r in g if r["model"]==m]),
     st.mean([r["orig_score"] for r in g if r["model"]==m]),
     st.mean([r["stripped_score"] for r in g if r["model"]==m])) for m in sorted({r["model"] for r in g})]
for m,n,o,s in sorted(gm,key=lambda x:-x[3]):
    print(f"  {m:<20} n={n:>4}  unstripped {o:.4f}  stripped {s:.4f}")

print("\n"+"="*78); print("DOWNGRADE ANATOMY: the 49 rows where stripping LOWERED the score"); print("="*78)
dnr=[r for r in rescore if r["delta"]<0]
print(f"  mean orig_score {st.mean([r['orig_score'] for r in dnr]):.2f} vs corpus rescored mean "
      f"{st.mean([r['orig_score'] for r in rescore if r['was_rescored']]):.2f}")
print(f"  of the 49, orig level 4 or 5 (sufficient): {sum(1 for r in dnr if r['orig_level_raw'] in (4,5))}")
print(f"  of the 49, stripped level became 6 (Overdone): {sum(1 for r in dnr if r['stripped_level_raw']==6)}")
print(f"  label mix: {Counter(r['label'] for r in dnr)}")
print(f"  model mix: {Counter(r['model'] for r in dnr).most_common()}")
print(f"  domain mix: {Counter(r['domain'] for r in dnr).most_common()}")

print("\n"+"="*78); print("HOW MUCH OF THE 1,200 RESCORED SET IS GENUINE vs META vs T1"); print("="*78)
rs=[r for r in rescore if r["was_rescored"]]
print(f"  T1: {sum(1 for r in rs if r['turn']==1)}")
print(f"  post-T1 GENUINE: {sum(1 for r in rs if r['label']=='GENUINE')}")
print(f"  post-T1 META: {sum(1 for r in rs if r['label']=='META')}")
print(f"  mean delta by label: T1={st.mean([r['delta'] for r in rs if r['turn']==1]):+.3f}, "
      f"GENUINE={st.mean([r['delta'] for r in rs if r['label']=='GENUINE']):+.3f}, "
      f"META={st.mean([r['delta'] for r in rs if r['label']=='META']):+.3f}")
print(f"  raised share by label: T1={sum(1 for r in rs if r['turn']==1 and r['delta']>0)}/{sum(1 for r in rs if r['turn']==1)}, "
      f"GENUINE={sum(1 for r in rs if r['label']=='GENUINE' and r['delta']>0)}/{sum(1 for r in rs if r['label']=='GENUINE')}, "
      f"META={sum(1 for r in rs if r['label']=='META' and r['delta']>0)}/{sum(1 for r in rs if r['label']=='META')}")
