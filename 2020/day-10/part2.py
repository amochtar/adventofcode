#!/usr/bin/env python

from aoc import *
from collections import Counter


def solve(inp: str):
    adapters = sorted([int(i) for i in inp.splitlines()])
    adapters = [0] + adapters + [max(adapters)+3]  # add outlet and device

    arrangements = Counter({0: 1})
    for a in adapters:
        for b in range(1, 4):
            if a - b in adapters:
                arrangements[a] += arrangements[a-b]

    print(arrangements[max(arrangements)])


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
