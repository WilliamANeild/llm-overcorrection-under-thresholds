# Prose metrics per section

Measured 2026-09-14 by `scripts/introduction_corpus/07_prose_census.py` over the same 69 cached
papers as the length census, split into the whole corpus and Ali's 24. Same Flesch implementation
used for the abstract and introduction work, so the numbers are comparable across every section.

`section_length_census.md` says how long a section should be. This says how it should read.

## Method note

Paragraph counts are symmetric across the two sides. LaTeXML renders a run-in `\paragraph{}`
heading as `<h6 class="ltx_title_paragraph">` with the following text in its own `<p class="ltx_p">`,
so a corpus paragraph breaks at a run-in heading exactly as our blank-line split does. 55 of the 69
papers use run-in headings, 1,112 in total. This was checked before the paragraph findings below
were trusted, because our related work and results use 6 and 10 of them.

## Flesch reading ease

| section | ours | n | p25 | median | p75 | Emami median | |
|---|---:|---:|---:|---:|---:|---:|---|
| introduction | 44.4 | 42 | 18.3 | 25.1 | 30.3 | 20.7 | far above |
| related work | 28.8 | 39 | 24.8 | 32.5 | 39.6 | 29.4 | in band |
| method | 22.7 | 22 | 31.0 | 34.8 | 39.9 | 35.4 | below |
| results | 35.0 | 27 | 25.6 | 32.5 | 36.9 | 25.7 | in band |
| discussion | 41.4 | 9 | 21.7 | 25.1 | 27.3 | too few | above |
| conclusion | 29.1 | 25 | 4.5 | 8.8 | 23.1 | 2.9 | above |

The paper reads easier than the field everywhere except the methods, which is the densest section
we have and the hardest in the corpus comparison. The introduction's 44.4 against a field median of
25.1 is Tania's rewrite and is a deliberate departure, not a defect.

## Words per sentence

| section | ours | p25 | median | p75 | Emami median | |
|---|---:|---:|---:|---:|---:|---|
| introduction | 22.0 | 20.9 | 23.4 | 27.6 | 22.5 | in band |
| related work | 21.7 | 15.1 | 21.5 | 26.0 | 17.2 | in band |
| method | 23.7 | 19.5 | 21.8 | 25.7 | 27.0 | in band |
| results | 23.2 | 19.4 | 21.0 | 22.9 | 21.6 | 0.3 over |
| discussion | 25.1 | 20.4 | 21.5 | 25.5 | too few | in band |
| conclusion | 22.0 | 21.5 | 22.2 | 25.2 | 21.9 | in band |

## Words per paragraph

| section | ours | n | p25 | median | p75 | Emami median | |
|---|---:|---:|---:|---:|---:|---:|---|
| introduction | 125 | 42 | 89 | 115 | 129 | 77 | in band |
| related work | 65 | 39 | 102 | 123 | 158 | 126 | below p25 |
| method | 70 | 22 | 69 | 97 | 107 | 63 | at p25 |
| results | 64 | 27 | 78 | 90 | 107 | 69 | below p25 |
| discussion | 159 | 9 | 56 | 108 | 145 | too few | above p75 |
| conclusion | 55 | 25 | 86 | 108 | 133 | 106 | below p25 |

## What this says about the page cut

The cut compressed by shortening paragraphs rather than by dropping them, and it left two sections
made of stubs. Related work is 6 paragraphs of which 5 run between 35 and 66 words against a corpus
p25 of 102: 120, 66, 62, 59, 49, 35. Results is 15 paragraphs with a median near 60. Both sections
pass their length benchmark and fail their paragraph benchmark, which is the signature of trimming
every paragraph a little instead of cutting whole claims.

The remedy is not to add words, since the length is right and the page budget is full. It is to
merge adjacent stubs so the same content arrives in fewer, fuller paragraphs. In related work, six
run-in headings over 445 words is roughly one heading per 74 words, which is what makes it read as
a list. Merging to four clusters would put it at about 111 words per paragraph, inside the band,
with no words added or removed.

The discussion has the opposite problem at 159 words per paragraph against a p75 of 145.

The conclusion at 55 is below p25 but is only 113 words in two paragraphs; the corpus conclusions
that set the band are longer overall, so this one is a weak flag.
