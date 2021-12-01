#!/usr/bin/env python3

import sys

if (len(sys.argv) != 2):
    print("Expected one argument (filename), got %d" % (len(sys.argv)-1))
    exit(1)

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()
    depths = list(map(lambda x: int(x), lines))

increase_count = 0

for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        increase_count += 1

print("Increase count: %d" % increase_count)
