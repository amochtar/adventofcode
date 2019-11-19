from operator import add
import re

with open('input.txt', 'r') as f:
    logs = f.read()

robots_pattern = re.compile(r'\[(-?\d+),(-?\d+)\]+')
robots = [tuple(map(int, r)) for r in robots_pattern.findall(logs)]

steps_pattern = re.compile(r'(?:\(-?\d+,-?\d+\)){' + str(len(robots)) + '}')
step_pattern = re.compile(r'\((-?\d+),(-?\d+)\)+')

collisions = set()
for steps in steps_pattern.finditer(logs):
    steps = [tuple(map(int, s)) for s in step_pattern.findall(steps[0])]
    for i in range(len(robots)):
        robots[i] = tuple(map(add, robots[i], steps[i]))

    if len(set(robots)) < len(robots):
        coll = robots[:]
        for r in set(robots):
            coll.remove(r)
        collisions.update(coll)

print("Part 1:", len(collisions))

xmax = max(collisions, key=lambda x: x[0])[0] + 1
ymax = max(collisions, key=lambda x: x[1])[1] + 1

print("Part 2:")
for y in range(ymax):
    for x in range(xmax):
        if (x, y) in collisions:
            print('#', end='')
        else:
            print(' ', end='')
    print()
