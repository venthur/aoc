def task1(fn, n_steps):
    rocks, pots, steps = set(), set(), set()
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                if char == 'S':
                    pots.add((x, y))
                    steps.add((x, y))
                elif char == '.':
                    pots.add((x, y))
                elif char == '#':
                    rocks.add((x, y))

    for i in range(n_steps):

        steps_prev = steps.copy()
        steps = set()

        for x, y in steps_prev:
            for xi, yi in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
                if (xi, yi) in rocks:
                    continue
                if (xi, yi) in pots:
                    steps.add((xi, yi))

    return len(steps)


def task2(fn, n_steps):
    # this calculation does not work on the test input as there is no straight
    # line from S to the sides of the map
    rocks, pots, steps = set(), set(), set()
    with open(fn) as fh:
        for y, line in enumerate(fh.read().splitlines()):
            for x, char in enumerate(line):
                if char == 'S':
                    pots.add((x, y))
                    steps.add((x, y))
                elif char == '.':
                    pots.add((x, y))
                elif char == '#':
                    rocks.add((x, y))

    assert x == y
    size = x + 1

    cycles, modulos = divmod(n_steps, size)

    for i in range(size * 2 + modulos):

        prev_steps = steps.copy()
        steps = set()

        for (x, y) in prev_steps:
            for xi, yi in ((x, y-1), (x, y+1), (x-1, y), (x+1, y)):
                if (xi % size, yi % size) in rocks:
                    continue
                elif (xi % size, yi % size) in pots:
                    steps.add((xi, yi))

    counts = dict()
    for (x, y) in steps:
        counts[(x//size, y//size)] = counts.get((x//size, y//size), 0) + 1

    result = 0

    result += counts[(-2, -1)] * cycles
    result += counts[(-2, 0)]
    result += counts[(-2, 1)] * cycles

    result += counts[(-1, -1)] * (cycles - 1)
    result += counts[(-1, 0)] * cycles**2
    result += counts[(-1, 1)] * (cycles - 1)

    result += counts[(0, -2)]
    result += counts[(0, 0)] * (cycles-1)**2
    result += counts[(0, 2)]

    result += counts[(1, -2)] * cycles
    result += counts[(1, -1)] * (cycles - 1)
    result += counts[(1, 1)] * (cycles - 1)
    result += counts[(1, 2)] * cycles

    result += counts[(2, 0)]

    return result


assert task1('test_input.txt', 6) == 16
print(task1('input.txt', 64))

print(task2('input.txt', 26501365))
