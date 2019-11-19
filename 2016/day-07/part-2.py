import regex as re

with open("input.txt", "r") as f:
    ips = [x.strip() for x in f.readlines()]

aba = re.compile(r'([a-z])(?!\1)([a-z])\1')

count = 0
for ip in ips:
    components = re.split('[][]', ip)
    supernets = components[::2]
    hypernets = components[1::2]
    m = set(aba.findall(" ".join(supernets), overlapped=True))
    for (first, second) in m:
        if ("%s%s%s" % (second, first, second)) in " ".join(hypernets):
            count += 1
            break

print count
