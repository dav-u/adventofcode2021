#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()

nums = [list(map(int, list(line.rstrip()))) for line in lines]

# nums[y][x]
adjacent_delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

len_x = len(nums[0])
len_y = len(nums)

def is_in_bounds(value, upper_bound_exclusive):
    return value >= 0 and value < upper_bound_exclusive

def check(candidate, adjacent):
    if not is_in_bounds(adjacent[0], len_x) or not is_in_bounds(adjacent[1], len_y):
        return True

    candidate_v = nums[candidate[1]][candidate[0]]
    adjacent_v = nums[adjacent[1]][adjacent[0]]

    return candidate_v < adjacent_v

low_points = []

for y in range(len_y):
    for x in range(len_x):
        is_low_point = True
        for d in adjacent_delta:
            if not check((x, y), (x+d[0], y+d[1])):
                is_low_point = False
                break;

        if is_low_point:
            low_points.append((x, y))

#print(low_points)

low_point_values = [nums[p[1]][p[0]] for p in low_points]
#print(low_point_values)

risk_level = sum(1+v for v in low_point_values)

print(risk_level)
