#!/usr/bin/env python

import aoc
from collections import Counter


def solve(inp: str):
    ingredients = Counter()
    allergens = {}
    for line in inp.splitlines():
        ingredients_str, allergens_str = line[:-1].split(' (contains ')
        ingrs = set(ingredients_str.split(' '))
        ingredients.update(ingrs)
        for a in allergens_str.split(', '):
            if a not in allergens:
                allergens[a] = ingrs
            else:
                allergens[a] = allergens[a].intersection(ingrs)

    ingr_without_allergens = ingredients.keys() - set(
        [i for ingrs in allergens.values() for i in ingrs])
    print('Part 1:', sum([ingredients[i]
                          for i in ingr_without_allergens]))

    used = set([])
    while len(used) < len(allergens):
        for a, ingrs in allergens.items():
            if len(ingrs) > 1:
                allergens[a] -= used
            else:
                used.update(ingrs)

    print('Part 2:', ','.join([allergens[a].pop()
                               for a in sorted(allergens.keys())]))


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
