#!/usr/bin/env python

from collections import defaultdict
from aoc import *
import re


bags_re = re.compile(r'(\d+) (.+?) bag')


def get_containers(containers: dict, want: str):
    bags = set(containers[want])
    for b in containers[want]:
        bags.update(get_containers(containers, b))
    return bags


def solve(inp: str):
    containers = defaultdict(list)
    for line in inp.splitlines():
        outer, inner = line.split(" bags contain ", 2)
        for _, bag in bags_re.findall(inner):
            containers[bag].append(outer)

    want = 'shiny gold'
    print(len(get_containers(containers, want)))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
