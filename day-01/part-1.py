import numpy as np
with open("input.txt", "r") as f:
    steps = [x.strip() for x in f.read().split(',')]

directions = {}
directions['N'] = np.array([1, 0])
directions['S'] = np.array([-1, 0])
directions['E'] = np.array([0, 1])
directions['W'] = np.array([0, -1])

turns = {}
turns['N'] = {'R': 'E', 'L': 'W'}
turns['S'] = {'R': 'W', 'L': 'E'}
turns['E'] = {'R': 'S', 'L': 'N'}
turns['W'] = {'R': 'N', 'L': 'S'}

location = np.array([0, 0])
direction = 'N'

part_2 = 0
history = []

for step in steps:
    turn = step[0]
    length = int(step[1:])
    direction = turns[direction][turn]
    done = False
    for i in range(length):
        history.append(location.tolist())
        move = directions[direction]
        location += move
        if part_2 == 0 and location.tolist() in history:
            part_2 = sum(abs(location))

print "Part 1:", sum(abs(location))
print "Part 2:", part_2
