import numpy as np


def neighbours(acre, y, x):
    pass


def print_land(land):
    print('\n'.join(''.join(a) for a in land))
    print()


def change(land):
    new_land = np.copy(land)

    height, width = land.shape
    for y in range(1, height-1):
        for x in range(1, width-1):
            neighbours = land[y-1:y+2,x-1:x+2]
            t = len(neighbours[neighbours=='|'])
            if land[y][x] == '|':
                t -= 1
            l = len(neighbours[neighbours=='#'])
            if land[y][x] == '#':
                l -= 1

            if land[y][x] == '.' and t >= 3:
                new_land[y][x] = '|'
            elif land[y][x] == '|' and l >= 3:
                new_land[y][x] = '#'
            elif land[y][x] == '#':
                if l >= 1 and t >= 1:
                    new_land[y][x] = '#'
                else:
                    new_land[y][x] = '.'

    return new_land


def solve(input):
    land = np.array([list(line) for line in input])
    land = np.pad(land, ((1,1),(1,1)), 'constant', constant_values=('*'))
    # print_land(land)
    for _ in range(10):
        land = change(land)
        # print_land(land)

    t = len(land[land=='|'])
    l = len(land[land=='#'])
    print(t*l)



# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
