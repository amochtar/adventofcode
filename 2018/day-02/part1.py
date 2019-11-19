from collections import Counter


def solve(input):
    twos = 0
    threes = 0
    for line in input:
        c = Counter(line)
        has2 = False
        has3 = False
        for k, v in c.items():
            if not has2 and v == 2:
                twos += 1
                has2 = True
            elif not has3 and v == 3:
                threes += 1
                has3 = True
    print (twos*threes)


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
