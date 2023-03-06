from math import dist
from heapq import heappush, heappop


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
    visited = {(0, 0)}
    while todo:
        _, x, y, cost = heappop(todo)
        print(x, y, cost)
        if (x, y) == goal:
            return cost
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if (xi, yi) in risklevel and (xi, yi) not in visited:
                visited.add((xi, yi))
                cost2 = cost + risklevel[xi, yi]
                heappush(todo, (cost2+dist((xi, yi), goal), xi, yi, cost2))


assert task1('test_input0.txt') == 40
print(task1('input.txt'))
