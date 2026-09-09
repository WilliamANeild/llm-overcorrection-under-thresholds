# Bibliography audit, chunk 3

File audited: `/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/references.bib`
Keys audited: 17 (listed in the summary table at the end)
All retrievals performed 2026-09-05 unless a different date is stated in the entry section.
Nothing in `references.bib` or any other project file was modified.

Sources used, and how each was reached:

- arXiv abstract pages, fetched directly at `https://arxiv.org/abs/<id>` (the arXiv API at
  `export.arxiv.org` returned HTTP 429/503 throughout and was not used).
- ACL Anthology canonical BibTeX, fetched at `https://aclanthology.org/<id>.bib`.
- NeurIPS official proceedings BibTeX at `https://papers.nips.cc/paper_files/paper/2023/file/<hash>-Bibtex-*.bib`.
- PMLR proceedings pages at `https://proceedings.mlr.press/`.
- Crossref REST API at `https://api.crossref.org/works/<doi>`.
- OpenAlex at `https://api.openalex.org/works`.
- DBLP at `https://dblp.org/search/publ/api`.
- Publisher and vendor pages fetched directly.

Two sources could not be fetched and are flagged where they matter: `direct.mit.edu`
(Cloudflare interstitial), `dl.acm.org` (Cloudflare interstitial), and `openreview.net`
(bot challenge). In each case the same fact was obtained from a different fetched source and
the substitution is stated in the entry.

---

## 1. `wei2024simple` — FIELD ERRORS

Current entry:

```bibtex
@article{wei2024simple,
  title={Simple Synthetic Data Reduces Sycophancy in Large Language Models},
  author={Wei, Jerry and Huang, Da and Lu, Yifeng and Ippolito, Daphne and Hashimoto, Tatsunori and Chowdhery, Aakanksha and Le, Quoc V},
  journal={arXiv preprint arXiv:2308.03958},
  year={2024}
}
```

Evidence: `https://arxiv.org/abs/2308.03958`, `https://arxiv.org/abs/2308.03958v1`,
`https://arxiv.org/abs/2308.03958v2`, all retrieved 2026-09-05.

The paper exists. The arXiv record gives the same five authors in both v1 (7 Aug 2023) and
v2 (15 Feb 2024):

> Wei, Jerry | Huang, Da | Lu, Yifeng | Zhou, Denny | Le, Quoc V.

Errors:

| Field | In the entry | Correct value |
|---|---|---|
| `author` | Wei, Huang, Lu, **Ippolito**, **Hashimoto**, **Chowdhery**, Le | Wei, Jerry; Huang, Da; Lu, Yifeng; **Zhou, Denny**; Le, Quoc V. |
| `year` | 2024 | 2023 (v1 posted 7 Aug 2023); 2024 is defensible only if citing v2 specifically |

Three people named in the entry (Daphne Ippolito, Tatsunori Hashimoto, Aakanksha Chowdhery)
are not authors of this paper in either version, and Denny Zhou, who is an author, is
omitted. This is the most serious author-list problem in the chunk.

Notes, not errors: arXiv renders the title in sentence case, "Simple synthetic data reduces
sycophancy in large language models"; the entry's title case is a normal BibTeX styling
choice. No journal or conference publication was found for this work; DBLP and OpenAlex hold
only the arXiv record, so listing it as a preprint is correct.

Corrected entry:

```bibtex
@article{wei2024simple,
  title={Simple Synthetic Data Reduces Sycophancy in Large Language Models},
  author={Wei, Jerry and Huang, Da and Lu, Yifeng and Zhou, Denny and Le, Quoc V.},
  journal={arXiv preprint arXiv:2308.03958},
  year={2023}
}
```

---

## 2. `sclar2024quantifying` — FIELD ERRORS

Current entry:

```bibtex
@article{sclar2024quantifying,
  title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design with a Focus on Faithfulness and Consistency},
  author={Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
  journal={arXiv preprint arXiv:2310.11324},
  year={2024}
}
```

Evidence: `https://arxiv.org/abs/2310.11324`, retrieved 2026-09-05. The arXiv title reads:

> Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I
> learned to start worrying about prompt formatting

and the arXiv comment field reads "ICLR 2024 Camera Ready version."

| Field | In the entry | Correct value |
|---|---|---|
| `title` | "... in Prompt Design **with a Focus on Faithfulness and Consistency**" | "... in Prompt Design **or: How I learned to start worrying about prompt formatting**" |
| venue | arXiv preprint only | Published at ICLR 2024 |

The subtitle in the entry does not appear in any version of this paper. The authors (four,
in that order) and the arXiv ID are correct, and `year=2024` is correct for the ICLR
publication.

On the ICLR publication: the arXiv comment field (fetched directly) states the ICLR 2024
camera-ready status, and DBLP holds an ICLR 2024 conference record for it
(`https://dblp.org/rec/conf/iclr/Sclar0TS24`, retrieved 2026-09-05) pointing to
`https://openreview.net/forum?id=RIu5lyNXjT`. That OpenReview page could not be fetched
(bot challenge on both `openreview.net` and the OpenReview API, 2026-09-05), so the ICLR
venue rests on the arXiv comment plus DBLP rather than on the venue's own page.

Corrected entry (as a conference paper):

