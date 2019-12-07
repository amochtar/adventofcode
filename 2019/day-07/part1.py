#!/usr/bin/env python

from collections import defaultdict
from itertools import permutations


def get_parameter(opcodes, i, immediate_mode):
    if immediate_mode:
        return opcodes[i]
    return opcodes[opcodes[i]]


def run(opcodes, phase, inp):
    used = False
    i = 0
    out = []
    while True:
        opcode = opcodes[i] % 100
        modes = [p == '1'
                 for p in reversed(str(opcodes[i] // 100).rjust(4, '0'))]

        if opcode == 1:
            a = get_parameter(opcodes, i+1, modes[0])
            b = get_parameter(opcodes, i+2, modes[1])
            opcodes[opcodes[i+3]] = a + b
            i += 4
        elif opcode == 2:
            a = get_parameter(opcodes, i+1, modes[0])
            b = get_parameter(opcodes, i+2, modes[1])
            opcodes[opcodes[i+3]] = a * b
            i += 4
        elif opcode == 3:
            if used:
                opcodes[opcodes[i+1]] = inp
            else:
                opcodes[opcodes[i+1]] = phase
                used = True
            i += 2
        elif opcode == 4:
            a = get_parameter(opcodes, i+1, modes[0])
            out.append(a)
            i += 2
        elif opcode == 5:
            a = get_parameter(opcodes, i+1, modes[0])
            b = get_parameter(opcodes, i+2, modes[1])
            if a != 0:
                i = b
            else:
                i += 3
        elif opcode == 6:
            a = get_parameter(opcodes, i+1, modes[0])
            b = get_parameter(opcodes, i+2, modes[1])
            if a == 0:
                i = b
            else:
                i += 3
        elif opcode == 7:
            a = get_parameter(opcodes, i+1, modes[0])
            b = get_parameter(opcodes, i+2, modes[1])
            if a < b:
                opcodes[opcodes[i+3]] = 1
            else:
                opcodes[opcodes[i+3]] = 0
            i += 4
        elif opcode == 8:
            a = get_parameter(opcodes, i+1, modes[0])
            b = get_parameter(opcodes, i+2, modes[1])
            if a == b:
                opcodes[opcodes[i+3]] = 1
            else:
                opcodes[opcodes[i+3]] = 0
            i += 4
        elif opcode == 99:
            break

    # print(out)
    return out[-1]


def solve(opcodes):
    phases_perms = permutations(range(5))
    max_ret = 0
    for phases in phases_perms:
        ret = 0
        for p in phases:
            ret = max(ret, run(opcodes[:], p, ret))

        if ret > max_ret:
            print(phases, ret)
            max_ret = ret
        # max_ret = max(ret, max_ret)

    print(max_ret)


# with open('test.txt', 'r') as f:
#     input = list(map(int, f.read().split(',')))
#     solve(input)

with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
    solve(input)
