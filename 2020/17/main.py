from itertools import product
from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    space = defaultdict(lambda: '.')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            space[x, y, 0] = char

    for cycle in range(6):
        active_coords = [pos for pos, v in space.items() if v == '#']
        xs, ys, zs = zip(*active_coords)
        lower = min(min(xs), min(ys), min(zs))
        upper = max(max(xs), max(ys), max(zs))
        space_old = space.copy()
        for x, y, z in product(range(lower-1, upper+2), repeat=3):
            # count active neighbors
            active_n = 0
            for dx, dy, dz in product((-1, 0, 1), repeat=3):
                xi, yi, zi = x+dx, y+dy, z+dz
                if (xi, yi, zi) == (x, y, z):
                    continue
                if space_old[xi, yi, zi] == '#':
                    active_n += 1
            # compute new space
            if (
                space_old[x, y, z] == '#' and active_n in (2, 3) or
                space_old[x, y, z] == '.' and active_n == 3
            ):
                space[x, y, z] = '#'
            else:
                space[x, y, z] = '.'

    return list(space.values()).count('#')


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    space = defaultdict(lambda: '.')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            space[x, y, 0, 0] = char

    for cycle in range(6):
        active_coords = [pos for pos, v in space.items() if v == '#']
        xs, ys, zs, ws = zip(*active_coords)
        lower = min(min(xs), min(ys), min(zs), min(ws))
        upper = max(max(xs), max(ys), max(zs), max(ws))
        space_old = space.copy()
        for x, y, z, w in product(range(lower-1, upper+2), repeat=4):
            # count active neighbors
            active_n = 0
            for dx, dy, dz, dw in product((-1, 0, 1), repeat=4):
                xi, yi, zi, wi = x+dx, y+dy, z+dz, w+dw
                if (xi, yi, zi, wi) == (x, y, z, w):
                    continue
                if space_old[xi, yi, zi, wi] == '#':
                    active_n += 1
            # compute new space
            if (
                space_old[x, y, z, w] == '#' and active_n in (2, 3) or
                space_old[x, y, z, w] == '.' and active_n == 3
            ):
                space[x, y, z, w] = '#'
            else:
                space[x, y, z, w] = '.'

    return list(space.values()).count('#')


assert task1('test_input0.txt') == 112
print(task1('input.txt'))

assert task2('test_input0.txt') == 848
print(task2('input.txt'))
