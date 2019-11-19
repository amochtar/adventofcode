f = open("input.txt", "r")
input = f.read()

floor = 0
for i in range(len(input)):
    if input[i] == '(':
        floor += 1
    elif input[i] == ')':
        floor -= 1

    if floor == -1:
        print "part 2: floor -1 at", i + 1

print floor
