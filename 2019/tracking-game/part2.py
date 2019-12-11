#!/usr/bin/env python

import math
import statistics
from collections import Counter, defaultdict
import binascii
import json


def solve(input):
    words = input.split()

    decoded = ""
    for word in words:
        n = int(word, 2)
        decoded += n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

    data = json.loads(decoded)

    readings = defaultdict(Counter)
    for d in data:
        for reading in d['readings']:
            for c, val in reading['contaminants'].items():
                readings[d['date']]['total'] += val
                readings[d['date']][c] += val

    mean = statistics.mean([r['total'] for r in readings.values()])
    # print(readings)
    compare = sorted([(d, r['total'])
                      for (d, r) in readings.items()], key=lambda v: abs(v[1]/mean))
    anomaly = compare[-1]
    print(anomaly[0])

    anomaly_readings = [d for d in data if d['date']
                        == anomaly[0]][0]['readings']

    at = Counter()
    for r in anomaly_readings:
        t = r['time']
        i = r['id']
        for c, val in r['contaminants'].items():
            at[(t, i)] += val
    print(binascii.unhexlify(at.most_common(1)[0][0][1]))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)
with open('ppb.bin.log', 'r') as f:
    input = f.read()
    solve(input)
