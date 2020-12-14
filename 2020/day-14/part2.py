#!/usr/bin/env python

import aoc


def solve(inp: str):
    program = [line.split(' = ') for line in inp.splitlines()]
    mask = {}
    memory = {}
    for b, val in program:
        if b == 'mask':
            mask = list(val)
        else:
            address = aoc.ints(b)[0]
            bitaddress = list(bin(address)[2:].zfill(36))
            for i, b in enumerate(mask):
                if b == '1':
                    bitaddress[i] = b

            floating = [i for i, b in enumerate(mask) if b == 'X']
            for ones in aoc.powerset(floating):
                for b in floating:
                    if b in ones:
                        bitaddress[b] = '1'
                    else:
                        bitaddress[b] = '0'
                address = int(''.join(bitaddress), 2)
                memory[address] = int(val)

    print(sum(memory.values()))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
