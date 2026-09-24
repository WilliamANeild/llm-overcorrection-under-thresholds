#!/usr/bin/env python3
"""
Compile and report the two numbers that decide whether the paper is submittable:
the page the body ends on, and the total page count.

Both builds are checked. main.tex carries a \\newif switch that selects the camera-ready
form or the anonymised ARR form, and the anonymised one is what reviewers see, so it is
the one the page limit has to hold against. Line numbers and the suppressed author block
change the layout, so the two builds can disagree.

The body-end page is read from the .aux via a label placed after the conclusion, so it is
exact rather than estimated. ARR allows 8 pages of body; Limitations, references and
appendices sit outside that.

    python3 paper/build_check.py            compile both, then report
    python3 paper/build_check.py --quiet    report only the summary lines
    python3 paper/build_check.py --fast     camera-ready build only
"""
import re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIMIT = 8
QUIET = "--quiet" in sys.argv


def compile_variant(stem, source=None):
    """Compile stem.tex (or a temp file holding `source`) and return (body, total, warns)."""
    tmp = None
    if source is not None:
        tmp = HERE / f"{stem}.tex"
        tmp.write_text(source)
    try:
        r = subprocess.run(["tectonic", "-X", "compile", f"{stem}.tex", "--outdir", "builds/",
                            "--keep-intermediates"], cwd=HERE, capture_output=True, text=True)
    finally:
        if tmp is not None:
            tmp.unlink(missing_ok=True)

    if r.returncode != 0:
        errs = [l for l in r.stderr.splitlines() if l.startswith("error")]
        return None, None, ["BUILD FAILED"] + errs[:8]

    warns = sorted({l.replace("warning: ", "") for l in r.stderr.splitlines()
                    if "Overfull" in l or "undefined" in l.lower()})

    aux = (HERE / "builds" / f"{stem}.aux").read_text(errors="replace")
    m = re.search(r'\\newlabel\{endofbody\}\{\{[^}]*\}\{(\d+)\}', aux)
    body = int(m.group(1)) if m else None

    info = subprocess.run(["pdfinfo", str(HERE / "builds" / f"{stem}.pdf")],
                          capture_output=True, text=True).stdout
    m = re.search(r'^Pages:\s+(\d+)', info, re.M)
    total = int(m.group(1)) if m else None
    return body, total, warns


def report(label, body, total, warns):
    if not QUIET:
        if warns and warns[0] == "BUILD FAILED":
            print(f"{label}: BUILD FAILED")
            for w in warns[1:]:
                print("   ", w)
            return False
        if warns:
            print(f"{label}: {len(warns)} layout warning(s)")
            for w in warns[:8]:
                print("   ", w)
        else:
            print(f"{label}: no overfull boxes, no undefined references")
    ok = bool(body) and body <= LIMIT
    over = f", {body - LIMIT} over" if body and body > LIMIT else ""
    print(f"  {label:<14} body ends p{body} / limit {LIMIT}   "
          f"total {total} pages   [{'OK' if ok else 'OVER'}{over}]")
    return ok


src = (HERE / "main.tex").read_text()
# Target the \newif line itself, not the first occurrence of the word: the switch is
# also named in the comment above it, and a bare replace flips the comment and leaves the
# real setting alone, which silently compiles the camera-ready twice.
SWITCH = re.compile(r'^(\s*\\newif\\ifreview\s*)\\reviewfalse', re.M)
if not SWITCH.search(src):
    sys.exit("main.tex no longer sets \\reviewfalse on the \\newif line; "
             "update build_check.py to match how the review build is now selected")

ok = report("camera-ready", *compile_variant("main"))

if "--fast" not in sys.argv:
    body, total, warns = compile_variant("_review", SWITCH.sub(r"\1\\reviewtrue", src, count=1))
    ok &= report("ARR review", body, total, warns)
    for f in (HERE / "builds").glob("_review.*"):
        f.unlink()

sys.exit(0 if ok else 1)
