#!/usr/bin/env python

import parse
from itertools import combinations


def energy(moon):
    return (abs(moon[0])+abs(moon[1])+abs(moon[2])) * (abs(moon[3])+abs(moon[4])+abs(moon[5]))


def solve(input, iterations):
    moons = []
    p = parse.compile("<x={:d}, y={:d}, z={:d}>")
    for line in input:
        x, y, z = p.parse(line)
        moons.append([x, y, z, 0, 0, 0])

    for t in range(iterations):
        for a, b in combinations(range(len(moons)), 2):
            if moons[a][0] > moons[b][0]:
                moons[a][3] -= 1
                moons[b][3] += 1
            elif moons[a][0] < moons[b][0]:
                moons[a][3] += 1
                moons[b][3] -= 1

            if moons[a][1] > moons[b][1]:
                moons[a][4] -= 1
                moons[b][4] += 1
            elif moons[a][1] < moons[b][1]:
                moons[a][4] += 1
                moons[b][4] -= 1

            if moons[a][2] > moons[b][2]:
                moons[a][5] -= 1
                moons[b][5] += 1
            elif moons[a][2] < moons[b][2]:
                moons[a][5] += 1
                moons[b][5] -= 1
        for moon in moons:
            moon[0] += moon[3]
            moon[1] += moon[4]
            moon[2] += moon[5]
    print(sum(energy(m) for m in moons))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input, 10)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input, 1000)
