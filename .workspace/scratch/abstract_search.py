"""
Exhaustive search over abstract variants, scored against the measured venue corpus.

Every variant is factually grounded in results_FINAL.md. The scorer encodes what the
research established, not taste:
  density   - reward sitting between the venue p50 and p90; penalise outside
  length    - reward 160-200 words (venue median 161)
  register  - hard penalties for the things measured at zero in the corpus
  repetition- penalise content words used more than twice
  coverage  - require the non-revision finding, the asymmetry, and the close
Component scores are printed so the total can be argued with.
"""
import json, re, itertools, statistics as st

CORP = json.load(open('paper/reference/acl2026_abstracts.json'))
def collect(o, acc):
    if isinstance(o, str):
        if len(o.split()) > 60: acc.append(o)
    elif isinstance(o, dict):
        for k, v in o.items():
            if not k.startswith('_'): collect(v, acc)
    elif isinstance(o, list):
        for v in o: collect(v, acc)
    return acc
A = collect(CORP, [])

MODEL = r'GPT-4o|GPT-\d[\w.-]*|Llama[\s-]?\d[\d.]*\s?\d*B?|Gemini[\s-]?[\d.]+|Qwen[\s-]?[\d.-]*|Claude Sonnet \d'
NOMIN = r'\b\w{4,}(tion|ment|ance|ence|ity|ness|ism|ization|isation)s?\b'

def syll(w):
    w = re.sub(r'[^a-z]', '', w.lower())
    if not w: return 1
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1: n -= 1
    return max(1, n)

def measure(t):
    sents = [x for x in re.split(r'(?<=[.!?])\s+', t) if len(x.split()) > 3]
    w = t.split()
    return dict(
        words=len(w), sents=len(sents),
        flesch=206.835 - 1.015*(len(w)/len(sents)) - 84.6*(sum(syll(x) for x in w)/len(w)),
        dens=len(re.findall(r'(?<![\w.])\d[\d,.]*\s?%?', re.sub(MODEL, 'M', t)))/len(w)*100,
        nomin=len(re.findall(NOMIN, t, re.I))/len(w)*100)

CD = sorted(measure(t)['dens'] for t in A)
CF = sorted(measure(t)['flesch'] for t in A)
def pctile(x, v): return sum(1 for a in v if a <= x)/len(v)*100

# ---- variant slots. every figure traces to results_FINAL.md ----
SLOTS = {
 "open": [
  ("Q",   "Do language models know when a good answer should be left alone?"),
  ("decl","Language models are increasingly handed work their users could not do themselves."),
  ("find","Asked to improve work that is already good enough, language models mostly make it worse."),
 ],
 "setup": [
  ("full","They are increasingly handed work their users could not do themselves, and a user unable to name what is wrong falls back on undirected requests that carry no information about what to change."),
  ("lean","A user unable to name what is wrong falls back on undirected requests that carry no information about what to change."),
  ("users","Users who cannot say what is wrong with an output fall back on undirected requests that carry no information about what to change."),
 ],
 "prior": [
  ("long","Studies of self-correction ask whether a model can repair a response that is wrong, and find that it can with a specific critique and largely cannot without one."),
  ("tight","Self-correction research asks whether a model can repair a wrong response, and finds that it can with a specific critique and largely cannot without one."),
 ],
 "gap": [
  ("plain","That leaves unexamined the case where the work is already sufficient and gets revised anyway because the user cannot tell."),
  ("num","That leaves unexamined the case where the work is already sufficient and gets revised anyway, as 88% of first drafts here are."),
 ],
 "method": [
  ("words","In this work, we run five-turn revision conversations with six models on forty tasks across five domains, contrasting undirected requests with a single targeted critique."),
  ("nums","In this work, we run five-turn revision conversations with 6 models on 40 tasks across 5 domains, contrasting undirected requests with a single targeted critique."),
  ("named","We run five-turn revision conversations with 6 models, including GPT-4o, Claude Sonnet 4 and Llama 3.3 70B, on 40 tasks across 5 domains, contrasting undirected requests with a single targeted critique."),
 ],
 "norev": [
  ("qual","Most replies contain no revision at all, with models restating the work or declining while presenting it as compliance."),
  ("pct","75% of replies contain no revision at all, with models restating the work or declining while presenting it as compliance."),
  ("decline","Genuine revision falls from 39% of replies at the second turn to 13% by the fifth, with models instead restating the work or declining while presenting it as compliance."),
 ],
 "asym": [
  ("worse","Revisions that change quality make it worse 70% of the time."),
  ("down","70% of the revisions that move quality at all move it downward."),
 ],
 "mag": [
  ("suff","Applied to work that was already sufficient, 27% of them leave it insufficient."),
  ("suffdom","Applied to work that was already sufficient, 27% of them leave it insufficient, and the pattern holds in all five domains."),
  ("none",""),
 ],
 "formal": [
  ("none",""),
  ("tstar","The quality-optimal stopping point is the first turn for all six models."),
 ],
 "texture": [
  ("plain","For every model the first draft rates highest, and blind readers show no reliable preference between it and the last."),
  ("tstar","For every model the quality-optimal turn is the first, and blind readers show no reliable preference between the first draft and the last."),
  ("peak","Quality peaks at the first turn for every model, and blind readers show no reliable preference between the first draft and the last."),
 ],
 "close": [
  ("fault","These results indicate that undirected revision lowers the quality of work that was already sufficient, and that naming the fault reverses the effect."),
  ("dir","These results indicate that undirected revision lowers the quality of work that was already sufficient, and that the failure is one of direction rather than capacity."),
  ("restore","These results indicate that undirected revision lowers the quality of work that was already sufficient, and that a single targeted critique restores it."),
 ],
}
ORDER = ["open","setup","prior","gap","method","norev","asym","mag","formal","texture","close"]

