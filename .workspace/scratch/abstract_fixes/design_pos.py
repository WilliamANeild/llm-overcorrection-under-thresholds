"""Report the design-sentence position for each variant, same regex used on the corpus."""
import re, sys
DES = re.compile(r'^(We |In this (paper|work|study)|This (paper|work|study)|Here,? we|To (this|that) end,? we)', re.I)
for f in sys.argv[1:]:
    t = open(f).read().strip()
    s = [x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if len(x.split()) > 3]
    pos = next((i for i, x in enumerate(s, 1) if DES.match(x)), None)
    longest = max(len(x.split()) for x in s)
    print(f"{f.split('/')[-1].replace('.txt',''):<26} design at S{pos} of {len(s)}   longest sentence {longest}w")
