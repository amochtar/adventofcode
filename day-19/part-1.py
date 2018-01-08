with open('input.txt', 'r') as f:
    input = int(f.read())

elves = range(1, input+1)
num_elves = len(elves)
while num_elves > 1:
    elves = elves[::2]
    if num_elves % 2 == 1:
        elves = elves[1:]
    num_elves = len(elves)

print elves[0]
