import numpy as np


def hash(matrix):
    return tuple(map(tuple, matrix))


def solve(inp):
    patterns = {}
    for line in inp:
        left, right = line.split(' => ')

        left = np.array([list(row) for row in left.split('/')])
        right = np.array([list(row) for row in right.split('/')])

        for _ in range(4):
            left = np.rot90(left)
            patterns[hash(left)] = right

        left = np.fliplr(left)
        for _ in range(4):
            left = np.rot90(left)
            patterns[hash(left)] = right

    image = np.array([list(row) for row in [".#.", "..#", "###"]])

    for i in range(18):
        size = image.shape[0]
        if size % 2 == 0:
            step = 2
        else:
            step = 3

        count = size // step
        new_step = step + 1
        new_size = count * new_step
        new_image = np.empty((new_size, new_size), dtype=str)
        for x in range(count):
            for y in range(count):
                xfrom = x*step
                xto = xfrom + step
                yfrom = y*step
                yto = yfrom + step

                new_xfrom = x*new_step
                new_xto = new_xfrom + new_step
                new_yfrom = y*new_step
                new_yto = new_yfrom + new_step

                replacement = patterns[hash(image[xfrom:xto, yfrom:yto])]
                new_image[new_xfrom:new_xto, new_yfrom:new_yto] = replacement

        image = new_image

        if i == 4:
            print("Part 1:", sum(sum(image == "#")))

    print("Part 2:", sum(sum(image == "#")))


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
