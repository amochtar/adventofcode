#!/usr/bin/env python

from collections import defaultdict
from itertools import permutations


def get_parameter(opcodes, i, immediate_mode):
    if immediate_mode:
        return opcodes[i]
    return opcodes[opcodes[i]]


def run(opcodes, phases, outputs, amp):
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
                opcodes[opcodes[i+1]] = outputs[amp]
            else:
                opcodes[opcodes[i+1]] = phases[amp]
                used = True
            i += 2
        elif opcode == 4:
            a = get_parameter(opcodes, i+1, modes[0])
            yield a
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
            return


outputs = [0, 0, 0, 0, 0]


def run_series(opcodes, phases):
    outputs = [0, 0, 0, 0, 0]  # these are shared between runs
    amps = [run(opcodes[:], phases, outputs, amp) for amp in range(5)]
    amp = 0
    try:
        while True:
            out = next(amps[amp])
            amp = (amp+1) % 5
            outputs[amp] = out
    except StopIteration:
        return outputs[amp]


def solve(opcodes):
    phases_perms = permutations(range(5, 10))
    max_ret = 0
    for phases in phases_perms:
        ret = run_series(opcodes[:], phases)
        if ret > max_ret:
            print(phases, ret)
            max_ret = ret

    print(max_ret)


# with open('test.txt', 'r') as f:
#     input = list(map(int, f.read().split(',')))
#     solve(input)

with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
    solve(input)
