from collections import namedtuple
from collections import Counter

with open('input.txt', 'r') as f:
    input = f.readlines()

Reindeer = namedtuple('Reindeer', ['name', 'speed', 'run_time', 'rest_time'])

duration = 2503
reindeer = []

for line in input:
    parts = line.split(' ')
    reindeer.append(Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[-2])))


def distance(reindeer, duration):
    cycle_time = reindeer.run_time + reindeer.rest_time
    return (duration / cycle_time * reindeer.run_time + min(reindeer.run_time, duration % cycle_time)) * reindeer.speed


print "Part 1:", max([distance(r, duration) for r in reindeer])


scores = Counter()
for t in range(1, duration):
    distances = [(r.name, distance(r, t)) for r in reindeer]
    max_d = max(distances, key=lambda item: item[1])[1]
    for (n, d) in distances:
        if d == max_d:
            scores[n] += 1

print "Part 2:", scores.most_common()[0]
