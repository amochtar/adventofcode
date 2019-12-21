#!/usr/bin/env python

import intcode


def spring(inp, script):
    inp = intcode.parse(inp)
    runner = intcode.runner(inp)

    script = [ord(c) for c in script]

    i = 0
    try:
        while True:
            out = next(runner)
            while out == 'inp':
                out = runner.send(script[i])
                i += 1
            # else:
            #     print(chr(out), end='')
    except StopIteration:
        print(out)


def solve(inp):
    # Jump is D is land, and A or B or C isn't
    script1 = '''NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
'''
    spring(inp, script1)

    # Jump is D is ground, AND A or B or C isn't
    # AND if E is ground, OR H is ground
    script2 = '''NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
'''
    spring(inp, script2)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
