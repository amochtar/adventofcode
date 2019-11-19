with open("input.txt", "r") as f:
    input = [x.strip() for x in f.readlines()]


def swap_pos(s, x, y):
    sl = list(s)
    sl[x], sl[y] = sl[y], sl[x]
    return ''.join(sl)


def swap_letter(s, x, y):
    xi = s.index(x)
    yi = s.index(y)
    return swap_pos(s, xi, yi)


def rotate_step(s, x):
    x = x % len(s)
    return s[-x:] + s[:-x]


def rotate_letter(s, x):
    xi = s.index(x)
    rot = 1 + xi
    if xi >= 4:
        rot += 1
    return rotate_step(s, rot)


def get_unrotate_lookup(seed):
    unrotate_lookup = {}
    for i, c in enumerate(seed):
        rot_s = rotate_letter(seed, c)
        ci = rot_s.index(c)
        unrotate_lookup[ci] = i - ci
    return unrotate_lookup


unrotate_lookup = get_unrotate_lookup('abcdefgh')


def unrotate_letter(s, x):
    return rotate_step(s, unrotate_lookup[s.index(x)])


def reverse(s, x, y):
    return s[:x] + s[x:y+1][::-1] + s[y+1:]


def move(s, x, y):
    c = s[x]
    s = s[:x] + s[x+1:]
    return s[:y] + c + s[y:]


def scramble(file, s):
    with open(file, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split()

            if line.startswith('swap position'):
                s = swap_pos(s, int(parts[2]), int(parts[5]))
            elif line.startswith('swap letter'):
                s = swap_letter(s, parts[2], parts[5])
            elif line.startswith('rotate based on position'):
                s = rotate_letter(s, parts[-1])
            elif line.startswith('rotate left'):
                s = rotate_step(s, -int(parts[2]))
            elif line.startswith('rotate right'):
                s = rotate_step(s, int(parts[2]))
            elif line.startswith('reverse position'):
                s = reverse(s, int(parts[2]), int(parts[4]))
            elif line.startswith('move'):
                s = move(s, int(parts[2]), int(parts[5]))
        return s


def unscramble(file, s):
    with open(file, 'r') as f:
        for line in reversed(f.readlines()):
            parts = line.strip().split()

            if line.startswith('swap position'):
                s = swap_pos(s, int(parts[5]), int(parts[2]))
            elif line.startswith('swap letter'):
                s = swap_letter(s, parts[5], parts[2])
            elif line.startswith('rotate based on position'):
                s = unrotate_letter(s, parts[-1])
            elif line.startswith('rotate left'):
                s = rotate_step(s, int(parts[2]))
            elif line.startswith('rotate right'):
                s = rotate_step(s, -int(parts[2]))
            elif line.startswith('reverse position'):
                s = reverse(s, int(parts[2]), int(parts[4]))
            elif line.startswith('move'):
                s = move(s, int(parts[5]), int(parts[2]))
        return s


print 'Part 1:', scramble('input.txt', 'abcdefgh')
print 'Part 2:', unscramble('input.txt', 'fbgdceah')
