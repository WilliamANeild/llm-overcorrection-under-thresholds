# -*- coding: utf-8 -*-
import json, statistics as st
from collections import Counter
OUT='/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/reference/acl2026_density.md'
M=json.load(open('/tmp/aclfetch/measured.json')); new,prior=M['new'],M['prior9']
code=json.load(open('/tmp/aclfetch/coding.json')); code.pop('_note')
hc=json.load(open('/tmp/aclfetch/handcodes.json')); hc.pop('_note')
for a,r in new.items():
    r['genre'],r['valence']=code[a]
    r['hv_model']=a in hc['names_specific_model']
    r['hv_dataset']=a in hc['names_eval_resource']
    r['hv_metric']=a in hc['names_metric']
    r['hv_artifact']=a not in hc['no_named_artifact']
R=list(new.values())
def q(xs):
    xs=sorted(xs); n=len(xs)
    def p(f):
        if n==1: return xs[0]
        k=(n-1)*f; i=int(k); j=min(i+1,n-1); return xs[i]+(xs[j]-xs[i])*(k-i)
    return dict(n=n,mn=xs[0],p25=p(.25),med=p(.5),p75=p(.75),p90=p(.9),mx=xs[-1],mean=sum(xs)/n)
def fq(d,f='%.2f'): return f"min {f%d['mn']} / p25 {f%d['p25']} / median {f%d['med']} / p75 {f%d['p75']} / p90 {f%d['p90']} / max {f%d['mx']} / mean {f%d['mean']}"
def pctl(xs,v):
    xs=sorted(xs); return 100*(sum(1 for x in xs if x<v)+0.5*sum(1 for x in xs if x==v))/len(xs)
dens=[r['numerals_per_100w'] for r in R]
L=[]; w=L.append
w("# Quantitative and technical density of 2026 ACL-venue abstracts\n")
w("Compiled 2026-09-06. Purpose: calibrate the abstract of a paper going to ARR in October 2026 against what abstracts in the target venues carry, after a reviewer of a 9-abstract sample said the abstract needed \"more geek and numbers\" and, scanning for its single statistic, missed it.\n")
w("## Corpus and how it was drawn\n")
w("Source: ACL Anthology landing pages, one HTTP request per paper, retrieved **2026-09-06**. The abstract was taken from the `div` with class `card-body acl-abstract` on each landing page, parsed by walking `div` nesting to the matching close rather than by assuming a `<span>` follows the heading, then stripped of markup. Abstracts are stored verbatim in `acl2026_abstracts.json`.\n")
w("**2026 volumes that exist on the Anthology** (checked directly): `2026.acl-long` (2,222 papers excluding front matter), `2026.acl-short` (74), `2026.findings-acl` (2,163), `2026.eacl-long` (394). **`2026.naacl-long` does not exist** (HTTP 404), nor do `2026.emnlp-main` or `2026.starsem-1`; no paper from those was fetched or invented.\n")
w("**Sampling.** Systematic sample with a fixed random start and a constant stride over each volume's paper list in Anthology order, seeded at 20260906 so the draw is reproducible. Target counts were 20 from `acl-long` (stride 111), 16 from `findings-acl` (stride 135), 8 from `eacl-long` (stride 49), 4 from `acl-short` (stride 18.5). This spreads the draw across the whole volume rather than taking a run of consecutive papers. 48 IDs were drawn; 47 yielded an abstract. `2026.findings-acl.1664` (microCLIP) has no abstract block on its landing page at all and is excluded rather than replaced.\n")
w("**Bound on the sample.** The draw is unconditional on topic. It was not filtered toward empirical studies of LLM behaviour, because a filtered draw cannot say what the venue norm is. Genre is recorded per paper instead so the comparison can be conditioned. The consequence is that the corpus is dominated by method papers, which is what the volumes are dominated by: 36 of 47 propose a new method or system.\n")
w("**How things were counted.** Word counts, sentence counts, every numeral count and category, and the position of the first statistic are produced mechanically by script (`measure2.py`, regex tokenizer and sentence splitter), never by eye. Three things are hand-coded, and are marked as such wherever they appear: paper genre, result valence, and the referent-attachment classification. The naming flags were script-detected and then hand-adjudicated, because \"recall\", \"calibration\" and \"agreement\" occur in these abstracts as ordinary English rather than as metric names; both counts are given.\n")
w("A numeral is counted as **quantitative** only if it is not part of an identifier. Digits inside model and dataset names (GPT-o3, Gemma-2, Llama-3-8B, MQuAKE-2002, T2I, System-2), four-digit years, and enumeration markers such as \"(1)\" and \"(2)\" are counted separately and excluded from the density measure. Both figures are reported below.\n")
# corpus table
w("## Corpus table\n")
w("Genre: M = new method or system, B = new benchmark, dataset or resource, A = empirical analysis of model behaviour, P = position. Valence: POS = the principal reported result is that the authors' method works; NEG = the principal reported result is that models fail, are brittle, or an expected effect is absent. Density is quantitative numerals per 100 words.\n")
w("| Anthology ID | Genre | Val | Words | Sent | Quant numerals | Ident/year digits | Number-words | Per 100w | Result % | First stat at sentence |")
w("|---|---|---|---|---|---|---|---|---|---|---|")
for a in sorted(new, key=lambda x:(-new[x]['numerals_per_100w'], x)):
    r=new[a]; fs=f"{r['first_stat_sentence_index']}/{r['first_stat_of_n_sentences']}" if r['first_stat_text'] else "none"
    w(f"| `{a}` | {r['genre']} | {r['valence']} | {r['n_words']} | {r['n_sentences']} | {r['numerals_quant']} | {r['digit_runs_identifier']+r['digit_runs_year']+r['digit_runs_enumeration']} | {r['number_words_spelled']} | {r['numerals_per_100w']:.2f} | {r['cat_result_percentage']} | {fs} |")
