# Written 2026-09-06 for paper/reference/scen_06_openings_closings.md.
# Run order is the numeric prefix. Scripts 01-05 and 07 read and write in the directory
# they live in plus a ./pages subdirectory of fetched HTML; they were run from a scratch
# directory, so set the working directory before rerunning. Fetched abstracts and their
# provenance are stored in paper/reference/acl2026_abstracts.json under the keys
# sample_2026_09_06_wave2 and arxiv_cs_cl_2026_09_06.
import re,json,os
S=os.path.dirname(os.path.abspath(__file__))
t=open('/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/reference/neighbor_abstracts.md',encoding='utf-8').read()
blocks=re.split(r'\n## ',t)
out=[]
for b in blocks[1:]:
    lines=b.split('\n')
    head=lines[0].strip()
    m=re.match(r'^(\d+)\.\s*(.*?)\s*\(arXiv:([0-9.]+)\)\s*$',head)
    if not m: print('SKIP HEAD:',head[:90]); continue
    num,titleline,aid=m.groups()
    rest=[l.strip() for l in lines[1:] if l.strip() and not l.startswith('#')]
    # first non-empty line is the author list; abstract is the longest remaining paragraph
    body=[l for l in rest[1:] if len(l.split())>25]
    if not body: print('SKIP BODY:',head[:60]); continue
    out.append({'id':'arXiv:'+aid,'source':'neighbor corpus (topical)','num':int(num),
                'title':titleline,'abstract':max(body,key=len),
                'url':'https://arxiv.org/abs/'+aid,'retrieved':'2026-09-02'})
json.dump(out,open(f'{S}/s3_neighbors.json','w'),indent=1,ensure_ascii=False)
print('parsed',len(out))
