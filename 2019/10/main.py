from math import gcd, atan2, dist, degrees


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    astroids = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                astroids.add((x, y))

    maxvis = None
    for x, y in astroids:
        visible = astroids.copy()
        visible.discard((x, y))
        for xi, yi in astroids:
            dx, dy = abs(x - xi), abs(y - yi)
            steps = gcd(dx, dy)
            for i in range(1, steps):
                if x < xi:
                    xn = x + i*dx//steps
                else:
                    xn = x - i*dx//steps
                if y < yi:
                    yn = y + i*dy//steps
                else:
                    yn = y - i*dy//steps
                if (xn, yn) in visible:
                    visible.discard((xi, yi))
                    break
        if maxvis is None or len(visible) > maxvis:
            maxvis = len(visible)

    return maxvis


def task2(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    astroids = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                astroids.add((x, y))

    maxvis = None
    xs, ys = None, None
    for x, y in astroids:
        visible = astroids.copy()
        visible.discard((x, y))
        for xi, yi in astroids:
            dx, dy = abs(x - xi), abs(y - yi)
            steps = gcd(dx, dy)
            for i in range(1, steps):
                if x < xi:
                    xn = x + i*dx//steps
                else:
                    xn = x - i*dx//steps
                if y < yi:
                    yn = y + i*dy//steps
                else:
                    yn = y - i*dy//steps
                if (xn, yn) in visible:
                    visible.discard((xi, yi))
                    break
        if maxvis is None or len(visible) > maxvis:
            maxvis = len(visible)
            xs, ys = x, y

    #print(xs, ys)

    astroids.discard((xs, ys))
    astroids = [[x, y, -(degrees(atan2(-y+ys, x-xs)) + 360 - 90) % 360, dist((x, y), (xs, ys))] for x, y in astroids]

    astroids.sort(key=lambda x: x[-1])
    astroids.sort(key=lambda x: x[-2])

    shots = 0
    i = 0
    last_angle = None
    while shots < 200:
        while astroids[0][-2] == last_angle:
            a = astroids.pop(0)
            astroids.append(a)
        a = astroids.pop(0)
        #print(f'{shots} shot {a}')
        last_angle = a[-2]
        shots += 1

    return a[0] * 100 + a[1]


assert task1('test_input0.txt') == 8
print(task1('input.txt'))

assert task2('test_input1.txt') == 802
print(task2('input.txt'))
