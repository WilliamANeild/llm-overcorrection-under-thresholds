#!/usr/bin/env python3
"""Generate emami_update.excalidraw -- advisor update diagram."""

import json, random

random.seed(42)

elements = []
_id_counter = 0

def uid():
    global _id_counter
    _id_counter += 1
    return f"el_{_id_counter:04d}"

def seed():
    return random.randint(1, 2**31)

def rect(x, y, w, h, bg="#a5d8ff", stroke="#1e1e1e", sw=2, radius=True, opacity=100):
    eid = uid()
    elements.append({
        "id": eid, "type": "rectangle",
        "x": x, "y": y, "width": w, "height": h, "angle": 0,
        "strokeColor": stroke, "backgroundColor": bg,
        "fillStyle": "solid", "strokeWidth": sw, "roughness": 0,
        "opacity": opacity, "groupIds": [], "frameId": None,
        "roundness": {"type": 3} if radius else None,
        "seed": seed(), "version": 1, "versionNonce": seed(),
        "isDeleted": False, "boundElements": None,
        "updated": 1718000000000, "link": None, "locked": False,
    })
    return eid

def text(x, y, txt, size=16, family=1, color="#1e1e1e", align="left", w=None):
    eid = uid()
    lines = txt.split("\n")
    if family == 3:
        cw = size * 0.62
    else:
        cw = size * 0.65
    est_w = w if w else max(len(l) for l in lines) * cw + 10
    est_h = len(lines) * size * 1.35
    elements.append({
        "id": eid, "type": "text",
        "x": x, "y": y, "width": est_w, "height": est_h, "angle": 0,
        "strokeColor": color, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": 1, "roughness": 0,
        "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": None,
        "seed": seed(), "version": 1, "versionNonce": seed(),
        "isDeleted": False, "boundElements": None,
        "updated": 1718000000000, "link": None, "locked": False,
        "text": txt, "fontSize": size, "fontFamily": family,
        "textAlign": align, "verticalAlign": "top",
        "containerId": None, "originalText": txt,
        "autoResize": True, "lineHeight": 1.25,
    })
    return eid

def arrow(x1, y1, x2, y2, color="#1e1e1e", sw=2):
    eid = uid()
    dx = x2 - x1
    dy = y2 - y1
    elements.append({
        "id": eid, "type": "arrow",
        "x": x1, "y": y1, "width": abs(dx), "height": abs(dy), "angle": 0,
        "strokeColor": color, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": sw, "roughness": 0,
        "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": {"type": 2},
        "seed": seed(), "version": 1, "versionNonce": seed(),
        "isDeleted": False, "boundElements": None,
        "updated": 1718000000000, "link": None, "locked": False,
        "points": [[0, 0], [dx, dy]],
        "lastCommittedPoint": None,
        "startBinding": None, "endBinding": None,
        "startArrowhead": None, "endArrowhead": "arrow",
    })
    return eid

def line(x1, y1, x2, y2, color="#868e96", sw=2, dash=False):
    eid = uid()
    dx = x2 - x1
    dy = y2 - y1
    el = {
        "id": eid, "type": "line",
        "x": x1, "y": y1, "width": abs(dx), "height": abs(dy), "angle": 0,
        "strokeColor": color, "backgroundColor": "transparent",
        "fillStyle": "solid", "strokeWidth": sw, "roughness": 0,
        "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": {"type": 2},
        "seed": seed(), "version": 1, "versionNonce": seed(),
        "isDeleted": False, "boundElements": None,
        "updated": 1718000000000, "link": None, "locked": False,
        "points": [[0, 0], [dx, dy]],
        "lastCommittedPoint": None,
        "startBinding": None, "endBinding": None,
        "startArrowhead": None, "endArrowhead": None,
    }
    if dash:
        el["strokeStyle"] = "dashed"
    elements.append(el)
    return eid

# ===============================================
# COLORS
# ===============================================
C_BLUE     = "#a5d8ff"
C_RED      = "#ffc9c9"
C_GREEN    = "#b2f2bb"
C_PURPLE   = "#d0bfff"
C_YELLOW   = "#ffec99"
C_TAN      = "#e9c6af"
C_LAVENDER = "#c5b4e3"
C_ORANGE   = "#ffd8a8"
C_PINK     = "#fcc2d7"
C_DKBLUE   = "#339af0"
C_DKRED    = "#e03131"
C_DKGREEN  = "#2f9e44"

# ===============================================
# LAYOUT
# ===============================================
BW = 420        # phase box width
BG = 50         # gap between boxes
PAD = 22        # text padding inside boxes
TPAD = 16       # top padding

