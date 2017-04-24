#! /usr/bin/env python3

import sys
from collections import Counter

filename = sys.argv[1]

counts = Counter()
type(counts)

for line in open(filename):
    if line.startswith('#'): continue
    fields = line.split('\t')
    chrom = fields[0]
    counts[chrom] += 1

for chrom, count in counts.items():
    print(chrom, count, sep = '\t')
sortme = [(v,k) for k,v in counts.items()]

sortme

sortme.sort()

sortme

sortme.reverse()

print(sortme[0][1])
