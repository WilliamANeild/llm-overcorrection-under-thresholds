# Bibliography audit — chunk 1 (17 entries)

Source file: `/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/references.bib`
Auditor pass date: **2026-09-05** (all retrieval dates below are 2026-09-05 unless stated otherwise)
Scope: the 17 keys listed below only. No other entry in `references.bib` was examined, and no file other than this one was written.

Conventions used here:

- **VERIFIED** — every present field was checked against a fetched source and is correct. A "Completeness note" under a VERIFIED entry flags a field that is *absent* but would be worth adding; an absent field is not counted as an error.
- **FIELD ERRORS** — the work is real but at least one present field carries a wrong value, or the entry describes the work's publication status incorrectly (preprint that has since appeared in a venue, superseded title).

---

## 1. `perez2023discovering`

**Current entry:**

```bibtex
@inproceedings{perez2023discovering,
  title={Discovering Language Model Behaviors with Model-Written Evaluations},
  author={Perez, Ethan and Ringer, Sam and Luko{\v{s}}i{\=u}t{\.e}, Kamil{\.e} and Nguyen, Karina and Chen, Edwin and Heiner, Scott and Pettit, Craig and Olsson, Catherine and Kundu, Sandipan and Kadavath, Saurav and others},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2023},
  pages={13387--13434},
  year={2023}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://aclanthology.org/2023.findings-acl.847/ — retrieved 2026-09-05
- https://aclanthology.org/2023.findings-acl.847.bib (official Anthology BibTeX) — retrieved 2026-09-05

Title matches character for character. Venue "Findings of the Association for Computational Linguistics: ACL 2023" matches. Pages 13387–13434 match. Year 2023 matches. The first ten authors in the entry match the Anthology order exactly (Perez, Ringer, Lukosiute, Nguyen, Chen, Heiner, Pettit, Olsson, Kundu, Kadavath); the `and others` conceals 54 further authors ending with Jared Kaplan, which is a legitimate truncation, not an error. The Anthology renders the third author unaccented as "Lukosiute"; the entry's diacritics ("Lukošiūtė, Kamilė") are the correct rendering used by the author herself and are not an error.

**Completeness note (not an error):** DOI `10.18653/v1/2023.findings-acl.847` and publisher/address are absent.

---

## 2. `lu2022fantastically`

**Current entry:**

```bibtex
@inproceedings{lu2022fantastically,
  title={Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity},
  author={Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp, Pontus},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics},
  pages={8086--8098},
  year={2022}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://aclanthology.org/2022.acl-long.556/ — retrieved 2026-09-05
- https://aclanthology.org/2022.acl-long.556.bib (official Anthology BibTeX) — retrieved 2026-09-05

Title matches character for character. Full author list matches (5 authors, correct order). Conference **number 60** and **year 2022** both correct — this is the class of error the audit targets, and it is clean here. Pages 8086–8098 match.

**Completeness note (not an error):** the Anthology booktitle is "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)". The entry omits the volume qualifier. Nothing in the entry is wrong; adding "(Volume 1: Long Papers)" would make it exact. DOI `10.18653/v1/2022.acl-long.556` is also absent.

---

## 3. `madaan2024self`

**Current entry:**

```bibtex
@article{madaan2024self,
  title={Self-Refine: Iterative Refinement with Self-Feedback},
  author={Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and others},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
}
```

**Classification: FIELD ERRORS**

**Evidence:**
- https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html — retrieved 2026-09-05
- https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Bibtex-Conference.bib (official NeurIPS BibTeX) — retrieved 2026-09-05
- https://neurips.cc/virtual/2023/poster/71632 — retrieved 2026-09-05

Errors found:

| Field | Entry value | Correct value |
|---|---|---|
| `year` | `2024` | `2023` — the paper is in the NeurIPS **2023** proceedings; the official NeurIPS BibTeX states `year = {2023}` |
| entry type | `@article` | `@inproceedings` — official NeurIPS BibTeX uses `@inproceedings` |
| `pages` | absent | `46534--46594` |

Title, the first ten authors, and `volume={36}` are correct. The `and others` conceals six further authors (Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark), a legitimate truncation.

**Corrected entry (year kept in the key to avoid breaking existing `\cite` calls):**

