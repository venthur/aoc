from collections import Counter
from itertools import combinations


def rotx(x, y, z):
    return x, -z, y


def rotz(x, y, z):
    return -y, x, z


def rotations(readings):
    # yield all rotations from list of readings

    for rotation in (
        lambda x, y, z: (x, y, z),
        rotz, rotz, rotz,
        rotx,
        rotz, rotz, rotz,
        rotx,
        rotz, rotz, rotz,
        lambda x, y, z: (-x, -z, -y),
        rotz, rotz, rotz,
        rotx,
        rotz, rotz, rotz,
        lambda x, y, z: (x, z, -y),
        rotz, rotz, rotz,
    ):
        readings2 = []
        res = set()
        for r in readings:
            r2 = rotation(*r)
            res.add(r2)
            readings2.append(r2)

        readings = readings2[:]
        yield res


def move(readings, dx, dy, dz):
    res = set()
    for r in readings:
        res.add((r[0] + dx, r[1] + dy, r[2] + dz))

    return res


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    readings = []
    for line in lines:
        if not line:
            continue
        if line.startswith('---'):
            readings.append([])
            continue
        pos = tuple(int(n) for n in line.split(','))
        readings[-1].append(pos)

    # test all readings with all possible rotations against the first one with
    # the original rotation:
    beacons = set()
    for b in readings.pop(0):
        beacons.add(b)

    i = 0
    scanners = [(0, 0, 0)]
    while readings:
        if i >= len(readings):
            i = 0

        bi = readings[i][:]
        for bir in rotations(bi):
            [(diff, count)] = Counter(
                (x2 - x1, y2 - y1, z2 - z1)
                for x1, y1, z1 in bir
                for x2, y2, z2 in beacons
            ).most_common(1)
            if count >= 12:
                bir = move(bir, *diff)
                beacons.update(bir)
                readings.remove(bi)
                scanners.append(diff)
                break
        i += 1

    p1 = len(beacons)

    maxd = 0
    for a, b in combinations(scanners, 2):
        d = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        maxd = max(maxd, d)

    p2 = maxd

    return p1, p2


assert task1('test_input0.txt') == (79, 3621)
print(task1('input.txt'))
