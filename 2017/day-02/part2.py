from itertools import combinations

with open("input.txt", "r") as f:
    lines = f.readlines()

checksum = 0
for line in lines:
    numbers = sorted(map(int, line.split()))
    for pair in combinations(numbers, 2):
        div, rem = divmod(pair[1], pair[0])
        if rem == 0:
            checksum += div

print("Part 2:", checksum)
