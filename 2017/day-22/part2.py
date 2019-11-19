from collections import defaultdict
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

moves = {
    'n': lambda p: Point(p.x, p.y-1),
    's': lambda p: Point(p.x, p.y+1),
    'e': lambda p: Point(p.x+1, p.y),
    'w': lambda p: Point(p.x-1, p.y),
}
left_turn = {
    'n': 'w',
    's': 'e',
    'e': 'n',
    'w': 's',
}
right_turn = {
    'n': 'e',
    's': 'w',
    'e': 's',
    'w': 'n',
}
reverse = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e',
}


def solve(inp):
    nodes = defaultdict(lambda: '.')
    for y, line in enumerate(inp):
        for x, node in enumerate(line):
            nodes[Point(x, y)] = node

    start = len(inp) // 2
    pos = Point(start, start)
    direction = 'n'
    count = 0
    for i in range(10000000):
        if nodes[pos] == '#':
            nodes[pos] = 'F'
            direction = right_turn[direction]
        elif nodes[pos] == 'W':
            count += 1
            nodes[pos] = '#'
        elif nodes[pos] == 'F':
            nodes[pos] = '.'
            direction = reverse[direction]
        elif nodes[pos] == '.':
            nodes[pos] = 'W'
            direction = left_turn[direction]
        new_pos = moves[direction](pos)
        pos = new_pos

    print('Part 2:', count)


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
