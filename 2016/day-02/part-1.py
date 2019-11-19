import numpy as np
with open("input.txt", "r") as f:
    instructions = [x.strip() for x in f.readlines()]

buttons = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

number = np.array([1, 1])

code = []
for instruction in instructions:
    for move in instruction:
        if move == 'U':
            number[0] = max(0, number[0]-1)
        elif move == 'D':
            number[0] = min(2, number[0]+1)
        elif move == 'L':
            number[1] = max(0, number[1]-1)
        elif move == 'R':
            number[1] = min(2, number[1]+1)

    button = buttons[number[0]][number[1]]
    code.append(button)

print "".join(code)
