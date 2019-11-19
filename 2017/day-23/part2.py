def solve(b):
    b = b * 100 + 100000
    c = b + 17000

    h = 0
    while True:
        f = 1
        d = 2

        while True:
            # # Inefficient inner loop:
            # e = 2
            # while True:
            #     g = d * e - b
            #     if g == 0:
            #         f = 0
            #     e += 1
            #     g = e - b
            #     if g == 0:
            #         break
            # d += 1
            # if d == b:
            #     break
            # # Replace with:
            if b % d == 0:
                f = 0
            d += 1
            if d == b:
                break
            # # End replace

        if f == 0:
            h += 1
        if b == c:
            print('Part 2:', h)
            return
        b += 17


with open('input.txt', 'r') as f:
    inp = int(f.readlines()[0].split(' ')[-1])
    solve(inp)
