from collections import defaultdict


class Region(object):
    def __init__(self, y, x, gi, el, t):
        self.y = y
        self.x = x
        self.gi = gi
        self.el = el
        self.t = t

    def pos(self):
        return (self.y, self.x)


def solve(depth, target):
    cave = defaultdict(Region)
    for y in range(target[0]+1):
        for x in range(target[1]+1):
            pos = (y,x)
            if pos == (0,0) or pos == target:
                gi = 0
            elif y == 0:
                gi = x * 16807
            elif x == 0:
                gi = y * 48271
            else:
                gi = cave[(y,x-1)].el * cave[(y-1,x)].el

            el = (gi + depth) % 20183

            if el % 3 == 0:
                t = '.'
            elif el % 3 == 1:
                t = '='
            else:
                t = '|'
            cave[(y,x)] = Region(y, x, gi, el, t)

    rl = 0
    for y in range(target[0]+1):
        for x in range(target[1]+1):
            if cave[(y,x)].t == '=':
                rl += 1
            if cave[(y,x)].t == '|':
                rl += 2
            # print(cave[(y,x)].t, end='')
        # print()

    print(rl)


# solve(510, (10,10))
solve(11991, (797,6))
