from itertools import permutations
from collections import defaultdict

with open('input2.txt', 'r') as f:
    input = f.readlines()

people = defaultdict(dict)

for line in input:
    line = line.strip().replace('lose ', '-').replace('gain ', '').replace('.', '')
    parts = line.split(' ')
    people[parts[0]][parts[-1]] = int(parts[2])

max_happiness = 0
max_perm = None
for perm in permutations(sorted(people)[1:]):
    order = (sorted(people)[0],) + perm
    happiness = 0
    for i in range(len(order)):
        happiness += people[order[i]][order[i-1]]
        happiness += people[order[i-1]][order[i]]
    if happiness > max_happiness:
        max_happiness = happiness
        max_perm = perm

print max_perm, max_happiness
