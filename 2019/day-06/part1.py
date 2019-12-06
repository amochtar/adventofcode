#!/usr/bin/env python
import networkx as nx


def count_orbits(G, n):
    cnt = len(nx.descendants(G, n))
    for x in G.successors(n):
        cnt += count_orbits(G, x)
    return cnt


def solve(input):
    G = nx.DiGraph()

    for orbit in input:
        objects = orbit.split(')')
        if len(objects) > 1:
            G.add_edge(objects[0], objects[1])

    print(count_orbits(G, 'COM'))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
