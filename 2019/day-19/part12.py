#!/usr/bin/env python

import intcode
from itertools import product
from collections import defaultdict


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def print_beam(grid, x, y, width, height):
    for dy in range(y, y+height):
        for dx in range(x, x+width):
            if grid[(dx, dy)] == 0:
                print('.', end='')
            if grid[(dx, dy)] == 1:
                print('#', end='')
        print('')


def beam_size(beam, x, y, w, h):
    points = 0
    for x, y in product(range(x, x+w), range(y, y+h)):
        points += beam[(x, y)]
    return points


def get_beam(inp, x, y):
    runner = intcode.runner(inp)
    out = next(runner)
    assert out == 'inp'
    out = runner.send(x)
    assert out == 'inp'
    out = runner.send(y)
    assert out in [0, 1]
    return out


def solve(inp):
    inp = intcode.parse(inp)
    beam = keydefaultdict(lambda xy: get_beam(inp, xy[0], xy[1]))

    # part 1
    print_beam(beam, 0, 0, 50, 50)
    print(beam_size(beam, 0, 0, 50, 50))

    # part 2 (manual)
    # print(beam_size(beam, 667, 1097, 100, 100))

    # part 2
    x, y = 0, 10  # skip over first few rows, since they have blanks
    while True:
        if beam[(x, y)] == 1:
            if beam[(x, y+99)] == 1 and beam[(x+99, y)] == 1:
                print((x, y), x*10_000 + y)
                break
            elif beam[(x+99, y)] == 0:
                y += 1
            else:
                x += 1
        else:
            x += 1


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
