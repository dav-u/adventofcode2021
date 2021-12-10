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
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def get_completion_score(line):
    stack = []

    for char in line:
        if char in pairs:
            stack.append(char)
        else:
            expected = pairs[stack.pop()]
            if expected != char:
                # invalid lines are discarded
                return 0

    # everything still present in stack has to be closed

    score = 0
    stack.reverse()

    for unmatched in stack:
        score *= 5
        score += cost[unmatched]

    return score

scores = [get_completion_score(line) for line in lines]
scores = [s for s in scores if s != 0]

scores.sort()
print(scores[len(scores)//2])