```bibtex
@inproceedings{madaan2024self,
  title={Self-Refine: Iterative Refinement with Self-Feedback},
  author={Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and others},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  pages={46534--46594},
  publisher={Curran Associates, Inc.},
  year={2023}
}
```

---

## 4. `panickssery2024llm`

**Current entry:**

```bibtex
@article{panickssery2024llm,
  title={{LLM} Evaluators Recognize and Favor Their Own Generations},
  author={Panickssery, Arjun and Bowman, Samuel R and Feng, Shi},
  journal={arXiv preprint arXiv:2404.13076},
  year={2024}
}
```

**Classification: FIELD ERRORS**

**Evidence:**
- https://arxiv.org/abs/2404.13076 — retrieved 2026-09-05 (confirms title, three authors, 2024, arXiv ID; the abs page shows no journal reference)
- https://proceedings.neurips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html — retrieved 2026-09-05
- https://proceedings.neurips.cc/paper_files/paper/2024/file/7f1f0218e45f5414c79c0679633e47bc-Bibtex-Conference.bib (official NeurIPS BibTeX) — retrieved 2026-09-05

The error is publication status. The work is cited as an arXiv preprint but appeared in **Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Main Conference Track, pages 68772–68802**. The arXiv abstract page carries no journal-reference field, which is why the preprint citation looks defensible; the NeurIPS proceedings record is definitive.

| Field | Entry value | Correct value |
|---|---|---|
| entry type / `journal` | `@article`, `journal={arXiv preprint arXiv:2404.13076}` | `@inproceedings`, `booktitle={Advances in Neural Information Processing Systems}`, `volume={37}` |
| `pages` | absent | `68772--68802` |

Title, author list (three authors, correct order), and year 2024 are correct.

**Corrected entry:**

```bibtex
@inproceedings{panickssery2024llm,
  title={{LLM} Evaluators Recognize and Favor Their Own Generations},
  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},
  booktitle={Advances in Neural Information Processing Systems},
  volume={37},
  pages={68772--68802},
  publisher={Curran Associates, Inc.},
  year={2024}
}
```

---

## 5. `openai2025prompting`

**Current entry:**

