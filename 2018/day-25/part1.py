import networkx as nx

def manhattan(p, q):
    return sum(abs(i-j) for i, j in zip(p, q))

points = []
for line in open('input.txt').readlines():
    points.append(tuple(map(int, line.split(','))))

spacetime = nx.Graph()
for p in points:
    for q in points:
        if manhattan(p, q) <= 3:
            spacetime.add_edge(p, q)

print(nx.number_connected_components(spacetime))
