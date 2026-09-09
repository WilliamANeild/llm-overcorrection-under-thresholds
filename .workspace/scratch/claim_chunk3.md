# Claim-verification worklist, chunk 3

7 sentences, 15 claim-source pairs.

## 3.1  [related_work_v2]

**The sentence as written:**

> \citet{huang2024large} report that without external feedback models struggle to correct their own reasoning and at times degrade it, and that apparent gains often trace to oracle labels or to more informative prompts.

**Cited works:**

```bibtex
@inproceedings{huang2024large,
  title={Large Language Models Cannot Self-Correct Reasoning Yet},
  author={Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
  booktitle={The Twelfth International Conference on Learning Representations (ICLR)},
  year={2024},
  note={arXiv:2310.01798}
}
```

## 3.2  [related_work_v2]

**The sentence as written:**

> The limit appears to lie in error detection rather than error correction: \citet{tyen2024llms} find that models cannot reliably locate their own reasoning errors but can fix them once the location is supplied, and \citet{tsui2025selfcorrection} document a self-correction blind spot in which models repair errors introduced by others while overlooking their own.

**Cited works:**

```bibtex
@inproceedings{tsui2025selfcorrection,
  title={Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models},
  author={Tsui, Ken},
  booktitle={Proceedings of the Conference on Language Modeling (COLM)},
  year={2026},
  note={arXiv:2507.02778}
}
```
```bibtex
@article{tyen2024llms,
  title={{LLMs} Cannot Find Reasoning Errors, but Can Correct Them Given the Error Location},
  author={Tyen, Gladys and Mansoor, Hassan and C{\u{a}}rbune, Victor and Chen, Peter and Mak, Tony},
  journal={Findings of the Association for Computational Linguistics: ACL 2024},
  year={2024},
  note={arXiv:2311.08516}
}
```

## 3.3  [related_work_v2]

**The sentence as written:**

> Reliable self-correction correspondingly depends on a strong external verifier or on additional training rather than on intrinsic prompting \cite{zhang2024small, qu2024recursive}.

**Cited works:**

```bibtex
@inproceedings{qu2024recursive,
  title={Recursive Introspection: Teaching Language Model Agents How to Self-Improve},
  author={Qu, Yuxiao and Zhang, Tianjun and Garg, Naman and Kumar, Aviral},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2024},
  note={arXiv:2407.18219}
}
```
```bibtex
@article{zhang2024small,
  title={Small Language Models Need Strong Verifiers to Self-Correct Reasoning},
  author={Zhang, Yunxiang and Khalifa, Muhammad and Logeswaran, Lajanugen and Kim, Jaekyeom and Lee, Moontae and Lee, Honglak and Wang, Lu},
  journal={Findings of the Association for Computational Linguistics: ACL 2024},
  year={2024},
  note={arXiv:2404.17140}
}
```

## 3.4  [related_work_v2]

**The sentence as written:**

> A critical survey by \citet{kamoi2024selfcorrection} synthesizes these results and locates the bottleneck in feedback generation rather than in the capacity to revise, the seam on which our finding sits \cite{shinn2023reflexion}.

**Cited works:**

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
```bibtex
@inproceedings{shinn2023reflexion,
  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
  author={Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  year={2023}
}
```

## 3.5  [related_work_v2]

**The sentence as written:**

> Reasoning models continue generating past the point at which their answer is complete and degrade it through redundant self-correction \cite{chen2024overthinking, chen2025overthinking}, and test-time scaling produces non-monotonic accuracy that rises and then falls as further computation introduces variance \cite{ghosal2025overthinking}.

**Cited works:**

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
```bibtex
@article{chen2025overthinking,
  title={The Evolution of Thought: Tracking {LLM} Overthinking via Reasoning Dynamics Analysis},
  author={Wei, Zihao and Pang, Liang and Liu, Jiahao and Shi, Wenjie and Deng, Jingcheng and Xu, Shicheng and Duan, Zenghao and Sun, Fei and Shen, Huawei and Cheng, Xueqi},
  journal={arXiv preprint arXiv:2508.17627},
  year={2025}
}
```
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

## 3.6  [related_work_v2]

**The sentence as written:**

> Knowing when to stop is now treated as an open problem in its own right \cite{sui2025efficient}.

**Cited works:**

```bibtex
@article{sui2025efficient,
  title={Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models},
  author={Sui, Yang and Chuang, Yu-Neng and Wang, Guanchu and Zhang, Jiamu and Zhang, Tianyi and Yuan, Jiayi and Liu, Hongyi and Wen, Andrew and Zhong, Shaochen and Zou, Na and Chen, Hanjie and Hu, Xia},
  journal={Transactions on Machine Learning Research (TMLR)},
  year={2025},
  note={arXiv:2503.16419}
}
```

## 3.7  [related_work_v2]

**The sentence as written:**

> Instruction-tuned models exhibit sycophancy, agreeing with users and avoiding disagreement even when holding firm would be more helpful \cite{perez2023discovering, sharma2024towards, wei2024simple}, a tendency embedded deeply enough in preference training that a 2025 model update was rolled back for it \cite{openai2025sycophancy}.

**Cited works:**

```bibtex
@misc{openai2025sycophancy,
  title={Sycophancy in {GPT}-4o: What Happened and What We're Doing About It},
  author={{OpenAI}},
  year={2025},
  howpublished={\url{https://openai.com/index/sycophancy-in-gpt-4o/}},
  note={Published 2025-04-29. Accessed 2026-09-05}
}
```
```bibtex
@inproceedings{perez2023discovering,
  title={Discovering Language Model Behaviors with Model-Written Evaluations},
  author={Perez, Ethan and Ringer, Sam and Luko{\v{s}}i{\=u}t{\.e}, Kamil{\.e} and Nguyen, Karina and Chen, Edwin and Heiner, Scott and Pettit, Craig and Olsson, Catherine and Kundu, Sandipan and Kadavath, Saurav and others},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2023},
  pages={13387--13434},
  year={2023}
}
```
```bibtex
@inproceedings{sharma2024towards,
  title={Towards Understanding Sycophancy in Language Models},
  author={Sharma, Mrinank and Tong, Meg and Korbak, Tomasz and Duvenaud, David and Askell, Amanda and Bowman, Samuel R. and Cheng, Newton and Durmus, Esin and Hatfield-Dodds, Zac and Johnston, Scott R. and Kravec, Shauna and Maxwell, Timothy and McCandlish, Sam and Ndousse, Kamal and Rausch, Oliver and Schiefer, Nicholas and Yan, Da and Zhang, Miranda and Perez, Ethan},
  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
  year={2024},
  note={arXiv:2310.13548}
}
```
```bibtex
@article{wei2024simple,
  title={Simple Synthetic Data Reduces Sycophancy in Large Language Models},
  author={Wei, Jerry and Huang, Da and Lu, Yifeng and Zhou, Denny and Le, Quoc V.},
  journal={arXiv preprint arXiv:2308.03958},
  year={2023}
}
```
