with open('input.txt', 'r') as f:
    input = f.readlines()

ranges = []
for line in input:
    parts = line.strip().split('-')
    ranges.append((int(parts[0]), int(parts[1])))
ranges.sort()

# ranges = [(0,2),(4,7),(5,8)]

ip = 0
max_ip = 4294967295

for r in ranges:
    if r[0] > ip:
        break
    if r[1] > ip:
        ip = r[1]+1

print "Part 1:", ip
