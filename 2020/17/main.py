from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    space = defaultdict(lambda: '.')
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            space[x, y, 0] = '#'

    for cycle in range(6):
        active_coords = [pos for pos, v in space.items() if v == '#']
        xs, ys, zs = zip(*active_coords)
        space_old = space.copy()
        for x in range(min(xs)-1, max(xs)+2):
            for y in range(min(ys)-1, max(ys)+2):
                for z in range(min(zs)-1, max(zs)+2):
                    # count active neighbors
                    active_n = 0
                    for xi in range(x-1, x+2):
                        for yi in range(y-1, y+2):
                            for zi in range(z-1, z+2):
                                if (xi, yi, zi) == (x, y, z):
                                    continue
                                if space_old[xi, yi, zi] == '#':
                                    active_n += 1
                    # compute new space
                    if space_old[x, y, z] == '#' and active_n not in (2, 3):
                        space[x, y, z] = '.'
                    elif space_old[x, y, z] == '.' and active_n == 3:
                        space[x, y, z] = '#'

        print(cycle, sum((1 if v == '#' else 0 for v in space.values())))

    return sum((1 if v == '#' else 0 for v in space.values()))


assert task1('test_input0.txt') == 112
print(task1('input.txt'))
