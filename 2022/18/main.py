from itertools import product


def parse_input(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    cubes = []
    for line in lines:
        cubes.append(tuple(int(n) for n in line.split(',')))

    return cubes


def task1(fn):
    cubes = parse_input(fn)

    free = 0
    for x, y, z in cubes:
        for xi, yi, zi in (
            (x+1, y, z),
            (x-1, y, z),
            (x, y+1, z),
            (x, y-1, z),
            (x, y, z+1),
            (x, y, z-1),
        ):
            if (xi, yi, zi) not in cubes:
                free += 1
    return free

assert task1('test_input0.txt') == 64
print(task1('input.txt'))
