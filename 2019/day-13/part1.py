#!/usr/bin/env python

from collections import defaultdict
import intcode


def print_arcade(panels):
    minx = min([k[0] for k in panels.keys()])
    maxx = max([k[0] for k in panels.keys()])
    miny = min([k[1] for k in panels.keys()])
    maxy = max([k[1] for k in panels.keys()])

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if panels[(x, y)] == 0:
                print(' ', end='')
            if panels[(x, y)] == 1:
                print('#', end='')
            if panels[(x, y)] == 2:
                print('=', end='')
            if panels[(x, y)] == 3:
                print('_', end='')
            if panels[(x, y)] == 4:
                print('o', end='')
        print('')


def solve(opcodes):
    run = intcode.runner(opcodes)
    grid = defaultdict(int)
    try:
        while True:
            x, y, id = next(run), next(run), next(run)
            grid[(x, y)] = id
    except StopIteration:
        pass

    print_arcade(grid)
    print(len([v for v in grid.values() if v == 2]))


with open('input.txt', 'r') as f:
    inp = f.read().strip().split(',')
    solve(inp)
