#!/usr/bin/env python3
"""Classify all 2,880 candidate rows as GENUINE or META using the sharpened LLM classifier.
Run: python3 scripts/study3/run_full_classification.py
"""

import json, os, sys, time, random
from pathlib import Path
from collections import defaultdict

from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

import anthropic

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"
CANDIDATES = DATA_DIR / "candidate_finals_for_classification.jsonl"
OUTPUT = DATA_DIR / "genuine_meta_labels.jsonl"
TRIALS = DATA_DIR / "worker_trials.jsonl"

SYSTEM_PROMPT = """You are a binary classifier. You will be shown a task prompt and a model's response to that task. Classify the response as GENUINE or META.

CRITICAL: The opening sentence does NOT determine the label. Models often begin with a decline or "I'll keep this as final" and THEN reproduce the full content in the body. Read the ENTIRE response. If the body contains the actual task content (a full function, a full paragraph, a full list, code blocks, the rewritten text), label GENUINE regardless of how it opens. Only label META if, after reading the whole response, there is NO self-contained task content present -- only commentary, description, praise, or an offer to revise.

GENUINE: The response body contains self-contained task content -- the actual revised text, code, paragraph, list, or other deliverable. The content must be PRESENT in the response, not merely described or referenced. A response that says "I'll keep this as final" but then REPRODUCES the full content in the body is GENUINE. Ask: could a user copy task-ready content out of this response? If yes, GENUINE.

META: The response only TALKS ABOUT the work, declines to revise, says it will keep a prior version, praises or summarizes a previous answer, or offers revision options without producing content. This applies EVEN IF the response is long, confident, or uses technical language. Describing or recapping what the content does, listing its features, or explaining why it is good -- without including the actual content itself -- is META. A response that says "the code handles X, Y, Z" without including the code is META. Ask: could a user only copy talk-about-the-work from this response? If yes, META.

Key test: if you removed all meta-commentary from the response, would there be a complete, self-contained piece of task content left (code, a written paragraph, an analysis, etc.) that someone could use? If yes: GENUINE. If no: META.

Reply with exactly one line:
GENUINE: <one-line reason>
or
META: <one-line reason>"""


def classify_revision_keyword(response):
    if not response or len(response.strip()) < 5:
        return False
    strong_decline = [
        "keep this as my final", "this is my final version",
        "i'd like to keep this", "i would like to keep this",
        "keep this as the final", "i'll keep this", "i will keep this",
        "happy with this version", "this version is ready",
        "no changes needed", "no improvements needed",
        "no further changes", "no further improvements",
        "no revisions needed", "nothing to improve",
        "nothing i would change", "i wouldn't change",
        "i don't think any changes", "don't see any need",
    ]
    weak_decline = [
        "looks good as is", "looks good as-is", "looks good",
        "already well", "already good", "ready to use",
        "ready as is", "ready as-is", "satisfied with",
        "meets the requirements", "the output is complete",
        "this is complete", "complete as is", "is ready",
        "is done", "i agree", "well done", "no need",
        "i think it's good", "i think this is good",
        "i think it looks good", "no, i think",
        "i'm satisfied", "final version", "no changes",
    ]
    head = response[:300].lower()
    for phrase in strong_decline:
        if phrase in head:
            return False
    if len(response) < 500:
        response_lower = response.lower()
        for phrase in weak_decline:
            if phrase in response_lower:
                return False
    return True


