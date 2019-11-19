from operator import add

f = open("input.txt", "r")
input = f.read()

moves = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0)
}

santa_location = (0, 0)
robo_location = (0, 0)

counter = set()
for i in range(len(input)):
    move = input[i]
    if i % 2 == 0:
        santa_location = tuple(map(add, santa_location, moves[move]))
        counter.add(santa_location)
    else:
        robo_location = tuple(map(add, robo_location, moves[move]))
        counter.add(robo_location)

print len(counter)
