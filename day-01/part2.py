def solve(input):
    f = 0
    ff = set([f])

    frs = list(map(int, input))
    while True:
        for fr in frs:
            f += fr
            if f in ff:
                print(f)
                return

            ff.add(f)


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
