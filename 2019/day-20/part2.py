#!/usr/bin/env python

import networkx as nx
from heapq import heappop, heappush
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
    width = len(inp[0])
    height = len(inp)

    def is_inner(pos):
        return pos[0] not in (
            2, width-3) and pos[1] not in (2, height-3)

    def other(portal):
        if portal[-1] == 'i':
            return (portal[:2]+'o', 1)
        if portal[-1] == 'o':
            return (portal[:2]+'i', -1)
        return (portal, 0)

    start = None
    end = None
    portals = {}
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
                p1 = None
                for n in neighbors(inp, p):
                    nc = inp[n[1]][n[0]]
                    if nc == '.':
                        portal_pos = n
                    if 'A' <= nc <= 'Z':
                        p1 = ''.join(sorted(c+nc))
                if p1 != None and portal_pos != None:
                    if p1 == 'AA':
                        start = portal_pos
                    elif p1 == 'ZZ':
                        end = portal_pos
                    else:
                        if is_inner(portal_pos):
                            p1 += 'i'
                        else:
                            p1 += 'o'
                        portals[p1] = portal_pos

    paths = defaultdict(dict)
    if nx.has_path(maze, start, end):
        l = nx.shortest_path_length(maze, start, end)
        paths['AA']['ZZ'] = l
        paths['ZZ']['AA'] = l
    for p1, pos1 in portals.items():
        if p1[-1] == 'i':  # is inner
            if nx.has_path(maze, start, pos1):
                l = nx.shortest_path_length(maze, start, pos1)
                paths['AA'][p1] = l
                paths[p1]['AA'] = l
            if nx.has_path(maze, end, pos1):
                l = nx.shortest_path_length(maze, end, pos1)
                paths['ZZ'][p1] = l
                paths[p1]['ZZ'] = l
        for p2, pos2 in portals.items():
            if p1 == p2:
                continue
            if nx.has_path(maze, pos1, pos2):
                l = nx.shortest_path_length(maze, pos1, pos2)
                paths[p1][p2] = l
                paths[p2][p1] = l

    q = []
    heappush(q, (0, 0, 'AA'))  # steps, level, pos
    seen = set()
    while q:
        steps, level, pos = heappop(q)

        state = (level, pos)
        if state in seen:
            continue
        seen.add(state)

        if level == 0 and pos == 'ZZ':
            print(len(seen), steps)
            return

        for portal, s in paths[pos].items():
            next_portal, l = other(portal)
            if l >= 0 or level > 0:
                heappush(q, (steps + s + abs(l), level + l, next_portal))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
