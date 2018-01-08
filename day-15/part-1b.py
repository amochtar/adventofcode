import re
from collections import Counter
from collections import namedtuple
from itertools import combinations_with_replacement

with open('input.txt', 'r') as f:
    input = f.readlines()

ingredient_pattern = re.compile(r'([^:]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
Ingredient = namedtuple('Ingredient', ['capacity', 'durability', 'flavor', 'texture', 'calories'])

max_teaspoons = 100
ingredients = {}
for line in input:
    i = ingredient_pattern.match(line)
    ingredients[i.group(1)] = Ingredient(capacity=int(i.group(2)), durability=int(i.group(3)), flavor=int(i.group(4)), texture=int(i.group(5)), calories=int(i.group(6)))

print ingredients

max_score = 0

for combi in combinations_with_replacement(ingredients.keys(), max_teaspoons):
    mix = Counter(combi)
    if len(mix) != len(ingredients):
        continue

    calories = 0
    for name in sorted(ingredients):
        calories += mix[name] * ingredients[name].calories
    if calories != 500:
        continue

    capacity_score, durability_score, flavor_score, texture_score = 0, 0, 0, 0
    for name in sorted(ingredients):
        capacity_score += mix[name] * ingredients[name].capacity
        durability_score += mix[name] * ingredients[name].durability
        flavor_score += mix[name] * ingredients[name].flavor
        texture_score += mix[name] * ingredients[name].texture
    score = max(0, capacity_score) * max(0, durability_score) * max(0, flavor_score) * max(0, texture_score)
    max_score = max(max_score, score)

print max_score
