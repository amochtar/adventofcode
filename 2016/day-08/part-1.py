import numpy as np

with open("input.txt", "r") as f:
    instructions = [x.strip() for x in f.readlines()]


def rotate_row(screen, index, amount):
    row = screen[index].tolist()
    amount = amount % len(row)
    screen[index] = row[-amount:] + row[:-amount]


def rotate_column(screen, index, amount):
    screen = screen.T
    rotate_row(screen, index, amount)
    screen = screen.T


def rect(screen, width, height):
    for x in range(width):
        for y in range(height):
            screen[y][x] = 1


def print_screen(screen):
    for row in screen:
        print ''.join(['#' if l else ' ' for l in row])


screen = np.zeros((6, 50), dtype=int)
for instruction in instructions:
    i = instruction.split()
    if i[0] == 'rect':
        (width, height) = i[1].split('x')
        rect(screen, int(width), int(height))
    elif i[0] == 'rotate':
        index = int(i[2].split('=')[1])
        amount = int(i[4])
        if i[1] == 'column':
            rotate_column(screen, index, amount)
        elif i[1] == 'row':
            rotate_row(screen, index, amount)

print 'Part 1:', sum(sum(screen))

print 'Part 2:'
print_screen(screen)