def classify_with_llm(client, task_prompt, response_text):
    truncated = response_text[:1500]
    if len(response_text) > 1500:
        truncated += f"\n[... truncated, total {len(response_text)} chars]"

    user_msg = f"TASK PROMPT:\n{task_prompt}\n\nMODEL RESPONSE:\n{truncated}"

    for attempt in range(3):
        try:
            resp = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=150,
                temperature=0,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_msg}],
            )
            answer = resp.content[0].text.strip()

            if answer.upper().startswith("GENUINE"):
                label = "GENUINE"
                reason = answer.split(":", 1)[1].strip() if ":" in answer else answer
            elif answer.upper().startswith("META"):
                label = "META"
                reason = answer.split(":", 1)[1].strip() if ":" in answer else answer
            else:
                label = "UNKNOWN"
                reason = answer

            return label, reason
        except Exception as e:
            if attempt < 2:
                wait = 2 ** (attempt + 1)
                print(f"    Retry {attempt+1} after error: {e} (waiting {wait}s)")
                time.sleep(wait)
            else:
                return "ERROR", str(e)


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: Set ANTHROPIC_API_KEY in .env")
        sys.exit(1)

    client = anthropic.Anthropic()

    # Load candidates
    with open(CANDIDATES) as f:
        rows = [json.loads(l) for l in f]
    print(f"Loaded {len(rows)} candidates")

    # Load task prompts
    trial_map = {}
    with open(TRIALS) as f:
        for line in f:
            t = json.loads(line)
            trial_map[t["trial_id"]] = t

    # Check for existing progress (resume support)
    done = {}
    if OUTPUT.exists():
        with open(OUTPUT) as f:
            for line in f:
                r = json.loads(line)
                done[(r["trial_id"], r["turn"])] = r
        print(f"Resuming: {len(done)} already classified")

    # Classify
    total = len(rows)
    with open(OUTPUT, "a") as out_f:
        for i, row in enumerate(rows):
            key = (row["trial_id"], row["turn"])
            if key in done:
                continue

            trial = trial_map.get(row["trial_id"])
            task_prompt = trial["task_prompt"] if trial else "(not found)"
            keyword_label = "REVISION" if classify_revision_keyword(row["text"]) else "META"

            label, reason = classify_with_llm(client, task_prompt, row["text"])

            result = {
                "trial_id": row["trial_id"],
                "model": row["model"],
                "domain": row["domain"],
                "turn": row["turn"],
                "classifier_label": label,
                "reason": reason,
                "keyword_label": keyword_label,
            }
            out_f.write(json.dumps(result) + "\n")
            out_f.flush()
            done[key] = result

            classified = len(done)
            if classified % 50 == 0 or classified == total:
                print(f"  [{classified}/{total}] last: {row['model']} T{row['turn']} -> {label}")

    print(f"\nDone. {len(done)} rows classified -> {OUTPUT}")

    # ── Reports ────────────────────────────────────────────────────────────
    with open(OUTPUT) as f:
        results = [json.loads(l) for l in f]

    # 1. Overall counts
    print("\n" + "=" * 80)
    print("REPORT 1: OVERALL COUNTS")
    print("=" * 80)

    genuine = sum(1 for r in results if r["classifier_label"] == "GENUINE")
    meta = sum(1 for r in results if r["classifier_label"] == "META")
    other = sum(1 for r in results if r["classifier_label"] not in ("GENUINE", "META"))
    print(f"\n  Total: {len(results)}")
    print(f"  GENUINE: {genuine} ({genuine/len(results)*100:.1f}%)")
    print(f"  META:    {meta} ({meta/len(results)*100:.1f}%)")
    if other:
        print(f"  OTHER:   {other}")

    print("\n  By turn:")
    for t in [2, 3, 4, 5]:
        t_rows = [r for r in results if r["turn"] == t]
        t_gen = sum(1 for r in t_rows if r["classifier_label"] == "GENUINE")
        t_meta = sum(1 for r in t_rows if r["classifier_label"] == "META")
        print(f"    T{t}: {len(t_rows)} total | GENUINE {t_gen} ({t_gen/len(t_rows)*100:.1f}%) | META {t_meta} ({t_meta/len(t_rows)*100:.1f}%)")

    print("\n  By model:")
    models = sorted(set(r["model"] for r in results))
    for m in models:
        m_rows = [r for r in results if r["model"] == m]
        m_gen = sum(1 for r in m_rows if r["classifier_label"] == "GENUINE")
        m_meta = sum(1 for r in m_rows if r["classifier_label"] == "META")
        print(f"    {m:<20} | GENUINE {m_gen:>3} ({m_gen/len(m_rows)*100:.1f}%) | META {m_meta:>3} ({m_meta/len(m_rows)*100:.1f}%)")

    # 2. Disagreements with keyword classifier
    print("\n" + "=" * 80)
    print("REPORT 2: DISAGREEMENTS WITH KEYWORD CLASSIFIER")
    print("=" * 80)

    disagree = [r for r in results if (
        (r["keyword_label"] == "REVISION" and r["classifier_label"] == "META") or
        (r["keyword_label"] == "META" and r["classifier_label"] == "GENUINE")
    )]
    kw_rev_new_meta = [r for r in disagree if r["keyword_label"] == "REVISION" and r["classifier_label"] == "META"]
    kw_meta_new_gen = [r for r in disagree if r["keyword_label"] == "META" and r["classifier_label"] == "GENUINE"]

    print(f"\n  Total disagreements: {len(disagree)} / {len(results)} ({len(disagree)/len(results)*100:.1f}%)")
    print(f"    Keyword=REVISION, LLM=META:  {len(kw_rev_new_meta)} (keyword missed a meta-response)")
    print(f"    Keyword=META, LLM=GENUINE:   {len(kw_meta_new_gen)} (keyword missed a genuine revision)")

    print("\n  By model:")
    for m in models:
        m_dis = [r for r in disagree if r["model"] == m]
        m_rm = sum(1 for r in m_dis if r["keyword_label"] == "REVISION" and r["classifier_label"] == "META")
        m_mg = sum(1 for r in m_dis if r["keyword_label"] == "META" and r["classifier_label"] == "GENUINE")
        print(f"    {m:<20} | kw=REV->META {m_rm:>3} | kw=META->GEN {m_mg:>3} | total {len(m_dis):>3}")

    print("\n  By turn:")
    for t in [2, 3, 4, 5]:
        t_dis = [r for r in disagree if r["turn"] == t]
        t_rm = sum(1 for r in t_dis if r["keyword_label"] == "REVISION" and r["classifier_label"] == "META")
        t_mg = sum(1 for r in t_dis if r["keyword_label"] == "META" and r["classifier_label"] == "GENUINE")
        print(f"    T{t}: kw=REV->META {t_rm:>3} | kw=META->GEN {t_mg:>3} | total {len(t_dis):>3}")

    # 3. Audit sample from disagreements
    print("\n" + "=" * 80)
    print("REPORT 3: 20-ROW AUDIT SAMPLE (from disagreements only)")
    print("=" * 80)

    # Load full text for audit
    text_map = {}
    with open(CANDIDATES) as f:
        for line in f:
            r = json.loads(line)
            text_map[(r["trial_id"], r["turn"])] = r["text"]

    random.seed(20260608)
    audit = list(disagree)
    random.shuffle(audit)
    audit = audit[:20]

    for i, r in enumerate(audit, 1):
        text = text_map.get((r["trial_id"], r["turn"]), "(text not found)")
        print(f"\n  --- AUDIT #{i} ---")
        print(f"  trial={r['trial_id']} | {r['model']} | T{r['turn']} | domain={r['domain']}")
        print(f"  Keyword: {r['keyword_label']} | LLM: {r['classifier_label']}")
        print(f"  Reason: {r['reason']}")
        print(f"  TEXT ({len(text)} chars):")
        print(text[:2000])
        if len(text) > 2000:
            print(f"  [... truncated, {len(text)} total chars]")
        print(f"  --- END #{i} ---")

    print("\n" + "=" * 80)
    print("DONE. Labels saved to genuine_meta_labels.jsonl")
    print("Awaiting user review of audit sample before any recomputation.")
    print("=" * 80)


if __name__ == "__main__":
    main()
