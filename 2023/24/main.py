from itertools import combinations


def task1(fn, lo, hi):
    stones = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            p, v = line.split(' @ ')
            p = [int(i) for i in p.split(', ')]
            v = [int(i) for i in v.split(', ')]

            stones.append((p[:2], v[:2]))

    def intersect(p1, v1, p2, v2):

        x1, y1 = p1
        x2, y2 = p1[0] + v1[0], p1[1] + v1[1]
        x3, y3 = p2
        x4, y4 = p2[0] + v2[0], p2[1] + v2[1]

        try:
            x = (
                ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) /
                ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
            )
            y = (
                ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) /
                ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
            )
        except ZeroDivisionError:
            return 0

        if (
            lo <= x <= hi and lo <= y <= hi and
            (x1 < x and v1[0] > 0 or x1 > x and v1[0] < 0) and
            (y1 < y and v1[1] > 0 or y1 > y and v1[1] < 0) and
            (x3 < x and v2[0] > 0 or x3 > x and v2[0] < 0) and
            (y3 < y and v2[1] > 0 or y3 > y and v2[1] < 0)
        ):
            return 1
        else:
            return 0

    return sum(
        intersect(*s1, *s2) for s1, s2 in combinations(stones, 2)
    )


def task2(fn):
    stones = []
    with open(fn) as fh:
        for line in fh.read().splitlines():
            p, v = line.split(' @ ')
            p = [int(i) for i in p.split(', ')]
            v = [int(i) for i in v.split(', ')]
            stones.append((*p, *v))

    potential_x = None
    potential_y = None
    potential_z = None
    for a, b in combinations(stones, 2):
        apx, apy, apz, avx, avy, avz = a
        bpx, bpy, bpz, bvx, bvy, bvz = b

        if avx == bvx:
            new = set()
            diff = bpx - apx
            for v in range(-1000, 1000):
                if v == avx:
                    new.add(v)
                    continue
                if diff % (v - avx) == 0:
                    new.add(v)
            if potential_x is not None:
                potential_x &= new
            else:
                potential_x = new.copy()

        if avy == bvy:
            new = set()
            diff = bpy - apy
            for v in range(-1000, 1000):
                if v == avy:
                    new.add(v)
                    continue
                if diff % (v - avy) == 0:
                    new.add(v)
            if potential_y is not None:
                potential_y &= new
            else:
                potential_y = new.copy()

        if avz == bvz:
            new = set()
            diff = bpz - apz
            for v in range(-1000, 1000):
                if v == avz:
                    new.add(v)
                    continue
                if diff % (v - avz) == 0:
                    new.add(v)
            if potential_z is not None:
                potential_z &= new
            else:
                potential_z = new.copy()

    rvx = potential_x.pop()
    rvy = potential_y.pop()
    rvz = potential_z.pop()

    apx, apy, apz, avx, avy, avz = stones[0]
    bpx, bpy, bpz, bvx, bvy, bvz = stones[1]

    ma = (avy - rvy) / (avx - rvx)
    mb = (bvy - rvy) / (bvx - rvx)

    ca = apy - (ma * apx)
    cb = bpy - (mb * bpx)

    x = int((cb - ca) / (ma - mb))
    y = int(ma * x + ca)
    t = (x - apx) // (avx - rvx)
    z = apz + (avz - rvz) * t

    return x + y + z


assert task1('test_input.txt', 7, 27) == 2
print(task1('input.txt', 200000000000000, 400000000000000))

# doesn't work for test input
# assert task2('test_input.txt') == 47
print(task2('input.txt'))
