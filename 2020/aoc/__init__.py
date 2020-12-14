import itertools
import re
import math
from typing import List, Tuple


def ints(text: str) -> Tuple[int, ...]:
    "Return a tuple of all ints in a string"
    return tuple(map(int, re.findall(r'-?\b\d+\b', text)))


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def manhattan(p: Tuple[int, ...], q=itertools.repeat(0)) -> Tuple[int, ...]:
    "Return the manhattan distance between 2 (multi-dimensional) points"
    return sum([abs(a-b) for a, b in zip(p, q)])


def king_distance(p: Tuple[int, ...], q=itertools.repeat(0)) -> Tuple[int, ...]:
    "Return thenNumber of chess King moves between two points"
    return max(abs(a - b) for a, b in zip(p, q))


def neighbors4(p: Tuple[int, int]) -> List[Tuple[int, int]]:
    "Return the 4 neighboring cells for a given position"
    x, y = p
    return [
        (x, y-1),
        (x, y+1),
        (x-1, y),
        (x+1, y)
    ]


def neighbors8(p: Tuple[int, int]) -> List[Tuple[int, int]]:
    "Return the 8 neighboring cells for a given position"
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

facing_dir = {
    'n': (0, -1),
    's': (0, 1),
    'e': (1, 0),
    'w': (-1, 0),
}

origin = (0, 0)


def add_pos(a: Tuple[int, int], b: Tuple[int, int], factor: int = 1) -> Tuple[int, int]:
    "Adds two position tuples"
    return (a[0]+b[0]*factor, a[1]+b[1]*factor)


def sub_pos(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    "Subtracts the position tuple b from a"
    return (a[0]-b[0], a[1]-b[1])


def mult_pos(a: Tuple[int, int], factor: int) -> Tuple[int, int]:
    "Multiplies a position tuple with a given factor"
    return (a[0]*factor, a[1]*factor)


def rot_left(pos: Tuple[int, int], rel: Tuple[int, int] = origin) -> Tuple[int, int]:
    rel_pos = sub_pos(pos, rel)
    new_pos = (rel_pos[1], -rel_pos[0])
    return add_pos(new_pos, rel)


def rot_right(pos: Tuple[int, int], rel: Tuple[int, int] = origin) -> Tuple[int, int]:
    rel_pos = sub_pos(pos, rel)
    new_pos = (-rel_pos[1], rel_pos[0])
    return add_pos(new_pos, rel)
