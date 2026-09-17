#!/usr/bin/env python3
"""
Diagnostic metrics beyond length: the measures a referee reacts to rather than the ones
that describe a manuscript. Each is computed for this paper and, where the corpus supports
it, for the 69 cached papers and Ali's 24 separately.

    python3 scripts/introduction_corpus/08_advanced_metrics.py
"""
import re, statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".workspace/reference/intro_corpus/html"
SEC = ROOT / "paper/sections"
EMAMI = set("""2607.05113 2604.16845 2604.05074 2603.20620 2602.13110 2601.15550 2510.20543
2509.01035 2508.05525 2506.00748 2504.07385 2502.05331 2502.03418 2412.01690 2412.01621
2409.13935 2409.13843 2405.16282 2405.16277 2405.14555 2402.13372 2401.17703 2607.06845
2607.13162 2508.21628""".split())

LIVE = ["abstract_v2", "introduction_v2", "related_work_v2", "methods", "results_v2",
        "discussion", "conclusion", "limitations"]

HEDGE = r'\b(may|might|could|appears?|seems?|suggests?|indicates?|likely|possibly|potentially|arguably|tends? to|somewhat|relatively|generally|typically|often|usually)\b'
FIRST = r'\b(we|our|us)\b'
STAT = {
    "p-values":     r'p\s*(=|<|>|\\[a-z]+)\s*\\?\$?\s*\d|\$p',
    "conf. ints":   r'\bCI\b|confidence interval',
    "sample sizes": r'\bn\s*=|\$n\s*=|\bN\s*=',
    "effect sizes": r'\bkappa|\\kappa|Spearman|Wilcoxon|binomial|\blevels?\b.*\bp\s*=|\br\s*=',
}
REPRO = {
    "model versions named":  r'Sonnet|GPT-4o|Gemini|Llama|Qwen|DeepSeek',
    "temperature stated":    r'temperature',
    "prompt text given":     r'``[^\']{20,}|\\texttt\{',
    "sample/filter stated":  r'filter|restricted to|excluding|after filtering',
    "human validation":      r'human rater|annotator|inter-rater|Krippendorff',
    "code or data release":  r'available at|we release|github|anonymous\.4open|supplementary',
    "compute stated":        r'GPU|compute budget|API cost|wall-clock',
}
# concepts that must each have ONE name in the paper
TERMS = {
    "the non-revision reply": ["meta-response", "meta-commentary", "meta-wrapping", "meta-wrapper", "meta-reply"],
    "the quality threshold":  ["sufficiency threshold", "sufficient threshold", "task completion threshold", "level 4"],
    "the stop point":         ["quality-optimal stopping point", "quality-maximizing stopping point", "quality-optimal turn", "optimal turn"],
    "the undirected ask":     ["undirected request", "undirected revision", "generic revision", "generic probe", "generic next-turn"],
}


def strip_html(s):
    s = re.sub(r'<(script|style|figure|figcaption|table)\b.*?</\1>', ' ', s, flags=re.S | re.I)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s)).strip()


def body_and_bib(html):
    cut = re.search(r'ltx_bibliography|<h2[^>]*>\s*References', html, re.I)
    body = strip_html(html[:cut.start()] if cut else html)
    years = []
    for item in re.findall(r'<li[^>]*ltx_bibitem[^>]*>(.*?)</li>', html, re.S):
        y = re.findall(r'\b(?:19|20)\d{2}\b', re.sub(r'<[^>]+>', ' ', item))
        if y:
            years.append(max(int(x) for x in y))
    return body, years


def our_text(files=LIVE):
    out = {}
    for f in files:
        t = re.sub(r'(?<!\\)%.*', '', (SEC / f"{f}.tex").read_text())
        t = re.sub(r'\\begin\{(figure|table)\*?\}.*?\\end\{\1\*?\}', ' ', t, flags=re.S)
        t = re.sub(r'\\(cite[tp]?|ref|label)\{[^}]*\}', ' ', t)
        t = re.sub(r'\\(section|subsection|paragraph)\*?\{([^}]*)\}', r' \2 ', t)
        out[f] = re.sub(r'\s+', ' ', re.sub(r'\\[a-zA-Z]+\*?', ' ', t)).strip()
    return out


