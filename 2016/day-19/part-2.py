with open('input.txt', 'r') as f:
    input = int(f.read())


class Elf:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.prev = None

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def __repr__(self):
        return "Elf(id=%r, next=%s, prev=%s)" % (self.id, self.next, self.prev)

    def __str__(self):
        return "Elf(id=%r)" % (self.id)


elves = map(Elf, xrange(1, input+1))
for i in xrange(input):
    elves[i].next = elves[(i+1) % input]
    elves[i].prev = elves[(i-1) % input]

start = elves[0]
middle = elves[input//2]

for i in xrange(1, input):
    middle.delete()
    middle = middle.next
    if i % 2 == 1:
        middle = middle.next
    start = start.next

print start.id
