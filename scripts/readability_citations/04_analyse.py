"""Readability of an abstract against the paper's citation count.

Reads .rc_matched.json (abstracts + Semantic Scholar citation counts), measures each
abstract with 02_metrics.py, and computes the correlations, the year-stratified
correlations, the regressions with controls, and the tail comparison. Every number
in readability_citations.md comes from this script.

Run with the venv python that has textstat, numpy and scipy.
"""
from pathlib import Path
import importlib.util, json, math, re, sys
import numpy as np
from scipy import stats

REF = str(Path(__file__).resolve().parents[2] / "paper/reference/")
spec = importlib.util.spec_from_file_location(
    "m", str(Path(__file__).resolve().parent / "02_metrics.py"))
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)

MEASURES = [("flesch", "Flesch reading ease"),
            ("words_per_sentence", "Words per sentence"),
            ("syllables_per_word", "Syllables per word"),
            ("nominal_per_100w", "Nominalisations per 100 words"),
            ("n_words", "Abstract length (words)"),
            ("numerals_per_100w", "Numerals per 100 words")]

# Mechanical proxy for "released a benchmark or model": release language in the
# abstract. A proxy, not a verified artifact check; disclosed as such.
ART = re.compile(r"\b(we (?:release|publicly release|open[- ]source|make .{0,30}publicly)"
                 r"|publicly available|released? (?:at|our)|our (?:code|dataset|benchmark|model)s?"
                 r" (?:and|is|are|will)|we (?:introduce|present|construct|curate|build)"
                 r" .{0,60}(?:benchmark|dataset|corpus|test ?set|suite)"
                 r"|new benchmark|we (?:train|fine-?tune|release) .{0,40}model)\b", re.I)


def fisher_ci(r, n, alpha=0.05):
    if n < 4 or abs(r) >= 1:
        return (float("nan"), float("nan"))
    z = 0.5 * math.log((1 + r) / (1 - r))
    se = 1.0 / math.sqrt(n - 3)
    c = stats.norm.ppf(1 - alpha / 2)
    lo, hi = z - c * se, z + c * se
    return (math.tanh(lo), math.tanh(hi))


