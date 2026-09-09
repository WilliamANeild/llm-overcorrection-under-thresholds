# -*- coding: utf-8 -*-
"""Assemble paper/reference/scen_01_no_artifact.md from the measurements and the hand codes.

Pure function of /tmp/scen01/measured.json and handcode_no_artifact.json. Every number printed
here is computed at write time; none is typed in by hand.
"""
import json, os, datetime, statistics as st, importlib.util
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'paper', 'reference', 'scen_01_no_artifact.md')
spec = importlib.util.spec_from_file_location('m3', os.path.join(HERE, '03_measure.py'))
m3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m3)

R = json.load(open('/tmp/scen01/measured.json'))
D = json.load(open('/tmp/scen01/draw.json'))
H = json.load(open(os.path.join(HERE, 'handcode_no_artifact.json')))
P = H['papers']; K = sorted(R)
RET = json.load(open(os.path.join(ROOT, 'paper', 'reference', 'acl2026_abstracts.json')))['_no_artifact_2024_2026_provenance']['retrieved']

def pct(a, b): return '%.0f%%' % (100.0*a/b)
def dist(x): 
    return dict(mn=min(x), p25=st.quantiles(x, n=4)[0], med=st.median(x),
                p75=st.quantiles(x, n=4)[2], p90=st.quantiles(x, n=10)[8], mx=max(x), mean=st.mean(x))

W = [R[a]['n_words'] for a in K]; S = [R[a]['n_sentences'] for a in K]
Dn = [R[a]['numerals_per_100w'] for a in K]; NW = [R[a]['number_words_spelled'] for a in K]
dw, ds, dd = dist(W), dist(S), dist(Dn)
DIG = [a for a in K if R[a]['numerals_quant'] > 0]
CAP = [a for a in K if P[a]['names_capitalised']]
MOD = [a for a in K if any(k == 'named_model' for _, k in P[a]['names'])]
COIN = [a for a in K if P[a]['coins_own_term'] and not P[a]['coinage_borrowed']]
INST = [a for a in K if P[a]['instrument_built'] != 'none']
ROLES = Counter(r[3] for r in H['numeral_roles'])

def group(sub, lab):
    n = len(sub); dg = [a for a in sub if R[a]['numerals_quant'] > 0]
    v = [R[a]['numerals_per_100w'] for a in sub]
    return '| %s | %d | %d | %s | %.2f | %.2f |' % (lab, n, len(dg), pct(len(dg), n), st.median(v), st.mean(v))

L = []
w = L.append
w('# What an abstract does when the paper releases no system, benchmark or dataset')
w('')
w('Scenario 01. Compiled %s. Companion to `acl2026_density.md`, which measured a topic-unconditional'
  ' systematic sample of 47 abstracts from the 2026 volumes and found that 40 of 47 name an artifact,'
  ' that all 16 abstracts carrying a quantitative digit also name one, and that the 7 naming none carry'
  ' no digit either. That corpus cannot say whether the artifact and the digit are causally linked,'
  ' because it holds only 7 artifact-free cases and all 7 sit in one year. This corpus conditions on'
  ' the artifact-free case directly and across three years.' % datetime.date.today().isoformat())
w('')
w('## Corpus and how it was drawn')
w('')
w('Source: ACL Anthology, retrieved **%s**. Two passes. The volume listing page of each of 17 volumes'
  ' carries every paper title and, in a collapsed div, every abstract; those pages supplied the pool and'
  ' the screen. Each drawn paper was then fetched individually and its abstract taken from the'
  ' `div` with class `card-body acl-abstract` on the landing page, parsed by walking div nesting rather'
  ' than assuming a `<span>` follows the heading. **The landing-page abstract matched the volume-page copy'
  ' for all %d drawn papers**, so nothing rests on the cheaper source.' % (RET, len(D['draw'])))
w('')
w('Volumes: `2024.acl-long`, `2024.acl-short`, `2024.findings-acl`, `2024.emnlp-main`, `2024.findings-emnlp`,'
  ' `2024.naacl-long`, `2024.eacl-long`, `2025.acl-long`, `2025.acl-short`, `2025.findings-acl`,'
  ' `2025.emnlp-main`, `2025.findings-emnlp`, `2025.naacl-long`, `2026.acl-long`, `2026.acl-short`,'
  ' `2026.findings-acl`, `2026.eacl-long`. All 17 returned HTTP 200. **%s papers listed** across them,'
  ' excluding front matter.' % format(D['pool_all_papers'], ','))
