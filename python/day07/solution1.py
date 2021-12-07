#!/usr/bin/env python3

import sys
from statistics import median

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()

positions = list(map(int, lines[0].split(',')))

m = round(median(positions))
s = sum(abs(m-x) for x in positions)
print(s)
