#!/usr/bin/env python

from aoc import *


def solve(inp: str):
    inp = inp.replace('F', '0').replace(
        'B', '1').replace('R', '1').replace('L', '0')
    passes = set([int(i, 2) for i in inp.splitlines()])
    seats = set(range(min(passes), max(passes) + 1))
    print(seats - passes)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
