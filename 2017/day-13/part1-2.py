from itertools import count


def caught_by_scanner(layer, depth, delay=0):
    return (layer+delay) % ((depth-1)*2) == 0


def solve(inp):
    layers = {}
    for line in inp:
        layer, depth = line.split(': ')
        layers[int(layer)] = int(depth)

    severity = 0
    for layer, depth in layers.items():
        if caught_by_scanner(layer, depth):
            severity += layer*depth
    print("Part 1:", severity)

    for delay in count():
        caught = False
        for layer, depth in layers.items():
            if caught_by_scanner(layer, depth, delay):
                caught = True
                break
        if not caught:
            break
    print("Part 2:", delay)


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
