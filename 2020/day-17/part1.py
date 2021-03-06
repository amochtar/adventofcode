#!/usr/bin/env python

import aoc
from collections import defaultdict


def solve(inp: str):
    grid = defaultdict(bool)
    for x, line in enumerate(inp.splitlines()):
        for y, char in enumerate(line):
            grid[(x, y, 0)] = char == '#'

    for _ in range(6):
        (min_x, max_x), \
            (min_y, max_y), \
            (min_z, max_z) = aoc.min_max(grid.keys())

        new_grid = grid.copy()
        for x in range(min_x-1, max_x+2):
            for y in range(min_y-1, max_y+2):
                for z in range(min_z-1, max_z+2):
                    p = (x, y, z)
                    active = grid[p]
                    active_neighbors = sum(grid[n]
                                           for n in aoc.neighbors_cube(p))
                    if active and (active_neighbors < 2 or active_neighbors > 3):
                        new_grid[p] = False
                    if not active and active_neighbors == 3:
                        new_grid[p] = True
        grid = new_grid

    print(sum(grid.values()))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
