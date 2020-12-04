#!/usr/bin/env python

from aoc import *
import re


def solve(inp):
    p_re = re.compile(r'(\w{3}):[^\s]+\s?')

    required = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"}

    inp = inp.split("\n\n")
    num_valid = 0
    for passport in inp:
        fields = set(p_re.findall(passport))
        if fields >= required:
            num_valid += 1

    print(num_valid)


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
