# Bibliography audit, chunk 2

Source file audited: `/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/references.bib`

Scope: 17 keys only. All other entries in the file were ignored.

Audit performed 2026-09-05. Every URL listed under "Evidence" was fetched on that
date unless a different date is stated on the line. Where a page could not be
fetched directly, the section says so and names what was fetched instead.

Conference ordinals used below were checked at source: ICLR 2024 is the Twelfth
(`https://iclr.cc/Conferences/2024`, retrieved 2026-09-05) and ICLR 2026 is the
Fourteenth (`https://iclr.cc/Conferences/2026`, retrieved 2026-09-05).

Nothing in `references.bib` was modified. Corrected entries below are drafts for
the author to accept, amend or reject.

---

## sharma2024towards

Current entry:

```bibtex
@article{sharma2024towards,
  title={Towards Understanding Sycophancy in Language Models},
  author={Sharma, Mrinank and Tong, Meg and Korbak, Tomasz and Duvenaud, David and Askell, Amanda and Bowman, Samuel R and Cheng, Newton and Durmus, Esin and Hatfield-Dodds, Zac and Johnston, Scott R and others},
  journal={arXiv preprint arXiv:2310.13548},
  year={2024}
}
```

**Classification: FIELD ERRORS**

Wrong fields:

| Field | Current value | Correct value |
|---|---|---|
| entry type / venue | `@article`, `journal={arXiv preprint arXiv:2310.13548}` | `@inproceedings`, published at ICLR 2024 (the Twelfth International Conference on Learning Representations) |
| author | truncated at `Johnston, Scott R and others` (10 named of 19) | 19 authors, full list below |

The arXiv identifier itself is correct (2310.13548) and the title matches the
published version character for character. The year 2024 is correct for the ICLR
citation, though the arXiv v1 is October 2023, so the entry as currently written
(a 2023 preprint dated 2024) is internally inconsistent.

Evidence:

- `https://arxiv.org/abs/2310.13548`, retrieved 2026-09-05. Title, 19-author list, v1 2023-10-20, v4 2025-05-10. No journal-ref field.
- `https://proceedings.iclr.cc/paper_files/paper/2024/file/0105f7972202c1d4fb817da9f21a9663-Paper-Conference.pdf`, retrieved 2026-09-05. Page 1 header reads verbatim: "Published as a conference paper at ICLR 2024". Title and full author list confirmed from the PDF body.
- `https://iclr.cc/virtual/2024/poster/17593`, retrieved 2026-09-05. ICLR 2024, poster. No award designation.

Corrected entry:

```bibtex
@inproceedings{sharma2024towards,
  title={Towards Understanding Sycophancy in Language Models},
  author={Sharma, Mrinank and Tong, Meg and Korbak, Tomasz and Duvenaud, David and Askell, Amanda and Bowman, Samuel R. and Cheng, Newton and Durmus, Esin and Hatfield-Dodds, Zac and Johnston, Scott R. and Kravec, Shauna and Maxwell, Timothy and McCandlish, Sam and Ndousse, Kamal and Rausch, Oliver and Schiefer, Nicholas and Yan, Da and Zhang, Miranda and Perez, Ethan},
  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
  year={2024},
  note={arXiv:2310.13548}
}
```

---

## zhao2021calibrate

Current entry:

```bibtex
@inproceedings{zhao2021calibrate,
  title={Calibrate Before Use: Improving Few-Shot Performance of Language Models},
  author={Zhao, Zihao and Wallace, Eric and Feng, Shi and Klein, Dan and Singh, Sameer},
  booktitle={Proceedings of the 38th International Conference on Machine Learning},
  pages={12697--12706},
  year={2021}
}
```

**Classification: VERIFIED**

Title, all five authors, the conference number (38th), the page range
12697--12706 and the year 2021 all match the publisher record.

One cosmetic difference, not an error: PMLR sets the title as "Improving
Few-shot Performance" with a lowercase s in "shot". The entry has "Few-Shot".
Either is defensible in a title-case bibliography style.

Optional additions the publisher record supports: `volume={139}`,
`series={Proceedings of Machine Learning Research}`, `publisher={PMLR}`,
`editor={Meila, Marina and Zhang, Tong}`.

Evidence:

- `https://proceedings.mlr.press/v139/zhao21c.html`, retrieved 2026-09-05. Publisher BibTeX read directly from the page.

---

## kim2024language

Current entry:

```bibtex
@article{kim2024language,
  title={Language Models Can Improve Their Own Reasoning---and Sometimes They Can't},
  author={Kim, Seungone and Suk, Se June and Longpre, Shayne and Lin, Bill Yuchen and Shin, Jamin and Welleck, Sean and Neubig, Graham and Lee, Moontae and Lee, Kyungjae and Seo, Minjoon},
  journal={arXiv preprint arXiv:2401.12294},
  year={2024}
}
```

