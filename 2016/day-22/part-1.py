import copy
from itertools import permutations
from collections import defaultdict
from collections import namedtuple
# from collections import deque
import re

State = namedtuple('State', ['steps', 'nodes'])
Node = namedtuple('Node', ['location', 'size', 'used', 'avail'])
node_pattern = re.compile(r'.+?-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%')

with open("input.txt", "r") as f:
    input = [x.strip() for x in f.readlines() if x.startswith('/dev')]

nodes = defaultdict(dict)
for line in input:
    match = node_pattern.match(line)
    x = int(match.group(1))
    y = int(match.group(2))
    size = int(match.group(3))
    used = int(match.group(4))
    avail = int(match.group(5))
    nodes[y][x] = Node(location=(x, y), size=size, used=used, avail=avail)

pairs = permutations([n for nl in nodes.values() for n in nl.values()], 2)
moves = [pair for pair in pairs
         if pair[1].used == 0 and pair[1].avail >= pair[0].used]
print 'Part 1:', len(moves)


def adjecent(pair):
    if pair[0].location[0] == pair[1].location[0] and abs(pair[0].location[1] - pair[1].location[1]) == 1:
        return True
    elif pair[0].location[1] == pair[1].location[1] and abs(pair[0].location[0] - pair[1].location[0]) == 1:
        return True
    return False


def next_states(state):
    next_states = []
    pairs = permutations([n for nl in state.nodes.values() for n in nl.values()], 2)
    valid_moves = [(pair[0].location, pair[1].location) for pair in pairs
                   if pair[0].used > 0 and pair[1].avail >= pair[0].used and adjecent(pair)]
    print valid_moves
    for pair in valid_moves:
        nodes = copy.deepcopy(state.nodes)
        to_node = nodes[pair[1][1]][pair[1][0]]
        from_node = nodes[pair[0][1]][pair[0][0]]
        nodes[pair[1][1]][pair[1][0]] = Node(location=to_node.location, size=to_node.size, used=to_node.used+from_node.used, avail=to_node.avail-from_node.used)
        nodes[pair[0][1]][pair[0][0]] = Node(location=from_node.location, size=from_node.size, used=0, avail=from_node.size)
        next_states.append(State(steps=state.steps+1, nodes=nodes))
    return next_states


def done(state):
    return True


def print_nodes(nodes):
    for y, nl in nodes.iteritems():
        line = ''
        for x, node in nl.iteritems():
            if y == 0 and x == 0:
                line += '(.)'
            elif y == 0 and x == len(nl)-1:
                line += ' G '
            elif node.used == 0:
                line += ' _ '
            elif node.size > 100:
                line += ' # '
            else:
                line += ' . '
        print line


print 'Part 2:'
print_nodes(nodes)

# initial_state = State(steps=0, nodes=nodes)
# next_states(initial_state)
# visited = []
# q = deque([initial_state])
# while q:
#     s = q.popleft()
#     print len(q)
#     # if done(s):
#     #     print "Part 2: ", s.steps

#     if s.nodes in visited:
#         continue
#     visited.append(s.nodes)
#     q.extend(next_states(s))
# else:
#     print "Failed..."
