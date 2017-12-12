import networkx as nx


def solve(inp):
    graph = nx.Graph()

    for line in inp:
        node, children = line.strip().split(' <-> ')
        graph.add_edges_from((node, child) for child in children.split(', '))

    print("Part 1:", len(nx.node_connected_component(graph, '0')))
    print("Part 2:", nx.number_connected_components(graph))


with open('input.txt', 'r') as f:
    inp = f.readlines()
    solve(inp)
