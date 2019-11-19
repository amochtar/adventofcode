from itertools import permutations


def strength(bridge):
    return sum(map(sum, bridge))


def bridges(components, port=0, bridge=[]):
    comp = [c for c in components if c not in bridge and port in c]
    for c in comp:
        yield bridge+[c]
    for c in comp:
        next_port = c[1] if c[0] == port else c[0]
        yield from bridges(components, next_port, bridge+[c])


def solve(inp):
    components = [tuple(map(int, line.split('/'))) for line in inp]

    bridge = max(bridges(components), key=strength)
    print('Part 1:', strength(bridge))


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
