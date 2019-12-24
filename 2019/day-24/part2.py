#!/usr/bin/env python

from itertools import product
from collections import defaultdict
from copy import deepcopy


def neighbors(l, x, y):
    n = set()

    if y > 0:
        n.add((l, (x, y-1)))
    if y < 4:
        n.add((l, (x, y+1)))
    if x > 0:
        n.add((l, (x-1, y)))
    if x < 4:
        n.add((l, (x+1, y)))

    n.discard((l, (2, 2)))

    if x == 0:
        nl = l-1
        n.add((nl, (1, 2)))
    elif x == 4:
        nl = l-1
        n.add((nl, (3, 2)))
    elif (x, y) == (1, 2):
        nl = l+1
        n.add((nl, (0, 0)))
        n.add((nl, (0, 1)))
        n.add((nl, (0, 2)))
        n.add((nl, (0, 3)))
        n.add((nl, (0, 4)))
    elif (x, y) == (3, 2):
        nl = l+1
        n.add((nl, (4, 0)))
        n.add((nl, (4, 1)))
        n.add((nl, (4, 2)))
        n.add((nl, (4, 3)))
        n.add((nl, (4, 4)))

    if y == 0:
        nl = l-1
        n.add((nl, (2, 1)))
    elif y == 4:
        nl = l-1
        n.add((nl, (2, 3)))
    elif (x, y) == (2, 1):
        nl = l+1
        n.add((nl, (0, 0)))
        n.add((nl, (1, 0)))
        n.add((nl, (2, 0)))
        n.add((nl, (3, 0)))
        n.add((nl, (4, 0)))
    elif (x, y) == (2, 3):
        nl = l+1
        n.add((nl, (0, 4)))
        n.add((nl, (1, 4)))
        n.add((nl, (2, 4)))
        n.add((nl, (3, 4)))
        n.add((nl, (4, 4)))

    return n


def solve(inp, minutes=200):
    lines = inp.splitlines()
    grids = defaultdict(lambda: defaultdict(int))
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grids[0][(x, y)] = 1 if c == '#' else 0

    for i in range(minutes):
        new_grids = deepcopy(grids)
        # assume it takes 2 minutes to reach a new level
        min_l, max_l = -i//2-1, i//2+1
        for l, x, y in product(range(min_l, max_l+1), range(5), range(5)):
            if (x, y) == (2, 2):
                continue
            bugs = 0
            for nl, nxy in neighbors(l, x, y):
                bugs += grids[nl][nxy]

            if grids[l][(x, y)] == 0:
                new_grids[l][(x, y)] = 1 if 1 <= bugs <= 2 else 0
            if grids[l][(x, y)] == 1:
                new_grids[l][(x, y)] = 1 if bugs == 1 else 0

        grids = new_grids

    print(sum(sum(g.values()) for g in grids.values()))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp, 10)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
