#!/usr/bin/env python

import intcode


def solve(input):
    runner = intcode.runner(input)
    img = [chr(i) for i in runner]
    img = ''.join(img)
    print(img)
    img = img.strip().split('\n')

    height = len(img)
    width = len(img[0])
    alignment = 0
    for y, line in enumerate(img):
        for x, c in enumerate(line):
            if 0 < y < height-2 and 0 < x < width-2:
                if img[y][x] == '#' and \
                        img[y-1][x] == '#' and \
                        img[y+1][x] == '#' and \
                        img[y][x-1] == '#' and \
                        img[y][x+1] == '#':
                    alignment += x*y
    print(alignment)


with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]
    solve(input)
