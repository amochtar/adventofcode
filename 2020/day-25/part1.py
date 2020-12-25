#!/usr/bin/env python

import aoc
from itertools import count
from tqdm import tqdm


def solve(inp: str):
    card_pubkey, door_pubkey = list(map(int, inp.splitlines()))

    tf = 1
    card_loopsize = 0
    while tf != card_pubkey:
        tf = (tf*7) % 20201227
        card_loopsize += 1

    enc_key = 1
    for _ in tqdm(range(card_loopsize), leave=False, disable=card_loopsize < 1000):
        enc_key = enc_key * door_pubkey % 20201227
    print(enc_key)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
