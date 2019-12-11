#!/usr/bin/env python

import intcode


def solve(opcodes):
    print(list(intcode.runner(opcodes, 5))[-1])


# with open('test.txt', 'r') as f:
#     input = list(map(int, f.read().split(',')))
#     solve(input)

with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
    solve(input)
