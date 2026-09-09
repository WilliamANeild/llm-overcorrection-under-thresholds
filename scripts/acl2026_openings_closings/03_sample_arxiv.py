# Written 2026-09-06 for paper/reference/scen_06_openings_closings.md.
# Run order is the numeric prefix. Scripts 01-05 and 07 read and write in the directory
# they live in plus a ./pages subdirectory of fetched HTML; they were run from a scratch
# directory, so set the working directory before rerunning. Fetched abstracts and their
# provenance are stored in paper/reference/acl2026_abstracts.json under the keys
# sample_2026_09_06_wave2 and arxiv_cs_cl_2026_09_06.
import subprocess, re, json, time, random, os, sys, html as H
S=os.path.dirname(os.path.abspath(__file__))
months=['2025-01','2025-03','2025-05','2025-07','2025-09','2025-11','2026-01','2026-03','2026-05','2026-07']
rng=random.Random(20260906007); frac0=rng.random()
def curl(url):
    for a in range(5):
        r=subprocess.run(['curl','-sL','--max-time','60','-A','Mozilla/5.0 (abstract-rhetoric-survey; williamaneild@gmail.com)','-w','\\nHTTPCODE:%{http_code}',url],capture_output=True,text=True)
        b=r.stdout; code=b.rsplit('HTTPCODE:',1)[-1].strip()
        if code=='200': return b
        print('  retry',a,code,url[:80],file=sys.stderr); sys.stderr.flush(); time.sleep(8*(a+1))
    return None
rows=[]; fails=[]
for j,mo in enumerate(months):
    frac=(frac0+j/len(months))%1.0
    h=curl(f'https://arxiv.org/list/cs.CL/{mo}?skip=0&show=25')
    if h is None: fails.append([mo,'listing head failed']); continue
    tm=re.search(r'Total of ([\d,]+) entries',h)
    if not tm: fails.append([mo,'no total']); continue
    tot=int(tm.group(1).replace(',','')); idx=int(frac*tot); time.sleep(3)
    h=curl(f'https://arxiv.org/list/cs.CL/{mo}?skip={idx}&show=25')
    if h is None: fails.append([mo,'listing page failed at %d/%d'%(idx,tot)]); continue
    ids=re.findall(r'arXiv:(\d{4}\.\d{4,5})',h)
    if not ids: fails.append([mo,'no ids at skip=%d'%idx]); continue
    aid=ids[0]; time.sleep(3)
    p=curl(f'https://arxiv.org/abs/{aid}')
    if p is None: fails.append([mo,'abs page failed '+aid]); continue
    am=re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>',p,re.S)
    if not am: fails.append([mo,'no abstract block '+aid]); continue
    ab=re.sub(r'<span class="descriptor">Abstract:?</span>','',am.group(1))
    ab=H.unescape(re.sub(r'<[^>]+>','',ab)); ab=re.sub(r'\s+',' ',ab).strip()
    tt=re.search(r'<h1 class="title[^"]*">(.*?)</h1>',p,re.S)
    tt=H.unescape(re.sub(r'<[^>]+>','',tt.group(1))).replace('Title:','').strip() if tt else ''
    pc=re.search(r'<span class="primary-subject">(.*?)</span>',p)
    dt=re.search(r'\[Submitted on ([^\]<]+)',p)
    rows.append({'arxiv_id':aid,'title':re.sub(r'\s+',' ',tt),'abstract':ab,
                 'url':f'https://arxiv.org/abs/{aid}','stratum':mo,'frac':round(frac,4),
                 'index_in_stratum':idx,'stratum_total':tot,
                 'primary_category':(pc.group(1) if pc else ''),'submitted':(dt.group(1).strip() if dt else '')})
    print('%s tot=%d frac=%.3f idx=%d -> %s (%d words) %s'%(mo,tot,frac,idx,aid,len(ab.split()),rows[-1]['primary_category']),file=sys.stderr); sys.stderr.flush()
    json.dump({'rows':rows,'fails':fails,'frac0':frac0,'strata':months},open(f'{S}/s2_arxiv.json','w'),indent=1,ensure_ascii=False)
    time.sleep(4)
json.dump({'rows':rows,'fails':fails,'frac0':frac0,'strata':months},open(f'{S}/s2_arxiv.json','w'),indent=1,ensure_ascii=False)
print('DONE',len(rows),'fails',fails,file=sys.stderr)
