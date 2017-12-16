def dance(programs, moves):
    progs = list(programs)
    size = len(progs)
    for move in moves:
        if move[0] == 's':
            spin = size - int(move[1:])
            progs = progs[spin:] + progs[:spin]
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            idx_a = int(a)
            idx_b = int(b)
            progs[idx_a], progs[idx_b] = progs[idx_b], progs[idx_a]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            idx_a = progs.index(a)
            idx_b = progs.index(b)
            progs[idx_a], progs[idx_b] = progs[idx_b], progs[idx_a]
    return ''.join(progs)


def solve(moves):
    programs = 'abcdefghijklmnop'

    print("Part 1:", dance(programs, moves))

    seen = []
    for c in range(1000000000):
        if programs in seen:
            print("Part 2:", seen[1000000000 % c])
            break
        seen.append(programs)
        programs = dance(programs, moves)


with open('input.txt', 'r') as f:
    inp = f.read().split(',')
    solve(inp)