**Classification: NOT FOUND**

No work with this title exists, and the arXiv identifier belongs to an unrelated
paper in a different field. Three separate problems, each independently
disqualifying:

1. **The arXiv ID points somewhere else.** arXiv 2401.12294 is "Nearly critical
   superfluid: effective field theory and holography" by Yanyan Bu, Hongfei Gao,
   Xin Gao and Zhiwei Li, a high-energy-theory (hep-th) paper. It has no
   connection to language models.
2. **The title does not exist.** No paper called "Language Models Can Improve
   Their Own Reasoning - and Sometimes They Can't" appears on arXiv, in the ACL
   Anthology, or in the publication list on the first author's own website.
3. **The author list belongs to a different paper.** The ten names, in this
   order, are the author list of "Prometheus 2: An Open Source Language Model
   Specialized in Evaluating Other Language Models" (EMNLP 2024, arXiv
   2405.01535), with one corruption: the second author is Juyoung Suk, not
   "Se June Suk".

What was searched:

- `https://arxiv.org/abs/2401.12294`, retrieved 2026-09-05. Returns the hep-th superfluid paper.
- `https://seungonekim.github.io/`, retrieved 2026-09-05. The first author's own publication list. No paper with this or a similar title appears anywhere in it.
- Web searches on the exact title, on the title plus author surnames, and on the title fragment "Sometimes They Can't" with "Seungone Kim". No matching work.
- `https://arxiv.org/abs/2405.01535` and `https://aclanthology.org/2024.emnlp-main.248/`, both retrieved 2026-09-05, confirming the author list belongs to Prometheus 2.

No corrected entry is supplied, because there is no way to tell what work was
intended. If the intended citation is Prometheus 2, the correct entry is:

```bibtex
@inproceedings{kim2024prometheus,
  title={Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models},
  author={Kim, Seungone and Suk, Juyoung and Longpre, Shayne and Lin, Bill Yuchen and Shin, Jamin and Welleck, Sean and Neubig, Graham and Lee, Moontae and Lee, Kyungjae and Seo, Minjoon},
  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  pages={4334--4353},
  year={2024},
  address={Miami, Florida, USA},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2024.emnlp-main.248}
}
```

But that is a guess about intent, not a verification. **The author needs to
decide what this citation was meant to point at, and check that whatever claim
it supports in the manuscript body is actually made by the replacement work.**

---

## koo2024benchmarking

Current entry:

```bibtex
@article{koo2024benchmarking,
  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},
  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},
  journal={arXiv preprint arXiv:2309.17012},
  year={2024}
}
```

**Classification: FIELD ERRORS**

Title, all six authors, the arXiv identifier and the year 2024 are correct. The
venue is not: this was published at ACL 2024 (Findings) and the arXiv page says
so in its own comments field.

| Field | Current value | Correct value |
|---|---|---|
| entry type / venue | `@article`, `journal={arXiv preprint arXiv:2309.17012}` | `@inproceedings`, `booktitle={Findings of the Association for Computational Linguistics: ACL 2024}` |
| pages | absent | `517--545` |
| doi | absent | `10.18653/v1/2024.findings-acl.29` |

Evidence:

- `https://arxiv.org/abs/2309.17012`, retrieved 2026-09-05. v1 2023-09-29, v3 2024-09-25. Comments field states publication at ACL 2024.
- `https://aclanthology.org/2024.findings-acl.29/`, retrieved 2026-09-05. Anthology BibTeX read from the page: Findings of ACL 2024, Bangkok, Thailand, August 2024, pages 517--545.

Corrected entry:

```bibtex
@inproceedings{koo2024benchmarking,
  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},
  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
  pages={517--545},
  year={2024},
  address={Bangkok, Thailand},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2024.findings-acl.29}
}
```

---

## anthropic2025prompting

Current entry:

```bibtex
@misc{anthropic2025prompting,
  title={Prompt Engineering Best Practices},
  author={{Anthropic}},
  year={2025},
  howpublished={\url{https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct}},
  note={Accessed 2026-03-31}
}
```

**Classification: FIELD ERRORS**

The page has moved and been restructured, and the title in the entry is not the
title of the page.

| Field | Current value | Correct value |
|---|---|---|
| title | `Prompt Engineering Best Practices` | `Prompting best practices` (page title as published) |
| howpublished (URL) | `https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct` | `https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct` |

The old URL is not dead: it 301-redirects (HTTP 200 after redirect) to the new
`platform.claude.com` location. "Be clear and direct" is no longer a page of its
own; it is now a level-3 section heading inside the consolidated "Prompting best
practices" page. The `#be-clear-and-direct` anchor still resolves to that
section, so the corrected URL preserves what the citation was pointing at.

The access note is five months stale. Anthropic's documentation is a
fast-churning source, and the page has demonstrably changed since 2026-03-31:
the whole document was reorganized into three parts and now covers models
released after that date. The note should be restamped to the date the citation
is finalized.

