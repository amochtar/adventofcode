#!/usr/bin/env python

from collections import defaultdict


def get_parameter(opcodes, i, mode, base):
    if mode == 1:
        return opcodes[i]
    elif mode == 2:
        return opcodes[base+opcodes[i]]
    return opcodes[opcodes[i]]


def get_parameter_write(opcodes, i, mode, base):
    if mode == 2:
        return base+opcodes[i]
    return opcodes[i]


def write_parameter(opcodes, i, mode, base, value):
    target = opcodes[i]
    if mode == 2:
        target += base
    opcodes[target] = value


def run(opcodes, inp):
    used = False
    i = 0
    out = []
    base = 0
    while True:
        opcode = opcodes[i] % 100
        modes = [int(p)
                 for p in reversed(str(opcodes[i] // 100).rjust(4, '0'))]
        a = get_parameter(opcodes, i+1, modes[0], base)
        b = get_parameter(opcodes, i+2, modes[1], base)

        if opcode == 1:
            a = get_parameter(opcodes, i+1, modes[0], base)
            b = get_parameter(opcodes, i+2, modes[1], base)
            write_parameter(opcodes, i+3, modes[2], base, a+b)
            i += 4
        elif opcode == 2:
            a = get_parameter(opcodes, i+1, modes[0], base)
            b = get_parameter(opcodes, i+2, modes[1], base)
            write_parameter(opcodes, i+3, modes[2], base, a*b)
            i += 4
        elif opcode == 3:
            write_parameter(opcodes, i+1, modes[0], base, inp)
            i += 2
        elif opcode == 4:
            a = get_parameter(opcodes, i+1, modes[0], base)
            yield a
            i += 2
        elif opcode == 5:
            a = get_parameter(opcodes, i+1, modes[0], base)
            b = get_parameter(opcodes, i+2, modes[1], base)
            if a != 0:
                i = b
            else:
                i += 3
        elif opcode == 6:
            a = get_parameter(opcodes, i+1, modes[0], base)
            b = get_parameter(opcodes, i+2, modes[1], base)
            if a == 0:
                i = b
            else:
                i += 3
        elif opcode == 7:
            a = get_parameter(opcodes, i+1, modes[0], base)
            b = get_parameter(opcodes, i+2, modes[1], base)
            if a < b:
                write_parameter(opcodes, i+3, modes[2], base, 1)
            else:
                write_parameter(opcodes, i+3, modes[2], base, 0)
            i += 4
        elif opcode == 8:
            a = get_parameter(opcodes, i+1, modes[0], base)
            b = get_parameter(opcodes, i+2, modes[1], base)
            if a == b:
                write_parameter(opcodes, i+3, modes[2], base, 1)
            else:
                write_parameter(opcodes, i+3, modes[2], base, 0)
            i += 4
        elif opcode == 9:
            a = get_parameter(opcodes, i+1, modes[0], base)
            base += a
            i += 2
        elif opcode == 99:
            return


def solve(opcodes):
    opcodes = defaultdict(
        int, {i: int(v) for i, v in enumerate(opcodes)})
    print(list(run(opcodes, 1)))
    print(list(run(opcodes, 2)))


# with open('test.txt', 'r') as f:
#     inp = f.read().strip().split(',')
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read().strip().split(',')
    solve(inp)
