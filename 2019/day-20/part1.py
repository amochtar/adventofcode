#!/usr/bin/env python

import networkx as nx
from collections import defaultdict


def neighbors(grid, p):
    height = len(grid)
    width = len(grid[0])

    px, py = p
    if px == 0 or py == 0 or px == width-1 or py == height-1:
        return []

    return [
        (p[0], p[1]-1),
        (p[0], p[1]+1),
        (p[0]-1, p[1]),
        (p[0]+1, p[1])
    ]


def solve(inp):
    start = None
    end = None
    portals = defaultdict(list)
    maze = nx.Graph()
    for y, line in enumerate(inp):
        for x, c in enumerate(line):
            p = (x, y)
            if c == '.':
                maze.add_node(p)
                for n in neighbors(inp, p):
                    if inp[n[1]][n[0]] == '.':
                        maze.add_edge(p, n)
            if 'A' <= c <= 'Z':
                portal_pos = None
                portal = None
                for n in neighbors(inp, p):
                    nc = inp[n[1]][n[0]]
                    if nc == '.':
                        portal_pos = n
                    if 'A' <= nc <= 'Z':
                        portal = ''.join(sorted(c+nc))
                if portal != None and portal_pos != None:
                    if portal == 'AA':
                        start = portal_pos
                    if portal == 'ZZ':
                        end = portal_pos
                    portals[portal].append(portal_pos)
                    if len(portals[portal]) == 2:
                        maze.add_edge(portals[portal][0], portals[portal][1])
                        maze.add_edge(portals[portal][1], portals[portal][0])

    print(nx.shortest_path_length(maze, start, end))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
