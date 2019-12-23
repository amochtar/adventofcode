#!/usr/bin/env python


def rev(stack):
    return stack[::-1]


def cut(stack, n):
    return stack[n:] + stack[:n]


def incr(stack, n):
    size = len(stack)
    new_stack = [-1] * size
    i = 0
    for a in range(size):
        new_stack[i % size] = stack[a]
        i += n
    return new_stack


def solve(inp, size):
    steps = [line.split(' ') for line in inp.strip().splitlines()]
    stack = list(range(size))

    for techn in steps:
        if techn[1] == 'into':
            stack = rev(stack)
        if techn[0] == 'cut':
            stack = cut(stack, int(techn[1]))
        if techn[1] == 'with':
            stack = incr(stack, int(techn[-1]))
    return stack


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print(solve(inp, 10))

with open('input.txt', 'r') as f:
    inp = f.read()
    print(solve(inp, 10007).index(2019))
