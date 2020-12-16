#!/usr/bin/env python

from collections import defaultdict
import aoc


def in_range(r, v):
    return r[0] <= v <= r[1] or r[2] <= v <= r[3]


def solve(inp: str):
    ranges, ticket, nearby = inp.split('\n\n')
    fields = {}
    for f in ranges.splitlines():
        name, vals = f.split(":")
        fields[name] = aoc.ints(vals.replace('-', ' '))

    error_rate = 0
    valid_tickets = []
    for n in nearby.splitlines()[1:]:
        valid = True
        for v in aoc.ints(n):
            if not any(in_range(r, v) for r in fields.values()):
                valid = False
                error_rate += v
                break
        if valid:
            valid_tickets.append(aoc.ints(n))

    print("Part 1:", error_rate)

    possible_idx = defaultdict(set)
    for i, vals in enumerate(zip(*valid_tickets)):
        for name, r in fields.items():
            if all(in_range(r, v) for v in vals):
                possible_idx[name].add(i)

    ticket = aoc.ints(ticket)
    departure = 1
    used_idx = set()
    for name in sorted(possible_idx, key=lambda i: len(possible_idx[i])):
        idx = (possible_idx[name]-used_idx).pop()
        used_idx.add(idx)
        if name.startswith('departure'):
            departure *= ticket[idx]

    print("Part 2:", departure)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
