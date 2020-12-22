#!/usr/bin/env python

import aoc


def game(deck1, deck2, recurse=False):
    seen = set()
    while len(deck1) > 0 and len(deck2) > 0:
        state = (tuple(deck1), tuple(deck2))
        if state in seen:
            return deck1, []
        seen.add(state)

        c1 = deck1.pop(0)
        c2 = deck2.pop(0)

        if recurse and c1 <= len(deck1) and c2 <= len(deck2):
            d1, _ = game(deck1[:c1], deck2[:c2])
            if len(d1) > 0:
                deck1.extend([c1, c2])
            else:
                deck2.extend([c2, c1])
        else:
            if c1 > c2:
                deck1.extend([c1, c2])
            else:
                deck2.extend([c2, c1])

    return deck1, deck2


def solve(inp: str):
    deck1, deck2 = [list(aoc.ints(p.split('\n', 1)[1]))
                    for p in inp.split('\n\n')]

    d1, d2 = game(deck1[:], deck2[:])
    print(
        'Part 1:',
        max(
            sum([(i+1) * c for i, c in enumerate(d1[::-1])]),
            sum([(i+1) * c for i, c in enumerate(d2[::-1])])
        )
    )

    d1, d2 = game(deck1[:], deck2[:], True)
    print(
        'Part 2:',
        max(
            sum([(i+1) * c for i, c in enumerate(d1[::-1])]),
            sum([(i+1) * c for i, c in enumerate(d2[::-1])])
        )
    )


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
