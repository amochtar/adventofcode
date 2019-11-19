def solve(inp):
    pos = 0
    val_after_0 = 0
    for i in range(1, 50000001):
        pos = (pos+inp) % i + 1
        if pos == 1:
            val_after_0 = i

    print("Part 2:", val_after_0)


solve(386)
