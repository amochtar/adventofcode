#!/usr/bin/env python

import aoc
from collections import Counter


@aoc.timing
def solve(inp: str, n: int = 80):
    fish = Counter(aoc.ints(inp))

    for _ in range(n):
        new_fish = Counter()
        for k, v in fish.items():
            if k <= 0:
                new_fish[8] += v
                new_fish[6] += v
            else:
                new_fish[k-1] += v
        fish = new_fish
    return sum(fish.values())


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", solve(inp))
#     print("Part 2:", solve(inp, 256))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", solve(inp))
    print("Part 2:", solve(inp, 256))
