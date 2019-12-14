#!/usr/bin/env python

from collections import defaultdict
from math import ceil


def solve(input):
    def element(s):
        n, el = s.split()
        return (el, int(n))

    def nxt(needs):
        for el, n in needs.items():
            if el != 'ORE' and n > 0:
                return (el, n)

    def ore_needed(f):
        needs = defaultdict(int)
        needs['FUEL'] = f
        while next_el := nxt(needs):
            el, need = next_el
            produces, ins = reactions[el]

            factor = ceil(need/produces)
            needs[el] -= factor*produces
            for (in_el, in_need) in ins:
                requires = factor*in_need
                needs[in_el] += requires
        return needs['ORE']

    reactions = {}
    for line in input:
        ins, out = line.split(' => ')
        el, produces = element(out)
        reactions[el] = (produces, [element(i) for i in ins.split(', ')])

    ore_1fuel = ore_needed(1)
    print(ore_1fuel)

    max_ore = 1000000000000
    low = max_ore // ore_1fuel
    high = low * 2
    max_fuel = 0
    while low < high:
        fuel = (low+high+1)//2
        ore = ore_needed(fuel)
        if ore <= max_ore:
            max_fuel = max(fuel, max_fuel)
            low = fuel
        else:
            high = fuel-1
    print(max_fuel)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
