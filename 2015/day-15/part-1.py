import re
from collections import namedtuple

with open('input.txt', 'r') as f:
    input = f.readlines()

ingredient_pattern = re.compile(r'([^:]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
Ingredient = namedtuple('Ingredient', ['name', 'capacity', 'durability', 'flavor', 'texture', 'calories'])

max_teaspoons = 100
ingredients = []
for line in input:
    i = ingredient_pattern.match(line)
    ingredients.append(Ingredient(name=i.group(1), capacity=int(i.group(2)), durability=int(i.group(3)), flavor=int(i.group(4)), texture=int(i.group(5)), calories=int(i.group(6))))

print ingredients

max_score = 0
for a in range(max_teaspoons):
    for b in range(max_teaspoons-a):
        for c in range(max_teaspoons-a-b):
            d = max_teaspoons - a - b - c
            mix = [a, b, c, d]

            calories = sum([k*l for (k, l) in zip(mix, [w.calories for w in ingredients])])
            if calories != 500:
                continue

            capacity_score = max(0, sum([k*l for (k, l) in zip(mix, [w.capacity for w in ingredients])]))
            durability_score = max(0, sum([k*l for (k, l) in zip(mix, [w.durability for w in ingredients])]))
            flavor_score = max(0, sum([k*l for (k, l) in zip(mix, [w.flavor for w in ingredients])]))
            texture_score = max(0, sum([k*l for (k, l) in zip(mix, [w.texture for w in ingredients])]))
            score = capacity_score * durability_score * flavor_score * texture_score
            max_score = max(max_score, score)

print max_score
