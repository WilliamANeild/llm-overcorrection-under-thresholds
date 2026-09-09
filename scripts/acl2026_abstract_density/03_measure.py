# -*- coding: utf-8 -*-
"""Mechanical measurement of abstract quantitative density.
Every count below is produced by regex/tokenizer, never by eye."""
import re, json, statistics as st

ABBR = r'(?:e\.g|i\.e|et al|vs|cf|Fig|Eq|Sec|Tab|approx|resp|Dr|Prof|St|No|Inc|etc|al)'
def sentences(t):
    p = re.sub(r'\b'+ABBR+r'\.', lambda m: m.group(0).replace('.','\x00'), t)
    p = re.sub(r'(\d)\.(\d)', lambda m: m.group(1)+'\x00'+m.group(2), p)
    p = re.sub(r'\b([A-Z])\.(?=\s?[A-Z]\.)', lambda m: m.group(1)+'\x00', p)
    p = re.sub(r'(?<=[.!?])(?=[A-Z])', ' ', p)              # missing space after period
    parts = re.split(r'(?<=[.!?])["”\')\]]*\s+(?=[A-Z“"(\[\d])', p)
    return [x.replace('\x00','.').strip() for x in parts if x.strip()]

def words(t): return re.findall(r"[A-Za-z0-9][A-Za-z0-9%–\-\.,/@’']*", t)

DIGITRUN = re.compile(r'\d[\d,]*(?:\.\d+)?')
MODELWORD = re.compile(r'\b(?:GPT|ChatGPT|Llama|LLaMA|Qwen|Mistral|Mixtral|Gemma|Gemini|Claude|Sonnet|DeepSeek|Phi|OLMo|Falcon|BERT|RoBERTa|DeBERTa|BLOOM|Vicuna|GLM|InternLM|Grok|Nemotron|Pythia|Whisper|Baichuan|MiniCPM|Ernie|StarCoder|CodeLlama|WizardLM|Doubao|Ministral|SDXL|Stable Diffusion)\b[\s\-]*$')
QUANT_PREFIX = re.compile(r'(?:top|pass@|recall@|precision@|hits?@|n\s*=|N\s*=|k\s*=|@)\s*[-]?$', re.I)

LIST_MARKER_LEFT = re.compile(r'(?:^|[:;.]\s{1,2}|\s\s)$')

def classify_run(t, m):
    """Return 'name', 'year', 'enum', or 'quant'."""
    s, e = m.span(); tok = m.group(0)
    if t[max(0,s-1):s] == '(' and t[e:e+1] == ')' and len(tok) <= 2: return 'enum'
    # bare list marker introducing a numbered finding: "four key findings: 1. Larger models ..."
    if re.fullmatch(r'\d{1,2}', tok) and t[e:e+2] == '. ' and LIST_MARKER_LEFT.search(t[:s]): return 'enum'
    # digit glued to a following all-caps identifier: the 3 in "3XCM"
    if re.match(r'[A-Z]{2,}', t[e:e+4]) and (s == 0 or not t[s-1].isalnum()): return 'name'
    left = t[:s]
    if QUANT_PREFIX.search(left[-10:]): return 'quant'
    lc = left[-1:]
    if lc.isalpha(): return 'name'
    # walk back through a digit/hyphen/dot chain: "Llama-3-8B" -> the 8 is part of the name
    k = len(left)
    while k > 0 and (left[k-1].isdigit() or left[k-1] in '-._'): k -= 1
    if k < len(left) and k > 0 and left[k-1].isalpha() and (len(left)-k) <= 8: return 'name'
    if lc in '-_.' and left[-2:-1].isalpha(): return 'name'
    if MODELWORD.search(left[-14:]): return 'name'
    core = tok.replace(',','')
    if re.fullmatch(r'(?:19|20)\d\d', core) and not re.match(r'\s*(?:%|percent)', t[e:e+8]):
        return 'year'
    return 'quant'

