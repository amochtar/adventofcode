#!/usr/bin/env python

from itertools import permutations
import intcode


def inputs(phases, outputs, amp):
    yield phases[amp]
    while True:
        yield(outputs[amp])


def run_series(opcodes, phases):
    outputs = [0, 0, 0, 0, 0]  # these are shared between runs
    amps = [intcode.runner(opcodes, inputs(phases, outputs, amp))
            for amp in range(5)]
    amp = 0
    try:
        while True:
            out = next(amps[amp])
            amp = (amp+1) % 5
            outputs[amp] = out
    except StopIteration:
        return outputs[amp]


def solve(opcodes):
    phases_perms = permutations(range(5, 10))
    max_ret = 0
    for phases in phases_perms:
        ret = run_series(opcodes, phases)
        if ret > max_ret:
            # print(phases, ret)
            max_ret = ret

    print(max_ret)


# with open('test.txt', 'r') as f:
#     input = list(map(int, f.read().split(',')))
#     solve(input)

with open('input.txt', 'r') as f:
    input = list(map(int, f.read().split(',')))
    solve(input)
