from itertools import combinations
from functools import cache

def task1(fn):
    coords = []
    with open(fn) as fh:
        for line in fh:
            x, y = [int(i) for i in line.strip().split(',')]
            coords.append((x, y))

    max_a = 0
    for a, b in combinations(coords, 2):
        xa, ya = a
        xb, yb = b

        a = (1+abs(xa - xb)) * (1+abs(ya - yb))

        if a > max_a:
            max_a = a

    return max_a


def task2(fn):
    coords = []
    with open(fn) as fh:
        for line in fh:
            x, y = [int(i) for i in line.strip().split(',')]
            coords.append((x, y))

    @cache
    def is_inside(p):
        # ray casting algorithm
        # cast to the right and count the number of crossings
        x0, y0 = p

        crossings = 0
        for i in range(len(coords)):

            x1, y1 = coords[i]
            x2, y2 = coords[(i+1) % len(coords)]

            if (x0, y0) == (x1, y1):
                return True

            if (
                x1 == x2 == x0 and min(y1, y2) <= y0 <= max(y1, y2) or
                y1 == y2 == y0 and min(x1, x2) <= x0 <= max(x1, x2)
            ):
                return True

            if x1 == x2:
                if (
                    min(y1, y2) <= y0 and
                    max(y1, y2) >= y0 and
                    x0 < x1
                ):
                    crossings += 1
            elif y1 == y2:
                if y0 == y1 and x0 <= min(x1, x2):
                    crossings += 1
            else:
                raise ValueError(x1, y1, x2, y2)

        return (crossings % 2) == 1



    max_a = 0

    for a, b in combinations(coords, 2):
        xa, ya = a
        xb, yb = b

        points = []
        for yi in range(min(ya, yb), max(ya, yb)+1):
            points.append((min(xa, xb), yi))
            points.append((max(xa, xb), yi))
        for xi in range(min(xa, xb), max(xa, xb)+1):
            points.append((xi, min(ya, yb)))
            points.append((xi, max(ya, yb)))

        for xi, yi in points:
            if not is_inside((xi, yi)):
                break
        else:
            area = (1+abs(xa - xb)) * (1+abs(ya - yb))
            if area > max_a:
                max_a = area


    return max_a

assert task1('test_input.txt') == 50
print(task1('input.txt'))

assert task2('test_input.txt') == 24
print(task2('input.txt'))
