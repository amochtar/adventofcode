with open('input.txt', 'r') as f:
    input = f.readlines()

scan = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


sues = {}
for line in input:
    parts = line.replace(':', '').replace(',', '').split(' ')
    sues[parts[1]] = {parts[i]: int(parts[i+1]) for i in range(2, len(parts), 2)}


def is_sue(s):
    return all(scan[k] == v for k, v in s.iteritems())


def is_sue2(s):
    for k, v in sue.iteritems():
        if k in ['cats', 'trees']:
            if v > scan[k]:
                continue
            return False
        elif k in ['pomeranians', 'goldfish']:
            if v < scan[k]:
                continue
            return False
        elif scan[k] != v:
            return False
    return True


print "Part 1:", [i for i, sue in sues.iteritems() if is_sue(sue)]
print "Part 2:", [i for i, sue in sues.iteritems() if is_sue2(sue)]
