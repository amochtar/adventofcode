#!/usr/bin/env python

import aoc
import re
from tqdm import tqdm


def solve(inp: str):
    steps_re = re.compile(r'ne|nw|se|sw|e|w')
    instructions = [steps_re.findall(line) for line in inp.splitlines()]

    tiles = {}
    for i in instructions:
        pos = aoc.hex_origin
        for step in i:
            pos = aoc.hex_moves[step](pos)

        tiles[pos] = not tiles[pos] if pos in tiles else True

    print('Part 1:', sum(tiles.values()))

    for _ in tqdm(range(100), leave=False, desc='Part 2'):
        new_tiles = {}
        for tile in tiles.keys():
            for t in aoc.hex_neighbors(tile):
                if t in new_tiles:
                    continue
                black_neighbors = sum(
                    tiles[n] for n in aoc.hex_neighbors(t) if n in tiles)

                new_tiles[t] = tiles[t] if t in tiles else False
                if new_tiles[t] and (black_neighbors == 0 or black_neighbors > 2):
                    new_tiles[t] = False
                elif not new_tiles[t] and black_neighbors == 2:
                    new_tiles[t] = True
        tiles = new_tiles

    print('Part 2:', sum(tiles.values()))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
