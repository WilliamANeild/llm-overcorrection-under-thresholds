#!/usr/bin/env python3
"""
Find arXiv papers close to this project's topic whose arXiv record states an
ACL-family venue. Extends the corpus in paper/rules/03_introduction.md, which was
thin exactly here: 23 introductions but only 4 with a confirmed ACL-family venue.

Venue is read from the arXiv `comment` and `journal_ref` fields. Nothing is inferred:
a paper with no stated venue is recorded as such and is not counted as ACL-family.

    python3 scripts/introduction_corpus/01_find_candidates.py

Writes .workspace/reference/intro_corpus/candidates.json
"""
import json, re, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / ".workspace/reference/intro_corpus"
API = "https://export.arxiv.org/api/query?"
NS = {"a": "http://www.w3.org/2005/Atom"}

# Topic terms drawn from the paper's own related-work themes (paper/SKELETON.md §2).
TOPICS = [
    '"self-correction"', '"self-refinement"', '"self-critique"', '"self-improvement"',
    '"sycophancy"', '"LLM-as-a-judge"', '"LLM evaluators"', '"judge bias"',
    '"multi-turn"', '"underspecification"', '"conversational"',
    '"human-AI interaction"', '"over-reliance"', '"revision"', '"feedback"',
]
VENUES = ['"ACL 2024"', '"ACL 2025"', '"ACL 2026"', '"EMNLP 2024"', '"EMNLP 2025"',
          '"NAACL 2024"', '"NAACL 2025"', '"EACL 2024"', '"EACL 2025"', '"TACL"']

ACL_FAMILY = re.compile(r'\b(ACL|EMNLP|NAACL|EACL|CoNLL|TACL|COLING)\b', re.I)


def query(q, n=40):
    url = API + urllib.parse.urlencode(
        {"search_query": q, "max_results": n, "sortBy": "relevance"})
    with urllib.request.urlopen(url, timeout=60) as r:
        return ET.fromstring(r.read())


def entries(root):
    for e in root.findall("a:entry", NS):
        idu = e.find("a:id", NS).text
        m = re.search(r'abs/([\w.\-]+?)(v\d+)?$', idu)
        comment = e.find("{http://arxiv.org/schemas/atom}comment")
        jref = e.find("{http://arxiv.org/schemas/atom}journal_ref")
        yield {
            "arxiv_id": m.group(1),
            "version": (m.group(2) or ""),
            "title": " ".join(e.find("a:title", NS).text.split()),
            "comment": " ".join(comment.text.split()) if comment is not None and comment.text else "",
            "journal_ref": " ".join(jref.text.split()) if jref is not None and jref.text else "",
            "published": e.find("a:published", NS).text[:10],
        }


def main():
    found, seen = [], set()
    for v in VENUES:
        topic_clause = " OR ".join(f"abs:{t}" for t in TOPICS)
        q = f'cat:cs.CL AND co:{v} AND ({topic_clause})'
        try:
            root = query(q)
        except Exception as exc:
            print(f"  query failed for {v}: {exc}")
            continue
        n_v = 0
        for e in entries(root):
            if e["arxiv_id"] in seen:
                continue
            stated = f'{e["comment"]} {e["journal_ref"]}'.strip()
            if not ACL_FAMILY.search(stated):
                continue          # venue not stated in the record; not asserted
            seen.add(e["arxiv_id"])
            e["venue_stated"] = stated
            found.append(e)
            n_v += 1
        print(f"{v:<14} {n_v:>3} new")
        time.sleep(3)             # arXiv asks for 3s between requests

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "candidates.json").write_text(json.dumps(found, indent=1))
    print(f"\n{len(found)} candidates with a stated ACL-family venue")


if __name__ == "__main__":
    main()
