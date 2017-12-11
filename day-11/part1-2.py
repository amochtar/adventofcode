from collections import namedtuple

Hexpoint = namedtuple('Hexpoint', ['x', 'y', 'z'])
moves = {
    'n': lambda p: Hexpoint(p.x, p.y+1, p.z-1),
    's': lambda p: Hexpoint(p.x, p.y-1, p.z+1),
    'ne': lambda p: Hexpoint(p.x+1, p.y, p.z-1),
    'sw': lambda p: Hexpoint(p.x-1, p.y, p.z+1),
    'nw': lambda p: Hexpoint(p.x-1, p.y+1, p.z),
    'se': lambda p: Hexpoint(p.x+1, p.y-1, p.z),
}


def distance(a, b=Hexpoint(0, 0, 0)):
    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) // 2


def solve(steps):
    pos = Hexpoint(0, 0, 0)
    maxdist = 0

    for step in steps:
        pos = moves[step](pos)
        dist = distance(pos)
        maxdist = max(maxdist, dist)

    print("Part 1:", dist)
    print("Part 2:", maxdist)


with open('input.txt', 'r') as f:
    steps = f.read().split(',')
    solve(steps)
