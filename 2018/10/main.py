import re


def task1(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    stars = []
    for line in lines:
        g = re.match(
            r'^.*<(.*), (.*)> .*<(.*),(.*)>$',
            line,
        ).groups()
        stars.append([int(n) for n in g])

    for i in range(10880):
        for star in stars:
            star[0] += star[2]
            star[1] += star[3]

    pos = set()
    for xy in map(lambda x: x[:2], stars):
        pos.add(tuple(xy))

    xs = list(map(lambda x: x[0], stars))
    ys = list(map(lambda x: x[1], stars))

    s = ''
    for y in range(min(ys), max(ys)+1):
        for x in range(min(xs), max(xs)+1):
            s += '#' if (x, y) in pos else ' '
        s += '\n'
    print(s)
    print(i+1)


task1('input.txt')
