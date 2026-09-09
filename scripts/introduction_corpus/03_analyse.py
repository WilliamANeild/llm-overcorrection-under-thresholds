#!/usr/bin/env python3
"""
Distributions over the extended introduction corpus, split by whether the arXiv
record states an ACL-family venue, plus the top-level section-count benchmark
(counted from the same cached HTML).

    python3 scripts/introduction_corpus/03_analyse.py
"""
import json, re, statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / ".workspace/reference/intro_corpus"
CACHE = OUT / "html"

# Venue as stated in the arXiv record. The first four are the ACL-family papers of
# the original 23 (paper/rules/03_introduction.md corpus table); everything fetched
# in the extension pass was selected on a stated ACL-family venue.
ORIGINAL_ACL = {"2311.08516", "2402.14762", "2402.14809", "2406.01297"}
ORIGINAL_OTHER_VENUE = {"2310.01798", "2306.05685", "2201.06796"}
ORIGINAL = {"2201.06796", "2206.05802", "2212.09746", "2303.11366", "2303.17651",
            "2306.05685", "2308.03188", "2308.03958", "2310.01798", "2310.12397",
            "2310.13548", "2311.07961", "2311.08516", "2401.16745", "2402.14762",
            "2402.14809", "2403.04132", "2404.12272", "2404.13076", "2406.01297",
            "2410.16184", "2501.17399", "2505.06120"}

STOP = re.compile(r'\b(references|acknowledg|appendix|bibliography|limitations|ethic)', re.I)


def section_counts(aid):
    f = CACHE / f"{aid}.html"
    if not f.exists():
        return None
    html = f.read_text(errors="replace")
    tops, subs, stop = [], 0, False
    for m in re.finditer(r'<h([23])[^>]*ltx_title_(sub)?section[^>]*>(.*?)</h\1>', html, re.S):
        title = re.sub(r'<[^>]+>', ' ', m.group(3))
        title = re.sub(r'\s+', ' ', title).strip()
        if m.group(1) == '2':
            if STOP.search(title):
                stop = True
                continue
            if not stop:
                tops.append(title)
        elif not stop:
            subs += 1
    return {"top_level": len(tops), "subsections": subs, "titles": tops}


def q(v, p):
    v = sorted(v)
    return v[int(p * (len(v) - 1))]


def describe(name, rows, keys):
    print(f"\n{'='*74}\n{name}  (n = {len(rows)})\n{'='*74}")
    for k, label in keys:
        v = [r[k] for r in rows if r.get(k) is not None]
        if not v:
            continue
        print(f"  {label:<26} min {min(v):>6.0f}  p25 {q(v,.25):>6.0f}  median {st.median(v):>6.1f}"
              f"  p75 {q(v,.75):>6.0f}  max {max(v):>6.0f}")


def main():
    intros = json.loads((OUT / "intros.json").read_text())
    rows = []
    for aid, m in intros.items():
        if m.get("error") or not m.get("words"):
            print(f"excluded {aid}: {m.get('error', 'no words extracted')}")
            continue
        sc = section_counts(aid) or {}
        rows.append({**m, "aid": aid,
                     "acl": aid in ORIGINAL_ACL or aid not in ORIGINAL,
                     "top_level": sc.get("top_level"), "subsections": sc.get("subsections")})

    keys = [("words", "Intro words"), ("paragraphs", "Intro paragraphs"),
            ("citations", "Citation references"), ("cites_per_100w", "Cites per 100 words"),
            ("cites_p1", "Citations in paragraph 1"), ("cites_last2", "Citations, last 2 blocks")]
    describe("WHOLE CORPUS", rows, keys)
    describe("CONFIRMED ACL-FAMILY VENUE", [r for r in rows if r["acl"]], keys)
    describe("NO ACL-FAMILY VENUE STATED", [r for r in rows if not r["acl"]], keys)

    sec = [r for r in rows if r.get("top_level")]
    describe("SECTION STRUCTURE (all)", sec,
             [("top_level", "Top-level sections"), ("subsections", "Subsections (pre-appendix)")])
    acl_sec = [r for r in sec if r["acl"]]
    describe("SECTION STRUCTURE (ACL-family)", acl_sec,
             [("top_level", "Top-level sections"), ("subsections", "Subsections (pre-appendix)")])

    fig = [r for r in rows if r.get("figure_referenced")]
    print(f"\nIntroductions referencing a figure: {len(fig)} of {len(rows)} "
          f"({len(fig)/len(rows)*100:.0f}%)")
    ql = [r for r in rows if r["opening_sentence"].rstrip().endswith("?")]
    print(f"Introductions opening on a question: {len(ql)} of {len(rows)}")
    json.dump(rows, open(OUT / "rows.json", "w"), indent=1)


if __name__ == "__main__":
    main()
