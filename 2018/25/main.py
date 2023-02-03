def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    points = list(map(lambda l: [int(n) for n in l.split(',')], lines))

    clusters = 0
    while points:
        p = points.pop(0)
        candidates = []
        candidates.append(p)

        while candidates:
            c = candidates.pop(0)
            processed = []
            for p in points:
                if (
                    abs(c[0] - p[0]) + abs(c[1] - p[1]) +
                    abs(c[2] - p[2]) + abs(c[3] - p[3]) <= 3
                ):
                    candidates.append(p)
                    processed.append(p)

            for p in processed:
                points.remove(p)

        clusters += 1

    return clusters


print(task1('input.txt'))
