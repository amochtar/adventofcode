#!/usr/bin/env python

from collections import Counter


def valid_pass(p):
    has_double = False
    for i in range(1, len(p)):
        if p[i] < p[i-1]:
            return False

    cnt = Counter(p).most_common()
    return len([c for c in cnt if c[1] == 2]) > 0


def solve(input):
    start, end = list(map(int, input.split('-')))

    count = 0
    for i in range(start, end):
        if valid_pass(str(i)):
            count += 1

    print(count)

# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)


with open('input.txt', 'r') as f:
    input = f.read()
    solve(input)
