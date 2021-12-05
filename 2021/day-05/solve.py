#!/usr/bin/env python

from typing import Counter
import aoc


@aoc.timing
def solve(inp: str, part2=False):
    lines = [aoc.ints(line) for line in inp.splitlines()]
    positions = Counter()
    for (x1, y1, x2, y2) in lines:
        if part2 or (x1 == x2 or y1 == y2):
            dx = aoc.sign(x2-x1)
            dy = aoc.sign(y2-y1)
            l = aoc.king_distance((x1, y1), (x2, y2))
            for i in range(l+1):
                positions[(x1+i*dx, y1+i*dy)] += 1
    return sum(1 for v in positions.values() if v > 1)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", solve(inp))
#     print("Part 2:", solve(inp, True))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", solve(inp))
    print("Part 2:", solve(inp, True))
