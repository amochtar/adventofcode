#!/usr/bin/env python

import aoc
from tqdm import tqdm


def solve(inp: str):
    labels = list(map(int, list(inp.strip())))
    labels += range(len(labels)+1, 1_000_000+1)

    cups = {c: i for c, i in zip(labels, labels[1:]+labels[:1])}
    num_cups = len(labels)
    current = labels[-1]

    for _ in tqdm(range(10_000_000), leave=False):
        current = cups[current]

        one = cups[current]
        two = cups[one]
        three = cups[two]

        destination = aoc.mod1(current - 1, num_cups)
        while destination in [one, two, three]:
            destination = aoc.mod1(destination - 1, num_cups)

        next = cups[three]
        cups[current] = next
        cups[three] = cups[destination]
        cups[destination] = one

    print(cups[1] * cups[cups[1]])


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
