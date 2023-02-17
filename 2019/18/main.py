import heapq
from math import dist
from functools import cache
from collections import deque


def read_input(fn):

    with open(fn) as fh:
        lines = fh.read().splitlines()

    area = dict()
    keys, doors = dict(), dict()
    x, y = None, None
    for yi, line in enumerate(lines):
        for xi, char in enumerate(line):
            if char in '#.':
                area[xi, yi] = char
            elif char == '@':
                x, y = xi, yi
                area[xi, yi] = '.'
            elif char in 'abcdefghijklmnopqrstuvwxyz':
                area[xi, yi] = '.'
                keys[xi, yi] = char
            elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                area[xi, yi] = '.'
                doors[xi, yi] = char.lower()
            else:
                raise ValueError(char)
    return x, y, area, doors, keys


@cache
def reachable_keys(x, y, area, doors, keys):
    area = dict(area)
    doors = dict(doors)
    keys = dict(keys)

    queue = deque([(x, y, 0)])
    visited = {(x, y)}
    reachable = dict()
    while queue:
        x, y, d = queue.popleft()
        if (x, y) in keys:
            reachable[keys.pop((x, y))] = (x, y, d)
            # treat the key as a wall
            continue
        for xi, yi in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if (
                (xi, yi) not in visited and
                area[xi, yi] == '.' and
                (xi, yi) not in doors
            ):
                visited.add((xi, yi))
                queue.append((xi, yi, d+1))
    return reachable


def h(x, y, points):
    points = points + [(x, y)]
    xs, ys = zip(*points)
    return dist((min(xs), min(ys)), (max(xs), max(ys)))


def task1(fn):
    reachable_keys.cache_clear()
    x, y, area, doors, keys = read_input(fn)

    pq = []
    heapq.heappush(pq, (0, 0, x, y, doors.items(), keys.items(), []))
    kh = ''.join(sorted(list(keys.values())))
    visited = {(x, y, 0, kh)}
    while pq:
        _, d, x, y, doors, keys, path = heapq.heappop(pq)
        doors = dict(doors)
        keys = dict(keys)

        #print(f'{int(_):>5} -> {" ".join(path):<50} {len(pq):>5}', end='\r')
        if len(keys) == 0:
            return d

        for key, (kx, ky, l) in reachable_keys(x, y, tuple(area.items()), tuple(doors.items()), tuple(keys.items())).items():
            doors2 = dict(filter(lambda x: x[1] != key, doors.items()))
            keys2 = dict(filter(lambda x: x[1] != key, keys.items()))
            x2, y2 = kx, ky

            kh = ''.join(sorted(list(keys2.values())))
            if (x2, y2, d+l, kh) not in visited:
                dist = h(x2, y2, list(keys2.keys()))
                visited.add((x2, y2, d+l, kh))
                heapq.heappush(pq, (d+l+dist, d+l, x2, y2, doors2.items(), keys2.items(), path + [key]))


def task2(fn):
    reachable_keys.cache_clear()

    x, y, area, doors, keys = read_input(fn)
    area[x, y] = '#'
    area[x+1, y] = '#'
    area[x-1, y] = '#'
    area[x, y+1] = '#'
    area[x, y-1] = '#'
    pos = [[x-1, y-1], [x+1, y-1], [x-1, y+1], [x+1, y+1]]

    pq = []
    heapq.heappush(pq, (0, pos, doors.items(), keys.items()))
    kh = ''.join(sorted(list(keys.values())))
    visited = set()
    while pq:
        d, pos, doors, keys = heapq.heappop(pq)
        doors = dict(doors)
        keys = dict(keys)

        #print(f'{int(d):>5} -> {" ".join(keys.values()):<50} {len(pq):>5}', end='\r')
        if len(keys) == 0:
            return d

        for i, (x, y) in enumerate(pos):

            for key, (kx, ky, l) in reachable_keys(x, y, tuple(area.items()), tuple(doors.items()), tuple(keys.items())).items():
                doors2 = dict(filter(lambda x: x[1] != key, doors.items()))
                keys2 = dict(filter(lambda x: x[1] != key, keys.items()))
                x2, y2 = kx, ky

                pos2 = list(pos[:])
                pos2[i] = [x2, y2]
                pos2 = tuple((xi, yi) for xi, yi in pos2)

                kh = ''.join(sorted(list(keys2.values())))
                if (pos2, d+l, kh) not in visited:
                    visited.add((pos2, d+l, kh))
                    heapq.heappush(pq, (d+l, pos2, doors2.items(), keys2.items()))


assert task1('test_input0.txt') == 132
assert task1('test_input1.txt') == 136
assert task1('test_input2.txt') == 81
print(task1('input.txt'))

assert task2('test_input3.txt') == 72
print(task2('input.txt'))
