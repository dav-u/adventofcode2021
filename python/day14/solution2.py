#!/usr/bin/env python3

'''
This solution has basically the same idea as day six (Lanternfish).
Instead of constructing the polymer string, just count the number of
occurences of each pair. Because each pair with the same letters
behaves the same, independent of its location in the polymer string,
this simplification can be made.

In the end though, the number of elements is required and not the
number of pairs. So the pairs are split up and each element is counted
seperately. But because the pairs overlap, each element is part of two
pairs (except the very first and the very last element). To account for this,
the count for each element needs to be divided by 2 and to correct for the
first and the last element we can just look at the first and last element
of the template, because they stay the first and the last element respectively,
and add one to their count.
'''

import sys
import collections

filename = sys.argv[1]

with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]

polymer_template = list(lines[0])

rules = dict(line.split(' -> ') for line in lines[2:])

# defaultdict lets me update the count, even 
# if the entry was not present before
pair_counts = collections.defaultdict(int)

for i in range(len(polymer_template) - 1):
    pair = "".join(polymer_template[i:i+2])
    pair_counts[pair] += 1

for step in range(40):
    new_pair_counts = collections.defaultdict(int)

    for pair, count in pair_counts.items():
        char_to_insert = rules.get(pair)

        if not char_to_insert:
            new_pair_counts[pair] += count
            continue

        resulting_pair_1 = pair[0] + char_to_insert
        resulting_pair_2 = char_to_insert + pair[1]

        new_pair_counts[resulting_pair_1] += count
        new_pair_counts[resulting_pair_2] += count

    pair_counts = new_pair_counts

element_counts = collections.defaultdict(int)

for pair, count in pair_counts.items():
    element_counts[pair[0]] += count
    element_counts[pair[1]] += count

for pair, count in element_counts.items():
    element_counts[pair] //= 2

element_counts[polymer_template[0]] += 1
element_counts[polymer_template[len(polymer_template)-1]] += 1

element_counts = list(element_counts.items())
element_counts.sort(key=lambda i: i[1])

print(element_counts[len(element_counts)-1][1] - element_counts[0][1])
