#!/usr/bin/env python

import json
from heapq import heappop, heappush


def next_jumps(pos, flats):
    jumps = []
    x, y = pos
    for jump_x in range(0, 5):
        new_x = x + 1 + jump_x
        try:
            flat = flats[new_x]
            jump_y = max(0, flat - y)
            if jump_x + jump_y <= 4:
                jumps.append(
                    (jump_x+jump_y, [jump_x, jump_y], [new_x, flat]))
        except KeyError:
            continue

    return jumps


def solve(input):
    data = json.loads(input)
    flats = {k: v for [k, v] in data['flats']}

    pos = data['flats'][0]

    q = []
    moves = next_jumps(pos, flats)
    for m in moves:
        heappush(q, m)

    while q:
        cost, jump, flat = heappop(q)
        if flat == data["flats"][-1]:
            print(cost)
            return

        moves = next_jumps(flat, flats)
        for (c, j, f) in moves:
            heappush(q, (cost+c, j, f))


with open('test.txt', 'r') as f:
    input = f.read()
    solve(input)

with open('input.txt', 'r') as f:
    input = f.read()
    solve(input)
