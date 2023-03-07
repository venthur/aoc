from math import dist
from heapq import heappush, heappop, heapify


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    risklevel = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            risklevel[x, y] = int(char)
    goal = (x, y)

    todo = []
    heappush(todo, (0, 0, 0, 0))
    visited = set()
    while todo:
        _, x, y, cost = heappop(todo)
        visited.add((x, y))

        if (x, y) == goal:
            return cost

        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):

            if (xi, yi) not in risklevel or (xi, yi) in visited:
                continue

            cost2 = cost + risklevel[xi, yi]
            if any(
                filter(lambda n: n[1] == xi and n[2] == yi and cost2 >= n[3], todo)
            ):
                continue

            f = cost2 + dist((xi, yi), goal)
            if any(
                filter(lambda n: n[1] == xi and n[2] == yi, todo)
            ):
                todo = list(filter(lambda n: n[1] != xi or n[2] != yi, todo))
                heapify(todo)
            heappush(todo, (f, xi, yi, cost2))


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    risklevel = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            risklevel[x, y] = int(char)

    xs, ys = zip(*risklevel)
    maxx = max(xs)
    maxy = max(ys)
    for y in range(maxy+1):
        for x in range(maxx+1):
            for yi in range(5):
                for xi in range(5):
                    if yi == xi == 0:
                        continue
                    base = risklevel[x, y]
                    offset = xi + yi
                    v = base + offset
                    while v > 9:
                        v -= 9
                    risklevel[xi*(maxx+1)+x, yi*(maxy+1)+y] = v

    xs, ys = zip(*risklevel)

    goal = (max(xs), max(ys))

    todo = []
    heappush(todo, (0, 0, 0, 0))
    visited = set()
    while todo:
        _, x, y, cost = heappop(todo)
        visited.add((x, y))

        if (x, y) == goal:
            return cost

        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):

            if (xi, yi) not in risklevel or (xi, yi) in visited:
                continue

            cost2 = cost + risklevel[xi, yi]
            if any(
                filter(lambda n: n[1] == xi and n[2] == yi and cost2 >= n[3], todo)
            ):
                continue

            f = cost2 + dist((xi, yi), goal)
            if any(
                filter(lambda n: n[1] == xi and n[2] == yi, todo)
            ):
                todo = list(filter(lambda n: n[1] != xi or n[2] != yi, todo))
                heapify(todo)
            heappush(todo, (f, xi, yi, cost2))


assert task1('test_input0.txt') == 40
print(task1('input.txt'))

assert task2('test_input0.txt') == 315
print(task2('input.txt'))
