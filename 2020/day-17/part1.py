#!/usr/bin/env python

import aoc
from collections import defaultdict


def solve(inp: str):
    grid = defaultdict(bool)
    for x, line in enumerate(inp.splitlines()):
        for y, char in enumerate(line):
            grid[(x, y, 0)] = char == '#'

    for cycle in range(6):
        min_x = min(x for x, _, _ in grid.keys())-1
        max_x = max(x for x, _, _ in grid.keys())+2
        min_y = min(y for _, y, _ in grid.keys())-1
        max_y = max(y for _, y, _ in grid.keys())+2
        min_z = min(z for _, _, z in grid.keys())-1
        max_z = max(z for _, _, z in grid.keys())+2

        new_grid = grid.copy()
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                for z in range(min_z, max_z):
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
