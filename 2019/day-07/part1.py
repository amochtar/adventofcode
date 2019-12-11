#!/usr/bin/env python

from itertools import permutations, chain, repeat
import intcode


def solve(opcodes):
    phases_perms = permutations(range(5))
    max_ret = 0
    for phases in phases_perms:
        ret = 0
        for p in phases:
            inputs = chain(repeat(p, 1), repeat(ret))
            ret = max(ret, next(intcode.runner(opcodes, inputs)))

        if ret > max_ret:
            # print(phases, ret)
            max_ret = ret

    print(max_ret)


# with open('test.txt', 'r') as f:
#     input = list(map(int, f.read().split(',')))
#     solve(input)

with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
    solve(input)
