#!/usr/bin/env python

from collections import defaultdict


def solve(opcodes):
    i = 0
    while True:
        if opcodes[i] == 1:
            opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] + \
                opcodes[opcodes[i+2]]
        elif opcodes[i] == 2:
            opcodes[opcodes[i+3]] = opcodes[opcodes[i+1]] * \
                opcodes[opcodes[i+2]]
        elif opcodes[i] == 99:
            break
        i += 4

    print(opcodes[0])


# with open('test.txt', 'r') as f:
#     input = list(map(int, f.read().split(',')))
#     solve(input)

with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
    input[1] = 12
    input[2] = 2
    solve(input)
