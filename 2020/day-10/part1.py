#!/usr/bin/env python

from aoc import *


def solve(inp: str):
    adapters = sorted([int(i) for i in inp.splitlines()])
    adapters = [0] + adapters + [max(adapters)+3]  # add wall outlet and device

    ones = 0
    threes = 0

    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i-1] == 1:
            ones += 1
        if adapters[i] - adapters[i-1] == 3:
            threes += 1

    print(ones * threes)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
