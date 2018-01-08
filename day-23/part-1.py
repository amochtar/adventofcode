def get_value(values, val):
    try:
        return int(val)
    except ValueError:
        return values[val]


def calculate(values, instructions):
    i = 0
    while i < len(instructions):
        instruction = instructions[i].split(' ')
        if i == 4:
            values['a'] = values['b'] * values['d']
            values['c'] = 0
            values['d'] = 0
            i = 10
            continue
        if instruction[0] == 'cpy':
            val = get_value(values, instruction[1])
            values[instruction[2]] = val
            # print str(i).rjust(2), 'cpy', val, instruction[2]
        elif instruction[0] == 'inc':
            values[instruction[1]] += 1
            # print str(i).rjust(2), instructions[i]
        elif instruction[0] == 'dec':
            values[instruction[1]] -= 1
            # print str(i).rjust(2), instructions[i]
        elif instruction[0] == 'jnz':
            val = get_value(values, instruction[1])
            # print str(i).rjust(2), 'jnz', val, instruction[2]
            if val != 0:
                i += get_value(values, instruction[2])
                continue
        elif instruction[0] == 'tgl':
            target = get_value(values, instruction[1])
            try:
                target_instr = instructions[i+target].split()
                if len(target_instr) == 2:
                    if target_instr[0] == 'inc':
                        target_instr[0] = 'dec'
                    else:
                        target_instr[0] = 'inc'
                else:
                    if target_instr[0] == 'jnz':
                        target_instr[0] = 'cpy'
                    else:
                        target_instr[0] = 'jnz'
                instructions[i+target] = ' '.join(target_instr)
            except IndexError:
                pass
        elif instruction[0] == 'mul':
            values[instruction[3]] = get_value(values, instruction[1]) * get_value(values, instruction[2])
        i += 1
    return values


with open('input.txt', 'r') as f:
    values = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    print 'Part 1:', calculate(values, [x.strip() for x in f.readlines()])

with open('input2.txt', 'r') as f:
    values = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    print 'Part 2:', calculate(values, [x.strip() for x in f.readlines()])