```bibtex
@inproceedings{sclar2024quantifying,
  title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting},
  author={Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
  booktitle={The Twelfth International Conference on Learning Representations (ICLR)},
  year={2024},
  url={https://openreview.net/forum?id=RIu5lyNXjT},
  note={arXiv:2310.11324}
}
```

If you prefer to keep citing the preprint, at minimum the title must be corrected.

---

## 3. `zheng2024judging` — FIELD ERRORS

Current entry:

```bibtex
@inproceedings{zheng2024judging,
  title={Judging {LLM}-as-a-Judge with {MT}-Bench and Chatbot Arena},
  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P and others},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}
```

Evidence: official NeurIPS proceedings BibTeX,
`https://papers.nips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Bibtex-Datasets_and_Benchmarks.bib`,
and the 2023 index page `https://papers.nips.cc/paper_files/paper/2023`, both retrieved
2026-09-05. The proceedings record:

```
booktitle = {Advances in Neural Information Processing Systems},
volume = {36}, year = {2023}, pages = {46595--46623},
publisher = {Curran Associates, Inc.}, doi = {10.52202/075280-2020}
author = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric and Zhang, Hao and Gonzalez, Joseph and Stoica, Ion}
```

| Field | In the entry | Correct value |
|---|---|---|
| `year` | 2024 | **2023** (NeurIPS 36 is the 2023 conference) |

`volume={36}` and the booktitle are correct. The three authors hidden behind `and others`
are **Hao Zhang, Joseph E. Gonzalez, and Ion Stoica**; the ten named authors are correct and
in the right order. Missing but recoverable: `pages={46595--46623}`, publisher, DOI. The
paper appeared in the NeurIPS 2023 Datasets and Benchmarks Track, which is worth naming if
the bibliography style has room for it.

Corrected entry:

```bibtex
@inproceedings{zheng2024judging,
  title={Judging {LLM}-as-a-Judge with {MT}-Bench and Chatbot Arena},
  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  pages={46595--46623},
  publisher={Curran Associates, Inc.},
  year={2023},
  doi={10.52202/075280-2020}
}
```

---

## 4. `zhou2024calibrated` — FIELD ERRORS (severe)

Current entry:

```bibtex
@article{zhou2024calibrated,
  title={Calibrated Language Models Must Hallucinate},
  author={Zhou, Adam Tauman and Bai, Yifei and Mei, Song and Kakade, Sham M},
  journal={arXiv preprint arXiv:2311.14648},
  year={2024}
}
```

Evidence: `https://arxiv.org/abs/2311.14648`, retrieved 2026-09-05, which gives:

> AUTHORS: Kalai, Adam Tauman | Vempala, Santosh S.
> COMMENTS: In Proceedings of the 56th Annual ACM Symposium on Theory of Computing (STOC) 2024

and Crossref for `10.1145/3618260.3649777`
(`https://api.crossref.org/works/10.1145/3618260.3649777`, retrieved 2026-09-05):

> title: Calibrated Language Models Must Hallucinate
> container: Proceedings of the 56th Annual ACM Symposium on Theory of Computing
> page: 160-171 | issued: 2024-06-10 | publisher: ACM
> authors: Adam Tauman Kalai; Santosh S. Vempala
> event: STOC '24: 56th Annual ACM Symposium on Theory of Computing, Vancouver BC Canada

| Field | In the entry | Correct value |
|---|---|---|
| `author` | Zhou, Adam Tauman; Bai, Yifei; Mei, Song; Kakade, Sham M | **Kalai, Adam Tauman; Vempala, Santosh S.** |
| venue | arXiv preprint only | Proceedings of the 56th Annual ACM Symposium on Theory of Computing (STOC 2024), pp. 160–171, ACM |

The entry names four authors; the paper has two. The first author's surname is **Kalai**,
not Zhou: the entry has taken "Adam Tauman" as given names and attached a surname that is
not his. Yifei Bai, Song Mei and Sham M. Kakade are not authors of this paper. The bibtex
key `zhou2024calibrated` itself encodes the wrong surname and would be worth renaming to
`kalai2024calibrated`, which is a call for you rather than a citation error as such.

The title and the arXiv ID are correct, and `year=2024` is correct for the STOC publication
(arXiv v1 was posted 24 Nov 2023).

Corrected entry:

```bibtex
@inproceedings{zhou2024calibrated,
  title={Calibrated Language Models Must Hallucinate},
  author={Kalai, Adam Tauman and Vempala, Santosh S.},
  booktitle={Proceedings of the 56th Annual ACM Symposium on Theory of Computing (STOC)},
  pages={160--171},
  publisher={ACM},
  year={2024},
  doi={10.1145/3618260.3649777},
  note={arXiv:2311.14648}
}
```

---

## 5. `white2023prompt` — VERIFIED

Current entry:

```bibtex
@article{white2023prompt,
  title={A Prompt Pattern Catalog to Enhance Prompt Engineering with {ChatGPT}},
  author={White, Jules and Fu, Quchen and Hays, Sam and Sandborn, Michael and Olea, Carlos and Gilbert, Henry and Elnashar, Ashraf and Spencer-Smith, Jesse and Schmidt, Douglas C},
  journal={arXiv preprint arXiv:2302.11382},
  year={2023}
}
```

