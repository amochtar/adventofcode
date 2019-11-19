from itertools import combinations
from itertools import permutations
from collections import namedtuple
from collections import deque
import numpy as np

numbers = {}
with open('input.txt', 'r') as f:
    input = f.readlines()
    maze = np.array([[c != '#' for c in line.strip()] for line in input])
    for x, line in enumerate(input):
        for y, c in enumerate(line):
            try:
                number = int(c)
                numbers[number] = (x, y)
            except:
                pass


State = namedtuple('State', ['steps', 'location'])


def shortest_path(maze, a, b):
    visited = []
    q = deque([State(steps=0, location=a)])
    while q:
        s = q.popleft()
        if s.location == b:
            return s.steps
        if s.location in visited:
            continue
        visited.append(s.location)

        for next_step in next_steps(maze, s.location):
            q.append(State(steps=s.steps+1, location=next_step))
    else:
        print "Failed"


def next_steps(maze, location):
    next_steps = []
    for i in [1, -1]:
        new_x = (location[0] + i, location[1])
        try:
            if new_x[0] >= 0 and maze[new_x[0], new_x[1]]:
                next_steps.append(new_x)
        except:
            pass

        new_y = (location[0], location[1] + i)
        try:
            if new_x[1] >= 0 and maze[new_y[0], new_y[1]]:
                next_steps.append(new_y)
        except:
            pass
    return next_steps


def paths(numbers):
    paths = {}
    for a, b in combinations(numbers, 2):
        paths[(a, b)] = shortest_path(maze, numbers[a], numbers[b])
        paths[(b, a)] = paths[(a, b)]
    return paths


def shortest(numbers, paths, start=0, end=None):
    shortest = None
    path_perms = list(permutations([n for n in numbers if n != 0]))
    for perm in path_perms:
        path = [start] + list(perm)
        if end is not None:
            path += [end]
        path_len = 0
        for i in range(len(path)-1):
            path_len += paths[(path[i], path[i+1])]
        if not shortest or shortest > path_len:
            shortest = path_len
    return shortest


paths = paths(numbers)
print 'Part 1:', shortest(numbers, paths, 0)
print 'Part 2:', shortest(numbers, paths, 0, 0)
