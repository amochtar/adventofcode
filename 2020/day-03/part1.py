#!/usr/bin/env python

from aoc import *
from collections import defaultdict


def solve(inp):
    print(inp)

    x, y = 0, 0
    num_trees = 0

    while y < len(inp)-1:
        x = (x + 3) % len(inp[0])
        y += 1
        if inp[y][x] == '#':
            num_trees += 1

    print(num_trees)


# with open('test.txt', 'r') as f:
#     inp = f.read().splitlines()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
