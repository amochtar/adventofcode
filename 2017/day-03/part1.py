from math import sqrt
from math import ceil


def nearest_odd_sqrt(n):
    root = int(ceil(sqrt(n)))
    if root % 2 == 0:
        root += 1
    return root, root*root


def manhattan_distance(n):
    # Bottom right corner is sequence of squares of odd numbers:
    # 1, 9, 25, 49, 81, etc. So find nearest odd sqrt higher than
    # our input, and start counting from there.
    width, square = nearest_odd_sqrt(n)
    if n == square:
        return width-1

    steps_to_edge = (width-1)//2

    # Remaining steps depend on width of the square and position
    # of the number on the edge
    remaining_steps = 1 + (n - 1) % (width - 1)
    remaining_steps -= (width//2 + 1)

    return steps_to_edge + abs(remaining_steps)


inp = 289326
print("Part 1:", manhattan_distance(inp))
