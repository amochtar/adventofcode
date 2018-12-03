from collections import defaultdict
import re


def parse(claim):
    r = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    c = re.match(r, claim)
    (id, x, y, w, h) = c.groups()
    return (id, int(x), int(y), int(w), int(h))


def solve(input):
    claims = list(map(parse, input))

    fabric = defaultdict(int)
    for (_, x ,y, w, h) in claims:
        for i in range(w):
            for j in range(h):
                fabric[(x+i,y+j)] += 1

    for (id, x ,y, w, h) in claims:
        overlaps = False
        for i in range(w):
            for j in range(h):
                if fabric[(x+i,y+j)] != 1:
                    overlaps = True
                    break
            if overlaps:
                break
        if not overlaps:
            print(id)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
