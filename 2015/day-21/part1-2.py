from collections import namedtuple
import itertools

Player = namedtuple('player', ['name', 'hp', 'damage', 'armor'])
Item = namedtuple('item', ['name', 'cost', 'damage', 'armor'])

weapons = [
    Item(name='Dagger', cost=8, damage=4, armor=0),
    Item(name='Shortsword', cost=10, damage=5, armor=0),
    Item(name='Warhammer', cost=25, damage=6, armor=0),
    Item(name='Longsword', cost=40, damage=7, armor=0),
    Item(name='Greataxe', cost=74, damage=8, armor=0),
]

armor = [
    Item(name='Leather', cost=13, damage=0, armor=1),
    Item(name='Chainmail', cost=31, damage=0, armor=2),
    Item(name='Splintmail', cost=53, damage=0, armor=3),
    Item(name='Bandedmail', cost=75, damage=0, armor=4),
    Item(name='Platemail', cost=102, damage=0, armor=5),
]

rings = [
    Item(name='Damage +1', cost=25, damage=1, armor=0),
    Item(name='Damage +2', cost=50, damage=2, armor=0),
    Item(name='Damage +3', cost=100, damage=3, armor=0),
    Item(name='Defense +1', cost=20, damage=0, armor=1),
    Item(name='Defense +2', cost=40, damage=0, armor=2),
    Item(name='Defense +3', cost=80, damage=0, armor=3),
]

plyr = Player(name='Plyr', hp=100, damage=0, armor=0)
boss = Player(name='Boss', hp=103, damage=9, armor=2)


def gear_permutations():
    w = list(itertools.combinations(weapons, 1))
    a = list(itertools.combinations(armor, 0)) + list(itertools.combinations(armor, 1))
    r = list(itertools.combinations(rings, 0)) + list(itertools.combinations(rings, 1)) + list(itertools.combinations(rings, 2))

    perms = itertools.product(w, a, r)
    return [[item for gear in perm for item in gear if item] for perm in perms]


def attack(attacker, defender):
    return Player(
        name=defender.name,
        hp=defender.hp - max(attacker.damage - defender.armor, 1),
        damage=defender.damage,
        armor=defender.armor,
    )


def player_with_gear(player, gear):
    p = player
    for g in gear:
        p = Player(
            name=p.name,
            hp=p.hp,
            damage=p.damage + g.damage,
            armor=p.armor + g.armor,
        )
    return p


def gear_cost(gear):
    return sum([g.cost for g in gear])


gear_perms = sorted(gear_permutations(), key=gear_cost)
for gear in gear_perms:
    attacker = player_with_gear(plyr, gear)
    defender = boss

    while attacker.hp > 0 and defender.hp > 0:
        defender = attack(attacker, defender)
        attacker, defender = defender, attacker

    if attacker.hp <= 0 and attacker.name == 'Boss':
        print "Part 1:", gear_cost(gear)
        break


gear_perms = sorted(gear_permutations(), key=gear_cost, reverse=True)
for gear in gear_perms:
    attacker = player_with_gear(plyr, gear)
    defender = boss

    while attacker.hp > 0 and defender.hp > 0:
        defender = attack(attacker, defender)
        attacker, defender = defender, attacker

    if attacker.hp <= 0 and attacker.name == 'Plyr':
        print "Part 2:", gear_cost(gear)
        break
