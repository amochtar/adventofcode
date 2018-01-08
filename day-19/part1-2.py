import re

with open("input.txt", "r") as f:
    lines = f.readlines()

medicine = lines[-1]
replacements = [r.strip().split(" => ") for r in lines[:-2]]


def gen_molecules(molecule):
    molecules = set()
    for fr, to in replacements:
        ix = [m.start() for m in re.finditer(fr, molecule)]
        for i in ix:
            gen_molecule = molecule[:i] + molecule[i:].replace(fr, to, 1)
            molecules.add(gen_molecule)
    return molecules


print("Part 1: " + str(len(gen_molecules(medicine))))


molecule = medicine
count = 0
while len(molecule) > 1:
    for fr, to in replacements:
        while to in molecule:
            count += molecule.count(to)
            print(molecule)
            molecule = molecule.replace(to, fr)

print("Part 2: " + str(count))
