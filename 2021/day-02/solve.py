#!/usr/bin/env python

import aoc
import fileinput


@aoc.timing
def part1(inp: str):
    h, d = 0, 0
    for line in inp.splitlines():
        command, units = line.split(' ')
        if command == 'forward':
            h += int(units)
        elif command == 'down':
            d += int(units)
        elif command == 'up':
            d -= int(units)

    return h*d


@aoc.timing
def part2(inp: str):
    h, d, a = 0, 0, 0
    for line in inp.splitlines():
        command, units = line.split(' ')
        if command == 'forward':
            h += int(units)
            d += a*int(units)
        elif command == 'down':
            a += int(units)
        elif command == 'up':
            a -= int(units)

    return h*d


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", part1(inp))
#     print("Part 2:", part2(inp))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
