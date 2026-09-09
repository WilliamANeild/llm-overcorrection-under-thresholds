# Bibliography audit, chunk 4

Source file: `/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/references.bib`
Auditor pass date: **2026-09-05** (all retrieval dates below are 2026-09-05 unless stated)
Scope: the 16 keys listed below only. No other entry was examined, and no file other than this one was written.

Every classification below rests on a page that was actually fetched. Where a claim rests
only on a search-engine summary, the entry is marked UNVERIFIABLE and the attempt is
described.

---

## 1. `ranaldi2023large` — FIELD ERRORS

Current entry:

```bibtex
@article{ranaldi2023large,
  title={When Large Language Models Contradict Humans and When They Do Not},
  author={Ranaldi, Leonardo and Pucci, Giulia},
  journal={arXiv preprint arXiv:2311.12193},
  year={2023}
}
```

**Evidence**

- https://arxiv.org/abs/2311.12193 (retrieved 2026-09-05). This identifier does **not** belong to
  the cited work. It is "Disentangling Structure and Appearance in ViT Feature Space" by Narek
  Tumanyan, Omer Bar-Tal, Shir Amir, Shai Bagon, Tali Dekel, submitted 20 Nov 2023, accepted to
  ACM Transactions on Graphics, DOI 10.1145/3630096. A computer-vision paper on semantic
  appearance transfer, unrelated in every respect.
- https://arxiv.org/abs/2311.09410 (retrieved 2026-09-05). Title line: "When Large Language Models
  contradict humans? Large Language Models' Sycophantic Behaviour". Authors: Leonardo Ranaldi,
  Giulia Pucci. v1 submitted Wed, 15 Nov 2023; v4 Tue, 24 Jun 2025.
- https://dblp.org/search/publ/api?q=When+Large+Language+Models+contradict+humans+Sycophantic&format=json
  (retrieved 2026-09-05). Single record, venue CoRR, abs/2311.09410, 2023, DOI 10.48550/ARXIV.2311.09410.
  No conference or journal version is indexed, so the preprint designation is correct.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `title` | When Large Language Models Contradict Humans and When They Do Not | When Large Language Models contradict humans? Large Language Models' Sycophantic Behaviour |
| arXiv ID in `journal` | arXiv:2311.12193 | arXiv:2311.09410 |

Authors and year are correct. The work is still a preprint as of 2026-09-05.

**Corrected entry**

```bibtex
@article{ranaldi2023large,
  title={When Large Language Models contradict humans? Large Language Models' Sycophantic Behaviour},
  author={Ranaldi, Leonardo and Pucci, Giulia},
  journal={arXiv preprint arXiv:2311.09410},
  year={2023}
}
```

---

## 2. `mizrahi2024state` — FIELD ERRORS

Current entry:

```bibtex
@article{mizrahi2024state,
  title={State of What Art? A Call for Multi-Prompt {LLM} Evaluation},
  author={Mizrahi, Moran and Stengel-Eskin, Elias and Chari, Abhishek and Ringel, Yonatan and Melamud, Oren and Van Durme, Benjamin},
  journal={Transactions of the Association for Computational Linguistics},
  volume={12},
  pages={933--949},
  year={2024}
}
```

**Evidence**