CANVAS_W = 4 * BW + 3 * BG + 40  # ~1870

# ===============================================
# HEADER (top)
# ===============================================
rect(20, 20, 460, 55, bg=C_PINK, sw=3)
text(38, 30, "LLM Overcorrection Under Revision", size=22, w=440)

text(25, 95, "720 trials across 6 models, 40 tasks, 5 turns", size=14, color="#495057", w=500)
text(25, 118, "Blind LLM-judge evaluation + human annotation", size=14, color="#868e96", w=500)

# Two sentences box
ts_x = 530
rect(ts_x, 20, 560, 120, bg="#fff3bf", sw=2)
text(ts_x + PAD, 30, "MY TWO SENTENCES", size=15, color="#e67700", w=520)
text(ts_x + PAD, 56, (
    "LLMs don't know when to stop revising. Left unchecked,\n"
    "they degrade their own output, and that is a massive\n"
    "problem for any multi-turn workflow."
), size=14, color="#495057", w=520)

# Finding vs methods
fvm_x = ts_x + 580
rect(fvm_x, 20, 520, 120, bg="#d3f9d8", sw=2)
text(fvm_x + PAD, 30, "FINDING vs METHODS", size=15, color=C_DKGREEN, w=480)
text(fvm_x + PAD, 56, (
    "FINDING: Quality degrades when models revise\n"
    "without direction. This is the core problem.\n"
    "METHODS: Meta-commentary was a measurement\n"
    "challenge we solved. Not the headline."
), size=13, color="#495057", w=480)

# ===============================================
# ROW 1: PHASES 0-3
# ===============================================
R1_Y = 160
R1_H = 370

p0x = 20
p1x = p0x + BW + BG
p2x = p1x + BW + BG
p3x = p2x + BW + BG

# -- helper: commentary vs stat text --
TW = BW - 2*PAD  # text width inside boxes

def commentary(x, y, txt):
    """Lighter hand-drawn text for interpretation."""
    return text(x, y, txt, size=13, family=1, color="#495057", w=TW)

def stat(x, y, txt):
    """Darker monospace text for numbers/stats."""
    return text(x, y, txt, size=12, family=3, color="#1e1e1e", w=TW)

# ---- PHASE 0: Judge Calibration ----
rect(p0x, R1_Y, BW, R1_H, bg=C_BLUE, sw=2)
text(p0x + PAD, R1_Y + TPAD, "PHASE 0: Judge Calibration", size=18, color="#1864ab", w=TW)

commentary(p0x + PAD, R1_Y + 50,
    "We needed a reliable automated judge\n"
    "before running 720 trials. Tested 6\n"
    "LLM judges against 3 human raters.")

stat(p0x + PAD, R1_Y + 115,
    "Winner: Claude Sonnet 4\n"
    "Judge-human kappa: 0.526\n"
    "Spearman r: 0.505")

commentary(p0x + PAD, R1_Y + 175,
    "Human raters themselves only agreed\n"
    "at similar levels, so the judge is\n"
    "roughly as reliable as a human.")

stat(p0x + PAD, R1_Y + 240,
    "Human kappa: 0.41-0.60\n"
    "Krippendorff alpha: 0.529")

rect(p0x + PAD, R1_Y + R1_H - 52, BW - 2*PAD, 40, bg="#d0ebff", sw=1)
text(p0x + PAD + 10, R1_Y + R1_H - 44, "Locked one judge. Agreement is\nmoderate but adequate.", size=12, color="#1864ab", w=TW - 20)

# ---- PHASE 1: Working Conversations ----
rect(p1x, R1_Y, BW, R1_H, bg=C_RED, sw=2)
text(p1x + PAD, R1_Y + TPAD, "PHASE 1: Working Conversations", size=18, color="#c92a2a", w=TW)

commentary(p1x + PAD, R1_Y + 50,
    "The core experiment. Each model gets\n"
    "5 turns of undirected \"keep improving\"\n"
    "prompts on real tasks across 5 domains.")

stat(p1x + PAD, R1_Y + 115,
    "720 trials (6 models x 40 tasks x 3)\n"
    "Domains: writing, code, analysis,\n"
    "  creative, data/logic")

commentary(p1x + PAD, R1_Y + 175,
    "Models tested: Claude Sonnet 4,\n"
    "GPT-4o, Gemini 2.5 Flash,\n"
    "Llama 3.3 70B, DeepSeek V4,\n"
    "Qwen 3 235B.")

