#!/usr/bin/env python

from aoc import *


def solve(inp: str):
    groups = inp.split("\n\n")

    anyone = 0
    everyone = 0

    for group in groups:
        persons = group.splitlines()

        anyone += len(set().union(*persons))
        everyone += len(set(persons[0]).intersection(*persons))

    print("Part 1:", anyone)
    print("Part 2:", everyone)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
