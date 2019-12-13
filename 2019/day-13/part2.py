#!/usr/bin/env python

from collections import defaultdict
import intcode


def solve(opcodes):
    opcodes[0] = 2
    run = intcode.runner(opcodes)
    score = 0
    ball, paddle = 0, 0
    try:
        while True:
            x = next(run)
            while x == 'inp':
                joystick = 1 if ball > paddle else -1 if ball < paddle else 0
                x = run.send(joystick)
            y = next(run)
            id = next(run)
            if x == -1 and y == 0:
                score = id
            else:
                if id == 3:
                    paddle = x
                elif id == 4:
                    ball = x

    except StopIteration:
        pass

    print(score)


with open('input.txt', 'r') as f:
    inp = f.read().strip().split(',')
    solve(inp)
