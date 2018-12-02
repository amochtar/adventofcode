from collections import deque
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
State = namedtuple('State', ['steps', 'loc'])


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

    visited = set([])
    q = deque([State(steps=0, loc=Point(0, 0))])
    while q:
        s = q.popleft()
        if s.loc.x == width-1 and s.loc.y == height-1:
            print(s.steps)
            return

        if s in visited:
            continue

        visited.add(s.loc)

        tile = input[s.loc.y][s.loc.x]
        next_locs = []
        nm = exits[tile]
        # print(s, tile, nm)
        for m in nm:
            next_loc = moves[m](s.loc)
            if next_loc not in visited and valid_move(input, s.loc, m):
                q.append(State(steps=s.steps+1, loc=next_loc))


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
