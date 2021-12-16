#!/usr/bin/env python3

import sys
import math

filename = sys.argv[1]

with open(filename) as file:
    content = file.read().rstrip()

class Package:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

class LiteralValuePackage(Package):
    def __init__(self, version, type_id, value):
        super().__init__(version, type_id)
        self.value = value

    def __str__(self):
        return "Literal: " + str(self.value)

class OperatorPackage(Package):
    def __init__(self, version, type_id, length_id, length, sub_packages):
        super().__init__(version, type_id)

        self.length_id = length_id
        self.length = length
        self.sub_packages = sub_packages

    def __str__(self):
        result = "Operator:\n"
        sub = ['\t' + str(p) for p in self.sub_packages]
        for p in sub:
            result += p
            result += '\n'

        return result

hex_mapping = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

package_bits = []

for h in content:
    package_bits.extend(list(hex_mapping[h]))

parse_index = 0

def take_bits(count):
    global parse_index
    result = package_bits[parse_index:parse_index+count]
    parse_index += count

    return result

def get_number(count):
    bits = take_bits(count)
    number = int("".join(bits), 2)

    return number

def ignore_padding():
    # align to multiple of 4
    global parse_index
    misalign = parse_index % 4
    correction = 4 - misalign
    parse_index += correction

def parse_literal_value_body():
    value_bits = []
    is_done = False
    while not is_done:
        bits = take_bits(5)
        if bits[0] == '0':
            is_done = True
        value_bits.extend(bits[1:])
    value = int("".join(value_bits), 2)
    #ignore_padding()
    
    return value

def parse_operator_body_bit_length(version, type_id, length_type_id):
    sub_packages = []
    length = get_number(15)
    index_before = parse_index

    while parse_index - index_before != length:
        sub_packages.append(parse_package())

    return OperatorPackage(version, type_id, length_type_id, length, sub_packages)

def parse_operator_body_package_length(version, type_id, length_type_id):
    sub_packages = []
    sub_package_count = get_number(11)

    for _ in range(sub_package_count):
        sub_packages.append(parse_package())

    return OperatorPackage(version, type_id, length_type_id, sub_package_count, sub_packages)

def parse_operator_body(version, type_id):
    length_type_id = get_number(1)

    if length_type_id == 0:
        return parse_operator_body_bit_length(version, type_id, length_type_id)
    else: #length_type_pd == 1
        return parse_operator_body_package_length(version, type_id, length_type_id)

def parse_package():
    version = get_number(3)
    type_id = get_number(3)

    if type_id == 4:
        value = parse_literal_value_body()
        return LiteralValuePackage(version, type_id, value)
    else:
        return parse_operator_body(version, type_id)

package = parse_package()

def visit_sum(package):
    return sum(visit(p) for p in package.sub_packages)

def visit_product(package):
    return math.prod(visit(p) for p in package.sub_packages)

def visit_min(package):
    return min(visit(p) for p in package.sub_packages)

def visit_max(package):
    return max(visit(p) for p in package.sub_packages)

def visit_gt(package):
    a = visit(package.sub_packages[0])
    b = visit(package.sub_packages[1])
    return a > b

def visit_lt(package):
    a = visit(package.sub_packages[0])
    b = visit(package.sub_packages[1])
    return a < b

def visit_eq(package):
    a = visit(package.sub_packages[0])
    b = visit(package.sub_packages[1])
    return a == b

def visit(package):
    if package.type_id == 0:
        return visit_sum(package)
    elif package.type_id == 1:
        return visit_product(package)
    elif package.type_id == 2:
        return visit_min(package)
    elif package.type_id == 3:
        return visit_max(package)
    elif package.type_id == 4:
        return package.value
    elif package.type_id == 5:
        return visit_gt(package)
    elif package.type_id == 6:
        return visit_lt(package)
    elif package.type_id == 7:
        return visit_eq(package)

print(visit(package))
