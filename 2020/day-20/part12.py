#!/usr/bin/env python

from typing import Dict
import aoc
import math
import numpy as np
import numpy.ma as ma
import sys


def rot_flips(data):
    rot_data = np.rot90(data)
    return [
        data,
        np.fliplr(data),
        np.flipud(data),
        np.rot90(data, 2),
        rot_data,
        np.fliplr(rot_data),
        np.flipud(rot_data),
        np.rot90(rot_data, 2),
    ]


def borders(data):
    return {
        'n': ''.join(data[0, :].tolist()),
        's': ''.join(data[-1, :].tolist()),
        'w': ''.join(data[:, 0].tolist()),
        'e': ''.join(data[:, -1].tolist()),
    }


def dfs(tiles, used: set, image: Dict):
    if len(tiles) == len(used):
        return image

    for pos, edge, border in possible_neighbors(image):
        # print(pos, edge, border)

        for id, data in tiles:
            if id not in used:
                for rot_flip in rot_flips(data):
                    if borders(rot_flip)[edge] == border:
                        u = used.copy()
                        u.add(id)
                        i = image.copy()
                        i[pos] = (id, rot_flip)
                        return dfs(tiles, u, i)


def image_neighbors(image: Dict, p):
    b = borders(image[p][1])
    ns = []
    for dir, rel_pos in aoc.facing_dir.items():
        n = aoc.add_pos(p, rel_pos)
        if n not in image:
            ns.append((n, aoc.opposite[dir], b[dir]))
    return ns


def possible_neighbors(image: Dict):
    ns = []
    for p in image:
        ns.extend(image_neighbors(image, p))
    return ns


def stitch(image):
    (min_x, max_x), (min_y, max_y) = aoc.min_max(image.keys())

    blocks = []
    for y in range(min_y, max_y+1):
        blocks_row = []
        for x in range(min_x, max_x+1):
            blocks_row.append(image[(x, y)][1][1:-1, 1:-1])
        blocks.append(blocks_row)

    return np.block(blocks)


def find_monsters(image, monster):
    monster_len = (monster == '#').sum()
    mask = (monster != '#')

    i_h, i_w = image.shape
    m_h, m_w = monster.shape
    monsters = 0
    for y in range(i_h - m_h):
        for x in range(i_w - m_w):
            sub_img = ma.masked_array(image[y:y+m_h, x:x+m_w], mask)
            if (sub_img == '#').sum() == monster_len:
                monsters += monster_len

    return monsters


def solve(inp: str):
    tiles = [(aoc.ints(lines.splitlines()[0])[0],
              np.array([list(line) for line in lines.splitlines()[1:]]))
             for lines in inp.split('\n\n')]

    used = set([tiles[0][0]])
    image = {(0, 0): tiles[0]}

    image = dfs(tiles, used, image)
    (min_x, max_x), (min_y, max_y) = aoc.min_max(image.keys())
    print(
        "Part 1:",
        image[(min_x, min_y)][0] * image[(min_x, max_y)][0] *
        image[(max_x, min_y)][0] * image[(max_x, max_y)][0]
    )

    sea = stitch(image)
    monster = np.array([list('                  # '),
                        list('#    ##    ##    ###'),
                        list(' #  #  #  #  #  #   ')])

    roughness = (sea == '#').sum()
    for rot_flip in rot_flips(sea):
        m = find_monsters(rot_flip, monster)
        roughness -= m
    print("Part 2:", roughness)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