def per1k(text, pat):
    n = len(re.findall(pat, text, re.I))
    w = len(text.split())
    return 1000 * n / w if w else 0


def q(v, p):
    v = sorted(v)
    return v[int(p * (len(v) - 1))]


def main():
    ours = our_text()
    whole = " ".join(ours.values())

    acl, em = [], []
    for f in sorted(CACHE.glob("*.html")):
        body, years = body_and_bib(f.read_text(errors="replace"))
        if len(body.split()) < 1500:
            continue
        pub = 2000 + int(f.stem[:2])
        rec = {"hedge": per1k(body, HEDGE), "first": per1k(body, FIRST),
               "num": per1k(body, r'\b\d'), "pub": pub, "years": years,
               **{k: per1k(body, p) for k, p in STAT.items()}}
        (em if f.stem in EMAMI else acl).append(rec)

    def row(label, ourv, key, fmt="{:.1f}"):
        a = [x[key] for x in acl]; e = [x[key] for x in em]
        lo, hi = q(a, .25), q(a, .75)
        flag = "ok" if lo <= ourv <= hi else ("LOW" if ourv < lo else "HIGH")
        print(f"  {label:<24}{fmt.format(ourv):>8}{fmt.format(lo):>8}{fmt.format(st.median(a)):>8}"
              f"{fmt.format(hi):>8}{fmt.format(st.median(e)):>9}   {flag}")

    print(f"{'ACL corpus n=':<24}{len(acl)}   Emami n={len(em)}\n")
    print(f"  {'per 1000 words':<24}{'ours':>8}{'p25':>8}{'med':>8}{'p75':>8}{'   Emami':>9}")
    for lab, key in [("hedge words", "hedge"), ("first person (we/our)", "first"), ("numerals", "num")]:
        row(lab, per1k(whole, {"hedge": HEDGE, "first": FIRST, "num": r'\b\d'}[key]), key)
    for lab in STAT:
        row(lab, per1k(whole, STAT[lab]), lab)

    print("\nCITATION RECENCY")
    bib = (ROOT / "paper/references.bib").read_text()
    cited = {k.strip() for c in re.findall(r'\\cite[tp]?\{([^}]*)\}',
             " ".join((SEC / f"{f}.tex").read_text() for f in LIVE)) for k in c.split(',')}
    oy = []
    for k in cited:
        m = re.search(r'@\w+\{' + re.escape(k) + r',(.*?)\n\}', bib, re.S)
        if m:
            y = re.search(r'year\s*=\s*\{?(\d{4})', m.group(1))
            if y:
                oy.append(int(y.group(1)))
    ca = [(2026 - y) for x in acl for y in x["years"] if 1990 <= y <= 2026]
    print(f"  {'':<24}{'ours':>8}{'corpus':>10}")
    print(f"  {'cited works':<24}{len(oy):>8}{'':>10}")
    print(f"  {'median age (years)':<24}{st.median([2026 - y for y in oy]):>8.1f}{st.median(ca):>10.1f}")
    print(f"  {'share <= 2 years old':<24}{sum(1 for y in oy if 2026-y<=2)/len(oy)*100:>7.0f}%"
          f"{sum(1 for a in ca if a<=2)/len(ca)*100:>9.0f}%")
    print(f"  {'share >= 7 years old':<24}{sum(1 for y in oy if 2026-y>=7)/len(oy)*100:>7.0f}%"
          f"{sum(1 for a in ca if a>=7)/len(ca)*100:>9.0f}%")

    print("\nREPRODUCIBILITY DISCLOSURE (presence in our live build)")
    for lab, pat in REPRO.items():
        hits = len(re.findall(pat, whole, re.I))
        print(f"  {'yes' if hits else 'NO ':<4} {lab:<24}{hits:>4} mention(s)")

    print("\nTERMINOLOGY CONSISTENCY (one name per concept)")
    for concept, variants in TERMS.items():
        found = {v: len(re.findall(re.escape(v), whole, re.I)) for v in variants}
        used = {v: n for v, n in found.items() if n}
        tag = "ok" if len(used) <= 1 else f"{len(used)} VARIANTS"
        print(f"  {tag:<12}{concept:<26}{used}")


if __name__ == "__main__":
    main()
