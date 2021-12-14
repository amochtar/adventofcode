#!/usr/bin/env python

from collections import Counter
import aoc


@aoc.timing
def part1(inp):
    polymer = inp[0]
    instructions = {a: b for a, b in (line.split(' -> ') for line in inp[2:])}

    for i in range(10):
        new_polymer = polymer[0]
        for a, b in aoc.sliding_window(polymer):
            if a+b in instructions:
                new_polymer += instructions[a+b] + b
            else:
                new_polymer += b
        polymer = new_polymer

    cnt = Counter(polymer).most_common()
    return cnt[0][1] - cnt[-1][1]


@aoc.timing
def part2(inp):
    polymer = inp[0]
    instructions = {a: b for a, b in (line.split(' -> ') for line in inp[2:])}

    pairs_cnt = Counter(a+b for a, b in aoc.sliding_window(polymer))
    polymer_cnt = Counter(polymer)

    for _ in range(40):
        new_pairs_cnt = Counter()
        for pair, c in pairs_cnt.items():
            if pair in instructions:
                insert = instructions[pair]
                new_pairs_cnt[pair[0]+insert] += c
                new_pairs_cnt[insert+pair[1]] += c
                polymer_cnt[insert] += c
            pairs_cnt = new_pairs_cnt

    cnt = polymer_cnt.most_common()
    return cnt[0][1] - cnt[-1][1]


# with open('test.txt', 'r') as f:
#     inp = f.read().splitlines()
#     print("Part 1:", part1(inp))
#     print("Part 2:", part2(inp))

with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