Evidence: `https://arxiv.org/abs/2302.11382`, retrieved 2026-09-05. Title matches character
for character. All nine authors match, in order: White, Jules; Fu, Quchen; Hays, Sam;
Sandborn, Michael; Olea, Carlos; Gilbert, Henry; Elnashar, Ashraf; Spencer-Smith, Jesse;
Schmidt, Douglas C. Single version, posted 21 Feb 2023, so `year=2023` is right. arXiv ID
correct.

Every field asserted in the entry is correct, so this is VERIFIED. One thing you may want to
act on: the work has since been published. Crossref for `10.64346/plop2023p05`
(`https://api.crossref.org/works/10.64346/plop2023p05`, retrieved 2026-09-05) records it in
*Proceedings of the 30th Conference on Pattern Languages of Programs* (PLoP 2023, Allerton
Park, Monticello, Illinois, 22–25 October 2023), publisher The Hillside Group. The Crossref
record carries no author list, so the deposit is thin, and the arXiv preprint remains the
version almost everyone cites. Updating is optional; the current entry is not wrong.

---

## 6. `rafailov2023direct` — FIELD ERRORS (author order)

Current entry:

```bibtex
@article{rafailov2023direct,
  title={Direct Preference Optimization: Your Language Model is Secretly a Reward Model},
  author={Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Ermon, Stefano and Manning, Christopher D and Finn, Chelsea},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2023}
}
```

Evidence: official NeurIPS proceedings BibTeX,
`https://papers.nips.cc/paper_files/paper/2023/file/a85b405ed65c6477a4fe8302b5e06ce7-Bibtex-Conference.bib`,
and the proceedings landing page
`https://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html`,
both retrieved 2026-09-05. Both give:

> Rafael Rafailov, Archit Sharma, Eric Mitchell, **Christopher D Manning, Stefano Ermon**, Chelsea Finn
> Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Main Conference Track
> pages = {53728--53741}, publisher = {Curran Associates, Inc.}, doi = {10.52202/075280-2338}, year = {2023}

**Two sources disagree, and both are reported.** The arXiv record
(`https://arxiv.org/abs/2305.18290`, via OpenAlex `https://api.openalex.org/works`, retrieved
2026-09-05) lists the order as Rafailov, Sharma, Mitchell, **Ermon, Manning**, Finn, which is
what the entry currently has. The NeurIPS proceedings, both in its BibTeX export and on the
paper's landing page, lists **Manning before Ermon**.

Since this entry cites the NeurIPS proceedings rather than the preprint, the publisher's
order should govern:

| Field | In the entry | Correct value for the cited venue |
|---|---|---|
| `author` | ... Mitchell, **Ermon**, **Manning**, Finn | ... Mitchell, **Manning, Christopher D**, **Ermon, Stefano**, Finn |

Title, volume 36, and year 2023 are all correct. Missing but recoverable:
`pages={53728--53741}`, publisher, DOI.

Corrected entry:

```bibtex
@inproceedings{rafailov2023direct,
  title={Direct Preference Optimization: Your Language Model is Secretly a Reward Model},
  author={Rafailov, Rafael and Sharma, Archit and Mitchell, Eric and Manning, Christopher D. and Ermon, Stefano and Finn, Chelsea},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  pages={53728--53741},
  publisher={Curran Associates, Inc.},
  year={2023},
  doi={10.52202/075280-2338}
}
```

---

## 7. `deloitte2026stateofai` — VERIFIED

Current entry:

```bibtex
@misc{deloitte2026stateofai,
  title={The State of {AI} in the Enterprise, 2026},
  author={{Deloitte AI Institute}},
  year={2026},
  howpublished={\url{https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html}},
  note={Accessed 2026-06-06}
}
```

Evidence: the URL as given, fetched 2026-09-05, HTTP 200, no redirect. The page returns:

- `<title>`: "The State of AI in the Enterprise - 2026 AI report | Deloitte US"
- `og:title`: "The State of AI in the Enterprise - 2026 AI report"
- meta description: "Explore the Deloitte AI Institute's State of AI in the Enterprise report tracking AI investments, adoption, impacts on business, and challenges throughout 2025."
- body text: "State of AI in the Enterprise — Deloitte's 2026 AI report tracking adoption and impact"; "State of AI in the Enterprise is a research series by the Deloitte AI Institute™"; and a navigation label "State of AI in the Enterprise 2024-2026 reports and associated research".

The page exists at the URL given, is attributed to the Deloitte AI Institute, and is the
2026 edition. Title, author, year and URL all hold.

Two things to be aware of, neither an error in the entry as written. The URL is the series
landing page rather than a stable link to the 2026 report PDF, so it will roll forward to
the 2027 edition when that appears; if the paper leans on a particular figure from the 2026
report, a direct link to that report would be more durable. And the `note={Accessed
2026-06-06}` stamp is three months old. The page was still live and still the 2026 edition
on 2026-09-05, so you can update the stamp to that date, or re-check nearer to submission.

---

## 8. `copilot2025agentmode` — FIELD ERRORS

Current entry:

```bibtex
@misc{copilot2025agentmode,
  title={Introducing {GitHub} {Copilot} Agent Mode},
  author={{GitHub}},
  year={2025},
  howpublished={\url{https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode}},
  note={Accessed 2026-06-06}
}
```

