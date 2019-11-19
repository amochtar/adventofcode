class Particle(object):
    def __init__(self, i, p, v, a):
        self.i = i
        self.p = p
        self.v = v
        self.a = a

    def distance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

    def move(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.v[2] += self.a[2]
        self.p[0] += self.v[0]
        self.p[1] += self.v[1]
        self.p[2] += self.v[2]


def solve(lines):
    particles = []
    for i, line in enumerate(lines):
        pos, vel, acc = line.split(', ')
        p = list(map(int, pos[3:-1].split(',')))
        v = list(map(int, vel[3:-1].split(',')))
        a = list(map(int, acc[3:-1].split(',')))
        particles.append(Particle(i=i, p=p, v=v, a=a))

    order = [part.i for part in sorted(particles, key=lambda p: p.distance())]
    while True:
        for part in particles:
            part.move()

        seen = []
        to_remove = []
        for part in particles:
            if part.p in seen:
                to_remove.append(part.p)
            else:
                seen.append(part.p)
        particles = [part for part in particles if part.p not in to_remove]

        new_order = [part.i for part in sorted(particles, key=lambda p: p.distance())]
        if order == new_order:
            break
        order = new_order

    print("Part 2:", len(particles))


with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    solve(lines)