- https://aclanthology.org/2024.tacl-1.52/ (retrieved 2026-09-05). Title "State of What Art? A Call
  for Multi-Prompt LLM Evaluation". Authors in order: Moran Mizrahi, Guy Kaplan, Dan Malkin,
  Rotem Dror, Dafna Shahaf, Gabriel Stanovsky. TACL, volume 12, pages 933–949, 2024,
  DOI 10.1162/tacl_a_00681.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` (2nd) | Stengel-Eskin, Elias | Kaplan, Guy |
| `author` (3rd) | Chari, Abhishek | Malkin, Dan |
| `author` (4th) | Ringel, Yonatan | Dror, Rotem |
| `author` (5th) | Melamud, Oren | Shahaf, Dafna |
| `author` (6th) | Van Durme, Benjamin | Stanovsky, Gabriel |

Five of six author names are wrong. Only the first author is correct. Title, journal, volume,
pages and year are all correct. DOI is absent (not an error, but worth adding).

**Corrected entry**

```bibtex
@article{mizrahi2024state,
  title={State of What Art? A Call for Multi-Prompt {LLM} Evaluation},
  author={Mizrahi, Moran and Kaplan, Guy and Malkin, Dan and Dror, Rotem and Shahaf, Dafna and Stanovsky, Gabriel},
  journal={Transactions of the Association for Computational Linguistics},
  volume={12},
  pages={933--949},
  year={2024},
  doi={10.1162/tacl_a_00681},
  url={https://aclanthology.org/2024.tacl-1.52/}
}
```

---

## 3. `li2024generation` — FIELD ERRORS

Current entry:

```bibtex
@article{li2024generation,
  title={From Generation to Judgment: Opportunities and Challenges of {LLM}-as-a-Judge},
  author={Li, Dawei and Jiang, Bohan and Liang, Liangjie and Zhang, Zhengyang and Li, Ziqian and He, Junxian and Xie, Pengtao},
  journal={arXiv preprint arXiv:2411.16594},
  year={2024}
}
```

**Evidence**

- https://arxiv.org/abs/2411.16594 (retrieved 2026-09-05). Thirteen authors: Dawei Li, Bohan Jiang,
  Liangjie Huang, Alimohammad Beigi, Chengshuai Zhao, Zhen Tan, Amrita Bhattacharjee, Yuxuan
  Jiang, Canyu Chen, Tianhao Wu, Kai Shu, Lu Cheng, Huan Liu. Listed as EMNLP 2025.
- https://aclanthology.org/2025.emnlp-main.138/ (retrieved 2026-09-05). Title "From Generation to
  Judgment: Opportunities and Challenges of LLM-as-a-judge". Same 13 authors, same order.
  Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
  pages 2757–2791, November 2025, Suzhou, China, DOI 10.18653/v1/2025.emnlp-main.138.
- https://dblp.org/search/publ/api?q=From+Generation+to+Judgment+Opportunities+and+Challenges+of+LLM-as-a-judge&format=json
  (retrieved 2026-09-05). Confirms EMNLP 2025, pages 2757-2791, DOI 10.18653/V1/2025.EMNLP-MAIN.138.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` (3rd) | Liang, Liangjie | Huang, Liangjie |
| `author` (4th) | Zhang, Zhengyang | Beigi, Alimohammad |
| `author` (5th) | Li, Ziqian | Zhao, Chengshuai |
| `author` (6th) | He, Junxian | Tan, Zhen |
| `author` (7th) | Xie, Pengtao | Bhattacharjee, Amrita |
| `author` (8th–13th) | absent entirely | Jiang, Yuxuan; Chen, Canyu; Wu, Tianhao; Shu, Kai; Cheng, Lu; Liu, Huan |
| venue | arXiv preprint | Published at EMNLP 2025 |
| `title` | LLM-as-a-Judge | LLM-as-a-judge (lowercase j in both arXiv and ACL Anthology) |

The third author "Liangjie Huang" has been given the surname "Liang", and authors 4 through 7
are names that do not appear on the paper at all. Six of the thirteen authors are missing.

**Corrected entry**

```bibtex
@inproceedings{li2024generation,
  title={From Generation to Judgment: Opportunities and Challenges of {LLM}-as-a-judge},
  author={Li, Dawei and Jiang, Bohan and Huang, Liangjie and Beigi, Alimohammad and Zhao, Chengshuai and Tan, Zhen and Bhattacharjee, Amrita and Jiang, Yuxuan and Chen, Canyu and Wu, Tianhao and Shu, Kai and Cheng, Lu and Liu, Huan},
  booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
  pages={2757--2791},
  month={nov},
  year={2025},
  address={Suzhou, China},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2025.emnlp-main.138},
  url={https://aclanthology.org/2025.emnlp-main.138/}
}
```

Note: renaming the key to match the new year is the author's call. If the key is kept as
`li2024generation` the entry is still correct, only the mnemonic is stale.

---

## 4. `lin2022teaching` — VERIFIED

Current entry:

```bibtex
@article{lin2022teaching,
  title={Teaching Models to Express Their Uncertainty in Words},
  author={Lin, Stephanie and Hilton, Jacob and Evans, Owain},
  journal={Transactions on Machine Learning Research},
  year={2022}
}
```

**Evidence**

- https://arxiv.org/abs/2205.14334 (retrieved 2026-09-05). Title "Teaching Models to Express Their
  Uncertainty in Words". Authors Stephanie Lin, Jacob Hilton, Owain Evans. v1 28 May 2022,
  v2 13 Jun 2022.
- https://dblp.org/search/publ/api?q=Teaching+Models+to+Express+Their+Uncertainty+in+Words&format=json
  (retrieved 2026-09-05). Journal record: Trans. Mach. Learn. Res., volume 2022, year 2022, same
  three authors. A second CoRR record for abs/2205.14334.

Title, all three authors, journal and year are correct. Optional addition: `volume={2022}`, which
is how TMLR volumes are numbered.

---

## 5. `schulhoff2024prompt` — FIELD ERRORS

Current entry:

```bibtex
@article{schulhoff2024prompt,
  title={The Prompt Report: A Systematic Survey of Prompting Techniques},
  author={Schulhoff, Sander and Ilie, Michael and Balepur, Nishant and Kahadze, Konstantine and Liu, Amanda and Si, Chenglei and Li, Yinheng and Gupta, Aayush and Han, HyoJung and Schulhoff, Sevien and others},
  journal={arXiv preprint arXiv:2406.06608},
  year={2024}
}
```

**Evidence**

- https://arxiv.org/abs/2406.06608 (retrieved 2026-09-05). Current title on the abstract page:
  "The Prompt Report: A Systematic Survey of **Prompt Engineering** Techniques". Thirty-one authors
  in order: Sander Schulhoff, Michael Ilie, Nishant Balepur, Konstantine Kahadze, Amanda Liu,
  Chenglei Si, Yinheng Li, Aayush Gupta, HyoJung Han, Sevien Schulhoff, Pranav Sandeep Dulepet,
  Saurav Vidyadhara, Dayeon Ki, Sweta Agrawal, Chau Pham, Gerson Kroiz, Feileen Li, Hudson Tao,
  Ashay Srivastava, Hevander Da Costa, Saloni Gupta, Megan L. Rogers, Inna Goncearenco, Giuseppe
  Sarli, Igor Galynker, Denis Peskoff, Marine Carpuat, Jules White, Shyamal Anadkat, Alexander
  Hoyle, Philip Resnik. Submitted 6 June 2024; most recent version 26 February 2025.
- https://dblp.org/search/publ/api?q=The+Prompt+Report+A+Systematic+Survey&format=json
  (retrieved 2026-09-05). Single record, venue CoRR, abs/2406.06608, 2024, DOI
  10.48550/ARXIV.2406.06608. dblp's title is the **v1** form: "A Systematic Survey of Prompting
  Techniques". dblp gives the 16th author as "Gerson C. Kroiz" and the 30th as "Alexander Miserlis
  Hoyle"; arXiv gives "Gerson Kroiz" and "Alexander Hoyle".

**Sources disagree on the title.** arXiv's current version reads "Prompt Engineering Techniques";
dblp (indexed from v1) reads "Prompting Techniques". The .bib matches the older form. Citing the
current arXiv version is the safer choice, since that is what a reader following the arXiv ID will
see. Reporting both so the author can decide.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` | 10 names plus `and others` | 31 authors; 21 hidden behind `and others` |
| `title` | ...Survey of Prompting Techniques | arXiv current version: ...Survey of Prompt Engineering Techniques (dblp/v1 retains the .bib form) |

The work remains a preprint; no conference or journal version is indexed as of 2026-09-05.

**Corrected entry** (title taken from the current arXiv version)

```bibtex
@article{schulhoff2024prompt,
  title={The Prompt Report: A Systematic Survey of Prompt Engineering Techniques},
  author={Schulhoff, Sander and Ilie, Michael and Balepur, Nishant and Kahadze, Konstantine and Liu, Amanda and Si, Chenglei and Li, Yinheng and Gupta, Aayush and Han, HyoJung and Schulhoff, Sevien and Dulepet, Pranav Sandeep and Vidyadhara, Saurav and Ki, Dayeon and Agrawal, Sweta and Pham, Chau and Kroiz, Gerson and Li, Feileen and Tao, Hudson and Srivastava, Ashay and Da Costa, Hevander and Gupta, Saloni and Rogers, Megan L. and Goncearenco, Inna and Sarli, Giuseppe and Galynker, Igor and Peskoff, Denis and Carpuat, Marine and White, Jules and Anadkat, Shyamal and Hoyle, Alexander and Resnik, Philip},
  journal={arXiv preprint arXiv:2406.06608},
  year={2024}
}
```

---

## 6. `huang2024large` — FIELD ERRORS

Current entry:

```bibtex
@article{huang2024large,
  title={Large Language Models Cannot Self-Correct Reasoning Yet},
  author={Huang, Jie and Gu, Shima Sadegh and Hou, Le and Wu, Yuwei and Wang, Xuezhi and Yu, Hongkun and Han, Jiawei},
  journal={arXiv preprint arXiv:2310.01798},
  year={2024}
}
```

**Evidence**

- https://arxiv.org/abs/2310.01798 (retrieved 2026-09-05). Authors: Jie Huang, Xinyun Chen, Swaroop
  Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou. v1 3 October 2023, latest
  revision 14 March 2024. Listed as ICLR 2024.
- https://dblp.org/search/publ/api?q=Large+Language+Models+Cannot+Self-Correct+Reasoning+Yet&format=json
  (retrieved 2026-09-05). Two records with identical author lists: ICLR 2024, and CoRR
  abs/2310.01798 (2023, DOI 10.48550/ARXIV.2310.01798).

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` (2nd) | Gu, Shima Sadegh | Chen, Xinyun |
| `author` (3rd) | Hou, Le | Mishra, Swaroop |
| `author` (4th) | Wu, Yuwei | Zheng, Huaixiu Steven |
| `author` (5th) | Wang, Xuezhi | Yu, Adams Wei |
| `author` (6th) | Yu, Hongkun | Song, Xinying |
| `author` (7th) | Han, Jiawei | Zhou, Denny |
| venue | arXiv preprint | Published at ICLR 2024 |

Six of seven author names are wrong; only Jie Huang is correct. Title and arXiv ID are correct.

**Corrected entry**

```bibtex
@inproceedings{huang2024large,
  title={Large Language Models Cannot Self-Correct Reasoning Yet},
  author={Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
  booktitle={The Twelfth International Conference on Learning Representations (ICLR)},
  year={2024},
  note={arXiv:2310.01798}
}
```

---

## 7. `mckinsey2025stateofai` — UNVERIFIABLE (and the URL has almost certainly drifted)

Current entry:

```bibtex
@misc{mckinsey2025stateofai,
  title={The State of {AI} in 2025: Agents, Innovation, and Transformation},
  author={{McKinsey \& Company}},
  year={2025},
  howpublished={\url{https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai}},
  note={Accessed 2026-06-06}
}
```

**What was tried**

- https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai — fetched four
  times on 2026-09-05 (plain URL, and with a `#/` fragment). Every attempt exceeded the 60-second
  timeout with no response body. mckinsey.com appears to be behind bot protection that blocks
  automated retrieval.
- https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf
  — the November 2025 report PDF. Fetch attempted 2026-09-05, also timed out.
- https://webcache.googleusercontent.com/... — returned a Google error page, no cached copy.
- https://www.brianheger.com/the-state-of-ai-in-2025-agents-innovation-and-transformation-quantumblack-ai-by-mckinsey/
  (retrieved 2026-09-05) — a third-party page that **was** fetched successfully. It gives the
  report title as "The State of AI in 2025: Agents, Innovation, and Transformation", attributes it
  to QuantumBlack, AI by McKinsey, and links to exactly the URL in the .bib. Its own post date is
  13 November 2025. This corroborates the title but is not the publisher's own page.

**The finding that matters.** Web search on 2026-09-05 returns that same URL slug under the title
"The State of AI: Global Survey 2026", with survey fieldwork described as 4 May to 8 June 2026 and
1,719 respondents in 97 nations. This is an evergreen landing page for an annual survey: it serves
whatever the current edition is. The .bib cites it as though it were a fixed 2025 document. A
reader following the link in October 2026 will land on the 2026 survey, not the 2025 report the
paper relies on. I could not fetch the page to confirm this directly, so it is reported as a
strong indication rather than a verified fact, but it is the single highest-risk item in this set
after the two entries whose content is wrong.

**Recommended handling** (for the author to decide; I have changed nothing)

Point the entry at the dated November 2025 PDF rather than the rolling landing page, and re-stamp
the access date. Note that the report's own headline capitalization is sentence case:
"The state of AI in 2025: Agents, innovation, and transformation".

```bibtex
@misc{mckinsey2025stateofai,
  title={The State of {AI} in 2025: Agents, Innovation, and Transformation},
  author={{McKinsey \& Company}},
  year={2025},
  month={nov},
  howpublished={\url{https://www.mckinsey.com/~/media/mckinsey/business\%20functions/quantumblack/our\%20insights/the\%20state\%20of\%20ai/november\%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf}},
  note={QuantumBlack, AI by McKinsey. Accessed 2026-09-05}
}
```

Before submission, someone should open the landing page in an ordinary browser, confirm which
edition it now serves, and confirm the November 2025 PDF still resolves.

---

## 8. `claudecode2025loop` — FIELD ERRORS, and the cited claim does not match the source

Current entry:

```bibtex
@misc{claudecode2025loop,
  title={{Claude Code} Issue \#27281: Infinite Loop Bug},
  author={{Anthropic}},
  year={2025},
  howpublished={\url{https://github.com/anthropics/claude-code/issues/27281}},
  note={Accessed 2026-06-06}
}
```

**The claim in the paper.** `sections/discussion.tex` line 5: "public issue trackers document
agents stuck in infinite loops editing the same file (VSCode Issue \#257885, Claude Code Issue
\#27281) \cite{claudecode2025loop}."

**Evidence — Claude Code #27281**

- https://github.com/anthropics/claude-code/issues/27281 (retrieved 2026-09-05)
- https://api.github.com/repos/anthropics/claude-code/issues/27281 (retrieved 2026-09-05), which
  returned: title "Agent stuck in infinite loop — repeated 'let me write the document' without
  executing, burned full context window"; opened by GitHub user `brickhousemb`; created
  2026-02-21T00:20:38Z; state closed, state_reason duplicate.
- Body: "During a multi-agent research task, Claude Code got stuck in a loop where it repeatedly
  stated 'let me write the document' across multiple turns without ever actually calling the Write
  tool. This continued until the full context window was consumed and the session had to be
  compacted/continued. The actual task (writing a single markdown file from completed agent
  outputs) took ~10 seconds once the new session started."

The issue exists. It is a loop of **stated intent without any tool invocation**, ending in context
exhaustion. No file was edited repeatedly; the complaint is that the file was never written at all.
It does not support "agents stuck in infinite loops editing the same file."

**Evidence — VSCode #257885**

- https://github.com/microsoft/vscode/issues/257885 (retrieved 2026-09-05)
- https://api.github.com/repos/microsoft/vscode/issues/257885 (retrieved 2026-09-05), which
  returned: title "Copilot Chat agent mode stuck in infinite loop editing the same file over and
  over"; opened by `jasonkcarter`; created 2025-07-25T18:45:04Z; state closed, state_reason
  completed. Body describes the Keep/Undo history filling with thousands of references to one
  Markdown file and a counter reading "2080 files changed" within about 20 seconds, using Gemini
  2.5 Pro Preview.

This issue exists and **does** support the claim, precisely and by its own title. It has no entry
in `references.bib` at all; the prose cites it by number under the Claude Code key.

**Errors in the entry**

| Field | In the .bib | Correct |
|---|---|---|
| `title` | Claude Code Issue #27281: Infinite Loop Bug | Agent stuck in infinite loop — repeated 'let me write the document' without executing, burned full context window |
| `author` | {Anthropic} | Opened by GitHub user `brickhousemb`. Anthropic owns the repository but did not author the report |
| `year` | 2025 | 2026 (created 2026-02-21) |
| URL | correct | correct |

**Substantive problem, for the author's decision.** One citation currently does the work of two
sources, and it is the one that does not say what the sentence claims. Two options, neither of
which I have implemented:

1. Keep the "editing the same file" wording, cite the VSCode issue for it (add a `vscode2025loop`
   entry), and either drop the Claude Code issue or describe it separately and accurately, for
   example as a loop of restated intent that exhausted the context window without acting.
2. Broaden the sentence to "agents stuck in infinite loops" and let both issues sit under it, which
   costs the vivid "same file" detail but makes both citations true.

**Corrected entry for the existing key, plus the missing companion**

```bibtex
@misc{claudecode2025loop,
  title={Agent stuck in infinite loop: repeated ``let me write the document'' without executing, burned full context window},
  author={{brickhousemb}},
  year={2026},
  howpublished={GitHub issue \#27281, \texttt{anthropics/claude-code}, \url{https://github.com/anthropics/claude-code/issues/27281}},
  note={Opened 2026-02-21. Accessed 2026-09-05}
}

@misc{vscode2025loop,
  title={Copilot Chat agent mode stuck in infinite loop editing the same file over and over},
  author={{jasonkcarter}},
  year={2025},
  howpublished={GitHub issue \#257885, \texttt{microsoft/vscode}, \url{https://github.com/microsoft/vscode/issues/257885}},
  note={Opened 2025-07-25. Accessed 2026-09-05}
}
```

Note the key `claudecode2025loop` now carries a 2026 date. Renaming it is the author's call.

---

## 9. `skalse2022defining` — FIELD ERRORS

Current entry:

```bibtex
@article{skalse2022defining,
  title={Defining and Characterizing Reward Hacking},
  author={Skalse, Joar and Howe, Nikolaus H. R. and Krasheninnikov, Dmitrii and Krueger, David},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  pages={20460--20471},
  year={2022}
}
```

**Evidence**

- https://proceedings.neurips.cc/paper_files/paper/2022/hash/3d719fee332caa23d5038b8a90e81796-Abstract-Conference.html
  (retrieved 2026-09-05). The proceedings index page titles the paper "Defining and Characterizing
  Reward **Gaming**". Authors Joar Skalse, Nikolaus Howe, Dmitrii Krasheninnikov, David Krueger.
  Advances in Neural Information Processing Systems 35 (NeurIPS 2022), Main Conference Track.
- https://proceedings.neurips.cc/paper_files/paper/2022/file/3d719fee332caa23d5038b8a90e81796-Paper-Conference.pdf
  (retrieved 2026-09-05, text extracted locally). The camera-ready PDF's own first line reads
  "Defining and Characterizing Reward **Hacking**", by Joar Skalse (Oxford), Nikolaus H. R. Howe
  (Mila, Université de Montréal), Dmitrii Krasheninnikov (Cambridge), David Krueger (Cambridge).
- https://dblp.org/search/publ/api?q=Defining+Characterizing+Reward+Gaming&format=json and
  `&format=bibtex` (retrieved 2026-09-05). dblp indexes the NeurIPS 2022 paper as "Defining and
  Characterizing Reward Gaming"; no pages field.
- https://www.proceedings.com/content/068/068431webtoc.pdf (retrieved 2026-09-05, text extracted
  locally). The Curran Associates table of contents for the printed proceedings lists "Defining and
  Characterizing Reward Hacking .... **9460**", authors Nikolaus Howe, Dmitrii Krasheninnikov,
  David Krueger, Joar Skalse. The following entry, "Learning Distinct and Representative Modes for
  Image Captioning", begins at 9472, which fixes the end page at 9471.
- https://api.openalex.org/works/doi:10.52202/068431-0687 (retrieved 2026-09-05). Title "Defining
  and Characterizing Reward Hacking", 2022, source "Advances in Neural Information Processing
  Systems 35", first_page 9460, last_page 9471. Independently agrees with the Curran TOC.

**Sources disagree on the title.** The NeurIPS proceedings index page and dblp say "Reward Gaming";
the camera-ready PDF and the Curran printed TOC say "Reward Hacking". The .bib matches the PDF and
the printed volume, which is the defensible reading for a page-numbered citation. Reporting both.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `pages` | 20460--20471 | 9460--9471 |

Authors, volume 35 and year 2022 are all correct.

**Corrected entry**

```bibtex
@article{skalse2022defining,
  title={Defining and Characterizing Reward Hacking},
  author={Skalse, Joar and Howe, Nikolaus H. R. and Krasheninnikov, Dmitrii and Krueger, David},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  pages={9460--9471},
  year={2022}
}
```

---

## 10. `shinn2023reflexion` — VERIFIED

Current entry:

```bibtex
@inproceedings{shinn2023reflexion,
  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
  author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  year={2023}
}
```

**Evidence**

- https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html
  (retrieved 2026-09-05). Title "Reflexion: language agents with verbal reinforcement learning".
  Authors Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao. Advances
  in Neural Information Processing Systems 36 (NeurIPS 2023), Main Conference Track.
- https://dblp.org/search/publ/api?q=Reflexion+Language+Agents+with+Verbal+Reinforcement+Learning&format=json
  and `&format=bibtex` (retrieved 2026-09-05). Same five authors in the same order, NeurIPS 2023.

All five authors, the venue, volume 36 and year 2023 are correct. The published title is set in
sentence case ("language agents with verbal reinforcement learning"); the .bib uses title case,
which is a normal bibliography convention, not an error.

---

## 11. `borisov2026yapbench` — FIELD ERRORS

Current entry:

```bibtex
@article{borisov2026yapbench,
  title={Do Chatbot {LLMs} Talk Too Much? The {YapBench} Benchmark},
  author={Borisov, Vadim and Groger, Kathrin and Mikhael, John and Schreiber, Jens},
  journal={arXiv preprint arXiv:2601.00624},
  year={2026}
}
```

**Evidence**

- https://arxiv.org/abs/2601.00624 (retrieved 2026-09-05) and
  https://arxiv.org/abs/2601.00624v1 (retrieved 2026-09-05), where the authors line was copied
  character for character from the page: Vadim Borisov, Michael Gröger, Mina Mikhael,
  Richard H. Schreiber. Title "Do Chatbot LLMs Talk Too Much? The YapBench Benchmark". Submitted
  2 January 2026. Subjects: Machine Learning (cs.LG). No Comments or Journal-ref field.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` (2nd) | Groger, Kathrin | Gr\"oger, Michael |
| `author` (3rd) | Mikhael, John | Mikhael, Mina |
| `author` (4th) | Schreiber, Jens | Schreiber, Richard H. |

Three of four given names are wrong, and the second author's umlaut is dropped. Title, arXiv ID
and year are correct. Still a preprint.

**Corrected entry**

```bibtex
@article{borisov2026yapbench,
  title={Do Chatbot {LLMs} Talk Too Much? The {YapBench} Benchmark},
  author={Borisov, Vadim and Gr{\"o}ger, Michael and Mikhael, Mina and Schreiber, Richard H.},
  journal={arXiv preprint arXiv:2601.00624},
  year={2026}
}
```

---

## 12. `zhou2026oversight` — FIELD ERRORS

Current entry:

```bibtex
@article{zhou2026oversight,
  title={Steering {LLMs} via Scalable Interactive Oversight},
  author={Zhou, Enyu and Xi, Zhiheng and Huang, Xuanjing and others},
  journal={arXiv preprint arXiv:2602.04210},
  year={2026}
}
```

**Evidence**

- https://arxiv.org/abs/2602.04210 (retrieved 2026-09-05) and
  https://arxiv.org/abs/2602.04210v1 (retrieved 2026-09-05). Title "Steering LLMs via Scalable
  Interactive Oversight". Twelve authors in order: Enyu Zhou, Zhiheng Xi, Long Ma, Zhihao Zhang,
  Shihan Dou, Zhikai Lei, Guoteng Wang, Rui Zheng, Hang Yan, Tao Gui, Qi Zhang, Xuanjing Huang.
  Submitted 4 February 2026. No Comments or Journal-ref field.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` (3rd) | Huang, Xuanjing | Ma, Long |
| `author` | 3 names plus `and others` | 12 authors; 9 hidden, and Xuanjing Huang is the 12th (last) author, not the third |

This is the twelve-author truncation. Beyond hiding nine names, it promotes the last author to
third position, which misrepresents the ordering as well as the completeness.

**Corrected entry**

```bibtex
@article{zhou2026oversight,
  title={Steering {LLMs} via Scalable Interactive Oversight},
  author={Zhou, Enyu and Xi, Zhiheng and Ma, Long and Zhang, Zhihao and Dou, Shihan and Lei, Zhikai and Wang, Guoteng and Zheng, Rui and Yan, Hang and Gui, Tao and Zhang, Qi and Huang, Xuanjing},
  journal={arXiv preprint arXiv:2602.04210},
  year={2026}
}
```

---

## 13. `schemmer2023reliance` — VERIFIED

Current entry:

```bibtex
@inproceedings{schemmer2023reliance,
  title={Appropriate Reliance on {AI} Advice: Conceptualization and the Effect of Explanations},
  author={Schemmer, Max and Kuehl, Niklas and Benz, Carina and Bartos, Andrea and Satzger, Gerhard},
  booktitle={Proceedings of the 28th International Conference on Intelligent User Interfaces (IUI)},
  year={2023},
  note={arXiv:2302.02187}
}
```

**Evidence**

- https://arxiv.org/abs/2302.02187 (retrieved 2026-09-05). Title "Appropriate Reliance on AI
  Advice: Conceptualization and the Effect of Explanations". Authors Max Schemmer, Niklas Kühl,
  Carina Benz, Andrea Bartos, Gerhard Satzger. Journal-ref: "ACM 28th International Conference on
  Intelligent User Interfaces (IUI), 2023". DOI 10.1145/3581641.3584066.
- https://dblp.org/search/publ/api?q=Appropriate+Reliance+on+AI+Advice+Conceptualization+Effect+of+Explanations&format=json
  (retrieved 2026-09-05). IUI 2023, pages 410-422, DOI 10.1145/3581641.3584066, same five authors,
  plus a CoRR record for abs/2302.02187.
- https://dl.acm.org/doi/10.1145/3581641.3584066 returned HTTP 403 on 2026-09-05; the ACM record
  could not be fetched directly, so the pages figure rests on dblp and the arXiv journal-ref rests
  on arXiv.

Title, all five authors, conference number (IUI 2023 was indeed the 28th), year and arXiv ID are
all correct. "Kuehl" is a standard ASCII transliteration of "Kühl" and is acceptable; setting it
as `K{\"u}hl` would match the author's own spelling. Pages (410--422) and the DOI are absent but
not wrong. Optional strengthened form:

```bibtex
@inproceedings{schemmer2023reliance,
  title={Appropriate Reliance on {AI} Advice: Conceptualization and the Effect of Explanations},
  author={Schemmer, Max and K{\"u}hl, Niklas and Benz, Carina and Bartos, Andrea and Satzger, Gerhard},
  booktitle={Proceedings of the 28th International Conference on Intelligent User Interfaces (IUI)},
  pages={410--422},
  year={2023},
  doi={10.1145/3581641.3584066},
  note={arXiv:2302.02187}
}
```

---

## 14. `zhang2024small` — VERIFIED

Current entry:

```bibtex
@article{zhang2024small,
  title={Small Language Models Need Strong Verifiers to Self-Correct Reasoning},
  author={Zhang, Yunxiang and Khalifa, Muhammad and Logeswaran, Lajanugen and Kim, Jaekyeom and Lee, Moontae and Lee, Honglak and Wang, Lu},
  journal={Findings of the Association for Computational Linguistics: ACL 2024},
  year={2024},
  note={arXiv:2404.17140}
}
```

**Evidence**

- https://aclanthology.org/2024.findings-acl.924/ (retrieved 2026-09-05). Title "Small Language
  Models Need Strong Verifiers to Self-Correct Reasoning". Authors in order: Yunxiang Zhang,
  Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim, Moontae Lee, Honglak Lee, Lu Wang.
  Findings of the Association for Computational Linguistics: ACL 2024, pages 15637–15653, 2024,
  DOI 10.18653/v1/2024.findings-acl.924.

Title, all seven authors in order, venue and year are correct. Pages and DOI are absent but not
wrong. Optional strengthened form:

```bibtex
@inproceedings{zhang2024small,
  title={Small Language Models Need Strong Verifiers to Self-Correct Reasoning},
  author={Zhang, Yunxiang and Khalifa, Muhammad and Logeswaran, Lajanugen and Kim, Jaekyeom and Lee, Moontae and Lee, Honglak and Wang, Lu},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
  pages={15637--15653},
  year={2024},
  doi={10.18653/v1/2024.findings-acl.924},
  note={arXiv:2404.17140}
}
```

---

## 15. `sui2025efficient` — FIELD ERRORS

Current entry:

```bibtex
@article{sui2025efficient,
  title={Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models},
  author={Sui, Yang and Chuang, Yu-Neng and Wang, Guanchu and Zhang, Jiamu and Zhang, Tianyi and Yuan, Jiayi and Liu, Hongyi and Wen, Andrew and Zhong, Shaochen and Chen, Hanjie and Hu, Xia},
  journal={Transactions on Machine Learning Research (TMLR)},
  year={2025},
  note={arXiv:2503.16419}
}
```

**Evidence**

- https://arxiv.org/abs/2503.16419 (retrieved 2026-09-05) and https://arxiv.org/abs/2503.16419v4
  (retrieved 2026-09-05, authors line copied in order). Twelve authors: Yang Sui, Yu-Neng Chuang,
  Guanchu Wang, Jiamu Zhang, Tianyi Zhang, Jiayi Yuan, Hongyi Liu, Andrew Wen, Shaochen Zhong,
  **Na Zou**, Hanjie Chen, Xia Hu. Title "Stop Overthinking: A Survey on Efficient Reasoning for
  Large Language Models". Submitted 20 March 2025; v4 21 August 2025. Comments: "Accepted by TMLR
  2025. Project website: https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs".

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` | 11 names; **Na Zou** omitted between Zhong, Shaochen and Chen, Hanjie | 12 authors including Zou, Na |

Title, venue (TMLR 2025, confirmed by the arXiv Comments field), year and arXiv ID are correct.
This is a single dropped author, not a truncation, so it is easy to miss on a read-through.

**Corrected entry**

```bibtex
@article{sui2025efficient,
  title={Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models},
  author={Sui, Yang and Chuang, Yu-Neng and Wang, Guanchu and Zhang, Jiamu and Zhang, Tianyi and Yuan, Jiayi and Liu, Hongyi and Wen, Andrew and Zhong, Shaochen and Zou, Na and Chen, Hanjie and Hu, Xia},
  journal={Transactions on Machine Learning Research (TMLR)},
  year={2025},
  note={arXiv:2503.16419}
}
```

---

## 16. `zhang2024lists` — FIELD ERRORS

Current entry:

```bibtex
@article{zhang2024lists,
  title={From Lists to Emojis: How Format Bias Affects Model Alignment},
  author={Zhang, Xuanchang and Yu, Wei and Yu, Ping and Xu, Mingyu and Chen, Jiawei and Weston, Jason and others},
  journal={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2025},
  note={arXiv:2409.11704}
}
```

**Evidence**

- https://aclanthology.org/2025.acl-long.1308/ (retrieved 2026-09-05). Title "From Lists to Emojis:
  How Format Bias Affects Model Alignment". Authors in order: Xuanchang Zhang, Wei Xiong, Lichang
  Chen, Tianyi Zhou, Heng Huang, Tong Zhang. Proceedings of the 63rd Annual Meeting of the
  Association for Computational Linguistics (Volume 1: Long Papers), pages 26940–26961, July 2025,
  Vienna, Austria, DOI 10.18653/v1/2025.acl-long.1308.
- As a check that the anthology ID was not a near-miss, https://aclanthology.org/2025.acl-long.1259/
  (retrieved 2026-09-05) was also fetched and is a different paper ("Dehumanizing Machines:
  Mitigating Anthropomorphic Behaviors in Text Generation Systems"), confirming .1308 is the right
  record.

**Errors**

| Field | In the .bib | Correct |
|---|---|---|
| `author` (2nd) | Yu, Wei | Xiong, Wei |
| `author` (3rd) | Yu, Ping | Chen, Lichang |
| `author` (4th) | Xu, Mingyu | Zhou, Tianyi |
| `author` (5th) | Chen, Jiawei | Huang, Heng |
| `author` (6th) | Weston, Jason | Zhang, Tong |
| `author` | trailing `and others` | there are no further authors; the paper has exactly 6 |
| venue detail | ...(ACL) | ...(Volume 1: Long Papers); pages 26940--26961 absent |

Five of six author names are wrong, only the first is correct, and the trailing `and others`
implies authors who do not exist. The second author "Wei Xiong" has been rendered as "Yu, Wei".
The `year` field (2025) is correct and matches the anthology; the key's own `2024` is a stale
mnemonic from the arXiv posting, not a field error.

**Corrected entry**

```bibtex
@inproceedings{zhang2024lists,
  title={From Lists to Emojis: How Format Bias Affects Model Alignment},
  author={Zhang, Xuanchang and Xiong, Wei and Chen, Lichang and Zhou, Tianyi and Huang, Heng and Zhang, Tong},
  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={26940--26961},
  month={jul},
  year={2025},
  address={Vienna, Austria},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2025.acl-long.1308},
  note={arXiv:2409.11704}
}
```

---

## Summary table

| # | Key | Classification | Shortest statement of the problem |
|---|---|---|---|
| 1 | `ranaldi2023large` | FIELD ERRORS | Wrong arXiv ID (points to an unrelated vision paper); wrong title |
| 2 | `mizrahi2024state` | FIELD ERRORS | 5 of 6 authors wrong |
| 3 | `li2024generation` | FIELD ERRORS | 5 authors wrong, 6 missing (13 total); now published at EMNLP 2025 |
| 4 | `lin2022teaching` | VERIFIED | — |
| 5 | `schulhoff2024prompt` | FIELD ERRORS | 21 authors hidden by `and others` (31 total); arXiv's current title differs |
| 6 | `huang2024large` | FIELD ERRORS | 6 of 7 authors wrong; published at ICLR 2024, listed as preprint |
| 7 | `mckinsey2025stateofai` | UNVERIFIABLE | mckinsey.com fetch timed out on every attempt; URL is a rolling page now serving the 2026 edition |
| 8 | `claudecode2025loop` | FIELD ERRORS | Fabricated title, wrong author, wrong year; source does not support the claim it is cited for |
| 9 | `skalse2022defining` | FIELD ERRORS | Pages 20460--20471 should be 9460--9471; index page and PDF disagree on Hacking vs Gaming |
| 10 | `shinn2023reflexion` | VERIFIED | — |
| 11 | `borisov2026yapbench` | FIELD ERRORS | 3 of 4 given names wrong |
| 12 | `zhou2026oversight` | FIELD ERRORS | 12-author list cut to 3 plus `and others`; last author promoted to third |
| 13 | `schemmer2023reliance` | VERIFIED | — |
| 14 | `zhang2024small` | VERIFIED | — |
| 15 | `sui2025efficient` | FIELD ERRORS | Author Na Zou omitted (12 authors, 11 listed) |
| 16 | `zhang2024lists` | FIELD ERRORS | 5 of 6 authors wrong; `and others` implies authors that do not exist |

**Counts:** VERIFIED 4 · FIELD ERRORS 11 · UNVERIFIABLE 1 · NOT FOUND 0 · total 16.

Every one of the 16 cited works exists; none is a hallucinated paper. The damage is concentrated
in author lists (9 of the 11 FIELD ERRORS entries have a wrong or incomplete author list) and in
two entries where the citation points somewhere other than what the paper relies on:
`ranaldi2023large`, whose arXiv ID resolves to an unrelated computer-vision paper, and
`claudecode2025loop`, whose issue does not describe the behaviour the discussion section
attributes to it.

Nothing in `references.bib` or any other project file was changed by this audit.