Evidence: the URL as given, fetched 2026-09-05, HTTP 200, no redirect. The page returns:

- `<title>` and `og:title`: "Introducing GitHub Copilot agent mode (preview)"
- byline and date in the body: "Introducing GitHub Copilot agent mode (preview) — February 24, 2025 by Isidor Nikolic"
- meta description: "Announcing the GitHub Copilot agent mode in Visual Studio Code."

| Field | In the entry | Correct value |
|---|---|---|
| `title` | Introducing GitHub Copilot **Agent Mode** | Introducing GitHub Copilot **agent mode (preview)** |
| `author` | `{GitHub}` | The post is on the Visual Studio Code blog (`code.visualstudio.com`, Microsoft) and is bylined **Isidor Nikolic**, not GitHub |

The date (24 February 2025) and the URL are correct. The title differs both in the
capitalization of "agent mode" and in dropping "(preview)"; since the parenthetical is part
of the published headline and is substantively meaningful here, it should stay.

On attribution: the piece is a Visual Studio Code product blog post about a GitHub Copilot
feature. Crediting it to `{GitHub}` misplaces the publisher. Either the individual byline or
the VS Code team is defensible; pick one and be consistent with how other vendor posts are
handled in the bibliography.

The page also now carries a tip box stating that agent mode has since reached VS Code Stable
with MCP server support, so the post describes a preview state that has been superseded. The
page itself is unchanged and still live, so the citation remains valid; just be sure the
prose around it is not claiming agent mode is still in preview.

Corrected entry:

```bibtex
@misc{copilot2025agentmode,
  title={Introducing {GitHub} {Copilot} agent mode (preview)},
  author={Nikolic, Isidor},
  organization={{Visual Studio Code Team, Microsoft}},
  year={2025},
  month={February},
  howpublished={\url{https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode}},
  note={Accessed 2026-09-05}
}
```

---

## 9. `thoppilan2022lamda` — VERIFIED

Current entry:

```bibtex
@article{thoppilan2022lamda,
  title={{LaMDA}: Language Models for Dialog Applications},
  author={Thoppilan, Romal and De Freitas, Daniel and Hall, Jamie and Shazeer, Noam and Kulshreshtha, Apoorv and Cheng, Heng-Tze and Jin, Alicia and Bos, Taylor and Baker, Leslie and Du, Yu and others},
  journal={arXiv preprint arXiv:2201.08239},
  year={2022}
}
```

Evidence: `https://arxiv.org/abs/2201.08239`, retrieved 2026-09-05. Title matches character
for character. The arXiv record carries **60 authors**; the ten named in the entry match the
first ten on the paper, in the correct order (Thoppilan; De Freitas; Hall; Shazeer;
Kulshreshtha; Cheng; Jin; Bos; Baker; Du). The 50 hidden behind `and others` begin YaGuang
Li, Hongrae Lee, Huaixiu Steven Zheng, Amin Ghafouri, Marcelo Menegali, ... and end Claire
Cui, Marian Croak, Ed Chi, Quoc Le. With 60 authors, `and others` is the right call and the
truncation point is standard.

v1 posted 20 Jan 2022, latest v3 posted 10 Feb 2022, so `year=2022` is correct. DBLP and
OpenAlex hold no journal or conference record for it, so listing it as a preprint is correct
and current as of 2026-09-05.

---

## 10. `kamoi2024selfcorrection` — VERIFIED

This is one of the two entries flagged for particular care. **The prose claim that it
appeared "in TACL" is correct.**

Current entry:

```bibtex
@article{kamoi2024selfcorrection,
  title={When Can {LLMs} Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of {LLMs}},
  author={Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui},
  journal={Transactions of the Association for Computational Linguistics},
  volume={12},
  pages={1417--1440},
  year={2024}
}
```

Evidence, three independent fetched sources, all agreeing:

1. ACL Anthology canonical BibTeX, `https://aclanthology.org/2024.tacl-1.78.bib`, retrieved
   2026-09-05:

   ```
   journal = "Transactions of the Association for Computational Linguistics",
   volume = "12", year = "2024", pages = "1417--1440",
   publisher = "MIT Press", address = "Cambridge, MA", doi = "10.1162/tacl_a_00713"
   author = "Kamoi, Ryo and Zhang, Yusen and Zhang, Nan and Han, Jiawei and Zhang, Rui"
   ```

   The paper was located in the volume listing `https://aclanthology.org/volumes/2024.tacl-1/`
   (retrieved 2026-09-05), which places it at `2024.tacl-1.78`.
2. OpenAlex, `https://api.openalex.org/works` title search, retrieved 2026-09-05:
   Transactions of the Association for Computational Linguistics, journal, vol 12, pp.
   1417–1440, 2024, DOI 10.1162/tacl_a_00713.
3. DBLP, `https://dblp.org/rec/journals/tacl/KamoiZZHZ24`, retrieved 2026-09-05: Trans.
   Assoc. Comput. Linguistics, vol 12, pp. 1417–1440, 2024.

The MIT Press page at `https://doi.org/10.1162/tacl_a_00713` (which resolves to
`direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/...`) returned HTTP 403 behind a
Cloudflare interstitial on 2026-09-05 and could not be read. The ACL Anthology is TACL's
co-publisher of record and is treated as authoritative here.

