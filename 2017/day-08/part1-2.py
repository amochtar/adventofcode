from collections import defaultdict


def solve(inp):
    registers = defaultdict(int)
    highest = 0
    for line in inp:
        parts = line.split()
        expression = 'registers["' + parts[4] + '"]' + parts[5] + parts[6]
        if parts[1] == 'inc':
            if eval(expression):
                registers[parts[0]] += int(parts[2])
        elif parts[1] == 'dec':
            if eval(expression):
                registers[parts[0]] -= int(parts[2])
        highest = max(highest, max(registers.values()))

    print("Part 1:", max(registers.values()))
    print("Part 2:", highest)


with open('input.txt', 'r') as f:
    inp = f.readlines()
    solve(inp)
