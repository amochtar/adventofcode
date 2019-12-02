#!/usr/bin/env python

from collections import defaultdict


def solve(opcodes):
    for i in range(100):
        for j in range(100):
            if run(opcodes[:], i, j) == 19690720:
                print(100*i+j)
                return


def run(opcodes, noun, verb):
    opcodes[1] = noun
    opcodes[2] = verb
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

    return opcodes[0]


# with open('test.txt', 'r') as f:
#     input = list(map(int, f.read().split(',')))
#     solve(input)

with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
    solve(input)
