#!/usr/bin/env python

from typing import List
import aoc
from collections import defaultdict


@aoc.timing
def solve(inp: str, part2=False):
    def find_path(current: str, path: List[str] = []):
        if current == 'end':
            yield path
            return

        for nxt in caves[current]:
            if nxt == 'start':
                continue
            if nxt.islower() and nxt in path:
                if not part2:
                    continue
                elif any(path.count(c) > 1 for c in path if c.islower()):
                    continue

            yield from find_path(nxt, path + [nxt])

    caves = defaultdict(list)
    for line in inp.splitlines():
        parts = line.split('-')
        caves[parts[0]].append(parts[1])
        caves[parts[1]].append(parts[0])

    return len(list(find_path('start')))


@aoc.timing
def part2(inp: str):
    return inp


with open('test2.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", solve(inp))
    print("Part 2:", solve(inp, True))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", solve(inp))
    print("Part 2:", solve(inp, True))
