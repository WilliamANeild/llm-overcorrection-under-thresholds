#!/usr/bin/env python3
"""
Build Figure 1: a real five-turn trial shown against the balanced-panel trajectory.

Everything on the figure is read from the project's data files at build time, so the
figure cannot drift from the analysis. Nothing is hand-entered and nothing is invented.

Trial: s3_worker__llama-3.3-70b__quarterly_sales__run3
  The user asks for a quarterly sales summary that "suggests a couple possible
  explanations" for the Q3 dip and Q4 spike. Turn 1 supplies them. By turn 5 they are
  gone, and the judge says so in its own rationale.

Text shown is the meta-commentary-stripped text, matching the stripped scores that are
primary throughout the paper. Omissions are marked [...]; nothing else is altered.

    python3 paper/figures/gen_fig1.py

Writes fig1.png and fig1.pdf next to this file.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import ast, json, subprocess
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = ROOT / "data" / "study3" / "raw_responses"
TRIAL = "s3_worker__llama-3.3-70b__quarterly_sales__run3"

# Level colours, shared by the bubble accent bars and the chart markers.
LEVEL_COLOUR = {5: "#2E7D32", 4: "#2E7D32", 3: "#EF6C00", 2: "#E53935", 1: "#B71C1C"}
GREY = "#78909C"
BLUE = "#2E6FA7"   # comparison series; darker than the #4878A8 used in Results
INK = "#1a1a1a"


def stripper():
    """Load strip_text without executing the module body.

    strip_meta_commentary.py has no main guard and rewrites annotation files when
    imported, so only the pure definitions are extracted and compiled here.
    """
    src = (ROOT / "scripts" / "study3" / "strip_meta_commentary.py").read_text()
    keep, wanted = [], {"is_meta_paragraph", "split_paragraphs", "strip_text",
                        "PREAMBLE_META", "POSTAMBLE_META", "CONTENT_SIGNALS"}
    for node in ast.parse(src).body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            keep.append(node)
        elif isinstance(node, ast.FunctionDef) and node.name in wanted:
            keep.append(node)
        elif isinstance(node, ast.Assign) and any(
                getattr(t, "id", None) in wanted for t in node.targets):
            keep.append(node)
    ns = {}
    exec(compile(ast.Module(body=keep, type_ignores=[]), "<strip>", "exec"), ns)
    return ns["strip_text"]


def load():
    strip_text = stripper()
    trial = next(json.loads(l) for l in open(RAW / "worker_trials.jsonl")
                 if json.loads(l)["trial_id"] == TRIAL)
    stripped, words, levels = {}, {}, {}
    for i, resp in enumerate(trial["responses"], 1):
        s = strip_text(resp)
        s = s[0] if isinstance(s, tuple) else s
        stripped[i], words[i] = s, len(s.split())
    from scripts.config import recode_level as recode
    for line in open(RAW / "stripped_rescore_full.jsonl"):
        r = json.loads(line)
        if r["trial_id"] == TRIAL:
            levels[r["turn"]] = recode(r["stripped_score"])
    rationale = {}
    for line in open(RAW / "evaluator_results.jsonl"):
        r = json.loads(line)
        if r["worker_trial_id"] == TRIAL and r["eval_id"].endswith("clean"):
            rationale[r["turn"]] = r["rationale"]
    billed = np.cumsum([t["input"] + t["output"] for t in trial["token_counts"]])

    # balanced panel mean (GENUINE at all of turns 2-5), stripped, for the grey line
    labels = {}
    for line in open(RAW / "genuine_meta_labels.jsonl"):
        r = json.loads(line)
        labels[(r["trial_id"], r["turn"])] = r["classifier_label"]
    scores = {}
    for line in open(RAW / "stripped_rescore_full.jsonl"):
        r = json.loads(line)
        scores[(r["trial_id"], r["turn"])] = recode(r["stripped_score"])
    trials = {t for t, _ in labels}
    panel = [t for t in trials if all(labels.get((t, k)) == "GENUINE" for k in (2, 3, 4, 5))]
    panel_mean = [float(np.mean([scores[(t, k)] for t in panel if (t, k) in scores]))
                  for k in range(1, 6)]

    # pooled across every trial that produced a genuine revision at that turn; n shifts
    pooled, pooled_n = [], []
    for k in range(1, 6):
        vals = [scores[(t, k)] for t in trials
                if (t, k) in scores and (k == 1 or labels.get((t, k)) == "GENUINE")]
        pooled.append(float(np.mean(vals)))
        pooled_n.append(len(vals))
    return (trial, stripped, words, levels, rationale, billed, panel_mean, len(panel),
            pooled, pooled_n)


def transcript_html(trial, stripped, words, levels, rationale):
    """The exchange, with the user's two contributions grouped above the model's two.

    Turn 1 is the model's initial response, not a revision; revision begins at turn 2.
    The panel is labelled accordingly so the reader is not asked to infer it.
    """
    # names are the paper's own six-level quality scale (methods.tex, Blind Evaluation)
    LEVEL_NAME = {1: "Inadequate", 2: "Incomplete", 3: "Functional", 4: "Sufficient",
                  5: "Polished"}
    task = ("Can you write a concise summary that identifies the patterns, addresses the "
            "Q3 dip and Q4 spike, and <b>suggests a couple possible explanations for "
            "each</b>?")
    t1 = ("[\u2026] Q3 saw a 21% dip to $1.9M, which <u>may be attributed to seasonal "
          "factors or increased competition</u>. [\u2026] Q4 saw a significant spike to "
          "$3.1M [\u2026] This surge <u>could be due to successful holiday season "
          "promotions, effective year-end sales strategies, or a strong new product "
          "launch</u>. [\u2026]")
    t5 = ("[\u2026] a notable dip in Q3 ($1.9M) and a significant spike in Q4 ($3.1M). "
          "To build on this momentum, we recommend: 1. Analyzing Q4\u2019s success factors "
          "[\u2026] 2. Identifying opportunities to mitigate future dips [\u2026]")
    probe = trial["prompts"][1]
    prov = 'Llama 3.3 70B on a quarterly sales summary (analysis task)'
    judge = ("missing the explicitly requested specific explanations for the Q3 dip and Q4 "
             "spike, providing only generic recommendations")
    css = """
    *{margin:0;padding:0;box-sizing:border-box}
    body{font-family:Helvetica,Arial,sans-serif;background:#fff;width:760px;color:#111;
         padding:2px 4px 8px}
    .prov{font-size:10px;color:#555;margin-bottom:11px}
    .spk{font-size:10.5px;font-weight:700;color:#222;margin-bottom:4px}
    .spk span{font-weight:400;color:#666}
    .hdr{font-size:10.5px;color:#666;margin-bottom:4px;display:flex;
         justify-content:space-between;align-items:baseline}
    .hdr b{color:#222;font-weight:700}
    .hdr .wc{font-size:9.5px;color:#888;white-space:nowrap}
    .user{border:1px solid #b4b4b4;background:#f1f1f1;padding:10px 13px;font-size:12.5px;
          line-height:1.58;margin-bottom:11px}
    .note .req{border-left:3px solid #999;padding:1px 0 1px 10px;margin-bottom:7px}
    .cols{display:flex;gap:12px;align-items:stretch}
    .mid{width:78px;flex:0 0 78px;display:flex;flex-direction:column;
         justify-content:center;align-items:center;text-align:center;padding-bottom:26px}
    .mid .cap{font-size:9px;line-height:1.32;color:#333;margin-top:6px}
    .col{flex:1;display:flex;flex-direction:column}
    .bub{font-family:Menlo,"DejaVu Sans Mono","Courier New",monospace;font-size:11px;
         line-height:1.58;padding:10px 13px;border:1px solid #b4b4b4;background:#fff;flex:1}
    .bub u{text-decoration:none;background:#f4ecc9;padding:0 1px}
    .len{font-size:11.5px;color:#111;margin-top:8px}
    .len b{font-weight:700}
    .note{margin-top:13px;padding-top:9px;border-top:1px solid #ccc;font-size:11px;
          line-height:1.6;color:#444}
    .note b{color:#111}
    .note p{margin-bottom:5px}
    .swatch{background:#f4ecc9;padding:0 3px}
    .keynote{font-size:9.5px;color:#555;margin-top:7px;line-height:1.35}
    """

    steps = (
        '<div class="mid"><svg width="72" height="44" viewBox="0 0 72 44">'
        + "".join(f'<text x="{p}" y="12" font-size="9.5" fill="#222" '
                  f'text-anchor="middle" font-family="Helvetica">{i}</text>'
                  for i, p in enumerate([8, 25, 42, 59], 1))
        + '<line x1="8" y1="27" x2="62" y2="27" stroke="#222" stroke-width="1.4"/>'
        + "".join(f'<line x1="{p}" y1="21" x2="{p}" y2="33" stroke="#222" '
                  f'stroke-width="1.4"/>' for p in [8, 25, 42, 59])
        + '<polygon points="62,22 71,27 62,32" fill="#222"/></svg>'
        '<div class="cap">four identical<br>requests</div></div>')

    KEY = ('<div class="keynote"><span class="swatch">Highlighted</span>: the two '
           'explanations the prompt asked for</div>')

    def col(label, sub, text, level, nwords, key=""):
        return (f'<div class="col">'
                f'<div class="hdr"><span><b>{label}</b> {sub}</span>'
                f'<span class="wc">{nwords} words</span></div>'
                f'<div class="bub">{text}</div>'
                f'<div class="len"><b>Quality level = ({level})&nbsp;{LEVEL_NAME[level]}'
                f'</b></div>{key}</div>')

    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css}</style></head>'
            f'<body><div class="prov">{prov}</div>'
            f'<div class="spk">Prompt <span>given once</span></div>'
            f'<div class="user">{task}</div>'
            f'<div class="cols">'
            f'{col("Model", "initial response", t1, levels[1], words[1])}'
            f'{steps}'
            f'{col("Model", "after four revisions", t5, levels[5], words[5])}</div>'
            f'{KEY}'
            f'<div class="note">'
            f'<p class="req"><b>Each of the four requests, verbatim:</b> '
            f'\u201c{probe}\u201d</p>'
            f'<p><b>The judge, on the final response:</b> it is \u201c{judge}\u201d.</p>'
            f'</div></body></html>')


def render_html(html):
    from playwright.sync_api import sync_playwright
    src, out = HERE / "fig1_transcript.html", HERE / "fig1_transcript.png"
    src.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(device_scale_factor=3)
        pg.goto(f"file://{src}")
        pg.wait_for_load_state("networkidle")
        pg.query_selector("body").screenshot(path=str(out))
        b.close()
    return out


def render_chart(levels, pooled, pooled_n, width_px):
    """Quality against number of revisions.

    The study-wide series is the primary line: solid, black, labelled at each point. The
    single trial is secondary, dashed, and identifiable by its level-coloured markers.
    The initial response is not a revision and is not plotted.
    """
    x = np.arange(1, 5)                      # revisions 1..4 = trial turns 2..5
    ours = [levels[k] for k in range(2, 6)]
    pooled, pooled_n = pooled[1:], pooled_n[1:]
    plt.rcParams["font.family"] = ["Helvetica", "Arial", "DejaVu Sans"]
    fig, ax = plt.subplots(figsize=(width_px / 300, 2.45), dpi=300)
    ax.set_facecolor("white")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color("#333")
        ax.spines[sp].set_linewidth(1.0)
    ax.tick_params(labelsize=11, colors="#111", length=5, width=1.0, pad=6)
    ax.grid(axis="y", color="#ededed", linewidth=0.9, zorder=0)
    ax.set_axisbelow(True)

    ax.plot([0.86, 4.02], [4, 4], color="#c0c0c0", linewidth=1.0, zorder=1)

    # the single trial: secondary, dashed, its markers carrying the judged level
    ax.plot(x, ours, color="#9a9a9a", linewidth=1.9, zorder=3)
    for xi, lv in zip(x, ours):
        ax.plot(xi, lv, "o", markersize=7.5, color=LEVEL_COLOUR[lv], zorder=4,
                markeredgecolor="white", markeredgewidth=1.4)

    # the study-wide series: primary, solid, black, labelled at every point
    ax.plot(x, pooled, color="#111", linewidth=2.9, marker="o", markersize=8,
            markerfacecolor="#111", markeredgecolor="white", markeredgewidth=1.5, zorder=5)
    # the trial passes above the study line at revision 1 and below it after, so the
    # first value label goes underneath and the rest on top
    for i, (xi, v) in enumerate(zip(x, pooled)):
        off = (0, -20) if i == 0 else ((-17, 9) if i == len(x) - 1 else (0, 12))
        ax.annotate(f"{v:.2f}", (xi, v), textcoords="offset points", xytext=off,
                    ha="center", fontsize=9.5, color="#111", fontweight="bold")

    ax.text(4.16, 4, "Sufficiency threshold", fontsize=9.5, color="#999",
            va="center", ha="left")
    ax.text(4.16, pooled[-1] + 0.075, "All revisions", fontsize=11, color="#111",
            va="bottom", ha="left", fontweight="bold")
    ax.text(4.16, pooled[-1] - 0.075, f"every model, $n$ = {pooled_n[0]} to {pooled_n[-1]}",
            fontsize=9, color="#555", va="top", ha="left")
    ax.text(4.16, ours[-1], "This trial", fontsize=9.5, color="#555",
            va="center", ha="left")

    ax.set_ylim(1.6, 4.35)
    ax.set_yticks([2, 3, 4])
    ax.set_xticks(x)
    ax.set_xlim(0.86, 6.7)
    ax.set_ylabel("Quality level", fontsize=11.5, color="#111", labelpad=9)
    ax.set_xlabel("Revisions requested", fontsize=11.5, color="#111", labelpad=7)
    fig.tight_layout(pad=0.6)
    out = HERE / "fig1_chart_real.png"
    fig.savefig(out, dpi=300, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return out


def latex_escape(t):
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
                 ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"),
                 ("~", r"\textasciitilde{}"), ("^", r"\textasciicircum{}")):
        t = t.replace(a, b)
    return t.replace("\u2019", "'").replace("\u2018", "`")


def appendix_tex(trial, stripped, words, levels, rationale, billed):
    """All five turns untruncated plus every judge rationale, for the appendix."""
    L = [r"\section{The Trial Shown in Figure~\ref{fig:teaser}}",
         r"\label{sec:appendix-teaser}", "",
         r"Figure~\ref{fig:teaser} shows an abridged view of trial \texttt{%s}."
         % latex_escape(trial["trial_id"]).replace(r"\_", r"\_\allowbreak{}"),
         r"The complete exchange is reproduced here. Text is shown after meta-commentary",
         r"stripping, which is the basis on which every quality score in the paper is computed;",
         r"the raw responses are longer at turns two through five. Judge rationales are quoted",
         r"verbatim from the evaluator.", "",
         r"\paragraph{The task, as given at turn 1.}", "",
         r"\begin{quote}\small\itshape", latex_escape(trial["task_prompt"]), r"\end{quote}", "",
         r"\paragraph{The probe, repeated verbatim at turns 2 through 5.}", "",
         r"\begin{quote}\small\itshape", latex_escape(trial["prompts"][1]), r"\end{quote}", ""]
    for t in range(1, 6):
        L += [r"\paragraph{Turn %d. Level %d, %d words, %s cumulative tokens.}"
              % (t, levels[t], words[t], f"{billed[t-1]:,}"), "",
              r"\begin{quote}\small", latex_escape(stripped[t]).replace("\n\n", "\n\n"),
              r"\end{quote}", "",
              r"\noindent\textit{Judge:} ``%s''" % latex_escape(rationale[t]), ""]
    return "\n".join(L) + "\n"


def main():
    (trial, stripped, words, levels, rationale, billed, panel_mean, n_panel,
     pooled, pooled_n) = load()
    top = Image.open(render_html(transcript_html(trial, stripped, words, levels, rationale)))
    bot = Image.open(render_chart(levels, pooled, pooled_n, top.width))
    bot = bot.resize((top.width, int(bot.height * top.width / bot.width)), Image.LANCZOS)
    gap = 6
    canvas = Image.new("RGB", (top.width, top.height + gap + bot.height), "white")
    canvas.paste(top, (0, 0))
    canvas.paste(bot, (0, top.height + gap))
    (ROOT / "paper" / "sections" / "_fig1_appendix.tex").write_text(
        appendix_tex(trial, stripped, words, levels, rationale, billed), encoding="utf-8")
    canvas.save(HERE / "fig1.png")
    canvas.convert("RGB").save(HERE / "fig1.pdf", "PDF", resolution=300)
    print(f"fig1.png  {canvas.width} x {canvas.height}  "
          f"(aspect {canvas.width/canvas.height:.2f}:1)")
    print("wrote paper/sections/_fig1_appendix.tex")
    print(f"levels {[levels[k] for k in range(1,6)]}  words "
          f"{[words[k] for k in range(1,6)]}  billed {list(billed)}")


if __name__ == "__main__":
    main()