```bibtex
@misc{openai2025prompting,
  title={{GPT}-5 Prompting Guide},
  author={{OpenAI}},
  year={2025},
  howpublished={\url{https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide}},
  note={Accessed 2026-03-31}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide — fetched and confirmed live, **retrieved 2026-09-05**. Page title renders as "GPT-5 prompting guide". Content is an official OpenAI developer guide to prompting GPT-5, covering agentic-behavior control, coding performance, and instruction adherence.
- https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide — retrieved 2026-09-05. This older canonical address now returns **HTTP 308 Permanent Redirect** to the `developers.openai.com` URL already in the entry. The entry therefore already points at the current location; no URL change is needed.
- Publication date August 7, 2025 (reported by secondary sources; the page itself displays no date). Year 2025 is consistent with the GPT-5 launch and with the page's content.

The URL resolves, the page exists, and it says what the entry claims. Case differs between the entry's "Prompting Guide" and the page's rendered "prompting guide"; this is title-case styling, not a factual error.

**Completeness note (not an error):** the byline on the cookbook page names Anoop Kotha, Julian Lee, Eric Zakariasson and Erin Kavanaugh. Crediting `{OpenAI}` as corporate author is standard for vendor documentation and is left as the author's call. The `note` records an access date of 2026-03-31; consider refreshing it to 2026-09-05, the date the page was re-fetched for this audit.

---

## 6. `ouyang2022training`

**Current entry:**

```bibtex
@article{ouyang2022training,
  title={Training Language Models to Follow Instructions with Human Feedback},
  author={Ouyang, Long and Wu, Jeffrey and Jiang, Xu and Almeida, Diogo and Wainwright, Carroll and Mishkin, Pamela and Zhang, Chong and Agarwal, Sandhini and Slama, Katarina and Ray, Alex and others},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  pages={27730--27744},
  year={2022}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html — retrieved 2026-09-05
- https://proceedings.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Bibtex-Conference.bib (official NeurIPS BibTeX) — retrieved 2026-09-05

Volume 35, pages 27730–27744, year 2022 all match the official NeurIPS record exactly. The first ten authors match the official order (Ouyang, Wu, Jiang, Almeida, Wainwright, Mishkin, Zhang, Agarwal, Slama, Ray); `and others` conceals ten more, ending with Ryan Lowe. Note that the official record gives "Wainwright, Carroll" without a middle initial, matching the entry (some secondary indexes render "Carroll L. Wainwright"); the entry follows the proceedings.

The title is printed in sentence case in the proceedings ("Training language models to follow instructions with human feedback"); the entry's title case is a styling choice, not a factual error.

**Completeness note (not an error):** `@article` is used for what the proceedings record as `@inproceedings`. This is the same structural issue as `madaan2024self`, but here no field value is wrong, so it is not counted as an error. DOI `10.52202/068431-2011` is absent.

---

## 7. `liang2023holistic`

**Current entry:**

```bibtex
@article{liang2023holistic,
  title={Holistic Evaluation of Language Models},
  author={Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and others},
  journal={Transactions on Machine Learning Research},
  year={2023}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://arxiv.org/abs/2211.09110 — retrieved 2026-09-05. First twelve authors in order: Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, Benjamin Newman, Binhang Yuan.
- https://arxiv.org/abs/2211.09110v2 — retrieved 2026-09-05. Journal reference reads: "Published in Transactions on Machine Learning Research (TMLR), 2023".
- The published PDF header reads "Published in Transactions on Machine Learning Research (08/2023)" (https://openreview.net/pdf/1882e7aa18c29c4487d64455658f6498456bc0dc.pdf, seen 2026-09-05).

Title, first ten authors in order, journal, and year 2023 all correct. TMLR does not assign volume or page numbers, so their absence is correct.

---

## 8. `chen2025overthinking`

**Current entry:**

```bibtex
@article{chen2025overthinking,
  title={Stop Spinning Wheels: Mitigating {LLM} Overthinking},
  author={Chen, Haotian and Zheng, Chuanyang and Zhu, Zhengying and Calandriello, Daniele and Lakshminarayanan, Balaji and others},
  journal={arXiv preprint arXiv:2508.17627},
  year={2025}
}
```

**Classification: FIELD ERRORS** (severe — the author list does not correspond to the cited work)

**Evidence:**
- https://arxiv.org/abs/2508.17627 — retrieved 2026-09-05. Current (v2, revised 2026-01-13) title: **"The Evolution of Thought: Tracking LLM Overthinking via Reasoning Dynamics Analysis"**. Authors: Zihao Wei, Liang Pang, Jiahao Liu, Wenjie Shi, Jingcheng Deng, Shicheng Xu, Zenghao Duan, Fei Sun, Huawei Shen, Xueqi Cheng. No journal reference.
- https://arxiv.org/abs/2508.17627v1 — retrieved 2026-09-05. v1 (2025-08-25) title: **"Stop Spinning Wheels: Mitigating LLM Overthinking via Mining Patterns for Early Reasoning Exit"**. Authors: Zihao Wei, Liang Pang, Jiahao Liu, Jingcheng Deng, Shicheng Xu, Zenghao Duan, Jingang Wang, Fei Sun, Xunliang Cai, Huawei Shen, Xueqi Cheng.

Errors found:

| Field | Entry value | Correct value |
|---|---|---|
| `author` | `Chen, Haotian and Zheng, Chuanyang and Zhu, Zhengying and Calandriello, Daniele and Lakshminarayanan, Balaji and others` | **None of these five people is an author of arXiv:2508.17627, in any version.** The v1 author list is Wei, Pang, Liu, Deng, Xu, Duan, Wang, Sun, Cai, Shen, Cheng; the v2 list is Wei, Pang, Liu, Shi, Deng, Xu, Duan, Sun, Shen, Cheng. The first author is Zihao Wei, not Haotian Chen. |
| `title` | `Stop Spinning Wheels: Mitigating {LLM} Overthinking` | v1: `Stop Spinning Wheels: Mitigating {LLM} Overthinking via Mining Patterns for Early Reasoning Exit` (the entry truncates the subtitle). The current version is retitled `The Evolution of Thought: Tracking {LLM} Overthinking via Reasoning Dynamics Analysis`. |

This is the most serious problem in the chunk. The citation key `chen2025overthinking` and the author list appear to have been assembled independently of the arXiv record. Two sources disagree only about the title, and they are the two versions of the same preprint, so the author should decide which version the paper cites; the author list is wrong under either choice. The arXiv ID and year 2025 are correct, and the work is still an unpublished preprint (no journal reference on arXiv as of 2026-09-05).

**Corrected entry — citing the current version (v2), recommended:**

```bibtex
@article{chen2025overthinking,
  title={The Evolution of Thought: Tracking {LLM} Overthinking via Reasoning Dynamics Analysis},
  author={Wei, Zihao and Pang, Liang and Liu, Jiahao and Shi, Wenjie and Deng, Jingcheng and Xu, Shicheng and Duan, Zenghao and Sun, Fei and Shen, Huawei and Cheng, Xueqi},
  journal={arXiv preprint arXiv:2508.17627},
  year={2025}
}
```

**Corrected entry — if the paper's argument relies on the v1 text specifically:**

```bibtex
@article{chen2025overthinking,
  title={Stop Spinning Wheels: Mitigating {LLM} Overthinking via Mining Patterns for Early Reasoning Exit},
  author={Wei, Zihao and Pang, Liang and Liu, Jiahao and Deng, Jingcheng and Xu, Shicheng and Duan, Zenghao and Wang, Jingang and Sun, Fei and Cai, Xunliang and Shen, Huawei and Cheng, Xueqi},
  journal={arXiv preprint arXiv:2508.17627v1},
  year={2025}
}
```

If the key is changed to match the true first author (`wei2025overthinking`), every `\cite{chen2025overthinking}` in the manuscript must be updated. That is the author's decision; nothing has been changed here.

---

## 9. `goodhart1984problems`

**Current entry:**

```bibtex
@article{goodhart1984problems,
  title={Problems of Monetary Management: The {U.K.} Experience},
  author={Goodhart, Charles A. E.},
  journal={Monetary Theory and Practice},
  pages={91--121},
  year={1984},
  publisher={Palgrave, London}
}
```

**Classification: FIELD ERRORS** (minor)

**Evidence:**
- https://api.crossref.org/works/10.1007/978-1-349-17295-5_4 (Crossref REST API record) — retrieved 2026-09-05. Title: "Problems of Monetary Management: The UK Experience". Author: C. A. E. Goodhart. Container: "Monetary Theory and Practice". Publisher: Macmillan Education UK. Pages: 91-121. Year: 1984. DOI: 10.1007/978-1-349-17295-5_4.
- https://link.springer.com/chapter/10.1007/978-1-349-17295-5_4 — attempted 2026-09-05; Springer returned HTTP 303 to an authentication endpoint, so the landing page itself could not be read. The Crossref record for the same DOI is the authority used above.
- Full book title confirmed as "Monetary Theory and Practice: The UK Experience" from library and retail catalogue listings (HathiTrust record 000324283; Amazon ISBN 9780333360606), seen 2026-09-05.

The work exists, and pages 91–121 and year 1984 are both correct.

| Field | Entry value | Correct value |
|---|---|---|
| `title` | `Problems of Monetary Management: The {U.K.} Experience` | `Problems of Monetary Management: The {UK} Experience` — Crossref and the book both render "UK" without periods |
| `publisher` | `Palgrave, London` | Crossref gives **Macmillan Education UK**. The 1984 first edition was published by Macmillan, London; the Springer/Palgrave Macmillan digital reissue is where the DOI comes from. **Two sources disagree**, and both are reported: cite Macmillan if citing the 1984 book, Palgrave Macmillan if citing the digitized chapter. |
| entry type | `@article` with `journal=` | `@incollection` with `booktitle=` — this is a book chapter, not a journal article, and the book title in the entry is truncated ("Monetary Theory and Practice" rather than "Monetary Theory and Practice: The UK Experience") |

**Corrected entry:**

```bibtex
@incollection{goodhart1984problems,
  title={Problems of Monetary Management: The {UK} Experience},
  author={Goodhart, Charles A. E.},
  booktitle={Monetary Theory and Practice: The {UK} Experience},
  pages={91--121},
  year={1984},
  publisher={Macmillan},
  address={London},
  doi={10.1007/978-1-349-17295-5_4}
}
```

---

## 10. `singhal2023long`

**Current entry:**

```bibtex
@article{singhal2023long,
  title={A Long Way to Go: Investigating Length Correlations in {RLHF}},
  author={Singhal, Prasann and Goyal, Tanya and Xu, Jiacheng and Durrett, Greg},
  journal={arXiv preprint arXiv:2310.03716},
  year={2023}
}
```

**Classification: FIELD ERRORS**

**Evidence:**
- https://arxiv.org/abs/2310.03716 — retrieved 2026-09-05. Title, four authors and 2023 submission all confirmed. The comments field states **"Accepted to COLM 2024"**.
- https://arxiv.org/pdf/2310.03716 — retrieved 2026-09-05. The PDF header reads "Published as a conference paper at COLM 2024".

The error is publication status: cited as a preprint, but the work appeared at the **Conference on Language Modeling (COLM) 2024**. Title, full author list and arXiv ID are all correct.

| Field | Entry value | Correct value |
|---|---|---|
| entry type / `journal` | `@article`, `journal={arXiv preprint arXiv:2310.03716}` | `@inproceedings`, `booktitle={Proceedings of the First Conference on Language Modeling (COLM)}`, `year={2024}` |

**Corrected entry (key left unchanged to avoid breaking `\cite` calls; note the year field now reads 2024 while the key says 2023):**

```bibtex
@inproceedings{singhal2023long,
  title={A Long Way to Go: Investigating Length Correlations in {RLHF}},
  author={Singhal, Prasann and Goyal, Tanya and Xu, Jiacheng and Durrett, Greg},
  booktitle={Proceedings of the First Conference on Language Modeling (COLM)},
  year={2024},
  note={arXiv:2310.03716}
}
```

---

## 11. `menlo2025llmmarket`

**Current entry:**

```bibtex
@misc{menlo2025llmmarket,
  title={2025 Mid-Year {LLM} Market Update},
  author={{Menlo Ventures}},
  year={2025},
  howpublished={\url{https://menlovc.com/2025-mid-year-llm-market-update/}},
  note={Survey of 150 technical leaders. Accessed 2026-06-10}
}
```

**Classification: FIELD ERRORS** (minor)

**Evidence:**
- https://menlovc.com/2025-mid-year-llm-market-update/ — fetched and confirmed live, **retrieved 2026-09-05**. Page title: "2025 Mid-Year LLM Market Update: Foundation Model Landscape + Economics". Publisher: Menlo Ventures. Publication date: **July 31, 2025**. The page describes a survey of **"over 150 technical leaders"**, fielded June 30 to July 10, 2025, among technical decision-makers at enterprises (5,000+ employees) and startups that had raised at least $5 million, weighted by application scale.

The URL resolves, the page exists, and it broadly says what the entry claims.

| Field | Entry value | Correct value |
|---|---|---|
| `title` | `2025 Mid-Year {LLM} Market Update` | `2025 Mid-Year {LLM} Market Update: Foundation Model Landscape + Economics` — the entry truncates the subtitle |
| `note` | `Survey of 150 technical leaders` | The page says **"over 150"**, not 150. If any number in the manuscript is sourced to this survey's sample size, it should read "over 150" or be recast; "150" understates and misquotes the source. |

Year 2025 and the corporate author are correct.

**Corrected entry:**

```bibtex
@misc{menlo2025llmmarket,
  title={2025 Mid-Year {LLM} Market Update: Foundation Model Landscape + Economics},
  author={{Menlo Ventures}},
  year={2025},
  howpublished={\url{https://menlovc.com/2025-mid-year-llm-market-update/}},
  note={Published 31 July 2025. Survey of over 150 technical leaders, fielded 30 June--10 July 2025. Accessed 2026-09-05}
}
```

---

## 12. `ghosal2025overthinking`

**Current entry:**

```bibtex
@article{ghosal2025overthinking,
  title={Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models},
  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Reddy, Avinash and Lu, Yifu and Wang, Mengdi and Manocha, Dinesh and Huang, Furong and Ghavamzadeh, Mohammad and Bedi, Amrit Singh},
  journal={arXiv preprint arXiv:2506.04210},
  year={2025}
}
```

**Classification: FIELD ERRORS**

**Evidence:**
- https://arxiv.org/abs/2506.04210 — retrieved 2026-09-05. Nine authors in the order given, 2025, arXiv ID confirmed. Comments field: **"Accepted at NeurIPS 2025"**. The arXiv title styles the third word lowercase: "Does Thinking More always Help?".
- https://proceedings.neurips.cc/paper_files/paper/2025/hash/fc067ac218430c409d6f65403328f740-Abstract-Conference.html — retrieved 2026-09-05
- https://proceedings.neurips.cc/paper_files/paper/2025/file/fc067ac218430c409d6f65403328f740-Bibtex-Conference.bib (official NeurIPS BibTeX) — retrieved 2026-09-05. Title as published: "Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models". Volume "38, Main Conference". Pages 172664–172691. Year 2025.

The full author list matches the official NeurIPS record exactly, in order. The entry's title matches the **published** NeurIPS title character for character (the arXiv version's lowercase "always" is the outlier, and the published form is the one to cite). The error is publication status only.

| Field | Entry value | Correct value |
|---|---|---|
| entry type / `journal` | `@article`, `journal={arXiv preprint arXiv:2506.04210}` | `@inproceedings`, `booktitle={Advances in Neural Information Processing Systems}`, `volume={38}` |
| `pages` | absent | `172664--172691` |

**Corrected entry:**

```bibtex
@inproceedings{ghosal2025overthinking,
  title={Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models},
  author={Ghosal, Soumya Suvra and Chakraborty, Souradip and Reddy, Avinash and Lu, Yifu and Wang, Mengdi and Manocha, Dinesh and Huang, Furong and Ghavamzadeh, Mohammad and Bedi, Amrit Singh},
  booktitle={Advances in Neural Information Processing Systems},
  volume={38},
  pages={172664--172691},
  publisher={Curran Associates, Inc.},
  year={2025}
}
```

---

## 13. `bansal2021whole`

**Current entry:**

```bibtex
@inproceedings{bansal2021whole,
  title={Does the Whole Exceed its Parts? The Effect of {AI} Explanations on Complementary Team Performance},
  author={Bansal, Gagan and Wu, Tongshuang and Zhou, Joyce and Fok, Raymond and Nushi, Besmira and Kamar, Ece and Ribeiro, Marco Tulio and Weld, Daniel},
  booktitle={Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems},
  year={2021},
  doi={10.1145/3411764.3445717}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://api.crossref.org/works/10.1145/3411764.3445717 (Crossref REST API record) — retrieved 2026-09-05. Title, all eight authors in the order given, container-title "Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems", publisher ACM, pages 1-16, year 2021, DOI 10.1145/3411764.3445717.
- https://idl.cs.washington.edu/files/2021-AIExplanationsTeamPerformance-CHI.pdf — retrieved 2026-09-05, downloaded and text-extracted. Printed author block confirms all eight authors in the entry's order. The ACM Reference Format block prints: "In CHI Conference on Human Factors in Computing Systems (CHI '21), May 8–13, 2021, Yokohama, Japan. ACM, New York, NY, USA, 16 pages. https://doi.org/10.1145/3411764.3445717".
- https://dl.acm.org/doi/10.1145/3411764.3445717 — attempted 2026-09-05, returned HTTP 403; Crossref and the author-hosted camera-ready PDF were used instead.

Title, all eight authors, venue, year 2021 and DOI are all correct. Note the published title spells "Effect" correctly; the PDF's rendered text drops the "f" ("Efect") as a font-ligature artifact of the extraction, not a real title variant. Crossref confirms "Effect".

**Completeness notes (not errors):** `pages={1--16}` (Crossref) could be added. The printed PDF byline gives the last author as **Daniel S. Weld** with a middle initial, while Crossref and the ACM record give **Daniel Weld**; the entry follows Crossref. Reported as a source disagreement, not an error.

---

## 14. `parasuraman2010complacency`

**Current entry:**

```bibtex
@article{parasuraman2010complacency,
  title={Complacency and Bias in Human Use of Automation: An Attentional Integration},
  author={Parasuraman, Raja and Manzey, Dietrich H.},
  journal={Human Factors},
  volume={52},
  number={3},
  pages={381--410},
  year={2010}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://api.crossref.org/works/10.1177/0018720810376055 (Crossref REST API record) — retrieved 2026-09-05. Title, both authors, journal "Human Factors: The Journal of the Human Factors and Ergonomics Society", volume 52, issue 3, pages 381-410, year 2010, DOI 10.1177/0018720810376055.
- https://journals.sagepub.com/doi/10.1177/0018720810376055 — attempted 2026-09-05, returned HTTP 403; the Crossref record for the same DOI was used instead.

Title character for character, both authors, volume 52, number 3, pages 381–410, year 2010 all correct.

**Completeness note (not an error):** DOI `10.1177/0018720810376055` is absent. The journal's full registered name is "Human Factors: The Journal of the Human Factors and Ergonomics Society"; the entry's "Human Factors" is the standard short form used in citation practice and is not an error.

---

## 15. `tsui2025selfcorrection`

**Current entry:**

```bibtex
@article{tsui2025selfcorrection,
  title={Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in {LLMs}},
  author={Tsui, Ken},
  journal={arXiv preprint arXiv:2507.02778},
  year={2025}
}
```

**Classification: FIELD ERRORS**

**Evidence:**
- https://arxiv.org/abs/2507.02778 — retrieved 2026-09-05. Current title: **"Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models"**. Sole author Ken Tsui. First submitted 3 July 2025, revised through 2 August 2026. Comments field: **"Accepted to COLM 2026"**.
- https://arxiv.org/abs/2507.02778v1 — retrieved 2026-09-05. v1 title: "Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in LLMs" — this matches the entry exactly, confirming the entry was written against v1.

Two issues, both consequences of the preprint having been revised and accepted since the entry was written.

| Field | Entry value | Correct value |
|---|---|---|
| `title` | `Self-Correction Bench: Revealing and Addressing the Self-Correction Blind Spot in {LLMs}` | `Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models` — "Revealing" became "Uncovering" and "LLMs" was expanded, as of v2 |
| entry type / `journal` | `@article`, `journal={arXiv preprint arXiv:2507.02778}` | `@inproceedings`, `booktitle={Proceedings of the Conference on Language Modeling (COLM)}`, `year={2026}` |

The v1 title in the entry is not fabricated: it was correct when written. Both titles are reported since the two arXiv versions disagree, but the current published form is the one to cite.

**Corrected entry:**

```bibtex
@inproceedings{tsui2025selfcorrection,
  title={Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models},
  author={Tsui, Ken},
  booktitle={Proceedings of the Conference on Language Modeling (COLM)},
  year={2026},
  note={arXiv:2507.02778}
}
```

COLM 2026 has not yet convened as of this audit, so no proceedings page numbers exist. If the author prefers to cite the preprint until the proceedings appear, keep `@article` but update the title to the current version.

---

## 16. `xu2024earth`

**Current entry:**

```bibtex
@inproceedings{xu2024earth,
  title={The Earth is Flat because...: Investigating {LLMs}' Belief towards Misinformation via Persuasive Conversation},
  author={Xu, Rongwu and Lin, Brian S. and Yang, Shujian and Zhang, Tianqi and Shi, Weiyan and Zhang, Tianwei and Fang, Zhixuan and Xu, Wei and Qiu, Han},
  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2024},
  note={arXiv:2312.09085}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://aclanthology.org/2024.acl-long.858/ — retrieved 2026-09-05
- https://aclanthology.org/2024.acl-long.858.bib (official Anthology BibTeX) — retrieved 2026-09-05
- https://arxiv.org/abs/2312.09085 — arXiv ID confirmed as the preprint of this paper, seen 2026-09-05

Title matches character for character. All nine authors present in the correct order. Conference **number 62** and **year 2024** both correct. arXiv ID in the note is correct.

**Source disagreement (reported, not an error):** the ACL Anthology renders the second author as **"Lin, Brian"**; the arXiv record and the paper's own GitHub repository render **"Brian S. Lin"**. The entry follows the arXiv form. Either is defensible; the Anthology form is the published one.

**Completeness notes (not errors):** the Anthology booktitle is "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)" — the entry's parenthetical "(ACL)" is a non-standard substitute for the volume qualifier but names the right venue. `pages={16259--16303}`, `address={Bangkok, Thailand}` and `doi={10.18653/v1/2024.acl-long.858}` are absent.

---

## 17. `chen2024humans`

**Current entry:**

```bibtex
@inproceedings{chen2024humans,
  title={Humans or {LLMs} as the Judge? A Study on Judgement Bias},
  author={Chen, Guiming Hardy and Chen, Shunian and Liu, Ziche and Jiang, Feng and Wang, Benyou},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  year={2024},
  note={arXiv:2402.10669}
}
```

**Classification: VERIFIED**

**Evidence:**
- https://aclanthology.org/2024.emnlp-main.474/ — retrieved 2026-09-05
- https://aclanthology.org/2024.emnlp-main.474.bib (official Anthology BibTeX) — retrieved 2026-09-05
- https://arxiv.org/abs/2402.10669 — arXiv ID confirmed as the preprint of this paper, seen 2026-09-05

Title matches the published Anthology title character for character. All five authors present in the correct order. Venue and year 2024 correct. arXiv ID in the note is correct.

**Source disagreement (reported, not an error):** the arXiv record titles the paper "A Study on Judgement **Biases**" (plural); the published EMNLP version uses "Judgement **Bias**" (singular). The entry follows the published form, which is correct.

**Completeness notes (not errors):** the Anthology booktitle is "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing" without the trailing "(EMNLP)"; the addition is harmless. `pages={8301--8327}`, `address={Miami, Florida, USA}` and `doi={10.18653/v1/2024.emnlp-main.474}` are absent.

---

## Summary table

| # | Key | Classification | Nature of the problem |
|---|---|---|---|
| 1 | `perez2023discovering` | VERIFIED | — |
| 2 | `lu2022fantastically` | VERIFIED | — |
| 3 | `madaan2024self` | FIELD ERRORS | Year 2024 should be 2023; missing pages; `@article` for a proceedings paper |
| 4 | `panickssery2024llm` | FIELD ERRORS | Cited as preprint; published at NeurIPS 2024, vol. 37, pp. 68772–68802 |
| 5 | `openai2025prompting` | VERIFIED | — (URL live; access date could be refreshed) |
| 6 | `ouyang2022training` | VERIFIED | — |
| 7 | `liang2023holistic` | VERIFIED | — |
| 8 | `chen2025overthinking` | FIELD ERRORS | **Author list wholly wrong** — none of the five named people wrote arXiv:2508.17627; title truncated and since superseded |
| 9 | `goodhart1984problems` | FIELD ERRORS | "U.K." should be "UK"; publisher disputed (Macmillan vs Palgrave); book chapter typed as `@article` with truncated book title |
| 10 | `singhal2023long` | FIELD ERRORS | Cited as preprint; published at COLM 2024 |
| 11 | `menlo2025llmmarket` | FIELD ERRORS | Title truncated; note says "150 technical leaders", the source says "over 150" |
| 12 | `ghosal2025overthinking` | FIELD ERRORS | Cited as preprint; published at NeurIPS 2025, vol. 38, pp. 172664–172691 |
| 13 | `bansal2021whole` | VERIFIED | — |
| 14 | `parasuraman2010complacency` | VERIFIED | — |
| 15 | `tsui2025selfcorrection` | FIELD ERRORS | Title superseded ("Revealing" to "Uncovering", "LLMs" expanded); accepted to COLM 2026 |
| 16 | `xu2024earth` | VERIFIED | — (Anthology gives "Brian Lin", arXiv "Brian S. Lin"; both reported) |
| 17 | `chen2024humans` | VERIFIED | — |

## Counts

| Classification | Count |
|---|---|
| VERIFIED | 9 |
| FIELD ERRORS | 8 |
| UNVERIFIABLE | 0 |
| NOT FOUND | 0 |
| **Total** | **17** |

Every one of the 17 works exists and was located at a source that was actually fetched. Three URLs refused direct access (ACM Digital Library, SAGE Journals, and SpringerLink, all HTTP 403 or a redirect to an authentication endpoint); in each case an independent authoritative record was fetched instead — the Crossref REST API for all three, plus the authors' own camera-ready PDF for the CHI paper.

Five of the eight FIELD ERRORS are the same class of problem: a work cited as an arXiv preprint that has since appeared in a venue (`panickssery2024llm`, `singhal2023long`, `ghosal2025overthinking`, `tsui2025selfcorrection`), or whose preprint has been revised and retitled (`tsui2025selfcorrection`, `chen2025overthinking`). Any other preprint entry in `references.bib` outside this chunk is worth re-checking for the same reason before submission.

No file other than this one was created or modified.
