from collections import namedtuple
from collections import deque

fav = 1358
target = (31, 39)

State = namedtuple('state', ['steps', 'location'])

maze = {}
visited = []


def is_valid(state):
    if any(i < 0 for i in state.location):
        return False

    x = state.location[0]
    y = state.location[1]

    bits = [int(s) for s in str(bin(x*x + 3*x + 2*x*y + y + y*y + fav))[2:]]
    is_open = sum(bits) % 2 == 0

    maze[state.location] = is_open

    return is_open


def done(state):
    return state.location == target


def next_states(state):
    next_states = []
    for i in [1, -1]:
        new_x = State(steps=state.steps+1, location=(state.location[0] + i, state.location[1]))
        new_y = State(steps=state.steps+1, location=(state.location[0], state.location[1] + i))
        if is_valid(new_x):
            next_states.append(new_x)
        if is_valid(new_y):
            next_states.append(new_y)
    return next_states


has_part_1 = False
has_part_2 = False
initial_state = State(steps=0, location=(1, 1))
q = deque([initial_state])
while q:
    s = q.popleft()

    if not has_part_2 and s.steps > 50:
        print "Part 2:", len(visited)
        has_part_2 = True
    if not has_part_1 and done(s):
        print "Part 1:", s.steps
        has_part_1 = True

    if has_part_1 and has_part_2:
        break

    if s.location in visited:
        continue
    else:
        visited.append(s.location)

    for next_s in next_states(s):
        q.append(next_s)
