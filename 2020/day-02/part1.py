#!/usr/bin/env python

import parse
from aoc import *
from collections import Counter


def solve(inp):
    p = parse.compile("{:d}-{:d} {}: {}")

    valid = 0
    for line in inp.splitlines():
        min_occ, max_occ, ch, password = p.parse(line).fixed

        if min_occ <= password.count(ch) <= max_occ:
            valid += 1
    print(valid)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
