#!/usr/bin/env python3
"""
Fetch arXiv LaTeXML HTML and extract the Introduction section, then count it
mechanically. Same method as the original 23-paper pass recorded in
paper/rules/03_introduction.md: isolate the <section> whose heading matches
"Introduction", count paragraphs, words and citation anchors by script.

Citation counting follows the established convention: individual bibliography
references, so href="#bib.bib12" is one whether or not it shares a bracket with
another. Figure captions are excluded from the word count.

    python3 scripts/introduction_corpus/02_fetch_intros.py <arxiv_id> [<arxiv_id> ...]

Caches raw HTML under .workspace/reference/intro_corpus/html/ so counts are
reproducible without refetching, and writes intros.json alongside.
"""
import json, re, sys, time, urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".workspace/reference/intro_corpus"
CACHE = OUT / "html"

UA = {"User-Agent": "Mozilla/5.0 (research; introduction-structure survey)"}


def fetch(aid):
    f = CACHE / f"{aid}.html"
    if f.exists():
        return f.read_text(errors="replace"), True
    req = urllib.request.Request(f"https://arxiv.org/html/{aid}", headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        html = r.read().decode("utf-8", errors="replace")
    CACHE.mkdir(parents=True, exist_ok=True)
    f.write_text(html)
    return html, False


def intro_section(html):
    """Return the HTML of the section whose title is the Introduction."""
    parts = re.split(r'(?=<section\b)', html)
    for p in parts:
        m = re.search(r'<h[1-6][^>]*ltx_title_section[^>]*>(.*?)</h[1-6]>', p, re.S)
        if m and re.search(r'\bintroduction\b', re.sub(r'<[^>]+>', ' ', m.group(1)), re.I):
            return p
    return None


def strip(s):
    s = re.sub(r'<(figure|figcaption|table)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<math\b.*?</math>', ' M ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', unescape(s)).strip()


def spans(sec):
    """(kind, start, end) for every ltx_para and ltx_item div, nesting-aware."""
    out = []
    for m in re.finditer(r'<div[^>]*class="[^"]*\bltx_(para|item)\b[^"]*"[^>]*>', sec):
        depth, end = 1, len(sec)
        for t in re.finditer(r'<(/?)div\b', sec[m.end():]):
            depth += -1 if t.group(1) else 1
            if depth == 0:
                end = m.end() + t.start()
                break
        out.append([m.group(1), m.end(), end])
    return out


def blocks(sec):
    """Outermost ltx_para blocks, with any nested ltx_item removed from the parent
    text and returned as its own block. LaTeXML nests ltx_para inside ltx_para for
    some structures, so inner paragraphs are dropped to avoid double counting.
    Words and list items are reported separately, matching the original pass
    recorded in paper/rules/03_introduction.md."""
    sp = spans(sec)
    def outermost(kind):
        s = [x for x in sp if x[0] == kind]
        return [x for x in s if not any(o is not x and o[1] <= x[1] and x[2] <= o[2] for o in s)]
    paras, items = outermost('para'), outermost('item')
    items = [i for i in items if not any(p[1] <= i[1] and i[2] <= p[2] for p in paras)] + \
            [i for i in items if any(p[1] <= i[1] and i[2] <= p[2] for p in paras)]
    out = []
    for kind, a, b in paras:
        h = sec[a:b]
        for _, ia, ib in sorted([i for i in items if i[1] > a and i[2] <= b], key=lambda x: -x[1]):
            h = h[:ia - a] + ' ' + h[ib - a:]
        out.append(('para', h))
    out += [('item', sec[a:b]) for _, a, b in items]
    return out


def measure(sec):
    body = re.sub(r'<h[1-6][^>]*ltx_title_section[^>]*>.*?</h[1-6]>', ' ', sec, flags=re.S)
    kept = [(k, h, strip(h)) for k, h in blocks(body)]
    kept = [b for b in kept if len(b[2].split()) >= 4]
    paras = [b for b in kept if b[0] == 'para']
    items = [b for b in kept if b[0] == 'item']
    words = sum(len(b[2].split()) for b in paras)      # body paragraphs only
    cites = len(re.findall(r'href="#bib\.bib', body))
    first = paras[0][1] if paras else ''
    last2 = ''.join(b[1] for b in kept[-2:])
    return {
        "paragraphs": len(paras),
        "list_items": len(items),
        "blocks": len(kept),
        "words": words,
        "words_incl_items": words + sum(len(b[2].split()) for b in items),
        "citations": cites,
        "cites_per_100w": round(cites / words * 100, 2) if words else 0,
        "cites_p1": len(re.findall(r'href="#bib\.bib', first)),
        "cites_last2": len(re.findall(r'href="#bib\.bib', last2)),
        "figure_referenced": bool(re.search(r'href="#S\d+\.F\d+', body)),
        "opening_sentence": (re.split(r'(?<=[.!?])\s', paras[0][2])[0] if paras else ""),
        "para_words": [len(b[2].split()) for b in paras],
    }


def main():
    ids = sys.argv[1:]
    results = {}
    f = OUT / "intros.json"
    if f.exists():
        results = json.loads(f.read_text())
    for aid in ids:
        try:
            html, cached = fetch(aid)
        except Exception as exc:
            print(f"{aid:<12} FETCH FAILED: {exc}")
            results[aid] = {"error": f"fetch failed: {exc}"}
            continue
        sec = intro_section(html)
        if sec is None:
            print(f"{aid:<12} no Introduction section found (likely no LaTeXML HTML)")
            results[aid] = {"error": "no introduction section in HTML"}
            if not cached:
                time.sleep(3)
            continue
        m = measure(sec)
        results[aid] = m
        print(f"{aid:<12} {m['words']:>4}w  {m['paragraphs']}p  {m['citations']:>2}c  "
              f"{m['cites_per_100w']:>4}/100w  p1={m['cites_p1']:>2}  last2={m['cites_last2']}"
              f"  {'(cached)' if cached else ''}")
        if not cached:
            time.sleep(3)
    OUT.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()
