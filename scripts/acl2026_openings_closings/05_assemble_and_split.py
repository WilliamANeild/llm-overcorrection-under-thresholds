# Written 2026-09-06 for paper/reference/scen_06_openings_closings.md.
# Run order is the numeric prefix. Scripts 01-05 and 07 read and write in the directory
# they live in plus a ./pages subdirectory of fetched HTML; they were run from a scratch
# directory, so set the working directory before rerunning. Fetched abstracts and their
# provenance are stored in paper/reference/acl2026_abstracts.json under the keys
# sample_2026_09_06_wave2 and arxiv_cs_cl_2026_09_06.
import json,re,os
S=os.path.dirname(os.path.abspath(__file__))
R='/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/reference/'
J=json.load(open(R+'acl2026_abstracts.json'))
corpus=[]
for aid,d in J['sample_2026_09_06'].items():
    corpus.append({'key':aid,'stratum':'A','source':'ACL Anthology 2026 (systematic wave 1)','id':aid,
                   'url':d['url'],'title':d['title'],'abstract':d['abstract'],'retrieved':'2026-09-06',
                   'genre':d.get('genre'),'valence':d.get('result_valence')})
for aid,d in json.load(open(f'{S}/s1_extracted.json')).items():
    corpus.append({'key':aid,'stratum':'A2','source':'ACL Anthology 2026 (systematic wave 2)','id':aid,
                   'url':d['url'],'title':d['title'],'abstract':d['abstract'],'retrieved':'2026-09-06'})
NICK={'ZIP *SEM':'ZIP (*SEM)','CGM Findings':'CGM (Findings)','DART Findings':'DART (Findings)',
 'MemoryDial Findings':'MemoryDial (Findings)','DogCat EACL':'DogCat (EACL)','SAGE ACL':'SAGE (ACL)',
 'CommonToWhom ACL':'CommonToWhom (ACL)','ReasoningTraces ACL':'ReasoningTraces (ACL)','SCOPE ICML':'SCOPE (ICML)'}
for k,v in J.items():
    if k in NICK:
        corpus.append({'key':NICK[k],'stratum':'C','source':'prior topical set (2026-09-02)','id':NICK[k],
                       'url':None,'title':NICK[k],'abstract':re.sub(r'^>?\s*Abstract\s+','',v),'retrieved':'2026-09-02'})
if os.path.exists(f'{S}/s2_arxiv.json'):
    for d in json.load(open(f'{S}/s2_arxiv.json'))['rows']:
        corpus.append({'key':d['arxiv_id'],'stratum':'B','source':'arXiv cs.CL (systematic, month strata)','id':'arXiv:'+d['arxiv_id'],
                       'url':d['url'],'title':d['title'],'abstract':d['abstract'],'retrieved':'2026-09-06','stratum_month':d['stratum']})
for d in json.load(open(f'{S}/s3_neighbors.json')):
    corpus.append({'key':d['id'],'stratum':'D','source':'topical neighbour corpus','id':d['id'],
                   'url':d['url'],'title':d['title'],'abstract':d['abstract'],'retrieved':'2026-09-02'})

ABBR=r'(?:e\.g|i\.e|et al|vs|cf|Fig|Eq|Sec|approx|Dr|Prof|St|No|resp|etc|w\.r\.t|a\.k\.a|U\.S)'
def sents(t):
    t=re.sub(r'\s+',' ',t).strip()
    # protect
    t=re.sub(ABBR+r'\.', lambda m:m.group(0).replace('.','\x00'), t)
    t=re.sub(r'(\d)\.(\d)', '\\1\x00\\2', t)
    t=re.sub(r'\b([A-Z])\.(?=[A-Z]\.)', '\\1\x00', t)
    parts=re.split(r'(?<=[.!?])["”\)\]]*\s+(?=[A-Z\(“"\d])', t)
    # also split on sentence-final punctuation immediately followed by a capital (no space) - common in this corpus
    out=[]
    for p in parts:
        subs=re.split(r'(?<=[a-z\)\]\.%])\.(?=[A-Z][a-z])', p)
        if len(subs)>1:
            subs=[s if s.endswith(('.','!','?')) else s+'.' for s in subs[:-1]]+[subs[-1]]
        out+=subs
    return [s.replace('\x00','.').strip() for s in out if s.strip()]
for c in corpus:
    ss=sents(c['abstract'])
    c['sentences']=ss; c['n_sent']=len(ss); c['n_words']=len(c['abstract'].split())
    c['opening']=ss[0]; c['closing']=ss[-1]
json.dump(corpus,open(f'{S}/corpus.json','w'),indent=1,ensure_ascii=False)
from collections import Counter
print(Counter(c['stratum'] for c in corpus), len(corpus))
