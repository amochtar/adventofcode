from string import ascii_lowercase


def solve(input):
    units = input[0]
    done = False
    l = len(units)
    while not done:
        for a in ascii_lowercase:
            units = units.replace(a+a.upper(), '')
            units = units.replace(a.upper()+a, '')
        if len(units) == l:
            done = True
        l = len(units)

    print(l)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
