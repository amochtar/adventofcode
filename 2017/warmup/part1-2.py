from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
markers = {'A': set(), 'B': set()}
moves = {
    'Up': lambda p: Point(p.x, p.y+1),
    'Down': lambda p: Point(p.x, p.y-1),
    'Right': lambda p: Point(p.x+1, p.y),
    'Left': lambda p: Point(p.x-1, p.y),
    'A': lambda p: set_marker(markers, 'A', p),
    'B': lambda p: set_marker(markers, 'B', p),
    'Start': lambda p: p,
}


def set_marker(markers, m, p):
    markers[m].add(p)
    return p


def distance(a, b=Point(0, 0)):
    return abs(a.x-b.x) + abs(a.y-b.y)


def solve(steps):
    pos = Point(0, 0)
    for step in steps:
        pos = moves[step](pos)

    max_marker_dist = max(distance(p) for points in markers.values() for p in points)
    print("Part 1:", max_marker_dist)

    max_pair_dist = max(distance(a, b) for a in markers['A'] for b in markers['B'])
    print("Part 2:", max_pair_dist)


with open('input.txt', 'r') as f:
    steps = f.read().split(', ')
    solve(steps)
