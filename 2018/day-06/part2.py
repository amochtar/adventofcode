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
            d = 0
            for p in points:
                d += distance(p, (i,j))
            grid[(i,j)] = d

    print(len([p for p, i in grid.items() if i < 10000]))

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
