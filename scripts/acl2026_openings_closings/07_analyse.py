# Written 2026-09-06 for paper/reference/scen_06_openings_closings.md.
# Run order is the numeric prefix. Scripts 01-05 and 07 read and write in the directory
# they live in plus a ./pages subdirectory of fetched HTML; they were run from a scratch
# directory, so set the working directory before rerunning. Fetched abstracts and their
# provenance are stored in paper/reference/acl2026_abstracts.json under the keys
# sample_2026_09_06_wave2 and arxiv_cs_cl_2026_09_06.
import json,re,sys,os
from collections import Counter,defaultdict
S=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,S)
from codes import CODES
C=json.load(open(f'{S}/corpus.json'))
for x in C:
    o,cl=CODES[x['key']]; x['open']=o; x['close_full']=cl
    x['close']=cl.split('/')[0]; x['close2']=cl.split('/')[1] if '/' in cl else None
    # mechanical: quantitative numeral count (same rule as the density file: exclude identifier/year digits)
    a=x['abstract']
    ident=set()
    for m in re.finditer(r'\b(?:19|20|26)\d{2}\b',a): ident.add(m.span())
    toks=[(m.group(0),m.span()) for m in re.finditer(r'\d[\d,\.]*',a)]
    q=0
    for t,sp in toks:
        ctx=a[max(0,sp[0]-14):sp[1]+14]
        if sp in ident: continue
        if re.search(r'[A-Za-z]-?$',a[:sp[0]][-2:] or ' ') and not re.search(r'[\s\(\[]$',a[:sp[0]][-1:]): pass
        q+=1
    x['digit_runs']=len(toks)
VEN=lambda x: x['stratum'] in ('A','A2','B','C')   # the venue-norm corpus (76+10=86)

def dist(rows,field):
    return Counter(r[field] for r in rows)

def show(title,rows):
    n=len(rows)
    print('\n==',title,'n=%d'%n)
    print(' OPEN :',sorted(dist(rows,'open').items(),key=lambda kv:-kv[1]))
    print(' CLOSE:',sorted(dist(rows,'close').items(),key=lambda kv:-kv[1]))

show('ALL',C)
show('VENUE (A+A2+B+C)',[r for r in C if VEN(r)])
show('ACL Anthology 2026 only (A+A2)',[r for r in C if r['stratum'] in ('A','A2')])
show('arXiv systematic (B)',[r for r in C if r['stratum']=='B'])
show('topical neighbours (D)',[r for r in C if r['stratum']=='D'])

# cross-tab
OP=['Q','DEF','SQ','PROB','SCENE','FIND','OTHER']
CLS=['KNOW_G','KNOW_A','CALL','FUTURE','RELEASE','CONTRIB','NAMED','PRACTICE','IMP','OTHER']
def xtab(rows,label):
    print('\n=== CROSS-TAB',label,'n=%d'%len(rows))
    t=Counter((r['open'],r['close']) for r in rows)
    hdr='open\\close  '+''.join('%-9s'%c for c in CLS)+'  tot'
    print(hdr)
    for o in OP:
        row=[t[(o,c)] for c in CLS]
        if sum(row)==0 and o not in ('Q',): continue
        print('%-11s'%o+''.join('%-9d'%v for v in row)+'  %d'%sum(row))
    print('%-11s'%'tot'+''.join('%-9d'%sum(t[(o,c)] for o in OP) for c in CLS)+'  %d'%len(rows))
    return t
tv=xtab([r for r in C if VEN(r)],'VENUE')
ta=xtab(C,'ALL 134')

# secondary-tag counts
print('\nsecondary close tags (all):',Counter(r['close2'] for r in C if r['close2']))

# opening length
print('\n== opening-sentence length in words, by opening type (all 134)')
by=defaultdict(list)
for r in C: by[r['open']].append(len(r['opening'].split()))
import statistics as st
for o in OP:
    v=sorted(by[o])
    if not v: continue
    print(' %-6s n=%-3d min=%-3d med=%-5.1f mean=%-5.1f max=%-3d  %s'%(o,len(v),v[0],st.median(v),sum(v)/len(v),v[-1],v))

print('\n== abstract length (words) and sentence count, by opening type (all 134)')
for o in OP:
    v=[r for r in C if r['open']==o]
    if not v: continue
    w=sorted(r['n_words'] for r in v); s=sorted(r['n_sent'] for r in v)
    d=sorted(r['digit_runs']/r['n_words']*100 for r in v)
    print(' %-6s n=%-3d words med=%-5.1f mean=%-5.1f | sent med=%-4.1f | digit-runs/100w med=%-5.2f mean=%-5.2f'%(
        o,len(v),st.median(w),sum(w)/len(w),st.median(s),st.median(d),sum(d)/len(d)))

# every sentence that is a question, anywhere
print('\n== QUESTION SENTENCES ANYWHERE (all 134)')
for r in C:
    for i,s in enumerate(r['sentences']):
        if s.rstrip().endswith('?'):
            print(' [%s] %s  sent %d/%d: %s'%(r['stratum'],r['key'],i+1,r['n_sent'],s))

# imperative scan
IMPV=set('Consider See Note Imagine Suppose Use Try Take Let Think Ask Read Stop Look Remember Recall Do Beware Compare Contrast Treat Build Design Start Begin Watch Check Avoid Adopt Apply Assume Picture Observe Notice Reconsider Rethink Stop Ensure Focus Keep Make Give Put Move Follow Choose Pick Test Measure Report Cite Prefer Resist Expect Suspend Withhold'.split())
print('\n== IMPERATIVE SCAN')
hits=[]
for r in C:
    for i,s in enumerate(r['sentences']):
        w=re.match(r'^([A-Z][a-z\']+)\b',s)
        if w and w.group(1) in IMPV:
            hits.append((r['stratum'],r['key'],i+1,r['n_sent'],s))
print(' sentence-initial base-form-verb candidates (whole abstract):',len(hits))
for h in hits: print('  ',h[0],h[1],'sent %d/%d:'%(h[2],h[3]),h[4][:170])
print(' in the CLOSING sentence only:',sum(1 for h in hits if h[2]==h[3]))
# hortatory modals in closings
HORT=re.compile(r'\b(we|researchers|practitioners|the (?:field|community)|future work|one)\s+(should|must|ought)\b|\bshould be (?:reported|used|treated|adopted)\b',re.I)
print('\n hortatory modal in the closing sentence:')
for r in C:
    if HORT.search(r['closing']): print('  ',r['stratum'],r['key'],':',r['closing'][:180])
print(' count:',sum(1 for r in C if HORT.search(r['closing'])))
json.dump([{k:v for k,v in r.items()} for r in C],open(f'{S}/corpus_coded.json','w'),indent=1,ensure_ascii=False)
