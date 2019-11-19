import re


def solve(inp):
    ignore_pattern = re.compile(r'!.')
    inp = ignore_pattern.sub('', inp)
    before = len(inp)

    garbage_pattern = re.compile(r'<[^>]*>')
    inp = garbage_pattern.sub('<>', inp)
    after = len(inp)

    num_open = 0
    score = 0
    for c in inp:
        if c == '{':
            num_open += 1
            score += num_open
        elif c == '}':
            num_open -= 1

    print("Part 1:", score)
    print("Part 2:", before - after)


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
