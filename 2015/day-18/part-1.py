import numpy as np

with open("input.txt", "r") as f:
    input = f.readlines()

lights = np.array([[c == '#' for c in line.strip()] for line in input])


def count_neighbors(arr, x, y):
    max_y = len(arr)
    max_x = len(arr[0])

    count = np.sum(arr[max(0, x-1):min(max_x, x+2), max(0, y-1):min(max_y, y+2)])
    if arr[x, y]:
        count -= 1
    return count


def is_on(arr, x, y):
    if x in [0, len(arr[0])-1] and y in [0, len(arr)-1]:
        return True

    n = count_neighbors(arr, x, y)
    if arr[x, y]:
        if n in [2, 3]:
            return True
    elif n == 3:
        return True
    return False


def animate(lights):
    new_lights = lights.copy()
    for y in range(len(new_lights)):
        for x in range(len(new_lights[0])):
            new_lights[x, y] = is_on(lights, x, y)
    return new_lights


lights[0, 0] = True
lights[0, -1] = True
lights[-1, 0] = True
lights[-1, -1] = True

for i in range(100):
    lights = animate(lights)

print np.sum(lights)