Title, all five authors in order, journal, volume 12, pages 1417–1440 and year 2024 are all
correct. The related-work prose at
`/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/sections/related_work.tex:19`
("provide a critical survey of LLM self-correction in TACL") is accurate and needs no change.

Optional addition, not a correction: `doi={10.1162/tacl_a_00713}` and
`url={https://aclanthology.org/2024.tacl-1.78/}`. Note that the arXiv preprint of this work
is **2406.01297**, not any of the IDs used elsewhere in this chunk, in case you ever want to
cite the preprint version.

---

## 11. `goldman2026tokens` — FIELD ERRORS (severe)

Current entry:

```bibtex
@misc{goldman2026tokens,
  title={Generative {AI}: Token Consumption to Grow 24x by 2030},
  author={Schneider, Eric and others},
  year={2026},
  howpublished={Goldman Sachs Research},
  note={Accessed 2026-06-10}
}
```

Evidence: `https://www.goldmansachs.com/insights/articles/ai-agents-forecast-to-boost-tech-cash-flow-as-usage-soars`,
fetched 2026-09-05, HTTP 200. The page gives:

- `og:title`: "AI Agents Forecast to Boost Tech Cash Flow as Usage Soars"
- structured data `datePublished`: 2026-05-20; body date line: "May 20, 2026"
- body, verbatim: "With consumers and enterprises adopting AI agents, token consumption is
  expected to multiply 24 times, to 120 quadrillion tokens per month, between 2026 and 2030,
  says **Jim Schneider**, the senior equity analyst covering US semiconductor and IT services
  at Goldman Sachs Research."
- summary bullet, verbatim: "Agentic AI is expected to drive a 24-fold increase in token
  consumption by 2030 as consumers and enterprises adopt the technology, according to Goldman
  Sachs Research."

| Field | In the entry | Correct value |
|---|---|---|
| `title` | "Generative AI: Token Consumption to Grow 24x by 2030" | No Goldman Sachs publication with this title was found. The public article is titled **"AI Agents Forecast to Boost Tech Cash Flow as Usage Soars"** |
| `author` | Schneider, **Eric**, and others | **Jim Schneider** is the named analyst. No co-authors are named on the page, so `and others` is unsupported |
| `howpublished` | "Goldman Sachs Research" with no URL | Should carry the article URL and the 20 May 2026 date |

**The underlying claim is sound.** The 24x-by-2030 token consumption figure, and the
120 quadrillion tokens per month endpoint, are stated on the Goldman Sachs page in those
terms. What is wrong is the bibliographic wrapper: the title reads as a paraphrase of the
finding rather than the name of a document, and the analyst's given name is wrong.

One loose end, reported rather than resolved. Several secondary outlets (Enterprise DNA,
Tokenscost, ZeroHedge, retrieved via web search 2026-09-05) describe the underlying Goldman
Sachs Research report as titled *"Decoding the Agentic Economy."* That title does **not**
appear anywhere in the goldmansachs.com page I fetched, and I could not reach a Goldman
Sachs source stating it. Do not put "Decoding the Agentic Economy" in the bibliography on
the strength of those secondary reports. Cite the public Insights article, which is
fetchable and dated.

Corrected entry:

```bibtex
@misc{goldman2026tokens,
  title={{AI} Agents Forecast to Boost Tech Cash Flow as Usage Soars},
  author={{Goldman Sachs Research}},
  year={2026},
  month={May},
  howpublished={\url{https://www.goldmansachs.com/insights/articles/ai-agents-forecast-to-boost-tech-cash-flow-as-usage-soars}},
  note={Published 2026-05-20; analyst Jim Schneider. Accessed 2026-09-05}
}
```

---

## 12. `yang2025underspecification` — FIELD ERRORS

This is the second entry flagged for particular care. **The Findings of ACL 2026 venue is
real and correct. The year field is wrong.**

Current entry:

```bibtex
@article{yang2025underspecification,
  title={What Prompts Don't Say: Understanding and Managing Underspecification in {LLM} Prompts},
  author={Yang, Chenyang and Shi, Yike and Ma, Qianou and Liu, Michael Xieyang and K{\"a}stner, Christian and Wu, Tongshuang},
  journal={Findings of the Association for Computational Linguistics: ACL 2026},
  year={2025},
  note={arXiv:2505.13360}
}
```

Evidence, in the order the checks were run:

1. `https://arxiv.org/abs/2505.13360`, retrieved 2026-09-05. Title, six authors and order all
   confirmed. Versions: v1 19 May 2025, v2 7 Oct 2025, **v3 24 Apr 2026**. The arXiv record
   carries **no journal reference and no venue comment**, which is why the venue could not be
   settled from arXiv alone.
2. DBLP, retrieved 2026-09-05: a conference record at
   `https://dblp.org/rec/conf/acl/YangSMLKW26`, venue ACL, **year 2026**, pages 9072–9101,
   DOI `10.18653/V1/2026.FINDINGS-ACL.441`.
