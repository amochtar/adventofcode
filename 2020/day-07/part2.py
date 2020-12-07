#!/usr/bin/env python

from collections import defaultdict
from aoc import *
import re


bags_re = re.compile(r'(\d+) (.+?) bag')


def count_bags(contains: dict, have: str):
    cnt = 0
    for b, c in contains[have].items():
        cnt += c + c * count_bags(contains, b)
    return cnt


def solve(inp: str):
    contains = {}
    for line in inp.splitlines():
        outer, inner = line.split(" bags contain ", 2)
        contains[outer] = {bag: int(c) for c, bag in bags_re.findall(inner)}

    have = 'shiny gold'
    print(count_bags(contains, have))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
