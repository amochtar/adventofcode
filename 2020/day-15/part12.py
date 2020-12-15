#!/usr/bin/env python

import aoc
from collections import defaultdict


def solve(inp: str):
    nums = defaultdict(list)
    turn, last = 1, 0
    for n in aoc.ints(inp):
        nums[n].append(turn)
        turn += 1
        last = n

    while turn <= 30000000:
        if turn == 2020 + 1:
            print("Part 1:", last)

        new_num = 0
        if len(nums[last]) >= 2:
            new_num = abs(nums[last][-1] - nums[last][-2])
        nums[new_num].append(turn)

        turn += 1
        last = new_num
    print("Part 2:", last)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
