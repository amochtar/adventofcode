from functools import reduce


def addr(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] + regs[b]
    return result

def addi(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] + b
    return result

def mulr(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] * regs[b]
    return result

def muli(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] * b
    return result

def banr(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] & regs[b]
    return result

def bani(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] & b
    return result

def borr(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] | regs[b]
    return result

def bori(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a] | b
    return result

def setr(regs, a, b, c):
    result = regs[:]
    result[c] = regs[a]
    return result

def seti(regs, a, b, c):
    result = regs[:]
    result[c] = a
    return result

def gtir(regs, a, b, c):
    result = regs[:]
    if a > regs[b]:
        result[c] = 1
    else:
        result[c] = 0
    return result

def gtri(regs, a, b, c):
    result = regs[:]
    if regs[a] > b:
        result[c] = 1
    else:
        result[c] = 0
    return result

def gtrr(regs, a, b, c):
    result = regs[:]
    if regs[a] > regs[b]:
        result[c] = 1
    else:
        result[c] = 0
    return result

def eqir(regs, a, b, c):
    result = regs[:]
    if a == regs[b]:
        result[c] = 1
    else:
        result[c] = 0
    return result

def eqri(regs, a, b, c):
    result = regs[:]
    if regs[a] == b:
        result[c] = 1
    else:
        result[c] = 0
    return result

def eqrr(regs, a, b, c):
    result = regs[:]
    if regs[a] == regs[b]:
        result[c] = 1
    else:
        result[c] = 0
    return result


ops = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr,
}


def factors(n):
    factors = set()
    for i in range(1,n+1):
        if n % i == 0:
            factors.add(i)
    return factors


def solve(input):
    registers = [0, 0, 0, 0, 0, 0]
    parts = input[0].split()
    ip_reg = int(parts[1])
    ip = 0

    instructions = []
    for line in input[1:]:
        instruction = line.split()
        instructions.append((instruction[0], int(instruction[1]), int(instruction[2]), int(instruction[3])))

    iterations = 0
    exits=set()
    while True:
        instruction = instructions[ip]
        op = ops[instruction[0]]
        registers[ip_reg] = ip
        after = op(registers, *instruction[1:])
        # print(iterations, ip, registers, instruction, after)
        registers = after
        ip = registers[ip_reg] + 1

        if ip < 0 or ip >= len(instructions):
            break

        if ip == 28:
            if registers[1] not in exits:
                exits.add(registers[1])
                print(registers[1])
        iterations += 1

        # print(sum(factors(registers[-1])))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
