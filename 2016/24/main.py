from functools import cache
from itertools import permutations, pairwise
import heapq
import math


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    walls = set()
    pos = None
    targets = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))
            elif char == '0':
                pos = (x, y)
            elif char.isnumeric():
                targets.add((x, y))
            else:
                assert char == '.'

    @cache
    def h(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    @cache
    def a_star(start, end):
        pq = []
        heapq.heappush(pq, (h(start, end), start, 0))
        seen = set()

        while pq:
            _, pos, steps = heapq.heappop(pq)
            if pos == end:
                return steps
            x, y = pos
            for x2, y2 in (x+1, y), (x-1, y), (x, y-1), (x, y+1):
                if (x2, y2) not in walls and (x2, y2) not in seen:
                    seen.add((x2, y2))
                    heapq.heappush(pq, (steps+h((x2, y2), end), (x2, y2), steps+1))

    current_best = None
    for p in permutations(targets):
        p = [pos, *p]
        l = 0
        for a, b in pairwise(p):
            l += a_star(a, b)
        if current_best is None or l < current_best:
            current_best = l

    return current_best


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    walls = set()
    pos = None
    targets = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))
            elif char == '0':
                pos = (x, y)
            elif char.isnumeric():
                targets.add((x, y))
            else:
                assert char == '.'

    @cache
    def h(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    @cache
    def a_star(start, end):
        pq = []
        heapq.heappush(pq, (h(start, end), start, 0))
        seen = set()

        while pq:
            _, pos, steps = heapq.heappop(pq)
            if pos == end:
                return steps
            x, y = pos
            for x2, y2 in (x+1, y), (x-1, y), (x, y-1), (x, y+1):
                if (x2, y2) not in walls and (x2, y2) not in seen:
                    seen.add((x2, y2))
                    heapq.heappush(pq, (steps+h((x2, y2), end), (x2, y2), steps+1))

    current_best = None
    for p in permutations(targets):
        p = [pos, *p, pos]
        l = 0
        for a, b in pairwise(p):
            l += a_star(a, b)
        if current_best is None or l < current_best:
            current_best = l

    return current_best


assert task1('test_input.txt') == 14
print(task1('input.txt'))

print(task2('input.txt'))
