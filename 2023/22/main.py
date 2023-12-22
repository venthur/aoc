from itertools import product


def settle_bricks(bricks):
    bricks_dropped = []
    xy_heights = dict()
    for (x1, y1, z1), (x2, y2, z2) in bricks:
        min_z = 1
        height = abs(max(z1, z2) - min(z1, z2)) + 1
        for x, y in product(
            range(min(x1, x2), max(x1, x2)+1),
            range(min(y1, y2), max(y1, y2)+1),
        ):
            min_z = max(xy_heights.get((x, y), 1), min_z)
        delta_z = abs(min_z - min(z1, z2))
        z1 -= delta_z
        z2 -= delta_z
        bricks_dropped.append(((x1, y1, z1), (x2, y2, z2)))
        for x, y in product(
            range(min(x1, x2), max(x1, x2)+1),
            range(min(y1, y2), max(y1, y2)+1),
        ):
            xy_heights[(x, y)] = min_z + height
    return bricks_dropped


def task1(fn):
    bricks = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            p1, p2 = line.split('~')
            p1 = tuple(int(i) for i in p1.split(','))
            p2 = tuple(int(i) for i in p2.split(','))
            bricks.append((p1, p2))
    bricks = sorted(bricks, key=lambda brick: min(brick[0][-1], brick[1][-1]))

    bricks = settle_bricks(bricks)
    result = 0
    for i in range(len(bricks)):
        bricks2 = bricks[:]
        bricks2.pop(i)
        bricks3 = bricks2[:]
        bricks2 = settle_bricks(bricks2)
        if all(b1 == b2 for b1, b2 in zip(bricks2, bricks3)):
            result += 1
    return result


def task2(fn):
    bricks = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            p1, p2 = line.split('~')
            p1 = tuple(int(i) for i in p1.split(','))
            p2 = tuple(int(i) for i in p2.split(','))
            bricks.append((p1, p2))
    bricks = sorted(bricks, key=lambda brick: min(brick[0][-1], brick[1][-1]))

    bricks = settle_bricks(bricks)
    result = 0
    for i in range(len(bricks)):
        bricks2 = bricks[:]
        bricks2.pop(i)
        bricks3 = bricks2[:]
        bricks2 = settle_bricks(bricks2)
        result += sum(0 if b1 == b2 else 1 for b1, b2 in zip(bricks2, bricks3))
    return result


assert task1('test_input.txt') == 5
print(task1('input.txt'))

assert task2('test_input.txt') == 7
print(task2('input.txt'))
