#!/usr/bin/env python3
"""
Words and citations per top-level section across the cached corpus, so each section of
our paper can be checked against what comparable papers actually do.

Sections are matched by heading keyword, body only (bibliography onward excluded).
Citation counts are individual bibliography references (href="#bib.bib"), the same
convention used throughout paper/rules/.

    python3 scripts/introduction_corpus/06_section_census.py
"""
import json, re, statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".workspace/reference/intro_corpus/html"
EMAMI = set("""2607.05113 2604.16845 2604.05074 2603.20620 2602.13110 2601.15550 2510.20543
2509.01035 2508.05525 2506.00748 2504.07385 2502.05331 2502.03418 2412.01690 2412.01621
2409.13935 2409.13843 2405.16282 2405.16277 2405.14555 2402.13372 2401.17703 2607.06845
2607.13162 2508.21628""".split())

KINDS = {
    "related work": r"related work|background|prior work",
    "method":       r"method|approach|experimental setup|our approach|\bdesign\b",
    "results":      r"^results|results and|findings|experiments and results|\bexperiments\b",
    "discussion":   r"discussion|analysis and discussion",
    "conclusion":   r"conclusion",
}


def strip(s):
    s = re.sub(r'<(figure|figcaption|table)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def sections(html):
    cut = re.search(r'ltx_bibliography|<h2[^>]*>\s*References', html, re.I)
    body = html[:cut.start()] if cut else html
    heads = [(m.start(), m.end(),
              re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip())
             for m in re.finditer(r'<h2[^>]*ltx_title_section[^>]*>(.*?)</h2>', body, re.S)]
    out = []
    for i, (s, e, title) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(body)
        chunk = body[e:end]
        out.append((re.sub(r'^\d+\.?\s*', '', title).lower(),
                    len(strip(chunk).split()),
                    len(re.findall(r'href="#bib\.bib', chunk))))
    return out


def q(v, p):
    v = sorted(v); return v[int(p * (len(v) - 1))]


def main():
    rows = {}
    for f in sorted(CACHE.glob("*.html")):
        rows[f.stem] = sections(f.read_text(errors="replace"))

    for group, keep in [("WHOLE CORPUS", lambda k: True),
                        ("ALI EMAMI", lambda k: k in EMAMI)]:
        print(f"\n{'='*78}\n{group}\n{'='*78}")
        print(f"  {'section':<16}{'n':>4}{'words p25':>11}{'median':>9}{'p75':>7}"
              f"{'  cites med':>12}{'per 100w':>10}")
        for kind, pat in KINDS.items():
            ws, cs, ds = [], [], []
            for aid, secs in rows.items():
                if not keep(aid):
                    continue
                hit = [(w, c) for t, w, c in secs if re.search(pat, t) and w > 40]
                if not hit:
                    continue
                w, c = max(hit, key=lambda x: x[0])
                ws.append(w); cs.append(c); ds.append(c / w * 100)
            if len(ws) < 5:
                print(f"  {kind:<16}{len(ws):>4}   too few to report"); continue
            print(f"  {kind:<16}{len(ws):>4}{q(ws,.25):>11}{st.median(ws):>9.0f}{q(ws,.75):>7}"
                  f"{st.median(cs):>12.0f}{st.median(ds):>10.1f}")


if __name__ == "__main__":
    main()
