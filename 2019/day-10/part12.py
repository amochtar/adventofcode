#!/usr/bin/env python

import math
from itertools import permutations


def is_between(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - \
        (c[0] - a[0]) * (b[1] - a[1])

    if abs(crossproduct) != 0:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True


def scan(station, asteroids):
    targets = set(asteroids)
    targets.discard(station)

    for b, c in permutations(targets, 2):
        if is_between(station, b, c):
            targets.discard(b)

    return targets


def angle(a, b):
    x1, y1 = 0, -1
    x2, y2 = b[0]-a[0], b[1]-a[1]

    dot = x1*x2 + y1*y2      # dot product
    det = x1*y2 - y1*x2      # determinant
    angle = math.degrees(math.atan2(det, dot))
    if angle < 0:
        angle += 360
    return angle


def solve(input):
    asteroids = set([])
    for y, line in enumerate(input):
        for x, ast in enumerate(line):
            if ast != '.':
                asteroids.add((x, y))

    stations = {}
    for a in asteroids:
        stations[a] = scan(a, asteroids)

    num_ast = {a: len(x) for a, x in stations.items()}
    monitoring_station = max(stations.items(), key=lambda s: len(s[1]))
    print(monitoring_station[0], len(monitoring_station[1]))

    station = monitoring_station[0]
    cnt = 0
    vaporized = set([])
    asteroids.discard(station)
    while len(asteroids) > 0:
        to_destroy = scan(station, asteroids-vaporized)
        to_destroy = sorted(to_destroy, key=lambda a: angle(station, a))
        for a in to_destroy:
            cnt += 1
            vaporized.add(a)
            asteroids.discard(a)
            if cnt == 200:
                print(cnt, a, a[0]*100 + a[1])
                break


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
