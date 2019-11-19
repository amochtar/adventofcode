def generator(x, fact, mod):
    nxt = x
    # http://mziccard.me/2015/05/08/modulo-and-division-vs-bitwise-operations/
    bitmod = mod - 1
    while True:
        nxt = nxt * fact % 2147483647
        if nxt & bitmod == 0:
            yield nxt


a = (634, 16807, 4)
b = (301, 48271, 8)

count = 0
matches = 0
for x, y in zip(generator(*a), generator(*b)):
    # compare only right 16 bits (2^16 - 1 = 65535)
    if x & 65535 == y & 65535:
        matches += 1
    count += 1
    if count > 5000000:
        break

print("Part 2:", matches)
