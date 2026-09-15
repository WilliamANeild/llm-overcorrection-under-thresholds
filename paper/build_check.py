#!/usr/bin/env python3
"""
Compile and report the two numbers that decide whether the paper is submittable:
the page the body ends on, and the total page count.

The body-end page is read from main.aux via a label placed after the conclusion, so it
is exact rather than estimated. ARR allows 8 pages of body; Limitations, references and
appendices sit outside that.

    python3 paper/build_check.py            compile, then report
    python3 paper/build_check.py --quiet    report only the summary line
"""
import re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIMIT = 8

r = subprocess.run(["tectonic", "-X", "compile", "main.tex", "--outdir", "builds/",
                    "--keep-intermediates"], cwd=HERE, capture_output=True, text=True)
errs = [l for l in r.stderr.splitlines() if l.startswith("error")]
warn = sorted({l for l in r.stderr.splitlines() if "Overfull" in l or "undefined" in l.lower()})
if r.returncode != 0:
    print("BUILD FAILED"); print("\n".join(errs[:10])); sys.exit(2)

aux = (HERE / "builds" / "main.aux").read_text(errors="replace")
m = re.search(r'\\newlabel\{endofbody\}\{\{[^}]*\}\{(\d+)\}', aux)
body = int(m.group(1)) if m else None

pdf = HERE / "builds" / "main.pdf"
total = subprocess.run(["mdls", "-name", "kMDItemNumberOfPages", str(pdf)],
                       capture_output=True, text=True).stdout
total = int(re.search(r'= (\d+)', total).group(1)) if "=" in total else None

if "--quiet" not in sys.argv:
    if warn:
        print(f"{len(warn)} layout warning(s):")
        for w in warn[:8]:
            print("   ", w.replace("warning: ", ""))
    else:
        print("no overfull boxes, no undefined references")
status = "OK" if body and body <= LIMIT else "OVER"
print(f"body ends p{body} / limit {LIMIT}   total {total} pages   [{status}"
      + (f", {body - LIMIT} over]" if body and body > LIMIT else "]"))
sys.exit(0 if body and body <= LIMIT else 1)
