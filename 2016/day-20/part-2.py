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
count = 0
for r in ranges:
    if r[0] > ip:
        count += r[0] - ip
    if r[1] > ip:
        ip = min(max_ip, r[1]+1)
else:
    count += max_ip - ip

print "Part 2:", count
