"""Readability and style measures for abstracts.

Every figure reported in readability_citations.md comes from this module. Nothing
is counted by eye.

Flesch reading ease, words per sentence and syllables per word come from
`textstat` (Pyphen-based syllabification), so the numbers are on the same scale as
the 49.3 quoted for the draft abstract. Nominalisation and numeral counts are
regex measures defined here.

Requires: textstat.
"""
import re
import textstat

NOMINAL_SUF = ("tion", "tions", "sion", "sions", "ment", "ments", "ness", "nesses",
               "ity", "ities", "ance", "ances", "ence", "ences", "ancy", "ency",
               "ism", "isms", "ization", "izations", "isation", "isations")
NOMINAL_MIN = 6   # length floor so "ion", "city", "dance" do not qualify


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'\-]*", text)


def measure(text):
    text = re.sub(r"\s+", " ", text).strip()
    ws = words(text)
    nw = len(ws)
    ns = max(1, textstat.sentence_count(text))
    syl = textstat.syllable_count(text)
    nom = sum(1 for w in ws if len(w) >= NOMINAL_MIN and w.lower().endswith(NOMINAL_SUF))
    numerals = len(re.findall(r"\d+(?:[.,]\d+)*%?", text))
    return {
        "n_words": nw,
        "n_sentences": ns,
        "words_per_sentence": round(nw / ns, 3),
        "syllables_per_word": round(syl / max(1, nw), 4),
        "flesch": round(textstat.flesch_reading_ease(text), 2),
        "nominalisations": nom,
        "nominal_per_100w": round(100.0 * nom / max(1, nw), 3),
        "numerals": numerals,
        "numerals_per_100w": round(100.0 * numerals / max(1, nw), 3),
    }


if __name__ == "__main__":
    import json, sys
    print(json.dumps(measure(sys.stdin.read()), indent=1))
