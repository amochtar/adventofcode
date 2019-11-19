with open("input.txt", "r") as f:
    lines = f.readlines()

print("Part 2:", len([l for l in lines if len(set([''.join(sorted(word)) for word in l.split()])) == len(l.split())]))
