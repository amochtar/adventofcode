#!/usr/bin/env python

import aoc
import networkx as nx
from math import prod


@aoc.timing
def part1(inp: str):
    area = [list(map(int, line)) for line in inp.splitlines()]
    w, h = len(area[0]), len(area)
    risk = 0
    for y in range(h):
        for x in range(w):
            if all(area[b][a] > area[y][x] for (a, b) in aoc.neighbors4(
                    (x, y)) if a >= 0 and a < w and b >= 0 and b < h):
                risk += 1+area[y][x]
    return risk


@aoc.timing
def part2(inp: str):
    area = [list(map(int, line)) for line in inp.splitlines()]
    w, h = len(area[0]), len(area)

    graph = nx.Graph()
    for y in range(h):
        for x in range(w):
            if area[y][x] == 9:
                continue
            for (a, b) in aoc.neighbors4((x, y)):
                if a >= 0 and a < w and b >= 0 and b < h:
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
