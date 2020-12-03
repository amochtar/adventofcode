#!/usr/bin/env python

from aoc import *
from collections import defaultdict


def solve(inp):
    mult = 1

    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        x, y = 0, 0
        num_trees = 0

        while y < len(inp)-1:
            x = (x + dx) % len(inp[0])
            y += dy
            if inp[y][x] == '#':
                num_trees += 1
        print(x, y, num_trees)
        mult *= num_trees

    print(mult)


# with open('test.txt', 'r') as f:
#     inp = f.read().splitlines()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
