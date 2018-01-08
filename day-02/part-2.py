import numpy as np
with open("input.txt", "r") as f:
    instructions = [x.strip() for x in f.readlines()]

buttons = [
    ['0', '0', '1', '0', '0'],
    ['0', '2', '3', '4', '0'],
    ['5', '6', '7', '8', '9'],
    ['0', 'A', 'B', 'C', '0'],
    ['0', '0', 'D', '0', '0']
]

number = np.array([0, 2])

code = []
for instruction in instructions:
    for move in instruction:
        new_number = number.copy()
        if move == 'U':
            new_number[0] = max(0, new_number[0]-1)
        elif move == 'D':
            new_number[0] = min(len(buttons)-1, new_number[0]+1)
        elif move == 'L':
            new_number[1] = max(0, new_number[1]-1)
        elif move == 'R':
            new_number[1] = min(len(buttons[0])-1, new_number[1]+1)

        button = buttons[new_number[0]][new_number[1]]
        if button != '0':
            number = new_number

    button = buttons[number[0]][number[1]]
    code.append(button)

print "".join(code)
