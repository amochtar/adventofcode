#!/usr/bin/env python

import aoc
import networkx as nx
from math import prod


@aoc.timing
def part1(inp: str):
    area, w, h = aoc.grid(inp, int)
    risk = 0
    for (x, y), v in aoc.walk_grid(area):
        if all(area[b][a] > v for (a, b) in aoc.neighbors4((x, y), (0, 0), (w-1, h-1))):
            risk += v + 1
    return risk


@aoc.timing
def part2(inp: str):
    area, w, h = aoc.grid(inp, int)

    graph = nx.Graph()
    for (x, y), v in aoc.walk_grid(area):
        if v == 9:
            continue
        for (a, b) in aoc.neighbors4((x, y), (0, 0), (w-1, h-1)):
            if area[b][a] != 9:
                graph.add_edge((x, y), (a, b))

    basins = map(len, nx.connected_components(graph))
    return prod(sorted(basins, reverse=True)[:3])


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", part1(inp))
#     print("Part 2:", part2(inp))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
