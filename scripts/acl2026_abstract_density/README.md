# ACL 2026 abstract density measurement

Scripts 01–04 produce `paper/reference/acl2026_density.md` and the `sample_2026_09_06`
block (47 abstracts) of `paper/reference/acl2026_abstracts.json`. Scripts 04b and 05
extend that corpus to 67 and produce `paper/reference/scen_04_length_density.md`.

Run in order. Scripts 01 and 02 hit the ACL Anthology (one request per paper, 0.4s apart)
and write intermediates to a working directory; 03 and 04 are pure functions of those
intermediates plus the two hand-coding files here.

- `01_sample_and_fetch.py` — systematic sample, seed 20260906, constant stride per volume;
  downloads one landing page per sampled paper.
- `02_extract_abstracts.py` — pulls the abstract from the `card-body acl-abstract` div by
  walking div nesting (the heading is not always followed by a `<span>`).
- `03_measure.py` — all mechanical counts: words, sentences, numerals by kind and category,
  position of the first statistic, naming regexes.
- `04_write_report.py` — assembles the report from the measurements and the hand codes.

- `04_sample_and_fetch_batch2.py` — second interleaved systematic draw, seed 20260907,
  20 further abstracts excluding everything already in batch A; writes them into
  `acl2026_abstracts.json` under `sample2_2026_09_06`.
- `05_length_density.py` — the length-versus-density analysis over all 67: correlations
  with confidence intervals and p-values, the short-and-dense and long-and-sparse sets,
  median length by figure count and by naming behaviour, the beat inventory by length
  band, and the drop order. Reuses `03_measure.py`'s measurement functions unchanged,
  with one documented override (half-parenthesised list enumerators such as "1)" and
  "2)", which `03_measure.py` scored as statistics; the override is stated inline in
  `05_length_density.py` and affects one abstract, `2026.findings-acl.900`, which is in
  batch B, so no figure in `acl2026_density.md` changes).

`handcode_artifact_naming_67.json` holds the read-through adjudication of the
artifact-naming flag over all 67 abstracts, with the reason for each override.

`handcode_genre_valence.json` and `handcode_naming_and_referent.json` hold the judgements
that are not mechanical: paper genre, result valence, the referent-attachment
classification, and the adjudicated naming flags. Each file states its coding rule.

Retrieval date: 2026-09-06.

## Scenario 01: artifact-free abstracts, 2024-2026

Produces `paper/reference/scen_01_no_artifact.md` and the `no_artifact_2024_2026` block of
`paper/reference/acl2026_abstracts.json`. Conditions on the case the 47-abstract sample holds
only 7 of: an analysis or empirical study that releases no benchmark, model or system.

- `05_no_artifact_sample.py` — 17 volume listing pages (2024-2026 ACL, EMNLP, NAACL, EACL and both
  Findings); title-shape regex; a release-and-coined-name screen run against the abstracts carried in
  the listing pages; systematic draw with a fixed start and constant stride per volume, seed 20260906;
  fetches one landing page per drawn paper.
- `06_no_artifact_measure.py` — re-extracts each abstract from the landing page's `card-body
  acl-abstract` div, checks it against the listing-page copy, measures it with `03_measure.py`, keeps
  the papers listed in the hand-code file, and stores everything in the shared JSON.
- `handcode_no_artifact.json` — the five hand judgements and the coding rule for each: which drawn
  papers are analyses rather than method or resource papers (with the reason for every drop), what the
  abstract names and of what kind, whether the paper coins a term of its own, the closing move, and
  whether each numeral states the size of the experiment or the size of an outcome.
- `07_write_no_artifact_report.py` — assembles the report. Every number in it is computed at write time.

`03_measure.py` gained two tokenizer amendments for this corpus: a bare list marker introducing a
numbered finding is an enumerator, not a quantity, and a digit glued to a following all-caps identifier
is part of a name. Re-measuring the 47-abstract and 9-abstract corpora under the amended tokenizer
changes no count in either.

Retrieval date: 2026-09-06.
