import numpy as np
import re

f = open("input.txt", "r")
input = f.readlines()
instructions = [x.strip() for x in input]

grid = np.zeros((1000, 1000))

instr = re.compile(r'(?P<action>[a-z ]+) (?P<startx>\d+),(?P<starty>\d+) through (?P<endx>\d+),(?P<endy>\d+)')

for instruction in instructions:
    i = instr.match(instruction).groupdict()
    startx = int(i['startx'])
    starty = int(i['starty'])
    endx = int(i['endx']) + 1
    endy = int(i['endy']) + 1
    print i, startx, starty, endx, endy
    if i['action'] == 'turn on':
        grid[startx:endx, starty:endy] += 1
    elif i['action'] == 'turn off':
        grid[startx:endx, starty:endy] -= 1
        grid[grid < 0] = 0
    elif i['action'] == 'toggle':
        grid[startx:endx, starty:endy] += 2

    print grid

print np.sum(grid)