3. **ACL Anthology, checked directly as instructed.** `https://aclanthology.org/2026.findings-acl.441/`
   returned HTTP 200 with page title "What Prompts Don't Say: Understanding and Managing
   Underspecification in LLM Prompts - ACL Anthology". The canonical BibTeX at
   `https://aclanthology.org/2026.findings-acl.441.bib`, retrieved 2026-09-05, reads:

   ```bibtex
   @inproceedings{yang-etal-2026-prompts,
       title = "What Prompts Don{'}t Say: Understanding and Managing Underspecification in {LLM} Prompts",
       author = "Yang, Chenyang and Shi, Yike and Ma, Qianou and Liu, Michael Xieyang and Kaestner, Christian and Wu, Tongshuang",
       booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {ACL} 2026",
       month = jul, year = "2026",
       address = "San Diego, California, United States",
       publisher = "Association for Computational Linguistics",
       url = "https://aclanthology.org/2026.findings-acl.441/",
       doi = "10.18653/v1/2026.findings-acl.441",
       pages = "9072--9101",
       ISBN = "979-8-89176-395-1"
   }
   ```

**Resolution of the year mismatch.** The paper did appear in Findings of ACL 2026, held July
2026 in San Diego. The venue string in the entry is therefore correct as written. The `year`
field must be **2026**, not 2025; 2025 is the year the preprint was first posted, and the
arXiv v3 of 24 April 2026 is consistent with an ARR camera-ready for that conference. The
bibtex key `yang2025underspecification` encodes the preprint year and is now misleading;
renaming it to `yang2026underspecification` would make the key agree with the year, but that
touches every `\citet` site in the paper, so it is your call.

| Field | In the entry | Correct value |
|---|---|---|
| `year` | 2025 | **2026** |
| entry type | `@article` with `journal=` | `@inproceedings` with `booktitle=` |
| `pages` | absent | 9072--9101 |
| `doi` | absent | 10.18653/v1/2026.findings-acl.441 |

Note on the surname: the Anthology transliterates as "Kaestner"; arXiv and the author's own
usage give "Kästner". The entry's `K{\"a}stner` is the better form and should be kept.

Corrected entry:

```bibtex
@inproceedings{yang2025underspecification,
  title={What Prompts Don't Say: Understanding and Managing Underspecification in {LLM} Prompts},
  author={Yang, Chenyang and Shi, Yike and Ma, Qianou and Liu, Michael Xieyang and K{\"a}stner, Christian and Wu, Tongshuang},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  month={July},
  year={2026},
  address={San Diego, California, United States},
  publisher={Association for Computational Linguistics},
  pages={9072--9101},
  doi={10.18653/v1/2026.findings-acl.441},
  url={https://aclanthology.org/2026.findings-acl.441/}
}
```

---

## 13. `vasconcelos2023explanations` — VERIFIED

Current entry:

```bibtex
@article{vasconcelos2023explanations,
  title={Explanations Can Reduce Overreliance on {AI} Systems During Decision-Making},
  author={Vasconcelos, Helena and Jörke, Matthew and Grunde-McLaughlin, Madeleine and Gerstenberg, Tobias and Bernstein, Michael S. and Krishna, Ranjay},
  journal={Proceedings of the ACM on Human-Computer Interaction (CSCW)},
  year={2023},
  note={arXiv:2212.06823}
}
```

Evidence:

- `https://arxiv.org/abs/2212.06823`, retrieved 2026-09-05: title matches character for
  character, six authors in the entry's order, arXiv comment "CSCW 2023".
- Crossref, `https://api.crossref.org/works/10.1145/3579605`, retrieved 2026-09-05:

  > container: Proceedings of the ACM on Human-Computer Interaction
  > vol: 7 | issue: CSCW1 | page: 1-38 | issued: 2023-04-14 | publisher: ACM
  > authors: Helena Vasconcelos; Matthew Jörke; Madeleine Grunde-McLaughlin; Tobias Gerstenberg; Michael S. Bernstein; Ranjay Krishna

The ACM Digital Library page at `https://dl.acm.org/doi/10.1145/3579605` returned HTTP 403
behind a Cloudflare interstitial on 2026-09-05; Crossref's deposit for the same DOI was used
instead and agrees with arXiv on title and authorship.

Every field asserted in the entry is correct, including the author list (note that OpenAlex's
arXiv-derived record renders the fifth author as "Michael A. Bernstein"; both arXiv and the
published Crossref record give **Michael S. Bernstein**, which is what the entry has).

Optional additions, not corrections: `volume={7}`, `number={CSCW1}`, `pages={1--38}`,
`doi={10.1145/3579605}`. Adding at least the volume and DOI would help a reader find it,
since "CSCW" alone does not identify the issue.

---

## 14. `tyen2024llms` — VERIFIED

Current entry:

```bibtex
@article{tyen2024llms,
  title={{LLMs} Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location},
  author={Tyen, Gladys and Mansoor, Hassan and C{\u{a}}rbune, Victor and Chen, Peter and Mak, Tony},
  journal={Findings of the Association for Computational Linguistics: ACL 2024},
  year={2024},
  note={arXiv:2311.08516}
}
```

Evidence:

- `https://arxiv.org/abs/2311.08516`, retrieved 2026-09-05: authors Tyen, Mansoor, Cărbune,
  Chen, Mak; arXiv comment "ACL 2024 Findings"; v1 14 Nov 2023, v3 4 Jun 2024.
