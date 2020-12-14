#!/usr/bin/env python

import aoc


def solve(inp: str):
    program = [line.split(' = ') for line in inp.splitlines()]
    mask = {}
    memory = {}
    for m, val in program:
        if m == 'mask':
            mask = {i: b for i, b in enumerate(val) if b != 'X'}
        else:
            address = aoc.ints(m)[0]
            bitval = list(bin(int(val))[2:].zfill(36))
            for i, b in mask.items():
                bitval[i] = b
            intval = int(''.join(bitval), 2)
            memory[address] = intval
    print(sum(memory.values()))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