commentary(p1x + PAD, R1_Y + 260,
    "The probe is undirected: no specific\n"
    "critique, just \"keep improving.\"")

rect(p1x + PAD, R1_Y + R1_H - 52, BW - 2*PAD, 40, bg="#ffe3e3", sw=1)
text(p1x + PAD + 10, R1_Y + R1_H - 44, "75% of post-T1 responses are meta.\nOnly 13% still revising at T5.", size=12, color="#c92a2a", w=TW - 20)

# ---- PHASE 2: Blind Evaluation ----
rect(p2x, R1_Y, BW, R1_H, bg=C_GREEN, sw=2)
text(p2x + PAD, R1_Y + TPAD, "PHASE 2: Blind Evaluation", size=18, color="#2b8a3e", w=TW)

commentary(p2x + PAD, R1_Y + 50,
    "Every response scored on a 6-level\n"
    "rubric. Level 6 (\"overdone\") broke\n"
    "the scale, so we recoded it to 2.")

commentary(p2x + PAD, R1_Y + 115,
    "This killed a major artifact where\n"
    "Llama looked like it improved:")

stat(p2x + PAD, R1_Y + 160,
    "Before recode: Llama +1.02\n"
    "After recode:  Llama -0.82")

commentary(p2x + PAD, R1_Y + 210,
    "Most first drafts were already good\n"
    "enough without any revision:")

stat(p2x + PAD, R1_Y + 255,
    "T1 sufficiency: 87.6% (631/720)")

rect(p2x + PAD, R1_Y + R1_H - 52, BW - 2*PAD, 40, bg="#d3f9d8", sw=1)
text(p2x + PAD + 10, R1_Y + R1_H - 44, "After the fix, all models degrade.\nBest turn is T1 for every model.", size=12, color="#2b8a3e", w=TW - 20)

# ---- PHASE 3: One-Shot Ceiling ----
P3_H = 230
rect(p3x, R1_Y, BW, P3_H, bg=C_PURPLE, sw=2)
text(p3x + PAD, R1_Y + TPAD, "PHASE 3: One-Shot Ceiling", size=18, color="#5f3dc4", w=TW)

commentary(p3x + PAD, R1_Y + 50,
    "Do first drafts even need revision?\n"
    "Mostly no.")

stat(p3x + PAD, R1_Y + 100,
    "87.6% of T1 responses meet or\n"
    "exceed the quality bar (631/720)")

commentary(p3x + PAD, R1_Y + 150,
    "The vast majority of revision in\n"
    "Phase 1 is unnecessary from\n"
    "the start.")

# Arrows row 1
ay = R1_Y + R1_H // 2
arrow(p0x + BW, ay, p1x, ay, color=C_DKBLUE, sw=3)
arrow(p1x + BW, ay, p2x, ay, color=C_DKRED, sw=3)
arrow(p2x + BW, ay, p3x, ay, color=C_DKGREEN, sw=3)

# ===============================================
# CLASSIFIER BOX (between rows)
# ===============================================
cl_x = p1x
cl_y = R1_Y + R1_H + 25
cl_w = BW * 2 + BG
rect(cl_x, cl_y, cl_w, 130, bg=C_ORANGE, sw=2)
text(cl_x + PAD, cl_y + TPAD, "GENUINE/META Classifier", size=16, color="#d9480f", w=cl_w - 2*PAD)
text(cl_x + PAD, cl_y + 44, (
    "Separates real revisions from meta-commentary.\n"
    "718 genuine vs 2,162 meta out of 2,880 post-T1 responses."
), size=13, color="#1e1e1e", w=cl_w - 2*PAD)
text(cl_x + PAD, cl_y + 85, (
    "Example meta: \"I think this is a good version but\n"
    "here is a slightly improved version...\""
), size=12, family=3, color="#868e96", w=cl_w - 2*PAD)

