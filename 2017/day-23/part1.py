from collections import defaultdict


def get_value(registers, instr):
    try:
        return int(instr)
    except ValueError:
        return registers[instr]


def solve(instructions):
    registers = defaultdict(int)
    i = 0
    count = 0
    while i < len(instructions):
        instruction = instructions[i].split(' ')
        if instruction[0] == 'set':
            registers[instruction[1]] = get_value(registers, instruction[2])
        elif instruction[0] == 'sub':
            registers[instruction[1]] -= get_value(registers, instruction[2])
        elif instruction[0] == 'mul':
            count += 1
            registers[instruction[1]] *= get_value(registers, instruction[2])
        elif instruction[0] == 'jnz':
            value = get_value(registers, instruction[1])
            if value != 0:
                i += get_value(registers, instruction[2])
                continue
        i += 1

    print('Part 1:', count)


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
