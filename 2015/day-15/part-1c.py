import re
import itertools
import collections

with open('input.txt', 'r') as f:
    input = f.readlines()

ingredient_pattern = re.compile(r'([^:]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
Ingredient = collections.namedtuple('Ingredient', ['name', 'capacity', 'durability', 'flavor', 'texture', 'calories'])


def seq(n, k, j=0):  # -> Iterable[Sequence[int]]:
    r"""Return k-element product from [0, n] range that sums up to n.
    >>> sorted(map(tuple, seq(3, 2)))
    [(0, 3), (1, 2), (2, 1), (3, 0)]
    """
    if k <= 1:
        yield collections.deque([n-j])
        raise StopIteration
    for i in range(n+1-j):
        for a, lst in itertools.product((i, ), seq(n, k-1, j+i)):
            lst.append(a)
            yield lst


max_teaspoons = 100
ingredients = []
for line in input:
    i = ingredient_pattern.match(line)
    ingredients.append(Ingredient(name=i.group(1), capacity=int(i.group(2)), durability=int(i.group(3)), flavor=int(i.group(4)), texture=int(i.group(5)), calories=int(i.group(6))))

print ingredients

max_score = 0

for combi in seq(max_teaspoons, len(ingredients)):
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for i, v in enumerate(combi):
        ingredient = ingredients[i]
        capacity += v * ingredient.capacity
        durability += v * ingredient.durability
        flavor += v * ingredient.flavor
        texture += v * ingredient.texture
        calories += v * ingredient.calories

    if calories != 500:
        continue

    score = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
    max_score = max(max_score, score)

print max_score
