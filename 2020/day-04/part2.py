#!/usr/bin/env python

from aoc import *
import re


def solve(inp):
    inp = inp.split("\n\n")
    num_valid = 0
    for entry in inp:
        passport = parse(entry)
        # print(passport, "\n")
        if valid(passport):
            num_valid += 1

    print(num_valid)


p_re = re.compile(r'(\w{3}):([^\s]+)\s?')
hcl_re = re.compile(r'^#[0-9a-f]{6}$')
pid_re = re.compile(r'^\d{9}$')


def parse(entry):
    fields = p_re.findall(entry)
    return {f[0]: f[1] for f in fields}


def valid(passport):
    required = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"}

    if not set(passport.keys()) >= required:
        return False

    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False

    hgt = passport['hgt']
    unit = hgt[-2:]
    if not unit in {"cm", "in"}:
        return False

    hgt = int(hgt[:-2])
    if unit == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    elif unit == 'in':
        if hgt < 59 or hgt > 76:
            return False

    if not hcl_re.match(passport['hcl']):
        return False

    ecl = passport['ecl']
    if not ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False

    if not pid_re.match(passport['pid']):
        return False

    return True


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
