#!/usr/bin/env python3

import sys
from statistics import median
from statistics import mean

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()

positions = list(map(int, lines[0].split(',')))

pos_median = round(median(positions))
pos_mean = round(mean(positions))

def calc_fuel(positions, pos):
    return sum(abs(p-pos)*(abs(p-pos)+1)//2 for p in positions)

d = pos_median - pos_mean
step = d//abs(d)

prev_fuel = calc_fuel(positions, pos_mean)
for i in range(step, d+step, step):
    fuel = calc_fuel(positions, pos_mean+i)

    if fuel > prev_fuel:
        break

    prev_fuel = fuel

print(prev_fuel)