- ACL Anthology canonical BibTeX, `https://aclanthology.org/2024.findings-acl.826.bib`,
  retrieved 2026-09-05:

  ```
  booktitle = "Findings of the Association for Computational Linguistics: ACL 2024",
  month = aug, year = "2024", address = "Bangkok, Thailand",
  publisher = "Association for Computational Linguistics",
  pages = "13894--13908", doi = "10.18653/v1/2024.findings-acl.826"
  ```

The venue is right, the conference year is right, the author list and order are right, and
the arXiv ID is right. Classified VERIFIED.

Two observations that do not change the classification. The published title is in sentence
case, "LLMs cannot find reasoning errors, but can correct them given the error location";
the entry's title case is a styling choice. And the Anthology drops the diacritic, spelling
"Carbune, Victor", while arXiv gives "Cărbune"; the entry's `C{\u{a}}rbune` matches arXiv and
should be kept.

Optional additions: `pages={13894--13908}`, `doi={10.18653/v1/2024.findings-acl.826}`, and
switching to `@inproceedings` with `booktitle=` so that a Findings volume is not typeset as a
journal.

---

## 15. `chen2024overthinking` — FIELD ERRORS (preprint has since been published, under a changed title)

Current entry:

```bibtex
@article{chen2024overthinking,
  title={Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like {LLMs}},
  author={Chen, Xingyu and Xu, Jiahao and Liang, Tian and He, Zhiwei and Pang, Jianhui and Yu, Dian and Song, Linfeng and Liu, Qiuzhi and Zhou, Mengfei and Zhang, Zhuosheng and others},
  journal={arXiv preprint arXiv:2412.21187},
  year={2024}
}
```

Evidence:

- `https://arxiv.org/abs/2412.21187`, retrieved 2026-09-05: title "Do NOT Think That Much for
  2+3=? On the Overthinking of o1-Like LLMs", 14 authors, v1 30 Dec 2024, v2 1 Feb 2025.
- PMLR, `https://proceedings.mlr.press/v267/chen25bx.html`, retrieved 2026-09-05:

  > citation_title: Do NOT Think That Much for 2+3=? On the Overthinking of **Long Reasoning Models**
  > citation_conference_title: International Conference on Machine Learning
  > citation_firstpage: 9487 | citation_lastpage: 9499 | citation_publisher: PMLR
  > 14 authors, identical list and order to arXiv

- DBLP, retrieved 2026-09-05, holds both records:
  `https://dblp.org/rec/conf/icml/ChenXL0P0SLZ00T25` (ICML 2025) and
  `https://dblp.org/rec/journals/corr/abs-2412-21187` (CoRR 2024).

| Field | In the entry | Correct value |
|---|---|---|
| venue | arXiv preprint only | **Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)**, PMLR volume 267, pp. 9487–9499 |
| `title` | "... On the Overthinking of **o1-Like LLMs**" | The published version is retitled "... On the Overthinking of **Long Reasoning Models**". The entry's title is correct for the preprint only |

Every field the entry asserts is accurate *for the arXiv preprint*, so if you deliberately
intend to cite the preprint the entry is defensible. But the work is published, and the
published title differs, so citing the preprint means a reader searching your title will not
find the ICML paper. Recommend switching.

The four authors hidden behind `and others` are **Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong
Yu** (14 authors total; the ten named in the entry are correct and in order).

Corrected entry:

```bibtex
@inproceedings{chen2024overthinking,
  title={Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models},
  author={Chen, Xingyu and Xu, Jiahao and Liang, Tian and He, Zhiwei and Pang, Jianhui and Yu, Dian and Song, Linfeng and Liu, Qiuzhi and Zhou, Mengfei and Zhang, Zhuosheng and Wang, Rui and Tu, Zhaopeng and Mi, Haitao and Yu, Dong},
  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},
  series={Proceedings of Machine Learning Research},
  volume={267},
  pages={9487--9499},
  publisher={PMLR},
  year={2025},
  url={https://proceedings.mlr.press/v267/chen25bx.html},
  note={arXiv:2412.21187}
}
```

Note that adopting this makes the key year (2024) disagree with the publication year (2025),
the same situation as `wu2023style` below. Renaming keys is your call.

---

## 16. `wu2023style` — VERIFIED

Current entry:

```bibtex
@article{wu2023style,
  title={Style Over Substance: Evaluation Biases for Large Language Models},
  author={Wu, Minghao and Aji, Alham Fikri},
  journal={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},
  year={2025},
  note={arXiv:2307.03025}
}
```

Evidence:

- ACL Anthology canonical BibTeX, `https://aclanthology.org/2025.coling-main.21.bib`,
  retrieved 2026-09-05:

  ```bibtex
  @inproceedings{wu-aji-2025-style,
      title = "Style Over Substance: Evaluation Biases for Large Language Models",
      author = "Wu, Minghao and Aji, Alham Fikri",
      booktitle = "Proceedings of the 31st International Conference on Computational Linguistics",
      month = jan, year = "2025", address = "Abu Dhabi, UAE",
      publisher = "Association for Computational Linguistics",
      pages = "297--312"
  }
  ```

  The landing page `https://aclanthology.org/2025.coling-main.21/` returned HTTP 200 the same
  day with the matching title.
- `https://arxiv.org/abs/2307.03025`, retrieved 2026-09-05: same title, both authors, v1
  6 Jul 2023, v3 12 Nov 2023.

