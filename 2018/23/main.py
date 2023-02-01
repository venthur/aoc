def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    bots = []
    for line in lines:
        pos, r = line.split(', ')

        pos = pos.split('=')[-1][1:-1]
        pos = [int(n) for n in pos.split(',')]

        r = int(r.split('=')[-1])

        bots.append((*pos, r))

    maxbot = max(bots, key=lambda x: x[-1])

    in_range = list(filter(
        lambda x: abs(x[0] - maxbot[0]) + abs(x[1] - maxbot[1]) + abs(x[2] - maxbot[2]) <= maxbot[-1],
        bots
    ))
    return len(in_range)


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    bots = []
    for line in lines:
        pos, r = line.split(', ')

        pos = pos.split('=')[-1][1:-1]
        pos = [int(n) for n in pos.split(',')]

        r = int(r.split('=')[-1])

        bots.append((*pos, r))

    xs, ys, zs, rs = zip(*bots)
    xs = list(xs) + [0]
    ys = list(ys) + [0]
    zs = list(zs) + [0]

    dist = 1
    while (
        dist < max(xs) - min(xs) or
        dist < max(ys) - min(ys) or
        dist < max(zs) - min(zs)
    ):
        dist *= 2

    while True:
        target_count = 0
        best = None
        best_val = None
        for x in range(min(xs), max(xs)+1, dist):
            for y in range(min(ys), max(ys)+1, dist):
                for z in range(min(zs), max(zs)+1, dist):
                    count = 0
                    for bx, by, bz, br in bots:
                        mdist = abs(bx - x) + abs(by - y) + abs(bz - z)
                        if (mdist - br) // dist <= 0:
                            count += 1
                    if count > target_count:
                        target_count = count
                        best_val = abs(x) + abs(y) + abs(z)
                        best = (x, y, z)
                    elif count == target_count:
                        if best_val is None or abs(x) + abs(y) + abs(z) < best_val:
                            best_val = abs(x) + abs(y) + abs(z)
                            best = (x, y, z)

        if dist == 1:
            return best_val

        xs = [best[0] - dist, best[0] + dist]
        ys = [best[1] - dist, best[1] + dist]
        zs = [best[2] - dist, best[2] + dist]
        dist //= 2


assert task1('test_input.txt') == 7
print(task1('input.txt'))

assert task2('test_input2.txt') == 36
print(task2('input.txt'))
