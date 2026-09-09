import re, os, json, random, subprocess, time, sys, html as htmlmod

VOLS = {'2026.acl-long':20, '2026.findings-acl':16, '2026.eacl-long':8, '2026.acl-short':4}
ids_by_vol = {}
for v in VOLS:
    h = open(f'/tmp/vol_{v}.html', encoding='utf-8').read()
    ids = sorted({int(m) for m in re.findall(r'href=/'+re.escape(v)+r'\.(\d+)/', h)})
    ids = [i for i in ids if i != 0]  # drop front matter
    ids_by_vol[v] = ids

# Systematic sample: fixed seed, random start, constant stride across the ordered volume.
rng = random.Random(20260906)
sample = []
for v, k in VOLS.items():
    ids = ids_by_vol[v]
    stride = len(ids)/k
    start = rng.random()*stride
    picks = [ids[min(int(start + j*stride), len(ids)-1)] for j in range(k)]
    picks = sorted(set(picks))
    sample += [f'{v}.{p}' for p in picks]
    print(v, 'N=', len(ids), 'stride=%.1f'%stride, 'picked', len(picks), file=sys.stderr)

os.makedirs('/tmp/aclfetch/pages', exist_ok=True)
for aid in sample:
    fp = f'/tmp/aclfetch/pages/{aid}.html'
    if os.path.exists(fp) and os.path.getsize(fp) > 5000: continue
    subprocess.run(['curl','-s','--max-time','30','-o',fp,f'https://aclanthology.org/{aid}/'])
    time.sleep(0.4)
json.dump(sample, open('/tmp/aclfetch/sample_ids.json','w'), indent=1)
print('fetched', len(sample), file=sys.stderr)
