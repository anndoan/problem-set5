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
print(strand_count.items())
print(mismatches_count.items())


        
    