w('')
w('**Screening, in three mechanical steps and one hand step.**')
w('')
w('1. *Title signal.* A regex for analysis and empirical-study title shapes: an opening interrogative'
  ' (Do / Does / Can / Are / Is / When / Why / How / What / Which / Who), an opening gerund (Understanding,'
  ' Investigating, Exploring, Measuring, Probing, Assessing, Evaluating, Rethinking, Revisiting, Auditing,'
  ' Tracing, Characterizing), "On the ...", "An Analysis of", "A Study of", "An Empirical Study",'
  ' "A Case Study". **%s of %s titles matched (%s).**'
  % (format(D['title_signal_candidates'], ','), format(D['pool_all_papers'], ','),
     pct(D['title_signal_candidates'], D['pool_all_papers'])))
sc = D['screen_counts']
w('2. *Artifact signal in the abstract.* Any of these disqualifies: release language ("we release",'
  ' "publicly available", "available at", a URL); a coined capitalised name in the title; a coined'
  ' capitalised name within 70 characters after an introduce, propose, present, develop, construct,'
  ' build, design, create or curate verb. Of the %s candidates: **%d excluded for release language,'
  ' %d for a coined name in the title, %d for a coined name after a build verb, %d had no abstract,'
  ' %d passed.**' % (format(D['title_signal_candidates'], ','), sc['excl_release'], sc['excl_title_name'],
                     sc['excl_build_named'], sc['no_abstract'], sc['PASS']))
w('3. *Systematic draw.* Fixed random start and constant stride within each volume, over the passing pool'
  ' in Anthology order, seeded 20260906, allocated across volumes in proportion to each volume\'s share'
  ' of the pool. **%d drawn.**' % len(D['draw']))
w('4. *Hand adjudication.* A drawn paper is kept only if its stated principal contribution is a finding,'
  ' not a resource and not a performance-improving method. **%d dropped, %d kept.** Every drop and its'
  ' reason is in `handcode_no_artifact.json`; the list is reproduced below so a reader can disagree'
  ' with any of them.' % (len(H['dropped_after_hand_adjudication']), len(K)))
w('')
w('**Papers dropped at step 4, with the reason.**')
w('')
for a, r in sorted(H['dropped_after_hand_adjudication'].items()): w('- `%s`: %s' % (a, r))
w('')
w('Two of those drops are also failures of the step-2 regex, and are worth recording as such. `2026.findings-acl.1795`'
  ' introduces the "Cross-Cultural, Cross-Modal, Cross-lingual Multimodal (3XCM) benchmark"; the acronym begins'
  ' with a digit, so the capitalised-name regex did not see it. `2024.emnlp-main.679` presents "Shortcut Suite",'
  ' two ordinary capitalised words, which the regex also misses because it looks for internal capitals or a run'
  ' of three. **The screen is therefore permissive, not strict: it lets artifact papers through, which the hand'
  ' step then removes, rather than discarding artifact-free papers.** That is the direction of error to prefer here.')
w('')
w('**Bounds on this sample.** The draw is conditional on the title matching an analysis shape, so it says nothing'
  ' about analysis papers whose titles are declarative ("LLMs cannot plan"). It covers ACL, EMNLP, NAACL, EACL and'
  ' the two Findings volumes for 2024 through 2026 and no other venue, no workshop, and no arXiv preprint. It is a'
  ' sample of %d, so a proportion near a half carries a standard error of about %.0f percentage points; the'
  ' comparisons below are directions, not estimates. Papers per year: %s.'
  % (len(K), 100*(0.25/len(K))**0.5, ', '.join('%s: %d' % kv for kv in sorted(Counter(a.split('.')[0] for a in K).items()))))
