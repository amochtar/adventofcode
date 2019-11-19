import re


class Unit(object):
    def __init__(self, t, count, hp, weak_to, immune_to, damage, damage_type, initiative):
        self.t = t
        self.count = count
        self.hp = hp
        self.weak_to = weak_to
        self.immune_to = immune_to
        self.damage = damage
        self.damage_type = damage_type
        self.initiative = initiative

    def __repr__(self):
        return '{}: {} units each with {} hit points (weak to {}; immune to {}) with an attack that does {} {} damage at initiative {}'.format(
            self. t,
            self.count,
            self.hp,
            self.weak_to,
            self.immune_to,
            self.damage,
            self.damage_type,
            self.initiative
        )

    def __str__(self):
        return '{}: {}c {}hp {}p {}i {}d'.format(
            self. t,
            str(self.count).rjust(5),
            str(self.hp).rjust(5),
            str(self.power()).rjust(6),
            str(self.initiative).rjust(3),
            str(self.damage).rjust(5),
        )

    def power(self):
        return self.count*self.damage

    def calc_damage(self, target):
        damage_done = 0
        if self.damage_type in target.weak_to:
            damage_done = 2*self.power()
        elif self.damage_type not in target.immune_to:
            damage_done = self.power()
        return damage_done

    def attack(self, target):
        damage_done = self.calc_damage(target)

        units_to_kill = min(target.count, damage_done // target.hp)
        target.count -= units_to_kill

    def alive(self):
        return self.count > 0


re_unit = re.compile(r'(\d+) units each with (\d+) hit points (?:\(([^)]*)\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)')


def parse_unit(t, line):
    m = re.match(re_unit, line)
    if not m:
        return None

    count, hp, weak_immune, damage, damage_type, initiative = m.groups()
    weak_to = []
    immune_to = []
    if weak_immune:
        for wi in weak_immune.split('; '):
            parts = wi.split()
            if parts[0] == 'weak':
                weak_to = [p.rstrip(',') for p in parts[2:]]
            if parts[0] == 'immune':
                immune_to = [p.rstrip(',') for p in parts[2:]]
    return Unit(t, int(count), int(hp), weak_to, immune_to, int(damage), damage_type, int(initiative))


def solve(input):
    groups = []
    t = 'imm'
    for line in input:
        if line.startswith('Infection'):
            t = 'inf'
        unit = parse_unit(t, line)
        if unit != None:
            groups.append(unit)

    round = 1
    while True:
        print('Round', round)
        imm_alive = [u for u in groups if u.t == 'imm' and u.alive()]
        inf_alive = [u for u in groups if u.t == 'inf' and u.alive()]
        if len(imm_alive) == 0 or len (inf_alive) == 0:
            break

        groups = sorted(groups, key=lambda u: (-u.power(),-u.initiative))
        for u in groups:
            print(u)
        print()

        print('Target selection')
        battles = []
        for u in groups:
            if u.alive():
                print('Attacker:', str(u))
                targets_available = [t for t in groups if t not in [b[1] for b in battles] and t.alive() and t.t != u.t and u.calc_damage(t)>0]
                targets_available = sorted(targets_available, key=lambda t: (u.calc_damage(t), t.power(), t.initiative))
                target = None
                if len(targets_available) > 0:
                    target = targets_available.pop()
                    battles.append((u, target))
                print('Target:  ', str(target))
        print()

        print('Attacking')
        battles = sorted(battles, key=lambda b: -b[0].initiative)
        for attacker, defender in battles:
            print('Attacker', attacker)
            print('Defender', defender)
            damage = attacker.calc_damage(defender)
            count_before = defender.count
            attacker.attack(defender)
            count_after = defender.count
            print('Damage      ', damage)
            print('Units killed', count_before - count_after)
            print()
            if not defender.alive():
                groups.remove(defender)

        round += 1

    print(sum(u.count for u in groups))


# with open('test.txt', 'r') as f:
#     input = f.readlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.readlines()
    solve(input)

