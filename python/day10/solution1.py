#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

cost = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def get_error_of_line(line):
    stack = []

    for char in line:
        if char in pairs:
            stack.append(char)
        else:
            expected = pairs[stack.pop()]
            if expected != char:
                # print('Expected %s, but found %s instead.' % (expected, char))
                return cost[char]

    return 0
            
print(sum(get_error_of_line(line) for line in lines))
