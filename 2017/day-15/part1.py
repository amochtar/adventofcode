def generator(x, fact):
    nxt = x
    while True:
        nxt = nxt * fact % 2147483647
        yield nxt


a = (634, 16807)
b = (301, 48271)

count = 0
matches = 0
for x, y in zip(generator(*a), generator(*b)):
    # compare only right 16 bits (2^16 - 1 = 65535)
    if x & 65535 == y & 65535:
        matches += 1
    count += 1
    if count > 40000000:
        break

print("Part 1:", matches)
