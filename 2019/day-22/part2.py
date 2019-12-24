#!/usr/bin/env python


def rev(size, a, b):
    return (-a % size, (-b - 1) % size)


def cut(size, a, b, n):
    return (a, (b + n) % size)


def incr(size, a, b, n):
    inv = pow(n, size-2, size)
    return ((a * inv) % size, (b * inv) % size)


def shuffle(steps, cards, a, b):
    for techn in steps[::-1]:
        if techn[1] == 'into':
            a, b = rev(cards, a, b)
        if techn[0] == 'cut':
            a, b = cut(cards, a, b, int(techn[-1]))
        if techn[1] == 'with':
            a, b = incr(cards, a, b, int(techn[-1]))
    return a, b


def solve(inp):
    steps = [line.split(' ') for line in inp.strip().splitlines()]
    size = 119315717514047
    shuffles = 101741582076661
    pos = 2020

    # calculate 1 shuffle
    a, b = shuffle(steps, size, 1, 0)

    # expand to all shuffles
    factor = pow(a, shuffles, size)
    print((factor * pos + b * (factor-1) * pow(a-1, size-2, size)) % size)


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
