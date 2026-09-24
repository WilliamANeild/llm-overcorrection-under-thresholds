#!/usr/bin/env python3
"""
Deterministic pre-submission checks. Runs first in the proofread process and must pass
before any agent is spent on the draft.

Every check here exists because the defect it looks for actually happened in this project.
Nothing here needs judgment, so nothing here is an agent.

    python3 paper/preflight.py            full report
    python3 paper/preflight.py --quiet    failures and warnings only
    python3 paper/preflight.py --no-build skip the tectonic compile (fast)

Exit status: 0 if no FAIL, 1 otherwise. Warnings never change the exit status; they are
findings for a human, not blockers.
"""
import re, subprocess, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
QUIET = "--quiet" in sys.argv

# Identity strings that must not ship. The rater table taught us to sweep the whole build
# rather than the lines someone flagged: the first name matched the author, so that table
# de-anonymised the submission on its own.
IDENTITY = [r"Liam\b", r"Neild", r"Sophie", r"Troy", r"@emory\.edu", r"/Users/liamneild"]
PLACEHOLDERS = [r"TKTK", r"\bTODO\b", r"\[TODO-SRC\]", r"\bXXX\b", r"\bFIXME\b",
                r"\\pvalstripped", r"\\rvalstripped", r"\bTBD\b"]

findings = defaultdict(list)


def add(check, level, msg):
    findings[check].append((level, msg))


def live_files():
    """Every .tex the build actually reads, resolved recursively from main.tex."""
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
    return seen


def text_of(files, strip_comments=True):
    out = {}
    for f in files:
        raw = (HERE / f).read_text()
        out[f] = re.sub(r'(?<!\\)%.*', '', raw) if strip_comments else raw
    return out


# ---------------------------------------------------------------- 1. build

def check_build():
    if "--no-build" in sys.argv:
        add("build", "SKIP", "skipped (--no-build)")
        return
    r = subprocess.run([sys.executable, str(HERE / "build_check.py"), "--quiet"],
                       capture_output=True, text=True)
    for line in r.stdout.splitlines():
        if line.strip():
            lvl = "PASS" if "[OK]" in line else "FAIL"
            add("build", lvl, line.strip())
    if r.returncode != 0 and not any(l == "FAIL" for l, _ in findings["build"]):
        add("build", "FAIL", "build_check.py exited non-zero")


# ------------------------------------------------- 2. placeholders, 3. floats

def check_placeholders(live):
    for f, t in text_of(live).items():
        for pat in PLACEHOLDERS:
            for m in re.finditer(pat, t):
                line = t[:m.start()].count("\n") + 1
                add("placeholders", "FAIL", f"{f}:{line} {m.group(0)!r} in text that compiles")
    # comments do not print but ship with the source
    for f, t in text_of(live, strip_comments=False).items():
        for m in re.finditer(r'(?<!\\)%.*?(TKTK|TODO|FIXME).*', t):
            line = t[:m.start()].count("\n") + 1
            add("placeholders", "WARN", f"{f}:{line} in a comment: {m.group(0).strip()[:64]}")


def check_float_refs(live):
    txt = text_of(live)
    labels = {}
    for f, t in txt.items():
        for m in re.finditer(r'\\begin\{(figure|table)\*?\}(.*?)\\end\{\1\*?\}', t, re.S):
            for lm in re.finditer(r'\\label\{([^}]+)\}', m.group(2)):
                labels[lm.group(1)] = (f, t[:m.start()].count("\n") + 1, m.group(1))
    allt = " ".join(txt.values())
    for lab, (f, line, _) in sorted(labels.items()):
        refs = len(re.findall(r'\\(?:ref|autoref|Cref|cref)\{' + re.escape(lab) + r'\}', allt))
        if refs == 0:
            add("float-refs", "WARN", f"{f}:{line} float {lab} is never referenced from prose")
    if not any(l == "WARN" for l, _ in findings["float-refs"]):
        add("float-refs", "PASS", f"all {len(labels)} floats referenced")


# --------------------------------------------- 4. dead sources, 5. cite keys

