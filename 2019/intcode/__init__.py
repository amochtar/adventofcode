from collections import defaultdict
import itertools
import types


def runner(opcodes, inp=None):
    if isinstance(inp, list):
        inputs = (x for x in inp)
    elif isinstance(inp, int):
        inputs = itertools.repeat(inp)
    elif isinstance(inp, types.GeneratorType):
        inputs = inp

    opcodes = defaultdict(
        int, {i: int(v) for i, v in enumerate(opcodes)})

    def get_parameter(i, mode):
        if mode == 1:
            return opcodes[i]
        elif mode == 2:
            return opcodes[base+opcodes[i]]
        return opcodes[opcodes[i]]

    def write_parameter(i, mode, value):
        target = opcodes[i]
        if mode == 2:
            target += base
        opcodes[target] = value

    i = 0
    base = 0
    jumps = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}
    while True:
        opcode = opcodes[i] % 100
        modes = [int(p)
                 for p in reversed(str(opcodes[i] // 100).rjust(4, '0'))]
        a = get_parameter(i+1, modes[0])
        b = get_parameter(i+2, modes[1])

        if opcode == 1:
            write_parameter(i+3, modes[2], a+b)
        elif opcode == 2:
            write_parameter(i+3, modes[2], a*b)
        elif opcode == 3:
            if inp == None:
                a = yield 'inp'
            else:
                a = next(inputs)
            write_parameter(i+1, modes[0], a)
        elif opcode == 4:
            yield a
        elif opcode == 5:
            if a != 0:
                i = b
                continue
        elif opcode == 6:
            if a == 0:
                i = b
                continue
        elif opcode == 7:
            if a < b:
                write_parameter(i+3, modes[2], 1)
            else:
                write_parameter(i+3, modes[2], 0)
        elif opcode == 8:
            if a == b:
                write_parameter(i+3, modes[2], 1)
            else:
                write_parameter(i+3, modes[2], 0)
        elif opcode == 9:
            base += a
        elif opcode == 99:
            return

        i += jumps[opcode]