w("")
w("Titles for every ID are stored with the abstracts in `acl2026_abstracts.json` under `sample_2026_09_06`.\n")
# distributions
w("## Distribution of numerals per 100 words\n")
w(f"Across all 47 abstracts: **{fq(q(dens))}**.\n")
w(f"**{sum(d==0 for d in dens)} of 47 abstracts ({100*sum(d==0 for d in dens)/47:.0f} percent) contain no quantitative digit at all.** That is what drives the median to zero. The quartiles are therefore not a smooth spread around a typical value: the distribution is a large spike at zero and a thin tail.\n")
w("| Statistic | Quantitative numerals / 100w | All digit runs / 100w (identifiers, years, enumerators included) |")
w("|---|---|---|")
qa=q([r['digitruns_all_per_100w'] for r in R])
qd=q(dens)
for lab,k in [('minimum','mn'),('25th percentile','p25'),('median','med'),('75th percentile','p75'),('90th percentile','p90'),('maximum','mx'),('mean','mean')]:
    w(f"| {lab} | {qd[k]:.2f} | {qa[k]:.2f} |")
w("")
w(f"**Where 0.5 sits.** A density of 0.5 numerals per 100 words falls at the **{pctl(dens,0.5):.0f}th percentile**: {sum(d<=0.5 for d in dens)} of 47 abstracts ({100*sum(d<=0.5 for d in dens)/47:.0f} percent) are at or below it. In a 170-word abstract, 0.5 per 100 words is a single statistic. One statistic already puts an abstract above two thirds of this corpus.\n")
w(f"**Where 3.5 sits.** A density of 3.5 falls at the **{pctl(dens,3.5):.0f}th percentile**. **No abstract in the sample reaches it.** The maximum observed is {max(dens):.2f} ({[a for a in new if new[a]['numerals_per_100w']==max(dens)][0]}), and only {sum(d>=2.0 for d in dens)} of 47 exceed 2.0. On the all-digit-runs measure, which counts model-name and year digits too, 3.5 sits at the {pctl([r['digitruns_all_per_100w'] for r in R],3.5):.0f}th percentile and one abstract reaches 4.39. Writing to 3.5 would put an abstract outside the range this venue produces.\n")
cnt=Counter(r['numerals_quant'] for r in R)
w("Raw counts rather than rates: "+", ".join(f"{cnt[k]} abstract{'s' if cnt[k]>1 else ''} carr{'y' if cnt[k]>1 else 'ies'} {k}" for k in sorted(cnt))+" quantitative numerals. The modal abstract has zero; the modal non-zero abstract has one.\n")
w(f"Abstract length itself: {fq(q([r['n_words'] for r in R]),'%.0f')} words, {fq(q([r['n_sentences'] for r in R]),'%.0f')} sentences.\n")
w("### Numbers written as words\n")
nwq=q([r['number_words_spelled'] for r in R])
w(f"Spelled-out numbers (\"three benchmarks\", \"five national cultures\") per abstract: {fq(nwq,'%.0f')}. {sum(r['number_words_spelled']>0 for r in R)} of 47 abstracts carry at least one. **{sum(r['numerals_quant']==0 and r['number_words_spelled']==0 for r in R)} of 47 carry neither a digit nor a spelled number.** This matters for a reviewer who scans: a spelled number does not catch the eye, and abstracts routinely use one where a digit was available (\"across five national cultures and ten culture-sensitive tasks\", `2026.acl-long.766`; \"four multi-party dialogue datasets\", `2026.acl-long.877`).\n")
# categories
w("## What kind of numerals they are\n")
w("A single numeral can carry more than one tag (\"70% on easy tasks\" is both a percentage and, in context, a count). Totals are numerals; the second column is abstracts.\n")
w("| Category | Total numerals | Abstracts with at least one |")
w("|---|---|---|")
for lab,k in [('Result percentage','cat_result_percentage'),('Sample size or count','cat_sample_size_count'),('p-value','cat_p_value'),('Effect size','cat_effect_size'),('Scale-point or level figure','cat_scale_level'),('Model / task / dataset count','cat_model_task_dataset_count'),('Speedup or ratio multiplier','cat_ratio_multiplier'),('Model size in parameters','cat_model_size'),('Metric score (non-percentage)','cat_metric_score'),('Unclassified','cat_unclassified')]:
    w(f"| {lab} | {sum(r[k] for r in R)} | {sum(r[k]>0 for r in R)} |")
