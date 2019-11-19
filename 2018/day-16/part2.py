from collections import defaultdict


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


ops = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
]


def registers(line):
    return list(map(int,line[9:-1].split(', ')))


def mapping(input):
    ops_mapping = defaultdict(lambda: set(ops))

    i=0
    while i <= len(input):
        before = registers(input[i])
        after = registers(input[i+2])
        op = list(map(int, input[i+1].split()))

        new_mapping = set([])
        for o in ops_mapping[op[0]]:
            if o(before, *op[1:]) == after:
                new_mapping.add(o)
        ops_mapping[op[0]] = new_mapping

        i += 4

    unique_ops = {}
    while True:
        for k, v in ops_mapping.items():
            if len(v) == 1:
                unique_ops[k] = v.pop()
        for o in unique_ops.values():
            for k, v in ops_mapping.items():
                if o in v:
                    v.remove(o)
        if len(unique_ops) == len(ops):
            break
    return unique_ops


def solve(input, mapping):
    regs = [0, 0, 0, 0]
    for line in input:
        op = list(map(int, line.split()))
        regs = mapping[op[0]](regs, *op[1:])

    print(regs[0])


with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    mapping = mapping(input)

with open('input2.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input, mapping)
