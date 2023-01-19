import re


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    canvas = set()
    common = set()
    for line in lines:
        g = re.match(
            r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$',
            line,
        ).groups()
        i, x, y, w, h = [int(i) for i in g]
        for xi in range(x, w+x):
            for yi in range(y, h+y):
                if (xi, yi) in canvas:
                    common.add((xi, yi))
                else:
                    canvas.add((xi, yi))

    return len(common)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    sets = []
    for line in lines:
        g = re.match(
            r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$',
            line,
        ).groups()
        i, x, y, w, h = [int(i) for i in g]
        s = set()
        for xi in range(x, w+x):
            for yi in range(y, h+y):
                s.add((xi, yi))
        sets.append((i, s))

    from itertools import combinations
    for a, b in combinations(sets, 2):
        ia, sa = a
        ib, sb = b
        if sa & sb:
            try:
                sets.remove(a)
            except ValueError:
                pass
            try:
                sets.remove(b)
            except ValueError:
                pass
    return sets.pop()[0]


assert task1('test_input.txt') == 4
print(task1('input.txt'))

assert task2('test_input.txt') == 3
print(task2('input.txt'))
