from itertools import pairwise, count
from time import sleep

def pprint(cave):
    minx = min(cave.keys(), key=lambda x: x[0])[0]
    miny = min(cave.keys(), key=lambda x: x[1])[1]
    cave = {(k[0]-minx, k[1]-miny): v for k, v in cave.items()}
    maxx = max(cave.keys(), key=lambda x: x[0])[0]
    maxy = max(cave.keys(), key=lambda x: x[1])[1]
    s = ''
    for row in range(maxy+1):
        for col in range(maxx+1):
            if col == 0:
                s += '\n'
            what = cave.get((col, row), '.')
            s += what
    print(s)


def pour(cave):
    maxy = max(cave.keys(), key=lambda x: x[1])[1]
    cave = cave.copy()
    pos = (500, 0)
    while True:
        d = pos[0], pos[1]+1
        l = d[0]-1, d[1]
        r = d[0]+1, d[1]
        if d[1] > maxy:
            return cave
        if cave.get(d, '.') == '.':
            pos = d
            continue
        else:
            if cave.get(l, '.') == '.':
                pos = l
                continue
            elif cave.get(r, '.') == '.':
                pos = r
                continue
            else:
                cave[pos] = 'o'
                return cave


def task1(input_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    paths = []
    for line in lines:
        points = line.split(' -> ')
        path = []
        for point in points:
            x, y = point.split(',')
            x = int(x)
            y = int(y)
            path.append([x, y])
        paths.append(path)

    cave = dict()
    cave[500, 0] = '+'
    for path in paths:
        for p1, p2 in pairwise(path):
            # find out if they differ in x or y
            if p1[0] == p2[0]:
                if p1[1] < p2[1]:
                    for i in range(p1[1], p2[1]+1):
                        cave[p1[0], i] = '#'
                elif p1[1] > p2[1]:
                    for i in range(p1[1], p2[1]-1, -1):
                        cave[p1[0], i] = '#'
            elif p1[1] == p2[1]:
                if p1[0] < p2[0]:
                    for i in range(p1[0], p2[0]+1):
                        cave[i, p1[1]] = '#'
                elif p1[0] > p2[0]:
                    for i in range(p1[0], p2[0]-1, -1):
                        cave[i, p1[1]] = '#'
            else:
                raise ValueError

    for sand in count():
        cave2 = pour(cave)
        if cave2 == cave:
            return sand
        cave = cave2


def pour2(cave, floor_level):
    cave = cave.copy()
    pos = (500, 0)
    while True:
        d = pos[0], pos[1]+1
        l = d[0]-1, d[1]
        r = d[0]+1, d[1]
        if cave[500, 0] == 'o':
            return cave
        if cave.get(d, '.') == '.' and d[1] < floor_level:
            pos = d
            continue
        else:
            if cave.get(l, '.') == '.' and l[1] < floor_level:
                pos = l
                continue
            elif cave.get(r, '.') == '.' and l[1] < floor_level:
                pos = r
                continue
            else:
                cave[pos] = 'o'
                return cave


def task2(input_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    paths = []
    for line in lines:
        points = line.split(' -> ')
        path = []
        for point in points:
            x, y = point.split(',')
            x = int(x)
            y = int(y)
            path.append([x, y])
        paths.append(path)

    cave = dict()
    cave[500, 0] = '+'
    for path in paths:
        for p1, p2 in pairwise(path):
            # find out if they differ in x or y
            if p1[0] == p2[0]:
                if p1[1] < p2[1]:
                    for i in range(p1[1], p2[1]+1):
                        cave[p1[0], i] = '#'
                elif p1[1] > p2[1]:
                    for i in range(p1[1], p2[1]-1, -1):
                        cave[p1[0], i] = '#'
            elif p1[1] == p2[1]:
                if p1[0] < p2[0]:
                    for i in range(p1[0], p2[0]+1):
                        cave[i, p1[1]] = '#'
                elif p1[0] > p2[0]:
                    for i in range(p1[0], p2[0]-1, -1):
                        cave[i, p1[1]] = '#'
            else:
                raise ValueError

    floor_level = max(cave.keys(), key=lambda x: x[1])[1] + 2
    for sand in count():
        cave2 = pour2(cave, floor_level)
        if cave2 == cave:
            return sand
        cave = cave2


assert task1('test_input.txt') == 24
print(task1('input.txt'))

assert task2('test_input.txt') == 93
print(task2('input.txt'))
