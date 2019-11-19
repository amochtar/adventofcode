import re
import math

re_nanobot = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')


def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])


def solve(input):
    nanobots = []
    for line in input:
        m = re.match(re_nanobot, line)
        x, y, z, r = m.groups()
        nanobots.append((int(x),int(y),int(z),int(r)))

    nanobot = sorted(nanobots, key=lambda n: n[3])[-1]
    count = 0
    for n in nanobots:
        # print(manhattan(n, nanobot))
        if manhattan(n, nanobot) <= nanobot[3]:
            count += 1

    print(count)

# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
