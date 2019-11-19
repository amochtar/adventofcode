import re
import math
import operator
from itertools import product


re_nanobot = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')


def manhattan(a, b=(0,0,0)):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])


def count_in_range(nanobots, pos):
    count = 0
    for n in nanobots:
        if manhattan(n, pos) <= n[3]:
            count += 1
    return count


def solve(input):
    nanobots = []
    for line in input:
        m = re.match(re_nanobot, line)
        x, y, z, r = m.groups()
        nanobots.append((int(x),int(y),int(z),int(r)))

    min_x, max_x = min(n[0] for n in nanobots), max(n[0] for n in nanobots)
    min_y, max_y = min(n[1] for n in nanobots), max(n[1] for n in nanobots)
    min_z, max_z = min(n[2] for n in nanobots), max(n[2] for n in nanobots)

    step = min(max_x-min_x, max_y-min_y, max_z-min_z) // 16
    while True:
        max_count = 0
        min_dist = None
        next_pos = None
        for x in range(min_x, max_x, step):
            for y in range(min_y, max_y, step):
                for z in range(min_z, max_z, step):
                    pos = (x,y,z)
                    count = count_in_range(nanobots, pos)
                    dist = manhattan(pos)
                    if min_dist == None or count > max_count or count == max_count and dist < min_dist:
                        max_count = count
                        min_dist = dist
                        next_pos = pos

        if step == 1:
            print(min_dist)
            return

        min_x, max_x = next_pos[0]-step, next_pos[0]+step
        min_y, max_y = next_pos[1]-step, next_pos[1]+step
        min_z, max_z = next_pos[2]-step, next_pos[2]+step
        step //= 2

# with open('test2.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
