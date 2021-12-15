#!/usr/bin/env python3

import sys
from collections import namedtuple

Point = namedtuple('Point', 'x y')
Instruction = namedtuple('Instruction', 'axis value')

filename = sys.argv[1]

with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]

points = set()
instr_start_index = 0
for i, line in enumerate(lines):
    if not line:
        instr_start_index = i+1
        break;

    split = line.split(',')
    points.add(Point(int(split[0]), int(split[1])))

instructions = []
for i in range(instr_start_index, len(lines)):
    line = lines[i]
    last_part = line.split(' ')[2]
    split = last_part.split('=')
    instructions.append(Instruction(split[0], int(split[1])))

def fold_coord_comp(comp, fold_point):
    return comp if comp < fold_point else 2*fold_point - comp

def debug_print(points):
    max_x = 0
    max_y = 0
    for point in points:
        if point.x > max_x:
            max_x = point.x
        if point.y > max_y:
            max_y = point.y
    
    for y in range(max_y+1):
        for x in range(max_x+1):
            if Point(x, y) in points:
                print('#', end="")
            else: print('.', end="")
        print()
    print()

instr = instructions[0]
points_after_fold = set()
for point in points:
    folded_point = None
    if instr.axis == 'y':
        new_y = fold_coord_comp(point.y, instr.value)
        folded_point = Point(point.x, new_y)
    else: # instr.axis == 'x'
        new_x = fold_coord_comp(point.x, instr.value)
        folded_point = Point(new_x, point.y)
    points_after_fold.add(folded_point)

print(len(points_after_fold))
