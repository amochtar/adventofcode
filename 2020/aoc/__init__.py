import itertools
import re
import math


def ints(text):
    "Return a tuple of all ints in a string"
    return tuple(map(int, re.findall(r'-?\b\d+\b', text)))


def lcm(a, b):
    "Return the least common multiple of a and b"
    return abs(a*b) // math.gcd(a, b)


def manhattan(p, q=itertools.repeat(0)):
    "Return the manhattan distance between 2 (multi-dimensional) points"
    return sum([abs(a-b) for a, b in zip(p, q)])


def king_distance(p, q=itertools.repeat(0)):
    "Number of chess King moves between two points."
    return max(abs(a - b) for a, b in zip(p, q))


def neighbors4(p):
    "Return the 4 neighboring cells"
    x, y = p
    return [
        (x, y-1),
        (x, y+1),
        (x-1, y),
        (x+1, y)
    ]


def neighbors8(p):
    "Return the 4 neighboring cells"
    x, y = p
    return [
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),
        (x-1, y),
        (x+1, y),
        (x-1, y+1),
        (x, y+1),
        (x+1, y+1)
    ]


moves = {
    'n': lambda p: (p[0], p[1]-1),
    's': lambda p: (p[0], p[1]+1),
    'e': lambda p: (p[0]+1, p[1]),
    'w': lambda p: (p[0]-1, p[1]),
}
left_turn = {
    'n': 'w',
    's': 'e',
    'e': 'n',
    'w': 's',
}
right_turn = {
    'n': 'e',
    's': 'w',
    'e': 's',
    'w': 'n',
}
