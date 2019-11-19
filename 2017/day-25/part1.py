from collections import defaultdict


def solve(inp):
    state = inp[0][-2]
    steps = int(inp[1].split()[-2])
    states = {}
    moves = {'right': +1, 'left': -1}
    for i in range(2, len(inp), 10):
        states[inp[i+1][-2]] = {
            int(inp[i+2][-2]): {
                'write': int(inp[i+3][-2]),
                'move': moves[inp[i+4].split()[-1][:-1]],
                'next': inp[i+5][-2]
            },
            int(inp[i+6][-2]): {
                'write': int(inp[i+7][-2]),
                'move': moves[inp[i+8].split()[-1][:-1]],
                'next': inp[i+9][-2]
            },
        }

    pos = 0
    tape = defaultdict(int)
    for i in range(steps):
        s = states[state][tape[pos]]
        tape[pos] = s['write']
        pos += s['move']
        state = s['next']

    print('Part 1:', sum(tape.values()))


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