def check_dead_sources(live):
    add("dead-sources", "PASS", f"main.tex reads {len(live)} files: " + ", ".join(live[:4]) + " ...")
    on_disk = {p.name for p in (HERE / "sections").glob("*.tex")}
    used = {Path(f).name for f in live}
    for orphan in sorted(on_disk - used):
        add("dead-sources", "WARN", f"sections/{orphan} is not read by main.tex")
    for bak in sorted((HERE / "sections").glob("*.bak*")) + sorted((HERE / "sections").glob(".*.bak*")):
        add("dead-sources", "WARN", f"orphan backup {bak.relative_to(HERE)}")
    # a retired file pointing at a figure that no longer exists is a trap for a later session
    for p in (HERE / "sections").glob("*.tex"):
        if Path(p.name) in {Path(f).name for f in live}:
            continue
        for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', p.read_text()):
            tgt = m.group(1)
            if not any((HERE / tgt).exists() or (HERE / (tgt + ext)).exists() for ext in (".pdf", ".png")):
                add("dead-sources", "WARN",
                    f"sections/{p.name} (retired) includes {tgt}, which is not on disk")


def check_cite_keys(live):
    txt = " ".join(text_of(live).values())
    cited = {k.strip() for c in re.findall(r'\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}', txt)
             for k in c.split(",") if k.strip()}
    bib = (HERE / "references.bib").read_text()
    entries = {m.group(1) for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib)}
    for k in sorted(cited - entries):
        add("cite-keys", "FAIL", f"\\cite{{{k}}} has no entry in references.bib")
    for k in sorted(entries - cited):
        add("cite-keys", "WARN", f"references.bib entry {k} is never cited")
    for k in sorted(cited & entries):
        m = re.search(r'@\w+\s*\{\s*' + re.escape(k) + r'\s*,(.*?)\n\}', bib, re.S)
        y = re.search(r'year\s*=\s*\{?\s*(\d{4})', m.group(1)) if m else None
        ky = re.search(r'(\d{4})', k)
        if y and ky and y.group(1) != ky.group(1):
            add("cite-keys", "WARN",
                f"{k} key says {ky.group(1)} but the entry says {y.group(1)}")
    if not findings["cite-keys"]:
        add("cite-keys", "PASS", f"{len(cited)} keys, all present and consistent")


# ----------------------------------------------------------- 6. anonymity

def check_anonymity(live):
    src = (HERE / "main.tex").read_text()
    review = bool(re.search(r'^\s*\\newif\\ifreview\s*\\reviewtrue', src, re.M))
    # Identity inside an \ifreview...\fi region is conditional by construction: the
    # review branch is what reviewers get, and whether that branch is really clean is
    # settled below by compiling it and reading the page. Trusting the conditional
    # without rendering is exactly what hid a leaked author block.
    author_lines = set()
    for reg in re.finditer(r'\\ifreview\b.*?\\fi', src, re.S):
        author_lines |= set(range(src[:reg.start()].count('\n') + 1,
                                  src[:reg.end()].count('\n') + 2))
    if not re.search(r'\\author\{', src):
        add('anonymity', 'FAIL', 'no \\author block in main.tex; cannot check anonymity')
    for f, t in text_of(live, strip_comments=False).items():
        for m in re.finditer(r'(?<!\\)%.*?(TKTK|TODO|FIXME).*', t):
            line = t[:m.start()].count("\n") + 1
            add("placeholders", "WARN", f"{f}:{line} in a comment: {m.group(0).strip()[:64]}")


def check_float_refs(live):
    txt = text_of(live)
    labels = {}
    for f, t in txt.items():
        for m in re.finditer(r'\\begin\{(figure|table)\*?\}(.*?)\\end\{\1\*?\}', t, re.S):
            for lm in re.finditer(r'\\label\{([^}]+)\}', m.group(2)):
                labels[lm.group(1)] = (f, t[:m.start()].count("\n") + 1, m.group(1))
    allt = " ".join(txt.values())
    for lab, (f, line, _) in sorted(labels.items()):
        refs = len(re.findall(r'\\(?:ref|autoref|Cref|cref)\{' + re.escape(lab) + r'\}', allt))
        if refs == 0:
            add("float-refs", "WARN", f"{f}:{line} float {lab} is never referenced from prose")
    if not any(l == "WARN" for l, _ in findings["float-refs"]):
        add("float-refs", "PASS", f"all {len(labels)} floats referenced")


# --------------------------------------------- 4. dead sources, 5. cite keys

