#!/usr/bin/env python
import networkx as nx


def solve(input):
    G = nx.Graph()

    for orbit in input:
        objects = orbit.split(')')
        if len(objects) > 1:
            G.add_edge(objects[0], objects[1])

    print(len(nx.shortest_path(G, 'YOU', 'SAN'))-3)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
