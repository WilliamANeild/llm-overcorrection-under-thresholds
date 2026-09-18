#!/usr/bin/env python3
"""
Prose metrics per section across the cached corpus: readability, sentence length,
paragraph length. The length census (06) says how long a section should be; this says
how it should read. Same Flesch implementation as the abstract and introduction work,
so the numbers are comparable across every section of the paper.

    python3 scripts/introduction_corpus/07_prose_census.py
"""
import importlib.util, re, statistics as st, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / ".workspace/reference/intro_corpus/html"

spec = importlib.util.spec_from_file_location("census", Path(__file__).parent / "06_section_census.py")
census = importlib.util.module_from_spec(spec); spec.loader.exec_module(census)
EMAMI, KINDS, strip = census.EMAMI, census.KINDS, census.strip

OURS = {"related work": "related_work_v2", "method": "methods", "results": "results_v2",
        "discussion": "discussion", "conclusion": "conclusion", "introduction": "introduction_v2"}


def live_sections():
    """Sections main.tex actually inputs. A hardcoded list reports sections that have been
    cut: the Discussion was dropped on 2026-09-18 and kept being measured for a day."""
    main = (ROOT / "paper/main.tex").read_text()
    body = re.sub(r'(?<!\\)%.*', '', main)
    return {m.group(1).split("/")[-1]
            for m in re.finditer(r'\\input\{([^}]+)\}', body)}


def syll(w):
    w = re.sub(r'[^a-z]', '', w.lower())
    if not w:
        return 1
    n = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and n > 1:
        n -= 1
    return max(1, n)


def prose(text, paras=None):
    """Flesch, words per sentence, syllables per word, words per paragraph."""
    sents = [s for s in re.split(r'(?<=[.!?])\s+', text) if len(s.split()) > 3]
    w = text.split()
    if len(sents) < 3 or len(w) < 80:
        return None
    wps = len(w) / len(sents)
    spw = sum(syll(x) for x in w) / len(w)
    m = {"words": len(w), "sents": len(sents), "wps": round(wps, 1),
         "spw": round(spw, 3), "flesch": round(206.835 - 1.015 * wps - 84.6 * spw, 1)}
    if paras:
        good = [p for p in paras if len(p.split()) >= 25]
        m["wpp"] = round(st.mean(len(p.split()) for p in good), 1) if good else None
    return m


def corpus_sections(html):
    """(kind, text, paragraphs) for each body section matching a known kind."""
    cut = re.search(r'ltx_bibliography|<h2[^>]*>\s*References', html, re.I)
    body = html[:cut.start()] if cut else html
    heads = [(m.start(), m.end(), re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip())
             for m in re.finditer(r'<h2[^>]*ltx_title_section[^>]*>(.*?)</h2>', body, re.S)]
    out = []
    for i, (s, e, title) in enumerate(heads):
        t = re.sub(r'^\d+\.?\s*', '', title).lower()
        chunk = body[e:(heads[i + 1][0] if i + 1 < len(heads) else len(body))]
        kind = next((k for k, pat in KINDS.items() if re.search(pat, t)), None)
        if kind is None and re.match(r'introduction', t):
            kind = "introduction"
        if kind:
            ps = [strip(p) for p in re.findall(r'<p[^>]*ltx_p[^>]*>(.*?)</p>', chunk, re.S)]
            out.append((kind, strip(chunk), [p for p in ps if p]))
    return out


def our_text(stem):
    t = re.sub(r'(?<!\\)%.*', '', (ROOT / f"paper/sections/{stem}.tex").read_text())
    t = re.sub(r'\\begin\{(figure|table)\*?\}.*?\\end\{\1\*?\}', ' ', t, flags=re.S)
    t = re.sub(r'\\(section|subsection|paragraph)\*?\{[^}]*\}', ' ', t)
    t = re.sub(r'\\(cite[tp]?|ref|label)\{[^}]*\}', ' ', t)
    t = re.sub(r'\\(emph|textbf|textit)\{([^}]*)\}', r'\2', t)
    t = re.sub(r'\$[^$]*\$', ' x ', t)
    t = re.sub(r'\\[a-zA-Z]+\*?', ' ', t).replace('\\%', '%')
    paras = [re.sub(r'\s+', ' ', p).strip() for p in re.split(r'\n\s*\n', t)]
    return re.sub(r'\s+', ' ', t).strip(), [p for p in paras if p]


def q(v, p):
    v = sorted(v); return v[int(p * (len(v) - 1))]


def main():
    acl, em = {}, {}
    for f in sorted(CACHE.glob("*.html")):
        tgt = em if f.stem in EMAMI else acl
        for kind, text, ps in corpus_sections(f.read_text(errors="replace")):
            m = prose(text, ps)
            if m:
                tgt.setdefault(kind, []).append(m)

    order = ["introduction", "related work", "method", "results", "discussion", "conclusion"]
    live = live_sections()
    order = [k for k in order if OURS[k] in live]
    print("FLESCH READING EASE, by section\n")
    print(f"{'section':<15}{'ours':>7}{'n':>5}{'p25':>7}{'med':>7}{'p75':>7}{'   Emami med':>13}{'  n':>4}   band?")
    flags = []
    for k in order:
        if k not in acl:
            continue
        g = [x["flesch"] for x in acl[k]]
        e = [x["flesch"] for x in em.get(k, [])]
        text, ps = our_text(OURS[k])
        o = prose(text, ps)
        if not o:
            continue
        lo, hi = q(g, .25), q(g, .75)
        ok = lo <= o["flesch"] <= hi
        if not ok:
            flags.append((k, "flesch", o["flesch"], lo, hi))
        print(f"{k:<15}{o['flesch']:>7}{len(g):>5}{lo:>7}{st.median(g):>7.1f}{hi:>7}"
              f"{(f'{st.median(e):.1f}' if len(e) >= 5 else '-'):>13}{len(e):>4}   {'ok' if ok else 'OUT'}")

    for lab, key, fmt in [("WORDS PER SENTENCE", "wps", "{:.1f}"),
                          ("WORDS PER PARAGRAPH", "wpp", "{:.0f}")]:
        print(f"\n{lab}, by section\n")
        print(f"{'section':<15}{'ours':>7}{'n':>5}{'p25':>7}{'med':>7}{'p75':>7}{'   Emami med':>13}   band?")
        for k in order:
            if k not in acl:
                continue
            g = [x[key] for x in acl[k] if x.get(key) is not None]
            e = [x[key] for x in em.get(k, []) if x.get(key) is not None]
            text, ps = our_text(OURS[k])
            o = prose(text, ps)
            if not o or o.get(key) is None or len(g) < 5:
                continue
            lo, hi = q(g, .25), q(g, .75)
            ok = lo <= o[key] <= hi
            if not ok:
                flags.append((k, key, o[key], lo, hi))
            print(f"{k:<15}{fmt.format(o[key]):>7}{len(g):>5}{fmt.format(lo):>7}{fmt.format(st.median(g)):>7}"
                  f"{fmt.format(hi):>7}{(fmt.format(st.median(e)) if len(e) >= 5 else '-'):>13}   {'ok' if ok else 'OUT'}")

    print("\n" + ("outside p25-p75:" if flags else "every section inside p25-p75 on every measure"))
    for k, meas, v, lo, hi in flags:
        print(f"  {k:<15}{meas:<8}{v:>7}   band {lo} to {hi}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
