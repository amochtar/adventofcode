import hashlib
from collections import namedtuple
from collections import deque

passcode = 'edjrjqaa'
target = (3, 3)

State = namedtuple('state', ['path', 'location'])

maze = {}
visited = []

moves = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}


def is_valid(state):
    if any(i < 0 or i > 3 for i in state.location):
        return False

    return True


def done(state):
    return state.location == target


def get_open_doors(path):
    md5 = hashlib.md5(passcode + path).hexdigest()
    doors = zip('UDLR', [True if ord(c) >= ord('b') else False for c in md5[:4]])
    return [d[0] for d in doors if d[1]]


def next_states(state):
    open_doors = get_open_doors(state.path)
    next_states = []
    for d in open_doors:
        next_state = State(path=state.path+d, location=(state.location[0] + moves[d][0], state.location[1] + moves[d][1]))
        if is_valid(next_state):
            next_states.append(next_state)
    return next_states


has_part_1 = False
has_part_2 = False
initial_state = State(path='', location=(0, 0))
q = deque([initial_state])
longest = 0
while q:
    s = q.popleft()

    if not has_part_1 and done(s):
        print "Part 1:", s.path
        has_part_1 = True

    if done(s):
        print s
        longest = max(longest, len(s.path))
        continue

    for next_s in next_states(s):
        q.append(next_s)
else:
    print "Part 2:", longest
