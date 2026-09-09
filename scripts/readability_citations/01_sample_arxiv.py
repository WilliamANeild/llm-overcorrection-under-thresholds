"""Draw a 2023-2024 arXiv cs.CL sample in the LLM self-correction / evaluation /
multi-turn / human-AI interaction literature, verbatim abstracts, for the
readability-vs-citations analysis. Systematic sample, fixed seed, per-phrase strata.
"""
import json, random, re, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET

SEED = 20260906
OUT = "/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/reference/.rc_arxiv_sample.json"
API = "https://export.arxiv.org/api/query?"
NS = {"a": "http://www.w3.org/2005/Atom"}

# One stratum per topical phrase. Frame = cs.CL, submitted 2023-01-01..2024-12-31,
# phrase present in title or abstract.
PHRASES = [
    ("self-correction",              22),
    ("self-refinement",              10),
    ("self-critique",                 8),
    ("self-consistency",             10),
    ("LLM-as-a-judge",               12),
    ("evaluating large language models", 14),
    ("multi-turn",                   22),
    ("human-AI interaction",         12),
    ("human-LLM",                     8),
    ("feedback",                     16),  # broad topical anchor within cs.CL LLM work
    ("revision",                     10),
    ("hallucination detection",      10),
]
DATE = "submittedDate:[202301010000+TO+202412312359]"


def fetch(query, start, n, tries=5):
    url = API + "search_query=%s&start=%d&max_results=%d&sortBy=submittedDate&sortOrder=ascending" % (
        query, start, n)
    for t in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except Exception as e:
            print("   retry", t, e)
            time.sleep(6 * (t + 1))
    return None


def total_for(query):
    b = fetch(query, 0, 1)
    if b is None:
        return 0
    root = ET.fromstring(b)
    el = root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults")
    return int(el.text) if el is not None else 0


def parse(b):
    root = ET.fromstring(b)
    out = []
    for e in root.findall("a:entry", NS):
        aid = e.find("a:id", NS).text.rsplit("/", 1)[-1]
        out.append({
            "arxiv_id_v": aid,
            "arxiv_id": re.sub(r"v\d+$", "", aid),
            "title": " ".join(e.find("a:title", NS).text.split()),
            "abstract": " ".join(e.find("a:summary", NS).text.split()),
            "published": e.find("a:published", NS).text,
        })
    return out


def main():
    rng = random.Random(SEED)
    picked, prov = {}, []
    for phrase, want in PHRASES:
        q = 'cat:cs.CL+AND+abs:%%22%s%%22+AND+%s' % (urllib.parse.quote(phrase), DATE)
        tot = total_for(q)
        time.sleep(3.5)
        print(phrase, "total", tot)
        if tot == 0:
            prov.append({"phrase": phrase, "stratum_total": 0, "target": want, "drawn": 0})
            continue
        cap = min(tot, 400)            # index positions we can reach cheaply
        stride = max(1, cap // want)
        start0 = rng.randrange(stride)
        idxs = [start0 + i * stride for i in range(want) if start0 + i * stride < cap]
        got = 0
        # fetch in contiguous pages covering the needed indices
        for i0 in range(0, cap, 100):
            need = [i for i in idxs if i0 <= i < i0 + 100]
            if not need:
                continue
            b = fetch(q, i0, 100)
            time.sleep(3.5)
            if b is None:
                continue
            page = parse(b)
            for i in need:
                j = i - i0
                if j < len(page):
                    rec = page[j]
                    rec.update(stratum=phrase, stratum_total=tot, index_in_stratum=i)
                    if rec["arxiv_id"] not in picked:
                        picked[rec["arxiv_id"]] = rec
                        got += 1
        prov.append({"phrase": phrase, "stratum_total": tot, "reachable_cap": cap,
                     "stride": stride, "random_start": start0, "target": want, "drawn_new": got})
        print("   kept", got, "running", len(picked))
    json.dump({"_provenance": {
        "retrieved": "2026-09-06", "source": "arXiv API export.arxiv.org/api/query",
        "frame": "cat:cs.CL AND phrase in abstract AND submittedDate 2023-01-01..2024-12-31",
        "sampling": "one stratum per topical phrase; systematic sample over date-ascending "
                    "result order with fixed random start and constant stride; seed 20260906; "
                    "cross-stratum duplicates kept once (first stratum to draw them)",
        "seed": SEED, "strata": prov, "n_unique": len(picked)},
        "papers": picked}, open(OUT, "w"), indent=1)
    print("TOTAL UNIQUE", len(picked))


main()
