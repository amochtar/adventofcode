#!/usr/bin/env python

from collections import deque
from itertools import count
import aoc


@aoc.timing
def solve(inp: str):
    grid, w, h = aoc.grid(inp, int)

    flash_count = 0
    for i in count(1):
        flashed = set()
        to_flash = set()

        # increase energy level
        for (x, y), _ in aoc.walk_grid(grid):
            grid[y][x] += 1
            if grid[y][x] > 9:
                to_flash.add((x, y))

        # flash octopi
        while to_flash:
            new_to_flash = set()
            for x, y in to_flash-flashed:
                for p, q in aoc.neighbors8((x, y), (0, 0), (w-1, h-1)):
                    grid[q][p] += 1
                    if grid[q][p] > 9 and (p, q) not in flashed:
                        new_to_flash.add((p, q))
                flashed.add((x, y))
            to_flash = new_to_flash

        # reset energy levels
        for (x, y), _ in aoc.walk_grid(grid):
            if grid[y][x] > 9:
                grid[y][x] = 0

        flash_count += len(flashed)
        if i == 100:
            print(f"Part 1: {flash_count}")

        if len(flashed) == 100:
            print(f"Part 2: {i}")
            return


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
