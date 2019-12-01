#!/usr/bin/env python

def solve(input):
    sum = 0
    for line in input:
        sum += int(line) // 3 -2

    print(sum)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
