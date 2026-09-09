import re, os, json, html as H

def strip_tags(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = H.unescape(s)
    s = s.replace(' ',' ')
    return re.sub(r'\s+',' ',s).strip()

def get_abstract(h):
    # loose parse: locate the acl-abstract div, walk div nesting to its close
    m = re.search(r'<div[^>]*class="[^"]*acl-abstract[^"]*"[^>]*>', h)
    if not m:
        m = re.search(r'<div[^>]*class=[^ >]*acl-abstract[^ >]*[^>]*>', h)
    if not m: return None
    i = m.end(); depth = 1; j = i
    for t in re.finditer(r'<(/?)div\b', h[i:]):
        depth += 1 if t.group(1)=='' else -1
        if depth == 0:
            j = i + t.start(); break
    inner = h[i:j]
    inner = re.sub(r'<h5[^>]*>.*?</h5>', '', inner, flags=re.S)  # drop the "Abstract" heading
    return strip_tags(inner)

def get_title(h):
    m = re.search(r'<h2[^>]*id=title[^>]*>(.*?)</h2>', h, re.S)
    if m: return strip_tags(m.group(1))
    m = re.search(r'<title>(.*?)</title>', h, re.S)
    return strip_tags(m.group(1)).replace(' - ACL Anthology','')

out = {}
fails = []
for aid in json.load(open('/tmp/aclfetch/sample_ids.json')):
    fp = f'/tmp/aclfetch/pages/{aid}.html'
    if not os.path.exists(fp): fails.append((aid,'nofile')); continue
    h = open(fp, encoding='utf-8', errors='replace').read()
    a = get_abstract(h)
    if not a or len(a.split()) < 30:
        fails.append((aid, 'noabs' if not a else 'short:%d'%len(a.split()))); continue
    out[aid] = {'anthology_id': aid, 'title': get_title(h), 'abstract': a,
                'url': f'https://aclanthology.org/{aid}/'}
json.dump(out, open('/tmp/aclfetch/extracted.json','w'), indent=1, ensure_ascii=False)
print('extracted', len(out), 'failed', fails)
