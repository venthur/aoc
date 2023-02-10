import re
from itertools import combinations, count


def task1(fn, steps):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    moons = []
    for line in lines:
        groups = re.match(
                r'^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$',
                line,
        ).groups()
        moons.append([int(n) for n in groups] + [0, 0, 0])

    for step in range(steps):
        # gravity
        for a, b in combinations(moons, 2):
            for i in range(3):
                if a[i] > b[i]:
                    a[i+3] -= 1
                    b[i+3] += 1
                elif a[i] < b[i]:
                    a[i+3] += 1
                    b[i+3] -= 1
        # velocity
        for moon in moons:
            for i in range(3):
                moon[i] += moon[i+3]

    energy = 0
    for moon in moons:
        absmoon = list(map(lambda x: abs(x), moon))
        energy += sum(absmoon[:3]) * sum(absmoon[3:])

    return energy


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    moons = []
    for line in lines:
        groups = re.match(
                r'^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$',
                line,
        ).groups()
        moons.append([int(n) for n in groups] + [0, 0, 0])

    seen = set()
    for step in count(0):
        # gravity
        for a, b in combinations(moons, 2):
            for i in range(3):
                if a[i] > b[i]:
                    a[i+3] -= 1
                    b[i+3] += 1
                elif a[i] < b[i]:
                    a[i+3] += 1
                    b[i+3] -= 1
        # velocity
        for moon in moons:
            for i in range(3):
                moon[i] += moon[i+3]

        fmoons = tuple(tuple(moon) for moon in moons)
        if fmoons in seen:
            return step
        seen.add(fmoons)


assert task1('test_input0.txt', 10) == 179
print(task1('input.txt', 1000))

assert task2('test_input0.txt') == 2772
print(task2('input.txt'))
