from operator import add

f = open("input.txt", "r")
input = f.read()

moves = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0)
}

location = (0, 0)
counter = set()
for move in input:
    location = tuple(map(add, location, moves[move]))
    counter.add(location)

print len(counter)