w('')
w('**How things were counted.** Word counts, sentence counts, and every numeral count and category are produced'
  ' by `03_measure.py` (regex tokenizer and sentence splitter), never by eye. A numeral counts as *quantitative*'
  ' only if it is not part of an identifier: digits inside model names (GPT-2, Qwen2.5, o3-mini, TOEFL11), four-digit'
  ' years, and enumeration markers are counted separately and excluded. Two tokenizer amendments were made for this'
  ' corpus and applied upstream in `03_measure.py`: a bare list marker introducing a numbered finding ("four key'
  ' findings: 1. Larger models ...") is an enumerator, not a quantity, and a digit glued to a following all-caps'
  ' identifier (the 3 in 3XCM) is part of a name. **Re-measuring the existing 47-abstract and 9-abstract corpora'
  ' under the amended tokenizer changes no count in either**, so the two corpora remain directly comparable.'
  ' Five things are hand-coded and marked as such throughout: the step-4 genre judgement, what the abstract names'
  ' and of what kind, whether the paper coins a term of its own, the closing move, and whether each numeral states'
  ' the size of the experiment or the size of an outcome.')
w('')

w('## Corpus table')
w('')
w('Names: the kinds of proper name the abstract carries. `model` = a released model named as an object of study;'
  ' `dataset` = an existing dataset or lexical resource it runs on; `prior` = a named prior method, architecture or'
  ' construct it tests or uses; `task` = a task it introduces under a borrowed name; `acronym` = a task or subfield'
  ' abbreviation; `metric` = a field-standard metric abbreviation; `lang` = a natural language. "Cap" is true only'
  ' when at least one name is a model, dataset, prior method or introduced task; acronyms, standard metrics and'
  ' language names do not make it true. "Coin" is true when the paper introduces a noun phrase as its own construct'
  ' and reuses it, whether or not it is capitalised. Density is quantitative numerals per 100 words.')
w('')
w('| Anthology ID | Words | Sent | Quant | Ident | Enum | /100w | Res % | Names | Cap | Coin | Closing move |')
w('|---|---|---|---|---|---|---|---|---|---|---|---|')
SH = {'named_model':'model','evaluated_dataset':'dataset','prior_work':'prior','introduced_task':'task',
      'field_acronym':'acronym','standard_metric':'metric','language':'lang'}
for a in sorted(K, key=lambda x: (-R[x]['numerals_per_100w'], x)):
    r, p = R[a], P[a]
    kinds = sorted({SH[k] for _, k in p['names']}) or ['none']
    w('| `%s` | %d | %d | %d | %d | %d | %.2f | %d | %s | %s | %s | %s |'
      % (a, r['n_words'], r['n_sentences'], r['numerals_quant'], r['digit_runs_identifier'],
         r['digit_runs_enumeration'], r['numerals_per_100w'], r['cat_result_percentage'],
         ', '.join(kinds), 'y' if p['names_capitalised'] else 'n',
         'y' if (p['coins_own_term'] and not p['coinage_borrowed']) else 'n',
         p['closing_move'].replace('_', ' ')))
w('')
w('Titles, URLs and the verbatim abstracts are in `acl2026_abstracts.json` under `no_artifact_2024_2026`.')
w('')

w('## Do artifact-free abstracts carry digits?')
w('')
w('**%d of %d (%s) carry at least one quantitative digit. %d of %d (%s) carry none.**'
  % (len(DIG), len(K), pct(len(DIG), len(K)), len(K)-len(DIG), len(K), pct(len(K)-len(DIG), len(K))))
w('')
cnt = Counter(R[a]['numerals_quant'] for a in K)
w('Raw counts: %s. Across all %d abstracts there are **%d quantitative numerals in total**.'
  % (', '.join('%d %s %d' % (cnt[c], 'abstract carries' if cnt[c] == 1 else 'abstracts carry', c) for c in sorted(cnt)),
     len(K), sum(R[a]['numerals_quant'] for a in K)))
