from collections import defaultdict
from collections import Counter


def neighbours_value(grid, pos):
    return \
        grid[pos[0]-1][pos[1]-1] \
        + grid[pos[0]-1][pos[1]] \
        + grid[pos[0]-1][pos[1]+1] \
        + grid[pos[0]][pos[1]-1] \
        + grid[pos[0]][pos[1]+1] \
        + grid[pos[0]+1][pos[1]-1] \
        + grid[pos[0]+1][pos[1]] \
        + grid[pos[0]+1][pos[1]+1]


def next_pos(pos):
    x, y, idx, ring, d = pos
    width = ring*2 + 1
    max_idx = width * width

    idx += 1
    if d == 'e':
        if idx > max_idx:
            ring += 1
            x += 1
            d = 'n'
        else:
            x += 1
    elif d == 'n':
        if y == ring:
            d = 'w'
            x -= 1
        else:
            y += 1
    elif d == 'w':
        if x == -ring:
            d = 's'
            y -= 1
        else:
            x -= 1
    elif d == 's':
        if y == -ring:
            d = 'e'
            x += 1
        else:
            y -= 1

    return (x, y, idx, ring, d)


def first_value_over(n):
    grid = defaultdict(Counter)
    grid[0][0] = 1
    pos = (0, 0, 1, 0, 'e')
    while True:
        pos = next_pos(pos)
        value = neighbours_value(grid, pos)
        grid[pos[0]][pos[1]] = value
        if value > n:
            return value


inp = 289326
print("Part 2:", first_value_over(inp))