def check_dead_sources(live):
    add("dead-sources", "PASS", f"main.tex reads {len(live)} files: " + ", ".join(live[:4]) + " ...")
    on_disk = {p.name for p in (HERE / "sections").glob("*.tex")}
    used = {Path(f).name for f in live}
    for orphan in sorted(on_disk - used):
        add("dead-sources", "WARN", f"sections/{orphan} is not read by main.tex")
    for bak in sorted((HERE / "sections").glob("*.bak*")) + sorted((HERE / "sections").glob(".*.bak*")):
        add("dead-sources", "WARN", f"orphan backup {bak.relative_to(HERE)}")
    # a retired file pointing at a figure that no longer exists is a trap for a later session
    for p in (HERE / "sections").glob("*.tex"):
        if Path(p.name) in {Path(f).name for f in live}:
            continue
        for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', p.read_text()):
            tgt = m.group(1)
            if not any((HERE / tgt).exists() or (HERE / (tgt + ext)).exists() for ext in (".pdf", ".png")):
                add("dead-sources", "WARN",
                    f"sections/{p.name} (retired) includes {tgt}, which is not on disk")


def check_cite_keys(live):
    txt = " ".join(text_of(live).values())
    cited = {k.strip() for c in re.findall(r'\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}', txt)
             for k in c.split(",") if k.strip()}
    bib = (HERE / "references.bib").read_text()
    entries = {m.group(1) for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib)}
    for k in sorted(cited - entries):
        add("cite-keys", "FAIL", f"\\cite{{{k}}} has no entry in references.bib")
    for k in sorted(entries - cited):
        add("cite-keys", "WARN", f"references.bib entry {k} is never cited")
    for k in sorted(cited & entries):
        m = re.search(r'@\w+\s*\{\s*' + re.escape(k) + r'\s*,(.*?)\n\}', bib, re.S)
        y = re.search(r'year\s*=\s*\{?\s*(\d{4})', m.group(1)) if m else None
        ky = re.search(r'(\d{4})', k)
        if y and ky and y.group(1) != ky.group(1):
            add("cite-keys", "WARN",
                f"{k} key says {ky.group(1)} but the entry says {y.group(1)}")
    if not findings["cite-keys"]:
        add("cite-keys", "PASS", f"{len(cited)} keys, all present and consistent")


# ----------------------------------------------------------- 6. anonymity

def check_anonymity(live):
    src = (HERE / "main.tex").read_text()
    review = bool(re.search(r'^\s*\\newif\\ifreview\s*\\reviewtrue', src, re.M))
    # The author block sits inside \ifreview/\else, so there are two of them and the
    # real one closes on an indented brace. Collect the lines of every \author{...}.
    author_lines = set()
    for ab in re.finditer(r'\\author\{.*?\n?\s*\}', src, re.S):
        author_lines |= set(range(src[:ab.start()].count("\n") + 1,
                                  src[:ab.end()].count("\n") + 2))
    if not author_lines:
        add("anonymity", "FAIL", "no \\author block found in main.tex; the anonymity check cannot run")
    for f, t in text_of(live, strip_comments=False).items():
        for pat in IDENTITY:
            for m in re.finditer(pat, t):
                line = t[:m.start()].count("\n") + 1
                prints = "%" not in t[t.rfind("\n", 0, m.start()) + 1:m.start()]
                in_author_block = (f == "main.tex" and line in author_lines)
                if f == "main.tex":
                    # main.tex is settled by compiling the review branch and reading the
                    # rendered page, below. A source-position heuristic cannot tell which
                    # branch of \ifreview a line is in once the file has several of them,
                    # and a wrong guess here either hides a leak or invents one.
                    lvl, where = "PASS", "in main.tex; settled by the rendered check below"
                elif in_author_block:
                    # correct in camera-ready, suppressed by the review option
                    lvl, where = ("PASS", "inside an \\ifreview region; see the rendered check")
                elif prints:
                    lvl, where = "FAIL", "prints in the PDF"
                else:
                    lvl, where = "WARN", "in a comment, ships with source"
                add("anonymity", lvl, f"{f}:{line} {m.group(0)!r} {where}")
    if review and any("author block" in m for l, m in findings["anonymity"]):
        add("anonymity", "FAIL", "main.tex is \\reviewtrue but the author block still resolves; check acl.sty")
    for p in sorted((HERE / "figures").glob("*.py")) + sorted((ROOT / "scripts").rglob("*.py")):
        t = p.read_text(errors="replace")
        if "/Users/liamneild" in t:
            line = t[:t.index("/Users/liamneild")].count("\n") + 1
            add("anonymity", "WARN", f"{p.relative_to(ROOT)}:{line} absolute path carries the username")
    src = (HERE / "main.tex").read_text()
    state = "reviewtrue" if re.search(r'^\s*\\newif\\ifreview\s*\\reviewtrue', src, re.M) else "reviewfalse"
    add("anonymity", "PASS" if state == "reviewtrue" else "WARN",
        f"main.tex is set to \\{state} (submission needs \\reviewtrue)")

    # Compile the anonymised form and read the rendered page, rather than trusting that
    # flipping the switch suppresses anything. It did not: the author block was outside
    # the conditional for weeks, and the harness that was meant to catch it flipped the
    # word inside a comment instead of the switch, so it compiled the camera-ready twice.
    import subprocess
    switch = re.compile(r'^(\s*\\newif\\ifreview\s*)\\reviewfalse', re.M)
    if switch.search(src):
        tmp = HERE / "_anoncheck.tex"
        tmp.write_text(switch.sub(r'\1\\reviewtrue', src, count=1))
        try:
            r = subprocess.run(["tectonic", "-X", "compile", "_anoncheck.tex", "--outdir", "builds/"],
                               cwd=HERE, capture_output=True, text=True)
            if r.returncode == 0:
                pdf = HERE / "builds" / "_anoncheck.pdf"
                txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
                info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
                leaks = [n for n in ("Neild", "Emami", "emory.edu") if n in txt or n in info]
                add("anonymity", "FAIL" if leaks else "PASS",
                    f"anonymised build leaks {leaks}" if leaks
                    else "anonymised build renders no author name, affiliation or email")
            else:
                add("anonymity", "FAIL", "anonymised build does not compile")
        finally:
            tmp.unlink(missing_ok=True)
            for f in (HERE / "builds").glob("_anoncheck.*"):
                f.unlink()


