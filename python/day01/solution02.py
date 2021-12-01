#!/usr/bin/env python3

import sys

if (len(sys.argv) != 2):
    print("Expected one argument (filename), got %d" % (len(sys.argv)-1))
    exit(1)

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()
    depths = list(map(lambda x: int(x), lines))

window_size = 3
summed_depths = []

for i in range(len(depths) - window_size + 1):
    summed_depths.append(sum(depths[i:i+window_size]))

increase_count = 0

for i in range(1, len(summed_depths)):
    if summed_depths[i-1] < summed_depths[i]:
        increase_count += 1

print("Increase count: %d" % increase_count)
