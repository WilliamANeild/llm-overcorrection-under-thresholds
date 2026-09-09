#!/usr/bin/env python3
"""
Build a standalone reading copy of the introduction and Figure 1.

Reads the live section file, so the reading copy cannot drift from the paper. The only
change made is to drop the caption's pointer to the appendix, which does not exist in a
document containing only the introduction.

    python3 paper/build_reading_copy.py
"""
import re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "sections" / "introduction_v2.tex").read_text()

# the appendix does not exist in this document; the sentence pointing at it would print "??"
out, n = re.subn(r'\s*The full exchange\s+and every judge rationale appear in Appendix~\\ref\{sec:appendix-teaser\}\.',
                 '', src)
if n != 1:
    sys.exit(f"expected exactly one appendix pointer in the caption, found {n}")

(HERE / "builds").mkdir(exist_ok=True)
(HERE / "builds" / "_intro_reading.tex").write_text(out)
print(f"prepared reading copy of the introduction ({n} appendix pointer removed)")
r = subprocess.run(["tectonic", "-X", "compile", "intro_standalone.tex", "--outdir", "builds/"],
                   cwd=HERE, capture_output=True, text=True)
for line in r.stderr.splitlines():
    if line.startswith(("error", "note: Writing")) or "Overfull" in line:
        print(" ", line)
sys.exit(r.returncode)
