#!/usr/bin/env python

from aoc import *
from itertools import combinations


def solve(inp: str, preamble_size: int):
    numbers = [int(i) for i in inp.splitlines()]

    invalid = 0
    for i in range(preamble_size, len(numbers)):
        preamble = numbers[i-preamble_size:i]
        if not any(sum(c) == numbers[i] for c in combinations(preamble, 2)):
            invalid = numbers[i]
            break

    print("Part 1:", invalid)

    for i in range(len(numbers)):
        j = i+2  # minimum of 2 numbers
        while sum(numbers[i:j]) < invalid:
            j += 1

        if sum(numbers[i:j]) == invalid:
            print("Part 2:", min(numbers[i:j]) + max(numbers[i:j]))
            return


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp, 5)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp, 25)