MET = re.compile(r'\b(accurac(?:y|ies)|F1|F-?scores?|BLEU|ROUGE|METEOR|BERTScore|chrF|COMET|exact match|kappa|κ|Krippendorff|win[- ]rates?|pass@\w+|AUROC|AUC|precision|recall|perplexity|MRR|nDCG|Elo|MAE|RMSE|WER|CER|Spearman|Pearson|correlation coefficients?|correlations?|success rates?|error rates?|agreement|macro-?F1|micro-?F1|MSE|calibration|Brier|refusal rates?|attack success rates?|BLEURT|feasibility|faithfulness|abstention)\b', re.I)
DATASET = re.compile(r'\b(MMLU(?:-Pro)?|GSM8K|HumanEval|MBPP|BBH|BIG-?Bench|TruthfulQA|HellaSwag|WinoGrande|PIQA|SQuAD|Natural Questions|TriviaQA|HotpotQA|XSum|CNN/DailyMail|WMT\d*|FLORES|XNLI|XQuAD|TyDiQA|CoNLL|OntoNotes|SuperGLUE|GLUE|MATH-?500|AIME|LiveCodeBench|SWE-?bench|AlpacaEval|MT-?Bench|Arena-?Hard|ToxiGen|RealToxicityPrompts|CrowS-?Pairs|StereoSet|HaluEval|FEVER|MultiWOZ|ImageNet|COCO|VQA|ScienceQA|MedQA|PubMedQA|C-?Eval|CMMLU|AGIEval|GPQA|MuSR|IFEval|BFCL|WildBench|Chatbot Arena|OpenBookQA|CommonsenseQA|StrategyQA|DROP|BoolQ|RACE|LAMBADA|WikiText|The Pile|OSCAR|Dolma|RedPajama|MQuAKE|EmpatheticDialogues|ESConv|CoQA|QuAC|ELI5|MSMARCO|BEIR|MIRACL|Spider|WikiSQL|CodeXGLUE|MMMU|MathVista|ChartQA|DocVQA|TextVQA|GQA|NLVR2?|SNLI|MNLI|ANLI|QQP|SST-?2?|IMDB|AG News|Yelp|Amazon Reviews|Wikipedia)\b')
INTRO = re.compile(r'\b(?:we|this (?:paper|work|study|article))\s+(?:\w+\s+){0,3}?(?:introduce|propose|present|release|develop|construct|build|design|create|curate|offer|contribute|open-source)[sd]?\b', re.I)
ACRO = re.compile(r"\b(?:[A-Z][a-z]*[A-Z][A-Za-z0-9\-]*|[A-Z]{3,}[A-Za-z0-9\-]*)\b")
COMMON = set('LLM LLMS NLP AI ML LM LMS QA MT NER ASR TTS RAG SFT RLHF DPO PPO GRPO PEFT LORA MOE COT ICL OOD IID SOTA API GPU CPU HTML JSON XML PDF URL SVM CNN RNN LSTM MLP KL EM MLE MAP AUC ROC SD CI ANOVA IRB VLM VLMS MLLM MLLMS SLM SLMS AGI CLM MLM NLU NLG SAE SAES OCR CoT NLI SRL POS IR RL SSL KG KGS TODO USA US UK EU ID IDS OK GPT LLAMA BERT CLIP T5 MCQ MCQA QLORA FFN MHA KV FLOPS TL DR AND OR NOT THE'.split())

NAMEY = r"[A-Z][A-Za-z0-9]*(?:[-–][A-Za-z0-9]+)*"
CTX_DS = re.compile(r'(?:[Ee]xperiments?|[Ee]valuat\w+|[Bb]enchmarks?|[Dd]atasets?|[Tt]est(?:ed|ing)?|[Rr]esults?|[Vv]alidat\w+|[Aa]ssess\w*|[Aa]nalys\w+)\s+(?:\w+\s+){0,4}?(?:on|across|using|over|with|from)\s+\(?\s*((?:'+NAMEY+')(?:\s*(?:,|and|,\s*and)\s*(?:'+NAMEY+'))*)')
SUFFIX_DS = re.compile(r'\b'+NAMEY+r'(?:Bench|QA|Eval|Bank|Corpus|Suite|Arena)\b')
DS_STOP = set('The This We Our Large Language Models Model English Chinese Experiments Extensive Comprehensive Across Using Results Analysis Human Code Data Dataset Benchmark Benchmarks Datasets Reinforcement Supervised Sparse Vision Text Image Knowledge Base Question Answering Natural Language Processing Deep Research Group Relative Policy Optimization Best Mode Token Multi Self Chain Thought Event Person Figurative State Art SOTA GUI KV CPU GPU RAG LLM LLMs VLM VLMs AI NLP QA ReID CO MDL SCE ACS I2P SWA DAG RoPE GRPO RL SFT PeFT ReFT MI SAE SAEs MwE LM LMs ABM CoT'.split())
def contextual_datasets(t):
    out=set()
    for m in CTX_DS.finditer(t):
        for cand in re.findall(NAMEY, m.group(1)):
            if cand not in DS_STOP and len(cand)>2 and not MODELNAME_ONLY.search(cand): out.add(cand)
    for m in SUFFIX_DS.finditer(t):
        if m.group(0) not in DS_STOP: out.add(m.group(0))
    return out
