#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Expected one argument, got %d instead" % len(sys.argv))
    exit(1)

filename = sys.argv[1]

def from_bin_str_to_int(bin_str):
    result = 0
    for c in bin_str:
        if c not in ['0', '1']:
            continue

        result <<= 1

        if c == '1':
            result |= 1

    return result

with open(filename) as file:
    lines = file.readlines()
    nums = list(map(from_bin_str_to_int, lines))

input_bit_length = len(lines[0])-1
input_bit_mask = (1 << input_bit_length) - 1

gamma_rate = 0

for i in range(input_bit_length):
    one_count = sum(1 for x in nums if (x & (1<<i)) != 0)
    print(one_count)

    if len(nums) < 2*one_count:
        gamma_rate |= 1 << i

epsilon_rate = ~gamma_rate & input_bit_mask

print('Gamma rate: %d (%s)' % (gamma_rate, bin(gamma_rate)))
print('Epsilon rate: %d (%s)' % (epsilon_rate, bin(epsilon_rate)))
print('Result: %d' % (gamma_rate*epsilon_rate))
