#!/usr/bin/env python

from aoc import *


def solve(inp):
    inp = list(map(int, inp.splitlines()))

    n = len(inp)
    for x in range(n):
        for y in range(x+1, n):
            if inp[x] + inp[y] == 2020:
                print("Part 1:", inp[x]*inp[y])

            for z in range(y+1, n):
                if inp[x] + inp[y] + inp[z] == 2020:
                    print("Part 2:", inp[x]*inp[y]*inp[z])


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
