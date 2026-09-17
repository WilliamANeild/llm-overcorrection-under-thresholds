#!/usr/bin/env python3
"""
Pull every quantity out of the paper and out of the analysis ledger, with enough context
to match them, and write both lists to one file for the number-ledger auditor agent.

The extraction is deterministic, so it is a script. The matching needs judgment (the same
quantity is stated as 87.6% in one place and 631 of 720 in another, and two numbers can
legitimately differ because they are computed on different bases), so that is the agent's
job and this script does not attempt it.

    python3 paper/extract_numbers.py

Input:  paper/sections/*.tex (resolved from main.tex), results_FINAL.md
Output: paper/reference/number_extract.md
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
# Study 3 numbers live in results_FINAL.md; Study 1 and Study 2, reported in the appendix,
# have their own records. A paper number missing from ALL of them has no ledger backing.
LEDGERS = [ROOT / "results_FINAL.md", ROOT / "MOMENTUM_SUMMARY.md", ROOT / "PIPELINE.md"]
OUT = HERE / "reference" / "number_extract.md"

# Numerals that are structure rather than evidence. Tagged, not dropped, so the agent can
# see what was set aside and disagree.
STRUCTURAL = [
    (r'Turn~?\d|turn \d', "turn index"),
    (r'[Ll]evel~?\d|\\geq 4|level $\\geq', "scale level"),
    (r'(Table|Figure|Section|Appendix|Appendices)~?\\?ref|~\\ref\{', "cross-reference"),
    (r'\d{4}[a-z]?\}|\\cite', "citation year"),
    (r'\d+(\.\d+)?(pt|cm|in|em|ex|\\textwidth|\\columnwidth)', "typesetting dimension"),
]

KINDS = [
    (r'p\s*(=|<|>)\s*', "p-value"),
    (r'\\times 10\^', "p-value"),
    (r'%', "percentage"),
    (r'\bCI\b|\[\s*[\d.]+\s*%?\s*,', "confidence interval"),
    (r'\\kappa|\bkappa\b|Spearman|Wilcoxon|\br\s*=|\\alpha\s*=', "reliability or effect size"),
    (r'\bn\s*=|\bN\s*=|\d+\s*/\s*\d+|\bof\s+\d', "count or denominator"),
    (r'[-+]?\d\.\d+', "mean or delta"),
]


def live_sections():
    seen, queue = [], ["main.tex"]
    while queue:
        f = queue.pop(0)
        p = HERE / f
        if not p.exists() or f in seen:
            continue
        seen.append(f)
        body = re.sub(r'(?<!\\)%.*', '', p.read_text())
        for m in re.finditer(r'\\(?:input|include)\{([^}]+)\}', body):
            t = m.group(1)
            queue.append(t if t.endswith(".tex") else t + ".tex")
    return [f for f in seen if f.startswith("sections/")]


def classify(context):
    for pat, tag in STRUCTURAL:
        if re.search(pat, context):
            return tag, True
    for pat, tag in KINDS:
        if re.search(pat, context):
            return tag, False
    return "bare number", False


# _fig1_appendix reproduces a model transcript verbatim. Numbers inside the quoted output
# are the model's own words, not claims the paper makes, and have no ledger entry by design.
TRANSCRIPTS = ("_fig1_appendix",)


def paper_numbers(files):
    rows = []
    for f in files:
        transcript = any(k in f for k in TRANSCRIPTS)
        raw = re.sub(r'(?<!\\)%.*', '', (HERE / f).read_text())
        floats = [(m.start(), m.end()) for m in
                  re.finditer(r'\\begin\{(figure|table)\*?\}.*?\\end\{\1\*?\}', raw, re.S)]
        for m in re.finditer(r'(?<![\w.])\d+(?:,\d{3})*(?:\.\d+)?(?![\w])', raw):
            s, e = m.span()
            ctx = re.sub(r'\s+', ' ', raw[max(0, s - 110):e + 110]).strip()
            kind, structural = classify(ctx)
            if transcript:
                kind, structural = "quoted transcript", True
            rows.append({
                "value": m.group(0),
                "where": f"{f}:{raw[:s].count(chr(10)) + 1}",
                "in_float": any(a <= s < b for a, b in floats),
                "kind": kind,
                "structural": structural,
                "context": ctx,
            })
    return rows


def ledger_numbers():
    rows = []
    for led in LEDGERS:
        if not led.exists():
            continue
        rows.extend(_one_ledger(led))
    return rows


def _one_ledger(led):
    lines = led.read_text().split("\n")
    section = subsection = ""
    last_filter = ""
    rows = []
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            section, subsection = line[3:].strip(), ""
        elif line.startswith("### "):
            subsection = line[4:].strip()
        if re.match(r'\s*-\s*\*\*Filter', line):
            last_filter = re.sub(r'\s+', ' ', line).strip()[:300]
        for m in re.finditer(r'(?<![\w.])\d+(?:,\d{3})*(?:\.\d+)?(?![\w])', line):
            ctx = re.sub(r'\s+', ' ', line).strip()
            if len(ctx) < 4:
                continue
            rows.append({
                "value": m.group(0),
                "where": f"{led.name}:{i}",
                "section": section,
                "subsection": subsection,
                "kind": classify(ctx)[0],
                "context": ctx[:200],
                "filter": last_filter,
                "ledger": led.name,
            })
    return rows


def main():
    files = live_sections()
    pn = paper_numbers(files)
    ln = ledger_numbers()
    evid = [r for r in pn if not r["structural"]]

    # a value present in the ledger at all is cheap to establish mechanically; whether it
    # backs THIS sentence is not, and is left to the agent
    ledger_values = {r["value"] for r in ln}
    unmatched = [r for r in evid if r["value"] not in ledger_values]

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w") as fh:
        fh.write("# Number extract\n\n")
        fh.write(f"Written by `paper/extract_numbers.py`. Sections read: {', '.join(files)}.\n\n")
        fh.write(f"- {len(pn)} numerals in the paper, of which {len(pn) - len(evid)} are "
                 f"structural (turn indices, scale levels, cross-references, citation years, "
                 f"typesetting dimensions) and set aside.\n")
        fh.write(f"- {len(evid)} evidential numerals remain.\n")
        fh.write(f"- {len(ln)} numerals across " + ", ".join(f"`{l.name}`" for l in LEDGERS if l.exists()) + ".\n")
        fh.write(f"- {len(unmatched)} paper values do not appear anywhere in the ledger as a "
                 f"literal string. That is a starting point, not a finding: a paper may state "
                 f"87.6% where the ledger states 631/720, and a rounded value will not match.\n\n")

        fh.write("## Paper values with no literal match in the ledger\n\n")
        fh.write("| value | where | kind | float? | context |\n|---|---|---|---|---|\n")
        for r in sorted(unmatched, key=lambda x: x["where"]):
            fh.write(f"| `{r['value']}` | {r['where']} | {r['kind']} | "
                     f"{'yes' if r['in_float'] else ''} | {r['context'][:150]} |\n")

        fh.write("\n## Every evidential value in the paper\n\n")
        fh.write("| value | where | kind | float? | context |\n|---|---|---|---|---|\n")
        for r in sorted(evid, key=lambda x: x["where"]):
            fh.write(f"| `{r['value']}` | {r['where']} | {r['kind']} | "
                     f"{'yes' if r['in_float'] else ''} | {r['context'][:150]} |\n")

        fh.write("\n## The ledgers, by section, with the filter each number was computed under\n\n")
        cur = None
        for r in ln:
            head = (r["section"], r["subsection"])
            head = (r["ledger"],) + head
            if head != cur:
                cur = head
                fh.write(f"\n### [{r['ledger']}] {r['section']}" + (f" -- {r['subsection']}" if r['subsection'] else "") + "\n\n")
                if r["filter"]:
                    fh.write(f"*{r['filter']}*\n\n")
            fh.write(f"- `{r['value']}` ({r['where']}, {r['kind']}) {r['context']}\n")

    print(f"{len(pn)} paper numerals ({len(evid)} evidential), {len(ln)} ledger numerals")
    print(f"{len(unmatched)} paper values with no literal match in the ledger")
    print(f"written: {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
