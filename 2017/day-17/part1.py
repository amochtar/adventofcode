def solve(inp):
    circbuffer = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos + inp) % i + 1
        circbuffer.insert(pos, i)

    print("Part 1:", circbuffer[pos+1])


solve(386)
