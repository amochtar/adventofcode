def parse(tree):
    num_childs = tree[0]
    num_metadata = tree[1]
    tree = tree[2:]

    total = 0
    values = []
    for _ in range(num_childs):
        sum_meta, value, tree = parse(tree)
        values.append(value)
        total += sum_meta

    sum_meta = sum(tree[:num_metadata])
    total += sum_meta

    if num_childs == 0:
        value = sum_meta
    else:
        value = 0
        for m in tree[:num_metadata]:
            idx = m - 1
            if idx >= 0 and idx < len(values):
                value += values[idx]

    return (total, value, tree[num_metadata:])


def solve(input):
    tree = list(map(int, input[0].split()))
    print(parse(tree)[1])


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
