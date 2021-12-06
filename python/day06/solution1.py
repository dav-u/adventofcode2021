#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Expected one argument, but got %d" % (len(sys.argv)-1))
    exit(1)

filename = sys.argv[1]

with open(filename) as file:
    line = file.readlines()[0]

fish_state = list(map(int, line.split(',')))

for day in range(80):
    new_count = 0
    for i,fish in enumerate(fish_state):
        if fish == 0:
            new_count += 1
            fish_state[i] = 6
        else:
            fish_state[i] = fish - 1

    fish_state.extend([8] * new_count)
    new_count = 0

print("Number of fish:", len(fish_state))
