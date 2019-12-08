#!/usr/bin/env python


def chunks(it, length):
    return list(it[0+i:length+i] for i in range(0, len(it), length))


def solve(input, width, height):
    layers = chunks(input.strip(), width*height)

    img = ['?'] * width * height
    for layer in layers:
        for i in range(width*height):
            if img[i] == '?':
                if layer[i] == '1':
                    img[i] = '#'
                elif layer[i] == '0':
                    img[i] = ' '

    for line in chunks(img, width):
        print(''.join(line))


# with open('test.txt', 'r') as f:
#     input = f.read()
#     solve(input, 2, 2)

with open('input.txt', 'r') as f:
    input = f.read()
    solve(input, 25, 6)