Evidence:

- `curl -L https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct` on 2026-09-05: HTTP 200, final URL `https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct`.
- `https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices`, retrieved 2026-09-05. Page title "Prompting best practices". Section headings enumerated; `### Be clear and direct` present at the top of the "General principles" part.

Corrected entry:

```bibtex
@misc{anthropic2025prompting,
  title={Prompting Best Practices},
  author={{Anthropic}},
  year={2025},
  howpublished={\url{https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct}},
  note={Accessed 2026-09-05}
}
```

A caution on the `year={2025}` field: the page carries no publication or
revision date of its own, so 2025 cannot be corroborated from the source. For an
undated web document the access stamp is the claim that can actually be
supported. If the manuscript needs a date attached to this citation, "current as
of 2026-09-05" is the defensible form.

---

## bai2022training

Current entry:

```bibtex
@article{bai2022training,
  title={Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback},
  author={Bai, Yuntao and Jones, Andy and Ndousse, Kamal and Askell, Amanda and Chen, Anna and DasSarma, Nova and Drain, Dawn and Fort, Stanislav and Ganguli, Deep and Henighan, Tom and others},
  journal={arXiv preprint arXiv:2204.05862},
  year={2022}
}
```

**Classification: VERIFIED**

Title matches character for character. The ten named authors are the first ten
in the correct order, and `and others` correctly stands in for the remaining 21
(Joseph, Kadavath, Kernion, Conerly, El-Showk, Elhage, Hatfield-Dodds,
Hernandez, Hume, Johnston, Kravec, Lovitt, Nanda, Olsson, Amodei, Brown, Clark,
McCandlish, Olah, Mann, Kaplan). Year 2022 and arXiv ID 2204.05862 are correct.

The preprint status is correct: the arXiv record carries no journal reference,
and this work was never published in a peer-reviewed venue. Citing it as an
arXiv preprint is right.

Evidence:

- `https://arxiv.org/abs/2204.05862`, retrieved 2026-09-05. Full 31-author list read from the page; no journal-ref.

---

## thompson2026aicost

Current entry:

