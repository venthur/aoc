from itertools import product


def parse(fn):
    with open(fn) as fh:
        lines = fh.read().splitlines()

    cmds = []
    for line in lines:
        cmd, rest = line.split()
        ranges = []
        for xyz in rest.split(','):
            xyz = xyz.split('=')[-1]
            l, h = [int(n) for n in xyz.split('..')]
            ranges.append((l, h))
        cmds.append((cmd, ranges))

    return cmds


def task1(fn):
    commands = parse(fn)

    ons = set()
    for cmd, ((xl, xh), (yl, yh), (zl, zh)) in commands:
        if any(
            filter(
                lambda x: x > 50,
                map(lambda x: abs(x), (xl, xh, yl, yh, zl, zh))
            )
        ):
            continue
        tmp = set()
        for x, y, z in product(range(xl, xh+1), range(yl, yh+1), range(zl, zh+1)):
            tmp.add((x, y, z))
        if cmd == 'on':
            ons.update(tmp)
        else:
            ons.difference_update(tmp)

    return len(ons)


def intersection(s, t):
    mm = [lambda a, b: -b, max, min, max, min, max, min]
    n = [mm[i](s[i], t[i]) for i in range(7)]
    return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n


def task2(fn):
    commands = parse(fn)
    cuboids = []
    for cmd, ((xl, xh), (yl, yh), (zl, zh)) in commands:
        cuboids.append((1 if cmd == 'on' else 0, xl, xh, yl, yh, zl, zh))

    cores = []
    for cuboid in cuboids:
        toadd = [cuboid] if cuboid[0] == 1 else []
        for core in cores:
            inter = intersection(cuboid, core)
            if inter:
                toadd += [inter]
        cores += toadd

    count = 0
    for c in cores:
        count += c[0] * (c[2]-c[1]+1) * (c[4]-c[3]+1) * (c[6]-c[5]+1)
    return count


assert task1('test_input.txt') == 590784
print(task1('input.txt'))

assert task2('test_input2.txt') == 2758514936282235
print(task2('input.txt'))
