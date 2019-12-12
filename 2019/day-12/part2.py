#!/usr/bin/env python

import parse
from itertools import combinations
import math
from copy import deepcopy


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def solve(input, iterations):
    moons = []
    p = parse.compile("<x={:d}, y={:d}, z={:d}>")
    for line in input:
        x, y, z = p.parse(line)
        moons.append([x, y, z, 0, 0, 0])

    orig_moons = deepcopy(moons)

    repeat = [0, 0, 0]
    for i in range(3):
        iterations = 0
        while True:
            iterations += 1
            for a, b in combinations(range(len(moons)), 2):
                if moons[a][0+i] > moons[b][0+i]:
                    moons[a][3+i] -= 1
                    moons[b][3+i] += 1
                elif moons[a][0+i] < moons[b][0+i]:
                    moons[a][3+i] += 1
                    moons[b][3+i] -= 1
            for moon in moons:
                moon[0+i] += moon[3+i]
            if moons == orig_moons:
                repeat[i] = iterations
                break

    print(lcm(lcm(repeat[0], repeat[1]), repeat[2]))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input, 10)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input, 1000)
