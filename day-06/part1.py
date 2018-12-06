from collections import defaultdict
from collections import Counter

def solve(input):
    points = [tuple(map(int, line.split(', '))) for line in input]

    min_x = min(map(lambda p: p[0], points))
    max_x = max(map(lambda p: p[0], points))
    min_y = min(map(lambda p: p[1], points))
    max_y = max(map(lambda p: p[1], points))

    grid = defaultdict(int)
    for j in range(0, max_y+2):
        for i in range(0, max_x+2):
            grid[(i,j)] = closest(points, (i,j))

    infinite = set([i for p, i in grid.items() if p[0] == 0 or p[1] == 0 or p[0] == max_x or p[1] == max_y])
    print(Counter([i for i in grid.values() if i not in infinite]))


def closest(points, a):
    x = None
    cl = []
    for i, p in enumerate(points):
        d = distance(p, a)
        if x == None or d < x:
            x = d
            cl = [i]
        elif d == x:
            cl.append(i)
    if len(cl) == 1:
        return cl[0]
    return None


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
