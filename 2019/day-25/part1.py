#!/usr/bin/env python

import intcode
from itertools import combinations


def solve(inp):
    inp = intcode.parse(inp)
    runner = intcode.runner(inp)
    command = ""
    # recorded these commands by walking the starship manually
    commands = ['north', 'take mutex', 'east', 'east', 'east', 'take whirled peas', 'west', 'west',
                'west', 'south', 'west', 'take space law space brochure', 'north', 'take loom',
                'south', 'south', 'take hologram', 'west', 'take manifold', 'east', 'north', 'east',
                'south', 'take cake', 'west', 'south', 'take easter egg', 'south', 'south']
    items = set(i[5:] for i in commands if i[:5] == 'take ')
    inv = set()
    for i in items:
        commands.append('drop %s' % i)
    commands.append('south')

    def item_combinations():
        for r in range(1, len(items)+1):
            yield from combinations(items, r)

    output = ""
    at_security = False
    item_gen = item_combinations()
    while True:
        try:
            out = next(runner)
        except StopIteration:
            print(output)
            return
        while out == 'inp':
            if len(command) == 0:
                if not at_security and "Alert!" in output:
                    at_security = True

                if len(commands) > 0:
                    command = commands.pop(0)
                elif at_security:
                    item_comb = next(item_gen)
                    output = ""
                    print("Trying", item_comb)
                    for i in inv:
                        if i not in item_comb:
                            commands.append('drop %s' % i)
                    for i in item_comb:
                        if i not in inv:
                            commands.append('take %s' % i)
                    inv = item_comb
                    commands.append("south")
                    command = commands.pop(0)
                else:
                    command = input()
                command += '\n'
            out = runner.send(ord(command[0]))
            command = command[1:]
        output += chr(out)


with open('input.txt', 'r') as f:
    inp = f.read()
    solve(inp)
