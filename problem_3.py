#! /usr/bin/env python3

import sys
from collections import Counter

filename = sys.argv[1]

count = 0
aka_hexamers_5 = Counter()
aka_hexamers_3 = Counter()

for line in open(filename):
    line = line.rstrip()

    if count == 0:
       name = line
       count += 1

    elif count == 1:
        seq = line
        count += 1

    elif count == 2:
        count += 1

    elif count == 3:
        qual = line
        count = 0
       
        aka_hexamer_5 = seq[0:6]
        aka_hexamer_3 = seq[-6:]
        aka_hexamers_5[aka_hexamer_5] += 1
        aka_hexamers_3[aka_hexamer_3] += 1

for key, value in aka_hexamers_5.items():
    print(aka_hexamer_5, value)

for key, value in aka_hexamers_3.items():
    print(aka_hexamer_3, value)
