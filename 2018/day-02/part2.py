from itertools import combinations


def solve(input):
    combs = combinations(input, 2)
    for (a, b) in combs:
        if distance(a,b) == 1:
            print(a, b)
            result = ""
            for (n, m) in zip(a, b):
                if n == m:
                    result += n
            print(result)


def distance(a, b):
    miss = 0
    for (n, m) in zip(a, b):
        if miss > 1:
            return miss
        if n != m:
            miss += 1
    return miss


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