w("")
w(f"**No abstract in the 47 reports a p-value, and none reports an effect size** (Cohen's d, a kappa, a correlation coefficient with a value attached). The inferential-statistics vocabulary of an experimental social science paper is absent from this venue's abstracts. What appears instead is a percentage improvement, a dataset size, a count of models or benchmarks, and occasionally a speedup.\n")
withp=[r['cat_result_percentage'] for r in R if r['cat_result_percentage']>0]
w("### Among abstracts carrying at least one result percentage\n")
cw=Counter(withp)
w(f"{len(withp)} of 47 abstracts ({100*len(withp)/47:.0f} percent) carry a result percentage. Among those {len(withp)}: "+", ".join(f"{cw[k]} carr{'y' if cw[k]>1 else 'ies'} {k}" for k in sorted(cw))+f". Median {st.median(withp):.1f}, mean {sum(withp)/len(withp):.2f}, maximum {max(withp)}.\n")
w("So the convention, where an abstract quantifies a result at all, is **one or two percentages, not a battery**. Half the abstracts that report any percentage report exactly one. The densest, `2026.acl-long.1543` and `2026.acl-short.38`, report three each, and both use them for a range or a contrast rather than a list.\n")
# beat
w("### Which beat the numbers sit in\n")
fs=[r for r in R if r['first_stat_text']]
w(f"Position of the first statistic, among the {len(fs)} abstracts that have one: sentence {fq(q([r['first_stat_sentence_index'] for r in fs]),'%.1f')}, out of a median of {st.median([r['first_stat_of_n_sentences'] for r in fs]):.0f} sentences. As a fraction of the way through the abstract: {fq(q([r['first_stat_sentence_frac'] for r in fs]),'%.2f')}.\n")
w(f"**{sum(r['first_stat_sentence_frac']>=0.667 for r in fs)} of {len(fs)} put their first statistic in the final third of the abstract; {sum(r['first_stat_sentence_frac']<=0.5 for r in fs)} of {len(fs)} put one in the first half.** Numbers cluster hard in the results beat and are essentially absent from the motivation and method beats. The motivation beat is qualitative in every abstract in the sample. Where a number appears early it is a resource size in a benchmark paper describing what was built (`2026.findings-acl.1529`, \"NLCO covers 43 CO problems\", sentence 3 of 7), never a finding.\n")
w(f"Within the sentence, the first statistic falls at word {fq(q([r['first_stat_word_index_in_sentence'] for r in fs]),'%.1f')} of a sentence averaging {sum(r['first_stat_sentence_n_words'] for r in fs)/len(fs):.0f} words. The median is word {st.median([r['first_stat_word_index_in_sentence'] for r in fs]):.0f}: mid-sentence, after the subject and verb have named what is being measured.\n")
# referent attachment
w("## First-statistic clauses, verbatim, classified by referent attachment\n")
w("Every clause below is quoted verbatim from the abstract, bounded by the punctuation around it. Classification is hand-coded. The categories are: **BEFORE**, the thing being measured is named immediately before the numeral, usually joined by \"of\" or \"by\"; **AFTER**, the referent follows the numeral as its head noun; **PAREN**, the numeral sits in a parenthetical gloss on a claim made in the preceding main clause; **PRECEDING SUBORDINATE CLAUSE**, the referent sits in a subordinate clause before the one holding the numeral.\n")
ra=hc['referent_attachment']
for cat,lab in [('BEFORE','Referent immediately before the numeral'),('AFTER','Referent after the numeral'),('PAREN','Numeral in a parenthetical, referent in the preceding main clause'),('PRECEDING_SUB','Referent in a preceding subordinate clause')]:
    ids=[a for a in ra if ra[a]==cat] if cat!='PAREN' else [a for a in ra if ra[a]=='PAREN_AFTER_MAIN']
    w(f"### {lab}, {len(ids)} of {len(ra)}\n")
    if not ids: w("None.\n"); continue
    for a in sorted(ids):
        w(f"- `{a}`: \"{new[a]['first_stat_clause']}\"")
    w("")