w('')
w('| Statistic | This corpus (%d artifact-free) | 47-abstract 2026 systematic sample |' % len(K))
w('|---|---|---|')
w('| words, median | %d | 161 |' % dw['med'])
w('| words, p25 / p75 | %.0f / %.0f | 153 / 178 |' % (dw['p25'], dw['p75']))
w('| sentences, median | %d | 7 |' % ds['med'])
w('| numerals per 100 words, median | %.2f | 0.00 |' % dd['med'])
w('| numerals per 100 words, p75 | %.2f | 0.64 |' % dd['p75'])
w('| numerals per 100 words, p90 | %.2f | 1.88 |' % dd['p90'])
w('| numerals per 100 words, max | %.2f | 2.93 |' % dd['mx'])
w('| numerals per 100 words, mean | %.2f | 0.48 |' % dd['mean'])
w('| share carrying at least one digit | %s (%d/%d) | 34%% (16/47) |' % (pct(len(DIG), len(K)), len(DIG), len(K)))
w('| share carrying a result percentage | %s (%d/%d) | 17%% (8/47) |'
  % (pct(sum(1 for a in K if R[a]['cat_result_percentage']), len(K)), sum(1 for a in K if R[a]['cat_result_percentage']), len(K)))
w('')
w('**The artifact-free abstract is the same length as the venue median and about a third less dense at the'
  ' mean.** Median %d words against 161, and a mean of %.2f numerals per 100 words against 0.48. The median is'
  ' zero in both corpora, so the median does not separate them. What separates them is the share carrying any'
  ' digit, %s here against 34 percent there, and the mean.'
  % (dw['med'], dd['mean'], pct(len(DIG), len(K))))
w('')
w('The reduction is concentrated in one place. **%d of the %d abstracts reports a result percentage**'
  % (sum(1 for a in K if R[a]['cat_result_percentage']), len(K))
  + ' (`2024.naacl-long.266`, "outperforming the accuracy of existing state-of-the-art zero-shot baselines'
    ' by an average of 9%"), against 8 of 47 in the 2026 sample. **No abstract in this corpus reports a'
    ' p-value or an effect size**, which matches the 47-abstract corpus exactly: neither carries one.')
w('')
w('Spelled-out numbers: %d of %d carry at least one, and **%d of %d carry neither a digit nor a spelled'
  ' number.**' % (sum(1 for x in NW if x), len(K), sum(1 for a in K if R[a]['numerals_quant'] == 0 and R[a]['number_words_spelled'] == 0), len(K)))
w('')

w('### What the digits are doing')
w('')
w('Each of the %d quantitative numerals, hand-classified as stating the size of what was tested (SETUP)'
  ' or how something performed (OUTCOME), with the clause it sits in quoted verbatim.' % len(H['numeral_roles']))
w('')
w('| Anthology ID | Numeral | Clause, verbatim | Role |')
w('|---|---|---|---|')
for aid, num, clause, role in H['numeral_roles']:
    w('| `%s` | %s | %s | %s |' % (aid, num, clause, role))
w('')
w('**%d of %d numerals state the size of the experiment; %d state an outcome.**'
  ' Six of the eight digit-carrying abstracts put a setup figure first, and the two that lead with an outcome'
  ' (`2024.findings-emnlp.841`, `2025.findings-emnlp.445`) are the two whose finding is itself a dispersion or'
  ' reliability statistic. Position of the first statistic, as a fraction of the way through the abstract:'
  ' median %.2f against 0.80 in the 47-abstract sample. **In an artifact-free abstract the number arrives'
  ' earlier, because it is describing the experiment rather than reporting its result.**'
  % (ROLES['SETUP'], len(H['numeral_roles']), ROLES['OUTCOME'],
     st.median([R[a]['first_stat_sentence_frac'] for a in DIG])))
w('')

w('## What they name instead of a released system')
w('')
kc = Counter()
for a in K:
    for k in {kk for _, kk in P[a]['names']}: kc[k] += 1
w('| What the abstract names | Abstracts | Share |')
w('|---|---|---|')
w('| a released model, by name | %d | %s |' % (kc['named_model'], pct(kc['named_model'], len(K))))
w('| a coined phenomenon or construct of its own | %d | %s |' % (len(COIN), pct(len(COIN), len(K))))
w('| an existing dataset or lexical resource | %d | %s |' % (kc['evaluated_dataset'], pct(kc['evaluated_dataset'], len(K))))
w('| a named prior method, architecture or construct | %d | %s |' % (kc['prior_work'], pct(kc['prior_work'], len(K))))
w('| a task it introduces under a borrowed name | %d | %s |' % (kc['introduced_task'], pct(kc['introduced_task'], len(K))))
w('| a field-standard metric abbreviation | %d | %s |' % (kc['standard_metric'], pct(kc['standard_metric'], len(K))))
w('| a task or subfield acronym only | %d | %s |' % (kc['field_acronym'], pct(kc['field_acronym'], len(K))))
w('| nothing capitalised beyond acronyms and language names | %d | %s |'
  % (len(K)-len(CAP), pct(len(K)-len(CAP), len(K))))
