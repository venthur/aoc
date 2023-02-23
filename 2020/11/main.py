def occupied(x, y, floor):
    res = 0
    for xi, yi in (
        (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1),
        (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1)
    ):
        if floor.get((xi, yi), '.') == '#':
            res += 1
    return res


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    floor = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            floor[x, y] = char

    seen = set()
    while True:
        floor_old = floor.copy()
        for (x, y), v in floor_old.items():
            if v == 'L' and occupied(x, y, floor_old) == 0:
                floor[x, y] = '#'
            if v == '#' and occupied(x, y, floor_old) >= 4:
                floor[x, y] = 'L'

        fi = list(floor.items())
        fi.sort(key=lambda x: x[0][0])
        fi.sort(key=lambda x: x[0][1])
        fi = tuple(v for _, v in fi)
        if fi in seen:
            break
        seen.add(fi)

    return len(list(filter(lambda x: x == '#', floor.values())))


def occupied_visible(x, y, floor, maxxy):

    res = 0
    for dx, dy in (
        (0, -1), (+1, -1), (+1, 0), (+1, +1),
        (0, +1), (-1, +1), (-1, 0), (-1, -1)
    ):
        xi, yi = x, y
        while True:
            xi += dx
            yi += dy
            if xi < 0 or xi > maxxy or yi < 0 or yi > maxxy:
                break
            if floor.get((xi, yi), '.') == '#':
                res += 1
                break
            elif floor.get((xi, yi), '.') == 'L':
                break

    return res


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    floor = dict()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            floor[x, y] = char

    maxxy = max(x, y)

    seen = set()
    while True:
        floor_old = floor.copy()
        for (x, y), v in floor_old.items():
            if v == 'L' and occupied_visible(x, y, floor_old, maxxy) == 0:
                floor[x, y] = '#'
            if v == '#' and occupied_visible(x, y, floor_old, maxxy) >= 5:
                floor[x, y] = 'L'

        fi = list(floor.items())
        fi.sort(key=lambda x: x[0][0])
        fi.sort(key=lambda x: x[0][1])
        fi = tuple(v for _, v in fi)
        if fi in seen:
            break
        seen.add(fi)

    return len(list(filter(lambda x: x == '#', floor.values())))


assert task1('test_input0.txt') == 37
print(task1('input.txt'))

assert task2('test_input0.txt') == 26
print(task2('input.txt'))
