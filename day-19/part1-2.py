from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])

moves = {
    'n': lambda p: Point(p.x-1, p.y),
    's': lambda p: Point(p.x+1, p.y),
    'e': lambda p: Point(p.x, p.y+1),
    'w': lambda p: Point(p.x, p.y-1),
}

turns = {
    'n': ['n', 'e', 'w'],
    's': ['s', 'e', 'w'],
    'e': ['e', 'n', 's'],
    'w': ['w', 'n', 's'],
}


def next_pos(lines, pos, direction):
    directions = turns[direction]
    for d in directions:
        nxt = moves[d](pos)
        if lines[nxt.x][nxt.y] != ' ':
            return (nxt, d)
    return (None, direction)


def solve(lines):
    pos = Point(0, lines[0].index('|'))
    direction = 's'
    seen = []
    count = 0
    while True:
        count += 1
        pos, direction = next_pos(lines, pos, direction)
        if not pos:
            break
        if lines[pos.x][pos.y] not in ' -|+':
            seen.append(lines[pos.x][pos.y])

    print("Part 1:", ''.join(seen))
    print("Part 2:", count)


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
