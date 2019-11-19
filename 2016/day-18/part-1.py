with open('input.txt', 'r') as f:
    input = f.read()

row = [c == '^' for c in input]
count_safe = row.count(False)


def next_row(row):
    next_row = []
    for i, c in enumerate(row):
        if i == 0:
            left = False
        else:
            left = row[i-1]
        if i == len(row) - 1:
            right = False
        else:
            right = row[i+1]

        next_row.append(left != right)
    return next_row


for r in range(400000-1):
    row = next_row(row)
    count_safe += row.count(False)
    if r == (40 - 1 - 1):
        print "Part 1:", count_safe

print "Part 2:", count_safe