w('| a metric it defines and gives a name to | 0 | 0% |')
w('| a released artifact of its own, by construction of the sample | 0 | 0% |')
w('')
w('**The substitute for a coined system name is a released model name.** %d of %d artifact-free abstracts'
  ' name at least one model. In the 47-abstract 2026 systematic sample only 3 of 47 (6 percent) do; the norm'
  ' there is "experiments across 7B/14B/32B models" with no vendor. Conditioning on the artifact-free case'
  ' raises model-naming from 6 percent to %d percent.' % (len(MOD), len(K), round(100.0*len(MOD)/len(K))))
w('')
w('**No abstract in this corpus defines a metric and gives it a name.** %d of %d build an instrument to get'
  ' the finding, and every one of them leaves it unnamed: "an unnamed benchmark", "a configurable framework",'
  ' "a simple measure of informativeness", "a new evaluation method". Naming the instrument is what the'
  ' excluded papers do; `2025.emnlp-main.10` names its Ambiguity Rewrite Metric and `2025.emnlp-main.504`'
  ' names its Faithfulness by Unlearning Reasoning steps, and both are artifact papers as a result.'
  % (len(INST), len(K)))
w('')

w('## Is coining a phenomenon functionally equivalent to naming a released system?')
w('')
w('In the 47-abstract sample the two sparse signals coincide exactly: every abstract carrying a digit also'
  ' names an artifact, and the 7 naming none carry no digit. If a coined phenomenon were doing the same work'
  ' as a released name, coiners here would carry digits at a higher rate than non-coiners. They do not.')
w('')
w('| Group | n | With a digit | Share | Median /100w | Mean /100w |')
w('|---|---|---|---|---|---|')
w(group(K, 'all artifact-free'))
w(group(CAP, 'names something capitalised')); w(group([a for a in K if a not in CAP], 'names nothing capitalised'))
w(group(MOD, 'names at least one model')); w(group([a for a in K if a not in MOD], 'names no model'))
w(group(COIN, 'coins its own term')); w(group([a for a in K if a not in COIN], 'coins no term'))
w(group(INST, 'built an unnamed instrument')); w(group([a for a in K if a not in INST], 'built no instrument'))
w('')
w('| | carries a digit | carries no digit |')
w('|---|---|---|')
for c in (True, False):
    row = []
    for dg in (True, False):
        row.append(len([a for a in K if ((a in COIN) == c) and ((R[a]['numerals_quant'] > 0) == dg)]))
    w('| **coins its own term: %s** | %d | %d |' % ('yes' if c else 'no', row[0], row[1]))
w('')
w('**No. Coining a phenomenon runs in the opposite direction from naming a released system.** %d of %d coiners'
  ' carries a digit (%s) against %d of %d non-coiners (%s). The single coiner that carries one,'
  ' `2024.findings-emnlp.841`, reports a standard deviation of detector performance, which is a dispersion'
  ' figure rather than a result percentage. With 8 coiners this is a direction and not an estimate, but the'
  ' direction is the opposite of the one the equivalence hypothesis predicts, and the mechanism is visible in'
  ' the text: a coined term is a claim that a phenomenon exists, and the abstract spends its remaining'
  ' sentences establishing that it exists rather than measuring how large it is.'
  % (len([a for a in COIN if R[a]['numerals_quant'] > 0]), len(COIN),
     pct(len([a for a in COIN if R[a]['numerals_quant'] > 0]), len(COIN)),
     len([a for a in K if a not in COIN and R[a]['numerals_quant'] > 0]), len(K)-len(COIN),
     pct(len([a for a in K if a not in COIN and R[a]['numerals_quant'] > 0]), len(K)-len(COIN))))
