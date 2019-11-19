with open("input.txt", "r") as f:
    input = [x.strip() for x in f.readlines()]


def calculate(values, instructions):
    i = 0
    while i < len(instructions):
        instruction = instructions[i].split(' ')
        if instruction[0] == 'cpy':
            try:
                value = int(instruction[1])
            except:
                value = values[instruction[1]]
            values[instruction[2]] = value
        elif instruction[0] == 'inc':
            values[instruction[1]] += 1
        elif instruction[0] == 'dec':
            values[instruction[1]] -= 1
        elif instruction[0] == 'jnz':
            try:
                value = int(instruction[1])
            except:
                value = values[instruction[1]]
            if value != 0:
                i += int(instruction[2])
                continue
        i += 1
    return values


values = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
print "Part 1:", calculate(values, input)
values = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
print "Part 2:", calculate(values, input)
