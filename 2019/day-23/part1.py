#!/usr/bin/env python

import intcode
from collections import defaultdict


def solve(inp):
    inp = intcode.parse(inp)

    def next_packet(i):
        if len(packets[i]) > 0:
            return packets[i].pop(0)
        return (-1, -1)

    packets = defaultdict(list)
    ins = [0] * 50
    computers = []
    for i in range(50):
        computer = intcode.runner(inp)
        assert computer.send(None) == 'inp'
        assert computer.send(i) == 'inp'
        computers.append(computer)

    while True:
        for i, computer in enumerate(computers):
            px, py = next_packet(i)
            a = computer.send(px)
            if a == 'inp':
                a = computer.send(py)
                if a == 'inp':
                    continue

            x = next(computer)
            y = next(computer)

            if a == 255:
                print(y)
                return

            packets[a].append((x, y))


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
