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


def solve(input):
    i = 0
    total = 0
    while i <= len(input):
        before = registers(input[i])
        after = registers(input[i+2])
        op = list(map(int, input[i+1].split()))
        count = 0
        for o in ops:
            # print( o(before, *op[1:]), after)
            if o(before, *op[1:]) == after:
                count += 1
        if count >= 3:
            total +=1
        i += 4
    print(total)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
