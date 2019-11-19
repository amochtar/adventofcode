from collections import deque
from functools import reduce


class Unit:
    def __init__(self, y, x, unit, hp, attack_power):
        self.y = y
        self.x = x
        self.unit = unit
        self.hp = hp
        self.attack_power = attack_power

    def __repr__(self):
        return '({},{}) {} {}'.format(self.y, self.x, self.unit, self.hp)

    def __str__(self):
        return '({},{}) {} {}'.format(self.y, self.x, self.unit, self.hp)

    def pos(self):
        return (self.y, self.x)


def neighbours(y, x):
    return [(y-1, x), (y,x-1), (y,x+1), (y+1,x)]


def select_enemy(a, b):
    if a.hp < b.hp:
        return a
    elif b.hp < a.hp:
        return b

    if a.pos() < b.pos():
        return a
    return b


def shortest_paths(grid, units, pos, targets):
    q = deque([(p, 1) for p in neighbours(*pos)])
    visited = set([])

    units_pos = [u.pos() for u in units if u.hp > 0]
    found_cost = None
    found_targets = []
    while q:
        p, cost = q.popleft()
        if found_cost != None and cost > found_cost:
            return found_targets, found_cost
        if p in visited or grid[p[0]][p[1]] != '.' or p in units_pos:
            continue
        visited.add(p)

        if p in targets:
            found_cost = cost
            found_targets.append(p)
        else:
            for n in neighbours(*p):
                q.append((n, cost+1))

    return found_targets, found_cost


def solve(input, power):
    grid = [list(line) for line in input]

    units = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            u = grid[y][x]
            if u == 'E':
                units.append(Unit(y, x, u, 200, power))
                grid[y][x] = '.'
            if u == 'G':
                units.append(Unit(y, x, u, 200, 3))
                grid[y][x] = '.'

    rounds = 0
    finished = False
    while not finished:
        units = sorted([u for u in units if u.hp > 0], key=lambda u: u.pos())
        for current in units:
            if current.hp <= 0:
                continue

            # check if there are enemies left
            enemies = [e for e in units if e.hp > 0 and current.unit != e.unit]
            if len(enemies) == 0:
                finished = True
                break

            # check if there are enemies in range
            enemies_in_range = [e for e in enemies if e.pos() in neighbours(*current.pos())]
            if len(enemies_in_range) == 0:
                # no enemies in range, lets move
                units_pos = [u.pos() for u in units if u.hp > 0]

                targets = set([])
                for e in enemies:
                    targets.update(neighbours(*e.pos()))
                targets = [t for t in targets if grid[t[0]][t[1]] == '.' and t not in units_pos]
                shortests, cost = shortest_paths(grid, units, current.pos(), targets)
                target = min(shortests, default=None)

                if target != None:
                    if target in neighbours(*current.pos()):
                        current.y, current.x = target
                    else:
                        for n in neighbours(*current.pos()):
                            if grid[n[0]][n[1]] == '.' and n not in units_pos:
                                _, n_cost = shortest_paths(grid, units, n, [target])
                                if n_cost == cost - 1:
                                    current.y, current.x = n
                                    break

                # Update range
                enemies_in_range = [e for e in enemies if e.pos() in neighbours(*current.pos())]

            # check if there are enemies in range
            if len(enemies_in_range) > 0:
                # attack
                enemy = reduce(select_enemy, enemies_in_range)
                enemy.hp -= current.attack_power
                if enemy.unit == 'E' and enemy.hp <= 0:
                    return False, 0
                pass

        if not finished:
            rounds += 1

    return True, rounds * sum([u.hp for u in units if u.hp > 0])

# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    power = 4
    while True:
        elves_win, score = solve(input, power)
        if elves_win:
            print(score)
            break
        power += 1
