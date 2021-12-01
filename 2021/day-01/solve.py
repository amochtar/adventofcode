#!/usr/bin/env python

import aoc


@aoc.timing
def part1(inp: str):
    depths = aoc.ints(inp)
    return sum(1 for (a, b) in aoc.sliding_window(depths) if b > a)


@aoc.timing
def part2(inp: str):
    depths = map(sum, aoc.sliding_window(aoc.ints(inp), 3))
    return sum(1 for (a, b) in aoc.sliding_window(depths) if b > a)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", part1(inp))
#     print("Part 2:", part2(inp))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
