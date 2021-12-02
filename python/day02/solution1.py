#!/usr/bin/env python3

import sys
import functools

if len(sys.argv) != 2:
    print("Incorrect number of arguments. Expected 1 got %d" % (len(sys.argv)-1))
    exit(1)

'''
Takes an instruction string like 'forward 5'
and converts it into the change in y and z coordinates.
Returns the change in y and z coordinates in a tuple (y, z).
Either y or z is 0.
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
#print(pos_changes)

pos = functools.reduce(
        lambda pos, change: (pos[0]+change[0], pos[1]+change[1]),
        pos_changes,
        pos)

print(pos)
print(pos[0]*pos[1])
