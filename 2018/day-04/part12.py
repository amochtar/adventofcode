from collections import Counter
from collections import defaultdict


def solve(input):
    guard = None
    guards = defaultdict(Counter)
    asleep = None
    for line in sorted(input):
        parts = line.split()
        # date = parts[0][1:]
        time = int(parts[1][3:5])
        if parts[2] == 'Guard':
            guard = int(parts[3][1:])
        elif parts[2] == 'falls':
            asleep = time
        elif parts[2] == 'wakes':
            awake = time
            for i in range(asleep, awake):
                guards[guard][i] += 1

    max_sleep = 0
    g = None
    for k, v in guards.items():
        sleep = sum(v.values())
        if sleep > max_sleep:
            max_sleep = sleep
            g = k
    print(g, g * guards[g].most_common(1)[0][0])

    max_sleep = 0
    g = None
    m = None
    for k, v in guards.items():
        (minute, sleep) = v.most_common(1)[0]
        if sleep > max_sleep:
            max_sleep = sleep
            g = k
            m = minute
    print(g, g * m)



# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
