from collections import defaultdict


def power(x, y, grid_serial):
    rack_id = x + 10
    power = rack_id * y
    power += grid_serial
    power *= rack_id
    s = str(power)
    if len(s) >= 3:
        power = int(s[-3])
    else:
        power = 0
    power -= 5
    return power


def solve(grid_serial):
    grid = defaultdict(int)
    for j in range(300):
        for i in range(300):
            grid[(i,j)] = power(i,j,grid_serial)

    max_power = None
    loc = None

    for size in range(1, 300):
        for j in range(300-size):
            for i in range(300-size):
                p = 0
                for dj in range(size):
                    for di in range(size):
                        p += grid[(i+di, j+dj)]
                if max_power == None or p > max_power:
                    max_power = p
                    loc = (i, j, size)
        print(max_power, loc)


solve(5468)

# with open('input.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)
