#!/usr/bin/env python

import intcode
import networkx as nx


moves = {
    'n': lambda p: (p[0]-1, p[1]),
    's': lambda p: (p[0]+1, p[1]),
    'w': lambda p: (p[0], p[1]-1),
    'e': lambda p: (p[0], p[1]+1),
}
inputs = {
    'n': 1,
    's': 2,
    'w': 3,
    'e': 4,
}
turn_left = {
    'n': 'w',
    's': 'e',
    'w': 's',
    'e': 'n',
}
turn_right = {
    'n': 'e',
    's': 'w',
    'w': 'n',
    'e': 's',
}


def print_maze(maze, oxy_pos):
    nodes = list(nx.nodes(maze))
    minx = min([n[0] for n in nodes])
    maxx = max([n[0] for n in nodes])
    miny = min([n[1] for n in nodes])
    maxy = max([n[1] for n in nodes])

    for y in range(miny-1, maxy+2):
        for x in range(minx-1, maxx+2):
            if (x, y) == (0, 0):
                print('D', end='')
            elif (x, y) == oxy_pos:
                print('O', end='')
            elif (x, y) in nodes:
                print('.', end='')
            else:
                print('#', end='')
        print()
    print()


def solve(input):
    runner = intcode.runner(input)

    maze = nx.Graph()
    pos = (0, 0)
    oxy_pos = None
    dir = 'e'

    visited = set()
    while True:
        if (pos, dir) in visited:
            break
        visited.add((pos, dir))

        out = next(runner)
        assert out == 'inp'
        new_dir = turn_left[dir]
        new_pos = moves[new_dir](pos)
        inp = inputs[new_dir]
        out = runner.send(inp)
        assert 0 <= out <= 2

        if out == 0:
            dir = new_dir
            continue

        maze.add_edge(pos, new_pos)
        pos = new_pos
        dir = turn_right[dir]

        if out == 2:
            oxy_pos = pos

    print_maze(maze, oxy_pos)
    print(nx.shortest_path_length(maze, (0, 0), oxy_pos))
    print(nx.dag_longest_path_length(nx.bfs_tree(maze, oxy_pos)))


with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]
    solve(input)
