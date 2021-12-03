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

def get_rating(nums, get_bit_value):
    filtered_nums = nums

    for i in range(input_bit_length-1, -1, -1):
        one_count = sum(1 for x in filtered_nums if (x & (1<<i)) != 0)
        bit_value = get_bit_value(len(filtered_nums), one_count)

        filtered_nums = [x for x in filtered_nums if ((x & (1<<i)) >> i) == bit_value]
        #print(filtered_nums)
        #print(list(map(bin, filtered_nums)))
        if len(filtered_nums) == 1:
            break;

    return filtered_nums[0]

oxygen_rating = get_rating(
        nums,
        lambda all_count, one_count: 1 if all_count <= 2*one_count else 0)
print(oxygen_rating)

scrubber_rating = get_rating(
        nums,
        lambda all_count, one_count: 0 if all_count <= 2*one_count else 1)
print(scrubber_rating)

print('Result %d' % (oxygen_rating*scrubber_rating))
