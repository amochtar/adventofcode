#!/usr/bin/env python

from aoc import *


def solve(inp: str):
    lines = inp.splitlines()
    buses = [(i, int(b))
             for i, b in enumerate(lines[1].split(',')) if b != 'x']

    time = 0
    offset = 1
    for dt, b in buses:
        while (dt+time) % b != 0:
            time += offset
        offset *= b

    print(time)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
