def parse(tree):
    num_childs = tree[0]
    num_metadata = tree[1]
    tree = tree[2:]

    total = 0
    for _ in range(num_childs):
        sum_meta, tree = parse(tree)
        total += sum_meta

    sum_meta = sum(tree[:num_metadata])
    total += sum_meta

    return (total, tree[num_metadata:])


def solve(input):
    tree = list(map(int, input[0].split()))
    print(parse(tree)[0])


with open('test.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)

# with open('input.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)
