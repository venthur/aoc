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


def task2(fn):
    cubes = parse_input(fn)

    xs, ys, zs = zip(*cubes)
    minx, maxx = min(xs)-1, max(xs)+1
    miny, maxy = min(ys)-1, max(ys)+1
    minz, maxz = min(zs)-1, max(zs)+1

    queue = [(minx, miny, minz)]
    seen = set()
    outside = 0
    while queue:
        x, y, z = queue.pop(0)
        if (x, y, z) in cubes:
            outside += 1
            continue
        if (x, y, z) not in seen:
            seen.add((x, y, z))
            for xi, yi, zi in (
                (x+1, y, z),
                (x-1, y, z),
                (x, y+1, z),
                (x, y-1, z),
                (x, y, z+1),
                (x, y, z-1),
            ):
                if (
                    minx <= xi <= maxx and
                    miny <= yi <= maxy and
                    minz <= zi <= maxz
                ):
                    queue.append((xi, yi, zi))

    return outside


assert task1('test_input0.txt') == 64
print(task1('input.txt'))

assert task2('test_input0.txt') == 58
print(task2('input.txt'))
