from heapq import heappop, heappush
from collections import deque
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

moves = {
    'n': lambda p: Point(p.x, p.y-1),
    's': lambda p: Point(p.x, p.y+1),
    'w': lambda p: Point(p.x-1, p.y),
    'e': lambda p: Point(p.x+1, p.y),
}

opposite = { 'n': 's', 's': 'n', 'w': 'e', 'e': 'w' }

exits = {
    "║": ["n", "s"],
    "╔": ["e", "s"],
    "╗": ["w", "s"],
    "╠": ["n", "s", "e"],
    "╦": ["s", "w", "e"],
    "╚": ["n", "e"],
    "╝": ["n", "w"],
    "╬": ["n", "s", "w", "e"],
    "╩": ["n", "w", "e"],
    "═": ["w", "e"],
    "╣": ["n", "s", "w"],
}


def distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def valid_loc(input, loc):
    if loc.x < 0 or loc.x >= len(input[0]):
        return False
    if loc.y < 0 or loc.y >= len(input):
        return False
    return True


def valid_move(input, loc, m):
    om = opposite[m]
    next_loc = moves[m](loc)
    try:
        if valid_loc(input, next_loc):
            tile = input[loc.y][loc.x]
            next_tile = input[next_loc.y][next_loc.x]
            if om in exits[next_tile]:
                return True
    except:
        return False


def solve(input):
    width = len(input[0])
    height = len(input)

    loc = Point(0,0)
    dest = Point(width-1, height-1)

    visited = {}
    q = [(0 + distance(loc, dest), 0, loc)]
    while q:
        _, steps, loc = heappop(q)
        if loc.x == dest.x and loc.y == dest.y:
            print(steps, len(visited))
            return

        if loc in visited:
            continue

        visited[loc] = steps

        tile = input[loc.y][loc.x]
        nm = exits[tile]
        for m in nm:
            next_loc = moves[m](loc)
            if next_loc not in visited and valid_move(input, loc, m):
                cost = steps+1+distance(next_loc, dest)
                heappush(q, (cost, steps+1, next_loc))


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
