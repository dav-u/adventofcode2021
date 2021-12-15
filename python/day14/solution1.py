#!/usr/bin/env python3

import sys
import collections

filename = sys.argv[1]

with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]

polymer_template = list(lines[0])

rules = dict(line.split(' -> ') for line in lines[2:])

for step in range(10):
    length = len(polymer_template)
    i = 0

    while i < length - 1:
        pair = "".join(polymer_template[i:i+2])
        if pair in rules:
            polymer_template.insert(i+1, rules[pair])
            i += 1
            length += 1

        i += 1

quantities = sorted(collections.Counter(polymer_template).values())
print(quantities[-1] - quantities[0])
