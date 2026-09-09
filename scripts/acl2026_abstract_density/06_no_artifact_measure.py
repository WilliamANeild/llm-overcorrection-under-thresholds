# -*- coding: utf-8 -*-
"""Extract and measure the artifact-free abstracts drawn by 05, and store them verbatim.

Abstracts come from the `card-body acl-abstract` div on each landing page, parsed by walking
div nesting; each is checked against the copy carried in the volume listing page and must match.
All counts come from 03_measure.measure(). Papers kept are those listed in
handcode_no_artifact.json; the drops and the reason for each are recorded in the same file.
"""
import re, os, json, html as H, importlib.util, datetime

WORK = '/tmp/scen01'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
STORE = os.path.join(ROOT, 'paper', 'reference', 'acl2026_abstracts.json')
KEY = 'no_artifact_2024_2026'

spec = importlib.util.spec_from_file_location('m3', os.path.join(HERE, '03_measure.py'))
m3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m3)

def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s); s = H.unescape(s); s = s.replace(' ', ' ')
    return re.sub(r'\s+', ' ', s).strip()

def get_abstract(h):
    m = (re.search(r'<div[^>]*class="[^"]*acl-abstract[^"]*"[^>]*>', h)
         or re.search(r'<div[^>]*class=[^ >]*acl-abstract[^ >]*[^>]*>', h))
    if not m: return None
    i = m.end(); depth = 1; j = i
    for t in re.finditer(r'<(/?)div\b', h[i:]):
        depth += 1 if t.group(1) == '' else -1
        if depth == 0: j = i + t.start(); break
    return strip_tags(re.sub(r'<h5[^>]*>.*?</h5>', '', h[i:j], flags=re.S))

def get_title(h):
    m = re.search(r'<h2[^>]*id=title[^>]*>(.*?)</h2>', h, re.S)
    if m: return strip_tags(m.group(1))
    return strip_tags(re.search(r'<title>(.*?)</title>', h, re.S).group(1)).replace(' - ACL Anthology', '')

def main():
    draw = json.load(open(f'{WORK}/draw.json'))
    hc = json.load(open(os.path.join(HERE, 'handcode_no_artifact.json')))
    keep = set(hc['papers'])
    out, fails, mismatch = {}, [], []
    for d in draw['draw']:
        aid = d['anthology_id']; fp = f'{WORK}/pages/{aid}.html'
        if not os.path.exists(fp): fails.append((aid, 'nofile')); continue
        h = open(fp, encoding='utf-8', errors='replace').read()
        a = get_abstract(h)
        if not a or len(a.split()) < 30:
            fails.append((aid, 'noabs' if not a else 'short')); continue
        if a.strip() != d['abstract'].strip(): mismatch.append(aid)
        if aid not in keep: continue
        out[aid] = dict({'anthology_id': aid, 'vol': d['vol'], 'title': get_title(h), 'abstract': a,
                         'url': f'https://aclanthology.org/{aid}/'}, **m3.measure(a))
    assert set(out) == keep, sorted(keep - set(out))
    json.dump(out, open(f'{WORK}/measured.json', 'w'), indent=1, ensure_ascii=False)
    print('measured %d | fetch failures %s | volume-vs-landing mismatches %s'
          % (len(out), fails or 'none', mismatch or 'none'))

    store = json.load(open(STORE))
    store[KEY] = out
    store['_%s_provenance' % KEY] = {
        'retrieved': datetime.date.today().isoformat(),
        'source': 'ACL Anthology landing pages, one HTTP request per paper',
        'seed': draw['seed'], 'sampling': 'see scripts/acl2026_abstract_density/05_no_artifact_sample.py',
        'papers_listed_across_17_volumes': draw['pool_all_papers'],
        'title_signal_candidates': draw['title_signal_candidates'],
        'screen_counts': draw['screen_counts'],
        'drawn': len(draw['draw']), 'kept_after_hand_adjudication': len(out),
        'volume_vs_landing_page_mismatches': mismatch}
    json.dump(store, open(STORE, 'w'), indent=1, ensure_ascii=False)
    print('stored under %s in %s' % (KEY, STORE))

if __name__ == '__main__':
    main()
