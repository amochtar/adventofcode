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

    heapify(q)
    order = []
    while len(q) > 0:
        curr = heappop(q)
        order.append(curr)
        next = sorted(steps[curr])
        for n in next:
            addable = True
            for p in pre_reqs[n]:
                if p not in order:
                    addable = False
            if addable:
                heappush(q, n)
    print (''.join(order))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
