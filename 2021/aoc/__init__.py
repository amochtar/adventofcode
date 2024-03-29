from functools import wraps
from time import time
from typing import Callable, List, Tuple, TypeVar, Generator
import itertools
import re

T = TypeVar('T')


def timing(f):
    "Decorator to time a function"
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.6f sec' %
              (f.__name__, te-ts))
        return result
    return wrap


def ints(text: str) -> Tuple[int, ...]:
    "Return a tuple of all ints in a string"
    return tuple(map(int, re.findall(r'-?\b\d+\b', text)))


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def sliding_window(iterable, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    iterables = itertools.tee(iterable, n)
    for i in range(1, n):
        for each in iterables[i:]:
            next(each, None)
    return zip(*iterables)


def identity(x: T) -> T:
    return x


def grid(s: str, mapper: Callable[[str], T] = identity) -> Tuple[List[List[T]], int, int]:
    "Converts a multiline string to a grid"
    grid = [[mapper(x) for x in line.strip()] for line in s.splitlines()]
    return grid, len(grid[0]), len(grid)


def walk_grid(grid: List[List[T]]) -> Generator[Tuple[Tuple[int, int], T], None, None]:
    "Walk over a grid in reading order"
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            yield (x, y), cell


def print_grid(grid: List[List[T]], mapper: Callable[[T], str] = str) -> None:
    "Print a grid"
    for row in grid:
        print(''.join(map(mapper, row)))


def manhattan(p: Tuple[int, ...], q=itertools.repeat(0)) -> Tuple[int, ...]:
    "Return the manhattan distance between 2 (multi-dimensional) points"
    return sum([abs(a-b) for a, b in zip(p, q)])


def king_distance(p: Tuple[int, ...], q=itertools.repeat(0)) -> Tuple[int, ...]:
    "Return thenNumber of chess King moves between two points"
    return max(abs(a - b) for a, b in zip(p, q))


def neighbors4(p: Tuple[int, int], min_p: Tuple[int, int] = None, max_p: Tuple[int, int] = None) -> List[Tuple[int, int]]:
    "Return the 4 neighboring cells for a given position"
    x, y = p
    min_x, min_y = min_p or (None, None)
    max_x, max_y = max_p or (None, None)

    n = []
    if min_x == None or x > min_x:
        n.append((x-1, y))
    if min_y == None or y > min_y:
        n.append((x, y-1))
    if max_y == None or y < max_y:
        n.append((x, y+1))
    if max_x == None or x < max_x:
        n.append((x+1, y))
    return n


def neighbors8(p: Tuple[int, int], min_p: Tuple[int, int] = None, max_p: Tuple[int, int] = None) -> List[Tuple[int, int]]:
    "Return the 8 neighboring cells for a given position in reading order from top left to bottom right"
    x, y = p
    min_x, min_y = min_p or (None, None)
    max_x, max_y = max_p or (None, None)

    n = []
    if min_y == None or y > min_y:
        if min_x == None or x > min_x:
            n.append((x-1, y-1))
        n.append((x, y-1))
        if max_x == None or x < max_x:
            n.append((x+1, y-1))
    if min_x == None or x > min_x:
        n.append((x-1, y))
    if max_x == None or x < max_x:
        n.append((x+1, y))
    if max_y == None or y < max_y:
        if min_x == None or x > min_x:
            n.append((x-1, y+1))
        n.append((x, y+1))
        if max_x == None or x < max_x:
            n.append((x+1, y+1))
    return n


def neighbors_cube(p: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
    "Return the 26 neighboring cells for a given position in a 3d cube"
    x, y, z = p
    n = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if (i, j, k) != (0, 0, 0):
                    n.append((x+i, y+j, z+k))
    return n


def neighbors_cube4(p: Tuple[int, int, int, int]) -> List[Tuple[int, int, int, int]]:
    "Return the 80 neighboring cells for a given position in a 4-d cube"
    x, y, z, w = p
    n = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (i, j, k, l) != (0, 0, 0, 0):
                        n.append((x+i, y+j, z+k, w+l))
    return n


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
opposite = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e',
}

facing_dir = {
    'n': (0, -1),
    's': (0, 1),
    'e': (1, 0),
    'w': (-1, 0),
}

origin = (0, 0)

hex_origin = (0, 0, 0)
hex_moves = {
    'ne': lambda p: (p[0]+1, p[1], p[2]-1),
    'nw': lambda p: (p[0], p[1]+1, p[2]-1),
    'se': lambda p: (p[0], p[1]-1, p[2]+1),
    'sw': lambda p: (p[0]-1, p[1], p[2]+1),
    'w': lambda p: (p[0]-1, p[1]+1, p[2]),
    'e': lambda p: (p[0]+1, p[1]-1, p[2]),
}


def hex_neighbors(p: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
    return [move(p) for move in hex_moves.values()]


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
    "Rotates a position 90 degrees left (counter clock-wise) relative to the given location (default origin)"
    rel_pos = sub_pos(pos, rel)
    new_pos = (rel_pos[1], -rel_pos[0])
    return add_pos(new_pos, rel)


def rot_right(pos: Tuple[int, int], rel: Tuple[int, int] = origin) -> Tuple[int, int]:
    "Rotates a position 90 degrees right (clock-wise) relative to the given location (default origin)"
    rel_pos = sub_pos(pos, rel)
    new_pos = (-rel_pos[1], rel_pos[0])
    return add_pos(new_pos, rel)


def min_max(lst: List[Tuple[int, ...]]) -> Tuple[int, ...]:
    "Returns the min and max values for every index in the given list of tuples"
    return tuple((min(e), max(e)) for e in zip(*lst))


def mod1(a: int, b: int) -> int:
    "Returns 1-based modulo"
    return 1 + (a-1) % b


def sign(x: int) -> int:
    "Returns the sign of a number"
    return -1 if x < 0 else (1 if x > 0 else 0)