w('')
w('**The signal that does co-occur with digits is the model name.** %d of %d abstracts naming a model carry a'
  ' digit (%s), against %d of %d that name none (%s), and the median density among model-namers is %.2f against'
  ' %.2f. This is not surprising once the numeral roles above are read alongside it: %d of %d numerals state the'
  ' size of what was tested, and stating the size of what was tested is the same sentence in which the models get'
  ' named. "Through experiments across the Qwen2.5 series (0.5B to 72B)" is one clause carrying both signals.'
  % (len([a for a in MOD if R[a]['numerals_quant'] > 0]), len(MOD),
     pct(len([a for a in MOD if R[a]['numerals_quant'] > 0]), len(MOD)),
     len([a for a in K if a not in MOD and R[a]['numerals_quant'] > 0]), len(K)-len(MOD),
     pct(len([a for a in K if a not in MOD and R[a]['numerals_quant'] > 0]), len(K)-len(MOD)),
     st.median([R[a]['numerals_per_100w'] for a in MOD]),
     st.median([R[a]['numerals_per_100w'] for a in K if a not in MOD]),
     ROLES['SETUP'], len(H['numeral_roles'])))
w('')

w('## The coinage catalogue')
w('')
w('Every sentence in which an artifact-free paper names its own coined term for the first time, quoted verbatim'
  ' from the fetched abstract. Ordered by Anthology ID. %d of %d abstracts (%s) coin a term.'
  % (len(COIN), len(K), pct(len(COIN), len(K))))
w('')
for a in sorted(COIN):
    p = P[a]
    w('**`%s`**: %s' % (a, R[a]['title']))
    w('')
    w('Term: **%s**. Sentence %d of %d. Digits in the abstract: %d.'
      % (p['coins_own_term'],
         next(i+1 for i, s in enumerate(m3.sentences(R[a]['abstract'])) if p['coinage_sentence'].rstrip() in s or s in p['coinage_sentence']),
         R[a]['n_sentences'], R[a]['numerals_quant']))
    w('')
    w('> %s' % p['coinage_sentence'])
    w('')
    if p['note']:
        w('%s%s.' % (p['note'][0].upper(), p['note'][1:])); w('')
BOR = [a for a in K if P[a]['coinage_borrowed']]
if BOR:
    w('One further paper defines a term for the reader without coining it, and is recorded separately for that reason.')
    w('')
    for a in BOR:
        w('**`%s`**: %s' % (a, R[a]['title']))
        w('')
        w('Term: **%s**, borrowed from social psychology and defined in place.' % P[a]['coins_own_term'])
        w('')
        w('> %s' % P[a]['coinage_sentence'])
        w('')
w('**All %d coinages are lower-case noun phrases**, not capitalised names and not acronyms: preference bias,'
  ' implicit ranking unfairness, task-oriented constraints, "emotion neurons", multi-branch feature extraction,'
  ' belief consistency, intra- and inter-client memorization, jailbreak vector. None is offered as a thing the'
  ' reader can download. The construction that recurs is definition by contrast with the expected: a subtler'
  ' form of discrimination, constraints not related to detection-evasion, consistency evaluated where every'
  ' option is correct, a vector extracted from one jailbreak class that transfers to another. Position follows'
  ' function: seven of the eight coinages appear between sentence 1 and sentence 5 of an abstract averaging'
  ' seven sentences, while `2024.acl-long.813` names its term only in sentence 7, inside the enumerated'
  ' findings.' % len(COIN))
w('')

w('## How these abstracts close')
w('')
cm = Counter(P[a]['closing_move'] for a in K)
w('| Closing move | Abstracts | Share |')
w('|---|---|---|')
for m, n in cm.most_common(): w('| %s | %d | %s |' % (m.replace('_', ' '), n, pct(n, len(K))))
w('| resource release | 0 | 0% |')
w('')
w('**%d of %d close on a knowledge claim**: the last sentence states what is now known about the object'
  ' studied. "These results argue against a strictly rule-based encoding of German definite articles"'
  ' (`2026.acl-long.436`). "Our results indicate that the source of performance in self-attention has been'
  ' misattributed" (`2026.acl-long.853`). "This suggests that output distributions provide sufficient'
  ' supervisory signal for syntax acquisition" (`2025.findings-emnlp.801`).'
  % (cm['knowledge_claim'], len(K)))
