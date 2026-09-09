# -*- coding: utf-8 -*-
"""Length-versus-density analysis over the 67-abstract systematic ACL-2026 corpus.

Extends the 47-abstract draw of 2026-09-06 with a second interleaved systematic
draw of 20 (seed 20260907, retrieved 2026-09-06). Every count, correlation,
percentile and beat tally printed here is produced by this script. Three things
are hand-adjudicated and marked HAND wherever they appear: the enumerator
override list, the long-and-sparse word-spend reading, and the beat spot-check.

Reads:  paper/reference/acl2026_abstracts.json, keys sample_2026_09_06 (47) and
        sample2_2026_09_06 (20). Batch B is drawn and stored by 04_sample_and_fetch_batch2.py.
Writes: <scratch>/analysis67.json, and prints the analysis block used to build
        paper/reference/scen_04_length_density.md
"""
import json, re, math, os, sys, statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SCRATCH = os.environ.get('ACL_SCRATCH', '/private/tmp/claude-501/-Users-liamneild-Desktop-School-llm-overcorrection-under-thresholds/00744317-e5e0-44e6-9b65-e83966797521/scratchpad')

# ---- reuse the 2026-09-06 measurement code verbatim -------------------------
_src = open(os.path.join(HERE, '03_measure.py')).read().split('if __name__')[0]
_ns = {}
exec(_src, _ns)
measure, sentences, words = _ns['measure'], _ns['sentences'], _ns['words']

# ---- HAND: enumerator override ---------------------------------------------
# 03_measure.py tags a digit run as an enumeration marker only when it is wrapped
# in parentheses on both sides, so the half-parenthesised list form "two critical
# challenges: 1) ... and 2) ..." was scored as two statistics. A sweep of every
# quant-tagged run in all 67 abstracts (printed by --dump-runs) found this form in
# exactly one abstract. The rule below catches it: a bare one- or two-digit
# integer immediately followed by ")" whose left neighbour is not "(".
ENUM_HALF = re.compile(r'(?<!\()\b\d{1,2}\)')
def enum_override_spans(t):
    return {m.start() for m in ENUM_HALF.finditer(t)}

def measure_fixed(t):
    d = measure(t)
    bad = enum_override_spans(t)
    if not bad:
        d['enum_override'] = 0
        return d
    # rebuild the run list, demoting the overridden runs
    DIGITRUN = _ns['DIGITRUN']; classify_run = _ns['classify_run']; cats_for = _ns['cats_for']
    runs = []
    for m in DIGITRUN.finditer(t):
        k = classify_run(t, m)
        if m.start() in bad and k == 'quant':
            k = 'enum'
        runs.append({'text': m.group(0), 'start': m.start(), 'end': m.end(), 'kind': k})
    quant = [r for r in runs if r['kind'] == 'quant']
    for r in quant: r['cats'] = cats_for(t, r)
    nw = d['n_words']
    d['enum_override'] = len(bad)
    d['digit_runs_enumeration'] += len(bad)
    d['numerals_quant'] = len(quant)
    d['numerals_per_100w'] = round(100*len(quant)/nw, 2)
    for key, tag in [('cat_result_percentage','percentage'), ('cat_sample_size_count','sample_size'),
                     ('cat_p_value','p_value'), ('cat_effect_size','effect_size'),
                     ('cat_scale_level','scale_level'), ('cat_model_task_dataset_count','mtd_count'),
                     ('cat_ratio_multiplier','ratio_multiplier'), ('cat_model_size','model_size'),
                     ('cat_metric_score','metric_score'), ('cat_unclassified','other')]:
        d[key] = sum(tag in r['cats'] for r in quant)
    d['run_detail'] = [f"{r['text']}[{r['kind']}{'|'+','.join(r['cats']) if r['kind']=='quant' else ''}]" for r in runs]
    return d