MODELNAME_ONLY = re.compile(r'^(?:GPT|ChatGPT|Llama|LLaMA|Qwen|Mistral|Mixtral|Gemma|Gemini|Claude|DeepSeek|Phi|OLMo|Falcon|BERT|RoBERTa|BLOOM|Vicuna|GLM|InternLM|Grok|Nemotron|Pythia|Whisper)', re.I)

def measure(t):
    sents = sentences(t); ws = words(t); nw = len(ws)
    runs = []
    for m in DIGITRUN.finditer(t):
        runs.append({'text': m.group(0), 'start': m.start(), 'end': m.end(), 'kind': classify_run(t, m)})
    quant = [r for r in runs if r['kind']=='quant']
    for r in quant: r['cats'] = cats_for(t, r)
    numwords = re.findall(r'\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|twenty|thirty|forty|fifty|hundred|thousand|million|billion|dozens?)\b', t, re.I)
    d = {'n_words': nw, 'n_sentences': len(sents),
         'digit_runs_total': len(runs),
         'digit_runs_identifier': sum(r['kind']=='name' for r in runs),
         'digit_runs_year': sum(r['kind']=='year' for r in runs),
         'digit_runs_enumeration': sum(r['kind']=='enum' for r in runs),
         'numerals_quant': len(quant),
         'number_words_spelled': len(numwords),
         'numerals_per_100w': round(100*len(quant)/nw, 2),
         'digitruns_all_per_100w': round(100*len(runs)/nw, 2),
         'cat_result_percentage': sum('percentage' in r['cats'] for r in quant),
         'cat_sample_size_count': sum('sample_size' in r['cats'] for r in quant),
         'cat_p_value': sum('p_value' in r['cats'] for r in quant),
         'cat_effect_size': sum('effect_size' in r['cats'] for r in quant),
         'cat_scale_level': sum('scale_level' in r['cats'] for r in quant),
         'cat_model_task_dataset_count': sum('mtd_count' in r['cats'] for r in quant),
         'cat_ratio_multiplier': sum('ratio_multiplier' in r['cats'] for r in quant),
         'cat_model_size': sum('model_size' in r['cats'] for r in quant),
         'cat_metric_score': sum('metric_score' in r['cats'] for r in quant),
         'cat_unclassified': sum('other' in r['cats'] for r in quant),
         'names_models': sorted({m.group(0) for m in re.finditer(r'\b(?:GPT-[\w.o-]+|GPT-?4o?|ChatGPT|LLaMA[-\d.]*|Llama[-\s]?[\d.]*\w*|Qwen[\d.\w-]*|Mistral[-\w.]*|Mixtral[-\w.]*|Gemma[-\d.\w]*|Gemini[-\s\d.\w]*|Claude[-\s\d.\w]*|DeepSeek[-\w.]*|Phi-?\d[\w.]*|OLMo[-\w.]*|Falcon[-\w]*|T5|BERT|RoBERTa|BLOOM|Vicuna|GLM-?[\w.]*|InternLM[\w.-]*|Grok[-\w.]*|Nemotron|Aya|Pythia|Whisper|o[13]-?\w*|R1|V3)\b', t)}),
         'names_metrics': sorted({m.group(0) for m in MET.finditer(t)}),
         'names_datasets': sorted(set([m.group(0) for m in DATASET.finditer(t)]) | contextual_datasets(t)),
         'introduces_verb': bool(INTRO.search(t)),
         'named_acronyms': sorted({a for a in ACRO.findall(t) if a.upper().split('-')[0] not in COMMON and len(a)>2}),
         'run_detail': [f"{r['text']}[{r['kind']}{'|'+','.join(r['cats']) if r['kind']=='quant' else ''}]" for r in runs]}
    d['names_artifact'] = bool(d['named_acronyms']) and d['introduces_verb']
    if quant:
        f = quant[0]; pos = f['start']
        si, sent, sstart = 0, sents[0], 0
        cur = 0
        for i,s in enumerate(sents):
            j = t.find(s, cur)
            if j < 0: j = cur
            if j <= pos < j+len(s): si, sent, sstart = i, s, j; break
            cur = j + len(s)
        off = pos - sstart
        # clause bounds: punctuation, but a comma between two digits is a thousands separator
        seps = [i for i,c in enumerate(sent) if c in ',;:()—' and not (c==',' and i>0 and i+1<len(sent) and sent[i-1].isdigit() and sent[i+1].isdigit())]
        lo = max([i for i in seps if i < off] + [-1]) + 1
        hi = min([i for i in seps if i >= off] + [len(sent)])
        d.update({'first_stat_text': f['text'], 'first_stat_cats': f['cats'],
                  'first_stat_sentence_index': si+1, 'first_stat_of_n_sentences': len(sents),
                  'first_stat_sentence_frac': round((si+1)/len(sents),3),
                  'first_stat_word_index_in_sentence': len(words(sent[:off]))+1,
                  'first_stat_sentence_n_words': len(words(sent)),
                  'first_stat_clause': sent[lo:hi].strip(),
                  'first_stat_sentence': sent})
    else:
        d.update({k: None for k in ['first_stat_text','first_stat_cats','first_stat_sentence_index','first_stat_of_n_sentences','first_stat_sentence_frac','first_stat_word_index_in_sentence','first_stat_sentence_n_words','first_stat_clause','first_stat_sentence']})
    return d