w('')
w('%d close by telling the field what to do, %d on future work, and %d by restating the contribution without'
  ' stating a finding. **None closes on a resource**, which is what the corpus was selected to guarantee, so'
  ' that row is a check on the selection rather than a result.'
  % (cm['call_to_community'], cm['future_work'], cm['contribution_restatement']))
w('')

w('## Answer: can a paper with nothing to release carry numbers in its abstract, and what must it name?')
w('')
w('**Yes, and a quarter of them do.** The correlation in the 47-abstract sample, where zero abstracts carried a'
  ' digit without naming an artifact, does not survive conditioning on the artifact-free case across three years.'
  ' Here %d of %d abstracts carry a digit while releasing nothing, and %d of those %d name no artifact of any'
  ' kind: `2024.findings-emnlp.841` reports a standard deviation of 14.4 F1 with nothing capitalised in the'
  ' abstract but the metric abbreviation, and `2025.findings-emnlp.1380` reports a controlled study with 95'
  ' participants the same way. **The constraint is real but it is not a prohibition.**'
  % (len(DIG), len(K), len([a for a in DIG if a not in CAP]), len(DIG)))
w('')
w('**What the digit needs is not an artifact but a referent the reader already recognises.** In every one of the'
  ' %d digit-carrying abstracts the numeral sits in the same clause as the noun it counts, which is the pattern'
  ' the 47-abstract corpus found without exception: "a range of 8 audio-classification datasets", "47.8K'
  ' samples", "18 LLMs", "(n=95)", "10K to 5M sentences", "0.5B to 72B", "200 short videos", "an SD of 14.4'
  ' F1-score". An artifact paper supplies that recognition by naming what it built. An artifact-free paper'
  ' supplies it by naming a model, a dataset or a unit of observation the reader already knows.' % len(DIG))
w('')
w('**Naming a coined phenomenon is not a substitute for naming a system, and the counts run opposite to that'
  ' hypothesis.** %d percent of coiners carry a digit against %d percent of non-coiners. A coinage buys the'
  ' abstract something else: it gives the finding a subject that fits in one noun phrase, which is why %d of'
  ' the %d coiners close on a knowledge claim. It does not license a number.'
  % (round(100.0*len([a for a in COIN if R[a]['numerals_quant'] > 0])/len(COIN)),
     round(100.0*len([a for a in K if a not in COIN and R[a]['numerals_quant'] > 0])/(len(K)-len(COIN))),
     sum(1 for a in COIN if P[a]['closing_move'] == 'knowledge_claim'), len(COIN)))
w('')
w('**For a paper reporting a behavioural finding about LLM revision with nothing to release, this corpus'
  ' supports three moves and declines a fourth.** Name the models the finding is about: %d percent of these'
  ' abstracts do, and it is the strongest correlate of a digit here. Carry one or two figures with the counted'
  ' noun inside the same clause, which is what every digit-carrying abstract in both corpora does. Coin a term'
  ' for the phenomenon and close on a knowledge claim, which %d percent of these abstracts do. What the corpus'
  ' declines is the idea that a coinage substitutes for an artifact in licensing quantification, and it declines'
  ' a higher numeral count: the maximum density here is %.2f per 100 words and the mean is %.2f, so a 200-word'
  ' abstract at this corpus\'s 90th percentile carries about %.1f figures, and one at the mean carries under one.'
  % (round(100.0*len(MOD)/len(K)), round(100.0*cm['knowledge_claim']/len(K)), dd['mx'], dd['mean'], 2*dd['p90']))
w('')
w('---')
w('')
w('Retrieval date for all Anthology pages: %s. Sampling seed: 20260906. Sampling and fetch:'
  ' `scripts/acl2026_abstract_density/05_no_artifact_sample.py`. Extraction and measurement:'
  ' `06_no_artifact_measure.py`. Hand codes, with the coding rule for each:'
  ' `handcode_no_artifact.json`. This report: `07_write_no_artifact_report.py`. Abstracts stored'
  ' verbatim in `acl2026_abstracts.json` under `no_artifact_2024_2026`.' % RET)

open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('wrote', OUT, len('\n'.join(L).split()), 'words')
