#!/usr/bin/env python3

import sys
import collections

if len(sys.argv) != 2:
    print("Expected one argument, but got %d" % (len(sys.argv)-1))
    exit(1)

filename = sys.argv[1]

with open(filename) as file:
    line = file.readlines()[0]

input_as_ints = map(int, line.split(','))
state = dict(collections.Counter(input_as_ints))

for day in range(256):
    new_state = {}
    for timer,count in state.items():
        if timer == 0:
            new_state[8] = count
            new_state[6] = new_state.get(6, 0) + count
        else: new_state[timer-1] = new_state.get(timer-1, 0) + count

    state = new_state

print(sum(count for _,count in state.items()))
