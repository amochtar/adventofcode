for f in ['test.txt', 'input.txt', 'input2.txt']:
    discs = []
    with open(f, 'r') as f:
        for line in f.readlines():
            parts = line.split()
            discs.append((int(parts[3]), int(parts[11][:-1])))

    t = 0
    while True:
        if all((t + disc[1] + i + 1) % disc[0] == 0 for i, disc in enumerate(discs)):
            break
        t += 1

    print f.name, t
