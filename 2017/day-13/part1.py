def move_scanners(scanners, layers):
    for scanner, position in scanners.items():
        idx, direction = position
        idx += direction
        if direction == 1 and idx > layers[scanner]-1:
            direction = -1
            idx -= 2
        elif idx < 0:
            direction = 1
            idx += 2
        scanners[scanner] = (idx, direction)
    return scanners


def solve(inp):
    layers = {}
    scanners = {}
    for line in inp:
        layer, depth = line.split(': ')
        layers[int(layer)] = int(depth)
        scanners[int(layer)] = (0, 1)

    severity = 0
    for i in range(max(layers.keys())+1):
        try:
            if scanners[i][0] == 0:
                severity += i*layers[i]
        except KeyError:
            pass
        scanners = move_scanners(scanners, layers)

    print("Part 1:", severity)


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