w(f"**{len([a for a in ra if ra[a]=='BEFORE'])} of {len(ra)} name the referent immediately before the numeral; {len([a for a in ra if ra[a]=='AFTER'])} of {len(ra)} put it immediately after. Zero of {len(ra)} put the referent in a preceding subordinate clause.** In every case in this corpus, the noun that says what the number is a number *of* sits inside the same clause as the number, adjacent to it: \"an average margin of 6.74%–19.39%\", \"speedups of 1.62×\", \"recovery rates of up to 94%\", \"5,200 samples\", \"43 CO problems\", \"2M examples\". A reader can stop at the numeral and read one noun phrase in either direction and have the whole fact.\n")
w("The single near-exception is `2026.findings-acl.1394`, where the numeral is parenthetical: \"SafePatch achieves robust unsafe suppression (7% unsafe on I2P)\". Even there the parenthetical is self-describing, and the qualitative claim it glosses stands on its own in the main clause.\n")
w("This is the direct answer to the reviewer's miss. The construction in our abstract, \"Among the revisions that do change quality, 70% lower it\", puts the referent in a preceding subordinate clause and leaves the numeral attached to a bare pronoun. **That construction occurs zero times in 47 abstracts and zero times in the prior 9.** The figure was not missed because there was only one of them; it was missed because it is written in a shape this venue's readers are not scanning for. Rewriting it as \"70% of quality-changing revisions lower quality\" puts the referent after the numeral, which is the second most common pattern here, without adding a single further statistic.\n")
# naming
w("## Naming: artifacts, models, metrics, datasets\n")
w("Counts are hand-verified. The script's regex count matched the hand count for artifacts, models and datasets; it differed only for metrics, where \"recall\", \"calibration\" and \"agreement\" appear in these abstracts as ordinary English. Both metric figures are given below.\n")
w("| Signal | Abstracts | Share |")
w("|---|---|---|")
rows=[("Introduces a named artifact (capitalised name or acronym)",sum(r['hv_artifact'] for r in R)),
      ("Names at least one quantitative evaluation metric",sum(r['hv_metric'] for r in R)),
      ("Names at least one evaluation dataset or benchmark it runs on",sum(r['hv_dataset'] for r in R)),
      ("Names at least one model by name (GPT, Llama, Gemma, Gemini, Pythia …)",sum(r['hv_model'] for r in R)),
      ("Carries at least one quantitative digit",sum(r['numerals_quant']>0 for r in R)),
      ("Carries at least one result percentage",sum(r['cat_result_percentage']>0 for r in R))]
