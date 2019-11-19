with open('input.txt', 'r') as f:
    jumps = list(map(int, f.readlines()))

list_size = len(jumps)

steps = 0
i = 0
while i >= 0 and i < list_size:
    jump = jumps[i]
    if jump >= 3:
        jumps[i] -= 1
    else:
        jumps[i] += 1
    i += jump
    steps += 1

print("Part 2:", steps)