def cats_for(t, r):
    s,e = r['start'], r['end']; before = t[max(0,s-70):s]; after = t[e:e+34]
    bl, al = before.lower(), after.lower(); c=[]
    if re.match(r'\s*(?:%|percent\b|percentage points?\b|\bpp\b)', al): c.append('percentage')
    if re.search(r'\bp\s*[<>=≤≥]\s*$', before): c.append('p_value')
    if re.search(r"(?:cohen'?s d|kappa|κ|ρ|τ|spearman|pearson|correlat\w*(?: of| at| coefficient of)?|effect size|odds ratio|cliff'?s|cramér|r\s*=|d\s*=)\s*(?:of\s*)?$", bl) or re.match(r'\s*(?:SD|standard deviations?)\b', after): c.append('effect_size')
    if re.match(r'\s*-?\s*(?:point|level|star|tier|grade)\b', al) or re.search(r'(?:likert|scale of|rating of|score of|on a|level|tier|grade)\s*$', bl): c.append('scale_level')
    if re.match(r'\s*[MBKk]?\s*(?:models?|llms?|systems?|tasks?|datasets?|benchmarks?|languages?|domains?|corpora|corpus|families|variants?|baselines?|settings?|configurations?|architectures?|strategies)\b', al): c.append('mtd_count')
    if re.match(r'\s*[MBKk]?\s*(?:examples?|instances?|samples?|questions?|items?|pairs?|annotators?|participants?|subjects?|documents?|sentences?|articles?|utterances?|dialogues?|images?|videos?|papers?|responses?|annotations?|labels?|entries?|records?|tokens?|episodes?|trials?|humans?|experts?|speakers?|users?|cases?|passages?|queries?|turns?|comments?|posts?|reviews?|prompts?|problems?|CO problems)\b', after) or re.search(r'\b[nN]\s*=\s*$', before) or re.search(r'(?:of|over|across|totalling|totaling|comprising|containing|spans|collect\w*|annotat\w*|construct\w*|releas\w*|curat\w*|includ\w*)\s+$', bl): c.append('sample_size')
    if re.search(r'(?:accurac\w+|F1|BLEU|ROUGE|AUC|AUROC|kappa|κ|score|rate|MRR|nDCG|NDCG|correlation|precision|recall|perplexity|Elo|MAE|RMSE|WER|CER|PW-MCC|[A-Z]{2,}(?:-[A-Z]+)*)\s*(?:of|=|≈|:|is|at|reaching|reaches)?\s*$', before) and 'percentage' not in c: c.append('metric_score')
    if re.match(r'\s*(?:[×x]|-?fold\b|\s*times\b)', after): c.append('ratio_multiplier')
    if re.match(r'\s*[BMK]\b|\s*[BMK]?\s*(?:parameters?|params)\b', after): c.append('model_size')
    if not c: c.append('other')
    return c

if __name__ == '__main__':
    new = json.load(open('/tmp/aclfetch/extracted.json'))
    rows = {a: dict(r, **measure(r['abstract'])) for a,r in new.items()}
    old = json.load(open('/Users/liamneild/Desktop/School/llm-overcorrection-under-thresholds/paper/reference/acl2026_abstracts.json'))
    oldrows = {}
    for k,v in old.items():
        a = re.sub(r'^>\s*Abstract\s*','',v).strip()
        oldrows[k] = dict({'anthology_id':None,'title':k,'abstract':a}, **measure(a))
    json.dump({'new':rows,'prior9':oldrows}, open('/tmp/aclfetch/measured.json','w'), indent=1, ensure_ascii=False)
    print('new=%d prior9=%d'%(len(rows),len(oldrows)))
