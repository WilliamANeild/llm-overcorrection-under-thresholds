# -*- coding: utf-8 -*-
"""Draw and fetch a sample of artifact-free analysis abstracts, 2024-2026 ACL-family venues.

Stage 1 of the scenario-01 corpus. Writes intermediates to WORK; 06 consumes them.
Every filtering decision below is a regex applied to the whole volume, not a hand pick.
Retrieval date is recorded in the provenance block written by 06.
"""
import re, os, json, random, subprocess, time, sys, html as H

WORK = '/tmp/scen01'
VOLS = ['2024.acl-long','2024.acl-short','2024.findings-acl','2024.emnlp-main','2024.findings-emnlp',
        '2024.naacl-long','2024.eacl-long','2025.acl-long','2025.acl-short','2025.findings-acl',
        '2025.emnlp-main','2025.findings-emnlp','2025.naacl-long','2026.acl-long','2026.acl-short',
        '2026.findings-acl','2026.eacl-long']
SEED = 20260906
TARGET = 44          # over-draw: hand adjudication (06 + handcode file) removes method and resource papers

def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s); s = H.unescape(s); s = s.replace(' ', ' ')
    return re.sub(r'\s+', ' ', s).strip()

# ---- title signal: analysis / empirical-study shapes -------------------------------
TITLE_SIG = re.compile(
    r'^(?:Do|Does|Did|Can|Could|Are|Is|Was|Will|Should|When|Why|How|What|Which|Who)\b'
    r'|^(?:An?\s+)?(?:Empirical|Systematic|Comparative|Quantitative|Qualitative)\s+'
    r'(?:Analysis|Study|Investigation|Comparison|Evaluation|Examination)\b'
    r'|^(?:An?\s+)?Analysis\s+of\b|^(?:An?\s+)?Study\s+of\b|^(?:An?\s+)?Investigation\b'
    r'|^Understanding\b|^Rethinking\b|^Revisiting\b|^Examining\b|^Investigating\b'
    r'|^Exploring\b|^Measuring\b|^Quantifying\b|^Characterizing\b|^Characterising\b'
    r'|^Assessing\b|^Evaluating\b|^Comparing\b|^Probing\b|^Tracing\b|^Auditing\b'
    r'|^On\s+the\b|^On\s+(?:Measuring|Understanding|Evaluating)\b'
    r'|\bAn\s+Empirical\s+(?:Study|Analysis|Investigation)\b|\bA\s+Case\s+Study\b'
    r'|\bAn?\s+Analysis\b|\bA\s+Systematic\s+(?:Review|Study|Analysis)\b', re.I)

# ---- artifact signals: any hit disqualifies ----------------------------------------
RELEASE = re.compile(
    r'\b(?:we|authors?)\s+(?:\w+\s+){0,3}?(?:release|open[- ]sourc\w+|publish|distribute)\b'
    r'|\b(?:publicly|freely|openly)\s+(?:available|released|accessible)\b'
    r'|\bavailable\s+(?:at|via|online|upon|here|from)\b'
    r'|https?://'
    r'|\bmake\s+(?:\w+\s+){0,3}?(?:publicly\s+)?available\b'
    r'|\bwe\s+(?:will\s+)?(?:make|provide)\s+(?:our|the|all)\b.{0,40}\b(?:available|public)\b', re.I)
BUILD = re.compile(
    r'\b(?:we|this\s+(?:paper|work|study|article))\s+(?:\w+\s+){0,4}?'
    r'(?:introduce|propose|present|develop|construct|build|design|create|curate|devise|contribute|offer)[sd]?\b', re.I)

COMMON = set('LLM LLMS NLP AI ML LM LMS QA MT NER ASR TTS RAG SFT RLHF DPO PPO GRPO PEFT LORA MOE COT '
             'ICL OOD IID SOTA API GPU CPU HTML JSON XML PDF URL SVM CNN RNN LSTM MLP KL EM MLE MAP AUC '
             'ROC SD CI ANOVA IRB VLM VLMS MLLM MLLMS SLM SLMS AGI CLM MLM NLU NLG SAE SAES OCR NLI SRL '
             'POS IR RL SSL KG KGS USA US UK EU ID IDS OK MCQ MCQA QLORA FFN MHA KV FLOPS AND OR NOT THE '
             'ACL EMNLP NAACL EACL TACL ARR IQ EEG FMRI HCI UI UX CO2 GDPR DNA RNA'.split())
