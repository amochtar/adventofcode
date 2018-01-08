def get_value(values, val):
    try:
        return int(val)
    except ValueError:
        return values[val]


def calculate(values, instructions):
    i = 0
    while i < len(instructions):
        instruction = instructions[i].split(' ')
        if instruction[0] == 'cpy':
            val = get_value(values, instruction[1])
            values[instruction[2]] = val
        elif instruction[0] == 'inc':
            values[instruction[1]] += 1
        elif instruction[0] == 'dec':
            values[instruction[1]] -= 1
        elif instruction[0] == 'jnz':
            val = get_value(values, instruction[1])
            if val != 0:
                i += get_value(values, instruction[2])
                continue
        elif instruction[0] == 'mul':
            values[instruction[3]] += get_value(values, instruction[1]) * get_value(values, instruction[2])
        elif instruction[0] == 'out':
            yield get_value(values, instruction[1])
        i += 1


with open('input.txt', 'r') as f:
    instructions = [x.strip() for x in f.readlines()]

done = False
i = 0
while not done:
    values = {'a': i, 'b': 0, 'c': 0, 'd': 0}
    next_val = 0
    iterations = 1000
    for val in calculate(values, instructions):
        if val != next_val:
            break
        next_val = 1 - next_val
        iterations -= 1
        if iterations <= 0:
            print 'Part 1:', i
            done = True
            break
    i += 1
