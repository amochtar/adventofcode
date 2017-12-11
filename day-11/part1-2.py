def distance(x, y, z):
    return (abs(x) + abs(y) + abs(z)) // 2


def solve(steps):
    x, y, z = 0, 0, 0
    maxdist = 0

    for step in steps:
        if step == 'n':
            y += 1
            z -= 1
        elif step == 'ne':
            x += 1
            z -= 1
        elif step == 'nw':
            x -= 1
            y += 1
        elif step == 's':
            y -= 1
            z += 1
        elif step == 'se':
            x += 1
            y -= 1
        elif step == 'sw':
            x -= 1
            z += 1
        maxdist = max(maxdist, distance(x, y, z))
    dist = distance(x, y, z)
    print("Part 1:", dist)
    print("Part 2:", maxdist)


with open('input.txt', 'r') as f:
    steps = f.read().split(',')
    solve(steps)
