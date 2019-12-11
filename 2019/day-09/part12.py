#!/usr/bin/env python

import intcode


def solve(opcodes):
    print(list(intcode.runner(opcodes, 1)))
    print(list(intcode.runner(opcodes, 2)))


# with open('test.txt', 'r') as f:
#     inp = f.read().strip().split(',')
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read().strip().split(',')
    solve(inp)
