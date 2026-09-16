#!/usr/bin/env python3
"""
Build a reading copy running from the abstract through the Results section.

Reads main.tex and the live section files, so the reading copy cannot drift from the
paper. Discussion, Conclusion, Limitations and the Ethics Statement are dropped. The
appendix is kept: five sentences in the retained sections point into it, and without it
they print "??".

    python3 paper/build_results_reading.py
"""
import re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "main.tex").read_text()

# everything from the discussion up to the bibliography goes; the appendix stays so the
# five Appendix~\ref pointers in the retained sections still resolve
start = r"\input{sections/discussion}"
end = r"\bibliography{references}"
if src.count(start) != 1 or src.count(end) != 1:
    sys.exit(f"main.tex structure has moved: found {src.count(start)} discussion inputs "
             f"and {src.count(end)} bibliography lines, expected one of each")
i, j = src.index(start), src.index(end)
out = src[:i] + src[j:]

for gone in ("sections/conclusion", "sections/limitations", "Ethics Statement"):
    if gone in out:
        sys.exit(f"{gone} survived the excision; check main.tex ordering")

(HERE / "builds").mkdir(exist_ok=True)
(HERE / "builds" / "results_reading.tex").write_text(out)

# tectonic resolves \input paths relative to the main file, so build from paper/
tmp = HERE / "_results_reading.tex"
tmp.write_text(out)
try:
    r = subprocess.run(["tectonic", "-X", "compile", tmp.name, "--outdir", "builds/"],
                       cwd=HERE, capture_output=True, text=True)
finally:
    tmp.unlink(missing_ok=True)

for line in r.stderr.splitlines():
    if "Overfull" in line or "undefined" in line.lower() or line.startswith("error"):
        print(" ", line)
if r.returncode == 0:
    pdf = HERE / "builds" / "_results_reading.pdf"
    print(f"built {pdf} ({pdf.stat().st_size // 1024} KB)")
sys.exit(r.returncode)
