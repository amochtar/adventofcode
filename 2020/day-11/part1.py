#!/usr/bin/env python

from aoc import *
import numpy as np


def occupied_seats(seats, x, y):
    occ = 0
    for p, q in neighbors8((x, y)):
        if seats[q][p] == '#':
            occ += 1
    return occ


def change(seats):
    new_seats = np.copy(seats)

    height, width = seats.shape
    for y in range(1, height-1):
        for x in range(1, width-1):
            occupied = occupied_seats(seats, x, y)
            if seats[y][x] == 'L' and occupied == 0:
                new_seats[y][x] = '#'
            elif seats[y][x] == '#' and occupied >= 4:
                new_seats[y][x] = 'L'

    return new_seats


def solve(inp: str):
    seats = np.array([list(line) for line in inp.splitlines()])
    # pad seats to make edge detection easier
    seats = np.pad(seats, ((1, 1), (1, 1)), constant_values=('*'))

    while True:
        new_seats = change(seats)
        if np.array_equal(seats, new_seats):
            break
        seats = new_seats

    print(np.sum(seats == '#'))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