# ------------------------------------- 8. promises, 9. duplicates, 10. axes

def check_promises(live):
    """Terms Methods coins in bold and no later section ever uses again.

    This reports DEAD COINAGE, not missing content: a metric can be reported under
    other wording while its coined name is never reused, which is what three of the
    four metric names in this paper do. Whether the underlying result is reported is
    a judgment call and belongs to the number-ledger agent, not here.

    False positives to expect: the six quality-scale level names are defined once as
    a scale and are not expected to recur, so they are excluded by name.
    """
    SCALE = {"inadequate", "incomplete", "functional", "sufficient", "polished", "overdone"}
    txt = text_of(live)
    coined = {}
    for f, s in txt.items():
        if "methods" not in f:
            continue
        # bold inside a float is a column header, not a coined term
        s = re.sub(r'\\begin\{(figure|table|tabular)\*?\}.*?\\end\{\1\*?\}',
                   lambda m: "\n" * m.group(0).count("\n"), s, flags=re.S)
        for m in re.finditer(r'\\textbf\{([A-Z][A-Za-z ,\-]{4,40})\}', s):
            term = m.group(1).strip().rstrip('.')
            if term.lower() in SCALE or len(term.split()) > 4:
                continue
            coined[term] = (f, s[:m.start()].count("\n") + 1)
    for term, (f, line) in sorted(coined.items()):
        # count uses anywhere outside the bold definition, hyphens and spaces alike
        loose = re.escape(term).replace(r'\-', '[- ]').replace(r'\ ', '[- ]')
        uses = 0
        for g, s in txt.items():
            body = re.sub(r'\\textbf\{' + re.escape(term) + r'\}', ' ', s)
            uses += len(re.findall(loose, body, re.I))
        if uses == 0:
            add("promises", "WARN",
                f"{f}:{line} coins {term!r} in bold and no section ever uses the term again")
    if not any(l == "WARN" for l, _ in findings["promises"]):
        add("promises", "PASS", f"{len(coined)} coined terms all reused at least once")


def check_duplicate_sentences(live):
    # _fig1_appendix reproduces a model transcript verbatim; the model repeating itself
    # across turns is the paper's finding, so repetition there is data, not a defect.
    TRANSCRIPTS = ("_fig1_appendix",)
    seen = {}
    for f, t in text_of(live).items():
        if any(k in f for k in TRANSCRIPTS):
            continue
        flat = re.sub(r'\s+', ' ', re.sub(r'\\begin\{(figure|table)\*?\}.*?\\end\{\1\*?\}', ' ', t, flags=re.S))
        for s in re.split(r'(?<=[.!?]) ', flat):
            norm = re.sub(r'[^a-z0-9 ]', '', re.sub(r'\\[a-zA-Z]+\*?', ' ', s).lower())
            norm = re.sub(r'\s+', ' ', norm).strip()
            if len(norm.split()) < 8:
                continue
            if norm in seen and seen[norm] != f:
                add("duplicates", "WARN", f"sentence repeated in {seen[norm]} and {f}: {norm[:78]}...")
            elif norm in seen:
                add("duplicates", "WARN", f"sentence repeated twice in {f}: {norm[:78]}...")
            seen[norm] = f
    if not any(l == "WARN" for l, _ in findings["duplicates"]):
        add("duplicates", "PASS", f"{len(seen)} sentences, none repeated")


