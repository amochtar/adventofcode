#!/usr/bin/env python

import intcode


def solve(input):
    input[0] = 2
    runner = intcode.runner(input)

    inp = 'A,B,A,B,C,C,B,A,B,C\nL,8,R,12,R,12,R,10\nR,10,R,12,R,10\nL,10,R,10,L,6\nn\n'
    i = 0
    dust = None
    try:
        while True:
            out = next(runner)
            while out == 'inp':
                out = runner.send(ord(inp[i]))
                i += 1
            else:
                dust = out
    except StopIteration:
        print(dust)


with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]
    solve(input)
