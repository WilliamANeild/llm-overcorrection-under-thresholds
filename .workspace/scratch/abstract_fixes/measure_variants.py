"""Score abstract variants against the 147-abstract ACL-venue corpus.

Same measurement code as .workspace/scratch/abstract_search.py so the numbers are
comparable with the header block in paper/sections/abstract_v2.tex.
Usage: python3 measure_variants.py <file> [<file> ...]
"""
import json, re, sys, statistics as st
from collections import Counter

ROOT = '/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/'
CORP = json.load(open(ROOT + 'paper/reference/acl2026_abstracts.json'))

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

def syll(w):
    w = re.sub(r'[^a-z]', '', w.lower())
    if not w: return 1
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1: n -= 1
    return max(1, n)

def sents_of(t):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if len(x.split()) > 3]

def measure(t):
    s, w = sents_of(t), t.split()
    return dict(words=len(w), sents=len(s), wps=len(w)/len(s),
        flesch=206.835 - 1.015*(len(w)/len(s)) - 84.6*(sum(syll(x) for x in w)/len(w)),
        dens=len(re.findall(r'(?<![\w.])\d[\d,.]*\s?%?', re.sub(MODEL, 'M', t)))/len(w)*100)

CW = sorted(measure(t)['words'] for t in A)
CS = sorted(measure(t)['sents'] for t in A)
CD = sorted(measure(t)['dens'] for t in A)
def pct(x, v): return sum(1 for a in v if a <= x)/len(v)*100

BAN = {'em dash': '—', 'en dash': '–', 'colon': ':', 'semicolon': ';'}
STOP = set("the a an and or of to in it is are that they them this these with as on for by "
           "not at be been was were do does can cannot what when whether their there here we "
           "run our its but so than then all any more most every each into over under".split())

def register(t):
    out = {k: t.count(v) for k, v in BAN.items()}
    out['we show'] = len(re.findall(r'we (show|demonstrate|prove)', t, re.I))
    out['sig adverb'] = len(re.findall(r'significantly|substantially|dramatically|remarkably|strikingly', t, re.I))
    out['not-X-but-Y'] = len(re.findall(r'\bnot .{1,40}\bbut\b', t))
    out['spelled frac'] = len(re.findall(r'\b(one|two|three|four|five|six|seven|eight|nine|ten) in (two|three|four|five|six|seven|eight|nine|ten)\b', t, re.I))
    out['prove'] = len(re.findall(r'\bprove', t, re.I))
    preps = {'of','in','on','to','for','with','at','by','from','about','into','over','under','between','through'}
    out['final prep'] = sum(1 for s in sents_of(t) if s.split()[-1].strip('.').lower() in preps)
    return out

def results_stats(t):
    """Percentages are result stats; bare counts of models/tasks/domains/turns are scale."""
    return len(re.findall(r'\d+\s?%', t))

rows = []
for f in sys.argv[1:]:
    t = open(f).read().strip()
    m, r = measure(t), register(t)
    words = [w.lower().strip('.,%;:') for w in t.split()]
    rep = [(w, n) for w, n in Counter(w for w in words if w not in STOP and len(w) > 3).most_common() if n >= 3]
    rows.append((f.split('/')[-1].replace('.txt',''), m, r, results_stats(t), rep))

print(f"CORPUS n={len(A)}   words med {st.median(CW):.0f} p90 {sorted(CW)[int(.9*len(CW))]:.0f} | "
      f"sents med {st.median(CS):.0f} p90 {sorted(CS)[int(.9*len(CS))]:.0f} | "
      f"dens med {st.median(CD):.2f} p90 {sorted(CD)[int(.9*len(CD))]:.2f}")
print()
hdr = f"{'variant':<16}{'words':>7}{'pct':>5}{'sent':>6}{'wps':>7}{'dens':>7}{'pct':>5}{'flesch':>8}{'res%':>6}{'reg':>5}"
print(hdr); print('-'*len(hdr))
for name, m, r, rs, rep in rows:
    bad = sum(r.values())
    print(f"{name:<16}{m['words']:>7}{pct(m['words'],CW):>5.0f}{m['sents']:>6}{m['wps']:>7.1f}"
          f"{m['dens']:>7.2f}{pct(m['dens'],CD):>5.0f}{m['flesch']:>8.1f}{rs:>6}{bad:>5}")
print("\nbands: words 150-200 | sents 7-9 | wps 22-26 | res% <=2 | reg must be 0")
for name, m, r, rs, rep in rows:
    viol = [k for k, v in r.items() if v]
    print(f"\n{name}: repetition 3+ {rep}")
    if viol: print(f"  REGISTER VIOLATIONS: {viol}")
