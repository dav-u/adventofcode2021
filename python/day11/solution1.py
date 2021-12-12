#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()

nums = [list(map(int, list(line.rstrip()))) for line in lines]

len_x = len(nums[0])
len_y = len(nums)
count = 0

adjacent_deltas = []
for x in range(-1, 2):
    for y in range(-1, 2):
        if x == 0 and y == 0: continue
        adjacent_deltas.append((x, y))

def debug_print():
    for y in range(len_y):
        for x in range(len_x):
            if nums[y][x] == -1:
                print('\033[91m', end="")
                print('_', end="")
                print('\033[0m', end="")
            elif nums[y][x] == 0:
                print('\033[93m', end="")
                print('0', end="")
                print('\033[0m', end="")
            elif nums[y][x] >= 10:
                print('ABCDEFGHIJ'[nums[y][x]-10], end="")
            else: print(nums[y][x], end="")
        print()
    print()

def coord_is_valid(coord):
    return coord[0] >= 0 and coord[0] < len_x and coord[1] >= 0 and coord[1] < len_y

def increment_energies():
    for y in range(len_y):
        for x in range(len_x):
            nums[y][x] += 1

def mark_flashes_and_get_count():
    c = 0
    for y in range(len_y):
        for x in range(len_x):
            if nums[y][x] > 9:
                nums[y][x] = -1
                c += 1
    return c

def increment_flash_adjacent_octopuses(x, y):
    for d in adjacent_deltas:
        coord = (x+d[0], y+d[1])

        if not coord_is_valid(coord): continue

        # if an octopus flashed in this step it is not incremented again
        if nums[coord[1]][coord[0]] in [-1, 0]: continue

        nums[coord[1]][coord[0]] += 1

def handle_unhandled_flashes():
    # unhandled flashes are marked with -1
    # if they are handled the get set to 0
    for y in range(len_y):
        for x in range(len_x):
            if nums[y][x] == -1:
                increment_flash_adjacent_octopuses(x, y)
                nums[y][x] = 0

for i in range(100):
    increment_energies()

    count += mark_flashes_and_get_count()

    run_again = True
    while run_again:
        handle_unhandled_flashes()

        c = mark_flashes_and_get_count()
        count += c
        run_again = c > 0

print(count)
