from heapq import heappop, heappush
from collections import namedtuple

Player = namedtuple('player', ['hp', 'armor', 'mana'])
Boss = namedtuple('boss', ['hp', 'damage'])
Spell = namedtuple('spell', ['name', 'cost', 'damage', 'heal', 'armor', 'poison', 'recharge', 'turns'])

spells = [
    Spell(name='Magic Missile', cost=53, damage=4, heal=0, armor=0, poison=0, recharge=0, turns=0),
    Spell(name='Drain', cost=73, damage=2, heal=2, armor=0, poison=0, recharge=0, turns=0),
    Spell(name='Shield', cost=113, damage=0, heal=0, armor=7, poison=0, recharge=0, turns=6),
    Spell(name='Poison', cost=173, damage=0, heal=0, armor=0, poison=3, recharge=0, turns=6),
    Spell(name='Recharge', cost=229, damage=0, heal=0, armor=0, poison=0, recharge=101, turns=5),
]
effects = []


def debug(message):
    if debug_enabled:
        print message


def boss_attack(player, boss):
    armor = ''
    if player.armor > 0:
        armor = ' - ' + str(player.armor)
    debug('Boss attacks for ' + str(boss.damage) + armor + ' damage!')
    return Player(
        hp=player.hp - max(boss.damage - player.armor, 1),
        armor=player.armor,
        mana=player.mana,
    ), boss


def apply_effects(player, boss, effects):
    p = Player(hp=player.hp, armor=0, mana=player.mana)
    b = boss
    es = []
    for e in effects:
        p = Player(hp=p.hp, armor=p.armor + e.armor, mana=p.mana + e.recharge)
        b = Boss(hp=b.hp - e.poison, damage=b.damage)
        effect = Spell(name=e.name, cost=e.cost, damage=e.damage, heal=e.heal, armor=e.armor, poison=e.poison, recharge=e.recharge, turns=e.turns - 1)
        effect_str = e.name
        if effect.poison > 0:
            effect_str += ' deals ' + str(effect.poison) + ' damage'
        elif effect.armor > 0:
            effect_str += '\'s active, armor +' + str(effect.armor)
        elif effect.recharge > 0:
            effect_str += ' provides ' + str(effect.recharge) + ' mana'
        effect_str += '; its timer is now ' + str(effect.turns) + '.'
        debug(effect_str)
        if effect.turns > 0:
            es.append(effect)
        else:
            debug(effect.name + ' wears off.')

    return p, b, es


def cast_spell(player, boss, effects, spell):
    damage = ''
    if spell.damage > 0:
        boss = Boss(hp=boss.hp - spell.damage, damage=boss.damage)
        damage = ', dealing ' + str(spell.damage) + ' damage'
    if spell.heal > 0:
        player = Player(hp=player.hp + spell.heal, armor=player.armor, mana=player.mana)
        damage += ', and healing ' + str(spell.damage) + ' hit points'
    player = Player(hp=player.hp, armor=player.armor, mana=player.mana - spell.cost)
    debug('Player casts ' + spell.name + damage + '.')
    if spell.turns > 0:
        effects.append(spell)
    return player, boss, effects


def print_stats(player, boss, effects):
    shields = sum([e.armor for e in effects])
    debug('- Player has %d hit points, %d armor, %d mana' % (player.hp, shields, player.mana))
    debug('- Boss has %d hit points' % (boss.hp))


def finished(player, boss):
    if player.hp <= 0:
        debug('Player is dead, boss wins')
        return True
    elif player.mana < 0:
        debug('Player out of mana, boss wins')
        return True
    elif boss.hp <= 0:
        debug('Boss is dead, player wins')
        return True
    return False


def turn(player, boss, effects, spell, hard):
    debug('')
    debug('-- Player turn --')
    if hard:
        debug('Hard mode; player loses 1 hit point.')
        player = Player(hp=player.hp-1, armor=player.armor, mana=player.mana)
    print_stats(player, boss, effects)
    if player.hp <= 0:
        return player, boss, effects
    player, boss, effects = apply_effects(player, boss, effects)
    if finished(player, boss):
        return player, boss, effects
    player, boss, effects = cast_spell(player, boss, effects, spell)
    if finished(player, boss):
        return player, boss, effects

    debug('')
    debug('-- Boss turn --')
    print_stats(player, boss, effects)
    player, boss, effects = apply_effects(player, boss, effects)
    if finished(player, boss):
        return player, boss, effects
    player, boss = boss_attack(player, boss)
    if finished(player, boss):
        return player, boss, effects
    return player, boss, effects


def play_game(part, hard=False):
    player = Player(hp=50, armor=0, mana=500)
    boss = Boss(hp=55, damage=8)
    q = []
    for spell in spells:
        heappush(q, (spell.cost, (player, boss, [], [spell.name], spell)))

    seen = set()
    while q:
        mana_spent, (player, boss, effects, spells_cast, spell) = heappop(q)
        effects_hash = tuple((e.name, e.turns) for e in effects)
        if (mana_spent, player, boss, effects_hash, spell) in seen:
            continue
        else:
            seen.add((mana_spent, player, boss, effects_hash, spell))
        debug('Mana spent: ' + str(mana_spent) + '; Casting spell: ' + spell.name)
        player, boss, effects = turn(player, boss, effects, spell, hard)
        if player.hp <= 0 or player.mana < 0:
            continue
        if boss.hp <= 0:
            print('Part ' + str(part) + ': ' + str(mana_spent))
            print spells_cast
            return

        for spell in spells:
            if spell.name not in [e.name for e in effects if e.turns > 1]:
                sc = spells_cast[:]
                sc.append(spell.name)
                heappush(q, (mana_spent + spell.cost, (player, boss, effects[:], sc, spell)))


debug_enabled = False
play_game(part=1, hard=False)
play_game(part=2, hard=True)
