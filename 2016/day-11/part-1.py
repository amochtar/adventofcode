from collections import namedtuple
from collections import deque
from itertools import combinations
import re


State = namedtuple('state', ['steps', 'elevator', 'items'])


def short_state(state):
    return str((
        state.elevator,
        sorted([(state.items[el+'g'], state.items[el+'m']) for el in elements])
    ))


def generators_floor(state, i):
    return [k[0] for k, v in state.items.iteritems() if v == i and k.endswith('g')]


def microchips_floor(state, i):
    return [k[0] for k, v in state.items.iteritems() if v == i and k.endswith('m')]


def print_floors(state):
    for i in reversed(range(num_floors)):
        floor = ""
        for el in elements:
            if el in generators_floor(state, i):
                generator = el.upper() + 'G'
            else:
                generator = ". "
            if el in microchips_floor(state, i):
                microchip = el.upper() + 'M'
            else:
                microchip = ". "
            floor += " " + generator + " " + microchip
        elev = "."
        if state.elevator == i:
            elev = "E"
        print "F"+str(i+1), elev, floor


def is_valid(state):
    if state.elevator < 0 or state.elevator >= num_floors:
        return False

    for i in range(num_floors):
        g = generators_floor(state, i)
        m = microchips_floor(state, i)
        if len(g) == 0 or len(m) == 0:
            continue

        for el in m:
            if el not in g:
                return False
    return True


def done(state):
    return all(v == (num_floors - 1) for k, v in state.items.iteritems())


def next_states(state):
    elevator_items = [k for k, v in state.items.iteritems() if v == state.elevator]
    combis = list(combinations(elevator_items, 1)) + list(combinations(elevator_items, 2))
    next_states = []
    for i in [1, -1]:
        for c in combis:
            steps = state.steps + 1
            elevator = state.elevator + i
            items = dict(state.items)
            for el in c:
                items[el] += i
            next_state = State(steps=steps, elevator=elevator, items=items)
            if is_valid(next_state):
                next_states.append(next_state)
    return next_states


def read_input(file):
    with open(file, "r") as f:
        input = [x.strip() for x in f.readlines()]

    generators_pattern = re.compile(r'([a-z])[a-z]* generator')
    microchips_pattern = re.compile(r'([a-z])[a-z]*-compatible microchip')

    items = {}
    elements = set()
    for i in range(len(input)):
        generators = generators_pattern.findall(input[i])
        microchips = microchips_pattern.findall(input[i])
        items.update({g+"g": i for g in generators})
        items.update({m+"m": i for m in microchips})
        elements.update(generators)

    elements = sorted(elements)
    num_floors = len(input)
    initial_state = State(steps=0, elevator=0, items=items)
    return (num_floors, elements, initial_state)


for f in ['input.txt', 'input2.txt']:
    (num_floors, elements, initial_state) = read_input(f)

    print_floors(initial_state)

    visited_states = set()
    q = deque([initial_state])
    while q:
        s = q.popleft()
        if done(s):
            print f + ":", s.steps
            break

        short_s = short_state(s)
        if short_s in visited_states:
            continue
        else:
            visited_states.add(short_s)

        for next_s in next_states(s):
            q.append(next_s)
    else:
        print "Failed..."
