import re

re_point = re.compile(r'position=< *(-?\d+),( *-?\d+)> velocity=< *(-?\d+),( *-?\d+)>')


def solve(input):
    points = []
    for line in input:
        x, y, dx, dy = re.match(re_point, line).groups()
        points.append((int(x), int(y), int(dx), int(dy)))

    i = 0
    a = area(points)
    while True:
        new_points = [(p[0]+p[2], p[1]+p[3], p[2], p[3]) for p in points]
        new_a = area(new_points)
        if new_a < a:
            a = new_a
            points = new_points
        else:
            break
        i += 1

    print_points(points)
    print(i)


def area(points):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    area = (max_x - min_x) * (max_y - min_y)
    return area


def print_points(points):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    locs = [(p[0], p[1]) for p in points]

    for j in range(min_y, max_y+1):
        for i in range(min_x, max_x+1):
            if (i,j) in locs:
                print('#', end='')
            else:
                print('.', end='')
        print('')


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
