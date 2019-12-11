#!/usr/bin/env python

import math
import statistics
from collections import Counter, defaultdict
import binascii
import json


def solve(input):
    data = json.loads(input)
    regions = data['regions']
    for region in regions:
        region_id = region['regionID']
        readings = region['readings']
        for rs in readings:
            reading_id = rs['readingID']
            reading = rs['reading']
            # print(reading)
            return


with open('flood.txt', 'r') as f:
    input = f.read()
    solve(input)


def pools(levels):
    left_index = 0
    left_level = levels[left_index]
    right_index = 0
    right_level = levels[right_index]
    potential_pool = False

    total_pool_size = 0

    for i, l in enumerate(levels):
        print(left_index, right_index, i, potential_pool)
        if potential_pool:
            right_index = i
            right_level = l

            # pool ends
            if l >= left_level:
                potential_pool = False
                total_pool_size += pool_size(levels, left_index, right_index)
                left_index = i
                left_level = l
        else:
            if l >= left_level:
                left_index = i
                left_level = l
            else:
                potential_pool = True
                right_index = i
                right_level = l

    return total_pool_size


def pool_size(levels, left, right):
    print(left, right)
    flood_level = min(levels[left], levels[right])
    flood_size = 0
    pool = levels[left:right+1]
    for l in pool:
        flood_size += max(0, flood_level-l)

    return flood_size


print(pools([7, 7, 6, 5, 4, 4, 9, 8, 8, 7, 7, 8]))
