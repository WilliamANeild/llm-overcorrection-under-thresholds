# Written 2026-09-06 for paper/reference/scen_06_openings_closings.md.
# Run order is the numeric prefix. Scripts 01-05 and 07 read and write in the directory
# they live in plus a ./pages subdirectory of fetched HTML; they were run from a scratch
# directory, so set the working directory before rerunning. Fetched abstracts and their
# provenance are stored in paper/reference/acl2026_abstracts.json under the keys
# sample_2026_09_06_wave2 and arxiv_cs_cl_2026_09_06.
import re,os,json,html as H
S=os.path.dirname(os.path.abspath(__file__))
def strip_tags(s):
    s=re.sub(r'<[^>]+>','',s); s=H.unescape(s); s=s.replace(' ',' ')
    return re.sub(r'\s+',' ',s).strip()
def get_abstract(h):
    m=re.search(r'<div[^>]*class="[^"]*acl-abstract[^"]*"[^>]*>',h) or re.search(r'<div[^>]*class=[^ >]*acl-abstract[^ >]*[^>]*>',h)
    if not m: return None
    i=m.end(); depth=1; j=i
    for t in re.finditer(r'<(/?)div\b',h[i:]):
        depth+=1 if t.group(1)=='' else -1
        if depth==0: j=i+t.start(); break
    inner=re.sub(r'<h5[^>]*>.*?</h5>','',h[i:j],flags=re.S)
    return strip_tags(inner)
def get_title(h):
    m=re.search(r'<h2[^>]*id=title[^>]*>(.*?)</h2>',h,re.S)
    if m: return strip_tags(m.group(1))
    m=re.search(r'<title>(.*?)</title>',h,re.S)
    return strip_tags(m.group(1)).replace(' - ACL Anthology','')
out={}; fails=[]
for aid in json.load(open(f'{S}/s1_ids.json'))['ids']:
    fp=f'{S}/pages/{aid}.html'
    if not os.path.exists(fp): fails.append((aid,'nofile')); continue
    h=open(fp,encoding='utf-8',errors='replace').read()
    a=get_abstract(h)
    if not a or len(a.split())<30: fails.append((aid,'noabs' if not a else 'short:%d'%len(a.split()))); continue
    out[aid]={'id':aid,'source':'ACL Anthology','title':get_title(h),'abstract':a,'url':f'https://aclanthology.org/{aid}/','retrieved':'2026-09-06'}
json.dump(out,open(f'{S}/s1_extracted.json','w'),indent=1,ensure_ascii=False)
print('extracted',len(out),'failed',fails)