# ---- stats helpers ----------------------------------------------------------
def q(v, p):
    s = sorted(v); k = (len(s)-1)*p; f = math.floor(k); c = math.ceil(k)
    return s[f] if f == c else s[f] + (s[c]-s[f])*(k-f)
def pearson(x, y):
    mx, my = st.mean(x), st.mean(y)
    sx = math.sqrt(sum((a-mx)**2 for a in x)); sy = math.sqrt(sum((b-my)**2 for b in y))
    return float('nan') if sx == 0 or sy == 0 else sum((a-mx)*(b-my) for a, b in zip(x, y))/(sx*sy)
def rank(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0]*len(v); i = 0
    while i < len(o):
        j = i
        while j+1 < len(o) and v[o[j+1]] == v[o[i]]: j += 1
        a = (i+j)/2 + 1
        for k in range(i, j+1): r[o[k]] = a
        i = j+1
    return r
def spearman(x, y): return pearson(rank(x), rank(y))
def _betacf(a, b, x):
    FPMIN = 1e-300; qab = a+b; qap = a+1; qam = a-1; c = 1.0; d = 1-qab*x/qap
    d = FPMIN if abs(d) < FPMIN else d; d = 1/d; h = d
    for m in range(1, 400):
        m2 = 2*m; aa = m*(b-m)*x/((qam+m2)*(a+m2))
        d = 1+aa*d; d = FPMIN if abs(d) < FPMIN else d
        c = 1+aa/c; c = FPMIN if abs(c) < FPMIN else c
        d = 1/d; h *= d*c
        aa = -(a+m)*(qab+m)*x/((a+m2)*(qap+m2))
        d = 1+aa*d; d = FPMIN if abs(d) < FPMIN else d
        c = 1+aa/c; c = FPMIN if abs(c) < FPMIN else c
        d = 1/d; de = d*c; h *= de
        if abs(de-1) < 3e-16: break
    return h
def _betai(a, b, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)+a*math.log(x)+b*math.log(1-x))
    return bt*_betacf(a, b, x)/a if x < (a+1)/(a+b+2) else 1-bt*_betacf(b, a, 1-x)/b
def corr_p(r, n):
    if n < 3 or abs(r) >= 1: return 0.0
    t = r*math.sqrt((n-2)/(1-r*r)); df = n-2
    return _betai(df/2, 0.5, df/(df+t*t))
def fisher_ci(r, n, z=1.959963985):
    zr = 0.5*math.log((1+r)/(1-r)); se = 1/math.sqrt(n-3)
    lo, hi = zr-z*se, zr+z*se
    return (round(math.tanh(lo), 3), round(math.tanh(hi), 3))

