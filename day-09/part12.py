from collections import defaultdict
from collections import deque


def play(num_elves, max_marble):
    elves = defaultdict(int)

    marble = 0
    marbles = deque([marble])
    elf = 0

    while marble <= max_marble:
        marble += 1
        if marble % 23 == 0:
            elves[elf] += marble
            marbles.rotate(-7)
            elves[elf] += marbles.popleft()
            marbles.rotate(1)
        else:
            marbles.rotate(1)
            marbles.appendleft(marble)
            pass

        elf = (elf+1) % num_elves

    print(max(elves.values()))


def solve(input):
    parts = input[0].split()
    num_elves = int(parts[0])
    max_marble = int(parts[6])

    play(num_elves, max_marble)
    play(num_elves, max_marble*100)


# with open('test.txt', 'r') as f:
#     input = f.read().splitlines()
#     solve(input)

with open('input.txt', 'r') as f:
    input = f.read().splitlines()
    solve(input)
