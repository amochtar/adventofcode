from itertools import permutations

f = open("input.txt", "r")
input = f.readlines()
input = [i.strip() for i in input]

locations = set()
distances = {}

for i in input:
    fr, _, to, _, distance = i.split(' ')
    locations.add(fr)
    locations.add(to)
    distances[(fr, to)] = int(distance)
    distances[(to, fr)] = int(distance)


def dist(cities):
    d = 0
    fr = cities[0]
    for to in cities[1:]:
        d += distances[(fr, to)]
        fr = to
    return d


perms = [dist(cities) for cities in list(permutations(locations))]

print "Part 1:", min(perms)
print "Part 2:", max(perms)
