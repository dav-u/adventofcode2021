#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("Expected one argument, got %d" % (len(sys.argv)-1))
    exit(1)

filename = sys.argv[1]

with open(filename) as file:
    input_lines = file.readlines()

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def tuple(self):
        return (self.x, self.y)

    def normalize(self):
        if self.x != 0:
            self.x = self.x // abs(self.x)
        
        if self.y != 0:
            self.y = self.y // abs(self.y)

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def sub(v1, v2):
        x = v1.x - v2.x
        y = v1.y - v2.y

        return Vec(x, y)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def is_straight(self):
        return self.p1.x == self.p2.x or self.p1.y == self.p2.y

    def get_points(self):
        diff = Vec.sub(self.p2, self.p1)
        diff.normalize()

        p = self.p1

        while p != self.p2:
            yield p
            p.add(diff)

        yield p

def input_line_to_line(input_line):
    match = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", input_line)
    groups = match.groups()
    x1 = int(groups[0])
    y1 = int(groups[1])
    x2 = int(groups[2])
    y2 = int(groups[3])

    p1 = Vec(x1, y1)
    p2 = Vec(x2, y2)

    return Line(p1, p2)

lines = list(map(input_line_to_line, input_lines))

coords = {}

for line in lines:
    for point in line.get_points():
        pt = point.tuple()
        if not pt in coords:
            coords[pt] = 0

        coords[pt] = coords[pt]+1

def print_coords(coords):
    max_x = 0
    max_y = 0

    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in coords:
                print(coords[(x, y)], end="")
            else:
                print('.', end="")

        print()

#print_coords(coords)
count = sum(1 for k,v in coords.items() if v >= 2)
print(count)
