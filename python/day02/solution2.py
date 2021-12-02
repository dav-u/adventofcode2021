#!/usr/bin/env python3

import sys
import functools

if len(sys.argv) != 2:
    print("Incorrect number of arguments. Expected 1 got %d" % (len(sys.argv)-1))
    exit(1)

'''
Takes an instruction string like 'forward 5'
and converts it into a tuple (f, a) forward and aim (aim is relative not absolute)
Either f or a is 0.
'''
def instruction_to_coord_change(instruction_string):
    split = instruction_string.split(' ')
    operation = split[0]
    argument = int(split[1])

    if operation == 'forward':
        return (argument, 0)
    elif operation == 'down':
        return (0, argument)
    elif operation == 'up':
        return (0, -argument)
    else:
        raise Exception('Unkown operation "%s"' % operation)

filename = sys.argv[1]
with open(filename) as file:
    lines = file.readlines()
    pos_changes = list(map(instruction_to_coord_change, lines))

pos = (0, 0) # (y, z)

y = 0
z = 0
aim = 0

for i in pos_changes:
    aim += i[1]

    y += i[0]
    z += aim * i[0]

print((y, z))
print(y*z)
