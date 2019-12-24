#!/usr/bin/env python

import numpy as np
from itertools import product


def neighbors(p, h, w):
    n = []
    px, py = p
    if py > 0:
        n.append((px, py-1))
    if py < h - 1:
        n.append((px, py+1))
    if px > 0:
        n.append((px-1, py))
    if px < w - 1:
        n.append((px+1, py))

    return n


def rating(grid):
    powers = 2 ** np.arange(grid.size)
    powers = powers.reshape(grid.shape)
    return np.sum(grid*powers)


def solve(inp):
    grid = np.array([[1 if c == '#' else 0 for c in line]
                     for line in inp.splitlines()])

    h, w = grid.shape
    seen = set()
    while True:
        if str(grid) in seen:
            break
        seen.add(str(grid))

        new_grid = grid.copy()
        for p in product(range(h), range(w)):
            bugs = 0
            for n in neighbors(p, h, w):
                bugs += grid[n]
            if grid[p] == 0:
                new_grid[p] = 1 if 1 <= bugs <= 2 else 0
            if grid[p] == 1:
                new_grid[p] = 1 if bugs == 1 else 0
        grid = new_grid
    print(rating(grid))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