for lab,n in rows: w(f"| {lab} | {n}/47 | {100*n/47:.0f}% |")
w("")
w(f"Script-detected metric mentions were {sum(1 for r in R if r['names_metrics'])}/47 before adjudication; the hand-verified figure is {sum(r['hv_metric'] for r in R)}/47.\n")
w(f"**Naming an artifact is by far the strongest technical signal in this corpus, and it is not close.** {sum(r['hv_artifact'] for r in R)} of 47 abstracts ({100*sum(r['hv_artifact'] for r in R)/47:.0f} percent) coin and use a capitalised name for what they built, against {sum(r['numerals_quant']>0 for r in R)} of 47 ({100*sum(r['numerals_quant']>0 for r in R)/47:.0f} percent) that carry any digit and {sum(r['cat_result_percentage']>0 for r in R)} of 47 ({100*sum(r['cat_result_percentage']>0 for r in R)/47:.0f} percent) that carry a result percentage. The typical abstract in these volumes reads as technical because it names a mechanism, not because it quantifies one.\n")
nm=[r for r in R if not r['hv_artifact']]
w(f"The {len(nm)} abstracts with no named artifact are `"+"`, `".join(hc['no_named_artifact'])+f"`. All {len(nm)} of them also carry no quantitative digit, so the two sparse signals coincide exactly: every abstract in the corpus that reports a figure also coins a name.\n")
w(f"Naming a model is rare: {sum(r['hv_model'] for r in R)} of 47. \"Experiments across 7B/14B/32B models\" and \"4 LLMs ranging from 1.7B to 30B parameters\" are the usual form, giving scale without a vendor name. Naming a dataset is likewise a minority behaviour, {sum(r['hv_dataset'] for r in R)} of 47; most abstracts say \"three QA benchmarks\" or \"four multi-party dialogue datasets\" and leave them unnamed.\n")
w("Combining the two signals: "+f"{sum(1 for r in R if r['hv_artifact'] and r['numerals_quant']>0)} of 47 abstracts both name an artifact and carry a digit; {sum(1 for r in R if r['hv_artifact'] and r['numerals_quant']==0)} name an artifact and carry no digit; {sum(1 for r in R if not r['hv_artifact'] and r['numerals_quant']>0)} carry a digit without naming an artifact; {sum(1 for r in R if not r['hv_artifact'] and r['numerals_quant']==0)} do neither.\n")
# valence
w("## Negative and null results versus working methods\n")
w("Valence is hand-coded from the principal reported result. Genre and valence are almost fully confounded in this sample, and that confound has to be stated rather than analysed away: **5 of the 6 benchmark papers report a negative principal finding, and all 5 negative-valence abstracts are benchmark papers.** No method paper in the sample reports a negative principal result, which is itself the finding: this venue's method abstracts do not publish failures.\n")
w("| Group | n | Median /100w | p75 | Mean | Zero-digit | With a result % |")
w("|---|---|---|---|---|---|---|")
for lab,sel in [('Negative or null principal result',lambda r:r['valence']=='NEG'),('Working-method principal result',lambda r:r['valence']=='POS'),
                ('Benchmark papers (B)',lambda r:r['genre']=='B'),('Method papers (M)',lambda r:r['genre']=='M'),('Analysis papers (A)',lambda r:r['genre']=='A')]:
    g=[r for r in R if sel(r)]; xs=[r['numerals_per_100w'] for r in g]; Q=q(xs)
    w(f"| {lab} | {len(g)} | {Q['med']:.2f} | {Q['p75']:.2f} | {Q['mean']:.2f} | {sum(x==0 for x in xs)} | {sum(r['cat_result_percentage']>0 for r in g)} |")
