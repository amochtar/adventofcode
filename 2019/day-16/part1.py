#!/usr/bin/env pypy3


def gen_pattern(i):
    p = [0] * (i+1)
    p.extend([1]*(i+1))
    p.extend([0]*(i+1))
    p.extend([-1]*(i+1))
    return p[1:]+p[:1]


def phase(inp):
    output = [0] * len(inp)
    for i, x in enumerate(inp):
        pattern = gen_pattern(i)
        for j, y in enumerate(inp):
            output[i] += y * pattern[j % len(pattern)]
        output[i] = abs(output[i]) % 10

    return output


def solve(input):
    for _ in range(100):
        input = phase(input)
    print(''.join(map(str, input[:8])))


# with open('test.txt', 'r') as f:
#     input = [int(i) for i in f.read().strip()]
#     solve(input)

with open('input.txt', 'r') as f:
    input = [int(i) for i in f.read().strip()]
    solve(input)
