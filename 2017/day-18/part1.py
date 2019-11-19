from collections import defaultdict


def get_value(registers, instr):
    try:
        return int(instr)
    except ValueError:
        return registers[instr]


def solve(instructions):
    registers = defaultdict(int)
    i = 0
    last_played = 0
    recovered = 0
    while i < len(instructions):
        instruction = instructions[i].split(' ')
        if instruction[0] == 'set':
            registers[instruction[1]] = get_value(registers, instruction[2])
        elif instruction[0] == 'add':
            registers[instruction[1]] += get_value(registers, instruction[2])
        elif instruction[0] == 'mul':
            registers[instruction[1]] *= get_value(registers, instruction[2])
        elif instruction[0] == 'mod':
            registers[instruction[1]] %= get_value(registers, instruction[2])
        elif instruction[0] == 'snd':
            last_played = registers[instruction[1]]
        elif instruction[0] == 'rcv':
            if get_value(registers, instruction[1]) != 0:
                recovered = last_played
                break
        elif instruction[0] == 'jgz':
            value = get_value(registers, instruction[1])
            if value > 0:
                i += get_value(registers, instruction[2])
                continue
        i += 1

    print("Part 1:", recovered)


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    solve(inp)
