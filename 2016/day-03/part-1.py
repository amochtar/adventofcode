import numpy as np


def is_valid(sides):
    sides.sort()
    return sides[0] + sides[1] > sides[2]


with open("input.txt", "r") as f:
    triangles = [map(int, x.strip().split()) for x in f.readlines()]
    print 'Part 1:', len([triangle for triangle in triangles if is_valid(triangle)])

with open("input.txt", "r") as f:
    triangles = np.matrix(";".join(f.readlines())).transpose().reshape((-1, 3)).tolist()
    print 'Part 2:', len([triangle for triangle in triangles if is_valid(triangle)])