def score(text, keys):
    m = measure(text)
    parts = {}
    dp = pctile(m['dens'], CD)
    parts['density']    = 12 if 70 <= dp <= 95 else (6 if 50 <= dp < 70 else -8)
    parts['length']     = 10 if 160 <= m['words'] <= 200 else (4 if m['words'] <= 215 else -10)
    parts['readable']   = min(10, (m['flesch'] - 35) / 2)
    parts['nominal']    = 6 if m['nomin'] <= 5 else 0
    bad = 0
    bad += 8 * len(re.findall(r'—|--', text))
    bad += 8 * text.count(':') + 6 * text.count(';')
    bad += 8 * len(re.findall(r'\b(one|two|three|seven)[- ]in[- ]\w+', text, re.I))
    bad += 8 * len(re.findall(r'\bwe\s+(show|demonstrate|prove)\b', text, re.I))
    bad += 8 * len(re.findall(r'\b(notably|crucially|importantly|significantly|remarkably)\b', text, re.I))
    parts['register']   = -bad
    words = [w.lower().strip('.,?%') for w in text.split() if len(w) > 5]
    reps = sum(c - 2 for c in __import__('collections').Counter(words).values() if c > 2)
    parts['repetition'] = -2 * reps
    # coherence: a question opening must be answered by a finding, not only by the close
    parts['coherence']  = 0
    # frequency without magnitude is uninformative: the asymmetry needs a size beside it
    if keys['mag'] == 'none':
        parts['coherence'] -= 7
    if keys['open'] == 'Q' and keys['norev'] == 'qual' and keys['mag'] == 'none':
        parts['coherence'] = -6
    if keys['setup'] == 'lean' and keys['open'] != 'decl':
        parts['coherence'] -= 6          # loses the human-AI framing Ali asked for
    if keys['formal'] == 'tstar' and keys['texture'] in ('tstar','peak'):
        parts['coherence'] -= 6          # states the peak twice
    if keys['open'] == 'find' and keys['asym'] == 'worse':
        parts['coherence'] = -5          # finding stated twice
    return sum(parts.values()), parts, m

best = []
for combo in itertools.product(*[SLOTS[s] for s in ORDER]):
    keys = {s: c[0] for s, c in zip(ORDER, combo)}
    text = " ".join(c[1] for c in combo if c[1])
    tot, parts, m = score(text, keys)
    best.append((tot, keys, parts, m, text))
best.sort(key=lambda x: -x[0])
print(f"searched {len(best):,} combinations\n")
print(f"{'#':>3} {'score':>6} {'words':>6} {'Flesch':>7} {'dens':>6} {'pct':>5}  slots")
for i, (tot, keys, parts, m, text) in enumerate(best[:8], 1):
    print(f"{i:>3} {tot:>6.1f} {m['words']:>6} {m['flesch']:>7.1f} {m['dens']:>6.2f} {pctile(m['dens'],CD):>4.0f}%  "
          + " ".join(f"{k}={v}" for k, v in keys.items()))

import statistics as _st
sc=[b[0] for b in best]
print(f"\nSCORE DISTRIBUTION over {len(sc):,} combinations")
print(f"   best {sc[0]:.2f} | rank10 {sc[9]:.2f} | rank100 {sc[99]:.2f} | rank1000 {sc[999]:.2f}")
print(f"   median {_st.median(sc):.2f} | worst {sc[-1]:.2f} | sd {_st.pstdev(sc):.2f}")
print(f"   gap best-to-rank100: {sc[0]-sc[99]:.2f} points, which is {(sc[0]-sc[99])/_st.pstdev(sc):.2f} sd")
print(f"   combinations within 1.0 point of the best: {sum(1 for x in sc if x >= sc[0]-1.0)}")
print(f"   distinct slot choices among the top 20:")
for _s in ORDER:
    vals=set(b[1][_s] for b in best[:20])
    print(f"      {_s:<9}{'CONVERGED -> '+list(vals)[0] if len(vals)==1 else 'varies: '+', '.join(sorted(vals))}")
print("\nTOP RESULT, component scores:")
tot, keys, parts, m, text = best[0]
for k, v in parts.items(): print(f"   {k:<12}{v:>7.1f}")
print(f"\n{text}\n")
open('.workspace/scratch/abstract_search_top.txt','w').write(text)
