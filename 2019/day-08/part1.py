#!/usr/bin/env python

from collections import Counter


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def solve(input, width, height):
    layers = chunkstring(input.strip(), width*height)

    min_zeros = width*height
    mul12 = 0
    for layer in layers:
        cnt = Counter(layer)
        if cnt['0'] < min_zeros:
            min_zeros = cnt['0']
            mul12 = cnt['1'] * cnt['2']
    print(mul12)


# with open('test.txt', 'r') as f:
#     input = f.read()
#     solve(input, 2, 2)

with open('input.txt', 'r') as f:
    input = f.read()
    solve(input, 25, 6)
