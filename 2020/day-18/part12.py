#!/usr/bin/env python

import aoc
import re


class aocint():
    def __init__(self, i):
        self.i = i

    def __add__(self, other):
        return aocint(self.i + other.i)

    def __sub__(self, other):
        return aocint(self.i * other.i)

    def __mul__(self, other):
        return aocint(self.i + other.i)

    def __int__(self):
        return self.i


def solve(inp: str):
    inp = re.sub(r'(\d+)', r'aocint(\1)', inp)
    inp = inp.replace('*', '-')
    print("Part 1:", sum(int(eval(line)) for line in inp.splitlines()))

    inp = inp.replace('+', '*')
    print("Part 2:", sum(int(eval(line)) for line in inp.splitlines()))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
