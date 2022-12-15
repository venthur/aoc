import re


def task1(input_, row):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    beacons = set()
    nobeacons = set()
    for line in lines:
        sx, sy, bx, by = [
            int(i) for i in re.match(
                r'^.*?x=(-?\d*), y=(-?\d*).*?x=(-?\d*), y=(-?\d*)$',
                line,
            ).groups()
        ]
        d = abs(sx - bx) + abs(sy - by)
        beacons.add((bx, by))
        for x in range(sx-d, sx+d+1):
            y = row
            if abs(sx - x) + abs(sy - y) <= d:
                nobeacons.add((x, y))
    nobeacons -= beacons

    r = list(filter(lambda x: x[1] == row, nobeacons))
    return len(r)


def task2(input_, max_):
    with open(input_) as fh:
        lines = fh.read().splitlines()

    sensors_d = set()
    for line in lines:
        sx, sy, bx, by = [
            int(i) for i in re.match(
                r'^.*?x=(-?\d*), y=(-?\d*).*?x=(-?\d*), y=(-?\d*)$',
                line,
            ).groups()
        ]
        d = abs(sx - bx) + abs(sy - by)
        sensors_d.add((sx, sy, d))

    candidates = set()
    for x, y, d in sensors_d:
        for i in range(d+1):
            candidates.add((x-i, y+d+1-i))
            candidates.add((x+i, y+d+1-i))
            candidates.add((x-i, y-d-1+i))
            candidates.add((x+i, y-d-1+i))

    for i, (x, y) in enumerate(candidates):
        if x < 0 or x > max_ or y < 0 or y > max_:
            continue
        for sx, sy, d in sensors_d:
            if abs(sx - x) + abs(sy - y) <= d:
                break
        else:
            return x*4000000 + y


assert task1('test_input.txt', 10) == 26
print(task1('input.txt', 2000000))

assert task2('test_input.txt', 20) == 56000011
print(task2('input.txt', 4000000))