**The conference number was checked and is correct.** COLING 2025 (Abu Dhabi, January 2025)
is the 31st International Conference on Computational Linguistics, exactly as the entry
states, and `year=2025` matches. Title matches character for character; both authors correct.

Two things worth doing, neither an error. The entry is `@article` with a proceedings volume
in `journal=`, which will typeset a conference paper as a journal article; `@inproceedings`
with `booktitle=` is the right form. And `pages={297--312}` plus the Anthology URL are
available. Separately, the key `wu2023style` carries the preprint year while the entry
correctly says 2025; harmless, but it will read oddly to a reader who sees the key.

Suggested improved entry (field values unchanged, form corrected):

```bibtex
@inproceedings{wu2023style,
  title={Style Over Substance: Evaluation Biases for Large Language Models},
  author={Wu, Minghao and Aji, Alham Fikri},
  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},
  month={January},
  year={2025},
  address={Abu Dhabi, UAE},
  publisher={Association for Computational Linguistics},
  pages={297--312},
  url={https://aclanthology.org/2025.coling-main.21/},
  note={arXiv:2307.03025}
}
```

---

## 17. `lee2025refinebench` — VERIFIED

Current entry:

```bibtex
@article{lee2025refinebench,
  title={RefineBench: Evaluating Refinement Capability of Language Models via Checklists},
  author={Lee, Young-Jun and Kim, Seungone and Lee, Byung-Kwan and Moon, Minkyeong and Hwang, Yechan and Kim, Jong Myoung and Neubig, Graham and Welleck, Sean and Choi, Ho-Jin},
  journal={arXiv preprint arXiv:2511.22173},
  year={2025}
}
```

Evidence: `https://arxiv.org/abs/2511.22173`, retrieved 2026-09-05. Title matches character
for character. All nine authors match, in the entry's order: Lee, Young-Jun; Kim, Seungone;
Lee, Byung-Kwan; Moon, Minkyeong; Hwang, Yechan; Kim, Jong Myoung; Neubig, Graham; Welleck,
Sean; Choi, Ho-Jin. Single version, posted 27 Nov 2025, so `year=2025` is correct. arXiv ID
correct.

DBLP holds only the CoRR record (`https://dblp.org/rec/journals/corr/abs-2511-22173`,
retrieved 2026-09-05) and OpenAlex returns no published record, so the work is still a
preprint as of 2026-09-05 and the entry's treatment of it is correct. Given the November 2025
posting date, it is a candidate to be published between now and the October ARR deadline;
worth one re-check before submission.

---

## Summary table

| # | Key | Classification | Wrong fields |
|---|---|---|---|
| 1 | `wei2024simple` | FIELD ERRORS | author (3 people who are not authors, 1 author omitted), year |
| 2 | `sclar2024quantifying` | FIELD ERRORS | title (fabricated subtitle), venue (ICLR 2024, not preprint) |
| 3 | `zheng2024judging` | FIELD ERRORS | year (2024 → 2023); `and others` hides 3 authors |
| 4 | `zhou2024calibrated` | FIELD ERRORS | author (wrong surname on author 1; 3 non-authors; 0 of 2 real co-authors), venue (STOC 2024) |
| 5 | `white2023prompt` | VERIFIED | — (since also published at PLoP 2023) |
| 6 | `rafailov2023direct` | FIELD ERRORS | author order (Manning/Ermon; sources disagree, both reported) |
| 7 | `deloitte2026stateofai` | VERIFIED | — (access stamp 3 months old) |
| 8 | `copilot2025agentmode` | FIELD ERRORS | title, author/publisher attribution |
| 9 | `thoppilan2022lamda` | VERIFIED | — |
| 10 | `kamoi2024selfcorrection` | VERIFIED | — (prose claim "in TACL" confirmed correct) |
| 11 | `goldman2026tokens` | FIELD ERRORS | title (no such publication), author given name, no URL |
| 12 | `yang2025underspecification` | FIELD ERRORS | year (2025 → 2026); venue itself confirmed correct |
| 13 | `vasconcelos2023explanations` | VERIFIED | — |
| 14 | `tyen2024llms` | VERIFIED | — |
| 15 | `chen2024overthinking` | FIELD ERRORS | venue (published ICML 2025); published title differs |
| 16 | `wu2023style` | VERIFIED | — (31st COLING confirmed correct) |
| 17 | `lee2025refinebench` | VERIFIED | — |

## Counts

- VERIFIED: **8** (`white2023prompt`, `deloitte2026stateofai`, `thoppilan2022lamda`,
  `kamoi2024selfcorrection`, `vasconcelos2023explanations`, `tyen2024llms`, `wu2023style`,
  `lee2025refinebench`)
- FIELD ERRORS: **9** (`wei2024simple`, `sclar2024quantifying`, `zheng2024judging`,
  `zhou2024calibrated`, `rafailov2023direct`, `copilot2025agentmode`, `goldman2026tokens`,
  `yang2025underspecification`, `chen2024overthinking`)
- UNVERIFIABLE: **0**
- NOT FOUND: **0**
- Total: 17

Every one of the 17 works exists. No entry cites a nonexistent paper. The damage is
concentrated in author lists and titles: `zhou2024calibrated`, `wei2024simple`,
`sclar2024quantifying` and `goldman2026tokens` each assert something about authorship or
titling that the source does not support, and those four are the ones to fix first.