def check_axis_limits(live):
    """Figure 2 once set ylim to 0.72 while three of its points were above 0.80.

    Only generators whose output the live build includes are scanned. Scratch and
    abandoned figure scripts set limits for figures nobody prints.
    """
    included = set()
    for f, t in text_of(live).items():
        for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', t):
            included.add(Path(m.group(1)).stem)
    n = 0
    for p in sorted((HERE / "figures").glob("*.py")):
        src = p.read_text(errors="replace")
        if not any(stem in src for stem in included):
            continue
        for m in re.finditer(r'set_(x|y)lim\(\s*([-\d.]+)\s*,\s*([-\d.]+)', src):
            n += 1
            line = src[:m.start()].count("\n") + 1
            add("axis-limits", "WARN",
                f"figures/{p.name}:{line} hardcodes {m.group(1)}lim "
                f"({m.group(2)}, {m.group(3)}) — confirm no plotted point sits outside it")
    if not n:
        add("axis-limits", "PASS", "no hardcoded axis limits in any live figure generator")


def check_stale_docs(live):
    """A planning document that no longer describes the paper is a trap, not a record."""
    newest = max((HERE / f).stat().st_mtime for f in live)
    for rel in ["SKELETON.md", "../RECOMPUTE_TODO.md", "reference/build_formatting_audit.md"]:
        p = (HERE / rel)
        if p.exists() and p.stat().st_mtime < newest:
            add("stale-docs", "WARN",
                f"{rel} predates the newest live section edit; confirm it still describes the paper")
    if not any(l == "WARN" for l, _ in findings["stale-docs"]):
        add("stale-docs", "PASS", "no known planning document is older than the draft")


# ---------------------------------------------------------- 7. terminology

def check_terminology():
    s = ROOT / "scripts/introduction_corpus/09_terminology_sweep.py"
    if not s.exists():
        add("terminology", "WARN", "09_terminology_sweep.py not found")
        return
    r = subprocess.run([sys.executable, str(s)], capture_output=True, text=True, cwd=ROOT)
    out = r.stdout
    (HERE / "reference").mkdir(exist_ok=True)
    rec = HERE / "reference/terminology_sweep.md"
    rec.write_text("# Terminology sweep\n\nWritten by `paper/preflight.py`. Flags need reading in "
                   "context: this sweep has produced false positives before, notably matching\n"
                   "\"sufficient threshold\" inside the correct phrase \"not-sufficient threshold\".\n\n"
                   "```\n" + out + "```\n")
    groups = len(re.findall(r'^   \w+\s+.*;', out, re.M))
    add("terminology", "WARN" if groups else "PASS",
        f"{groups} head-noun group(s) with several modifiers; full output written to "
        f"reference/terminology_sweep.md")


# ---------------------------------------------------------------- report

def main():
    live = live_files()
    check_build()
    check_placeholders(live)
    check_float_refs(live)
    check_dead_sources(live)
    check_cite_keys(live)
    check_anonymity(live)
    check_terminology()
    check_promises(live)
    check_duplicate_sentences(live)
    check_axis_limits(live)
    check_stale_docs(live)

    order = ["build", "placeholders", "cite-keys", "anonymity", "float-refs", "dead-sources",
             "terminology", "promises", "duplicates", "axis-limits", "stale-docs"]
    nf = nw = 0
    for c in order:
        items = findings.get(c, [])
        fails = [m for l, m in items if l == "FAIL"]
        warns = [m for l, m in items if l == "WARN"]
        nf += len(fails); nw += len(warns)
        mark = "FAIL" if fails else ("warn" if warns else "ok  ")
        print(f"[{mark}] {c}")
        for m in fails:
            print(f"        FAIL  {m}")
        if not QUIET:
            for m in [m for l, m in items if l in ("PASS", "SKIP")]:
                print(f"              {m}")
        for m in warns[:12]:
            print(f"        warn  {m}")
        if len(warns) > 12:
            print(f"              ... and {len(warns) - 12} more")

    print(f"\n{nf} failure(s), {nw} warning(s)")
    print("PREFLIGHT FAILED" if nf else "preflight passed; warnings are for a human to read")
    return 1 if nf else 0


if __name__ == "__main__":
    sys.exit(main())
