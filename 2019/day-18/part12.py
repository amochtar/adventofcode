#!/usr/bin/env python

import networkx as nx
from heapq import heappop, heappush


def neighbors(p):
    return [
        (p[0], p[1]-1),
        (p[0], p[1]+1),
        (p[0]-1, p[1]),
        (p[0]+1, p[1])
    ]


def solve(vault):
    starts = []
    keys = {}
    vault_no_doors = nx.Graph()
    for y, line in enumerate(vault):
        for x, c in enumerate(line):
            p = (x, y)
            if c != '#':
                vault_no_doors.add_node(p)
                for n in neighbors(p):
                    if vault[n[1]][n[0]] != '#':
                        vault_no_doors.add_edge(p, n)
            if c == '@':
                starts.append(p)
            elif 'a' <= c <= 'z':
                keys[c] = p

    paths = {}
    for k1 in list(keys.values()) + starts:
        for k2 in keys.values():
            if k1 != k2:
                if nx.has_path(vault_no_doors, k1, k2):
                    path = nx.shortest_path(vault_no_doors, k1, k2)
                    steps = len(path) - 1
                    paths[(k1, k2)] = (steps, path)
                    paths[(k2, k1)] = (steps, path[::-1])

    def check_no_doors(path, found):
        for (x, y) in path:
            door = vault[y][x]
            if 'A' <= door <= 'Z' and door.lower() not in found:
                return False
        return True

    q = []
    heappush(q, (0, [], starts))  # steps, keys_found, pos
    seen = set()
    while q:
        (steps, found, pos) = heappop(q)

        state = (frozenset(found), tuple(pos))
        if state in seen:
            continue
        seen.add(state)

        # if len(seen) % 1000 == 0:
        #     print(len(seen), steps, ''.join(found), pos)
        if set(found) == set(keys):
            print(steps, ''.join(found), pos)
            return

        for key, key_pos in keys.items():
            if key in found:
                continue

            for i, p in enumerate(pos):
                if (p, key_pos) in paths:
                    (l, path) = paths[(p, key_pos)]
                    if check_no_doors(path, found):
                        new_pos = pos[:]
                        new_pos[i] = key_pos
                        heappush(q, (steps+l, found + [key], new_pos))


def vault_part2(vault):
    v = [list(line) for line in vault]
    for y, line in enumerate(vault):
        for x, c in enumerate(line):
            if c == '@':
                v[y-1][x-1] = '@'
                v[y-1][x] = '#'
                v[y-1][x+1] = '@'
                v[y][x-1] = '#'
                v[y][x] = '#'
                v[y][x+1] = '#'
                v[y+1][x-1] = '@'
                v[y+1][x] = '#'
                v[y+1][x+1] = '@'
                return v

# with open('test2.txt', 'r') as f:
#     input = f.read().strip().splitlines()
#     solve(input)


with open('input.txt', 'r') as f:
    input = f.read().strip().splitlines()
    solve(input)
    vault = vault_part2(input)
    solve(vault)
