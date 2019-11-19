next_dt = {
    ('>', 'l'): ('^', 's'),
    ('>', 's'): ('>', 'r'),
    ('>', 'r'): ('v', 'l'),
    ('<', 'l'): ('v', 's'),
    ('<', 's'): ('<', 'r'),
    ('<', 'r'): ('^', 'l'),
    ('^', 'l'): ('<', 's'),
    ('^', 's'): ('^', 'r'),
    ('^', 'r'): ('>', 'l'),
    ('v', 'l'): ('>', 's'),
    ('v', 's'): ('v', 'r'),
    ('v', 'r'): ('<', 'l'),
}

next_dc = {
    ('>', '/'): '^',
    ('>', '\\'): 'v',
    ('<', '/'): 'v',
    ('<', '\\'): '^',
    ('^', '/'): '>',
    ('^', '\\'): '<',
    ('v', '/'): '<',
    ('v', '\\'): '>',
}

def next_dir(d, t, c):
    if c in ['|', '-']:
        return (d, t)
    elif c == '+':
        return next_dt[(d, t)]
    else:
        return (next_dc[(d, c)], t)


def solve(input):
    tracks = [list(line) for line in input]
    carts = []
    for y in range(len(tracks)):
        for x in range(len(tracks[0])):
            c = tracks[y][x]

            if c in ['>','<','^','v']:
                carts.append((y, x, c, 'l'))
            if c in ['>', '<']:
                tracks[y][x] = '-'
            elif c in ['^', 'v']:
                tracks[y][x] = '|'

    first_collision = False
    while len(carts) > 1:
        carts = sorted(carts)
        for i, c in enumerate(carts):
            if c == None:
                continue
            (y, x, d, t) = c
            if d == '>':
                new_x = x + 1
                new_y = y
            elif d == '<':
                new_x = x - 1
                new_y = y
            elif d == '^':
                new_x = x
                new_y = y - 1
            elif d == 'v':
                new_x = x
                new_y = y + 1

            new_d, new_t = next_dir(d, t, tracks[new_y][new_x])
            coll = [c for c in carts if c != None and c[0] == new_y and c[1] == new_x]
            if len(coll) > 0:
                if not first_collision:
                    print('%s,%s' % (new_x, new_y))
                    first_collision = True
                carts[i] = None
                coll_idx = carts.index(coll[0])
                carts[coll_idx] = None
            else:
                carts[i] = (new_y, new_x, new_d, new_t)
        carts = [c for c in carts if c != None]
    print('%s,%s' % (carts[0][1], carts[0][0]))


# with open('test2.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
