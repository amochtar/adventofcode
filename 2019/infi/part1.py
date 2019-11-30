#!/usr/bin/env python

import json


def solve(input):
    data = json.loads(input)
    flats = { k: v for [k,v] in data['flats']}
    jumps = data['sprongen']
    pos = data['flats'][0]

    num_jumps = 0
    for [i,j] in jumps:
        num_jumps += 1
        print(pos, [i,j])
        new_pos = [pos[0]+i+1, pos[1]+j]

        try:
            flat = flats[new_pos[0]]
            if flat > new_pos[1]:
                print("Flat is too high at jump", num_jumps)
                return
            pos = [new_pos[0], flat]
            print("Jump", num_jumps, "to flat", pos)
        except KeyError:
            print("No flat at jump", num_jumps)
            return


with open('test.txt', 'r') as f:
    input = f.read()
    solve(input)

with open('input.txt', 'r') as f:
    input = f.read()
    solve(input)
