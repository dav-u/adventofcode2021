#!/usr/bin/env python3

import sys

filename = sys.argv[1]

with open(filename) as file:
    lines = [line.rstrip() for line in file.readlines()]

node_connections = [line.split('-') for line in lines]

nodes = dict(
        (name, [])
        for names in
        node_connections
        for name in names)

for c in node_connections:
    nodes[c[0]].append(c[1])
    nodes[c[1]].append(c[0])

def count_distinct_ways(node_name, visited_nodes = set(), small_cave_visited_twice = None):
    if node_name == 'end':
        return 1

    connected_nodes = nodes[node_name]
    is_lower = node_name.islower()

    if is_lower:
        visited_nodes.add(node_name)

    count = 0
    for n in connected_nodes:
        # we never visit start again
        if n == 'start': continue
        if n in visited_nodes:
            # small caves are not allowed to be visited twice,
            # except it would be the first small cave we visite twice
            if small_cave_visited_twice == None:
                count += count_distinct_ways(n, visited_nodes, n)
            else: continue
        else:
            count += count_distinct_ways(n, visited_nodes, small_cave_visited_twice)

    if is_lower and node_name != small_cave_visited_twice:
        visited_nodes.remove(node_name)

    return count


print(count_distinct_ways('start'))
