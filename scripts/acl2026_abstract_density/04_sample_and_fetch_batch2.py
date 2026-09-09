"""Second interleaved systematic draw over the same four 2026 volumes, seed 20260907.

Extends the 2026-09-06 corpus from 47 to 67 abstracts for the length-versus-density
analysis. Excludes every ID already in sample_2026_09_06 and 2026.findings-acl.1664,
which has no abstract block; where a draw index lands on an excluded ID the next
unused index in volume order is taken. Fetches the landing pages, extracts the
abstracts with 02_extract_abstracts.py's parser, and writes them into
paper/reference/acl2026_abstracts.json under sample2_2026_09_06.

Run once. Re-running re-fetches and overwrites, which changes the retrieval date.
"""
import re, os, json, random, subprocess, time, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
WORK = os.environ.get('ACL_SCRATCH', os.path.join(ROOT, '.workspace', 'scratch', 'aclfetch2'))
JSON = os.path.join(ROOT, 'paper/reference/acl2026_abstracts.json')
VOLS = {'2026.acl-long': 8, '2026.findings-acl': 7, '2026.eacl-long': 3, '2026.acl-short': 2}
SEED = 20260907

os.makedirs(os.path.join(WORK, 'pages'), exist_ok=True)
prior = set(json.load(open(JSON))['sample_2026_09_06'])
prior.add('2026.findings-acl.1664')

ids_by_vol = {}
for v in VOLS:
    fp = os.path.join(WORK, 'vol_%s.html' % v)
    if not os.path.exists(fp) or os.path.getsize(fp) < 50000:
        subprocess.run(['curl', '-s', '--max-time', '60', '-o', fp, 'https://aclanthology.org/volumes/%s/' % v])
    h = open(fp, encoding='utf-8').read()
    ids = sorted({int(m) for m in re.findall(r'href=["\']?/' + re.escape(v) + r'\.(\d+)/', h)})
    ids_by_vol[v] = [i for i in ids if i != 0]

rng = random.Random(SEED)
sample, strides = [], {}
for v, k in VOLS.items():
    ids = ids_by_vol[v]; stride = len(ids)/k; start = rng.random()*stride
    picks = []
    for j in range(k):
        idx = min(int(start + j*stride), len(ids)-1)
        while idx < len(ids) and (('%s.%d' % (v, ids[idx])) in prior or ids[idx] in picks): idx += 1
        if idx < len(ids): picks.append(ids[idx])
    sample += ['%s.%d' % (v, p) for p in sorted(picks)]
    strides[v] = {'N': len(ids), 'k': k, 'stride': round(stride, 1), 'picked': len(picks)}
    print(v, len(ids), 'stride=%.1f' % stride, len(picks), file=sys.stderr)

for aid in sample:
    fp = os.path.join(WORK, 'pages', aid + '.html')
    if os.path.exists(fp) and os.path.getsize(fp) > 5000: continue
    subprocess.run(['curl', '-s', '--max-time', '30', '-o', fp, 'https://aclanthology.org/%s/' % aid])
    time.sleep(0.4)

_src = open(os.path.join(HERE, '02_extract_abstracts.py')).read().split('out = {}')[0]
_ns = {}; exec(_src, _ns)
out, fails = {}, []
for aid in sample:
    fp = os.path.join(WORK, 'pages', aid + '.html')
    if not os.path.exists(fp): fails.append((aid, 'nofile')); continue
    h = open(fp, encoding='utf-8', errors='replace').read()
    a = _ns['get_abstract'](h)
    if not a or len(a.split()) < 30:
        fails.append((aid, 'noabs' if not a else 'short:%d' % len(a.split()))); continue
    out[aid] = {'anthology_id': aid, 'url': 'https://aclanthology.org/%s/' % aid,
                'title': _ns['get_title'](h), 'abstract': a}
json.dump(out, open(os.path.join(WORK, 'extracted2.json'), 'w'), indent=1, ensure_ascii=False)
print('extracted', len(out), 'failed', fails, file=sys.stderr)
print(json.dumps({'strides': strides, 'ids': sample}, indent=1))
