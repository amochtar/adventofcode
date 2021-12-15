#!/usr/bin/env python

import aoc
from heapq import *


@aoc.timing
def solve(inp, part2=False):
    grid, w, h = aoc.grid(inp, int)

    if part2:
        # tile columns
        for y in range(h):
            grid[y].extend(aoc.mod1(grid[y][x-w]+1, 9) for x in range(w, w*5))
        # tile rows
        for y in range(h, h*5):
            grid.append(list(aoc.mod1(grid[y-h][x]+1, 9) for x in range(w*5)))
        w, h = len(grid[0]), len(grid)

    start = (0, 0)
    end = (w-1, h-1)
    q = [(0, start)]
    visited = set([start])
    while q:
        cost, (x, y) = heappop(q)
        if (x, y) == end:
            return cost

        for a, b in aoc.neighbors4((x, y), (0, 0), (w-1, h-1)):
            if (a, b) not in visited:
                visited.add((a, b))
                heappush(q, (cost + grid[b][a], (a, b)))

    return grid


@ aoc.timing
def part2(inp: str):
    return inp


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", solve(inp))
#     print("Part 2:", solve(inp, True))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", solve(inp))
    print("Part 2:", solve(inp, True))
