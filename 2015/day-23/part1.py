with open("input.txt", "r") as f:
    instructions = [x.strip() for x in f.readlines()]

registers = {'a': 0, 'b': 0}

i = 0
while i < len(instructions):
    instr = instructions[i].split()
    if instr[0] == 'hlf':
        registers[instr[1]] = registers[instr[1]] // 2
    elif instr[0] == 'tpl':
        registers[instr[1]] = registers[instr[1]] * 3
    elif instr[0] == 'inc':
        registers[instr[1]] += 1
    elif instr[0] == 'jmp':
        i += int(instr[1]) - 1
    elif instr[0] == 'jie':
        if registers[instr[1][0]] % 2 == 0:
            i += int(instr[2]) - 1
    elif instr[0] == 'jio':
        if registers[instr[1][0]] == 1:
            i += int(instr[2]) - 1
    i += 1

print(registers)
