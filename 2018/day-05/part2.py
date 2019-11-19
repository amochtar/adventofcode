from string import ascii_lowercase


def solve(input):
    shortest = len(input[0])
    for a in ascii_lowercase:
        units = input[0]
        units = units.replace(a, '')
        units = units.replace(a.upper(), '')
        done = False
        l = len(units)
        while not done:
            for a in ascii_lowercase:
                units = units.replace(a+a.upper(), '')
                units = units.replace(a.upper()+a, '')
            if len(units) == l:
                done = True
            l = len(units)

        shortest = min(shortest, l)
    print(shortest)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
