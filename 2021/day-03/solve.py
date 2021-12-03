#!/usr/bin/env python

import aoc
from itertools import count


@aoc.timing
def part1(inp: str):
    lines = inp.splitlines()
    l = len(lines)

    gamma, epsilon = "", ""
    for bits in zip(*lines):
        if bits.count("1") > l // 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


@ aoc.timing
def part2(inp: str):
    def rate(lines, bit):
        bits = list(map(lambda x: x[bit], lines))
        l = len(lines)
        if bits.count("0") > l // 2:
            return "0"
        else:
            return "1"

    lines = inp.splitlines()
    ox_lines = lines[:]
    for i in count():
        rating = rate(ox_lines, i)
        new_lines = []
        for line in ox_lines:
            if line[i] == rating:
                new_lines.append(line)
        ox_lines = new_lines

        if len(ox_lines) == 1:
            break

    co_lines = lines[:]
    for i in count():
        rating = rate(co_lines, i)
        new_lines = []
        for line in co_lines:
            if line[i] != rating:
                new_lines.append(line)
        co_lines = new_lines

        if len(co_lines) == 1:
            break

    return int(ox_lines[0], 2) * int(co_lines[0], 2)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", part1(inp))
#     print("Part 2:", part2(inp))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