```bibtex
@misc{thompson2026aicost,
  title={The {AI} Boom Has Entered Its `Wait, Is This Worth It?' Phase},
  author={Thompson, Derek},
  year={2026},
  howpublished={\url{https://www.derekthompson.org/p/the-great-ai-cost-panic-of-2026}},
  note={Accessed 2026-06-06}
}
```

**Classification: FIELD ERRORS**

The URL is live and correct, the author and year are correct, but the last word
of the title is wrong.

| Field | Current value | Correct value |
|---|---|---|
| title | `The AI Boom Has Entered Its 'Wait, Is This Worth It?' Phase` | `The AI Boom Has Entered Its 'Wait, Is This Worth It?' Era` |

Two sources disagree on this and the disagreement is worth recording. The
article's on-page `<h1>` and the page's structured metadata both read **Era**.
Some search-engine result listings render the headline as **Phase**, which is
probably how the wrong word got into the entry. The page itself is the
authority, so "Era" is correct.

The published date embedded in the page metadata is 2026-05-29, which is
consistent with the entry's year and precedes the recorded access date.
Adding the publication date to the entry would strengthen it.

Evidence:

- `https://www.derekthompson.org/p/the-great-ai-cost-panic-of-2026`, retrieved 2026-09-05. HTTP 200. Article `<h1>`: "The AI Boom Has Entered Its 'Wait, Is This Worth It?' Era". `"datePublished":"2026-05-29T10:02:13+00:00"`.

Corrected entry:

```bibtex
@misc{thompson2026aicost,
  title={The {AI} Boom Has Entered Its `Wait, Is This Worth It?' Era},
  author={Thompson, Derek},
  year={2026},
  howpublished={\url{https://www.derekthompson.org/p/the-great-ai-cost-panic-of-2026}},
  note={Published 2026-05-29. Accessed 2026-09-05}
}
```

---

## openai2025sycophancy

Current entry:

```bibtex
@misc{openai2025sycophancy,
  title={Sycophancy in {GPT}-4o: What Happened},
  author={{OpenAI}},
  year={2025},
  howpublished={\url{https://openai.com/index/sycophancy-in-gpt-4o/}},
  note={Accessed 2026-06-06}
}
```

**Classification: FIELD ERRORS**

The URL, author and year are right. The title is truncated: it stops halfway
through the published headline, which changes what the post appears to be about
(the full title announces a remedy, not just a postmortem).

| Field | Current value | Correct value |
|---|---|---|
| title | `Sycophancy in GPT-4o: What Happened` | `Sycophancy in GPT-4o: what happened and what we're doing about it` |

Note on how this was verified. `openai.com` returns HTTP 403 to every automated
fetch, both through the fetch tool and through curl with full browser headers,
so the rendered page could not be read directly. The title was instead taken
from **OpenAI's own RSS feed**, `https://openai.com/news/rss.xml`, which is a
primary source published by OpenAI and was fetched successfully. The feed item
gives the title verbatim and a publication date of Tue, 29 Apr 2025 18:00:00
GMT, which corroborates the year and confirms the URL.

Evidence:

- `https://openai.com/news/rss.xml`, retrieved 2026-09-05. Feed item: title "Sycophancy in GPT-4o: what happened and what we're doing about it", link `https://openai.com/index/sycophancy-in-gpt-4o`, pubDate Tue, 29 Apr 2025 18:00:00 GMT.
- `https://openai.com/index/sycophancy-in-gpt-4o/`, attempted 2026-09-05: HTTP 403 to automated clients. Existence independently corroborated by `https://www.law.georgetown.edu/tech-institute/research-insights/insights/tech-brief-ai-sycophancy-openai-2/` (retrieved 2026-09-05), which cites the URL.

Corrected entry:

```bibtex
@misc{openai2025sycophancy,
  title={Sycophancy in {GPT}-4o: What Happened and What We're Doing About It},
  author={{OpenAI}},
  year={2025},
  howpublished={\url{https://openai.com/index/sycophancy-in-gpt-4o/}},
  note={Published 2025-04-29. Accessed 2026-09-05}
}
```

A related post exists and may be the better citation depending on what the
manuscript claims: "Expanding on what we missed with sycophancy",
`https://openai.com/index/expanding-on-sycophancy`, published 2025-05-02 (same
RSS feed, same retrieval). That one is the detailed technical account; the
April 29 post is the short rollback announcement. Worth checking which one
supports the sentence it is attached to.

---

## zhang2020dialogpt

Current entry:

```bibtex
@article{zhang2020dialogpt,
  title={{DialoGPT}: Large-Scale Generative Pre-training for Conversational Response Generation},
  author={Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill},
  journal={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
  pages={270--278},
  year={2020}
}
```

**Classification: FIELD ERRORS**

Every bibliographic fact here is correct: the nine authors and their order, the
conference number (58th), the System Demonstrations track, the page range
270--278, and the year 2020 all match the ACL Anthology record. The error is
structural, and it will show up in the compiled bibliography.

| Field | Current value | Correct value |
|---|---|---|
| entry type | `@article` | `@inproceedings` |
| venue field | `journal={Proceedings of the 58th Annual Meeting...}` | `booktitle={Proceedings of the 58th Annual Meeting...}` |
| doi | absent | `10.18653/v1/2020.acl-demos.30` |
| publisher | absent | `Association for Computational Linguistics` |

A conference proceedings placed in a `journal` field of an `@article` entry will
be typeset as a journal article by `acl_natbib.bst`, which is the style this
manuscript uses. This is worth fixing before submission.

On the title: the Anthology sets it as "DIALOGPT : Large-Scale Generative
Pre-training for Conversational Response Generation", with the model name in
small capitals and a space before the colon. The entry's `{DialoGPT}:` is the
conventional rendering and needs no change.

Evidence:

- `https://aclanthology.org/2020.acl-demos.30/`, retrieved 2026-09-05. Anthology BibTeX read from the page.

Corrected entry:

```bibtex
@inproceedings{zhang2020dialogpt,
  title={{DialoGPT}: Large-Scale Generative Pre-training for Conversational Response Generation},
  author={Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill},
  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
  pages={270--278},
  year={2020},
  publisher={Association for Computational Linguistics},
  doi={10.18653/v1/2020.acl-demos.30}
}
```

---

## laban2025lost

Current entry:

```bibtex
@inproceedings{laban2025lost,
  title={{LLMs} Get Lost In Multi-Turn Conversation},
  author={Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},
  year={2025},
  note={Best Paper Award}
}
```

**Classification: FIELD ERRORS**

This is the entry that prompted the audit. Four things are wrong, and one thing
that looked wrong is in fact substantially right.

| Field | Current value | Correct value |
|---|---|---|
| booktitle (conference number) | `Thirteenth` | `Fourteenth` |
| year | `2025` | `2026` |
| note (award) | `Best Paper Award` | `Outstanding Paper Award` |
| bibtex key | `laban2025lost` | `laban2026lost` |

**Conference number and year.** The paper appears in ICLR 2026, which is the
Fourteenth International Conference on Learning Representations, held in Rio de
Janeiro, 23--27 April 2026. The entry's "Thirteenth / 2025" pairing was
internally consistent (ICLR 2025 was indeed the Thirteenth) but named the wrong
conference: the paper was not at ICLR 2025 in any form. The arXiv v1 is dated
2025-05-09, which is almost certainly where the 2025 came from, but ICLR 2025
had already taken place by then.

**Citation year for the key.** 2026. The publication being cited is the ICLR
2026 conference paper, so both the `year` field and the key should read 2026. If
the author prefers to cite the preprint instead, the year would still not be a
clean 2025 for an `@inproceedings` entry, because a preprint is not conference
proceedings. Citing the published version is the better choice here, and it is
the version that carries the award.

**The award claim is true, but the award has a different name.** ICLR 2026 does
not give a "Best Paper Award". Its top honour is the **Outstanding Paper Award**,
and this paper is one of two that received it. The categories used in the
official announcement are Outstanding Paper and Honorable Mention; there is no
Best Paper category. So the note should be kept, with the award named correctly.

**Authors and title are correct** exactly as they appear: Philippe Laban,
Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville, and "LLMs Get Lost In Multi-Turn
Conversation", confirmed from the camera-ready PDF.

Evidence:

- `https://proceedings.iclr.cc/paper_files/paper/2026/file/59f6421e64707225fdf5b28840679a07-Paper-Conference.pdf`, retrieved 2026-09-05. Page 1 header reads verbatim: "Published as a conference paper at ICLR 2026". Title and all four authors read from the PDF text (affiliations: Microsoft Research; Salesforce Research).
- `https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/`, retrieved 2026-09-05. Official ICLR announcement, 23 April 2026. Two Outstanding Papers: "Transformers are Inherently Succinct" (Bergsträßer, Cotterell, Lin) and "LLMs Get Lost In Multi-Turn Conversation" (Laban, Hayashi, Zhou, Neville). One Honorable Mention. No "Best Paper" category exists in the announcement.
- `https://iclr.cc/Conferences/2026`, retrieved 2026-09-05. Official name: "The Fourteenth International Conference on Learning Representations", 23--27 April 2026, Rio de Janeiro, Brazil.
- `https://iclr.cc/virtual/2026/oral/10009147`, retrieved 2026-09-05. ICLR 2026, oral presentation, 23 April 2026.
- `https://arxiv.org/abs/2505.06120`, retrieved 2026-09-05. arXiv v1 2025-05-09, no journal-ref at time of retrieval.

Corrected entry:

```bibtex
@inproceedings{laban2026lost,
  title={{LLMs} Get Lost In Multi-Turn Conversation},
  author={Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
  booktitle={Proceedings of the Fourteenth International Conference on Learning Representations (ICLR)},
  year={2026},
  note={Outstanding Paper Award. arXiv:2505.06120}
}
```

Changing the key means every `\citep{laban2025lost}` / `\citet{laban2025lost}`
in `sections/` must be updated to `laban2026lost`, or the build will emit
undefined-citation warnings and print question marks. The author may prefer to
keep the old key and change only the fields; that is a valid choice, at the cost
of a key whose year no longer matches the entry.

---

## gartner2026agentic

Current entry:

```bibtex
@misc{gartner2026agentic,
  title={Agentic {AI} Will Drive a 5--30x Increase in Token Consumption per Task},
  author={{Gartner}},
  year={2026},
  howpublished={Gartner Research Note},
  note={Accessed 2026-06-10}
}
```

**Classification: UNVERIFIABLE**

No Gartner document bearing this title could be located, and the entry provides
nothing that would let a reader find one: no URL, no Gartner document ID, no
publication date, no analyst name. "Gartner Research Note" is a category, not a
citation.

What was tried:

- `https://www.gartner.com/en/newsroom/press-releases/2026-06-24-...-token-consumption-surges` and `https://www.gartner.com/en/newsroom/press-releases/2026-08-17-...-fivefold-through-2028`: both return HTTP 403 to automated clients (attempted 2026-09-05 through both the fetch tool and curl with full browser headers). Gartner blocks non-interactive access, and its research notes sit behind a paid client login regardless.
- Searches for the exact title string, for "Gartner" with "5-30x" and "token consumption per task", and for Gartner research-note titles on agentic AI token cost. None returned a Gartner document with this or a closely similar title.
- `https://www.spheron.network/blog/agentic-ai-inference-cost-2026/`, retrieved 2026-09-05. This is one of the secondary pages carrying the figure. It attributes "agentic AI consumes 5 to 30 times more tokens per task than a standard chatbot exchange" to "Gartner, via NeuralWired" and links to a NeuralWired article of 2026-06-20, not to Gartner. It names no Gartner document, ID, date or URL.

What this means. The **substance** of the claim does circulate widely and is
consistently attributed to Gartner: the 5-to-30-times figure appears across
several independent industry pages. But every one of those is a secondary source
citing another secondary source, and the chain never terminates at a Gartner
document. Separately, two genuine Gartner press releases on adjacent claims do
exist by title: "Gartner Predicts AI Inference Costs Per Agentic Workflow Will
Increase More Than Fivefold Through 2028" (2026-08-17) and "Gartner Predicts AI
Coding Costs Will Surpass Average Developer's Salary by 2028 as Token
Consumption Surges" (2026-06-24). Neither is the document this entry describes,
and neither could be read directly.

Note also that the recorded access date, 2026-06-10, precedes both of those
press releases.

No corrected entry is supplied: there is nothing verified to correct it to. Three
options for the author, in order of preference:

1. Locate the actual Gartner note through institutional Gartner access, and cite
   it with its real title, document ID and date.
2. Re-point the citation at one of the two press releases above, whose titles are
   confirmed, after reading the release and checking it supports the sentence it
   is attached to.
3. Cite the figure to a named secondary source with its own URL and access date,
   and attribute it in the prose as a figure reported by that source.

A reviewer who tries to follow this citation as it stands will not find
anything, and an unfindable industry citation attached to a quantitative claim is
the kind of thing that draws a comment.

---

## anthropic2025economicindex

Current entry:

```bibtex
@misc{anthropic2025economicindex,
  title={The Anthropic Economic Index},
  author={{Anthropic}},
  year={2025},
  howpublished={\url{https://www.anthropic.com/news/the-anthropic-economic-index}},
  note={Accessed 2026}
}
```

**Classification: VERIFIED**

The URL is live (HTTP 200), the publisher is Anthropic, and the year 2025 is
correct: the page carries a publication date of 10 February 2025. The page
announces the Economic Index, an effort to measure AI use across the economy from
anonymized Claude conversations, and releases a first report plus an open-source
dataset.

Two title forms coexist on the page, and both are legitimate. The HTML
`<title>` and the Open Graph title read "Introducing the Anthropic Economic
Index"; the on-page `<h1>` reads "The Anthropic Economic Index". The entry
matches the `<h1>`, so it is not wrong. If the author prefers the form a reader
will see in a browser tab or a shared link, "Introducing the Anthropic Economic
Index" is the alternative.

One improvement, not an error: `note={Accessed 2026}` gives a year where a date
belongs. For a web citation the access stamp is the whole basis of the claim
that the page said what it is quoted as saying, so it should be a full date.

Evidence:

- `https://www.anthropic.com/news/the-anthropic-economic-index`, retrieved 2026-09-05. HTTP 200. `<title>`: "Introducing the Anthropic Economic Index \ Anthropic"; `og:title`: "Introducing the Anthropic Economic Index"; `<h1>`: "The Anthropic Economic Index". Publication date 10 February 2025.

Suggested tightening (dates only, no factual change):

```bibtex
@misc{anthropic2025economicindex,
  title={The Anthropic Economic Index},
  author={{Anthropic}},
  year={2025},
  howpublished={\url{https://www.anthropic.com/news/the-anthropic-economic-index}},
  note={Published 2025-02-10. Accessed 2026-09-05}
}
```

---

## bucinca2021trust

Current entry:

```bibtex
@article{bucinca2021trust,
  title={To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on {AI} in {AI}-assisted Decision-making},
  author={Bu{\c{c}}inca, Zana and Malaya, Maja Barbara and Gajos, Krzysztof Z.},
  journal={Proceedings of the ACM on Human-Computer Interaction (CSCW)},
  year={2021},
  doi={10.1145/3449287}
}
```

**Classification: VERIFIED**

Title matches the article's own title page character for character, including
the subtitle and the hyphenation of "AI-assisted Decision-making". All three
authors and the cedilla in Buçinca are correct. Journal, year and DOI are
correct.

Missing fields the record supports, none of them wrong as absent but all of them
worth adding for a submission: `volume={5}`, `number={CSCW1}`,
`articleno={188}`, `numpages={21}`, `month={apr}`,
`publisher={Association for Computing Machinery}`.

Evidence:

- Crossref API record for `10.1145/3449287`, retrieved 2026-09-05: title "To Trust or to Think", authors Zana Buçinca, Maja Barbara Malaya, Krzysztof Z. Gajos, container "Proceedings of the ACM on Human-Computer Interaction", volume 5, issue CSCW1, pages 1--21, issued 2021-04-13, publisher ACM.
- Author's copy of the published PDF, `https://www.eecs.harvard.edu/~kgajos/papers/2021/bucinca21trust.pdf`, retrieved 2026-09-05, text extracted locally. Its own ACM Reference Format block reads: "Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos. 2021. To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. Proc. ACM Hum.-Comput. Interact. 5, CSCW1, Article 188 (April 2021), 21 pages."
- `https://dl.acm.org/doi/10.1145/3449287` returned HTTP 403 to automated clients on 2026-09-05; the two sources above were used instead and agree with each other.

---

## skitka1999automation

Current entry:

```bibtex
@article{skitka1999automation,
  title={Does Automation Bias Decision-making?},
  author={Skitka, Linda J. and Mosier, Kathleen L. and Burdick, Mark},
  journal={International Journal of Human-Computer Studies},
  volume={51},
  number={5},
  pages={991--1006},
  year={1999}
}
```

**Classification: VERIFIED**

Title, all three authors, journal, volume 51, issue 5, pages 991--1006 and year
1999 all match the publisher record. The publication month is November 1999.

The publisher sets the title in sentence case, "Does automation bias
decision-making?"; the entry uses title case. That is a bibliography-style
choice, not an error.

Adding `doi={10.1006/ijhc.1999.0252}` would improve the entry.

Evidence:

- Crossref API record for `10.1006/ijhc.1999.0252`, retrieved 2026-09-05: title "Does automation bias decision-making?", authors Linda J. Skitka, Kathleen L. Mosier, Mark Burdick, International Journal of Human-Computer Studies, volume 51, issue 5, pages 991-1006, issued 1999-11.
- `https://www.sciencedirect.com/science/article/pii/S107158199990252X` and `https://dl.acm.org/doi/abs/10.1006/ijhc.1999.0252` both returned HTTP 403 to automated clients on 2026-09-05; the Crossref record was used instead.

---

## qu2024recursive

Current entry:

```bibtex
@inproceedings{qu2024recursive,
  title={Recursive Introspection: Teaching Language Model Agents How to Self-Improve},
  author={Qu, Yuxiao and Zhang, Tianjun and Garg, Naman and Kumar, Aviral},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2024},
  note={arXiv:2407.18219}
}
```

**Classification: VERIFIED**

Title, all four authors in order, venue, year and arXiv identifier are all
correct. The paper is in the NeurIPS 2024 main conference track.

Optional additions from the publisher BibTeX: `volume={37}`,
`pages={55249--55285}`, `publisher={Curran Associates, Inc.}`,
`doi={10.52202/079017-1754}`.

Evidence:

- `https://proceedings.neurips.cc/paper_files/paper/2024/hash/639d992f819c2b40387d4d5170b8ffd7-Abstract-Conference.html` and its BibTeX file `.../639d992f819c2b40387d4d5170b8ffd7-Bibtex-Conference.bib`, both retrieved 2026-09-05. Publisher BibTeX read in full: Advances in Neural Information Processing Systems, volume 37, pages 55249--55285, 2024, Curran Associates, DOI 10.52202/079017-1754.
- `https://arxiv.org/abs/2407.18219`, retrieved 2026-09-05. Four-author list, v1 2024-07-25.

---

## fanous2025syceval

Current entry:

```bibtex
@inproceedings{fanous2025syceval,
  title={{SycEval}: Evaluating {LLM} Sycophancy},
  author={Fanous, Aaron and Goldberg, Jacob and Agarwal, Ank A. and Lin, Joanna and Zhou, Aaron and Daneshjou, Roxana and Koyejo, Sanmi},
  booktitle={Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES)},
  year={2025},
  note={arXiv:2502.08177}
}
```

**Classification: FIELD ERRORS**

Title, venue, year and arXiv identifier are correct. The author list has one
wrong given name and, more consequentially, omits two authors who appear on the
published version.

| Field | Current value | Correct value |
|---|---|---|
| author (5th) | `Zhou, Aaron` | `Zhou, Anson` |
| author (list) | 7 authors | 9 authors on the published AIES version: adds `Xu, Sonnet` and `Bikia, Vasiliki` between Zhou and Daneshjou |
| volume / pages / doi | absent | volume 8, issue 1, pages 893--900, DOI `10.1609/aies.v8i1.36598` |

**Two sources disagree, and the disagreement is real, not an extraction error.**
The published AIES proceedings record lists nine authors: Aaron Fanous, Jacob
Goldberg, Ank Agarwal, Joanna Lin, Anson Zhou, Sonnet Xu, Vasiliki Bikia, Roxana
Daneshjou, Sanmi Koyejo. The arXiv record (checked at v4, 19 September 2025)
lists seven, omitting Sonnet Xu and Vasiliki Bikia. Both were read directly.

Since the entry cites the AIES proceedings, the published nine-author list is the
one that belongs in it. If the author would rather cite the preprint, the entry
type and venue would have to change to match, and the seven-author list would
then be correct for that version. Mixing the arXiv author list with the AIES
venue, which is the current state, is the one combination that is wrong either
way.

The given name "Aaron Zhou" appears in neither source; both give Anson Zhou. Note
that the first author is Aaron Fanous, so this looks like a name that migrated
down the list.

Evidence:

- `https://ojs.aaai.org/index.php/AIES/article/view/36598`, retrieved 2026-09-05. Published record: nine authors as listed, Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, volume 8, issue 1, pages 893--900, 2025, DOI 10.1609/aies.v8i1.36598.
- `https://arxiv.org/abs/2502.08177`, retrieved 2026-09-05. Seven authors, all Stanford; v1 2025-02-12 through v4 2025-09-19; comments field reads "AIES 2025".

Corrected entry (published version):

```bibtex
@inproceedings{fanous2025syceval,
  title={{SycEval}: Evaluating {LLM} Sycophancy},
  author={Fanous, Aaron and Goldberg, Jacob and Agarwal, Ank A. and Lin, Joanna and Zhou, Anson and Xu, Sonnet and Bikia, Vasiliki and Daneshjou, Roxana and Koyejo, Sanmi},
  booktitle={Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES)},
  volume={8},
  number={1},
  pages={893--900},
  year={2025},
  doi={10.1609/aies.v8i1.36598},
  note={arXiv:2502.08177}
}
```

---

## ye2024justice

Current entry:

```bibtex
@article{ye2024justice,
  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},
  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and others},
  journal={arXiv preprint arXiv:2410.02736},
  year={2024}
}
```

**Classification: FIELD ERRORS**

Title matches character for character, the ten named authors are correct and in
order, and the arXiv identifier is correct. Two problems.

| Field | Current value | Correct value |
|---|---|---|
| entry type / venue | `@article`, `journal={arXiv preprint arXiv:2410.02736}` | `@inproceedings`, published at ICLR 2025 (the Thirteenth International Conference on Learning Representations) |
| year | `2024` | `2025` if cited as the ICLR paper |
| author | `and others` (10 of 12 named) | 12 authors; adds `Chawla, Nitesh V.` and `Zhang, Xiangliang` |

The paper was accepted to and published at ICLR 2025. The arXiv abstract page
carries no journal reference, which is presumably why it was recorded as a
preprint, but the ICLR proceedings entry exists and was read directly.

Note that changing the year to 2025 makes the key `ye2024justice` inconsistent
with its own year field, exactly the situation flagged under `laban2025lost`. The
author can either rename the key to `ye2025justice` and update the citations in
`sections/`, or keep the key and accept the mismatch.

Evidence:

- `https://arxiv.org/abs/2410.02736`, retrieved 2026-09-05. Full 12-author list; v1 2024-10-03, v2 2024-10-04; no journal-ref.
- `https://proceedings.iclr.cc/paper_files/paper/2025/hash/fdca08d371e4b6c031397909e20043bd-Abstract-Conference.html`, retrieved 2026-09-05. Published at ICLR 2025, title and 12-author list confirmed.

Corrected entry:

```bibtex
@inproceedings{ye2025justice,
  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},
  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},
  booktitle={Proceedings of the Thirteenth International Conference on Learning Representations (ICLR)},
  year={2025},
  note={arXiv:2410.02736}
}
```

---

## Summary table

| # | BibTeX key | Classification |
|---|---|---|
| 1 | sharma2024towards | FIELD ERRORS |
| 2 | zhao2021calibrate | VERIFIED |
| 3 | kim2024language | NOT FOUND |
| 4 | koo2024benchmarking | FIELD ERRORS |
| 5 | anthropic2025prompting | FIELD ERRORS |
| 6 | bai2022training | VERIFIED |
| 7 | thompson2026aicost | FIELD ERRORS |
| 8 | openai2025sycophancy | FIELD ERRORS |
| 9 | zhang2020dialogpt | FIELD ERRORS |
| 10 | laban2025lost | FIELD ERRORS |
| 11 | gartner2026agentic | UNVERIFIABLE |
| 12 | anthropic2025economicindex | VERIFIED |
| 13 | bucinca2021trust | VERIFIED |
| 14 | skitka1999automation | VERIFIED |
| 15 | qu2024recursive | VERIFIED |
| 16 | fanous2025syceval | FIELD ERRORS |
| 17 | ye2024justice | FIELD ERRORS |

## Counts

| Classification | Count |
|---|---|
| VERIFIED | 6 |
| FIELD ERRORS | 9 |
| UNVERIFIABLE | 1 |
| NOT FOUND | 1 |
| **Total** | **17** |

## Notes for the author

Three items need a decision rather than a mechanical edit.

**kim2024language has no referent.** The title does not exist, the arXiv ID
belongs to a physics paper, and the author list is Prometheus 2's with one name
corrupted. Whatever claim this citation supports in the manuscript body is
currently unsupported, and the fix is not a corrected entry but a decision about
what work was meant and whether that work makes the claim.

**gartner2026agentic cannot be followed by a reader.** No URL, no document ID, no
date, and no Gartner document with that title could be found. The figure it
carries is quantitative and circulates only through secondary sources.

**Four keys now disagree with their own year fields** if the corrections are
accepted: laban2025lost becomes a 2026 paper, ye2024justice becomes 2025, and
sharma2024towards and koo2024benchmarking change venue but keep their years.
Renaming a key means updating every citation of it in `paper/sections/`. Whether
to rename or to keep the key and accept the mismatch is a matter of preference,
but it should be decided once and applied consistently.

Two entries in this set are affected by ICLR conference-number confusion, which
suggests it is worth checking the same fields on the ICLR entries outside this
chunk. For reference: ICLR 2024 is the Twelfth, ICLR 2025 the Thirteenth, ICLR
2026 the Fourteenth.
