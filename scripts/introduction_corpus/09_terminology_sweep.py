#!/usr/bin/env python3
"""
Terminology consistency across the whole live build, appendix included.

Finds places where one concept carries more than one name, by four independent routes
rather than by a hand-written list of suspects:

  1. head-noun grouping   several modifier phrases sharing a technical head noun
  2. hyphen and spacing   forms that differ only in hyphenation or spacing
  3. capitalisation       the same term cased two ways
  4. role words           which word names the LLM scorer and which names the humans

    python3 scripts/introduction_corpus/09_terminology_sweep.py
"""
import re
from collections import defaultdict
from pathlib import Path

SEC = Path(__file__).resolve().parents[2] / "paper/sections"
FILES = ["abstract_v2", "introduction_v2", "related_work_v2", "methods", "results_v2",
         "discussion", "conclusion", "limitations", "appendix"]

HEADS = """threshold point revision response commentary panel probe score level turn rate
tax judge evaluator annotator rater trial output draft classifier estimator sample
criterion baseline condition analysis comparison content wrapper""".split()

STOP = set("""the a an and or of to in on for with by at from as is are was were be been
this that these those our we its their it he she they which where when what how than
then but not no all any each per both same other more most less least very only also
such into over under after before between during""".split())


def load():
    out = {}
    for f in FILES:
        t = re.sub(r'(?<!\\)%.*', '', (SEC / f"{f}.tex").read_text())
        t = re.sub(r'\\begin\{(figure|table|tabular)\*?\}.*?\\end\{\1\*?\}', ' ', t, flags=re.S)
        t = re.sub(r'\\(cite[tp]?|ref|label)\{[^}]*\}', ' ', t)
        t = re.sub(r'\\(section|subsection|paragraph|textbf|textit|emph)\*?\{([^}]*)\}', r' \2 ', t)
        t = re.sub(r'\$[^$]*\$', ' ', t)
        t = re.sub(r'\\[a-zA-Z]+\*?', ' ', t)
        out[f] = re.sub(r'\s+', ' ', t.replace('~', ' ')).strip()
    return out


def phrases_by_head(text):
    """modifier phrases (1 to 3 words) immediately preceding each technical head noun"""
    found = defaultdict(lambda: defaultdict(int))
    toks = re.findall(r"[A-Za-z][A-Za-z'\-]*", text)
    low = [w.lower() for w in toks]
    for i, w in enumerate(low):
        h = w.rstrip('s') if w.rstrip('s') in HEADS else (w if w in HEADS else None)
        if not h:
            continue
        mods = []
        for j in range(i - 1, max(-1, i - 4), -1):
            if low[j] in STOP or low[j] in HEADS:
                break
            mods.insert(0, low[j])
        if mods:
            found[h][" ".join(mods)] += 1
    return found


def main():
    secs = load()
    whole = " ".join(secs.values())

    print("1. SEVERAL NAMES SHARING ONE HEAD NOUN")
    print("   (each group is one head; judge whether the modifiers name one thing)\n")
    groups = phrases_by_head(whole)
    hits = 0
    for head in sorted(groups):
        variants = {m: n for m, n in groups[head].items() if n >= 2}
        if len(variants) >= 2:
            hits += 1
            items = sorted(variants.items(), key=lambda x: -x[1])
            print(f"   {head:<12} " + ";  ".join(f"{m} ({n})" for m, n in items[:6]))
    if not hits:
        print("   none")

    print("\n2. HYPHEN AND SPACING VARIANTS")
    toks = re.findall(r"[A-Za-z][A-Za-z\-]{3,}", whole)
    norm = defaultdict(set)
    for t in toks:
        norm[t.lower().replace('-', '')].add(t.lower())
    found = False
    for k, v in sorted(norm.items()):
        if len(v) > 1:
            found = True
            print("   " + ";  ".join(f"{x} ({len(re.findall(re.escape(x), whole, re.I))})" for x in sorted(v)))
    # two-word vs hyphenated
    for a in ["multi turn", "meta response", "meta commentary", "per model", "first turn", "five turn"]:
        n2 = len(re.findall(a, whole, re.I)); n1 = len(re.findall(a.replace(' ', '-'), whole, re.I))
        if n2 and n1:
            found = True
            print(f"   {a} ({n2});  {a.replace(' ', '-')} ({n1})")
    if not found:
        print("   none")

    print("\n3. CAPITALISATION OF DEFINED TERMS")
    for term in ["sufficient", "functional", "incomplete", "inadequate", "polished", "overdone",
                 "revision tax", "balanced panel", "genuine revision", "meta-response", "turn"]:
        up = len(re.findall(r'\b' + term[0].upper() + term[1:], whole))
        lo = len(re.findall(r'\b' + term[0].lower() + term[1:], whole))
        if up and lo:
            print(f"   {term:<18} capitalised {up:>3}   lower {lo:>3}")

    print("\n4. WHO DOES THE SCORING: one word per role?")
    for w in ["evaluator", "judge", "rater", "annotator", "scorer", "grader"]:
        per = {f: len(re.findall(r'\b' + w, s, re.I)) for f, s in secs.items()}
        per = {f: n for f, n in per.items() if n}
        if per:
            print(f"   {w:<11}{sum(per.values()):>4}   {per}")


if __name__ == "__main__":
    main()
