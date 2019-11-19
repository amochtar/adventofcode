with open("input.txt", "r") as f:
    lines = f.readlines()

print("Part 1:", len([l for l in lines if len(set(l.split())) == len(l.split())]))
