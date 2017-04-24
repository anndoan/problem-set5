#! /usr/bin/env python3

import sys
from collections import Counter

filename = sys.argv[1]

from pysam import AlignmentFile
bamfile = AlignmentFile(filename)

strand = []
mismatches = []
for record in bamfile:
    strand.append(record.flag)
    mismatches.append(record.get_tag('NM'))

strand_count = Counter(strand)
mismatches_count = Counter(mismatches)
sortme = [(v,k) for k, v in strand_count.items()]
print(sortme)

print("Total number of alignments on the negative(16) strand:",sortme[0][0])

print("Total number of alignments on the positive(0) strand:",sortme[1][0])
sortme = [(v,k) for k,v in mismatches_count.items()]
print(sortme)

print("Total number of alignments with no mismatches:",sortme[0][0])

print("Total number of alignments with more than zero mismatches is the sum of the following:")

print(sortme[1][0])
print(sortme[2][0])
print(sortme[3][0])
print(sortme[4][0])    
       
