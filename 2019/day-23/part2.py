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
    ins = defaultdict(list)
    computers = []
    for i in range(50):
        computer = intcode.runner(inp)
        assert next(computer) == 'inp'
        computers.append(computer)

    nat = None
    last_y = None
    qs = list(range(50))
    while True:
        if nat and all(q == -1 for q in qs) and all(len(p) == 0 for p in packets.values()):
            if last_y == nat[1]:
                print(last_y)
                return
            last_y = nat[1]
            packets[0].append(nat)

        for i, computer in enumerate(computers):
            a = computer.send(qs[i])
            if a == 'inp':
                px, py = next_packet(i)
                if px != -1:
                    a = computer.send(px)
                qs[i] = py
            else:
                x = computer.send(None)
                y = computer.send(None)

                if a == 255:
                    nat = (x, y)
                    continue

                packets[a].append((x, y))


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
