"""Assemble every paper for which we hold a verbatim abstract, attach a Semantic
Scholar citation count, and write one flat record per paper.

Sources of abstracts:
  A. paper/reference/acl2026_abstracts.json  (2026 ACL-venue draws, the 2024/2026
     no-artifact draw, and two small arXiv cs.CL draws)
  B. paper/reference/.rc_arxiv_sample.json   (the 2023-2024 arXiv cs.CL topical draw
     built by 01_sample_arxiv.py)

Citation counts: Semantic Scholar Graph API /paper/batch, 100 ids per request,
paced. arXiv papers are looked up as arXiv:ID; Anthology papers as ACL:ID and, on
a miss, as DOI:10.18653/v1/ID.
"""
from pathlib import Path
import json, time, urllib.request

REF = str(Path(__file__).resolve().parents[2] / "paper/reference/")
S2 = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=" \
     "title,year,venue,citationCount,externalIds,publicationTypes,publicationDate"


def batch(ids, tries=6):
    body = json.dumps({"ids": ids}).encode()
    for t in range(tries):
        try:
            req = urllib.request.Request(S2, data=body,
                                         headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:
            print("   retry", t, e)
            time.sleep(8 * (t + 1))
    return [None] * len(ids)


def collect():
    d = json.load(open(REF + "acl2026_abstracts.json"))
    recs = {}

    def add(key, rec):
        if key not in recs:
            recs[key] = rec

    for setname in ("sample_2026_09_06", "sample2_2026_09_06", "sample_2026_09_06_wave2"):
        for k, v in d.get(setname, {}).items():
            if not v.get("abstract"):
                continue
            add("ACL:" + k, {"lookup": "ACL:" + k, "local_id": k, "kind": "anthology",
                             "title": v.get("title", ""), "abstract": v["abstract"],
                             "source_set": setname})
    for k, v in d.get("no_artifact_2024_2026", {}).items():
        if not v.get("abstract"):
            continue
        add("ACL:" + k, {"lookup": "ACL:" + k, "local_id": k, "kind": "anthology",
                         "title": v.get("title", ""), "abstract": v["abstract"],
                         "source_set": "no_artifact_2024_2026"})
    for setname in ("arxiv_cs_cl_2026_09_06", "arxiv_cs_cl_2026_09_06_api_unused"):
        for k, v in d.get(setname, {}).items():
            if not v.get("abstract"):
                continue
            aid = v.get("arxiv_id", k).split("v")[0]
            add("arXiv:" + aid, {"lookup": "arXiv:" + aid, "local_id": aid, "kind": "arxiv",
                                 "title": v.get("title", ""), "abstract": v["abstract"],
                                 "source_set": setname})
    try:
        s = json.load(open(REF + ".rc_arxiv_sample.json"))
        for k, v in s["papers"].items():
            add("arXiv:" + k, {"lookup": "arXiv:" + k, "local_id": k, "kind": "arxiv",
                               "title": v["title"], "abstract": v["abstract"],
                               "source_set": "arxiv_2023_2024_topical",
                               "arxiv_published": v["published"], "stratum": v["stratum"]})
    except FileNotFoundError:
        print("WARNING: 2023-2024 arXiv sample not present")
    return recs


def main():
    recs = collect()
    keys = list(recs)
    print("abstracts held:", len(keys))
    for i in range(0, len(keys), 100):
        chunk = keys[i:i + 100]
        res = batch(chunk)
        for k, r in zip(chunk, res):
            if r:
                recs[k].update(s2_title=r.get("title"), year=r.get("year"),
                               venue=r.get("venue"), citations=r.get("citationCount"),
                               s2_id=r.get("paperId"), ext=r.get("externalIds"),
                               pubtypes=r.get("publicationTypes"),
                               pubdate=r.get("publicationDate"))
        print("batch", i, "matched so far",
              sum(1 for v in recs.values() if v.get("citations") is not None))
        time.sleep(4)

    # second pass: anthology misses retried as DOI
    miss = [k for k, v in recs.items() if v.get("citations") is None and v["kind"] == "anthology"]
    print("anthology misses to retry as DOI:", len(miss))
    for i in range(0, len(miss), 100):
        chunk = miss[i:i + 100]
        res = batch(["DOI:10.18653/v1/" + recs[k]["local_id"] for k in chunk])
        for k, r in zip(chunk, res):
            if r:
                recs[k].update(s2_title=r.get("title"), year=r.get("year"),
                               venue=r.get("venue"), citations=r.get("citationCount"),
                               s2_id=r.get("paperId"), ext=r.get("externalIds"),
                               pubtypes=r.get("publicationTypes"),
                               pubdate=r.get("publicationDate"),
                               matched_via="DOI")
        time.sleep(4)

    got = sum(1 for v in recs.values() if v.get("citations") is not None)
    print("MATCHED", got, "of", len(recs))
    json.dump({"_retrieved": "2026-09-06",
               "_source": "Semantic Scholar Graph API /paper/batch",
               "_n_abstracts": len(recs), "_n_matched": got,
               "papers": recs}, open(REF + ".rc_matched.json", "w"), indent=1)


main()
