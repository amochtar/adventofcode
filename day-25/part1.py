import networkx as nx


def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3])


def solve(input):
    points = []
    for line in input:
        a,b,c,d = line.split(',')
        points.append((int(a), int(b), int(c), int(d)))

    G = nx.Graph()

    for p in points:
        for q in points:
            if manhattan(p, q) <= 3:
                G.add_edge(p, q)

    print(nx.number_connected_components(G))


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