ACRO = re.compile(r"\b(?:[A-Z][a-z]*[A-Z][A-Za-z0-9\-]*|[A-Z]{3,}[A-Za-z0-9\-]*)\b")
def coined(s):
    return [a for a in ACRO.findall(s) if a.upper().split('-')[0] not in COMMON and len(a) > 2]

def main():
    os.makedirs(f'{WORK}/vols', exist_ok=True); os.makedirs(f'{WORK}/pages', exist_ok=True)
    for v in VOLS:
        fp = f'{WORK}/vols/{v}.html'
        if os.path.exists(fp) and os.path.getsize(fp) > 100000: continue
        subprocess.run(['curl','-s','--max-time','90','-o',fp,f'https://aclanthology.org/volumes/{v}/'])
        time.sleep(0.4)

    rows, absmap = [], {}
    for v in VOLS:
        h = open(f'{WORK}/vols/{v}.html', encoding='utf-8', errors='replace').read()
        for m in re.finditer(r'<strong><a class=align-middle href=/('+re.escape(v)+r'\.(\d+))/>(.*?)</a></strong>', h, re.S):
            if int(m.group(2)) == 0: continue          # front matter
            rows.append({'vol': v, 'anthology_id': m.group(1), 'num': int(m.group(2)),
                         'title': strip_tags(m.group(3))})
        # the volume page carries every abstract in a collapsed div; use it to screen without 1,500 fetches
        for m in re.finditer(r'id=abstract-(\d{4})--([a-z\-]+)--(\d+)><div class="card-body p-3 small">(.*?)</div></div>', h, re.S):
            absmap[f'{m.group(1)}.{m.group(2)}.{int(m.group(3))}'] = strip_tags(m.group(4))

    cand = [r for r in rows if TITLE_SIG.search(r['title'])]
    for r in cand:
        a = absmap.get(r['anthology_id'])
        if not a or len(a.split()) < 30: r['screen'] = 'no_abstract'; continue
        bn = [c for m in BUILD.finditer(a) for c in coined(a[m.end():m.end()+70])]
        r.update({'abstract': a, 'title_coined': coined(r['title']),
                  'release_lang': bool(RELEASE.search(a)), 'build_named': bn})
        r['screen'] = ('excl_release' if r['release_lang'] else
                       'excl_title_name' if r['title_coined'] else
                       'excl_build_named' if bn else 'PASS')
    from collections import Counter
    print('papers listed %d | title-signal candidates %d | %s' % (
        len(rows), len(cand), dict(Counter(r['screen'] for r in cand))), file=sys.stderr)

    byvol = {}
    for r in cand:
        if r['screen'] == 'PASS': byvol.setdefault(r['vol'], []).append(r)
    for v in byvol: byvol[v].sort(key=lambda r: r['num'])
    rng = random.Random(SEED); tot = sum(len(x) for x in byvol.values()); draw = []
    for v in sorted(byvol):                              # systematic: random start, constant stride
        k = max(1, round(TARGET*len(byvol[v])/tot))
        ids = byvol[v]; stride = len(ids)/k; start = rng.random()*stride
        draw += [ids[i] for i in sorted({min(int(start+j*stride), len(ids)-1) for j in range(k)})]
    print('drawn %d' % len(draw), file=sys.stderr)

    for d in draw:
        fp = f"{WORK}/pages/{d['anthology_id']}.html"
        if os.path.exists(fp) and os.path.getsize(fp) > 5000: continue
        subprocess.run(['curl','-s','--max-time','40','-o',fp,f"https://aclanthology.org/{d['anthology_id']}/"])
        time.sleep(0.4)

    json.dump({'pool_all_papers': len(rows), 'title_signal_candidates': len(cand),
               'screen_counts': dict(Counter(r['screen'] for r in cand)),
               'pass_pool_by_volume': {v: len(x) for v, x in sorted(byvol.items())},
               'seed': SEED, 'draw': draw},
              open(f'{WORK}/draw.json','w'), indent=1, ensure_ascii=False)

if __name__ == '__main__':
    main()
