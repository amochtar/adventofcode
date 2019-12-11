from collections import defaultdict


def runner(opcodes, inputs):
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
    while True:
        opcode = opcodes[i] % 100
        modes = [int(p)
                 for p in reversed(str(opcodes[i] // 100).rjust(4, '0'))]
        a = get_parameter(i+1, modes[0])
        b = get_parameter(i+2, modes[1])

        if opcode == 1:
            a = get_parameter(i+1, modes[0])
            b = get_parameter(i+2, modes[1])
            write_parameter(i+3, modes[2], a+b)
            i += 4
        elif opcode == 2:
            a = get_parameter(i+1, modes[0])
            b = get_parameter(i+2, modes[1])
            write_parameter(i+3, modes[2], a*b)
            i += 4
        elif opcode == 3:
            write_parameter(i+1, modes[0], next(inputs))
            i += 2
        elif opcode == 4:
            a = get_parameter(i+1, modes[0])
            yield a
            i += 2
        elif opcode == 5:
            a = get_parameter(i+1, modes[0])
            b = get_parameter(i+2, modes[1])
            if a != 0:
                i = b
            else:
                i += 3
        elif opcode == 6:
            a = get_parameter(i+1, modes[0])
            b = get_parameter(i+2, modes[1])
            if a == 0:
                i = b
            else:
                i += 3
        elif opcode == 7:
            a = get_parameter(i+1, modes[0])
            b = get_parameter(i+2, modes[1])
            if a < b:
                write_parameter(i+3, modes[2], 1)
            else:
                write_parameter(i+3, modes[2], 0)
            i += 4
        elif opcode == 8:
            a = get_parameter(i+1, modes[0])
            b = get_parameter(i+2, modes[1])
            if a == b:
                write_parameter(i+3, modes[2], 1)
            else:
                write_parameter(i+3, modes[2], 0)
            i += 4
        elif opcode == 9:
            a = get_parameter(i+1, modes[0])
            base += a
            i += 2
        elif opcode == 99:
            return
