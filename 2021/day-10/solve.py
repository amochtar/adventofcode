#!/usr/bin/env python

import aoc
from collections import deque


closing_bracket = {'{': '}', '[': ']', '(': ')', '<': '>'}
illegal_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_points = {')': 1, ']': 2, '}': 3, '>': 4}


@aoc.timing
def solve(inp: str):
    illegal_score = 0
    completion_scores = []
    for line in inp.splitlines():
        corrupt = False
        d = deque()
        for c in line:
            if c in closing_bracket.keys():
                d.append(closing_bracket[c])
            elif c != d.pop():
                illegal_score += illegal_points[c]
                corrupt = True
                break

        if not corrupt:
            score = 0
            for c in reversed(d):
                score *= 5
                score += completion_points[c]
            completion_scores.append(score)

    print("Part 1:", illegal_score)
    print("Part 2:", sorted(completion_scores)[len(completion_scores)//2])


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     solve(inp)

with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