def corr_row(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    pr, pp = stats.pearsonr(x, y)
    sr, sp = stats.spearmanr(x, y)
    plo, phi = fisher_ci(pr, n)
    slo, shi = fisher_ci(sr, n)
    return dict(n=n, pearson=pr, p_lo=plo, p_hi=phi, p_p=pp,
                spearman=sr, s_lo=slo, s_hi=shi, s_p=sp)


def ols(y, X, names):
    X = np.asarray(X, float); y = np.asarray(y, float)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    n, k = X.shape
    dof = n - k
    s2 = resid @ resid / dof
    XtXi = np.linalg.pinv(X.T @ X)
    se = np.sqrt(np.diag(XtXi) * s2)
    t = beta / se
    p = 2 * stats.t.sf(np.abs(t), dof)
    crit = stats.t.ppf(0.975, dof)
    return [dict(name=nm, b=b, se=s, t=tt, p=pp, lo=b - crit * s, hi=b + crit * s)
            for nm, b, s, tt, pp in zip(names, beta, se, t, p)], dof


def main():
    d = json.load(open(REF + ".rc_matched.json"))
    rows = []
    for k, v in d["papers"].items():
        r = dict(v)
        r["metrics"] = M.measure(v["abstract"])
        r.update(r.pop("metrics"))
        r["artifact"] = 1 if ART.search(v["abstract"]) else 0
        # age variable: arXiv submission year where known, else S2 year
        ap = v.get("arxiv_published")
        r["post_year"] = int(ap[:4]) if ap else v.get("year")
        r["log1p_cit"] = math.log1p(v["citations"]) if v.get("citations") is not None else None
        rows.append(r)
    json.dump(rows, open(REF + ".rc_rows.json", "w"), indent=1)

    matched = [r for r in rows if r.get("citations") is not None]
    out = {"n_abstracts": len(rows), "n_matched": len(matched)}

    # analysis set: the 2023-2024 topical arXiv draw
    A = [r for r in matched if r["source_set"] == "arxiv_2023_2024_topical"]
    out["n_analysis"] = len(A)
    print("abstracts", len(rows), "matched", len(matched), "analysis set", len(A))

    def block(sample, label):
        res = {}
        y = [r["log1p_cit"] for r in sample]
        yr = [r["citations"] for r in sample]
        for key, _ in MEASURES:
            x = [r[key] for r in sample]
            res[key] = {"log1p": corr_row(x, y), "raw": corr_row(x, yr)}
        return res

    out["main"] = block(A, "all")
    out["by_year"] = {}
    for yv in sorted({r["post_year"] for r in A if r["post_year"]}):
        sub = [r for r in A if r["post_year"] == yv]
        if len(sub) >= 10:
            out["by_year"][str(yv)] = {"n": len(sub), **block(sub, str(yv))}

    # regression: log1p(cit) ~ measure + year dummies + venue-class dummies + artifact
    def venue_class(r):
        v = (r.get("venue") or "").lower()
        if not v or "arxiv" in v:
            return "preprint"
        if any(t in v for t in ("computational linguistics", "empirical methods",
                                "north american", "language resources", "findings")):
            return "acl-family"
        return "other-venue"
    yrs = sorted({r["post_year"] for r in A if r["post_year"]})
    vcs = sorted({venue_class(r) for r in A})
    out["reg"] = {}
    for key, _ in MEASURES:
        X, yv, names = [], [], ["const", key] + \
            ["year=%d" % t for t in yrs[1:]] + ["venue=%s" % c for c in vcs[1:]] + ["artifact"]
        for r in A:
            if r["post_year"] is None:
                continue
            row = [1.0, r[key]]
            row += [1.0 if r["post_year"] == t else 0.0 for t in yrs[1:]]
            row += [1.0 if venue_class(r) == c else 0.0 for c in vcs[1:]]
            row += [float(r["artifact"])]
            X.append(row); yv.append(r["log1p_cit"])
        co, dof = ols(yv, X, names)
        out["reg"][key] = {"n": len(yv), "dof": dof, "coefs": co}

    # descriptives
    def desc(vals):
        a = np.asarray(vals, float)
        return dict(n=len(a), min=float(a.min()), p25=float(np.percentile(a, 25)),
                    median=float(np.median(a)), p75=float(np.percentile(a, 75)),
                    max=float(a.max()), mean=float(a.mean()), sd=float(a.std(ddof=1)))
    out["desc"] = {k: desc([r[k] for r in A]) for k, _ in MEASURES}
    out["desc"]["citations"] = desc([r["citations"] for r in A])
    out["artifact_share"] = sum(r["artifact"] for r in A) / len(A)
    out["venue_counts"] = {c: sum(1 for r in A if venue_class(r) == c) for c in vcs}
    out["year_counts"] = {str(t): sum(1 for r in A if r["post_year"] == t) for t in yrs}

    # 2026 zero check
    recent = [r for r in matched if r["source_set"].startswith(("sample_2026", "sample2_2026"))]
    out["acl2026"] = {"n": len(recent),
                      "n_zero": sum(1 for r in recent if r["citations"] == 0),
                      "median": float(np.median([r["citations"] for r in recent])) if recent else None,
                      "max": max([r["citations"] for r in recent]) if recent else None}

    # tails
    S = sorted(A, key=lambda r: r["citations"])
    lo20, hi20 = S[:20], S[-20:]
    def tail(sample):
        return {k: desc([r[k] for r in sample]) for k, _ in MEASURES}
    out["tail_low"] = tail(lo20); out["tail_high"] = tail(hi20)
    out["tail_low_cit"] = [r["citations"] for r in lo20]
    out["tail_high_cit"] = [r["citations"] for r in hi20]
    for k, _ in MEASURES:
        u = stats.mannwhitneyu([r[k] for r in hi20], [r[k] for r in lo20],
                               alternative="two-sided")
        out.setdefault("tail_test", {})[k] = {"U": float(u.statistic), "p": float(u.pvalue)}
    hi_sorted = sorted(hi20, key=lambda r: -r["flesch"])
    out["hi_most_readable"] = [{"id": r["local_id"], "title": r["title"],
                                "flesch": r["flesch"], "cit": r["citations"],
                                "abstract": r["abstract"]} for r in hi_sorted[:3]]
    out["hi_least_readable"] = [{"id": r["local_id"], "title": r["title"],
                                 "flesch": r["flesch"], "cit": r["citations"],
                                 "abstract": r["abstract"]} for r in hi_sorted[-3:]]
    out["table"] = [{"id": r["local_id"], "year": r["post_year"], "cit": r["citations"],
                     "venue": venue_class(r), "artifact": r["artifact"],
                     **{k: r[k] for k, _ in MEASURES}} for r in
                    sorted(A, key=lambda r: -r["citations"])]
    json.dump(out, open(REF + ".rc_results.json", "w"), indent=1, default=float)
    print(json.dumps({k: out[k] for k in ("n_abstracts", "n_matched", "n_analysis",
                                          "year_counts", "venue_counts", "acl2026")},
                     indent=1, default=float))
    for k, lab in MEASURES:
        m = out["main"][k]["log1p"]
        print("%-24s n=%d  pearson %.3f [%.3f,%.3f] p=%.4f   spearman %.3f [%.3f,%.3f] p=%.4f"
              % (lab, m["n"], m["pearson"], m["p_lo"], m["p_hi"], m["p_p"],
                 m["spearman"], m["s_lo"], m["s_hi"], m["s_p"]))


main()
