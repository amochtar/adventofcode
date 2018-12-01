def solve(input):
    f = 0
    frs = list(map(int, input))
    for fr in frs:
        f += fr
    print(f)


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
