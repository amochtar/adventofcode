#!/usr/bin/env python

import itertools


def manhattan(a, b=itertools.repeat(0)):
    return sum([abs(a-b) for a, b in zip(a, b)])


def wire_length(wire):
    pos = (0, 0)
    w = {}
    length = 0
    for step in wire:
        if step[0] == 'L':
            direction = (-1, 0)
        elif step[0] == 'R':
            direction = (1, 0)
        elif step[0] == 'U':
            direction = (0, 1)
        elif step[0] == 'D':
            direction = (0, -1)

        for i in range(int(step[1:])):
            length += 1
            pos = (pos[0] + direction[0], pos[1]+direction[1])
            w[pos] = length
    return w


def solve(input):
    wire1 = wire_length(input[0].split(','))
    wire2 = wire_length(input[1].split(','))

    intersections = wire1.keys() & wire2.keys()
    print(min([manhattan(pos) for pos in intersections]))
    print(min([wire1[pos]+wire2[pos] for pos in intersections]))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
