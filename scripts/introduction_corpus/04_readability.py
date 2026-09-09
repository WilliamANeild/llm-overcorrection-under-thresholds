#!/usr/bin/env python3
"""
Readability of introductions: this paper's against the ACL-family corpus and against
Ali Emami's own. Same Flesch implementation used for the abstract work, so the numbers
are comparable across sections.

    python3 scripts/introduction_corpus/04_readability.py
"""
import importlib.util, json, re, statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".workspace/reference/intro_corpus"
spec = importlib.util.spec_from_file_location("fetch", Path(__file__).parent / "02_fetch_intros.py")
fetch = importlib.util.module_from_spec(spec); spec.loader.exec_module(fetch)

EMAMI = set("""2607.05113 2604.16845 2604.05074 2603.20620 2602.13110 2601.15550 2510.20543
2509.01035 2508.05525 2506.00748 2504.07385 2502.05331 2502.03418 2412.01690 2412.01621
2409.13935 2409.13843 2405.16282 2405.16277 2405.14555 2402.13372 2401.17703 2607.06845
2607.13162 2508.21628""".split())


def syll(w):
    w = re.sub(r'[^a-z]', '', w.lower())
    if not w:
        return 1
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1:
        n -= 1
    return max(1, n)


def readability(text):
    sents = [s for s in re.split(r'(?<=[.!?])\s+', text) if len(s.split()) > 3]
    w = text.split()
    if not sents or not w:
        return None
    wps = len(w) / len(sents)
    spw = sum(syll(x) for x in w) / len(w)
    return {"words": len(w), "sents": len(sents), "wps": round(wps, 1),
            "syll_per_word": round(spw, 3),
            "flesch": round(206.835 - 1.015 * wps - 84.6 * spw, 1)}


def intro_text(aid):
    f = OUT / "html" / f"{aid}.html"
    if not f.exists():
        return None
    sec = fetch.intro_section(f.read_text(errors="replace"))
    if not sec:
        return None
    body = re.sub(r'<h[1-6][^>]*ltx_title_section[^>]*>.*?</h[1-6]>', ' ', sec, flags=re.S)
    parts = [fetch.strip(h) for _, h in fetch.blocks(body)]
    return " ".join(p for p in parts if len(p.split()) >= 4)


def ours():
    t = re.sub(r'(?<!\\)%.*', '', (ROOT / "paper/sections/introduction_v2.tex").read_text())
    t = re.sub(r'\\begin\{figure\*?\}.*?\\end\{figure\*?\}', ' ', t, flags=re.S)
    t = t.replace('\\section{Introduction}', '')
    t = re.sub(r'\\(cite[tp]?|ref)\{[^}]*\}', ' ', t)
    t = re.sub(r'\\emph\{([^}]*)\}', r'\1', t)
    t = re.sub(r'\\[a-zA-Z]+', ' ', t).replace('\\%', '%')
    return re.sub(r'\s+', ' ', t).strip()


def q(v, p):
    v = sorted(v); return v[int(p * (len(v) - 1))]


def main():
    rows = json.loads((OUT / "rows.json").read_text())
    acl, em = [], []
    for r in rows:
        if r["aid"] in EMAMI:
            continue
        t = intro_text(r["aid"])
        m = readability(t) if t else None
        if m and r["acl"]:
            acl.append(m)
    for aid in EMAMI:
        t = intro_text(aid)
        m = readability(t) if t else None
        if m:
            em.append(m)
    o = readability(ours())

    print(f"{'group':<26}{'n':>4}{'Flesch p25':>12}{'median':>9}{'p75':>7}{'  words/sent':>13}{'syll/word':>11}")
    for name, g in [("ACL-family corpus", acl), ("Ali Emami", em)]:
        fl = [x["flesch"] for x in g]
        print(f"{name:<26}{len(g):>4}{q(fl,.25):>12}{st.median(fl):>9.1f}{q(fl,.75):>7}"
              f"{st.median([x['wps'] for x in g]):>13.1f}{st.median([x['syll_per_word'] for x in g]):>11.3f}")
    print(f"\n{'THIS PAPER':<26}{1:>4}{'':>12}{o['flesch']:>9}{'':>7}{o['wps']:>13.1f}{o['syll_per_word']:>11.3f}")
    print(f"   {o['words']} words, {o['sents']} sentences")
    fl_acl = sorted(x["flesch"] for x in acl); fl_em = sorted(x["flesch"] for x in em)
    print(f"\n   percentile vs ACL-family: {sum(1 for x in fl_acl if x <= o['flesch'])/len(fl_acl)*100:.0f}")
    print(f"   percentile vs Emami:      {sum(1 for x in fl_em if x <= o['flesch'])/len(fl_em)*100:.0f}")


if __name__ == "__main__":
    main()
