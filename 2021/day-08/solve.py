#!/usr/bin/env python

import aoc


@aoc.timing
def part1(inp):
    cnt = 0
    for line in inp.splitlines():
        _, outs = (part.split(' ') for part in line.split(' | ', 1))
        cnt += sum(1 for d in outs if len(d) in [2, 3, 4, 7])
    return cnt


@aoc.timing
def part2(inp):
    def digit_mapping(digits):
        mapping = {}
        # map unique digits 1, 4, 7, 8
        for d in digits:
            if len(d) == 2:
                mapping[1] = set(d)
            elif len(d) == 3:
                mapping[7] = set(d)
            elif len(d) == 4:
                mapping[4] = set(d)
            elif len(d) == 7:
                mapping[8] = set(d)
        assert len(mapping) == 4

        for d in digits:
            # map digits 2, 3 and 5 (all len 5)
            if len(d) == 5:
                if len(set(d).intersection(mapping[1])) == 2 or len(set(d).intersection(mapping[7])) == 3:
                    mapping[3] = set(d)
                elif len(set(d).intersection(mapping[4])) == 2:
                    mapping[2] = set(d)
                else:
                    mapping[5] = set(d)

            # map digits 0, 6 and 9 (all len 6)
            if len(d) == 6:
                if len(set(d).intersection(mapping[1])) == 1 or len(set(d).intersection(mapping[7])) == 2:
                    mapping[6] = set(d)
                elif len(set(d).intersection(mapping[4])) == 4:
                    mapping[9] = set(d)
                else:
                    mapping[0] = set(d)
        assert len(mapping) == 10

        # reverse mapping for easy lookup
        return {''.join(sorted(v)): k for k, v in mapping.items()}

    total_value = 0
    for line in inp.splitlines():
        ins, outs = (part.split(' ') for part in line.split(' | ', 1))
        mapping = digit_mapping(ins+outs)

        total_value += sum(10**(3-i)*mapping[''.join(sorted(out))]
                           for i, out in enumerate(outs))
    return total_value


# with open('test.txt', 'r') as f:
#     inp = f.read()
#     print("Part 1:", part1(inp))
#     print("Part 2:", part2(inp))

with open('input.txt', 'r') as f:
    inp = f.read()
    print("Part 1:", part1(inp))
    print("Part 2:", part2(inp))
