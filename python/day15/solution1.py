#!/usr/bin/env python3

'''
Dijkstra
'''

import sys
from collections import namedtuple

Point = namedtuple("Point", "x y")

filename = sys.argv[1]

with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]

nodes = [list(map(int, line)) for line in lines]
# nodes[y][x]

len_x = len(lines[0])
len_y = len(lines)

start_node = Point(0, 0)

# in costs are all nodes(and their cost)
# which need to be explored
costs = {start_node: 0}
visited = set()
visited.add(start_node)

adjacent_deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_coord(coord):
    return coord.x >= 0 and coord.x < len_x and coord.y >= 0 and coord.y < len_y

while True:
    # select node with min cost
    node, node_cost = min(costs.items(), key=lambda i: i[1])
    #print('Min node is:', node, node_cost)

    if node == (len_x-1, len_y-1):
        print("Found way")
        print("Cost:", node_cost)
        break

    for d in adjacent_deltas:
        adjacent_node = Point(node.x+d[0], node.y+d[1])
        if not is_valid_coord(adjacent_node):
            continue
        
        if adjacent_node in visited:
            continue

        costs[adjacent_node] = node_cost + nodes[adjacent_node.x][adjacent_node.y]
        visited.add(adjacent_node)
    del costs[node]
