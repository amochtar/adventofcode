f = open("input.txt", "r")
input = f.readlines()
boxes = ([sorted(map(int, x.split('x'))) for x in input])

paper = 0
ribbon = 0
for (l, w, h) in boxes:
    sides = [l*w, w*h, h*l]
    paper += 2 * sum(sides) + min(sides)
    ribbon += 2*(l+w) + l*w*h

print "Part 1: paper", paper
print "Part 2: ribbon", ribbon
