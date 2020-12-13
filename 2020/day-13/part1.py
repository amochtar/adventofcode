#!/usr/bin/env python

from aoc import *


def solve(inp: str):
    lines = inp.splitlines()
    time = int(lines[0])
    buses = [int(b) for b in lines[1].split(',') if b != 'x']

    fastest = min((b - (time % b), b) for b in buses)
    print(fastest[0]*fastest[1])


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
