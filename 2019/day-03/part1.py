#!/usr/bin/env python

from collections import defaultdict
import itertools


def manhattan(a, b=itertools.repeat(0)):
    return sum([abs(a-b) for a, b in zip(a, b)])


def solve(input):
    wire1, wire2 = input
    wire1 = wire1.split(',')
    wire2 = wire2.split(',')

    grid = defaultdict(lambda: '.')
    pos = (0, 0)
    for step in wire1:
        if step[0] == 'L':
            char = '-'
            direction = (-1, 0)
        elif step[0] == 'R':
            direction = (1, 0)
            char = '-'
        elif step[0] == 'U':
            direction = (0, 1)
            char = '|'
        elif step[0] == 'D':
            direction = (0, -1)
            char = '|'

        for i in range(int(step[1:])-1):
            pos = (pos[0] + direction[0], pos[1]+direction[1])
            # print(pos)
            grid[pos] = char

        pos = (pos[0] + direction[0], pos[1]+direction[1])
        grid[pos] = '+'

        # print(grid)

    pos = (0, 0)
    for step in wire2:
        if step[0] == 'L':
            char = '-'
            direction = (-1, 0)
        elif step[0] == 'R':
            direction = (1, 0)
            char = '-'
        elif step[0] == 'U':
            direction = (0, 1)
            char = '|'
        elif step[0] == 'D':
            direction = (0, -1)
            char = '|'

        for i in range(int(step[1:])-1):
            pos = (pos[0] + direction[0], pos[1]+direction[1])
            # print(pos)
            if grid[pos] != '.':
                char = 'X'
            grid[pos] = char

        pos = (pos[0] + direction[0], pos[1]+direction[1])
        grid[pos] = '+'

    print(sorted([manhattan((0, 0), pos)
                  for (pos, x) in grid.items() if x == 'X'])[0])


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
