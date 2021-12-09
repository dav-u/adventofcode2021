#!/usr/bin/env python3

import sys
import math

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

def is_point_in_bounds(point, hor_max_ex, vert_max_ex):
    return is_in_bounds(point[0], hor_max_ex) and is_in_bounds(point[1], vert_max_ex)

def check(candidate, adjacent):
    if not is_point_in_bounds(adjacent, len_x, len_y):
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

def print_debug(visited_points):
    for y in range(len_y):
        for x in range(len_x):
            is_red = (x, y) in visited_points
            if is_red:
                print(u"\u001b[31m", end="")
            print(nums[y][x], end="")
            if is_red:
                print(u"\u001b[0m", end="")
        print()
    print()

def count_basin_size_rec(starting_point, visited_points):
    # only consider valid points
    if not is_point_in_bounds(starting_point, len_x, len_y):
        return

    #if the point was handled before, we return
    if starting_point in visited_points:
        return

    # 9's are the border of basins and are not counted
    if nums[starting_point[1]][starting_point[0]] == 9:
        return

    visited_points.add(starting_point)
    #print_debug(visited_points)

    #handle adjacent numbers
    left_point = (starting_point[0]-1, starting_point[1])
    right_point = (starting_point[0]+1, starting_point[1])
    top_point = (starting_point[0], starting_point[1]+1)
    bottom_point = (starting_point[0], starting_point[1]-1)

    count_basin_size_rec(left_point, visited_points)
    count_basin_size_rec(right_point, visited_points)
    count_basin_size_rec(top_point, visited_points)
    count_basin_size_rec(bottom_point, visited_points)

def count_basin_size(starting_point):
    visited_points = set()
    count_basin_size_rec(starting_point, visited_points)
    return len(visited_points)

largest_basin_sizes = sorted([count_basin_size(p) for p in low_points], reverse=True)
print(math.prod(largest_basin_sizes[:3]))

