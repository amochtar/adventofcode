#!/usr/bin/env python

from collections import Counter
import base64


def solve(input):
    found = False
    for i,c in enumerate(input):
        password = input[i:i+16]
        count = Counter(password)
        if len(count) == 16:
            print(base64.b64decode(password))
            return



# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read()
    solve(input)
