from collections import defaultdict
import networkx as nx


directions = {
    'N': lambda p: (p[0]-1, p[1]),
    'S': lambda p: (p[0]+1, p[1]),
    'W': lambda p: (p[0], p[1]-1),
    'E': lambda p: (p[0], p[1]+1),
}


def solve(input):
    start = (0,0)

    pos = group_start = start
    stack = []

    regex = input[0]
    # print(regex)
    G = nx.Graph()
    for c in regex:
        # print(c, pos, group_start)
        if c in ['N','S','W','E']:
            next_pos = directions[c](pos)
            G.add_edge(pos, next_pos)
            pos = next_pos
        elif c == '(':
            stack.append(group_start)
            group_start = pos
        elif c == ')':
            group_start = stack.pop()
        elif c == '|':
            pos = group_start

    shortest_paths = nx.algorithms.shortest_path_length(G, start)
    print(max(shortest_paths.values()))
    print(len([p for p in shortest_paths.values() if p >= 1000]))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
