from collections import deque


def get_value(registers, instr):
    try:
        return int(instr)
    except ValueError:
        return registers[instr]


def exec_instruction(instructions, slf, oth):
    instr = instructions[slf['i']]
    if instr[0] == 'set':
        slf['registers'][instr[1]] = get_value(slf['registers'], instr[2])
    elif instr[0] == 'add':
        slf['registers'][instr[1]] += get_value(slf['registers'], instr[2])
    elif instr[0] == 'mul':
        slf['registers'][instr[1]] *= get_value(slf['registers'], instr[2])
    elif instr[0] == 'mod':
        slf['registers'][instr[1]] %= get_value(slf['registers'], instr[2])
    elif instr[0] == 'snd':
        slf['q'].append(get_value(slf['registers'], instr[1]))
        slf['sent'] += 1
        oth['blocked'] = False
    elif instr[0] == 'rcv':
        if len(oth['q']) > 0:
            slf['registers'][instr[1]] = oth['q'].popleft()
        else:
            slf['blocked'] = True
            return
    elif instr[0] == 'jgz':
        if get_value(slf['registers'], instr[1]) > 0:
            slf['i'] += get_value(slf['registers'], instr[2]) - 1

    slf['i'] += 1
    if not 0 <= slf['i'] < len(instructions):
        slf['terminated'] = True


def solve(instructions):
    p0 = {'i': 0, 'blocked': False, 'terminated': False, 'sent': 0, 'registers': {'p': 0}, 'q': deque()}
    p1 = {'i': 0, 'blocked': False, 'terminated': False, 'sent': 0, 'registers': {'p': 1}, 'q': deque()}

    while not ((p0['blocked'] or p0['terminated']) and (p1['blocked'] or p1['terminated'])):
        exec_instruction(instructions, p0, p1)
        exec_instruction(instructions, p1, p0)

    print("Part 2:", p1['sent'])


with open('input.txt', 'r') as f:
    inp = f.read().splitlines()
    instructions = [i.split(' ') for i in inp]
    solve(instructions)
