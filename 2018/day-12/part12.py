from collections import defaultdict


def sum_pots(idx, pots):
    s = 0
    for i, p in enumerate(pots):
        if p == '#':
            s += (i-idx)
    return s


def solve(input):
    state = input[0][15:]

    notes = defaultdict(lambda: '.')
    for line in input[2:]:
        parts = line.split(' => ')
        notes[parts[0]] = parts[1]

    idx = 0
    prev = 0
    iterations = 200
    for j in range(iterations):
        state = '....' + state + '....'
        new_state = list(state[2:-2])
        idx += 2

        for i in range(len(state)-4):
            lookup = state[i:i+5]
            new_state[i] = notes[lookup]

        state = ''.join(new_state)
        s = sum_pots(idx, state)
        diff = s - prev
        prev = s
        if j == 19:
            print(s)

    print(s + (50000000000-iterations) * diff)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
