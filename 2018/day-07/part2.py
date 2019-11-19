from collections import defaultdict
from collections import deque
from heapq import *


def solve(input):
    steps = defaultdict(list)
    pre_reqs = defaultdict(set)
    nodes = set([])
    for line in input:
        parts = line.split(' ')
        steps[parts[1]].append(parts[7])
        pre_reqs[parts[7]].add(parts[1])
        nodes.add(parts[1])
        nodes.add(parts[7])

    q = []
    for n in nodes:
        if n not in pre_reqs.keys():
            q.append(n)

    elves = [(0, None), (0, None), (0, None), (0, None), (0, None)]
    work_time = 60

    order = ''
    time = 0

    while len(order) < len(nodes):
        for i, e in enumerate(elves):
            if e[0] == time and e[1] != None:
                order += e[1]
                for next in sorted(steps[e[1]]):
                    addable = True
                    for p in pre_reqs[next]:
                        if p not in order:
                            addable = False
                            break
                    if addable:
                        heappush(q, next)
                elves[i] = (time, None)

        for s in sorted(q):
            for i, e in enumerate(elves):
                if elves[i][0] > time:
                    continue
                elves[i] = (time + work_time + ord(s) - ord('A') + 1, s)
                q.remove(s)
                break

        print(time, order, elves, q)

        if len(order) < len(nodes):
            time += 1

    print(order)
    print(time)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