# ---- beat detectors ---------------------------------------------------------
# Sentence-level. A sentence may carry several beats; presence is per abstract.
BEATS = [
 ('problem',   re.compile(r'\b(?:have (?:demonstrated|shown|emerged|become)|has (?:emerged|become|shown)|are (?:widely|increasingly|now)|is (?:widely|increasingly|a )|increasingly|recent(?:ly)? (?:advance|work|progress|LLM)|plays? a|serves? as|enable[sd]?\b|offers?\b)', re.I)),
 ('gap',       re.compile(r'\b(?:however|yet\b|nevertheless|but\b|remains?\b|still\b|limited|limitation|fail(?:s|ure|ed)?|lack(?:s|ing)?|struggle|underexplored|under-explored|overlook|neglect|challenge|difficult|bottleneck|poorly|little (?:is|work|attention)|absent|scarc|insufficient|brittle|unclear|unresolved|expensive|costly|prohibitiv)', re.I)),
 ('artifact',  None),   # from measure(): coined name + an introducing verb
 ('method',    re.compile(r'\b(?:we (?:propose|introduce|present|develop|design|build|construct|formulate)|our (?:method|approach|framework|model|system)|consists? of|comprises?|combines?|integrat(?:es|ing)|leverag(?:es|ing)|employ(?:s|ing)|module|component|stage|two-stage|pipeline|loss\b|objective\b|training|fine-?tun|decod(?:er|ing)|encoder|attention|reward|first\b.*\bthen\b|mechanism|algorithm|strategy)', re.I)),
 ('setup',     re.compile(r'\b(?:experiments?\b|we evaluate|evaluation(?:s)? on|evaluat(?:ed|ing) (?:on|across)|we (?:test|benchmark|assess|conduct)|benchmark\w* (?:on|across)|across \w+ (?:benchmarks?|datasets?|models?|tasks?|languages?|domains?)|on (?:\w+ )?(?:benchmarks?|datasets?)\b|human evaluation|annotat)', re.I)),
 ('result',    re.compile(r'\b(?:outperform|improv(?:es|ed|ement)|achiev(?:es|ed|ing)|surpass|exceed|boost|reduc(?:es|ed|ing)|gains?\b|results? (?:show|demonstrate|indicate|reveal)|(?:show|demonstrate|indicate|reveal)s? that|effective|superior|state-of-the-art|consistently|yield)', re.I)),
 ('quant_result', None),  # >=1 quant numeral in a result-bearing category
 ('ablation',  re.compile(r'\b(?:ablation|further(?: analysis| experiments| investigation)|error analysis|we further|additional (?:analysis|experiments)|analys(?:is|es) (?:show|reveal|indicate|of)|case stud|probing|attribut(?:ion|e) analysis|disabling|removing)', re.I)),
 ('implication', re.compile(r'\b(?:suggest(?:s|ing)?|implication|highlight(?:s|ing)?|underscore|paves? the way|future work|we hope|call(?:s)? for|our findings|point(?:s)? to|open(?:s)? (?:up )?(?:new|a)|offers? (?:a )?(?:new )?(?:perspective|direction)|motivat(?:es|ing)|argue|position|standard practice|should be)', re.I)),
 ('release',   re.compile(r'\b(?:publicly available|open-?sourc|will be released|are released|we release|code and (?:data|models)|our code|dataset and code|available at|to facilitate (?:further|future))', re.I)),
]
RESULT_CATS = ('percentage', 'metric_score', 'ratio_multiplier')

def beat_flags(rec):
    t = rec['abstract']
    f = {}
    for name, rx in BEATS:
        if name == 'artifact':
            f[name] = bool(rec['names_artifact'])
        elif name == 'quant_result':
            f[name] = any(any(c in r for c in RESULT_CATS) for r in rec['run_detail'] if '[quant|' in r)
        else:
            f[name] = bool(rx.search(t))
    return f

def sentence_beats(rec):
    """Assign each sentence to at most one beat, by a fixed priority, for the
    word-spend tally. Priority runs from the most specific beat to the least."""
    order = ['release', 'quant_result', 'ablation', 'implication', 'setup', 'result', 'method', 'gap', 'problem']
    rx = {n: r for n, r in BEATS if r is not None}
    out = []
    for s in sentences(rec['abstract']):
        hit = None
        has_num = bool(re.search(r'\d', s)) and any(c in ''.join(rec['run_detail']) for c in RESULT_CATS)
        for n in order:
            if n == 'quant_result':
                if re.search(r'\d+(?:\.\d+)?\s*(?:%|×|x\b|percent)', s): hit = n; break
                continue
            if n in rx and rx[n].search(s): hit = n; break
        out.append((hit or 'other', len(words(s)), s))
    return out

# ---- load -------------------------------------------------------------------
def load():
    J = json.load(open(os.path.join(ROOT, 'paper/reference/acl2026_abstracts.json')))
    A = J['sample_2026_09_06']
    B = J.get('sample2_2026_09_06') or json.load(open(os.path.join(SCRATCH, 'extracted2.json')))
    R = {}
    for a, r in A.items(): R[a] = dict(r, batch='A', **measure_fixed(r['abstract']))
    for a, r in B.items(): R[a] = dict(r, batch='B', **measure_fixed(r['abstract']))
    # HAND: apply the adjudicated artifact-naming overrides
    hc = json.load(open(os.path.join(HERE, 'handcode_artifact_naming_67.json')))
    for a in hc['false_negatives_now_named']:
        R[a]['names_artifact'] = True
    for a in hc['false_positives_now_unnamed']:
        R[a]['names_artifact'] = False
    for a in R: R[a]['beats'] = beat_flags(R[a])
    return R

