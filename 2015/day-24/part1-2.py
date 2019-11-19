from itertools import combinations
from operator import mul

with open("input.txt", "r") as f:
    available_packages = sorted([int(x) for x in f.readlines()], reverse=True)


def quantum_entanglement(packages):
    return reduce(mul, packages, 1)


def fewest_packages(packages, compartments):
    total_weight = sum(packages)
    compartment_weight = total_weight / compartments

    for i in range(1, len(packages)):
        comb = combinations(packages, i)
        packs = [p for p in comb if sum(p) == compartment_weight]
        if len(packs) > 0:
            sorted(packs, key=quantum_entanglement)
            return quantum_entanglement(packs[0])


print "Part 1:", fewest_packages(available_packages, 3)
print "Part 2:", fewest_packages(available_packages, 4)
