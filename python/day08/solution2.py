#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()

# map length of signal to number
known_mappings = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

'''
Counts the number of segments both patterns have in common.
p1 and p2 are sorted lists of chars which resemble patterns.
'''
def count_pattern_similarities(p1, p2):
    p1_i = 0
    p2_i = 0
    count = 0

    while p1_i < len(p1) and p2_i < len(p2):
        p1_c = p1[p1_i]
        p2_c = p2[p2_i]
        if p1_c == p2_c:
            count += 1
            p1_i += 1
            p2_i += 1
        elif p1_c < p2_c:
            p1_i += 1
        else: #p1_c > p2_c
            p2_i += 1

    return count

def solve_pattern(p, d):
    sim_1 = count_pattern_similarities(p.pattern_split, d[1].pattern_split)

    if p.pattern_len == 5: # => pattern either 2, 3 or 5
        if sim_1 == 2:
            return 3

        sim_4 = count_pattern_similarities(p.pattern_split, d[4].pattern_split)

        return 2 if sim_4 == 2 else 5

    else: # len == 6 => pattern either 0, 6 or 9
        if sim_1 == 1:
            return 6
        else:
            sim_4 = count_pattern_similarities(p.pattern_split, d[4].pattern_split)

            return 9 if sim_4 == 4 else 0

class SignalPattern:
    def __init__(self, pattern):
        self.pattern_split = sorted(pattern)
        self.pattern = "".join(self.pattern_split)
        self.pattern_len = len(pattern)

        if self.pattern_len in known_mappings:
            self.associated_num = known_mappings[self.pattern_len]
        else:
            self.associated_num = -1

    def __str__(self):
        num = '?' if self.associated_num == -1 else self.associated_num
        result = '(%s %s)' % (num, self.pattern)
        return result

class Entry:
    def __init__(self, signal_patterns, output):
        self.signal_patterns = [SignalPattern(p) for p in signal_patterns]
        self.output = output

    def solve_pattern_association(self):
        known_patterns = dict(
                (p.associated_num, p)
                for p in self.signal_patterns
                if p.associated_num != -1
            )
        unsolved_patterns = [p for p in self.signal_patterns if p.associated_num == -1]
        for p in unsolved_patterns:
            p.associated_num = solve_pattern(p, known_patterns)

    def calculate_output(self):
        pattern_mapping = dict(
                (p.pattern, p.associated_num)
                for p in self.signal_patterns)

        result = 0
        for o in self.output:
            result *= 10 # base 10
            o_sorted = "".join(sorted(o))
            value = pattern_mapping[o_sorted]
            result += value

        return result

    def __str__(self):
        result = ' '.join(map(str, self.signal_patterns))
        result += ' | '
        result += ' '.join(self.output)

        return result

    def __repr__(self):
        result = str(self)
        return result


split_lines = [line.split(' | ') for line in lines]

entries = [Entry(s[0].split(' '), s[1].rstrip().split(' ')) for s in split_lines]

for entry in entries:
    entry.solve_pattern_association()

print(sum(entry.calculate_output() for entry in entries))