def main():
    R = load()
    if '--dump-runs' in sys.argv:
        for a in sorted(R):
            t = R[a]['abstract']
            for d in R[a]['run_detail']:
                if '[quant' in d: print(a, d)
        return
    ids = sorted(R, key=lambda a: R[a]['n_words'])
    W = [R[a]['n_words'] for a in ids]; Dn = [R[a]['numerals_per_100w'] for a in ids]
    Q = [R[a]['numerals_quant'] for a in ids]
    o = {'n': len(ids), 'n_batchA': sum(R[a]['batch'] == 'A' for a in ids),
         'n_batchB': sum(R[a]['batch'] == 'B' for a in ids)}
    pct = lambda v: {k: round(q(v, p), 2) for k, p in
                     [('min',0),('p25',.25),('median',.5),('p75',.75),('p90',.9),('max',1)]}
    o['words'] = dict(pct(W), mean=round(st.mean(W),1))
    o['density'] = dict(pct(Dn), mean=round(st.mean(Dn),3))
    o['sentences'] = dict(pct([R[a]['n_sentences'] for a in ids]), mean=round(st.mean([R[a]['n_sentences'] for a in ids]),1))
    o['zero_digit'] = sum(1 for a in ids if R[a]['numerals_quant'] == 0)

    def cor(x, y, label):
        r = pearson(x, y); s = spearman(x, y); n = len(x)
        return {'pearson': round(r,3), 'pearson_p': round(corr_p(r,n),5), 'pearson_ci95': fisher_ci(r,n),
                'spearman': round(s,3), 'spearman_p': round(corr_p(s,n),5), 'n': n, 'what': label}
    o['corr_words_vs_density'] = cor(W, Dn, 'words vs quantitative numerals per 100 words, all 67')
    o['corr_words_vs_count']   = cor(W, Q, 'words vs raw quantitative numeral count, all 67')
    nz = [a for a in ids if R[a]['numerals_quant'] > 0]
    o['corr_words_vs_density_nonzero'] = cor([R[a]['n_words'] for a in nz], [R[a]['numerals_per_100w'] for a in nz],
                                             'words vs density, restricted to abstracts carrying >=1 numeral')
    o['corr_words_vs_hasnumeral'] = cor(W, [1.0 if R[a]['numerals_quant'] else 0.0 for a in ids],
                                        'point-biserial: words vs carries-any-numeral')
    o['median_words_by_hasnumeral'] = {
        'has_numeral': {'n': len(nz), 'median': round(q([R[a]['n_words'] for a in nz], .5),1)},
        'no_numeral': {'n': len(ids)-len(nz), 'median': round(q([R[a]['n_words'] for a in ids if R[a]['numerals_quant']==0], .5),1)}}

    med = q(W, .5); p75 = q(Dn, .75)
    o['thresholds'] = {'median_words': med, 'p75_density': round(p75, 3)}
    o['short_dense'] = [a for a in ids if R[a]['n_words'] < med and R[a]['numerals_per_100w'] > p75]
    o['long_sparse_zero'] = [a for a in ids if R[a]['n_words'] > med and R[a]['numerals_quant'] == 0]
    o['quadrants'] = {}
    for L in (0,1):
        for Dd in (0,1):
            o['quadrants']['%s_%s' % ('long' if L else 'short', 'dense' if Dd else 'sparse')] = sum(
                1 for a in ids if (R[a]['n_words'] >= med) == bool(L) and (R[a]['numerals_per_100w'] > p75) == bool(Dd))
    # frontier: densest abstract at or below each length
    fr = []
    best = -1
    for a in ids:
        if R[a]['numerals_per_100w'] > best:
            best = R[a]['numerals_per_100w']; fr.append((a, R[a]['n_words'], best))
    o['frontier'] = fr

    # word cost of a figure
    b = {'0': [], '1': [], '2': [], '3+': []}
    for a in ids:
        k = R[a]['numerals_quant']
        b['0' if k==0 else '1' if k==1 else '2' if k==2 else '3+'].append(R[a]['n_words'])
    o['words_by_numeral_count'] = {k: {'n': len(v), 'median': round(q(v,.5),1), 'mean': round(st.mean(v),1),
                                       'p25': round(q(v,.25),1), 'p75': round(q(v,.75),1), 'min': min(v), 'max': max(v)}
                                   for k, v in b.items()}
    p = {'0': [], '1': [], '2+': []}
    for a in ids:
        k = R[a]['cat_result_percentage']
        p['0' if k==0 else '1' if k==1 else '2+'].append(R[a]['n_words'])
    o['words_by_result_pct'] = {k: {'n': len(v), 'median': round(q(v,.5),1), 'mean': round(st.mean(v),1)} for k, v in p.items()}

    # word cost of naming
    for key, test in [('artifact', lambda r: r['names_artifact']),
                      ('metric',   lambda r: bool(r['names_metrics'])),
                      ('dataset',  lambda r: bool(r['names_datasets'])),
                      ('model',    lambda r: bool(r['names_models']))]:
        y = [R[a]['n_words'] for a in ids if test(R[a])]; n = [R[a]['n_words'] for a in ids if not test(R[a])]
        dy=[R[a]['numerals_per_100w'] for a in ids if test(R[a])]; dn=[R[a]['numerals_per_100w'] for a in ids if not test(R[a])]
        o['density_by_naming_'+key] = {'named': round(q(dy,.5),2) if dy else None, 'unnamed': round(q(dn,.5),2) if dn else None,
                                       'named_mean': round(st.mean(dy),2) if dy else None, 'unnamed_mean': round(st.mean(dn),2) if dn else None}
        if key == 'artifact': o['ids_unnamed_artifact'] = [a for a in ids if not test(R[a])]
        o['words_by_naming_'+key] = {
            'named': {'n': len(y), 'median': round(q(y,.5),1), 'mean': round(st.mean(y),1)} if y else None,
            'unnamed': {'n': len(n), 'median': round(q(n,.5),1), 'mean': round(st.mean(n),1)} if n else None}
    # count of distinct named acronyms vs length
    nac = [len(R[a]['named_acronyms']) for a in ids]
    o['corr_words_vs_n_acronyms'] = cor(W, [float(x) for x in nac], 'words vs count of distinct coined names')
    ab = {'0': [], '1': [], '2': [], '3+': []}
    for a in ids:
        k = len(R[a]['named_acronyms'])
        ab['0' if k==0 else '1' if k==1 else '2' if k==2 else '3+'].append(R[a]['n_words'])
    o['words_by_n_acronyms'] = {k: {'n': len(v), 'median': round(q(v,.5),1)} for k, v in ab.items() if v}

    # beats
    names = [n for n, _ in BEATS]
    o['beat_prevalence_all'] = {n: sum(R[a]['beats'][n] for a in ids) for n in names}
    BANDS = [('<=140', lambda w: w <= 140), ('141-160', lambda w: 141 <= w <= 160),
             ('161-180', lambda w: 161 <= w <= 180), ('>180', lambda w: w > 180)]
    o['beat_by_band'] = {}
    for lbl, f in BANDS:
        sub = [a for a in ids if f(R[a]['n_words'])]
        o['beat_by_band'][lbl] = {'n': len(sub), 'beats': {n: sum(R[a]['beats'][n] for a in sub) for n in names},
                                  'share': {n: round(100*sum(R[a]['beats'][n] for a in sub)/len(sub),0) for n in names},
                                  'median_words': round(q([R[a]['n_words'] for a in sub], .5),1),
                                  'median_sent': round(q([R[a]['n_sentences'] for a in sub], .5),1),
                                  'median_density': round(q([R[a]['numerals_per_100w'] for a in sub], .5),2)}
    # target band 150-180
    tgt = [a for a in ids if 150 <= R[a]['n_words'] <= 180]
    o['band_150_180'] = {'n': len(tgt), 'ids': tgt,
        'median_words': round(q([R[a]['n_words'] for a in tgt],.5),1),
        'median_sent': round(q([R[a]['n_sentences'] for a in tgt],.5),1),
        'median_density': round(q([R[a]['numerals_per_100w'] for a in tgt],.5),2),
        'p75_density': round(q([R[a]['numerals_per_100w'] for a in tgt],.75),2),
        'max_density': round(max(R[a]['numerals_per_100w'] for a in tgt),2),
        'zero_digit': sum(1 for a in tgt if R[a]['numerals_quant']==0),
        'beats': {n: sum(R[a]['beats'][n] for a in tgt) for n in names},
        'beat_share': {n: round(100*sum(R[a]['beats'][n] for a in tgt)/len(tgt)) for n in names},
        'n_beats_median': round(q([sum(R[a]['beats'].values()) for a in tgt],.5),1),
        'words_per_sentence': round(st.mean([R[a]['n_words']/R[a]['n_sentences'] for a in tgt]),1)}
    # beats carried, by length
    o['corr_words_vs_nbeats'] = cor(W, [float(sum(R[a]['beats'].values())) for a in ids], 'words vs number of beats present')
    o['nbeats_by_band'] = {lbl: round(q([sum(R[a]['beats'].values()) for a in ids if f(R[a]['n_words'])],.5),1)
                           for lbl, f in BANDS}
    # drop order: rank beats by (share in shortest band) and by slope across bands
    drop = []
    for n in names:
        sh = [o['beat_by_band'][lbl]['share'][n] for lbl, _ in BANDS]
        drop.append({'beat': n, 'share_by_band': sh, 'shortest_band_share': sh[0],
                     'drop_shortest_vs_longest': round(sh[-1]-sh[0], 0)})
    drop.sort(key=lambda d: (d['shortest_band_share'], -d['drop_shortest_vs_longest']))
    o['drop_order'] = drop

    # word spend for the long-and-sparse set
    spend = {}
    for a in o['long_sparse_zero']:
        sb = sentence_beats(R[a])
        agg = {}
        for beat, nwd, _ in sb: agg[beat] = agg.get(beat, 0) + nwd
        spend[a] = {'words': R[a]['n_words'], 'sent': R[a]['n_sentences'],
                    'by_beat': {k: v for k, v in sorted(agg.items(), key=lambda x: -x[1])},
                    'share': {k: round(100*v/R[a]['n_words']) for k, v in sorted(agg.items(), key=lambda x: -x[1])}}
    o['long_sparse_spend'] = spend
    tot = {}
    for a, v in spend.items():
        for k, w in v['by_beat'].items(): tot[k] = tot.get(k, 0) + w
    S = sum(tot.values())
    o['long_sparse_spend_pooled'] = {k: {'words': v, 'share': round(100*v/S)} for k, v in sorted(tot.items(), key=lambda x: -x[1])}
    # same tally for the dense abstracts, for contrast
    dense = [a for a in ids if R[a]['numerals_per_100w'] > p75]
    tot2 = {}
    for a in dense:
        for beat, nwd, _ in sentence_beats(R[a]): tot2[beat] = tot2.get(beat, 0) + nwd
    S2 = sum(tot2.values())
    o['dense_spend_pooled'] = {k: {'words': v, 'share': round(100*v/S2)} for k, v in sorted(tot2.items(), key=lambda x: -x[1])}
    o['dense_ids'] = dense

    json.dump({'analysis': o, 'rows': R}, open(os.path.join(SCRATCH, 'analysis67.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps(o, indent=1))

if __name__ == '__main__':
    main()
