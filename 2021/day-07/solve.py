#!/usr/bin/env python

import aoc
import statistics
import itertools


@aoc.timing
def part1(inp):
    m = int(statistics.median(inp))
    return sum(abs(x - m) for x in inp)


@aoc.timing
def part2(inp):
    def fuel(a, b):
        return sum(i for i in range(abs(a - b)+1))

    # check for mean value and direct neighbours
    m = int(round(statistics.mean(inp), 0))
    return min(sum(fuel(x, m+dm) for x in inp) for dm in [-1, 0, 1])


# with open('test.txt', 'r') as f:
#     inp = aoc.ints(f.read())
#     print("Part 1:", part1(inp))
#     print("Part 2:", part2(inp))

with open('input.txt', 'r') as f:
    inp = aoc.ints(f.read())
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