w("")
negd=[r['numerals_per_100w'] for r in R if r['valence']=='NEG']; posd=[r['numerals_per_100w'] for r in R if r['valence']=='POS']
w(f"**Negative-result abstracts carry *more* numbers, not fewer** (median {st.median(negd):.2f} against {st.median(posd):.2f}, mean {sum(negd)/len(negd):.2f} against {sum(posd)/len(posd):.2f}), though with n=5 in the negative cell this is a direction, not an estimate. The mechanism is visible in the text: a paper whose claim is that models fail has to say how much they fail by, or say what the benchmark contains, to make the failure legible. `2026.eacl-long.325` gives \"2M examples, 77 models across 11 families, and 9 programming languages\" before stating that detector performance \"remains far below practical usability\". `2026.acl-long.1655` gives \"5,200 samples\" and \"6 to 1,000 base pairs\".\n")
w(f"None of the five negative abstracts reports a result percentage; all {sum(r['cat_result_percentage']>0 for r in R)} abstracts carrying a result percentage report a positive result. A negative finding in this corpus is quantified by the size of what was tested, not by the size of the failure.\n")
w(f"Two of the five negative abstracts carry no digit at all: `2026.acl-long.210` (\"We reveal substantial performance variation\") and `2026.findings-acl.2070` (\"even simple transformations cause a significant performance drop\"). Both state the negative finding in words alone and were accepted. So a quantified negative is the denser convention, but an unquantified one is not disqualifying at these venues.\n")
w("Conditioning on genre rather than valence gives the same ordering: benchmark papers are the densest genre, method papers the sparsest, with analysis papers between them.\n")
# prior 9
P=list(prior.values()); pd=[r['numerals_per_100w'] for r in P]
w("## The prior 9-abstract sample was not representative\n")
w(f"Re-measuring the 9 abstracts already held in `acl2026_abstracts.json` with the same script: numerals per 100 words {fq(q(pd))}; {sum(r['numerals_quant']==0 for r in P)} of 9 carry no digit; {sum(r['cat_result_percentage']>0 for r in P)} of 9 carry a result percentage.\n")
w(f"Against the systematic sample, that is a different population. **Median density {st.median(pd):.2f} against {st.median(dens):.2f}. Result percentages in {sum(r['cat_result_percentage']>0 for r in P)}/9 ({100*sum(r['cat_result_percentage']>0 for r in P)/9:.0f} percent) against {sum(r['cat_result_percentage']>0 for r in R)}/47 ({100*sum(r['cat_result_percentage']>0 for r in R)/47:.0f} percent).** The 9 were gathered as topical neighbours of this paper, and abstracts that are topical neighbours of a quantitative behavioural study are themselves quantitative. Calibrating a target density on them overstates the venue norm by roughly a factor of four at the median. That is the concrete reason the 9-paper sample was the wrong instrument, independent of its size.\n")
w("| Prior-9 abstract | Words | Quant numerals | Per 100w | Result % |")
w("|---|---|---|---|---|")
for k,r in prior.items(): w(f"| {k} | {r['n_words']} | {r['numerals_quant']} | {r['numerals_per_100w']:.2f} | {r['cat_result_percentage']} |")
w("")
w("Their first-statistic clauses show the same referent attachment as the systematic sample: \"a benchmark of 4,180 questions\", \"a dataset of 9,720 comprehension questions\", \"Across 45,000 samples from three LRMs\", \"ZIP achieves 95.8% accuracy compared to 65.8% for LIME\", \"DART improves Llama-3-8B-Instruct accuracy from 39.0% to 68.8%\". Referent adjacent to the numeral in all seven that have one. None uses a preceding subordinate clause.\n")
# targets
w("## What a 200-word abstract in this venue would carry\n")
med=st.median(dens); p75=q(dens)['p75']
w(f"Scaling the observed rates to 200 words. The corpus median abstract is {st.median([r['n_words'] for r in R]):.0f} words, so 200 words is already at the {pctl([r['n_words'] for r in R],200):.0f}th percentile for length.\n")
w("**At the median.** The median abstract in this corpus contains **zero digits**. It names a coined artifact, states the gap it closes, describes the mechanism in two or three sentences, and closes with an unquantified claim of improvement over baselines on unnamed benchmarks. Writing to the median would mean removing the statistic altogether, which is not the goal here. The median is worth knowing for one reason: it establishes that the reviewer's premise, that the abstract is short on numbers by the standard of the venue, is not what the venue does.\n")
w(f"**At the 75th percentile.** The 75th percentile is {p75:.2f} numerals per 100 words, which over 200 words is **{p75*2:.1f} numerals, so one or two**. Concretely, a 200-word abstract at the 75th percentile of this corpus carries:\n")
w("- one coined, capitalised name for what the paper introduces, used two or three times (85 percent of the corpus does this, so it is not a percentile question, it is the floor);")
w(f"- one or two figures, most often a single result percentage (the {len(withp)} abstracts with any percentage carry a median of {st.median(withp):.1f});")
w("- the figure placed in the final third, in the results sentence, with its referent inside the same clause;")
w("- a named metric (34 percent of the corpus) and, less often, a named benchmark (19 percent);")
w("- no p-value, no effect size, no confidence interval; none of the 47 carries one.\n")
w(f"**At the 90th percentile**, {q(dens)['p90']:.2f} per 100 words, or about {q(dens)['p90']*2:.0f} numerals in 200 words: a resource size, a count of models or benchmarks evaluated, and two result figures used as a contrast or a range. `2026.acl-long.1877` is the worked example at this level, with \"4 LLMs ranging from 1.7B to 30B parameters, across 4 SWA ratios\" and \"6 strong static head-level methods\".\n")
w("**What none of them do.** No abstract in the corpus reaches 3.5 numerals per 100 words, so a 200-word abstract carrying seven figures would be outside the observed range. Adding numbers past two or three does not move the abstract toward the venue; it moves it away.\n")
w("### The implication for the reviewer's comment\n")
w("Two changes are indicated, and neither is \"add more numbers\".\n")
w("First, **reattach the referent**. \"Among the revisions that do change quality, 70% lower it\" is the one construction in the paper's abstract that does not occur anywhere in 56 measured abstracts. Recast so the noun sits against the numeral: \"70% of quality-changing revisions lower quality\". This costs nothing and is the change that addresses the failure that occurred, which was a scan that did not find the figure.\n")
w("Second, **the technical signal these venues read is the named artifact, not the digit count**. 85 percent name one; 34 percent carry any digit. If the abstract reads as insufficiently technical, the lever with the larger observed effect is to coin and repeat a name for the construct or the measure, and to name the metric and the models, rather than to raise the numeral count from one to five. Going from one figure to two, placed in the results sentence, moves the abstract from roughly the 66th to the 80th percentile of this corpus; going to five would put it beyond the maximum.\n")
w("---\n")
w("Retrieval date for all Anthology pages: 2026-09-06. Sampling seed: 20260906. Measurement script: `measure2.py` (held with the working files for this analysis). Abstracts stored verbatim in `acl2026_abstracts.json` under `sample_2026_09_06`.\n")
open(OUT,'w',encoding='utf-8').write('\n'.join(L))
print('wrote', OUT, len('\n'.join(L)), 'chars')
