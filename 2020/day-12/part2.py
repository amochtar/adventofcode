#!/usr/bin/env python

from aoc import *


def solve(inp: str):
    instructions = [(line[0].lower(), int(line[1:]))
                    for line in inp.splitlines()]

    wp = (10, -1)
    pos = origin
    for instr in instructions:
        if instr[0] in 'nsew':
            for _ in range(instr[1]):
                wp = moves[instr[0]](wp)
        if instr[0] == 'r':
            for _ in range(instr[1]//90):
                wp = rot_right(wp)
        if instr[0] == 'l':
            for _ in range(instr[1]//90):
                wp = rot_left(wp)
        if instr[0] == 'f':
            pos = add_pos(pos, wp, instr[1])

    print(manhattan(pos))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
