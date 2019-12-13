#!/usr/bin/env python

from collections import defaultdict
import intcode


moves = {
    'n': lambda p: (p[0], p[1]-1),
    's': lambda p: (p[0], p[1]+1),
    'e': lambda p: (p[0]+1, p[1]),
    'w': lambda p: (p[0]-1, p[1]),
}
left_turn = {
    'n': 'w',
    's': 'e',
    'e': 'n',
    'w': 's',
}
right_turn = {
    'n': 'e',
    's': 'w',
    'e': 's',
    'w': 'n',
}


def print_panels(panels):
    minx = min([k[0] for k in panels.keys()])
    maxx = max([k[0] for k in panels.keys()])
    miny = min([k[1] for k in panels.keys()])
    maxy = max([k[1] for k in panels.keys()])

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if panels[(x, y)] != 0:
                print('#', end='')
            else:
                print(' ', end='')
        print('')


def solve(opcodes, start_color=0):
    panels = defaultdict(int)
    pos = (0, 0)
    panels[pos] = start_color
    direction = 'n'
    robot = intcode.runner(opcodes)
    painting = True
    while True:
        try:
            out = next(robot)
            if out == 'inp':
                out = robot.send(panels[pos])
            if painting:
                panels[pos] = out
            else:
                if out == 0:
                    direction = left_turn[direction]
                elif out == 1:
                    direction = right_turn[direction]
                pos = moves[direction](pos)
            painting = not painting
        except StopIteration:
            break

    if start_color == 0:
        print(len(panels))
    else:
        print_panels(panels)


with open('input.txt', 'r') as f:
    inp = f.read().strip().split(',')
    solve(inp)
    solve(inp, 1)
