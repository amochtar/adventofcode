with open("input.txt", "r") as f:
    lines = f.readlines()

checksum = 0
for line in lines:
    numbers = sorted(map(int, line.split()))
    checksum += numbers[-1] - numbers[0]

print("Part 1:", checksum)
