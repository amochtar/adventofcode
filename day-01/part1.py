def solve(input):
    print(sum(list(map(int, input))))


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
