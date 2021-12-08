#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()

outputs = [line.split(' | ')[1].rstrip() for line in lines]

outputs = [o.split(' ') for o in outputs]

count = 0

unique_segment_numbers = [2, 4, 3, 7]

for output in outputs:
    for o in output:
        if len(o) in unique_segment_numbers:
            count += 1

print(count)
