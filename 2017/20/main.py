import re


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    particles = list()
    for i, line in enumerate(lines):
        p = re.match(
            r'^p=<(.+),(.+),(.+)>, v=<(.+),(.+),(.+)>, a=<(.+),(.+),(.+)>$',
            line,
        ).groups()
        p = [int(n) for n in p]
        particles.append([i, *p])

    particles.sort(key=lambda x: abs(x[1]) + abs(x[2]) + abs(x[3]))
    particles.sort(key=lambda x: abs(x[4]) + abs(x[5]) + abs(x[6]))
    particles.sort(key=lambda x: abs(x[7]) + abs(x[8]) + abs(x[9]))

    return particles[0][0]


class Particle:

    def __init__(self, values):
        self.id = values[0]
        self.pos = values[1:4]
        self.v = values[4:7]
        self.a = values[7:10]

    def tick(self):
        self.v = list(map(lambda x, y: x+y, self.v, self.a))
        self.pos = list(map(lambda x, y: x+y, self.pos, self.v))

    def __eq__(self, other):
        return self.pos == other.pos

    def __str__(self):
        return f"{self.id=} {self.pos=} {self.v=} {self.a=}"


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    particles = list()
    for i, line in enumerate(lines):
        p = re.match(
            r'^p=<(.+),(.+),(.+)>, v=<(.+),(.+),(.+)>, a=<(.+),(.+),(.+)>$',
            line,
        ).groups()
        p = [int(n) for n in p]
        particles.append(Particle(p))

    # just guessing after 1000 steps stuff is stable
    for i in range(1000):
        for particle in particles:
            collisions = list(filter(lambda x: x == particle, particles))

            # particle contains itself
            if len(collisions) > 1:
                for particle in collisions:
                    particles.remove(particle)

        for particle in particles:
            particle.tick()

    return len(particles)


print(task1('input.txt'))

print(task2('input.txt'))
