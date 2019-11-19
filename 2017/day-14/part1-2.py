from operator import xor
from functools import reduce
import networkx as nx


def reverse(lst, start, length):
    rev = lst[:]
    lst_len = len(lst)
    for i in range(length//2):
        a = (start+i) % lst_len
        b = (start+length-i-1) % lst_len
        rev[a], rev[b] = rev[b], rev[a]
    return rev


def knot_hash(s):
    inp = [ord(x) for x in s]
    inp.extend([17, 31, 73, 47, 23])
    circlist = list(range(256))
    pos = 0
    skip = 0
    for _ in range(64):
        for length in inp:
            circlist = reverse(circlist, pos, length)
            pos += length + skip
            pos = pos % len(circlist)
            skip += 1

    dense = ''.join(['{:08b}'.format(reduce(xor, circlist[j:j+16])) for j in range(0, 256, 16)])
    return list(map(int, dense))


def neighours(x, y):
    n = set()
    if x > 0:
        n.add((x-1, y))
    if x < 127:
        n.add((x+1, y))
    if y > 0:
        n.add((x, y-1))
    if y < 127:
        n.add((x, y+1))
    return n


def solve(inp):
    grid = []
    for i in range(128):
        grid.append(knot_hash(inp + '-' + str(i)))
    print("Part 1:", sum(map(sum, grid)))

    graph = nx.Graph()
    for i in range(128):
        for j in range(128):
            if grid[i][j]:
                graph.add_node((i, j))
                for (x, y) in neighours(i, j):
                    if grid[x][y]:
                        graph.add_edge((i, j), (x, y))
    print("Part 2:", nx.number_connected_components(graph))


# solve('flqrgnkx')
solve('amgozmfv')
