#!/usr/bin/env python

import parse
from aoc import *
from collections import Counter


def solve(inp):
    p = parse.compile("{:d}-{:d} {}: {}")

    valid = 0
    for line in inp.splitlines():
        first, second, ch, password = p.parse(line).fixed

        if (password[first-1] == ch) != (password[second-1] == ch):
            valid += 1
    print(valid)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
