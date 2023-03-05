from collections import defaultdict


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    a_to_bs = []
    for line in lines:
        line = line.replace(',', ' ')
        a, b, _, c, d = line.split()
        a, b, c, d = int(a), int(b), int(c), int(d)
        a_to_bs.append((a, b, c, d))

    # filter out the non-horizontal or -vertical ones
    a_to_bs = list(filter(lambda x: x[0] == x[2] or x[1] == x[3], a_to_bs))

    floor = defaultdict(int)
    for x1, y1, x2, y2 in a_to_bs:
        if x1 == x2:
            for yi in range(min(y1, y2), max(y1, y2)+1):
                floor[x1, yi] += 1
        if y1 == y2:
            for xi in range(min(x1, x2), max(x1, x2)+1):
                floor[xi, y1] += 1

    return len(list(filter(lambda x: x > 1, floor.values())))


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    a_to_bs = []
    for line in lines:
        line = line.replace(',', ' ')
        a, b, _, c, d = line.split()
        a, b, c, d = int(a), int(b), int(c), int(d)
        a_to_bs.append((a, b, c, d))

    floor = defaultdict(int)
    for x1, y1, x2, y2 in a_to_bs:
        if x1 == x2:
            for yi in range(min(y1, y2), max(y1, y2)+1):
                floor[x1, yi] += 1
        elif y1 == y2:
            for xi in range(min(x1, x2), max(x1, x2)+1):
                floor[xi, y1] += 1
        else:
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            xs = [i for i in range(x1, x2+dx, dx)]
            ys = [i for i in range(y1, y2+dy, dy)]
            for x, y in zip(xs, ys):
                floor[x, y] += 1

    return len(list(filter(lambda x: x > 1, floor.values())))


assert task1('test_input0.txt') == 5
print(task1('input.txt'))

assert task2('test_input0.txt') == 12
print(task2('input.txt'))
