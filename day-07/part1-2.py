def branch_weight(tree, branch):
    w = 0
    w, children = tree[branch]
    w += sum(branch_weight(tree, child)[1] for child in children)
    return (branch, w)


def solve(inp):
    tree = {}
    all_children = []
    for line in inp:
        parts = line.strip().split(' -> ')
        parent = parts[0].split()[0]
        try:
            children = parts[1].split(', ')
            all_children += children
        except IndexError:
            children = []
        weight = int(parts[0].split()[1][1:-1])
        tree[parent] = (weight, children)

    root = None
    for parent in tree.keys():
        if parent not in all_children:
            root = parent
            break
    print("Part 1:", root)

    prog = root
    while True:
        w, children = tree[prog]
        branches = sorted([branch_weight(tree, child) for child in children], key=lambda x: x[1])
        if branches[0][1] != branches[1][1]:
            prog = branches[0][0]
            diff = branches[0][1] - branches[1][1]
        elif branches[-1][1] != branches[1][1]:
            prog = branches[-1][0]
            diff = branches[-1][1] - branches[1][1]
        else:
            break

    return w - diff


with open('input.txt', 'r') as f:
    inp = f.readlines()

print("Part 2:", solve(inp))
