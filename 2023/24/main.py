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


assert task1('test_input.txt', 7, 27) == 2
print(task1('input.txt', 200000000000000, 400000000000000))
