#!/usr/bin/env python

from typing import DefaultDict
import aoc
import numpy as np


@aoc.timing
def solve(inp: str):
    def parse_fold(line: str):
        parts = line.split(' ')[-1].split('=')
        return parts[0], int(parts[1])

    parts = inp.split('\n\n')
    dots = [aoc.ints(line) for line in parts[0].splitlines()]
    max_x = max(d[0] for d in dots)
    max_y = max(d[1] for d in dots)

    paper = np.zeros((max_y+1, max_x+1), dtype=bool)
    for x, y in dots:
        paper[y][x] = True
    folds = list(map(parse_fold, parts[1].splitlines()))

    for i, (dir, f) in enumerate(folds):
        if dir == 'y':
            top = paper[:f, :]
            bottom = np.flipud(paper[f+1:, :])

            lw, rw = len(top), len(bottom)
            if lw > rw:
                bottom = np.pad(bottom, ((lw-rw, 0), (0, 0)))
            elif rw > lw:
                top = np.pad(top, ((rw-lw, 0), (0, 0)))
            paper = np.logical_or(top, bottom)
        elif dir == 'x':
            left = paper[:, :f]
            right = np.fliplr(paper[:, f+1:])

            lw, rw = len(left[0]), len(right[0])
            if lw > rw:
                right = np.pad(right, ((0, 0), (lw-rw, 0)))
            elif rw > lw:
                left = np.pad(left, ((0, 0), (rw-lw, 0)))
            paper = np.logical_or(left, right)
        if i == 0:
            print(f"Part 1: {np.sum(paper)}")

    print(f"Part 2: {i+1} folds")
    print('\n'.join(''.join(map(lambda x: '#' if x else ' ', line))
          for line in paper))


@aoc.timing
def part2(inp: str):
    return inp


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
