#!/usr/bin/env python

import aoc
from collections import deque


def rot(lst, n):
    return lst[n:] + lst[:n]


def take(lst, n):
    return lst[:n], lst[n:]


def insert(lst, x, n):
    return lst[:n] + x + lst[n:]


def solve(inp: str):
    cups = list(map(int, list(inp.strip())))
    num_cups = len(cups)

    for i in range(100):
        print(f'-- move {i+1} --')
        print(f'cups: {cups}')
        # rotate current cup to the end
        cups = rot(cups, 1)

        # take 3 cups
        taken, cups = take(cups, 3)

        # select destination cup (current cup - 1)

        # if destination cup in taken, subtract 1
        # note, cups are 1-based
        destination = aoc.mod1(cups[-1]-1, num_cups)
        while destination in taken:
            destination = aoc.mod1(destination-1, num_cups)

        dst_idx = cups.index(destination)+1
        print(f'pick up: {taken}')
        print(f'destination: {destination}')

        cups = insert(cups, taken, dst_idx)
        print('')

    print(''.join(map(str, rot(cups, cups.index(1))[1:])))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
