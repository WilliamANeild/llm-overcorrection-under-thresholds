#!/usr/bin/env python3
"""
Census of figures and tables across the cached corpus: how many, of what kind, and where.

Counts only outermost <figure class="ltx_figure"> (subfigure panels carry
ltx_figure_panel and are not counted separately) and <figure class="ltx_table">.
Each float is located by the nearest preceding top-level section heading, and floats
after References/Appendix are counted separately from body floats.

    python3 scripts/introduction_corpus/05_figure_census.py
"""
import json, re, statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".workspace/reference/intro_corpus/html"
OUT = ROOT / ".workspace/reference/intro_corpus"

EMAMI = set("""2607.05113 2604.16845 2604.05074 2603.20620 2602.13110 2601.15550 2510.20543
2509.01035 2508.05525 2506.00748 2504.07385 2502.05331 2502.03418 2412.01690 2412.01621
2409.13935 2409.13843 2405.16282 2405.16277 2405.14555 2402.13372 2401.17703 2607.06845
2607.13162 2508.21628""".split())
ORIGINAL = set("""2201.06796 2206.05802 2212.09746 2303.11366 2303.17651 2306.05685 2308.03188
2308.03958 2310.01798 2310.12397 2310.13548 2311.07961 2311.08516 2401.16745 2402.14762
2402.14809 2403.04132 2404.12272 2404.13076 2406.01297 2410.16184 2501.17399 2505.06120""".split())
APPENDIXY = re.compile(r'\b(appendix|references|acknowledg|bibliograph|supplement)', re.I)


def census(html):
    heads = [(m.start(), re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip())
             for m in re.finditer(r'<h2[^>]*ltx_title_section[^>]*>(.*?)</h2>', html, re.S)]
    def where(pos):
        cur = "(front matter)"
        for p, t in heads:
            if p < pos:
                cur = t
            else:
                break
        return cur
    figs, tabs = [], []
    for m in re.finditer(r'<figure[^>]*class="([^"]+)"', html):
        c = m.group(1)
        if 'ltx_figure_panel' in c:
            continue
        (tabs if 'ltx_table' in c else figs).append(where(m.start()))
    body = lambda xs: [x for x in xs if not APPENDIXY.search(x)]
    return {"figures": len(figs), "tables": len(tabs),
            "figures_body": len(body(figs)), "tables_body": len(body(tabs)),
            "fig_sections": figs, "tab_sections": tabs}


def q(v, p):
    v = sorted(v)
    return v[int(p * (len(v) - 1))]


def describe(name, rows):
    if not rows:
        return
    print(f"\n{'='*76}\n{name}   n = {len(rows)}\n{'='*76}")
    for k, lab in [("figures_body", "Figures in the body"), ("tables_body", "Tables in the body"),
                   ("figures", "Figures incl. appendix"), ("tables", "Tables incl. appendix")]:
        v = [r[k] for r in rows]
        print(f"  {lab:<26} min {min(v):>3}  p25 {q(v,.25):>3}  median {st.median(v):>5.1f}"
              f"  p75 {q(v,.75):>3}  max {max(v):>3}")
    tot = [r["figures_body"] + r["tables_body"] for r in rows]
    print(f"  {'Body floats, combined':<26} min {min(tot):>3}  p25 {q(tot,.25):>3}"
          f"  median {st.median(tot):>5.1f}  p75 {q(tot,.75):>3}  max {max(tot):>3}")
    ratio = [r["figures_body"] / max(1, r["tables_body"]) for r in rows]
    print(f"  figures per table (body), median {st.median(ratio):.2f}")
    nofig = sum(1 for r in rows if r["figures_body"] == 0)
    print(f"  papers with no body figure at all: {nofig} of {len(rows)}")


def main():
    rows = {}
    for f in sorted(CACHE.glob("*.html")):
        rows[f.stem] = census(f.read_text(errors="replace"))
    describe("WHOLE CACHED CORPUS", list(rows.values()))
    describe("ALI EMAMI", [v for k, v in rows.items() if k in EMAMI])
    describe("THE 23-PAPER TOPICAL SET", [v for k, v in rows.items() if k in ORIGINAL])

    from collections import Counter
    c = Counter()
    for v in rows.values():
        for s in v["fig_sections"]:
            if APPENDIXY.search(s):
                c["(appendix / back matter)"] += 1
            else:
                c[re.sub(r'^\d+\.?\s*', '', s).lower()[:34] or "(front matter)"] += 1
    print(f"\n{'='*76}\nWHERE FIGURES SIT, every figure in every cached paper\n{'='*76}")
    tot = sum(c.values())
    for s, n in c.most_common(14):
        print(f"  {n:>4}  {n/tot*100:>5.1f}%  {s}")
    json.dump(rows, open(OUT / "figure_census.json", "w"), indent=1)
    print(f"\nwrote {OUT/'figure_census.json'}")


if __name__ == "__main__":
    main()
