from collections import defaultdict
from heapq import heappop, heappush


class Region(object):
    def __init__(self, y, x, gi, el, t):
        self.y = y
        self.x = x
        self.gi = gi
        self.el = el
        self.t = t

    def pos(self):
        return (self.y, self.x)


tools = {
    '.': set(['c', 't']),
    '=': set(['c', 'n']),
    '|': set(['t', 'n']),
}


moves = {
    'n': lambda p: (p[0]-1,p[1]),
    's': lambda p: (p[0]+1,p[1]),
    'w': lambda p: (p[0],p[1]-1),
    'e': lambda p: (p[0],p[1]+1),
}


def solve(depth, target):
    # Mapping cave
    cave = defaultdict(Region)
    for y in range(1000):
        for x in range(1000):
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

    # Find quickest route
    pos = (0,0)
    q = [(0,'t',pos, [(0,'t',pos)])]
    seen = {}
    while q:
        time, tool, pos, steps = heappop(q)
        if pos == target:
            if tool == 't':
                for s in steps:
                    print(s)
                print(time)
                return
            else:
                next_time = time+7
                next_pos = pos
                next_steps = steps[:]
                next_steps.append((next_time, 't', next_pos))
                heappush(q, (next_time, 't', next_pos, next_steps))
                continue

        if (tool,pos) in seen: # and seen[(tool,pos)] <= time:
            continue
        seen[(tool,pos)] = time

        for m in moves.values():
            next_pos = m(pos)
            # print(next_pos)
            if next_pos[0] >= 0 and next_pos[1] >= 0:
                p_tools = tools[cave[pos].t]
                np_tools = tools[cave[next_pos].t]
                common_tools = p_tools.intersection(np_tools)
                for next_tool in common_tools:
                    next_time = time+1
                    if next_tool != tool:
                        next_time += 7
                    next_steps = steps[:]
                    next_steps.append((next_time, next_tool, next_pos))
                    heappush(q, (next_time, next_tool, next_pos, next_steps))


solve(510, (10,10))
# solve(11991, (797,6))