arrow(cl_x + cl_w // 2, cl_y, cl_x + cl_w // 2, R1_Y + R1_H, color="#d9480f", sw=2)

# ===============================================
# ROW 2: PHASES 4-6
# ===============================================
R2_Y = cl_y + 130 + 40
R2_H = 380

p4x = 20
p5x = p4x + BW + BG
p6x = p5x + BW + BG

# ---- PHASE 4: Reversibility ----
rect(p4x, R2_Y, BW, R2_H, bg=C_YELLOW, sw=2)
text(p4x + PAD, R2_Y + TPAD, "PHASE 4: Reversibility", size=18, color="#e67700", w=TW)
text(p4x + PAD, R2_Y + 42, "(measurement validation)", size=13, color="#868e96", w=TW)

commentary(p4x + PAD, R2_Y + 68,
    "Is the degradation real or a judge\n"
    "artifact? Blinded human raters\n"
    "compared T1 vs last revision.")

stat(p4x + PAD, R2_Y + 128,
    "56.2% prefer T1 (41/73 non-tie)\n"
    "Inter-rater kappa: 0.703")

commentary(p4x + PAD, R2_Y + 178,
    "The key insight: meta-commentary\n"
    "was inflating the judge's scores.")

stat(p4x + PAD, R2_Y + 228,
    "Judge unstripped: 91.8% T1-pref\n"
    "Judge stripped:   56.5% T1-pref\n"
    "Humans stripped:  56.2% T1-pref")

commentary(p4x + PAD, R2_Y + 285,
    "Stripping brings the judge in\n"
    "line with human raters.")

rect(p4x + PAD, R2_Y + R2_H - 52, BW - 2*PAD, 40, bg="#fff3bf", sw=1)
text(p4x + PAD + 10, R2_Y + R2_H - 44, "Meta-commentary inflates the judge.\nStripping solves it.", size=12, color="#e67700", w=TW - 20)

# ---- PHASE 5: Targeted Feedback ----
rect(p5x, R2_Y, BW, R2_H, bg=C_TAN, sw=2)
text(p5x + PAD, R2_Y + TPAD, "PHASE 5: Targeted Feedback", size=18, color="#862e0b", w=TW)
text(p5x + PAD, R2_Y + 42, "(the fix, not the headline)", size=13, color="#868e96", w=TW)

commentary(p5x + PAD, R2_Y + 68,
    "When you give specific critique\n"
    "instead of generic \"improve this,\"\n"
    "quality goes up instead of down.")

stat(p5x + PAD, R2_Y + 128,
    "Targeted: 4.68 vs Generic: 3.53\n"
    "Delta: +1.16 (p = 5.7e-19)\n"
    "n = 177 genuine trials")

commentary(p5x + PAD, R2_Y + 188,
    "Every model benefits. Direction\n"
    "is the missing ingredient.")

stat(p5x + PAD, R2_Y + 235,
    "Llama +1.62 | Qwen +1.48\n"
    "GPT-4o +1.33 | DeepSeek +1.05\n"
    "Claude +0.31")

commentary(p5x + PAD, R2_Y + 295,
    "Not more turns. Better turns.")

rect(p5x + PAD, R2_Y + R2_H - 52, BW - 2*PAD, 40, bg="#f4e2d1", sw=1)
text(p5x + PAD + 10, R2_Y + R2_H - 44, "All 5 powered models benefit.\nDirection recovers quality.", size=12, color="#862e0b", w=TW - 20)

# ---- PHASE 6: Self-Reflection ----
P6_H = 280
rect(p6x, R2_Y, BW, P6_H, bg=C_LAVENDER, sw=2)
text(p6x + PAD, R2_Y + TPAD, "PHASE 6: Self-Reflection", size=18, color="#5f3dc4", w=TW)

commentary(p6x + PAD, R2_Y + 50,
    "A fresh instance of each model\n"
    "reviews its own 5-turn trajectory\n"
    "and picks the best turn.")

stat(p6x + PAD, R2_Y + 115,
    "Mean recommended turn: 2.44\n"
    "40% recommend T1\n"
    "91% recommend not-T5")

commentary(p6x + PAD, R2_Y + 175,
    "Models know the first draft is best,\n"
    "but in-context they keep going\n"
    "anyway. They know better than\n"
    "they do.")

# Arrows row 2
ay2 = R2_Y + R2_H // 2
arrow(p4x + BW, ay2, p5x, ay2, color="#e67700", sw=3)
arrow(p5x + BW, ay2, p6x, ay2, color="#862e0b", sw=3)

# Arrow from row 1 down to row 2
arrow(p0x + BW // 2, R1_Y + R1_H, p4x + BW // 2, R2_Y, color="#5f3dc4", sw=2)

# ===============================================
# ZONE 2: THE THREE FINDINGS
# ===============================================
Z2_Y = R2_Y + R2_H + 60
Z2_X = 20

line(Z2_X, Z2_Y - 15, Z2_X + CANVAS_W, Z2_Y - 15, color="#adb5bd", sw=3, dash=True)

rect(Z2_X, Z2_Y, CANVAS_W, 55, bg="#dee2e6", sw=0)
text(Z2_X + PAD, Z2_Y + 14, "THE THREE FINDINGS", size=26, color="#495057", w=500)

# Main finding boxes: 3 across, sub-findings hang below each
TK_W = 480
TK_GAP = 40
TK_H = 200
tk_y = Z2_Y + 80
FW = TK_W - 2*PAD

# Sub-finding box dimensions
SB_W = 480
SB_H = 105
SB_GAP = 15
SB_YOFF = TK_H + 20  # below main box

f1x = Z2_X
f2x = Z2_X + TK_W + TK_GAP
f3x = f2x + TK_W + TK_GAP

# ---- Finding 1: Revision Makes It Worse ----
rect(f1x, tk_y, TK_W, TK_H, bg=C_RED, sw=3)
text(f1x + PAD, tk_y + TPAD, "1. REVISION MAKES IT WORSE", size=18, color="#c92a2a", w=FW)

commentary(f1x + PAD, tk_y + 50,
    "When you tell an LLM to \"keep improving\"\n"
    "without saying what to fix, quality goes\n"
    "down, not up.")

stat(f1x + PAD, tk_y + 120,
    "Cliff: -0.74 (p = 1e-4, n=50)\n"
    "Pooled: T1 4.11 -> T5 3.07")

# Sub-findings below Finding 1
s1y = tk_y + SB_YOFF
rect(f1x, s1y, SB_W, SB_H, bg="#ffe3e3", sw=1)
commentary(f1x + 14, s1y + 10,
    "Every domain degrades. Analysis drops\n"
    "the most, creative the least.")
stat(f1x + 14, s1y + 58,
    "Analysis -1.16 | Code -1.05\n"
    "Writing -1.06 | Creative -0.82")

rect(f1x, s1y + SB_H + SB_GAP, SB_W, SB_H, bg="#ffe3e3", sw=1)
commentary(f1x + 14, s1y + SB_H + SB_GAP + 10,
    "39% of the time, models revise work that\n"
    "was already good enough.")
stat(f1x + 14, s1y + SB_H + SB_GAP + 55,
    "Rev-despite-sufficient: 39.2% (CI 36-42%)")

arrow(f1x + TK_W // 2, tk_y + TK_H, f1x + TK_W // 2, s1y, color="#c92a2a", sw=2)

# ---- Finding 2: Most Models Just Stop ----
rect(f2x, tk_y, TK_W, TK_H, bg=C_BLUE, sw=3)
text(f2x + PAD, tk_y + TPAD, "2. MOST MODELS JUST STOP", size=18, color="#1864ab", w=FW)

commentary(f2x + PAD, tk_y + 50,
    "Three out of four post-T1 responses are\n"
    "not real revisions. They are polite\n"
    "declines or commentary, not edits.")

stat(f2x + PAD, tk_y + 120,
    "75% of post-T1 = meta-responses\n"
    "Genuine revision: 39% at T2 -> 13% at T5")

# Sub-findings below Finding 2
rect(f2x, s1y, SB_W, SB_H, bg="#d0ebff", sw=1)
commentary(f2x + 14, s1y + 10,
    "Models that stop sooner accidentally protect\n"
    "their output. Llama keeps going and degrades.")
stat(f2x + 14, s1y + 58,
    "T5 survival: Llama 53% | Claude 13%\n"
    "Gemini 1% | GPT-4o 3% | Qwen 5%")

rect(f2x, s1y + SB_H + SB_GAP, SB_W, SB_H, bg="#d0ebff", sw=1)
commentary(f2x + 14, s1y + SB_H + SB_GAP + 10,
    "Content drifts away from the original across\n"
    "turns. Declines are verbose and content-shaped.")
stat(f2x + 14, s1y + SB_H + SB_GAP + 55,
    "Overlap: T1 42% -> T5 29% (p < 1e-31)")

arrow(f2x + TK_W // 2, tk_y + TK_H, f2x + TK_W // 2, s1y, color="#1864ab", sw=2)

# ---- Finding 3: Tell Them What to Fix ----
rect(f3x, tk_y, TK_W, TK_H, bg=C_GREEN, sw=3)
text(f3x + PAD, tk_y + TPAD, "3. TELL THEM WHAT TO FIX", size=18, color="#2b8a3e", w=FW)

commentary(f3x + PAD, tk_y + 50,
    "Models are not bad at revision. They are\n"
    "bad at deciding what needs revision.\n"
    "Specific critique fixes it.")

stat(f3x + PAD, tk_y + 120,
    "Targeted: 4.68 vs Generic: 3.53\n"
    "Gap: +1.16 (p = 5.7e-19, n=177)")

# Sub-findings below Finding 3
rect(f3x, s1y, SB_W, SB_H, bg="#d3f9d8", sw=1)
commentary(f3x + 14, s1y + 10,
    "Every model benefits. The worse it does\n"
    "undirected, the more it gains from direction.")
stat(f3x + 14, s1y + 58,
    "Llama +1.62 | Qwen +1.48\n"
    "GPT-4o +1.33 | DeepSeek +1.05 | Claude +0.31")

rect(f3x, s1y + SB_H + SB_GAP, SB_W, SB_H, bg="#d3f9d8", sw=1)
commentary(f3x + 14, s1y + SB_H + SB_GAP + 10,
    "Models know T1 is best from a fresh context.\n"
    "In-context, they override that and keep going.")
stat(f3x + 14, s1y + SB_H + SB_GAP + 55,
    "40% recommend T1 | 91% say not T5")

arrow(f3x + TK_W // 2, tk_y + TK_H, f3x + TK_W // 2, s1y, color="#2b8a3e", sw=2)

# ---- Dropped/Corrected (bottom right) ----
drop_y = s1y + 2 * (SB_H + SB_GAP) + 20
drop_w = 3 * TK_W + 2 * TK_GAP
rect(Z2_X, drop_y, drop_w, 90, bg="#ffe3e3", sw=2)
text(Z2_X + PAD, drop_y + TPAD, "DROPPED / CORRECTED", size=16, color=C_DKRED, w=drop_w - 2*PAD)
commentary(Z2_X + PAD, drop_y + 42,
    "Akrasia framing dropped (reversibility 56%, near chance). "
    "Llama \"exception\" was an artifact (+1.02 became -0.82). "
    "\"Models can't stop\" was wrong (75% are declines). All old numbers superseded.")

# ===============================================
# ZONE 3: THE PAPER
# ===============================================
Z3_Y = drop_y + 90 + 60

line(Z2_X, Z3_Y - 15, Z2_X + CANVAS_W, Z3_Y - 15, color="#adb5bd", sw=3, dash=True)

rect(Z2_X, Z3_Y, CANVAS_W, 55, bg="#e9ecef", sw=0)
text(Z2_X + PAD, Z3_Y + 14, "THE PAPER: Structure, Figures, Next Steps", size=24, color="#495057", w=700)

ps_y = Z3_Y + 80

# Paper structure
ps_w = 520
rect(Z2_X, ps_y, ps_w, 260, bg=C_BLUE, sw=2)
text(Z2_X + PAD, ps_y + TPAD, "Paper Structure", size=18, color="#1864ab", w=ps_w - 2*PAD)
text(Z2_X + PAD, ps_y + 52, (
    "Results section leads with findings,\n"
    "not methods. Three main results:\n"
    "\n"
    "1. Revision behavior: models decline\n"
    "   rather than revise. 75% meta,\n"
    "   survival rates drop sharply.\n"
    "\n"
    "2. Quality degradation: cliff of -0.74\n"
    "   on clean content. Pooled -1.04.\n"
    "   All domains degrade. Tax is 62%.\n"
    "\n"
    "3. Targeted feedback recovers quality:\n"
    "   +1.16, universal across models."
), size=13, color="#1e1e1e", w=ps_w - 2*PAD)

# Methods note
rect(Z2_X, ps_y + 275, ps_w, 80, bg=C_YELLOW, sw=1)
text(Z2_X + PAD, ps_y + 285, "Methods handles measurement:", size=15, color="#e67700", w=ps_w - 2*PAD)
text(Z2_X + PAD, ps_y + 310, (
    "Meta-commentary stripping, human validation,\n"
    "6->2 recode. Not a finding, a solved challenge."
), size=12, family=3, color="#495057", w=ps_w - 2*PAD)

# ---- FIGURES (2x3 grid) ----
fig_x = Z2_X + ps_w + 40
fig_w = 260
fig_h = 110
fig_gap = 18

figs = [
    ("[FIG 1] Quality Cliff",       "Stripped pooled trajectory\nT1 (4.11) -> T5 (3.07)\nDashed line at Sufficient"),
    ("[FIG 2] Revision Rate Decay",  "Genuine revision rate by turn\n39.3% at T2 -> 13.3% at T5"),
    ("[FIG 3] Targeted Feedback",    "Dumbbell chart\nGeneric 3.53 vs Targeted 4.68\nGap = +1.16 stripped"),
    ("[FIG 4] Per-Model Survival",   "Survival curves by model\nLlama 53% to Gemini 1% at T5"),
    ("[FIG 5] Revision Tax",         "Horizontal bars\n62% wasted compute aggregate\nBest turn = T1 for all models"),
    ("[FIG 6] Domain Variation",     "Grouped bars across 5 domains\nAll degrade, -0.82 to -1.16"),
]

for i, (title, desc) in enumerate(figs):
    col = i % 2
    row = i // 2
    fx = fig_x + col * (fig_w + fig_gap)
    fy = ps_y + row * (fig_h + fig_gap)
    rect(fx, fy, fig_w, fig_h, bg="#e9ecef", sw=1)
    text(fx + 14, fy + 12, title, size=14, color="#495057", w=fig_w - 28)
    text(fx + 14, fy + 38, desc, size=12, family=3, color="#868e96", w=fig_w - 28)

# ---- NEXT STEPS ----
ns_x = fig_x + 2 * (fig_w + fig_gap) + 25
ns_w = 480
rect(ns_x, ps_y, ns_w, 375, bg=C_PINK, sw=2)
text(ns_x + PAD, ps_y + TPAD, "NEXT STEPS", size=20, color=C_DKRED, w=ns_w - 2*PAD)
text(ns_x + PAD, ps_y + 52, (
    "1. Results section drafted. Findings lead,\n"
    "   meta-commentary moved to methods.\n"
    "\n"
    "2. Regenerate all figures on the corrected\n"
    "   pipeline (6->2 recode, GENUINE filter,\n"
    "   stripped scores as primary).\n"
    "\n"
    "3. Update cost estimates to 2026 API pricing.\n"
    "\n"
    "4. NEED EMAMI'S READ:\n"
    "   - Does this framing work?\n"
    "   - Is the cliff strong enough?\n"
    "     (n=50, 90% from Llama)\n"
    "   - Is the decline phenomenon more\n"
    "     interesting than the quality cliff?\n"
    "\n"
    "5. Appendix: Studies 1 and 2 unchanged."
), size=13, color="#1e1e1e", w=ns_w - 2*PAD)

# ===============================================
# ZONE 4: REVISION-RATE DRIVERS (new analysis)
# ===============================================
Z4_Y = Z3_Y + 560  # below the paper section

line(Z2_X, Z4_Y - 15, Z2_X + CANVAS_W, Z4_Y - 15, color="#adb5bd", sw=3, dash=True)

C_TEAL = "#96f2d7"
C_DKTEAL = "#087f5b"

rect(Z2_X, Z4_Y, CANVAS_W, 55, bg=C_TEAL, sw=0)
text(Z2_X + PAD, Z4_Y + 12, "NEW: WHAT DRIVES REVISION RATE?", size=26, color=C_DKTEAL, w=700)

drv_y = Z4_Y + 80
DRV_W = 560
DRV_GAP = 40

# ---- 1. THE HIERARCHY (prominent) ----
hier_w = CANVAS_W
rect(Z2_X, drv_y, hier_w, 200, bg=C_TEAL, sw=3)
text(Z2_X + PAD, drv_y + TPAD, "THE HIERARCHY: How You Ask > Which Model > What Task", size=20, color=C_DKTEAL, w=hier_w - 2*PAD)

commentary(Z2_X + PAD, drv_y + 55,
    "Revision rate is driven overwhelmingly by how you phrase the prompt.\n"
    "Model identity matters next. Task type barely matters at all.")

# Visual: three bars
bar_x = Z2_X + PAD
bar_y = drv_y + 110
bar_max_w = hier_w - 300
# Probe phrasing: ~98pp
rect(bar_x, bar_y, int(bar_max_w * 0.98), 22, bg="#12b886", stroke="#087f5b", sw=2, radius=False)
text(bar_x + 10, bar_y + 2, "Probe phrasing: ~98pp range", size=13, color="#ffffff", w=400)
# Model identity: ~72pp
rect(bar_x, bar_y + 30, int(bar_max_w * 0.72), 22, bg="#38d9a9", stroke="#087f5b", sw=2, radius=False)
text(bar_x + 10, bar_y + 32, "Model identity: ~72pp range", size=13, color="#1e1e1e", w=400)
# Task type: 13.5pp
rect(bar_x, bar_y + 60, int(bar_max_w * 0.135), 22, bg="#96f2d7", stroke="#087f5b", sw=2, radius=False)
text(bar_x + int(bar_max_w * 0.135) + 10, bar_y + 62, "Task type: 13.5pp", size=13, color="#495057", w=200)

text(Z2_X + hier_w - 350, drv_y + 165, "Measured on 3 models: Claude, Gemini, GPT-4o", size=11, family=3, color="#868e96", w=340)

# ---- Row of 4 boxes below ----
row4_y = drv_y + 220
R4_W = 380
R4_GAP = 30
R4_H = 250

# ---- 2. PROBE IS A STEP FUNCTION ----
bx1 = Z2_X
rect(bx1, row4_y, R4_W, R4_H, bg="#c3fae8", sw=2)
text(bx1 + PAD, row4_y + TPAD, "Probe Is a Step Function", size=17, color=C_DKTEAL, w=R4_W - 2*PAD)

commentary(bx1 + PAD, row4_y + 48,
    "Revision rate is bimodal, not a\n"
    "gradient. There is no middle ground.")

stat(bx1 + PAD, row4_y + 100,
    "Change-requesting probes: ~100%\n"
    "Assessment-requesting:    2-39%\n"
    "Gap between clusters:     ~60pp")

commentary(bx1 + PAD, row4_y + 165,
    "The gate is semantic. If the prompt\n"
    "asks for change, models comply. If\n"
    "it asks for assessment, most decline.\n"
    "No probe lands in the middle.")

# ---- 3. CODE REVISES MORE ----
bx2 = bx1 + R4_W + R4_GAP
rect(bx2, row4_y, R4_W, R4_H, bg="#c3fae8", sw=2)
text(bx2 + PAD, row4_y + TPAD, "Code Revises More", size=17, color=C_DKTEAL, w=R4_W - 2*PAD)

commentary(bx2 + PAD, row4_y + 48,
    "Code tasks elicit more genuine revision\n"
    "than other domains, consistently across\n"
    "5 out of 6 models.")

stat(bx2 + PAD, row4_y + 110,
    "Code revision rate: 34%\n"
    "Other domains:      20-25%")

commentary(bx2 + PAD, row4_y + 160,
    "Why? Code has concrete targets: a\n"
    "failing test, a bug, a missing edge\n"
    "case. That built-in directed signal\n"
    "is the same thing targeted feedback\n"
    "provides. Code naturally has what\n"
    "other domains lack.")

# ---- 4. MODEL CLUSTERS ----
bx3 = bx2 + R4_W + R4_GAP
rect(bx3, row4_y, R4_W, R4_H, bg="#c3fae8", sw=2)
text(bx3 + PAD, row4_y + TPAD, "Three Model Clusters", size=17, color=C_DKTEAL, w=R4_W - 2*PAD)

commentary(bx3 + PAD, row4_y + 48,
    "Under change-probes, all models are\n"
    "identical (~100%). Under assessment-\n"
    "probes, they split into three clusters:")

stat(bx3 + PAD, row4_y + 115,
    "Gate-open:  Llama, Claude\n"
    "Gate-gated: GPT-4o, Qwen\n"
    "Gate-shut:  Gemini, DeepSeek")

commentary(bx3 + PAD, row4_y + 175,
    "The divergence is 0-90% on the\n"
    "evaluative side. Models differ in\n"
    "how they interpret ambiguity, not\n"
    "in whether they can revise.")

# ---- 5. MOMENTUM (small, model-specific) ----
bx4 = bx3 + R4_W + R4_GAP
mom_w = CANVAS_W - 3 * (R4_W + R4_GAP)
rect(bx4, row4_y, mom_w, R4_H - 50, bg="#e6fcf5", sw=1)
text(bx4 + PAD, row4_y + TPAD, "Momentum (model-specific)", size=15, color=C_DKTEAL, w=mom_w - 2*PAD)

commentary(bx4 + PAD, row4_y + 45,
    "One prior \"improve this?\" round\n"
    "flips GPT-4o from 31% to 98%\n"
    "on a later neutral probe.")

stat(bx4 + PAD, row4_y + 110,
    "GPT-4o: 31% -> 98%")

commentary(bx4 + PAD, row4_y + 140,
    "Claude and Gemini are largely\n"
    "unmoved. This is model-specific,\n"
    "not a general phenomenon.")

# Arrow from findings section down to drivers
arrow(Z2_X + CANVAS_W // 2, drop_y + 90, Z2_X + CANVAS_W // 2, Z4_Y, color=C_DKTEAL, sw=2)

# ===============================================
# WRITE
# ===============================================
doc = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "gridSize": None,
        "viewBackgroundColor": "#ffffff",
    },
    "files": {},
}

out = "emami_update.excalidraw"
with open(out, "w") as f:
    json.dump(doc, f, indent=2)

print(f"Wrote {out} with {len(elements)} elements")
