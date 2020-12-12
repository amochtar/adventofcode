#!/usr/bin/env python

from aoc import *


def solve(inp: str):
    instructions = [(line[0].lower(), int(line[1:]))
                    for line in inp.splitlines()]

    facing = 'e'
    pos = origin
    for instr in instructions:
        if instr[0] in 'nsew':
            for _ in range(instr[1]):
                pos = moves[instr[0]](pos)
        if instr[0] == 'r':
            for _ in range(instr[1]//90):
                facing = right_turn[facing]
        if instr[0] == 'l':
            for _ in range(instr[1]//90):
                facing = left_turn[facing]
        if instr[0] == 'f':
            dir = facing_dir[facing]
            pos = add_pos(pos, dir, instr[1])

    print(manhattan(pos))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
