#!/usr/bin/env python

from aoc import *


def run(instructions: list):
    visited = set()
    acc, idx = 0, 0
    while idx < len(instructions) and idx not in visited:
        visited.add(idx)
        op, value = instructions[idx]

        if op == "nop":
            idx += 1
        elif op == "acc":
            idx += 1
            acc += value
        elif op == "jmp":
            idx += value

    return (idx not in visited, acc)


def solve(inp: str):
    instructions = []
    for line in inp.splitlines():
        op, value = line.split(" ", 2)
        instructions.append((op, int(value)))

    print("Part 1:", run(instructions)[1])

    for idx in range(len(instructions)):
        op, value = instructions[idx]
        if op in ["nop", "jmp"]:
            instr_mut = instructions[:]
            if op == "nop":
                instr_mut[idx] = ("jmp", value)
            else:
                instr_mut[idx] = ("nop", value)

            terminates, acc = run(instr_mut)
            if terminates:
                print("Part 2:", acc)
                return


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
