import heapq
from functools import cache


@cache
def el(x, y, depth, xt, yt):
    if (x, y) in ((0, 0), (xt, yt)):
        index = 0
    elif y == 0:
        index = x * 16807
    elif x == 0:
        index = y * 48271
    else:
        index = el(x-1, y, depth, xt, yt) * el(x, y-1, depth, xt, yt)
    return (index + depth) % 20183


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    depth = int(lines[0].split()[-1])
    xt, yt = [int(n) for n in lines[1].split()[-1].split(',')]

    erosion_level = dict()
    for y in range(0, yt+1):
        for x in range(0, xt+1):
            erosion_level[x, y] = el(x, y, depth, xt, yt)

    return sum(map(lambda x: x % 3, erosion_level.values()))


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    depth = int(lines[0].split()[-1])
    xt, yt = [int(n) for n in lines[1].split()[-1].split(',')]

    def h(x, y):
        return abs(x - xt) + abs(y - yt)

    pq = []
    # gear: climbing, torch or neither
    # (heuristic, time, x, y, gear)
    heapq.heappush(pq, (0, 0, 0, 0, 't'))
    seen = set()
    seen.add((0, 0, 't'))
    while True:
        _, t, x, y, gear = heapq.heappop(pq)

        #print(t, x, y, gear)
        if (x, y, gear) == (xt, yt, 't'):
            return t

        type_ = el(x, y, depth, xt, yt) % 3
        for candidate in 'c', 't', 'n':
            if (
                type_ == 0 and gear == 'c' and candidate == 't' or
                type_ == 0 and gear == 't' and candidate == 'c' or
                type_ == 1 and gear == 'c' and candidate == 'n' or
                type_ == 1 and gear == 'n' and candidate == 'c' or
                type_ == 2 and gear == 't' and candidate == 'n' or
                type_ == 2 and gear == 'n' and candidate == 't'
            ) and (x, y, candidate) not in seen:
                seen.add((x, y, candidate))
                heapq.heappush(pq, (h(x, y)+t+7, t+7, x, y, candidate))

        for xn, yn in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
            if xn < 0 or yn < 0:
                continue

            type_ = el(xn, yn, depth, xt, yt) % 3
            if (
                gear == 'c' and type_ in (0, 1) or
                gear == 'n' and type_ in (1, 2) or
                gear == 't' and type_ in (0, 2)
            ) and (xn, yn, gear) not in seen:
                seen.add((xn, yn, gear))
                heapq.heappush(pq, (h(xn, yn)+t+1, t+1, xn, yn, gear))


assert task1('test_input.txt') == 114
print(task1('input.txt'))

assert task2('test_input.txt') == 45
print(task2('input.txt'))
