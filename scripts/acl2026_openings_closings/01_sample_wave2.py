# Written 2026-09-06 for paper/reference/scen_06_openings_closings.md.
# Run order is the numeric prefix. Scripts 01-05 and 07 read and write in the directory
# they live in plus a ./pages subdirectory of fetched HTML; they were run from a scratch
# directory, so set the working directory before rerunning. Fetched abstracts and their
# provenance are stored in paper/reference/acl2026_abstracts.json under the keys
# sample_2026_09_06_wave2 and arxiv_cs_cl_2026_09_06.
from pathlib import Path
import re, os, json, random, subprocess, time, sys
S=os.path.dirname(os.path.abspath(__file__))
EXIST=set(json.load(open(str(Path(__file__).resolve().parents[2] / 'paper/reference/acl2026_abstracts.json')))['sample_2026_09_06'].keys())
VOLS={'2026.acl-long':8,'2026.findings-acl':6,'2026.eacl-long':4,'2026.acl-short':2}
ids_by_vol={}
for v in VOLS:
    h=open(f'{S}/vol_{v}.html',encoding='utf-8').read()
    ids=sorted({int(m) for m in re.findall(r'href=/'+re.escape(v)+r'\.(\d+)/',h)})
    ids=[i for i in ids if i!=0]
    ids_by_vol[v]=ids
rng=random.Random(20260906007)
sample=[]; strides={}
for v,k in VOLS.items():
    ids=ids_by_vol[v]; stride=len(ids)/k; start=rng.random()*stride
    picks=[ids[min(int(start+j*stride),len(ids)-1)] for j in range(k)]
    picks=sorted(set(picks))
    cand=[f'{v}.{p}' for p in picks]
    # replace any collision with the existing sample by stepping one position forward in volume order
    out=[]
    for c in cand:
        if c in EXIST or c in out:
            n=int(c.split('.')[-1]); idx=ids.index(n)
            while True:
                idx=(idx+1)%len(ids); alt=f'{v}.{ids[idx]}'
                if alt not in EXIST and alt not in out: out.append(alt); break
        else: out.append(c)
    sample+=out
    strides[v]=f'{k} of {len(ids)}, stride {stride:.1f}'
    print(v,'N=',len(ids),'stride=%.1f'%stride,'picked',len(out),file=sys.stderr)
json.dump({'ids':sample,'strides':strides},open(f'{S}/s1_ids.json','w'),indent=1)
print(sample)
